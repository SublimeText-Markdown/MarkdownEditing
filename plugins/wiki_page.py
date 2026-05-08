import os
import re
import string
import sys

import sublime

from datetime import datetime

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
        date_format = self.view.settings().get("mde.journal.dateformat", DEFAULT_DATE_FORMAT)
        name = datetime.now().strftime(date_format)

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

    def project_folders(self):
        window = self.view.window()
        if window and window.folders():
            return window.folders()

        filename = self.view.file_name()
        if filename:
            return [os.path.dirname(filename)]

        return []

    def find_files_with_name(self, pagename):
        pagename = pagename.replace("\\", os.sep).replace(os.sep + os.sep, os.sep).strip()

        search_dirs = self.project_folders()
        if not search_dirs:
            return []

        sublime.status_message("Locating page '{}' in: {}".format(pagename, search_dirs))
        logger.debug("Locating page '%s' in: %s" % (pagename, search_dirs))

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        # Optionally strip extension...
        if pagename.endswith(markdown_extension):
            search_pattern = "^%s$" % pagename
        else:
            search_pattern = "^%s%s$" % (pagename, markdown_extension)

        # Scan project directory trees for files that match the pagename...
        results = []
        for search_dir in search_dirs:
            for dirname, _, files in self.list_dir_tree(search_dir):
                for file in files:
                    if re.search(search_pattern, file):
                        filename = os.path.join(dirname, file)
                        results.append([self.extract_page_name(filename), filename])

        return results

    def find_files_with_ref(self):
        current_file = self.view.file_name()
        if not current_file:
            return []
        _, current_base = os.path.split(current_file)
        search_dirs = self.project_folders()
        sublime.status_message("Showing backlinks from: {}".format(search_dirs))
        current_name, _ = os.path.splitext(current_base)

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        results = []
        for search_dir in search_dirs:
            for dirname, _, files in self.list_dir_tree(search_dir):
                for file in files:
                    page_name, extension = os.path.splitext(file)
                    filename = os.path.join(dirname, file)
                    if extension == markdown_extension and self.contains_ref(
                        filename, current_name
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
        search_dirs = self.project_folders()
        if not search_dirs:
            return

        # Prefer current file location
        filename = self.view.file_name()
        if filename:
            current_dir = os.path.dirname(filename)
        else:
            # Fallback to first project folder
            current_dir = search_dirs[0]

        sublime.status_message("New page location: {}".format(current_dir))

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
        sels = self.view.sel()
        if not sels:
            return None

        # return non-empty selection
        sel = sels[0]
        if not sel.empty():
            return sel

        # return empty selection if surrounded by whitespace
        reg = sublime.Region(sel.begin() - 1, sel.end())
        if all(c in " \t\n" for c in self.view.substr(reg)):
            return sel

        # expand selection to word boundaries
        reg = self.view.expand_by_class(
            sel, classes=sublime.CLASS_WORD_START | sublime.CLASS_WORD_END, separators=" \t\n?*"
        )
        if not reg.empty():
            sels.clear()
            sels.add(reg)
            return reg

        return sel

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

        search_dirs = self.project_folders()
        sublime.status_message("Finding matching files for {} in {}".format(word, search_dirs))
        logger.debug("Finding matching files for %s in %s", word, search_dirs)

        markdown_extension = self.view.settings().get(
            "mde.wikilinks.markdown_extension", DEFAULT_MARKDOWN_EXTENSION
        )

        # Optionally strip extension...
        if word is not None and word.endswith(markdown_extension):
            word = word[: -len(markdown_extension)]

        # Scan project directory trees for potential filenames that contain the word...
        results = []
        for search_dir in search_dirs:
            for dirname, _, files in self.list_dir_tree(search_dir):
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
