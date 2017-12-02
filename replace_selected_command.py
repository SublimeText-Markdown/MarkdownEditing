import sublime, sublime_plugin
import os, string

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *

class ReplaceSelectedCommand(MDETextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            self.view.replace(edit, region, args['text'])
