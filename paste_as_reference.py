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

def suggest_default_link_name(title, image):
    # Camel case impl.
    ret = ''
    title_segs = title.split()
    if len(title_segs) > 1:
        for word in title_segs:
          ret += word.capitalize()
          if len(ret) > 30:
            break
        return ('image' if image else 'link') + ret
    else:
        return title

def is_url(contents):
    # If the clipboard contains an URL, return it
    # Otherwise, return an empty string
    re_match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)
    m = re_match_urls.search(contents)
    return True if m else False

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

class PasteAsReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit, image = False):
        view = self.view
        edit_regions = []
        contents = sublime.get_clipboard().strip()
        link = mangle_url(contents) if is_url(contents) else ""
        if len(link) > 0:
            # If link already exists, reuse existing reference
            suggested_link_name = suggested_title = check_for_link(view, link)
        for sel in view.sel():
            text = view.substr(sel)
            if not suggested_title:
                suggested_link_name = suggest_default_link_name(text, image)
                suggested_title = suggested_link_name if suggested_link_name != text else ""
            edit_position = sel.end() + 3
            if image:
                edit_position += 1
                self.view.replace(edit, sel, "![" + text + "][" + suggested_title + "]")
            else:
                self.view.replace(edit, sel, "[" + text + "][" + suggested_title + "]")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(suggested_title)))
        if len(edit_regions) > 0:
            selection = view.sel()
            selection.clear()
            reference_region = append_reference_link(edit, view, suggested_link_name, link)
            selection.add(reference_region)
            selection.add_all(edit_regions)

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class PasteAsInlineLinkCommand(sublime_plugin.TextCommand):
    def run(self, edit, image = False):
        view = self.view
        edit_regions = []
        suggested_title = False
        contents = sublime.get_clipboard().strip()
        link = mangle_url(contents) if is_url(contents) else ""
        for sel in view.sel():
            text = view.substr(sel)
            edit_position = sel.end() + 3
            if image:
                edit_position += 1
                self.view.replace(edit, sel, "![" + text + "](" + link + ")")
            else:
                self.view.replace(edit, sel, "[" + text + "](" + link + ")")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(link)))
        if len(edit_regions) > 0:
            selection.clear()
            selection.add_all(edit_regions)

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class PasteAsInlineImage(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("paste_as_inline_link", {"image": True})

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class PasteAsImage(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("paste_as_reference", {"image": True})

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))