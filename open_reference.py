import sublime, sublime_plugin
import os, string


class OpenReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        reference = self.identify_reference_at_cursor()
        self.open_reference_in_browser(reference)

    def identify_reference_at_cursor(self):
        for region in self.view.sel():
            text_on_cursor = None
            scope = self.view.extract_scope(region.begin())
            if not scope.empty():
                text_on_cursor = self.view.substr(scope)
                return text_on_cursor

        return None

    def open_reference_in_browser(self, reference):
        print("Open reference: %s" % (reference))
        sublime.active_window().run_command('open_url', {"url": reference})
