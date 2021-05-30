import sys

import sublime

from .color_schemes import clear_color_schemes, select_color_scheme

package_name = "MarkdownEditing"


def get_ingored_packages():
    settings = sublime.load_settings("Preferences.sublime-settings")
    return settings.get("ignored_packages", [])


def save_ingored_packages(ignored_packages):
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.set("ignored_packages", ignored_packages)
    sublime.save_settings("Preferences.sublime-settings")


def disable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if "Markdown" not in ignored_packages:
        reassign_syntax(
            "Packages/Markdown/Markdown.sublime-syntax",
            "Packages/MarkdownEditing/Markdown.sublime-syntax",
        )
        reassign_syntax(
            "Packages/Markdown/MultiMarkdown.sublime-syntax",
            "Packages/MarkdownEditing/MultiMarkdown.sublime-syntax",
        )
        ignored_packages.append("Markdown")
        save_ingored_packages(ignored_packages)


def enable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if "Markdown" in ignored_packages:
        ignored_packages.remove("Markdown")
        save_ingored_packages(ignored_packages)

        def reassign():
            reassign_syntax(
                "Packages/MarkdownEditing/Markdown.sublime-syntax",
                "Packages/Markdown/Markdown.sublime-syntax",
            )
            reassign_syntax(
                "Packages/MarkdownEditing/MultiMarkdown.sublime-syntax",
                "Packages/Markdown/MultiMarkdown.sublime-syntax",
            )

        sublime.set_timeout(reassign, 100)


def reassign_syntax(current_syntax, new_syntax):
    for window in sublime.windows():
        for view in window.views():
            syntax = view.settings().get("syntax")
            if syntax and syntax == current_syntax:
                view.assign_syntax(new_syntax)


def on_after_install():
    if "package_control" in sys.modules:
        from package_control import events

        if events.install(package_name):
            # Native package causes some conflicts.
            disable_native_markdown_package()
            # Prompts to select a color scheme.
            select_color_scheme()


def on_before_uninstall():
    if "package_control" in sys.modules:
        from package_control import events

        if events.remove(package_name):
            # Native package causes some conflicts.
            enable_native_markdown_package()
            # Remove syntax specific color schemes.
            clear_color_schemes()
