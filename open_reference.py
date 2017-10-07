import sublime, sublime_plugin
import os, string


class OpenReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        reference = self.identify_reference()

        print("Open reference: %s" % (reference))
        self.open_reference_in_browser(reference)

    def identify_reference(self):
        for region in self.view.sel():
            text_on_cursor = None
            if region.begin() == region.end():
                scope = self.view.extract_scope(region.begin())
                if not scope.empty():
                    text_on_cursor = self.view.substr(scope)
                    return text_on_cursor

        return None

    def open_reference_in_browser(self, reference):
        sublime.active_window().run_command('open_url', {"url": reference})
