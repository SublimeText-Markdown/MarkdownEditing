import sublime
import sublime_plugin
import re

def append_reference_link(edit, view, title, url):
    # Detect if file ends with \n
    if view.substr(view.size() - 1) == '\n':
        nl = ''
    else:
        nl = '\n'
    # Append the new reference link to the end of the file
    edit_position = view.size() + len(nl) + 1
    view.insert(edit, view.size(), '{0}[{1}]: {2}\n'.format(nl, title, url))
    return sublime.Region(edit_position, edit_position + len(title))

def suggest_default_link_name(title):
    # Camel case impl.
    ret = ''
    for word in title.split():
      ret += word.capitalize()
      if len(ret) > 30:
        break
    return 'link' + ret

def is_url(contents):
    # If the clipboard contains an URL, return it
    # Otherwise, return an empty string
    re_match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)
    m = re_match_urls.search(contents)
    return True if m else False

class PasteAsReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        edit_regions = []
        suggested_title = False
        contents = sublime.get_clipboard()
        for sel in view.sel():
            text = view.substr(sel)
            if not suggested_title:
                if is_url(contents):
                    suggested_title = suggest_default_link_name(text)
                    link = contents
                else:
                    suggested_title = suggest_default_link_name(contents)
                    link = ''

            edit_position = sel.end() + 3
            self.view.replace(edit, sel, "[" + text + "][" + suggested_title + "]")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(suggested_title)))
        if len(edit_regions) > 0:
            selection = view.sel()
            selection.clear()
            reference_region = append_reference_link(edit, view, suggested_title, link)
            selection.add(reference_region)
            selection.add_all(edit_regions)

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class PasteAsInlineLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        edit_regions = []
        suggested_title = False
        contents = sublime.get_clipboard()
        for sel in view.sel():
            text = view.substr(sel)
            edit_position = sel.end() + 3
            self.view.replace(edit, sel, "[" + text + "](" + contents + ")")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(contents)))
        if len(edit_regions) > 0:
            selection.clear()
            selection.add_all(edit_regions)
