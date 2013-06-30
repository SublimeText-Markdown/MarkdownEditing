import re
import sublime
import sublime_plugin


class IndentQuote(sublime_plugin.TextCommand):
    def description(self):
        return 'Indent a quote'

    def run(self, edit):
        view = self.view
        selections = view.sel()
        new_selections = []

        for selection in selections:
            lines_in_selection = self.view.lines(selection)
            all_lines = []

            expanded_selection_start = lines_in_selection[0].begin()
            for line in lines_in_selection:
                complete_line = view.line(line)
                expanded_selection_end = complete_line.end()
                text = view.substr(complete_line)
                all_lines.append("> " + text)

            expanded_selection = sublime.Region(expanded_selection_start, expanded_selection_end)

            replacement_text = "\n".join(all_lines)
            view.replace(edit, expanded_selection, replacement_text)

            new_selections.append(sublime.Region(expanded_selection_start, expanded_selection_start + len(replacement_text)))

        selections.clear()
        for selection in new_selections:
            selections.add(selection)

    def is_enabled(self):
        return True


class DeindentQuote(sublime_plugin.TextCommand):
    def description(self):
        return 'Deindent a quote'

    def run(self, edit):
        view = self.view
        selections = view.sel()
        new_selections = []

        for selection in selections:
            lines_in_selection = self.view.lines(selection)
            all_lines = []

            expanded_selection_start = lines_in_selection[0].begin()
            for line in lines_in_selection:
                complete_line = view.line(line)
                expanded_selection_end = complete_line.end()
                text = view.substr(complete_line)
                all_lines.append(re.sub(r'^(> )', '', text))

            expanded_selection = sublime.Region(expanded_selection_start, expanded_selection_end)

            replacement_text = "\n".join(all_lines)
            view.replace(edit, expanded_selection, replacement_text)

            new_selections.append(sublime.Region(expanded_selection_start, expanded_selection_start + len(replacement_text)))

        selections.clear()
        for selection in new_selections:
            selections.add(selection)

    def is_enabled(self):
        return True
