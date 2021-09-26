import re
import sublime

from ..logging import logger
from ..view import MdeTextCommand


class MdeChangeHeadingsLevelCommand(MdeTextCommand):
    """
    The `mde_change_headings_level` command modifies headings levels to an
    absolute or by a relative value.

    1. Carets are moved to the beginning of each header label.
    2. Indentation level is kept intact.
    3. Works within block quotes.
    4. Respects `mde.match_heading_hashes` setting.

    Absolute:

    ```json
    { "command": "mde_change_headings_level", "args": {"to": 2, "select": false} }
    ```

    Relative

    ```json
    { "command": "mde_change_headings_level", "args": {"by": -1, "select": false} }
    ```
    """

    MAX_LEVEL = 6

    def description(self):
        # Used as the name for Undo.
        return "Change Headings Level"

    def run(self, edit, to=None, by=None, select=False):
        """
        Execute `mde_change_headings_level`

        :param      edit:    The edit token
        :type       edit:    sublime.Edit
        :param      to:      target heading level
        :type       to:      int
        :param      by:      increment to change heading level by
        :type       by:      int
        :param      select:  whether to select heading text or not
        :type       select:  bool
        """
        if by is not None:
            try:
                by = int(by)
            except (TypeError, ValueError):
                logger.error("Invalid headings level step size specified!")
                return

            def calc_level(level):
                return (level + by) % (self.MAX_LEVEL + 1)

            self._set_level(edit, calc_level, select)

        elif to is not None:
            try:
                to = max(0, min(self.MAX_LEVEL, int(to)))
            except (TypeError, ValueError):
                logger.error("Invalid headings level specified!")
                return

            def calc_level(level):
                return to

            self._set_level(edit, calc_level, select)

        else:
            logger.error("No headings level specified!")

    def _set_level(self, edit, calc_level, select):
        view = self.view
        match_heading_hashes = view.settings().get("mde.match_heading_hashes")
        pattern = re.compile(
            r"""
            (?x)
            ^([ \t>]*)                   # block quotes
            (?:
                (\#+)                    # leading hashes
                (?:                      # optionally followed by ...
                    [ \t]+?              # at least one space
                    ( .*? )              # tokens not looking like trailing hashes
                    ([ \t]+\#+[ \t]*$)?  # maybe trailing hashes
                )?
            |
                ([^-+*].*?)? [ \t]*      # no heading nor list item
            )
            $
            """
        )

        # One or more selections may span multiple lines each of them to change heading level for.
        # To correctly handle caret placements split all selections into single lines first.
        vsels = view.sel()
        regions = [region for sel in vsels for region in view.split_by_newlines(sel)]
        vsels.clear()
        vsels.add_all(regions)
        regions = []

        for sel in vsels:
            line = view.line(sel)
            string = view.substr(line)
            match = pattern.match(string)
            if not match:
                logger.debug(
                    "Change heading level ignored line %d: '%s'",
                    view.rowcol(line.a)[0] + 1,
                    string,
                )
                continue

            bol = line.begin()
            col = view.rowcol(sel.begin())[1]

            quote, _, heading, _, text = match.groups()

            old_level = match.end(2) - match.start(2)
            new_level = calc_level(old_level)

            leading = "#" * new_level + " " * bool(new_level)
            heading = heading or text or ""
            new_string = quote + leading + heading
            if match_heading_hashes and new_level:
                new_string += " " + "#" * new_level

            view.replace(edit, line, new_string)

            # convert to heading
            if old_level < 1:
                pt = bol + col + len(leading)
            # caret was in front of heading
            elif col <= match.end(1):
                pt = bol + col
            # caret after heading text
            elif col > match.end(3):
                pt = bol + len(leading) + len(heading)
            # keep caret in relative horizontal position
            else:
                pt = bol + col + len(leading) - max(0, match.start(3) - match.start(2))
                pt = min(max(bol, pt), view.line(bol).end())

            regions.append(sublime.Region(pt, pt))

        vsels.clear()
        vsels.add_all(regions)
