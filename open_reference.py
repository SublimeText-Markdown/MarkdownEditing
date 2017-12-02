import sublime, sublime_plugin
import os, string

try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *


class OpenReferenceCommand(MDETextCommand):
    def description(self):
        return "Open the URL reference in browser"

    def is_visible(self):
        """Return True if cursor is on a wiki page reference."""
        for sel in self.view.sel():
            scopes = self.view.scope_name(sel.b).split(" ")
            if 'meta.link.inline.markdown' in scopes:
                if 'markup.underline.link.markdown' in scopes:
                    return True                

        return False

    def run(self, edit):
        print("Running OpenReferenceCommand")
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
