import sublime, sublime_plugin

class PasteAsReferenceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		sel = view.sel()[0]
		text = view.substr(sel)
		contents = sublime.get_clipboard()
		self.view.replace(edit,sel,"["+text+"]: "+contents)

	def is_enabled(self):
		return self.view.sel()
