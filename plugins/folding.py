import sublime

from .headings import all_headings
from .view import MdeTextCommand, MdeViewEventListener

ST4 = int(sublime.version()) > 4000


def folding_target_level(view):
    return view.settings().get("mde.folding.target_level", -1)


def folded_region(view, region):
    """
    Find first unfolded selection.

    :param view:  The view
    """
    for i in view.folded_regions():
        if i.contains(region):
            return i
    return None


def first_unfolded_selection(view):
    """
    Find first unfolded selection.

    :param view:  The view
    """
    folded_regions = view.folded_regions()
    for sel in view.sel():
        if not any(r.contains(sel) for r in folded_regions):
            return sel
    return sublime.Region(0, 0)


def show_first_unfolded_selection(view):
    """
    Scroll to the first unfolded selection.

    :param view:  The view
    """
    if ST4:
        view.show(first_unfolded_selection(view), keep_to_left=True, animate=False)
    else:
        view.show(first_unfolded_selection(view))


def section_region_and_level(view, pt, target_level):
    """
    Calculate `region` and heading level of the section `pt` is in.

    :param view:          The view
    :param region:        The text position to find the section's region for
    :param target_level:  The level a section must have to be folded

    :returns:
        region of the whole section including all its child sections, if `target_level` < 9
        region between previous and next heading, if `target_level` is 9
    """
    section_start = -1
    section_end = view.size()
    section_level = 0
    for heading_begin, heading_end, heading_level in all_headings(view):
        if heading_begin <= pt:
            section_start = heading_end
            section_level = heading_level
        elif (section_level >= heading_level) or (target_level == 0 and section_start > 0):
            section_end = heading_begin - 1
            break
    if section_start >= 0 and section_end > section_start:
        return (sublime.Region(section_start, section_end), section_level)
    return (None, -1)


def sections_to_fold(view, region, target_level):
    """
    Generate foldable sections of a given region by target_level.

    :param view:          The view
    :param region:        The region to look for sections in
    :param target_level:  The level a section must have to be folded

    :yields:    The regions to fold

    :returns:   None
    """
    section_start = -1
    section_end = region.end()

    for heading_begin, heading_end, heading_level in all_headings(
        view, region.begin(), region.end()
    ):
        if target_level == 0 or heading_level <= target_level and section_start > 0:
            section_end = heading_begin - 1
            yield sublime.Region(section_start, section_end)
            section_start = -1
        if target_level == 0 or heading_level == target_level:
            section_start = heading_end

    if section_start >= 0:
        yield sublime.Region(section_start, region.end())


def links_to_fold(view):
    if view.settings().get("mde.auto_fold_link.enabled", True):
        return view.find_by_selector(view.settings().get("mde.auto_fold_link.selector", ""))
    return []


class MdeFoldSectionCommand(MdeTextCommand):
    """
    This class implements the `mde_fold_section` command.

    The command folds or unfolds sections at least one caret is within.

    It's behavior depends on former call of `mde_fold_all_secitons` command and
    the active `mde.folding.target_level` setting respectively.

    -1: The whole section, including all child sections is folded and unfolded.
        The folded region begins after the nearest heading found before a caret's
        position and ends with the next heading of same level after the caret.
     0: The region between two the headings enclosing the caret's position
        is folded or unfolded. That's the so called outline mode.
    >0: Like (-1) but all child sections of higher level then `target_level`
        keep folded if their parent section is unfolded.
    """

    def description(self):
        return "Toggle fold/unfold on current section"

    def run(self, edit):
        view = self.view
        target_level = folding_target_level(view)
        sections = []
        levels = []
        shouldUnfold = False
        for sel in view.sel():
            if not any(s.contains(sel) in s for s in sections):
                section, level = section_region_and_level(view, sel.a, target_level)
                if section:
                    levels.append(level)
                    folded = folded_region(view, section)
                    if folded:
                        sections.append(folded)
                        shouldUnfold = True
                    else:
                        sections.append(section)

        if shouldUnfold:
            regions_to_fold = []
            if target_level > -1:
                # keep all child sections folded
                for section, level in zip(sections, levels):
                    regions_to_fold.extend(
                        sections_to_fold(view, section, max(target_level, level + 1))
                    )
            else:
                for section in sections:
                    regions_to_fold.extend(sections_to_fold(view, section, -1))

            view.unfold(sections)
            view.fold(regions_to_fold + links_to_fold(view))

        else:
            view.fold(sections)

        sublime.status_message(
            "%d region%s %sfolded"
            % (len(sections), "s" if len(sections) > 1 else "", "un" if shouldUnfold else "")
        )


class MdeFoldSectionContextCommand(MdeFoldSectionCommand):
    def is_visible(self):
        if not super().is_visible():
            return False
        view = self.view
        target_level = folding_target_level(view)
        hasSection = False
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a, target_level)
            if section:
                folded = folded_region(view, section)
                if folded:
                    return False
                else:
                    hasSection = True
        return hasSection


class MdeUnfoldSectionContextCommand(MdeFoldSectionCommand):
    def is_visible(self):
        if not super().is_visible():
            return False
        view = self.view
        target_level = folding_target_level(view)
        hasSection = False
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a, target_level)
            if section:
                folded = folded_region(view, section)
                if folded:
                    hasSection = True
                else:
                    return False
        return hasSection


class MdeShowFoldAllSectionsCommand(MdeTextCommand):
    def run(self, edit):
        view = self.view
        view.window().run_command(
            "show_overlay", {"overlay": "command_palette", "text": "MarkdownEditing: Fold"}
        )


class MdeFoldAllSectionsCommand(MdeTextCommand):
    """
    The `mde_fold_all_sections` command folds sections by level.

    With `target_level`

    - `= 0`, all sections are folded, but their headings keep visible.
    - `> 0`, only headings of same or higher level are visible.
    """

    def run(self, edit, target_level=0):
        view = self.view
        view_region = sublime.Region(0, view.size())
        view.unfold(view_region)
        sections = list(sections_to_fold(view, view_region, target_level))
        view.fold(sections + links_to_fold(view))
        view.settings().set("mde.folding.target_level", target_level)
        show_first_unfolded_selection(view)
        sublime.status_message(
            "{} region{} folded".format(len(sections), "s" if len(sections) > 1 else "")
        )


class MdeUnfoldAllSectionsCommand(MdeTextCommand):
    """
    The `mde_unfold_all_sections` command unfolds all sections.
    """

    def run(self, edit):
        view = self.view
        view.unfold(sublime.Region(0, view.size()))
        view.fold(links_to_fold(view))
        view.settings().erase("mde.folding.target_level")
        show_first_unfolded_selection(view)


class MdeFoldLinksProviderMixin:
    def __init__(self):
        self._fold_regions = None
        self._folded_regions = set()
        self._unfolded_regions = set()

    def is_auto_fold_enabled(self):
        return self.view.settings().get("mde.auto_fold_link.enabled", True)

    def enable_auto_fold(self, enable=None):
        if enable is None:
            enable = not self.is_auto_fold_enabled()
        if enable:
            self.auto_fold_all()
        else:
            self.unfold_all()
        self.view.settings().set("mde.auto_fold_link.enabled", enable)

    def get_fold_regions(self):
        if self._fold_regions is None:
            self._fold_regions = self.view.find_by_selector(
                self.view.settings().get("mde.auto_fold_link.selector", "")
            )
        return self._fold_regions

    def invalidate_fold_regions(self):
        self._fold_regions = None

    def auto_fold_all(self):
        """
        Fold all but selected regions or those the caret intersects with.
        """

        def intersects(lhs, rhs):
            """
            Fix ST's dump Region.intersects().

            :param      lhs:    region on the left hand side
            :type       lhs:    sublime.Region
            :param      rhs:    region on the right hand side
            :type       rhs:    sublime.Region
            """
            lb = lhs.begin()
            le = lhs.end()
            rb = rhs.begin()
            re = rhs.end()
            return (
                (rb >= lb and rb <= le)
                or (re >= lb and re <= le)
                or (lb >= rb and lb <= re)
                or (le >= rb and le <= re)
            )

        fold_regions = self.get_fold_regions()
        folded_regions = []
        folded_set = set()
        unfolded_regions = []
        unfolded_set = set()
        for sel in self.view.sel():
            for region in fold_regions:
                if intersects(sel, region):
                    unfolded_regions.append(region)
                    unfolded_set.add(region.to_tuple())
                else:
                    folded_regions.append(region)
                    folded_set.add(region.to_tuple())

        if self._folded_regions != folded_set:
            self._folded_regions = folded_set
            self.view.fold(folded_regions)

        if self._unfolded_regions != unfolded_set:
            self._unfolded_regions = unfolded_set
            self.view.unfold(unfolded_regions)

    def fold_all(self):
        """
        Fold all auto folding regions.
        """
        self.view.fold(self.get_fold_regions())

    def unfold_all(self):
        """
        Unfold all auto folding regions.
        """
        self.view.unfold(self.get_fold_regions())


class MdeFoldLinksListener(MdeViewEventListener, MdeFoldLinksProviderMixin):
    def __init__(self, view):
        super().__init__(view)
        MdeFoldLinksProviderMixin.__init__(self)

    @classmethod
    def is_applicable(cls, settings):
        return MdeViewEventListener.is_applicable(settings) and settings.get(
            "mde.auto_fold_link.enabled", False
        )

    def on_init(self):
        """
        Fold all links after application startup.
        """
        self.fold_all()

    def on_load(self):
        """
        Fold all links once file is loaded.
        """
        self.fold_all()

    def on_activated(self):
        """
        Update link folding when activating view.
        """
        self.auto_fold_all()

    def on_selection_modified(self):
        """
        Update link folding when moving caret around.
        """
        self.auto_fold_all()

    def on_modified(self):
        self.invalidate_fold_regions()


class MdeFoldLinksCommand(MdeTextCommand, MdeFoldLinksProviderMixin):
    def __init__(self, view):
        super().__init__(view)
        MdeFoldLinksProviderMixin.__init__(self)

    def run(self, edit, fold=None):
        self.enable_auto_fold(fold)
