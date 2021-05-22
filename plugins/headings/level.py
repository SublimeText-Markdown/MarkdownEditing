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

    ATX_HEADER_PATTERN = re.compile(
        r"""(?x)
        ^
        (?P<quote> [\s>]* )           # maybe block quote
        (?:
           (?P<hashes> \#{1,6} )      # maybe leading hashes
           (?P<spacing> \s+? )        # followed by at least one whitespace
        |  (?! [-+*#] )               # or not an unordered list
        )
        (?P<text> .*? )               # maybe line text
        (?P<suffix> (?:\s+\#+)?\s* )  # maybe trailing hashes
        $
    """
    )

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

            def calc_level(start):
                return (int(start.count("#") + by)) % self.MAX_LEVEL

            self._set_level(edit, calc_level, select)

        elif to is not None:
            try:
                to = max(0, min(self.MAX_LEVEL, int(to)))
            except (TypeError, ValueError):
                logger.error("Invalid headings level specified!")
                return

            def calc_level(start):
                return to

            self._set_level(edit, calc_level, select)

        else:
            logger.error("No headings level specified!")

    def _set_level(self, edit, calc_level, select):
        view = self.view  # type: sublime.View
        vsels = view.sel()  # type: sublime.Selection
        match_heading_hashes = view.settings().get("mde.match_heading_hashes")

        # One or more selections may span multiple lines each of them to change heading level for.
        # To correctly handle caret placements split all selections into single lines first.
        regions = [region for sel in vsels for region in view.split_by_newlines(sel)]
        vsels.clear()
        vsels.add_all(regions)
        regions = []

        for sel in vsels:
            line = view.line(sel)
            string = view.substr(line)
            match = self.ATX_HEADER_PATTERN.match(string)
            if not match:
                logger.debug(
                    "Change heading level ignored line %d: '%s'",
                    view.rowcol(line.a)[0] + 1,
                    string,
                )
                continue

            quote, hashes, spacing, text, suffix = match.groups()
            to = calc_level(hashes or "")
            new_text = quote + "#" * to + " " * bool(to) + text
            if match_heading_hashes and to > 0:
                new_text += " " + "#" * to
            view.replace(edit, line, new_text)
            # move caret to the beginning of heading text and optionaly select it
            line.a += len(quote) + bool(to) + to
            line.b = line.a + len(text) * bool(select)
            regions.append(line)

        # fix caret positions and selections
        if regions:
            vsels.clear()
            vsels.add_all(regions)
