import re

from .view import MdeTextCommand


class MdeIndentListItemCommand(MdeTextCommand):

    def run(self, edit, reverse=False):
        for region in self.view.sel():
            line = self.view.line(region)
            line_content = self.view.substr(line)

            bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])
            bullet_pattern = '([' + ''.join(re.escape(i) for i in bullets) + '])'

            new_line = line_content

            # Transform the bullet to the next/previous bullet type
            if self.view.settings().get("mde.list_indent_auto_switch_bullet", True):

                for key, bullet in enumerate(bullets):
                    if bullet in new_line:
                        if reverse and new_line.startswith(bullet) and key == 0:
                            # In this case, do not switch bullets
                            continue

                        new_line = new_line.replace(
                            bullet, bullets[(key + (1 if not reverse else -1)) % len(bullets)])
                        break

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


class MdeIndentListMultiitemCommand(MdeTextCommand):

    def run(self, edit, reverse=False):
        todo = []
        for region in self.view.sel():
            lines = self.view.line(region)
            lines = self.view.split_by_newlines(lines)
            for line in lines:
                line_content = self.view.substr(line)

                if len(line_content) == 0:
                    continue

                # Determine how to indent (tab or spaces)
                if self.view.settings().get("translate_tabs_to_spaces"):
                    tab_str = self.view.settings().get("tab_size", 4) * " "

                else:
                    tab_str = "\t"

                if re.match(r"^\s*(>\s*)?[*+\\-]\s+(.*)$", line_content):
                    bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])
                    bullet_pattern = '([' + ''.join(re.escape(i) for i in bullets) + '])'
                    bullet_pattern_a = r"^\s*(?:>\s*)?("
                    bullet_pattern_b = r")\s+"
                    new_line = line_content
                    # Transform the bullet to the next/previous bullet type
                    if self.view.settings().get("mde.list_indent_auto_switch_bullet", True):
                        for key, bullet in enumerate(bullets):
                            re_bullet = re.escape(bullet)
                            search_pattern = bullet_pattern_a + re_bullet + bullet_pattern_b
                            if re.search(search_pattern, line_content):
                                if reverse and new_line.startswith(bullet) and key == 0:
                                    # In this case, do not switch bullets
                                    continue
                                new_bullet = bullets[(key + (1 if not reverse else -1)) % len(bullets)]
                                new_line = re.sub(re_bullet, new_bullet, new_line, 1)
                                break
                    if not reverse:
                        # Do the indentation
                        new_line = re.sub(bullet_pattern, tab_str + r"\1", new_line, 1)

                    else:
                        # Do the unindentation
                        new_line = re.sub(tab_str + bullet_pattern, r"\1", new_line, 1)
                else:
                    if not reverse:
                        new_line = tab_str + line_content
                    else:
                        new_line = re.sub(tab_str, "", line_content, 1)

                # Insert the new item
                todo.append([line, new_line])

        while len(todo) > 0:
            j = todo.pop()
            self.view.replace(edit, j[0], j[1])


class MdeSwitchListBulletTypeCommand(MdeTextCommand):

    def run(self, edit):
        todo = []
        unordered_bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])
        for region in self.view.sel():
            lines = self.view.line(region)
            lines = self.view.split_by_newlines(lines)
            number = 1
            for line in lines:
                line_content = self.view.substr(line)
                # print(line_content)
                m = re.match(
                    r"^(\s*(?:>\s*)?)["
                    + ''.join(re.escape(i) for i in unordered_bullets)
                    + r"](\s+.*)$", line_content)
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
                        # Transform the bullet to unnumbered bullet type
                        new_line = m.group(1) + unordered_bullets[0] + m.group(2)

                        # Insert the new item
                        todo.append([line, new_line])

        while len(todo) > 0:
            j = todo.pop()
            self.view.replace(edit, j[0], j[1])


class MdeNumberListCommand(MdeTextCommand):

    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(view.full_line(sel))
        num = re.search(r'\d', text).start()
        dot = text.find(".")
        additional_spaces = re.search(r"^\s*", text[dot + 1:]).group()
        increment = 0
        if self.view.settings().get('mde.auto_increment_ordered_list_number', True):
            increment = 1
        if num == 0:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%d.%s" % (int(text[:dot]) + increment, additional_spaces))
        else:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%s%d.%s" % (text[:num], int(text[num:dot]) + increment, additional_spaces))


class MdeNumberListReferenceCommand(MdeTextCommand):

    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(view.full_line(sel))
        num = re.search(r'\d', text).start()
        dot = text.find("]")
        if num == 0:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%d]: " % (int(text[:dot]) + 1,))
        else:
            view.erase(edit, sel)
            view.insert(edit, sel.begin(), "\n%s%d]: " % (text[:num], int(text[num:dot]) + 1))
