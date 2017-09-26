import sublime, sublime_plugin
import os, string
import re

from datetime import date

try:
    from MarkdownEditing.open_page import *
except ImportError:
    from open_page import *

class OpenJournal(OpenPage):
    def run(self, edit):
        today = date.today()
        page = today.strftime('%Y-%m-%d')

        print("Open journal: %s" % (page))
        self.select_page(page)
