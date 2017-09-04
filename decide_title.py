import sublime
import sublime_plugin
import re


class DecideTitle(sublime_plugin.EventListener):

    def on_modified_async(self, view):
        syntax = view.settings().get('syntax')
        if syntax and 'Markdown' in syntax:
            text = view.substr(sublime.Region(0, view.size()))
            it = re.finditer(r'^(#{1,6}(?!#))|^(-{3,}|={3,})', text, re.M)
            title = ''
            title_begin = None
            for m in it:
                if '.front-matter' in view.scope_name(m.start()):
                    continue
                if re.match(r'^(-{3,}|={3,})$', m.group()):
                    title_end = m.start() - 1
                    title_begin = text.rfind('\n', 0, title_end) + 1
                else:
                    title_begin = m.end()
                    title_end = re.search('(' + m.group() + ')?(\n|$)', text[title_begin:]).start() + title_begin
                    title_begin = m.start() + 1
                if 'markup.raw.block.markdown' not in view.scope_name(title_begin).split(' '):
                    break
            if len(title) == 0 and title_begin is not None:
                title = text[title_begin: title_end]

            title = title.strip()
            if view.file_name() is None and len(title) > 0:
                view.set_name(title[:55])
