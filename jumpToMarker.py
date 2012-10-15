# Author: Gabriel Weatherhead
# Contact: gabe@macdrifter.com

import sublime, sublime_plugin, re

class GotoReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.linkRef = []
        self.view.find_all("(^\s{0,3}\\[.*?\\]:) (.*)", 0, "$1 $2", self.linkRef)
        self.view.window().show_quick_panel(self.linkRef, self.jump_to_link, sublime.MONOSPACE_FONT)

    def jump_to_link(self, choice):
        if choice == -1:
            return
        # Set a bookmark so we can easily jump back
        self.view.run_command('toggle_bookmark')
        findmarker = self.linkRef[choice].split(':', 1)[1].strip()
        if len(findmarker) == 0:
            findmarker = self.linkRef[choice].split(':', 1)[0].strip()
        self.view.sel().clear()
        # Get the selection
        pt = self.view.find(re.escape(findmarker+':'), 0)
        self.view.sel().add(pt)
