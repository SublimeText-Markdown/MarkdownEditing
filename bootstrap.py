import sublime


def plugin_loaded():
    # Native package causes some conflicts.
    disable_native_markdown_package()

def disable_native_markdown_package():
    settings = sublime.load_settings('Preferences.sublime-settings')
    ignored_packages = settings.get('ignored_packages', [])

    if 'Markdown' not in ignored_packages:
        ignored_packages.append('Markdown')
        settings.set('ignored_packages', ignored_packages)
        sublime.save_settings('Preferences.sublime-settings')
