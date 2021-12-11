import re

import sublime

from .view import MdeTextCommand, syntax_specific_settings_file


class MdeSelectColorSchemeCommand(MdeTextCommand):
    def run(self, edit):
        select_color_scheme(self.view)


def select_color_scheme(view=None):
    syntax_settings = syntax_specific_settings_file(view) or "Markdown.sublime-settings"

    window = view.window() if isinstance(view, sublime.View) else sublime.active_window()
    pre_view = window.new_file(
        flags=sublime.TRANSIENT, syntax="Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"
    )
    pre_view.set_scratch(True)
    pre_view.run_command(
        "append",
        {
            "characters": sublime.load_resource(
                "Packages/MarkdownEditing/schemes/Preview.md"
            ).replace("\r\n", "\n")
        },
    )
    pre_view.set_read_only(True)

    md_settings = sublime.load_settings(syntax_settings)
    md_scheme = md_settings.get("color_scheme")

    global_settings = sublime.load_settings("Preferences.sublime-settings")
    global_scheme = global_settings.get("color_scheme")
    schemes = [global_scheme, "MarkdownEditor.sublime-color-scheme"]
    for scheme in sublime.find_resources("MarkdownEditor*.sublime-color-scheme"):
        if scheme not in schemes:
            schemes.append(scheme)
    for scheme in sublime.find_resources("MarkdownEditor*.tmTheme"):
        if scheme not in schemes:
            schemes.append(scheme)

    schemes_display = []
    selected_index = 0
    for i, s in enumerate(schemes):
        if s == "auto":
            theme_display = "Auto"
        else:
            m = re.search(r"[^/]+(?=\.(sublime-color-scheme|tmTheme)$)", s)
            theme_display = m.group(0)
        if s == global_scheme:
            theme_display += " (Global)"
            if not md_scheme:
                theme_display += " (Current)"
                selected_index = i
        if s == md_scheme:
            theme_display += " (Current)"
            selected_index = i
        schemes_display.append(theme_display)

    def set_scheme(scheme):
        if scheme:
            if scheme.endswith(".sublime-color-scheme"):
                scheme = scheme.split("/")[-1]
            md_settings.set("color_scheme", scheme)
        else:
            md_settings.erase("color_scheme")

    def on_done(index):
        if index == -1:
            # restore previous color scheme
            set_scheme(md_scheme)
        elif index == 0:
            # use global color scheme
            set_scheme(None)
        else:
            # use markdown color scheme
            set_scheme(schemes[index])
        sublime.save_settings(syntax_settings)
        pre_view.close()

    def on_highlighted(index):
        scheme = schemes[index]
        if scheme.endswith(".sublime-color-scheme"):
            scheme = scheme.split("/")[-1]
        pre_view.settings().set("color_scheme", scheme)

    window.show_quick_panel(
        schemes_display,
        flags=sublime.KEEP_OPEN_ON_FOCUS_LOST,
        selected_index=selected_index,
        on_select=on_done,
        on_highlight=on_highlighted,
    )


def clear_color_schemes():
    clear_color_scheme("Markdown.sublime-settings")
    clear_color_scheme("Markdown GFM.sublime-settings")
    clear_color_scheme("MultiMarkdown.sublime-settings")


def clear_color_scheme(filename):
    settings = sublime.load_settings(filename)
    settings.erase("color_scheme")
    sublime.save_settings(filename)


def clear_invalid_color_schemes():
    clear_invalid_color_scheme("Markdown.sublime-settings")
    clear_invalid_color_scheme("Markdown GFM.sublime-settings")
    clear_invalid_color_scheme("MultiMarkdown.sublime-settings")


def clear_invalid_color_scheme(filename):
    settings = sublime.load_settings(filename)
    color_scheme = settings.get("color_scheme")
    if not color_scheme:
        return
    try:
        sublime.load_resource(color_scheme)
    except (FileNotFoundError, IOError):
        settings.erase("color_scheme")
        sublime.save_settings(filename)
