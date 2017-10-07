import sublime, sublime_plugin
import os, string
import re

try:
    from MarkdownWiki.open_page import *
except ImportError:
    from open_page import *


HOME_PAGE = "HomePage"


class OpenHomePageCommand(OpenPageCommand):
    def run(self, edit):
        page = HOME_PAGE

        print("Open Home Page: %s" % (page))
        self.select_page(page)
