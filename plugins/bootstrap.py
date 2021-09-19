import os
import shutil
import sys

import sublime

from .color_schemes import clear_color_schemes, clear_invalid_color_schemes, select_color_scheme

BOOTSTRAP_VERSION = "3.0.3"

package_name = "MarkdownEditing"


def get_ingored_packages():
    settings = sublime.load_settings("Preferences.sublime-settings")
    return settings.get("ignored_packages") or []


def save_ingored_packages(ignored_packages):
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.set("ignored_packages", ignored_packages)
    sublime.save_settings("Preferences.sublime-settings")


def disable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if "Markdown" not in ignored_packages:
        ignored_packages.append("Markdown")
        save_ingored_packages(ignored_packages)


def enable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if "Markdown" in ignored_packages:
        ignored_packages.remove("Markdown")
        save_ingored_packages(ignored_packages)

        def reassign():
            reassign_syntax(
                "Markdown.sublime-syntax",
                "Packages/Markdown/Markdown.sublime-syntax",
            )
            reassign_syntax(
                "MultiMarkdown.sublime-syntax",
                "Packages/Markdown/MultiMarkdown.sublime-syntax",
            )

        sublime.set_timeout(reassign, 100)


def reassign_syntax(current_syntax, new_syntax):
    for window in sublime.windows():
        for view in window.views():
            syntax = view.settings().get("syntax")
            if syntax and syntax.endswith(current_syntax) and syntax != new_syntax:
                view.assign_syntax(new_syntax)


def bootstrap_syntax_assignments():
    """
    Reassign syntax to all open Markdown, MultiMarkdown or Plain Text files.

    Repair syntax assignments of open views after install or upgrade, in case
    old ones no longer exist.
    """
    markdown = "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"
    multimarkdown = "Packages/MarkdownEditing/syntaxes/MultiMarkdown.sublime-syntax"

    for window in sublime.windows():
        for view in window.views():
            syntax = view.settings().get("syntax")
            if syntax:
                syntax = os.path.basename(syntax)
                if syntax in ("Markdown.tmLanguage", "Markdown.sublime-syntax"):
                    view.assign_syntax(markdown)
                    continue
                if syntax in ("MultiMarkdown.tmLanguage", "MultiMarkdown.sublime-syntax"):
                    view.assign_syntax(multimarkdown)
                    continue

            file_name = view.file_name()
            if file_name:
                _, ext = os.path.splitext(file_name)
                if ext in (".md", ".mdown", ".markdown"):
                    view.assign_syntax(markdown)


def on_after_install():
    cache_path = os.path.join(sublime.cache_path(), "MarkdownEditing")
    bootstrapped = os.path.join(cache_path, "bootstrapped")

    # Check bootstrapped cookie.
    try:
        if open(bootstrapped).read() == BOOTSTRAP_VERSION:
            return
    except FileNotFoundError:
        pass

    # Clear previous syntax caches.
    shutil.rmtree(cache_path, ignore_errors=True)
    os.makedirs(cache_path, exist_ok=True)

    def async_worker():
        bootstrap_syntax_assignments()
        disable_native_markdown_package()
        clear_invalid_color_schemes()
        # Update bootstrap cookie.
        open(bootstrapped, "w").write(BOOTSTRAP_VERSION)

        select_color_scheme()

    sublime.set_timeout_async(async_worker, 200)


def on_before_uninstall():
    if "package_control" in sys.modules:
        from package_control import events

        if events.remove(package_name):
            # Native package causes some conflicts.
            enable_native_markdown_package()
            # Remove syntax specific color schemes.
            clear_color_schemes()
