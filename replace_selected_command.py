import sublime, sublime_plugin
import os, string

class ReplaceSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            self.view.replace(edit, region, args['text'])
