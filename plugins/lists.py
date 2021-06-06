import re

from .view import MdeTextCommand


class MdeIndentListItemCommand(MdeTextCommand):
    def run(self, edit, reverse=False):
        queue = []

        auto_switch_bullet = self.view.settings().get("mde.list_indent_auto_switch_bullet", True)
        bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])

        if self.view.settings().get("translate_tabs_to_spaces"):
            tab_str = " " * self.view.settings().get("tab_size", 4)
        else:
            tab_str = "\t"

        pattern = re.compile(
            r"^(?:[\s>]*>\s)?(\s*)(?:([%s])\s)?"
            % "".join(re.escape(bullet) for bullet in bullets)
        )

        for region in self.view.sel():
            for line in self.view.split_by_newlines(self.view.line(region)):
                match = re.search(pattern, self.view.substr(line))
                if not match:
                    continue

                indent, bullet = match.groups()
                if reverse:
                    if not indent:
                        continue

                    text = indent.replace(tab_str, "", 1)
                    if bullet:
                        if auto_switch_bullet:
                            text += bullets[(bullets.index(bullet) - 1) % len(bullets)]
                        else:
                            text += bullet
                else:
                    text = indent + tab_str
                    if bullet:
                        if auto_switch_bullet:
                            text += bullets[(bullets.index(bullet) + 1) % len(bullets)]
                        else:
                            text += bullet

                # setup region to replace based on pattern match
                line.b = line.a + max(match.end(1), match.end(2))
                line.a += match.start(1)

                queue.append([line, text])

        for r, text in reversed(queue):
            self.view.replace(edit, r, text)


class MdeSwitchListBulletTypeCommand(MdeTextCommand):
    """
    The `mde_switch_list_bullet_type` command converts selected list items to ordered and unordered.

    Each selected item is evaluated separately.
    """

    def run(self, edit):
        align_text = self.view.settings().get("mde.list_align_text", True)
        auto_increment = self.view.settings().get("mde.auto_increment_ordered_list_number", True)
        bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])
        pattern = re.compile(
            r"^\s*(?:>\s*)*(?:([%s])|([0-9]+\.))(\s+)"
            % "".join(re.escape(bullet) for bullet in bullets)
        )

        for sel in self.view.sel():
            idx = 1
            for region in self.view.split_by_newlines(self.view.line(sel)):
                text = self.view.substr(region)
                match = pattern.search(text)
                if not match:
                    continue

                bullet, number, space = match.groups()
                if bullet:
                    # Transform unordered to ordered list
                    new_text = str(idx) + "."
                    if auto_increment:
                        idx += 1

                    region.a += match.start(1)
                    region.b = region.a + min(len(new_text), max(1, len(space)))
                    self.view.replace(edit, region, new_text)

                elif number:
                    # Transform ordered to unordered list
                    region.a += match.start(2)
                    if align_text:
                        new_text = bullets[0] + " " * len(number)
                        region.b = region.a + len(new_text)
                    else:
                        new_text = bullets[0]
                        region.b = region.a + len(number)
                    self.view.replace(edit, region, new_text)


class MdeNumberListCommand(MdeTextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()[0]
        text = view.substr(view.full_line(sel))
        num = re.search(r"\d", text).start()
        dot = text.find(".")
        additional_spaces = re.search(r"^\s*", text[dot + 1 :]).group()
        increment = 0
        if self.view.settings().get("mde.auto_increment_ordered_list_number", True):
            increment = 1
        if num == 0:
            view.erase(edit, sel)
            view.insert(
                edit, sel.begin(), "\n%d.%s" % (int(text[:dot]) + increment, additional_spaces)
            )
        else:
            view.erase(edit, sel)
            view.insert(
                edit,
                sel.begin(),
                "\n%s%d.%s" % (text[:num], int(text[num:dot]) + increment, additional_spaces),
            )


class MdeToggleTaskListItemCommand(MdeTextCommand):
    """
    The `mde_toggle_task_list_item` command toggles the check mark of task list items.

    It must be called in the line of the check mark.

    **Examples:**

    ```markdown
    # Orderd Task List

    1. [ ] task 1
    2. [X] task 2

    # Unorderd Task List

    * [ ] task 1
    - [X] task 2
    + [ ] task 3

    # Quoted Task List

    > * [ ] task 1
    > * [X] task 2
    ```
    """

    def run(self, edit):
        bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])
        pattern = re.compile(
            r"^(\s*(?:>\s*)*(?:[%s]|[0-9]+\.)\s+\[)([ xX])\]\s"
            % "".join(re.escape(bullet) for bullet in bullets)
        )

        for sel in self.view.sel():
            sel = self.view.line(sel)
            sel.b = min(sel.b, sel.a + 50)
            match = pattern.search(self.view.substr(sel))
            if not match:
                continue

            # calculate text position of check mark
            sel.a += len(match.group(1))
            sel.b = sel.a + 1

            mark = "X" if match.group(2) == " " else " "
            self.view.replace(edit, sel, mark)
