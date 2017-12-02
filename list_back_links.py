import sublime, sublime_plugin
import os, string

try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *


class ListBackLinksCommand(MDETextCommand):
    def description(self):
        return "List wiki pages that reference this page"

    def is_visible(self):
        return True

    def run(self, edit):
        wiki_page = WikiPage(self.view)

        file_list = wiki_page.find_files_with_ref()
        wiki_page.select_backlink(file_list)

