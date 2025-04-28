import sublime_plugin

from bisect import bisect_left, bisect_right


class MdeGotoNextCriticCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if not sel:
            return

        critics = self.view.find_by_selector("markup.critic")
        if not critics:
            return

        idx = bisect_right(critics, sel[0])
        sel = critics[idx] if idx < len(critics) else critics[0]
        self.view.sel().clear()
        self.view.sel().add(sel)
        self.view.show_at_center(sel)


class MdeGotoPrevCriticCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        if not sel:
            return

        critics = self.view.find_by_selector("markup.critic")
        if not critics:
            return

        idx = bisect_left(critics, sel[0]) - 1
        sel = critics[idx] if idx >= 0 else critics[-1]
        self.view.sel().clear()
        self.view.sel().add(sel)
        self.view.show_at_center(sel)
