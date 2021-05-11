import sublime_plugin


def view_is_markdown(view):
    try:
        return view.match_selector(view.sel()[0].begin(), "text.html.markdown")
    except IndexError:
        return False


class MDETextCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return view_is_markdown(self.view)

    def is_visible(self):
        return view_is_markdown(self.view)
