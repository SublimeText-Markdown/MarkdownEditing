import sublime

from .headings import all_headings
from .view import MdeTextCommand, MdeViewEventListener


def folded_region(view, region):
    for i in view.folded_regions():
        if i.contains(region):
            return i
    return None


def section_level(view, pt):
    last_level = 0
    for heading_begin, heading_end, level in all_headings(view):
        if heading_end < pt:
            last_level = level
        elif heading_begin < pt:
            return level
        else:
            return last_level


def section_region_and_level(view, pt):
    section_start = -1
    section_end = view.size()
    section_level = 0
    for heading_begin, heading_end, heading_level in all_headings(view):
        if heading_begin <= pt:
            section_start = heading_end
            section_level = heading_level
        elif section_level >= heading_level:
            section_end = heading_begin - 1
            break
    if section_start >= 0 and section_end > section_start:
        return (sublime.Region(section_start, section_end), section_level)
    return (None, -1)


def unfold_all_sections(view):
    view.unfold(sublime.Region(0, view.size()))
    fold_all_links(view)


def fold_all_links(view):
    if view.settings().get("mde.auto_fold_link.enabled", True):
        ignored = view.find_by_selector(view.settings().get("mde.auto_fold_link.selector", ""))
        view.fold(ignored)


class MdeFoldSectionCommand(MdeTextCommand):
    def description(self):
        return "Toggle fold/unfold on current section"

    def run(self, edit):
        view = self.view
        sections = []
        shouldUnfold = False
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a)
            if section:
                folded = folded_region(view, section)
                if folded:
                    sections.append(folded)
                    shouldUnfold = True
                else:
                    sections.append(section)

        if shouldUnfold:
            for section in sections:
                view.unfold(section)
            fold_all_links(view)
        else:
            for section in sections:
                view.fold(section)

        sublime.status_message(
            "%d region%s %sfolded"
            % (len(sections), "s" if len(sections) > 1 else "", "un" if shouldUnfold else "")
        )


class MdeFoldSectionContextCommand(MdeFoldSectionCommand):
    def is_visible(self):
        if not super().is_visible():
            return False
        view = self.view
        hasSection = False
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a)
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
        hasSection = False
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a)
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
    def run(self, edit, target_level=0):
        view = self.view
        unfold_all_sections(view)
        section_start = -1
        section_end = view.size()
        n_sections = 0
        for heading_begin, heading_end, heading_level in all_headings(view):
            if target_level == 0 or heading_level <= target_level:
                if section_start > 0:
                    section_end = heading_begin - 1
                    reg = sublime.Region(section_start, section_end)
                    view.fold(reg)
                    n_sections += 1
                    section_start = -1
            if target_level == 0 or heading_level == target_level:
                section_start = heading_end
        if section_start >= 0:
            reg = sublime.Region(section_start, view.size())
            view.fold(reg)
            n_sections += 1
        if len(view.sel()) > 0:
            for sel in view.sel():
                if folded_region(view, sel) is None:
                    view.show(sel)
        else:
            view.show(sublime.Region(0, 0))
        sublime.status_message("%d region%s folded" % (n_sections, "s" if n_sections > 1 else ""))


class MdeUnfoldAllSectionsCommand(MdeTextCommand):
    def run(self, edit):
        unfold_all_sections(self.view)


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

    def on_load(self):
        """
        Called on load.
        """
        self.fold_all()

    def on_activated(self):
        """
        Called on load.
        """
        self.auto_fold_all()

    def on_selection_modified(self):
        """
        Temporarily unfold links
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
