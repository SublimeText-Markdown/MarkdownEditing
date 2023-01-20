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


def section_level(view, pt):
    """
    Calculate heading level of the section `pt` is in.

    :param view:          The view
    :param region:        The text position to find the section's region for

    :returns:             The section level
    """
    last_level = 0
    for heading_begin, heading_end, level in all_headings(view):
        if heading_end < pt:
            last_level = level
        elif heading_begin < pt:
            return level
        else:
            return last_level


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


def url_regions(view):
    """
    Returns a list of all url regions specified by `"mde.auto_fold_link.selector"`.

    It caches the current view's regions to reduce api calls. Regions are fetched from API
    whenever the function is called for another view or its content changed. It is just to prevent
    API calls everytime caret is moved around.

    :param view:  The view

    :returns:   A list of regions
    """
    view_id = view.id()
    change_count = view.change_count()

    try:
        if url_regions.view_id == view_id and url_regions.change_count == change_count:
            return url_regions.regions
    except AttributeError:
        pass

    url_regions.view_id = view_id
    url_regions.change_count = change_count
    url_regions.regions = view.find_by_selector(
        view.settings().get("mde.auto_fold_link.selector", "")
    )
    return url_regions.regions


def urls_to_fold(view):
    """
    Returns a list of url regions to fold.

    Returns all url regions but those a caret is placed within or which are partly selected.

    :param view:    The view
    :param region:  The region urls to return for.

    :returns:   A list of regions
    """
    if not view.settings().get("mde.auto_fold_link.enabled", True):
        return []

    return [url for url in url_regions(view) if not any(url.contains(sel) for sel in view.sel())]


def fold_urls(view):
    """
    Fold all urls the caret is not located within and unfold those it is.

    Partly or fully selected link urls are unfolded.
    Urls contained by larger selections are folded or keep folded.

    :param view:  The view
    """
    fold_regions = []
    unfold_regions = []
    for url in url_regions(view):
        if any(url.contains(sel) for sel in view.sel()):
            unfold_regions.append(url)
        else:
            fold_regions.append(url)

    view.fold(fold_regions)
    view.unfold(unfold_regions)


def unfold_urls(view):
    """
    Unold all urls which are not part of a larger folded region (section).

    Make sure not to unfold sections, just because a contained link url is to be unfolded.

    :param view:  The view
    """
    folded_regions = view.folded_regions()
    unfold_regions = [
        url for url in url_regions(view) if any(url.contains(folded) for folded in folded_regions)
    ]
    view.unfold(unfold_regions)


class MdeFoldSectionCommand(MdeTextCommand):
    """
    This class describes a `mde_fold_section` command.

    The command folds sections at least one caret is within.

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

    def is_enabled(self):
        view = self.view
        target_level = folding_target_level(view)
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a, target_level)
            if section:
                return not bool(folded_region(view, section))
        return False

    def run(self, edit):
        view = self.view
        target_level = folding_target_level(view)
        sections = []
        for sel in view.sel():
            if any(s.contains(sel) for s in sections):
                continue
            section, _ = section_region_and_level(view, sel.begin(), target_level)
            if not section:
                continue
            folded_section = folded_region(view, section)
            if not folded_section:
                sections.append(section)

        view.fold(sections)

        sublime.status_message(
            "{} region{} folded".format(len(sections), "s" if len(sections) > 1 else "")
        )


class MdeUnfoldSectionCommand(MdeTextCommand):
    """
    This class describes a `mde_unfold_section` command.

    The command unfolds sections at least one caret is within.

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

    def is_enabled(self):
        view = self.view
        target_level = folding_target_level(view)
        for sel in view.sel():
            section, _ = section_region_and_level(view, sel.a, target_level)
            if section:
                return bool(folded_region(view, section))
        return False

    def run(self, edit):
        view = self.view
        target_level = folding_target_level(view)
        sections = []
        levels = []
        for sel in view.sel():
            if any(s.contains(sel) for s in sections):
                continue
            section, level = section_region_and_level(view, sel.begin(), target_level)
            if not section:
                continue
            folded_section = folded_region(view, section)
            if folded_section:
                if folded_section != section:
                    level = section_level(view, folded_section.begin())
                sections.append(folded_section)
            levels.append(level)

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
        view.fold(regions_to_fold + urls_to_fold(view))

        sublime.status_message(
            "{} region{} unfolded".format(len(sections), "s" if len(sections) > 1 else "")
        )


class MdeShowFoldAllSectionsCommand(MdeTextCommand):
    """
    This class describes a `mde_show_fold_all_sections` command.
    """

    def run(self, edit):
        window = self.view.window()
        if window:
            window.run_command(
                "show_overlay", {"overlay": "command_palette", "text": "MarkdownEditing: Fold"}
            )


class MdeFoldAllSectionsCommand(MdeTextCommand):
    """
    This class describes a `mde_fold_all_sections` command which folds sections by level.

    With `target_level`

    - `= 0`, all sections are folded, but their headings keep visible.
    - `> 0`, only headings of same or higher level are visible.
    """

    def run(self, edit, target_level=0):
        view = self.view
        view_region = sublime.Region(0, view.size())
        view.unfold(view_region)
        sections = list(sections_to_fold(view, view_region, target_level))
        view.fold(sections + urls_to_fold(view))
        view.settings().set("mde.folding.target_level", target_level)
        show_first_unfolded_selection(view)
        sublime.status_message(
            "{} region{} folded".format(len(sections), "s" if len(sections) > 1 else "")
        )


class MdeUnfoldAllSectionsCommand(MdeTextCommand):
    """
    This class describes a `mde_unfold_all_sections` command which unfolds all sections.
    """

    def run(self, edit):
        view = self.view
        view.settings().erase("mde.folding.target_level")
        view.unfold(sublime.Region(0, view.size()))
        if view.settings().get("mde.auto_fold_link.enabled", True):
            fold_urls(view)
        show_first_unfolded_selection(view)
        sublime.status_message("all regions unfolded")


class MdeFoldLinksCommand(MdeTextCommand):
    """
    This class describes a `mde_fold_links` command.

    It can be used to eigther toggle automatic link folding or set it on/off for called view.

    Example:

    ```json
    { "command": "mde_fold_links", "args": {"fold": true} }
    ```
    """

    def is_checked(self):
        return self.view.settings().get("mde.auto_fold_link.enabled", True)

    def run(self, edit, fold=None):
        if fold is None:
            fold = not self.is_checked()

        self.view.settings().set("mde.auto_fold_link.enabled", fold)

        if fold:
            fold_urls(self.view)
        else:
            unfold_urls(self.view)


class MdeFoldLinksListener(MdeViewEventListener):
    """
    This class describes an automatic link folding event listener.
    """

    @classmethod
    def is_applicable(cls, settings):
        return MdeViewEventListener.is_applicable(settings) and settings.get(
            "mde.auto_fold_link.enabled", True
        )

    def on_init(self):
        """
        Fold all links after application startup.
        """
        fold_urls(self.view)

    def on_load(self):
        """
        Fold all links once file is loaded.
        """
        fold_urls(self.view)

    def on_activated(self):
        """
        Update link folding when activating view.
        """
        fold_urls(self.view)

    def on_selection_modified(self):
        """
        Update link folding when moving caret around.
        """
        fold_urls(self.view)
