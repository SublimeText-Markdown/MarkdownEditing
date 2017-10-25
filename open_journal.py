import sublime, sublime_plugin
import os, string
import re

from datetime import date

try:
    from MarkdownWiki.wiki_page import *
except ImportError:
    from wiki_page import *

class OpenJournalCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        today = date.today()
        name = today.strftime('%Y-%m-%d')

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(name)
