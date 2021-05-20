import sublime

from .folding import all_headings, get_folded_region
from .view import MdeTextCommand


class MDEBoldCommand(MdeTextCommand):

    def description(self):
        return 'Apply bold style'

    def run(self, edit):
        view = self.view
        sections = []
        shouldUnfold = False
        for sel in view.sel():
            section_start = -1
            section_end = view.size()
            section_level = 0
            for (title_begin, title_end, level) in all_headings(view):
                if title_begin <= sel.a:
                    section_start = title_end
                    section_level = level
                elif section_level >= level:
                    section_end = title_begin - 1
                    break
            if section_start >= 0 and section_end >= section_start:
                reg = sublime.Region(section_start, section_end)
                folded = get_folded_region(view, reg)
                if folded is not None:
                    sections.append(folded)
                    shouldUnfold = True
                else:
                    sections.append(reg)

        for reg in sections:
            if shouldUnfold:
                view.unfold(reg)
            else:
                view.fold(reg)
