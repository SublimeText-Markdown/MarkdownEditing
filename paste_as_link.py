import sublime
import sublime_plugin


class PasteAsLinkCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        contents = "[${1:$SELECTION}](${2:%s})" % sublime.get_clipboard()
        view.run_command("insert_snippet", {"contents": contents})

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))
