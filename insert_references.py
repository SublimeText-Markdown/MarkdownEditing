# -*- coding: UTF-8 -*-

import sublime
import sublime_plugin
import re


def get_clipboard_if_url():
    # If the clipboard contains an URL, return it
    # Otherwise, return an empty string
    re_match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)
    m = re_match_urls.search(sublime.get_clipboard())
    return m.group() if m else ''


def mangle_url(url):
    url = url.strip()
    if re.match(r'^([a-z0-9-]+\.)+\w{2,4}', url, re.IGNORECASE):
        url = 'http://' + url
    return url


def check_for_link(view, url):
    titles = []
    # Check if URL is already present as reference link
    view.find_all(r'^\s{0,3}\[([^^\]]+)\]:[ \t]+' + re.escape(url) + '$', 0, '$1', titles)
    return titles[0] if titles else None


def append_reference_link(edit, view, title, url):
    # Detect if file ends with \n
    if view.substr(view.size() - 1) == '\n':
        nl = ''
    else:
        nl = '\n'
    # Append the new reference link to the end of the file
    view.insert(edit, view.size(), '{0}[{1}]: {2}\n'.format(nl, title, url))


def insert_references(edit, view, title):
    # Add a reference with given title at the current cursor or around the current selection(s)
    sels = view.sel()
    caret = []

    for sel in sels:
        text = view.substr(sel)
        # If something is selected...
        if len(text) > 0:
            # ... turn the selected text into the link text
            view.replace(edit, sel, "[{0}][{1}]".format(text, title))
        else:
            # Add the link, with empty link text, and the caret positioned
            # ready to type the link text
            view.replace(edit, sel, "[][{0}]".format(title))
            caret += [sublime.Region(sel.begin() + 1, sel.begin() + 1)]

    if len(caret) > 0:
        sels.clear()
        for c in caret:
            sels.add(c)


# Inspired by http://www.leancrew.com/all-this/2012/08/markdown-reference-links-in-bbedit/
# Appends a new reference link to end of document, using a user-input name and URL.
# Then inserts a reference to the link at the current selection(s).

class InsertNamedReferenceCommand(sublime_plugin.TextCommand):

    def description(self):
        return 'Insert Numbered Reference Link'

    def run(self, edit):
        self.view.window().show_input_panel(
            'URL to link to:',
            get_clipboard_if_url(),
            self.receive_link,
            None, None)

    def receive_link(self, linkurl):
        linkurl = mangle_url(linkurl)

        newref = check_for_link(self.view, linkurl)
        if newref:
            # Link already exists, reuse existing reference
            self.insert_link(linkurl, newref, False)

        else:
            self.view.window().show_input_panel(
                'Name for reference:', '',
                lambda newref: self.insert_link(linkurl, newref),
                None, None)

    def insert_link(self, linkurl, newref, actually_insert=True):
        # Check if title is already present as reference
        if actually_insert and self.view.find(r'^\s{0,3}\[' + re.escape(newref) + '\]:[ \t]+', 0):
            sublime.error_message('A reference named "' + newref + '" already exists.')
            self.view.window().show_input_panel(
                'Name for reference:', '',
                lambda newref: self.insert_link(linkurl, newref),
                None, None)
            return

        edit = self.view.begin_edit()

        try:
            if actually_insert:
                append_reference_link(edit, self.view, newref, linkurl)

            insert_references(edit, self.view, newref)

        finally:
            self.view.end_edit(edit)

    def is_enabled(self):
        return True


# Inspired by http://www.leancrew.com/all-this/2012/08/markdown-reference-links-in-bbedit/
# Appends a new reference link to end of document, using an autoincrementing number as the reference title.
# Then inserts a reference to the link at the current selection(s).

class InsertNumberedReferenceCommand(sublime_plugin.TextCommand):

    def description(self):
        return 'Insert Numbered Reference Link'

    def run(self, edit):
        self.view.window().show_input_panel(
            'URL to link to:',
            get_clipboard_if_url(),
            self.insert_link,
            None, None)

    def insert_link(self, linkurl):
        edit = self.view.begin_edit()

        try:
            linkurl = mangle_url(linkurl)
            newref = check_for_link(self.view, linkurl)
            if not newref:
                # Find the next reference number
                reflinks = self.view.find_all(r'(?<=^\[)(\d+)(?=\]: )')
                if len(reflinks) == 0:
                    newref = 1
                else:
                    newref = max(int(self.view.substr(reg)) for reg in reflinks) + 1

                append_reference_link(edit, self.view, newref, linkurl)

            insert_references(edit, self.view, newref)

        finally:
            self.view.end_edit(edit)

    def is_enabled(self):
        return True
