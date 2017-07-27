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


def all_headings(view):
    text = view.substr(sublime.Region(0, view.size()))
    it = re.finditer(r'^(#{1,6}(?!#))|^(-{3,}|={3,})', text, re.M)
    for m in it:
        if '.front-matter' in view.scope_name(m.start()):
            continue
        if re.match(r'^(-{3,}|={3,})$', m.group()):
            title_end = m.start() - 1
            title_begin = text.rfind('\n', 0, title_end) + 1
            title_end = m.end()
            level = 2 if text[m.start()] == '-' else 1
        else:
            title_begin = m.end()
            title_end = re.search('(' + m.group() + ')?(\n|$)', text[title_begin:]).start() + title_begin
            title_begin = m.start()
            level = m.end() - m.start()
        if 'markup.raw.block.markdown' not in view.scope_name(title_begin).split(' '):
            yield (title_begin, title_end, level)


def get_current_level(view, p):
    last_level = 0
    for (title_begin, title_end, level) in all_headings(view):
        if title_end < p:
            last_level = level
        elif title_begin < p:
            return level
        else:
            return last_level


class FoldSectionCommand(MDETextCommand):

    def description(self):
        return 'Toggle fold/unfold on current section'

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
        sublime.status_message('%d region%s %sfolded' % (len(sections), 's' if len(sections) > 1 else '', 'un' if shouldUnfold else ''))


class FoldSectionContextCommand(FoldSectionCommand):

    def is_visible(self):
        if not FoldSectionCommand.is_visible(self):
            return False
        view = self.view
        hasSection = False
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
                folded = getFoldedRegion(view, reg)
                if folded != None:
                    return False
                else:
                    hasSection = True
        return hasSection


class UnfoldSectionContextCommand(FoldSectionCommand):

    def is_visible(self):
        if not FoldSectionCommand.is_visible(self):
            return False
        view = self.view
        hasSection = False
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
                folded = getFoldedRegion(view, reg)
                if folded != None:
                    hasSection = True
                else:
                    return False
        return hasSection


class ShowFoldAllSectionsCommand(MDETextCommand):

    def run(self, edit):
        view = self.view
        view.window().run_command('show_overlay', {'overlay': 'command_palette', 'text': 'MarkdownEditing: Fold'})


class FoldAllSectionsCommand(MDETextCommand):

    def run(self, edit, target_level=0):
        view = self.view
        view.run_command('unfold_all')
        section_start = -1
        section_end = view.size()
        n_sections = 0
        for (title_begin, title_end, level) in all_headings(view):
            if target_level == 0 or level <= target_level:
                if section_start > 0:
                    section_end = title_begin - 1
                    reg = sublime.Region(section_start, section_end)
                    view.fold(reg)
                    n_sections += 1
                    section_start = -1
            if target_level == 0 or level == target_level:
                section_start = title_end
        if section_start >= 0:
            reg = sublime.Region(section_start, view.size())
            view.fold(reg)
            n_sections += 1
        if len(view.sel()) > 0:
            for sel in view.sel():
                if getFoldedRegion(view, sel) == None:
                    view.show(sel)
        else:
            view.show(sublime.Region(0, 0))
        sublime.status_message('%d region%s folded' % (n_sections, 's' if n_sections > 1 else ''))


class UnfoldAllSectionsCommand(MDETextCommand):

    def run(self, edit):
        view = self.view
        view.run_command('unfold_all')


class GotoNextHeadingCommand(MDETextCommand):

    def run(self, edit, same_level=True):
        view = self.view
        new_sel = []
        for sel in view.sel():
            section_level = 0
            found = False
            for (title_begin, title_end, level) in all_headings(view):
                if title_begin <= sel.a:
                    section_level = level
                elif not same_level or section_level >= level:
                    found = True
                    break
            if found:
                new_sel.append(sublime.Region(title_begin, title_end))
        if len(new_sel) == 0:
            sublime.status_message('No heading can be found')
        else:
            view.sel().clear()
            for region in new_sel:
                view.sel().add(region)
                view.show(region)


class GotoPreviousHeadingCommand(MDETextCommand):

    def run(self, edit, same_level=True):
        view = self.view
        new_sel = []
        max_level = 0
        last_level = 0
        found = False
        for sel in view.sel():
            prev = {}
            for (title_begin, title_end, level) in all_headings(view):
                max_level = max(max_level, level)
                if title_end < sel.a:
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
        if len(new_sel) == 0:
            sublime.status_message('No heading can be found')
        else:
            view.sel().clear()
            for region in new_sel:
                view.sel().add(region)
                view.show(region)
