import sublime_plugin
import re

class IndentListItemCommand(sublime_plugin.TextCommand):
    def run(self, edit, reverse = False):
        for region in self.view.sel():
            line = self.view.line(region)
            line_content = self.view.substr(line)

            # List bullets in their order
            bullets = ["*", "-", "+"]

            bullet_pattern = "([*+\\-])"

            # Transform the bullet to the next/previous bullet type
            for key, bullet in enumerate(bullets):
                if bullet in line_content:
                    new_line = line_content.replace(bullet, bullets[(key + (1 if not reverse else -1)) % len(bullets)])
                    break

            else:
                return

            # Determine how to indent (tab or spaces)
            if self.view.settings().get("translate_tabs_to_spaces"):
                tab_str = self.view.settings().get("tab_size", 4) * " "

            else:
                tab_str = "\t"

            if not reverse:
                # Do the indentation
                new_line = re.sub(bullet_pattern, tab_str + "\\1", new_line)

            else:
                # Do the unindentation
                new_line = re.sub(tab_str + bullet_pattern, "\\1", new_line)

            # Insert the new item
            self.view.replace(edit, line, new_line)

    def is_enabled(self):
        return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))
