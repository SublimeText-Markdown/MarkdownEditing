import sys

import sublime

from .color_schemes import select_color_scheme

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


def on_after_install():
    if "package_control" in sys.modules:
        from package_control import events

        if events.install(package_name):
            # Native package causes some conflicts.
            disable_native_markdown_package()
            # Prompts to select a color theme
            select_color_scheme()


def on_before_uninstall():
    if "package_control" in sys.modules:
        from package_control import events

        if events.remove(package_name):
            # Native package causes some conflicts.
            enable_native_markdown_package()
