import sublime, sublime_plugin
import os, string
import re


try:
    from MarkdownWiki.wiki_page import *
except ImportError:
    from wiki_page import *


class OpenPageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        wiki_page = WikiPage(self.view)
        name = wiki_page.identify_page_at_cursor()
        wiki_page.select_page(name)
