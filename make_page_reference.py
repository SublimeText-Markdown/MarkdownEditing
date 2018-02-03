import sublime, sublime_plugin
import os, string

try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


class MakePageReferenceCommand(MDETextCommand):
    def is_visible(self):
        """Return True if cursor is on a wiki page reference."""
        for sel in self.view.sel():
            scopes = self.view.scope_name(sel.b).split(" ")
            if 'meta.link.wiki.markdown' in scopes:
                return False                

        return True

    def run(self, edit):
        print("Running MakePageReferenceCommand")        
        wiki_page = WikiPage(self.view)

        word_region = wiki_page.select_word_at_cursor()
        file_list = wiki_page.find_matching_files(word_region)

        wiki_page.make_page_reference(edit, word_region)

        if len(file_list) > 1:
            wiki_page.show_quick_list(file_list)
