import sublime_plugin
import re

class SwitchListBulletTypeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        todo = []
        for region in self.view.sel():
            lines = self.view.line(region)
            lines = self.view.split_by_newlines(lines)
            for line in lines:
                line_content = self.view.substr(line)
                print(line_content)
                m = re.match(r"^(\s*(?:>\s*)?)[*+\-](\s+.*)$", line_content)
                if m:
                    # Transform the bullet to numbered bullet type
                    new_line = m.group(1) + "1." + m.group(2)

                    # Insert the new item
                    todo.append([line, new_line])
                else:
                    m = re.match(r"^(\s*(?:>\s*)?)[0-9]+\.(\s+.*)$", line_content)
                    if m:
                        # Transform the bullet to unnumbered bullet type
                        new_line = m.group(1) + "-" + m.group(2)

                        # Insert the new item
                        todo.append([line, new_line])


        while len(todo) > 0:
            j = todo.pop()
            self.view.replace(edit, j[0], j[1])

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))
