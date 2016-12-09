import sublime
import sublime_plugin
import re
try:
    from MarkdownEditing.mdeutils import *
except ImportError:
    from mdeutils import *

def getFoldedRegion(view, reg):
    for i in view.folded_regions():
        if i.contains(reg):
            return i
    return None

class FoldSectionCommand(MDETextCommand):

    def run(self, edit):
        view = self.view
        sections = []
        shouldUnfold = False
        for sel in view.sel():
            text = view.substr(sublime.Region(0, view.size()))
            it = re.finditer(r'^(#{1,6}(?!#))|^(-{3,}|={3,})', text, re.M)
            section_start = -1
            section_end = view.size() - 1
            section_level = 0
            for m in it:
                if re.match(r'^(-{3,}|={3,})$', m.group()):
                    title_end = m.start() - 1
                    title_begin = text.rfind('\n', 0, title_end) + 1
                    title_end = m.end() + 1
                    level = 2 if text[m.start()] == '-' else 1
                else:
                    title_begin = m.end()
                    title_end = re.search('(' + m.group() + ')?(\n|$)', text[title_begin:]).start() + title_begin
                    title_begin = m.start()
                    level = m.end() - m.start()
                if title_begin <= sel.a:
                    section_start = title_end
                    section_level = level
                elif section_level >= level:
                    section_end = title_begin - 1
                    break
            if section_start >= 0 and section_end >= section_start:
                reg = sublime.Region(section_start, section_end)
                folded = getFoldedRegion(view, reg)
                if folded != None:
                    sections.append(folded)
                    shouldUnfold = True
                else:
                    sections.append(reg)

        for reg in sections:
            if shouldUnfold:
                view.unfold(reg)
            else:
                view.fold(reg)

