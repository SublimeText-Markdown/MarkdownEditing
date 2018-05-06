import sublime, sublime_plugin

class PrepareFromTemplateCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        print("Setting page title: " + args['title'])
        self.view.insert(edit, 0, "# " + args['title'] + "\n\n")