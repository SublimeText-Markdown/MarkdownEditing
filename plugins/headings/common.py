import re
import unicodedata

import sublime

from ..decorators import debounced
from ..view import MdeViewEventListener

HEADINGS_RE = re.compile(
    r"""
    ^( [ \t]* )                                   # leading whitespace
    (?:
      ( \#{1,6} ) [ \t]+ ( [^\n]+ )               # ATX headings
    | ( [^-=#\s][^|\n]* ) \n \1 ( -{3,} | ={3,} ) # SETEXT headings
    ) [ \t]*$                                     # maybe trailing whitespace
    """,
    re.X | re.M,
)


def all_headings(view, start=0, end=None):
    if end is None:
        end = view.size()
    text = view.substr(sublime.Region(start, end))
    for m in HEADINGS_RE.finditer(text):
        title_begin = start + m.start()
        title_end = start + m.end()
        if m.group(2):
            # ATX headings use group 2 (heading) and 3 (leading hashes)
            level = m.end(2) - m.start(2)
        else:
            # SETEXT headings use group 4 (text) and 5 (underlines)
            level = 2 if text[m.start(5)] == "-" else 1
        # ignore front matter and raw code blocks
        if view.match_selector(title_begin, "- markup.raw"):
            yield (title_begin, title_end, level)
    return None


def first_heading_text(view):
    text = view.substr(sublime.Region(0, min(view.size(), 1024 * 1024)))
    for m in HEADINGS_RE.finditer(text):
        if m.group(3):
            title_begin = m.start(3)
            title_end = m.end(3)
        else:
            title_begin = m.start(4)
            title_end = m.end(4)
        # ignore front matter and raw code blocks
        if view.match_selector(title_begin, "- markup.raw"):
            return text[title_begin:title_end]
    return text[0 : text.find("\n")]


class MdeUnsavedViewNameSetter(MdeViewEventListener):
    """
    This view event listener prints the first heading as tab title of unsaved documents.
    """

    @debounced(50, sync=True)
    def on_modified(self):
        if self.view.file_name() or self.view.is_loading():
            return

        view_settings = self.view.settings()
        if not view_settings.get("set_unsaved_view_name", True):
            return

        cur_name = view_settings.get("mde_auto_name")
        view_name = self.view.name()

        # Name has been explicitly set, don't override it
        if not cur_name and view_name:
            return

        # Name has been explicitly changed, don't override it
        if cur_name and cur_name != view_name:
            view_settings.erase("mde_auto_name")
            return

        # Don't set the names on widgets, it'll just trigger spurious
        # on_modified callbacks
        if view_settings.get("is_widget"):
            return

        name = first_heading_text(self.view)
        if len(name) > 50:
            name = name[:50] + "…"

        # Filter non-printable characters. Without this the save dialog on
        # windows fails to open.
        first_line = "".join(c for c in name if unicodedata.category(c)[0] != "C")

        self.view.set_name(name)
        view_settings.set("mde_auto_name", name)

        # make sure ST's default auto-namer keeps quite
        view_settings.erase("auto_name")
