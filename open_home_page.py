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


class OpenHomePageCommand(MDETextCommand):
    def run(self, edit):
        print("Running OpenHomePageCommand")
        home_page = self.view.settings().get("mde.wikilinks.homepage", DEFAULT_HOME_PAGE)

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(home_page)
