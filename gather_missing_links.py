import sublime_plugin


class GatherMissingLinkMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        edit = self.view.begin_edit()
        markers = []
        self.view.find_all("\]\[([^\]]+)\]", 0, "$1", markers)
        self.view.find_all("\[([^\]]*)\]\[\]", 0, "$1", markers)
        missinglinks = [link for link in set(markers) if not self.view.find_all("\n\s*\[%s\]:" % link)]
        if len(missinglinks):
            self.view.insert(edit, self.view.size(), "\n")
            for link in missinglinks:
                self.view.insert(edit, self.view.size(), '\n [%s]: ' % link)
        self.view.end_edit(edit)

    def is_enabled(self):
        return True
