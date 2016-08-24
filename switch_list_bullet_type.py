import sublime_plugin
import re
from MarkdownEditing.mdeutils import *


class SwitchListBulletTypeCommand(MDETextCommand):

    def run(self, edit):
        todo = []
        for region in self.view.sel():
            lines = self.view.line(region)
            lines = self.view.split_by_newlines(lines)
            number = 1
            for line in lines:
                line_content = self.view.substr(line)
                # print(line_content)
                m = re.match(r"^(\s*(?:>\s*)?)[*+\-](\s+.*)$", line_content)
                if m:
                    # Transform the bullet to numbered bullet type
                    new_line = m.group(1) + str(number) + "." + m.group(2)
                    if self.view.settings().get('mde.auto_increment_ordered_list_number', True):
                        number += 1

                    # Insert the new item
                    todo.append([line, new_line])
                else:
                    m = re.match(r"^(\s*(?:>\s*)?)[0-9]+\.(\s+.*)$", line_content)
                    if m:
                        marker = self.view.settings().get('mde.list_indent_bullets', ["*"])
                        # Transform the bullet to unnumbered bullet type
                        new_line = m.group(1) + marker[0] + m.group(2)

                        # Insert the new item
                        todo.append([line, new_line])

        while len(todo) > 0:
            j = todo.pop()
            self.view.replace(edit, j[0], j[1])
