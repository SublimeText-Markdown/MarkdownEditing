from .mdeutils import MDETextCommand


class ReplaceSelectedCommand(MDETextCommand):
    def run(self, edit, **args):
        for region in self.view.sel():
            self.view.replace(edit, region, args['text'])
