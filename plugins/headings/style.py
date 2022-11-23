import os.path
import re

from ..view import MdeTextCommand, MdeViewEventListener


class MdeMatchHeadingHashesCommand(MdeTextCommand):
    """
    The `mde_match_heading_hashes` command adds or removes trailing hashes to or from atx headings.

    If no argument is passed, trailing hashes are added or removed depending on actual value of
    the current view's `mde.match_heading_hashes` setting.

    If the argument `enabled` is of `True` or `False`, its value is applied to view specific
    `mde.match_heading_hashes` setting and trailing hashes are added and removed accordingly.

    Note: The function balances the amount of leading and trailing hashes.
    """

    def run(self, edit, enabled=None):
        view = self.view

        if enabled is None:
            enabled = view.settings().get("mde.match_heading_hashes", False)
        elif isinstance(enabled, bool):
            view.settings().set("mde.match_heading_hashes", enabled)
        else:
            raise TypeError("Argument: 'enabled' must be a bool!")

        if enabled:
            replacement = r"\1\2 \3 \2"
        else:
            replacement = r"\1\2 \3"

        pattern = re.compile(r"^([ \t]*)(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
        for region in reversed(view.find_by_selector("markup.heading")):
            text = view.substr(region)
            new_text = pattern.sub(replacement, text)
            if text != new_text:
                view.replace(edit, region, new_text)


class MdeMatchHeadingHashesDetector(MdeViewEventListener):
    """
    The `MdeMatchHeadingHashesDetector` auto-detects ATX heading style.

    The detected style is applied to the view specific setting `"mde.match_heading_hashes"`
    so that any modification to headings works as expected.
    """

    @classmethod
    def is_applicable(cls, settings):
        try:
            if "Markdown" not in settings.get("syntax"):
                return False
            if not settings.get("mde.detect_heading_style", False):
                # remove view specific setting to use global value from preferences
                settings.erase("mde.match_heading_hashes")
                return False
            return True
        except (AttributeError, TypeError):
            return False

    def on_load(self):
        self.auto_detect_heading_style()

    def on_pre_save(self):
        self.auto_detect_heading_style()
        if self.view.settings().get("mde.auto_match_heading_hashes", False):
            self.view.run_command("mde_match_heading_hashes")

    def auto_detect_heading_style(self):
        view = self.view

        # don't break syntax_test files
        file_name = view.file_name()
        if file_name and os.path.basename(file_name).startswith("syntax_test"):
            view.settings().set("mde.auto_match_heading_hashes", False)
            return

        num_leading = len(
            view.find_by_selector("markup.heading punctuation.definition.heading.begin")
        )
        if num_leading:
            num_trailing = len(
                view.find_by_selector("markup.heading punctuation.definition.heading.end")
            )
            view.settings().set("mde.match_heading_hashes", num_trailing / num_leading > 0.5)
        else:
            view.settings().erase("mde.match_heading_hashes")
