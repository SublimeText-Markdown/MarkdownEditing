import sublime, sublime_plugin

class PasteAsLinkCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = view.sel()[0]
		text = view.substr(sel)
		contents = sublime.get_clipboard()
		view.replace(edit,sel,"["+text+"]("+contents+")")

	def is_enabled(self):
		return self.view.sel()
