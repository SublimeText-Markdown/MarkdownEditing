import itertools
import re
import sublime

from .logging import logger
from .view import MdeTextCommand

SETEXT_DASHES_RE = re.compile(
    r'''
    (?: =+ | -+ ) # A run of ---- or ==== underline characters.
    \s*           # Optional trailing whitespace.
    $             # Must fill the while line. Don't match "- list items"
    ''', re.X
)

SETEXT_HEADER_RE = re.compile(
    r'''
    ^(.+)\n
    ( =+ | -+ ) # A run of ---- or ==== underline characters.
    [ \t]*        # Optional trailing whitespace.
    $             # Must fill the while line. Don't match "- list items"
    ''', re.X | re.M
)


def fix_dashes(view, edit, text_region, dash_region):
    """
    Replaces the underlined "dash" region of a setext header with a run of
    dashes or equal-signs that match the length of the header text.
    """

    if len(view.substr(text_region).strip()) == 0:
        # Ignore dashes not under text. They are HRs.
        return

    old_dashes = view.substr(dash_region)
    first_dash = old_dashes[0]
    new_dashes = first_dash * text_region.size()
    view.replace(edit, dash_region, new_dashes)


class MdeCompleteUnderlinedHeadingsCommand(MdeTextCommand):
    """
    The `mde_complete_underline_headings` command inserts enough dash characters
    to match the length of the previous (header text) line, if the selection
    looks like a setext underline of - or = .

    Before:

    ```markdown
    This is an H2
    -|
    ```

    After:

    ```markdown
    This is an H2
    -------------|
    ```

    Note:

    If the line before a selection is empty or starts with single dash, a tab
    character is inserted instead assuming the current line belonging to a list.
    """

    def run(self, edit):
        for region in self.view.sel():
            dashes_line = self.view.line(region)
            # Ignore first list
            if dashes_line.begin() == 0:
                continue

            text_line = self.view.line(dashes_line.begin() - 1)
            if text_line.begin() < 0:
                continue

            text = self.view.substr(text_line).lstrip()
            dashes = self.view.substr(dashes_line).strip()
            bullets = self.view.settings().get("mde.list_indent_bullets", ["*", "-", "+"])

            # ignore, text_line is a list item or empty
            if len(dashes) < 2 and (not text or text[0] in bullets):
                self.view.insert(edit, region.begin(), '\t')
                continue

            match = SETEXT_DASHES_RE.match(dashes)
            if match:
                fix_dashes(self.view, edit, text_line, dashes_line)


class MdeConvertUnderlinedHeadingsToAtxCommand(MdeTextCommand):
    """
    The `mde_convert_underlined_headings` command searches for all setext headings
    and converts them to atx format.
    """

    def run(self, edit, closed=False):
        regions = list(self.view.sel())
        if len(regions) == 1 and regions[0].size() == 0:
            regions = [sublime.Region(0, self.view.size())]
        regions.reverse()
        for region in regions:
            txt = self.view.substr(region)
            matches = list(SETEXT_HEADER_RE.finditer(txt))
            matches.reverse()
            for m in matches:
                mreg = sublime.Region(region.begin() + m.start(), region.begin() + m.end())
                atx = "# "
                if '-' in m.group(2):
                    atx = "#" + atx
                closing = atx[::-1] if closed else ""
                self.view.replace(edit, mreg, atx + m.group(1) + closing)


class MdeFixUnderlinedHeadingsCommand(MdeTextCommand):
    """
    The `mde_fix_underlined_headings` command searches for all setext headings
    resize them to match the preceding header text.
    """

    def description(self):
        # Used as the name for Undo.
        return 'Fix Underlined Markdown Headings'

    def run(self, edit):
        lines = self.view.split_by_newlines(sublime.Region(0, self.view.size()))
        if len(lines) < 2:
            return

        # Since we're modifying the text, we are shifting all the following
        # regions. To avoid this, just go backwards.
        lines = reversed(lines)

        # Duplicate the iterator and next() it once to get farther ahead.
        # Since lines are reversed, this will always point to the line *above*
        # the current one: the text of the header.
        prev_lines, lines = itertools.tee(lines)
        next(prev_lines)

        for text_line, dashes_line in zip(prev_lines, lines):
            dashes_text = self.view.substr(dashes_line)
            m = SETEXT_DASHES_RE.match(dashes_text)
            if m:
                fix_dashes(self.view, edit, text_line, dashes_line)


class MdeChangeHeadingsLevelCommand(MdeTextCommand):
    """
    The `mde_change_headings_level` command modifies headings levels to an
    absolute or by a relative value.

    1. Carets are moved to the beginning of each header label.
    2. Indentation level is kept intact.
    3. Works within block quotes.
    4. Respects `mde.match_header_hashes` setting.

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

    ATX_HEADER_PATTERN = re.compile(r"""(?x)
        ^
        (?P<quote> [\s>]* )           # maybe block quote
        (?:
           (?P<hashes> \#+ )          # maybe leading hashes
           (?P<spacing> \s+? )        # followed by at least one whitespace
        |  (?! [-+*#] )               # or not an unordered list
        )
        (?P<text> .*? )               # maybe line text
        (?P<suffix> (?:\s+\#+)?\s* )  # maybe trailing hashes
        $
    """)

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
        match_header_hashes = view.settings().get("mde.match_header_hashes")

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
                    string
                )
                continue

            quote, hashes, spacing, text, suffix = match.groups()
            to = calc_level(hashes or "")
            new_text = quote + "#" * to + " " * bool(to) + text
            if match_header_hashes and to > 0:
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
