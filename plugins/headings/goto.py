import sublime

from .common import all_headings
from ..view import MdeTextCommand


class MdeGotoNextHeadingCommand(MdeTextCommand):
    def run(self, edit, same_level=True):
        view = self.view
        headings = tuple(all_headings(view))
        new_sel = []
        for sel in view.sel():
            section_level = 0
            for title_begin, title_end, level in headings:
                if title_begin <= sel.begin():
                    section_level = level
                elif not same_level or section_level >= level:
                    new_sel.append(sublime.Region(title_begin, title_end))
                    break

        if not new_sel:
            sublime.status_message("No heading can be found")
            return

        view.sel().clear()
        view.sel().add_all(new_sel)
        view.show(new_sel[-1])


class MdeGotoPreviousHeadingCommand(MdeTextCommand):
    def run(self, edit, same_level=True):
        view = self.view
        headings = tuple(all_headings(view))
        new_sel = []
        max_level = 0
        last_level = 0
        found = False
        for sel in view.sel():
            prev = {}
            for title_begin, title_end, level in headings:
                max_level = max(max_level, level)
                if title_end < sel.begin():
                    for lvl in range(level, max_level + 1):
                        prev[lvl] = (title_begin, title_end)
                    last_level = level
                else:
                    found = True
                    break
            if found:
                if same_level:
                    while level not in prev and level > 0:
                        level -= 1
                    if level > 0 and level in prev:
                        new_sel.append(sublime.Region(prev[level][0], prev[level][1]))
                else:
                    if last_level > 0 and last_level in prev:
                        new_sel.append(sublime.Region(prev[last_level][0], prev[last_level][1]))
            elif max_level > 0:
                new_sel.append(sublime.Region(title_begin, title_end))

        if not new_sel:
            sublime.status_message("No heading can be found")
            return

        view.sel().clear()
        view.sel().add_all(new_sel)
        view.show(new_sel[-1])
