import itertools
import re
import sublime

from ..view import MdeTextCommand

SETEXT_DASHES_RE = re.compile(
    r"""
    (?: =+ | -+ ) # A run of ---- or ==== underline characters.
    \s*           # Optional trailing whitespace.
    $             # Must fill the while line. Don't match "- list items"
    """,
    re.X,
)

SETEXT_HEADER_RE = re.compile(
    r"""
    ^(.+)\n
    ( =+ | -+ ) # A run of ---- or ==== underline characters.
    [ \t]*        # Optional trailing whitespace.
    $             # Must fill the while line. Don't match "- list items"
    """,
    re.X | re.M,
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
                self.view.insert(edit, region.begin(), "\t")
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
                if "-" in m.group(2):
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
        return "Fix Underlined Markdown Headings"

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
