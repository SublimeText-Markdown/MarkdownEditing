import sublime, sublime_plugin
import os, string
import re

try:
    from MarkdownEditing.wiki_page import *
except ImportError:
    from wiki_page import *



class OpenHomePageCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		home_page = self.view.settings().get("mde.wikilinks.homepage", DEFAULT_HOME_PAGE)

		wiki_page = WikiPage(self.view)
		wiki_page.select_page(home_page)
