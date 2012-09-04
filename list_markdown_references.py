import sublime, sublime_plugin
import re


# Based on http://www.macdrifter.com/2012/08/making-a-sublime-text-plugin-markdown-reference-viewer.html
# and http://www.leancrew.com/all-this/2012/08/more-markdown-reference-links-in-bbedit/
# Displays a list of reference links in the document, and
# inserts a reference to the chosen item at the current selection.

class ListMarkdownReferencesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.markers = []
        self.view.find_all(r'^\s{0,3}(\[[^^\]]+\]):[ \t]+(.+)$', 0, '$1: $2', self.markers)
        self.view.window().show_quick_panel(self.markers, self.insert_link, sublime.MONOSPACE_FONT)

    def insert_link(self, choice):
        if choice == -1:
            return
        edit = self.view.begin_edit()

        try:
            # Extract the reference name that was selected
            ref = re.match(r'^\[([^^\]]+)\]', self.markers[choice]).group(1)

            # Now, add a reference to that link at the current cursor or around the current selection(s)
            sels = self.view.sel()
            caret = []

            for sel in sels:
                text = self.view.substr(sel)
                # If something is selected...
                if len(text) > 0:
                    # ... turn the selected text into the link text
                    self.view.replace(edit, sel, "[{0}][{1}]".format(text, ref))
                else:
                    # Add the link, with empty link text, and the caret positioned
                    # ready to type the link text
                    self.view.replace(edit, sel, "[][{0}]".format(ref))
                    caret += [sublime.Region(sel.begin() + 1, sel.begin() + 1)]

            if len(caret) > 0:
                sels.clear()
                for c in caret:
                    sels.add(c)

        finally:
            self.view.end_edit(edit)
