"""
	Re-implements `find_under_expand` command because ST refuses to use it inside macro
	definitions.

	Source: http://www.sublimetext.com/forum/viewtopic.php?f=3&t=5148
"""

import sublime, sublime_plugin


class CustomFindUnderExpandCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = []

        for s in self.view.sel():
            word = self.view.word(sublime.Region(s.begin(), s.end()))
            regions.append(word)

        for r in regions:
            self.view.sel().add(r)
