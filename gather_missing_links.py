import re
import sublime_plugin


class GatherMissingLinkMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        markers = []
        self.view.find_all("\]\[([^\]]+)\]", 0, "$1", markers)
        self.view.find_all("\[([^\]]*)\]\[\]", 0, "$1", markers)
        missinglinks = [link for link in set(markers) if not self.view.find_all("\n\s*\[%s\]:" % re.escape(link))]
        if len(missinglinks):
            # Remove all whitespace at the end of the file
            whitespace_at_end = self.view.find(r'\s*\z', 0)
            self.view.replace(edit, whitespace_at_end, "\n")

            # If there is not already a reference list at the and, insert a new line at the end
            if not self.view.find(r'\n\s*\[[^\]]*\]:.*\s*\z', 0):
                self.view.insert(edit, self.view.size(), "\n")

            for link in missinglinks:
                self.view.insert(edit, self.view.size(), '[%s]: \n' % link)

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))
