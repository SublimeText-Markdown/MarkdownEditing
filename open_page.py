
import sublime, sublime_plugin
import os, string
import re


try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


class OpenPageCommand(MDETextCommand):
    def is_visible(self):
        """Return True if cursor is on a wiki page reference."""
        for sel in self.view.sel():
            scopes = self.view.scope_name(sel.b).split(" ")
            if 'meta.link.wiki.markdown' in scopes:
                return True                

        return False

    def run(self, edit):
        print("Running OpenPageCommand")        
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

