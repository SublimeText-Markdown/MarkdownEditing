import os
import re
import string
import sys

import sublime

from datetime import date

from .logging import logger
from .view import MdeTextCommand

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
DEFAULT_HOME_PAGE = "HomePage"
DEFAULT_MARKDOWN_EXTENSION = ".md"
PAGE_REF_FORMAT = "[[%s]]"


class MdeListBackLinksCommand(MdeTextCommand):
    def run(self, edit):
        wiki_page = WikiPage(self.view)

        file_list = wiki_page.find_files_with_ref()
        wiki_page.select_backlink(file_list)


class MdeMakePageReferenceCommand(MdeTextCommand):
    def is_visible(self):
        """Return True if  is on a wiki page reference."""
        if not super().is_visible():
            return False
        for sel in self.view.sel():
            if self.view.match_selector(sel.begin(), "meta.link.reference.wiki"):
                return False
        return True

    def run(self, edit):
        wiki_page = WikiPage(self.view)

        word_region = wiki_page.select_word_at_cursor()
        file_list = wiki_page.find_matching_files(word_region)

        wiki_page.make_page_reference(edit, word_region)

        if len(file_list) > 1:
            wiki_page.show_quick_list(file_list)


class MdeOpenHomePageCommand(MdeTextCommand):
    def run(self, edit):
        home_page = self.view.settings().get("mde.wikilinks.homepage", DEFAULT_HOME_PAGE)

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(home_page)


class MdeOpenJournalCommand(MdeTextCommand):
    def run(self, edit):
        today = date.today()
        date_format = self.view.settings().get("mde.journal.dateformat", DEFAULT_DATE_FORMAT)
        name = today.strftime(date_format)

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(name)


class MdeOpenPageCommand(MdeTextCommand):
    def is_visible(self):
        """Return True if caret is on a wiki page reference."""
        for sel in self.view.sel():
            if self.view.match_selector(sel.begin(), "meta.link.reference.wiki"):
                return True
        return False

    def run(self, edit):
        wiki_page = WikiPage(self.view)

        sel_region = self.get_selected()
        if sel_region:
            wiki_page.select_word_at_cursor()

            region = sublime.Region(sel_region.begin(), sel_region.begin())
            file_list = wiki_page.find_matching_files(region)

            if len(file_list) > 1:
                wiki_page.show_quick_list(file_list)
        else:
            name = wiki_page.identify_page_at_cursor()
            wiki_page.select_page(name)

    def get_selected(self):
        selection = self.view.sel()
        for region in selection:
            return region

        return None


class MdePrepareFromTemplateCommand(MdeTextCommand):

    DEFAULT_PAGE_TEMPLATE = "templates/PageTemplate.md"
    PRESET_TEMPLATE_TEXT = "# $title\n\n"

    def run(self, edit, **args):
        """Prepare a new page content from a named template.

        :Example:

        view.run_command('mde_prepare_from_template', {
            'title': pagename,
            'template': 'default_page'
        })

        :param self: This command instance
        :param edit: The sublime edit instance
        :param args: The command arguments including 'title' and 'template'
        """

        template_name = args["template"]
        logger.info("Creating new page from template: ", template_name)

        text = self.generate_from_template(template_name, args)
        self.view.insert(edit, 0, text)

    def generate_from_template(self, template_name, args):
        """Generate the text using the template"""

        template_text = self.retrieve_template_text(template_name)
        template = string.Template(template_text)
        return template.substitute(args)

    def retrieve_template_text(self, template_name):
        """Retrieve the template text.

        The setting 'mde.wikilinks.templates' may be configured with a filename for
        the template.  This file (if it exists) will be loaded otherwise the preset
        template will be used
        """

        template = self.view.settings().get("mde.wikilinks.templates", self.DEFAULT_PAGE_TEMPLATE)

        if not os.path.isfile(template):
            current_file = self.view.file_name()
            current_dir = os.path.dirname(current_file)
            template = os.path.join(current_dir, template)

        if os.path.isfile(template):
            logger.debug("Using template:", template)
            try:
                with open(template, "rt") as f:
                    return f.read()
            except OSError:
                logger.debug("Unable to read template:", sys.exc_info()[0])

        # Unable to load template  so using preset template
        logger.warning("Template:", template, "not found. Using preset.")
        return self.PRESET_TEMPLATE_TEXT


class WikiPage:
    def __init__(self, view):
        self.view = view

    def identify_page_at_cursor(self):
        for region in self.view.sel():
            text_on_cursor = None

            pos = region.begin()
            scope_region = self.view.extract_scope(pos)
            if not scope_region.empty():
                text_on_cursor = self.view.substr(scope_region)
                return text_on_cursor.strip(string.punctuation)

        return None

    def select_page(self, pagename):
        logger.debug("Open page: %s" % (pagename))
        if not pagename:
            return

        self.file_list = self.find_files_with_name(pagename)
        if len(self.file_list) > 1:
            self.view.window().show_quick_panel(self.file_list, self.open_selected_file)
        elif len(self.file_list) == 1:
            self.open_selected_file(0)
        else:
            self.open_new_file(pagename)

    def find_files_with_name(self, pagename):
        pagename = pagename.replace("\\", os.sep).replace(os.sep + os.sep, os.sep).strip()

        self.current_file = self.view.file_name()
        self.current_dir = os.path.dirname(self.current_file)
        logger.debug("Locating page '%s' in: %s" % (pagename, self.current_dir))

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        # Optionally strip extension...
        if pagename.endswith(markdown_extension):
            search_pattern = "^%s$" % pagename
        else:
            search_pattern = "^%s%s$" % (pagename, markdown_extension)

        # Scan directory tree for files that match the pagename...
        results = []
        for dirname, _, files in self.list_dir_tree(self.current_dir):
            for file in files:
                if re.search(search_pattern, file):
                    filename = os.path.join(dirname, file)
                    results.append([self.extract_page_name(filename), filename])

        return results

    def find_files_with_ref(self):
        self.current_file = self.view.file_name()
        self.current_dir, current_base = os.path.split(self.current_file)
        self.current_name, _ = os.path.splitext(current_base)

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        results = []
        for dirname, _, files in self.list_dir_tree(self.current_dir):
            for file in files:
                page_name, extension = os.path.splitext(file)
                filename = os.path.join(dirname, file)
                if extension == markdown_extension and self.contains_ref(
                    filename, self.current_name
                ):
                    results.append([page_name, filename])

        return results

    def contains_ref(self, filename, page_name):
        link_text = PAGE_REF_FORMAT % page_name

        try:
            return bool(link_text in open(filename).read())
        except UnicodeDecodeError:
            return bool(link_text in open(filename, encoding="utf-8").read())
        except OSError:
            pass

        return False

    def select_backlink(self, file_list):
        if file_list:
            self.file_list = file_list
            self.view.window().show_quick_panel(self.file_list, self.open_selected_file)
        else:
            msg = "No pages reference this page"
            logger.error(msg)
            self.view.window().status_message(msg)

    def open_new_file(self, pagename):
        current_syntax = self.view.settings().get("syntax")
        current_file = self.view.file_name()
        current_dir = os.path.dirname(current_file)

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        filename = os.path.join(current_dir, pagename + markdown_extension)

        new_view = self.view.window().new_file()
        new_view.retarget(filename)
        new_view.run_command(
            "mde_prepare_from_template", {"title": pagename, "template": "default_page"}
        )
        logger.debug("Current syntax: %s", current_syntax)
        new_view.set_syntax_file(current_syntax)

        # Create but don't save page
        # new_view.run_command('save')

    def open_selected_file(self, selected_index):
        if selected_index != -1:
            _, file = self.file_list[selected_index]

            logger.debug("Opening file '%s'", file)
            self.view.window().open_file(file)

    def extract_page_name(self, filename):
        _, base_name = os.path.split(filename)
        page_name, _ = os.path.splitext(base_name)

        return page_name

    def list_dir_tree(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files

    def select_word_at_cursor(self):
        word_region = None

        selection = self.view.sel()
        for region in selection:
            word_region = self.view.word(region)
            if not word_region.empty():
                selection.clear()
                selection.add(word_region)
                return word_region

        return word_region

    def show_quick_list(self, file_list):
        self.file_list = file_list

        window = self.view.window()
        window.show_quick_panel(file_list, self.replace_selection_with_pagename)

    def replace_selection_with_pagename(self, selected_index):
        if selected_index != -1:
            page_name, file = self.file_list[selected_index]

            logger.debug("Using selected page '%s'", page_name)
            self.view.run_command("mde_replace_selected", {"text": page_name})

    def find_matching_files(self, word_region):
        word = None if word_region.empty() else self.view.substr(word_region)

        current_file = self.view.file_name()
        current_dir, current_base = os.path.split(current_file)
        logger.debug("Finding matching files for %s in %s", word, current_dir)

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        # Optionally strip extension...
        if word is not None and word.endswith(markdown_extension):
            word = word[: -len(markdown_extension)]

        # Scan directory tree for potential filenames that contain the word...
        results = []
        for dirname, _, files in self.list_dir_tree(current_dir):
            for file in files:
                page_name, extension = os.path.splitext(file)
                filename = os.path.join(dirname, file)

                if extension == markdown_extension and (not word or word in page_name):
                    results.append([page_name, filename])

        return results

    def make_page_reference(self, edit, region):
        logger.debug("Make page reference %s", region)

        begin = region.begin()
        end = region.end()

        self.view.insert(edit, end, "]]")
        self.view.insert(edit, begin, "[[")

        if region.empty():
            selection = self.view.sel()
            selection.clear()
            selection.add(sublime.Region(begin + 2, end + 2))
