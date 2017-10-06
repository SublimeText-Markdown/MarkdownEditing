import sublime, sublime_plugin
import os, string
import re

try:
    from MarkdownWiki.open_page import *
except ImportError:
    from open_page import *

class OpenHomePage(OpenPage):
    def run(self, edit):
        page = "HomePage"

        print("Open Home: %s" % (page))
        self.select_page(page)
