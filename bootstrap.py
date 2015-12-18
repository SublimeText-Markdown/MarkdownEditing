import sys

package_name = 'MarkdownEditing'

def get_ingored_packages():
    settings = sublime.load_settings('Preferences.sublime-settings')
    return settings.get('ignored_packages', [])

def save_ingored_packages(ignored_packages):
    settings.set('ignored_packages', ignored_packages)
    sublime.save_settings('Preferences.sublime-settings')

def disable_native_markdown_package():
    ignored_packages = get_ingored_packages()
    if 'Markdown' not in ignored_packages:
        ignored_packages.append('Markdown')
        save_ingored_packages(ignored_packages)

def enable_native_markdown_packageb():
    ignored_packages = get_ingored_packages()
    if 'Markdown' in ignored_packages:
        ignored_packages.remove('Markdown')
        save_ingored_packages(ignored_packages)

def plugin_loaded():
    from package_control import events

    if events.install(package_name):
        # Native package causes some conflicts.
        disable_native_markdown_package()

def plugin_unloaded():
    from package_control import events

    if events.remove(package_name):
        # Native package causes some conflicts.
        enable_native_markdown_package()

# Compat with ST2
if sys.version_info < (3,):
    plugin_loaded()
    unload_handler = plugin_unloaded