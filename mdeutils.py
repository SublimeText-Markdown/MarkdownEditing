import sublime
import sublime_plugin


def view_is_markdown(view):
    if len(view.sel()) > 0:
        return len(view.sel()) > 0 and bool(view.score_selector(view.sel()[0].a, "text.html.markdown"))
    else:
        return False


class MDETextCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return view_is_markdown(self.view)
