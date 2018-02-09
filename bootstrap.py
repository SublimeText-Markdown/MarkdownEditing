import sys
import sublime
import sublime_plugin
import re
try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *

package_name = 'MarkdownEditing'


def get_ingored_packages():
    settings = sublime.load_settings('Preferences.sublime-settings')
    return settings.get('ignored_packages', [])


def save_ingored_packages(ignored_packages):
    settings = sublime.load_settings('Preferences.sublime-settings')
    settings.set('ignored_packages', ignored_packages)
    sublime.save_settings('Preferences.sublime-settings')


def disable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if 'Markdown' not in ignored_packages:
        ignored_packages.append('Markdown')
        save_ingored_packages(ignored_packages)


def enable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if 'Markdown' in ignored_packages:
        ignored_packages.remove('Markdown')
        save_ingored_packages(ignored_packages)


def choose_color_theme(window):
    window = window or sublime.active_window()
    view = window.new_file()
    view.run_command('append', {'characters': '''# A sample Markdown document

This is a sample document so you can preview the color themes.

## I am a second-level header

Markdown supports _italics_, __bold__, and ___bold italics___ style.

There are also inline styles like `inline code in monospace font` and ~~strikethrough style~~. __There may be ~~strikethroughed text~~ or `code text` inside bold text.__ _And There may be ~~strikethroughed text~~ or `code text` inside italic text._

To reference something from a URL, [Named Links][links] and [Inline links](https://example.com/index.html) are of great help. Sometimes ![A picture][sample image] is worth a thousand words.

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

'''})
    view.set_syntax_file('Packages/MarkdownEditing/Markdown.tmLanguage')
    default_mde_scheme = sublime.load_settings('Markdown.sublime-settings').get('color_scheme') or 'Packages/MarkdownEditing/MarkdownEditor.tmTheme'
    print(default_mde_scheme)
    view.settings().set('color_scheme', default_mde_scheme)
    view.set_read_only(True)
    view.set_scratch(True)

    global_scheme = sublime.load_settings('Preferences.sublime-settings').get('color_scheme')
    themes = ['Packages/MarkdownEditing/MarkdownEditor.tmTheme',
              'Packages/MarkdownEditing/MarkdownEditor-Focus.tmTheme',
              'Packages/MarkdownEditing/MarkdownEditor-Yellow.tmTheme',
              'Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme',
              'Packages/MarkdownEditing/MarkdownEditor-ArcDark.tmTheme',
              global_scheme]

    themes_display = [re.search('[^/]+(?=\.tmTheme$)', s).group(0) + (' (Current)' if s == default_mde_scheme else '') + (' (Global)' if s == global_scheme else '') for s in themes]

    def set_scheme(scheme):
        view.settings().set('color_scheme', scheme)
        sublime.load_settings('Markdown.sublime-settings').set('color_scheme', scheme)

    def on_done(index):
        if index == -1:
            set_scheme(default_mde_scheme)
        elif index == len(themes) - 1:
            set_scheme(global_scheme)
        else:
            set_scheme(themes[index])
        sublime.save_settings('Markdown.sublime-settings')
        view.close()

    def on_highlighted(index):
        if index == len(themes) - 1:
            set_scheme(global_scheme)
        else:
            set_scheme(themes[index])

    window.show_quick_panel(themes_display, on_done, flags=sublime.KEEP_OPEN_ON_FOCUS_LOST, on_highlight=on_highlighted)


def plugin_loaded():
    if "package_control" in sys.modules:
        from package_control import events

        if events.install(package_name):
            # Native package causes some conflicts.
            disable_native_markdown_package()
            # Prmopts to select a color theme
            choose_color_theme()


def plugin_unloaded():
    if "package_control" in sys.modules:
        from package_control import events

        if events.remove(package_name):
            # Native package causes some conflicts.
            enable_native_markdown_package()

# Compat with ST2
if sys.version_info < (3,):
    plugin_loaded()
    unload_handler = plugin_unloaded


class MdeColorActivateCommand(MDETextCommand):

    def run(self, edit):
        choose_color_theme(self.view.window())
