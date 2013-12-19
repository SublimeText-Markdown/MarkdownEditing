"""
    This file contains some "distraction free" mode improvements. However they can be
    used in normal mode, too. These features can be enabled/disabled via settings files.
    In order to target "distraction free" mode, FullScreenStatus plugin must be installed:
    https://github.com/maliayas/SublimeText_FullScreenStatus
"""

import sublime, sublime_plugin


def on_distraction_free():
    return sublime.active_window().settings().get('fss_on_distraction_free')

def view_is_markdown(view):
    return bool(view.score_selector(view.sel()[0].a, "text.html.markdown"))

class KeepCurrentLineCentered(sublime_plugin.EventListener):
    def on_modified(self, view):
        # One of the MarkdownEditing syntax files must be in use.
        if not view_is_markdown(view):
            return False

        if on_distraction_free():
            if view.settings().get("mde.distraction_free_mode").get("mde.keep_centered") is False:
                return False

        else:
            if view.settings().get("mde.keep_centered") is False:
                return False

        view.show_at_center(view.sel()[0].begin())
