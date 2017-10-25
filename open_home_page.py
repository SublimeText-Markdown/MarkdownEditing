import sublime, sublime_plugin
import os, string
import re

try:
    from MarkdownWiki.wiki_page import *
except ImportError:
    from wiki_page import *



class OpenHomePageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		wiki_page = WikiPage(self.view)
		wiki_page.select_page(HOME_PAGE)
