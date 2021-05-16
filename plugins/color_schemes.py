import re

import sublime

from .view import (
    MdeTextCommand,
    syntax_specific_settings_file
)

MARKDOWN_TEMPLATE = """# A sample Markdown document

This is a sample document so you can preview the color schemes.

## I am a second-level header

Markdown supports _italics_, __bold__, and ___bold italics___ style.

There are also inline styles like `inline code in monospace font` and ~~strikethrough style~~.
__There may be ~~strikethroughed text~~ or `code text` inside bold text.__
_And There may be ~~strikethroughed text~~ or `code text` inside italic text._

To reference something from a URL, [Named Links][links],
[Inline links](https://example.com/index.html) and direct link like <https://example.com/>
are of great help. Sometimes ![A picture][sample image] is worth a thousand words.

There are two types of lists, numbered and unnumbered.

1. Item 1
2. Item 2
3. Item 3

* Item A
    - Sub list
        + Sub sub list
        + Sub sub list 2
    - Sub list 2
* Item B
* Item C

## Fenced code

You can write fenced code inside three backticks.

```javascript
function fibo(n) {
    fibo.mem = fibo.mem || []; // I am some comment
    return fibo.mem[n] || fibo.mem[n] = n <= 1 ? 1 : fibo(n - 1) + fibo(n - 2);
}
```

## The following section is used to define named links

[links]: https://example.com/index.html
[sample image]: https://example.com/sample.png

## Wiki links

This [[SamplePage]] is a wiki link

---

"""


class MdeSelectColorSchemeCommand(MdeTextCommand):

    def run(self, edit):
        select_color_scheme(self.view)


def select_color_scheme(view=None):
    syntax_settings = syntax_specific_settings_file(view) or "Markdown.sublime-settings"

    window = view.window() if isinstance(view, sublime.View) else sublime.active_window()
    pre_view = window.new_file(
        flags=sublime.TRANSIENT,
        syntax="Packages/MarkdownEditing/Markdown.sublime-syntax"
    )
    pre_view.set_scratch(True)
    pre_view.run_command("append", {"characters": MARKDOWN_TEMPLATE})
    pre_view.set_read_only(True)

    md_settings = sublime.load_settings(syntax_settings)
    md_scheme = md_settings.get("color_scheme")

    global_settings = sublime.load_settings("Preferences.sublime-settings")
    global_scheme = global_settings.get("color_scheme")
    schemes = [
        global_scheme,
        "MarkdownEditor.sublime-color-scheme"
    ]
    for scheme in sublime.find_resources("MarkdownEditor*.sublime-color-scheme"):
        file_name = scheme.split("/")[-1]
        if file_name not in schemes:
            schemes.append(file_name)

    schemes_display = []
    selected_index = 0
    for i, s in enumerate(schemes):
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
        pre_view.settings().set("color_scheme", schemes[index])

    window.show_quick_panel(
        schemes_display,
        flags=sublime.KEEP_OPEN_ON_FOCUS_LOST,
        selected_index=selected_index,
        on_select=on_done,
        on_highlight=on_highlighted
    )
