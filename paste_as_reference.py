import sublime, sublime_plugin

class PasteAsReferenceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		edit = self.view.begin_edit()
		contents = sublime.get_clipboard()
		self.view.replace(edit,self.view.sel()[0],"["+self.view.substr(self.view.sel()[0])+"]: "+contents)
		self.view.end_edit(edit)

	def is_enabled(self):
		return self.view.sel()
