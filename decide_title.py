import sublime
import sublime_plugin
import re


class DecideTitle(sublime_plugin.EventListener):

    def on_modified_async(self, view):
        syntax = view.settings().get('syntax')
        if syntax and 'Markdown' in syntax:
            text = view.substr(sublime.Region(0, view.size()))
            it = re.finditer(r'^(#{1,6}(?!#))|(-{3,}|={3,})', text, re.M)
            title = ''
            for m in it:
                if re.match(r'^(-{3,}|={3,})$', m.group()):
                    title_end = m.start() - 1
                    title_begin = text.rfind('\n', 0, title_end) + 1
                    title = text[title_begin: title_end]
                else:
                    title_begin = m.end() + 1
                    title_end = re.search(
                        '(' + m.group() + ')?(\n|$)', text[title_begin:]).start() + title_begin
                    title = text[title_begin: title_end]
                break

            if view.file_name() is None and len(title) > 0:
                view.set_name(title)
