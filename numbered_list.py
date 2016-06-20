import sublime_plugin
import re

class NumberListCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(view.full_line(sel))
        num = re.search('\d', text).start()
        dot = text.find(".")
        additional_spaces = re.search(r"^\s*", text[dot+1:]).group()
        increment = 0
        if self.view.settings().get('mde.auto_increment_ordered_list_number', True):
            increment = 1
        if num == 0:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%d.%s" % (int(text[:dot]) + increment, additional_spaces))
        else:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%s%d.%s" % (text[:num], int(text[num:dot]) + increment, additional_spaces))

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class NumberListReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(view.full_line(sel))
        num = re.search('\d', text).start()
        dot = text.find("]")
        if num == 0:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%d]: " % (int(text[:dot]) + 1,))
        else:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%s%d]: " % (text[:num], int(text[num:dot]) + 1))