import re
import sublime
import sublime_plugin


def view_is_markdown(view):
    try:
        return view.match_selector(view.sel()[0].begin(), "text.html.markdown")
    except IndexError:
        return False


def syntax_specific_settings_file(view):
    if isinstance(view, sublime.View):
        syntax = view.settings().get("syntax")
        if syntax:
            return re.sub(r".*/(.+)\.(sublime-syntax|tmLanguage)", r"\1.sublime-settings", syntax)
    return None


class MdeTextCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return view_is_markdown(self.view)

    def is_visible(self):
        return view_is_markdown(self.view)


class MdeReplaceSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            self.view.replace(edit, region, args['text'])


class MdeViewEventListener(sublime_plugin.ViewEventListener):

    @classmethod
    def is_applicable(cls, settings):
        try:
            return 'Markdown' in settings.get('syntax')
        except (AttributeError, TypeError):
            return False

    @classmethod
    def applies_to_primary_view_only(cls):
        return False


class MdeToggleCenteredLineCommand(MdeTextCommand):
    """
    The `mde_toggle_centered_line` command temporarily enables/disables line
    centering of the current view.

    To permanently enable or disable it, please tweak one of ST's user preferences files.

    - all markdown files: Preferences.sublime-settings
    - distraction free mode: Distraction Free.sublime-settings
    - syntax specific: [syntax name].sublime-settings
    - project specific: [Project].sublime-project

      ```json
      {
        // ...
        "settings": {
            "mde.keep_centered": true
        }
      }
      ```

    The setting is

    - enabled by default in `Distraction Free.sublime-settings`
    - disabled by default in `Preferences.sublime-settings`
    """

    def run(self, edit, **args):
        settings_file = syntax_specific_settings_file(self.view) or "Markdown.sublime-settings"
        syntax_settings = sublime.load_settings(settings_file)
        is_centered_by_syntax = syntax_settings.get('mde.keep_centered', False)

        settings = self.view.settings()
        want_centered = not settings.get('mde.keep_centered', False)
        if want_centered != is_centered_by_syntax:
            settings.set('mde.keep_centered', want_centered)
        else:
            settings.erase('mde.keep_centered')


class MdeCenteredLineKeeper(MdeViewEventListener):
    """
    This class keeps caret in vertical center position.
    These features can be enabled/disabled via settings files.
    """
    current_line = -1

    def on_modified(self):
        sel = self.view.sel()
        if sel and len(sel) != 1:
            return

        settings = self.view.settings()
        if not settings.get('mde.keep_centered', False):
            return

        pt = sel[0].begin()
        current_line, _ = self.view.rowcol(pt)
        if self.current_line != current_line:
            self.current_line = current_line
            self.view.show_at_center(pt)


class MdeUnsavedViewNameSetter(MdeViewEventListener):
    """
    This view event listener prints the first heading as tab title of unsaved documents.
    """

    HEADINGS_RE = re.compile(
        r"""
        ^( [ \t]* )                                   # leading whitespace
        (?:
          ( \#{1,6} ) [ \t]+ ( [^\n]+ )               # ATX headings
        | ( [^-#\s][^|\n]* ) \n \1 ( -{3,} | ={3,} )  # SETEXT headings
        ) [ \t]*$                                     # maybe trailing whitespace
        """,
        re.X | re.M
    )

    MAX_NAME = 50

    def first_heading(self):
        text = self.view.substr(sublime.Region(0, min(self.view.size(), 1024 * 1024)))
        for m in self.HEADINGS_RE.finditer(text):
            if m.group(3):
                title_begin = m.start(3)
                title_end = m.end(3)
            else:
                title_begin = m.start(4)
                title_end = m.end(4)
            # ignore front matter and raw code blocks
            if not self.view.match_selector(title_begin, "front-matter, markup.raw.block.markdown"):
                return text[title_begin:title_end]
        return text[0:text.find("\n")]

    def on_modified(self):
        if self.view.file_name() is not None:
            return

        name = self.first_heading()
        if len(name) > self.MAX_NAME:
            name = name[:self.MAX_NAME] + "…"
        self.view.set_name(name)
