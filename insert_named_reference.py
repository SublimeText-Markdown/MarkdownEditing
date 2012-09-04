# -*- coding: UTF-8 -*-

import sublime
import sublime_plugin
import re


# Inspired by http://www.leancrew.com/all-this/2012/08/markdown-reference-links-in-bbedit/
# Appends a new reference link to end of document, using a user-input name and URL.
# Then inserts a reference to the link at the current selection(s).

class InsertNamedReferenceCommand(sublime_plugin.TextCommand):

    def description(self):
        return 'Insert Numbered Reference Link'

    def run(self, edit):

        # If the clipboard contains an URL, use it as the default value in the input panel
        # Otherwise, leave it empty
        re_match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)
        m = re_match_urls.search(sublime.get_clipboard())
        s = m.group() if m else ''

        self.view.window().show_input_panel(
            'URL to link to:',
            s,
            self.receive_link,
            None, None)

    def receive_link(self, linkurl):
        self.view.window().show_input_panel(
            'Name for reference:',
            '',
            lambda newref: self.insert_link(linkurl, newref),
            None, None)

    def insert_link(self, linkurl, newref):
        view = self.view
        edit = view.begin_edit()

        try:
            # Detect if file ends with \n
            if view.substr(view.size() - 1) == '\n':
                nl = ''
            else:
                nl = '\n'

            # Append the new reference link to the end of the file
            view.insert(edit, view.size(), '{0}[{1}]: {2}\n'.format(nl, newref, linkurl))

            # Now, add a reference to that link at the current cursor or around the current selection(s)
            sels = view.sel()
            caret = []

            for sel in sels:
                text = view.substr(sel)
                # If something is selected...
                if len(text) > 0:
                    # ... turn the selected text into the link text
                    view.replace(edit, sel, "[{0}][{1}]".format(text, newref))
                else:
                    # Add the link, with empty link text, and the caret positioned
                    # ready to type the link text
                    view.replace(edit, sel, "[][{0}]".format(newref))
                    caret += [sublime.Region(sel.begin() + 1, sel.begin() + 1)]

            if len(caret) > 0:
                sels.clear()
                for c in caret:
                    sels.add(c)

        finally:
            view.end_edit(edit)

    def is_enabled(self):
        return self.view.sel()
