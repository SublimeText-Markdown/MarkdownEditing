import sublime
import sublime_plugin
import re


class DecideTitle(sublime_plugin.EventListener):

    def on_modified_async(self, view):
        if 'Markdown' in view.settings().get('syntax'):
            text = view.substr(sublime.Region(0, view.size()))
            it = re.finditer('^(#{1,6}(?!#))|(-+|=+)', text, re.M)
            title = ''
            for m in it:
                if re.match(r'^(-+|=+)$', m.group()):
                    title_end = m.start() - 1
                    title_begin = text.rfind('\n', 0, title_end) + 1
                    title = text[title_begin: title_end]
                else:
                    title_begin = m.end() + 1
                    title_end = re.search(
                        '(' + m.group() + ')?(\n|$)', text[title_begin:]).start() + title_begin
                    title = text[title_begin: title_end]
                break

            if len(view.name()) == 0 and len(title) > 0:
                view.set_name(title)
