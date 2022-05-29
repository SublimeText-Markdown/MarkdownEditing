import re
import sublime

from .view import MdeTextCommand


class MdeBaseUnIndentListItemCommand(MdeTextCommand):
    """
    This is an interanal text command class shared by `(un)indent_list_item` commands.

    It is responsible to read settings and cycle through all selections to replace text.
    """

    def run(self, edit):
        queue = []

        view = self.view
        settings = view.settings()
        bullets = settings.get("mde.list_indent_bullets", ["*", "-", "+"])
        if settings.get("mde.list_indent_auto_switch_bullet", True):
            new_bullets = bullets
        else:
            new_bullets = None

        if settings.get("translate_tabs_to_spaces"):
            tab_str = " " * settings.get("tab_size", 4)
        else:
            tab_str = "\t"

        pattern = re.compile(
            r"^(?:[\s>]*>\s)?(\s*)(?:([%s])\s)?" % "".join(re.escape(bullet) for bullet in bullets)
        )

        for sel in view.sel():
            for region in view.split_by_newlines(view.line(sel)):
                match = re.search(pattern, view.substr(region))
                if not match:
                    continue

                indent, bullet = match.groups()
                text = self.compute_replacement(indent, tab_str, bullet, new_bullets)
                if text is None:
                    continue

                # setup region to replace based on pattern match
                region.b = region.a + max(match.end(1), match.end(2))
                region.a += match.start(1)

                queue.append([region, text])

        for r, text in reversed(queue):
            view.replace(edit, r, text)

    def compute_replacement(self, indent, tab_str, bullet, bullets):
        raise RuntimeError


class MdeIndentListItemCommand(MdeBaseUnIndentListItemCommand):
    """
    The `mde_indent_list_item` command indents unordered list items.

    It indents lists within blockquotes.
    It changes list bullet according to indentation level
    if `mde.list_indent_auto_switch_bullet` is set `true`.
    """

    def compute_replacement(self, indent, tab_str, bullet, bullets):
        text = indent + tab_str
        if bullet:
            if bullets:
                text += bullets[(bullets.index(bullet) + 1) % len(bullets)]
            else:
                text += bullet
        return text


class MdeUnindentListItemCommand(MdeBaseUnIndentListItemCommand):
    """
    The `mde_unindent_list_item` command unindents unordered list items.

    It unindents lists within blockquotes.
    It changes list bullet according to indentation level.
    if `mde.list_indent_auto_switch_bullet` is set `true`.
    """

    def compute_replacement(self, indent, tab_str, bullet, bullets):
        if not indent:
            return None

        text = indent.replace(tab_str, "", 1)
        if bullet:
            if bullets:
                text += bullets[(bullets.index(bullet) - 1) % len(bullets)]
            else:
                text += bullet
        return text


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
            r"^\s*(?:>\s*)*(?:([%s])|(\d+[.)]))(\s+)"
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
    """
    This class describes the `mde_number_list` command.
    """

    def run(self, edit):
        view = self.view
        auto_increment = view.settings().get("mde.auto_increment_ordered_list_number", True)
        pattern = re.compile(r"^([ \t>]*)(\d+)([.)])([ \t]+|$)")

        for sel in view.sel():
            to_insert = "\n"

            line = view.line(sel)
            col = sel.begin() - line.begin()

            match = pattern.search(view.substr(line))
            if match:
                quote, number, punct, space = match.groups()
                next_number = str(int(number) + 1) if auto_increment else number

                num_spaces = max(1, len(space) - (len(next_number) - len(number)))
                # caret is in front of item text
                if col < match.end():
                    num_spaces -= match.end() - col

                to_insert += quote + next_number + punct + " " * num_spaces

            view.erase(edit, sel)
            view.insert(edit, sel.begin(), to_insert)


class MdeInsertTaskListItemCommand(MdeTextCommand):
    """
    The `mde_insert_task_list_item` command inserts a new GFM task.

    It respects the primary bullet set via `"mde.list_indent_bullets"` setting.
    """

    def run(self, edit):
        align_text = self.view.settings().get("mde.list_align_text", True)
        bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])

        to_insert = "{} [ ]".format(bullets[0])
        if align_text:
            to_insert += "\t"
        else:
            to_insert += " "

        for sel in self.view.sel():
            self.view.insert(edit, sel.begin(), to_insert)


class MdeToggleTaskListItemCommand(MdeTextCommand):
    """
    The `mde_toggle_task_list_item` command toggles the check mark of task list items.

    It must be called in the line of the check mark.

    **Examples:**

    ```markdown
    # Ordered Task List

    1. [ ] task 1
    2. [x] task 2

    # Unordered Task List

    * [ ] task 1
    - [x] task 2
    + [ ] task 3

    # Quoted Task List

    > * [ ] task 1
    > * [x] task 2
    ```
    """

    def run(self, edit):
        pattern = re.compile(
            r"""
            ^[ \t>]*                # leading blockquote or whitespace
            (?: [-+*] | \d+[.)] )   # unordered or ordered list bullet
            (?: [ \t]+\[([ xX])\] ) # GFM task checkbox
            (?: [ \t]+ | $ )        # at least one space,tab or eol
            """,
            re.X,
        )

        for sel in self.view.sel():
            for region in self.view.split_by_newlines(self.view.line(sel)):
                region.b = min(region.b, region.a + 50)
                match = pattern.search(self.view.substr(region))
                if not match:
                    continue

                # calculate text position of check mark
                region.a += match.start(1)
                region.b = region.a + 1

                self.view.replace(edit, region, "x" if match.group(1) == " " else " ")


class MdeJoinLines(MdeTextCommand):
    """
    This class describes a `mde_join_lines` command.

    It removes any leading list or blockquote punctuation from any line after a
    caret and the linefeed separating it from a line a caret is placed within.

    It is meant to be bound to `"delete"` key when caret is at eol.
    """

    def run(self, edit):
        view = self.view
        pattern = re.compile(
            r"""
            ^
            ([ \t>]*)                   # leading blockquote or whitespace
            (
                (?:[-+*]|\d+[.)])       # unordered or ordered list bullet
                (?:[ \t]+\[[ xX]\])?    # optional GFM task checkbox
                (?:[ \t]+|$)            # at least one space,tab or eol
            )?
            (\S|$)                      # first char of content, if any
            """,
            re.X,
        )

        for sel in view.sel():
            pt = sel.begin()
            if len(sel) == 0:
                # join current with following line
                lines = [view.line(sel)]
                _, col = view.rowcol(pt)
            else:
                # join all selected lines beginning with the one before the last
                lines = reversed(view.split_by_newlines(view.line(sel))[:-1])
                col = None

            for line in lines:
                eol = line.end()
                eol_ws = eol == 0 or view.substr(eol - 1) in (" ", "\t", "\n")

                # mark newline for deletion
                to_delete = 1

                next_line_matches = pattern.search(view.substr(view.line(eol + 1)))
                if next_line_matches:
                    if (
                        # selected text block
                        col is None
                        # caret is within list item paragraph
                        or col > next_line_matches.start(2)
                        # caret followed by content (not only whitespace or blockquote signs)
                        or any(ch not in " \t>" for ch in view.substr(sublime.Region(pt, eol)))
                    ):
                        # mark blockquote and list bullets for deletion
                        to_delete += next_line_matches.start(3)
                    else:
                        # mark blockquote for deletion
                        to_delete += next_line_matches.start(2)

                    # maintain at least one space between tokens (convert newline to space so to say)
                    if eol_ws is False and next_line_matches.end(3) > next_line_matches.start(3):
                        view.replace(edit, sublime.Region(eol, eol + to_delete), " ")
                        continue

                view.erase(edit, sublime.Region(eol, eol + to_delete))
