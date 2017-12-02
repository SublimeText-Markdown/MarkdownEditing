import sublime, sublime_plugin
import os, string
import re

from datetime import date

try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


class OpenJournalCommand(MDETextCommand):
    def run(self, edit):
        print("Running OpenJournalCommand")        
        today = date.today()
        name = today.strftime('%Y-%m-%d')

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(name)
