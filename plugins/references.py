"""
Commands related to links, references and footnotes.

Exported commands:
    MdeReferenceJumpCommand
    MdeReferenceJumpContextCommand
    MdeReferenceNewReferenceCommand
    MdeReferenceNewInlineLinkCommand
    MdeReferenceNewInlineImageCommand
    MdeReferenceNewImageCommand
    MdeReferenceNewFootnoteCommand
    MdeReferenceDeleteReferenceCommand
    MdeReferenceOrganizeCommand
    MdeGatherMissingLinkMarkersCommand
    MdeConvertInlineLinkToReferenceCommand
    MdeConvertInlineLinksToReferencesCommand
"""
import sublime
import re
import operator
import urllib.parse

from .view import MdeTextCommand
from .view import MdeViewEventListener

refname_scope_name = "entity.name.reference.link.markdown"
definition_scope_name = "meta.link.reference.def.markdown"
footnote_scope_name = "meta.link.reference.footnote.markdown-extra"
marker_scope_name = "meta.link.reference.description.markdown"
marker_literal_scope_name = "meta.link.reference.literal.description.markdown"
marker_image_scope_name = "meta.image.reference.description.markdown"
marker_ref_scope_name = "markup.underline.link.markdown"
ref_link_scope_name = "markup.underline.link.markdown"
marker_begin_scope_name = "punctuation.definition.link.begin.markdown"
marker_text_end_scope_name = "punctuation.definition.link.end.markdown"
marker_text_scope_name = "meta.image.inline.description.markdown, meta.image.reference.description.markdown, meta.link.inline.description.markdown, meta.link.reference.description.markdown, meta.link.reference.literal.description.markdown"
refname_start_scope_name = "punctuation.definition.metadata.begin.markdown"
marker_end_scope_name = "punctuation.definition.metadata.end.markdown"


class Obj(object):
    """A utility obj for anoymous object."""

    def __init__(self, **kwargs):
        """Take keyword arguments."""
        self.__dict__.update(kwargs)


def getMarkers(view, name=""):
    """Find all markers."""
    # returns {name -> Region}
    markers = []
    name = re.escape(name)
    if name == "":
        markers.extend(view.find_all(r"(?<=\]\[)([^\]]+)(?=\])", 0))  # ][???]
        markers.extend(view.find_all(r"(?<=\[)([^\]]*)(?=\]\[\])", 0))  # [???][]
        markers.extend(view.find_all(r"(?<=\[)(\^[^\]]+)(?=\])(?!\s*\]:)", 0))  # [^???]
        markers.extend(
            view.find_all(r"(?<!\]\[)(?<=\[)([^\]]+)(?=\])(?!\]\[)(?!\]\()(?!\]:)", 0)
        )  # [???]
    else:
        # ][name]
        markers.extend(view.find_all(r"(?<=\]\[)(?i)(%s)(?=\])" % name, 0))
        markers.extend(view.find_all(r"(?<=\[)(?i)(%s)(?=\]\[\])" % name, 0))  # [name][]
        markers.extend(
            view.find_all(r"(?<!\]\[)(?<=\[)(?i)(%s)(?=\])(?!\]\[)(?!\]\()(?!\]:)" % name, 0)
        )  # [name]
        if name[0] == "^":
            # [(^)name]
            markers.extend(view.find_all(r"(?<=\[)(%s)(?=\])(?!\s*\]:)" % name, 0))
    regions = []

    selector = marker_ref_scope_name + ", " + marker_text_scope_name
    for x in markers:
        if view.match_selector(x.begin(), selector):
            regions.append(x)

    ids = {}
    for reg in regions:
        name = view.substr(reg).strip()
        key = name.lower()
        if key in ids:
            ids[key].regions.append(reg)
        else:
            ids[key] = Obj(regions=[reg], label=name)
    return ids


def getReferences2(view):
    """Get a dictionary of all references in the document.
    Only includes real references with scope definition_scope_name, not footnotes.

    Returns:
        dict: {name: link} mapping
    """
    pattern = re.compile(r"\[(.+)\]:\s+(?:<([^>]+)>|(\S+))", re.MULTILINE)

    ret = {}
    for definition_line in view.find_by_selector(definition_scope_name):
        for reference_def in pattern.finditer(view.substr(definition_line)):
            name, angled_link, unquoted_link = reference_def.groups()
            assert not ret.get(name)
            ret[name] = angled_link or unquoted_link
    return ret


def getReferences(view, name=""):
    """Find all reference definitions.

    Args:
        name (str, optional): Specific name to filter for

    Returns:
        dict: {name -> Obj} mapping where Objs have a
              regions attribute with a list of regions
    """

    refs = []
    name = re.escape(name)
    if name == "":
        refs.extend(view.find_all(r"(?<=^\[)([^\]]+)(?=\]:)", 0))
    else:
        refs.extend(view.find_all(r"(?<=^\[)(%s)(?=\]:)" % name, 0))
    regions = refs
    ids = {}
    for reg in regions:
        name = view.substr(reg).strip()
        key = name.lower()
        if key in ids:
            ids[key].regions.append(reg)
        else:
            ids[key] = Obj(regions=[reg], label=name)
    return ids


def isMarkerDefined(view, name):
    """Return True if a marker is defined by that name."""
    return getReferences2(view).get(name) is not None


def getCurrentScopeRegion(view, pt):
    """Extend the region under current scope."""
    orig_scope = set(view.scope_name(pt).split())
    cur_scope = set(view.scope_name(pt).split())
    start = pt
    while start > 0 and orig_scope.issubset(cur_scope):
        start -= 1
        cur_scope = set(view.scope_name(start - 1).split())
    cur_scope = orig_scope
    end = pt
    while end < view.size() and orig_scope.issubset(cur_scope):
        end += 1
        cur_scope = set(view.scope_name(end).split())
    return sublime.Region(start, end)


def findScopeFrom(view, pt, selector, backwards=False, char=None):
    """Find the nearest position of a selector from given position."""
    for pt in range(pt, 0, -1) if backwards else range(pt, view.size()):
        if view.match_selector(pt, selector) and (char is None or view.substr(pt) != char):
            break
    return pt


def get_reference(view, pos):
    """Try to match a marker or reference on given position. Return a tuple (matched, is_definition, name)."""
    scope = view.scope_name(pos).split(" ")
    if definition_scope_name in scope or footnote_scope_name in scope:
        if refname_scope_name in scope:
            # Definition name
            defname = view.substr(getCurrentScopeRegion(view, pos))
        elif refname_start_scope_name in scope:
            # Starting "["
            defname = view.substr(getCurrentScopeRegion(view, pos + 1))
        else:
            # URL or footnote
            marker_pt = findScopeFrom(view, pos, refname_scope_name, True)
            defname = view.substr(getCurrentScopeRegion(view, marker_pt))
        return (True, True, defname)
    elif (
        marker_scope_name in scope
        or marker_image_scope_name in scope
        or marker_literal_scope_name in scope
    ):
        if refname_scope_name in scope:
            # defname name
            defname = view.substr(getCurrentScopeRegion(view, pos))
        else:
            # Text
            if marker_begin_scope_name in scope:
                pos += 1
            while pos >= 0 and view.substr(sublime.Region(pos, pos + 1)) in "[]":
                pos -= 1
            if not (
                marker_scope_name in scope
                or marker_image_scope_name in scope
                or marker_literal_scope_name in scope
            ):
                return (False, None, None)
            marker_text_end = findScopeFrom(view, pos, marker_text_end_scope_name) + 1
            if view.match_selector(
                marker_text_end, refname_start_scope_name
            ) and not view.match_selector(marker_text_end + 1, marker_end_scope_name):
                # of [Text][name] struct
                marker_pt = marker_text_end + 1
                marker_pt_end = findScopeFrom(view, marker_pt, marker_end_scope_name)
                defname = view.substr(sublime.Region(marker_pt, marker_pt_end))
            else:
                # of [Text] struct or [Text][] struct
                defname = view.substr(getCurrentScopeRegion(view, pos))
        return (True, False, defname)
    else:
        return (False, None, None)


class MdeReferenceJumpCommand(MdeTextCommand):
    """Jump between definition and reference."""

    def description(self):
        """Description for package control."""
        return "Jump between definition and reference"

    def run(self, edit):
        """Run command callback."""
        view = self.view
        edit_regions = []
        markers = getMarkers(view)
        refs = getReferences(view)
        missing_markers = []
        missing_refs = []
        for sel in view.sel():
            matched, is_definition, defname = get_reference(view, sel.begin())
            if matched:
                defname_key = defname.lower()
                if is_definition:
                    if defname_key in markers:
                        edit_regions.extend(markers[defname_key].regions)
                    else:
                        missing_markers.append(defname)
                else:
                    if defname_key in refs:
                        edit_regions.extend(refs[defname_key].regions)
                    else:
                        missing_refs.append(defname)
        if len(edit_regions) > 0:
            sels = view.sel()
            sels.clear()
            sels.add_all(edit_regions)
            view.show(edit_regions[0])
        if len(missing_refs) + len(missing_markers) > 0:
            # has something missing
            if len(missing_markers) == 0:
                sublime.status_message(
                    "The definition%s of %s cannot be found."
                    % ("" if len(missing_refs) == 1 else "s", ", ".join(missing_refs))
                )
            elif len(missing_refs) == 0:
                sublime.status_message(
                    "The marker%s of %s cannot be found."
                    % ("" if len(missing_markers) == 1 else "s", ", ".join(missing_markers))
                )
            else:
                sublime.status_message(
                    "The definition%s of %s and the marker%s of %s cannot be found."
                    % (
                        "" if len(missing_refs) == 1 else "s",
                        ", ".join(missing_refs),
                        "" if len(missing_markers) == 1 else "s",
                        ", ".join(missing_markers),
                    )
                )


class MdeReferenceJumpContextCommand(MdeReferenceJumpCommand):
    """Jump between definition and reference. Used in context menu."""

    def is_visible(self):
        """Return True if cursor is on a marker or reference."""
        return MdeReferenceJumpCommand.is_visible(self) and any(
            get_reference(self.view, sel.begin())[0] for sel in self.view.sel()
        )


def is_url(contents):
    """Return if contents contains an URL."""
    re_match_urls = re.compile(
        r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""",
        re.DOTALL,
    )
    m = re_match_urls.search(contents)
    return True if m else False


def mangle_url(url):
    """Mangle URL for links."""
    url = url.strip()
    if re.match(r"^([a-z0-9-]+\.)+\w{2,4}", url, re.IGNORECASE):
        url = "http://" + url
    return url


def append_reference_link(edit, view, name, url):
    r"""Detect if file ends with \n."""
    if view.substr(view.size() - 1) == "\n":
        nl = ""
    else:
        nl = "\n"
    # Append the new reference link to the end of the file
    edit_position = view.size() + len(nl) + 1
    view.insert(edit, view.size(), "{0}[{1}]: {2}\n".format(nl, name, url))
    return sublime.Region(edit_position, edit_position + len(name))


def suggest_default_link_name(name, link, image):
    """Suggest default link name in camel case, if `name` is small.

    Args:
        name (str): An existing name, used as a fallback
        link (str): The link href
        image (bool): Whether the link points to an image or not. Used for fallback.

    Returns:
        str: A suggested reference name in CamelCase, or `name`.
    """
    ret = ""
    # string.punctuation minus -.:;<=>_
    no_punctuation = str.maketrans("", "", "!\"#$%&'()*+,/?@[\\]^`{|}~")
    name_segs = name.translate(no_punctuation).split()
    if len(name_segs) > 1:
        for word in name_segs:
            ret += word.capitalize()
            if len(ret) > 30:
                break
        return ("image" if image else "") + ret
    elif len(name) < 4:
        try:
            parseresult = urllib.parse.urlparse(re.sub(r"/$", "", link))
            doc_name = parseresult.path.split("/")[-1]
            if doc_name:
                return doc_name
            elif parseresult.netloc:
                return parseresult.netloc
        except Exception as e:
            print("Couldn't parse url", name, image, e)
            return name
    return name


def check_for_link(view, link):
    """Check if the link already defined. Return the name if so."""
    links_by_name = getReferences2(view)
    names_by_link = {v: k for k, v in links_by_name.items()}
    return names_by_link.get(link)


class MdeReferenceNewReferenceCommand(MdeTextCommand):
    """Create a new reference."""

    def run(self, edit, image=False):
        """Run command callback."""
        view = self.view
        edit_regions = []
        contents = sublime.get_clipboard().strip()
        link = mangle_url(contents) if is_url(contents) else ""
        suggested_name = ""
        if len(link) > 0:
            # If link already exists, reuse existing reference
            suggested_link_name = suggested_name = check_for_link(view, link)
        for sel in view.sel():
            text = view.substr(sel)
            if not suggested_name:
                suggested_link_name = suggest_default_link_name(text, link, image)
                suggested_name = suggested_link_name if suggested_link_name != text else ""
            edit_position = sel.end() + 3
            if image:
                edit_position += 1
                view.replace(edit, sel, "![" + text + "][" + suggested_name + "]")
            else:
                view.replace(edit, sel, "[" + text + "][" + suggested_name + "]")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(suggested_name)))
        if len(edit_regions) > 0:
            selection = view.sel()
            selection.clear()
            reference_region = append_reference_link(edit, view, suggested_link_name, link)
            selection.add(reference_region)
            selection.add_all(edit_regions)


class MdeReferenceNewInlineLinkCommand(MdeTextCommand):
    """Create a new inline link."""

    def run(self, edit, image=False):
        """Run command callback."""
        view = self.view
        contents = sublime.get_clipboard().strip()
        link = mangle_url(contents) if is_url(contents) else ""
        link = link.replace("$", "\\$")
        if image:
            view.run_command(
                "insert_snippet", {"contents": "![${1:$SELECTION}](${2:" + link + "})"}
            )
        else:
            view.run_command("insert_snippet", {"contents": "[${1:$SELECTION}](${2:" + link + "})"})


class MdeReferenceNewInlineImageCommand(MdeTextCommand):
    """Create a new inline image."""

    def run(self, edit):
        """Run command callback."""
        self.view.run_command("mde_reference_new_inline_link", {"image": True})


class MdeReferenceNewImageCommand(MdeTextCommand):
    """Create a new image."""

    def run(self, edit):
        """Run command callback."""
        self.view.run_command("mde_reference_new_reference", {"image": True})


def get_next_footnote_marker(view):
    """Get the number of the next footnote."""
    refs = getReferences(view)

    footnotes = []
    for ref in refs:
        if ref[0] == "^":
            try:
                footnotes.append(int(ref[1:]))
            except ValueError:
                pass

    def target_loc(num):
        return (num - 1) % len(footnotes)

    for i in range(len(footnotes)):
        footnote = footnotes[i]
        tl = target_loc(footnote)
        # footnotes = [1 2 {4} 5], i = 2, footnote = 4, tl = 3
        while tl != i:
            target_fn = footnotes[tl]
            ttl = target_loc(target_fn)
            # target_fn = 5, ttl = 0
            if ttl != tl or target_fn > footnote:
                footnotes[i], footnotes[tl] = footnotes[tl], footnotes[i]
                tl, footnote = ttl, target_fn
                # [1 2 {5} 4]
            else:
                break
    for i in range(len(footnotes)):
        if footnotes[i] != i + 1:
            return i + 1
    return len(footnotes) + 1


class MdeReferenceNewFootnoteCommand(MdeTextCommand):
    """Create a new footnote."""

    def run(self, edit):
        """Run command callback."""
        view = self.view
        markernum = get_next_footnote_marker(view)
        markernum_str = "[^%s]" % markernum
        for sel in view.sel():
            startloc = sel.end()
            if bool(view.size()):
                targetloc = view.find(r"(\s|$)", startloc).begin()
            else:
                targetloc = 0
            view.insert(edit, targetloc, markernum_str)
        if len(view.sel()) > 0:
            view.show(view.size())
            view.insert(edit, view.size(), "\n" + markernum_str + ": ")
            view.sel().clear()
            view.sel().add(sublime.Region(view.size(), view.size()))


class MdeReferenceDeleteReferenceCommand(MdeTextCommand):
    """Delete a reference."""

    def run(self, edit):
        """Run command callback."""
        view = self.view
        edit_regions = []
        markers = getMarkers(view)
        refs = getReferences(view)
        for sel in view.sel():
            matched, is_definition, defname = get_reference(view, sel.begin())
            if matched:
                defname_key = defname.lower()
                if defname_key in markers:
                    for marker in markers[defname_key].regions:
                        if defname[0] == "^":
                            edit_regions.append(
                                sublime.Region(marker.begin() - 1, marker.end() + 1)
                            )
                        else:
                            left = findScopeFrom(
                                view, marker.begin(), marker_begin_scope_name, True
                            )
                            if left > 0 and view.substr(sublime.Region(left - 1, left)) == "!":
                                edit_regions.append(sublime.Region(left - 1, left + 1))
                            else:
                                edit_regions.append(sublime.Region(left, left + 1))
                            if view.match_selector(marker.end(), marker_text_end_scope_name):
                                if (
                                    view.substr(sublime.Region(marker.end() + 1, marker.end() + 2))
                                    == "["
                                ):
                                    # [Text][]
                                    right = findScopeFrom(
                                        view, marker.end(), marker_end_scope_name, False
                                    )
                                    edit_regions.append(sublime.Region(marker.end(), right + 1))
                                else:
                                    # [Text]
                                    edit_regions.append(
                                        sublime.Region(marker.end(), marker.end() + 1)
                                    )
                            else:
                                # [Text][name]
                                right = findScopeFrom(
                                    view, marker.begin(), marker_text_end_scope_name, True
                                )
                                edit_regions.append(sublime.Region(right, marker.end() + 1))
                if defname_key in refs:
                    for ref in refs[defname_key].regions:
                        edit_regions.append(view.full_line(ref.begin()))

        if len(edit_regions) > 0:
            sel = view.sel()
            sel.clear()
            sel.add_all(edit_regions)

            def delete_all(index):
                if index == 0:
                    view.run_command("left_delete")

            view.window().show_quick_panel(
                ["Delete the References", "Preview the Changes"], delete_all, sublime.MONOSPACE_FONT
            )


class MdeReferenceOrganizeCommand(MdeTextCommand):
    """Sort and report all references."""

    def run(self, edit):
        """Run command callback."""
        view = self.view

        # reorder
        markers = getMarkers(view)
        reference_order = sorted(
            markers.keys(), key=lambda marker: min(markers[marker].regions, key=lambda reg: reg.a).a
        )
        reference_order = dict(zip(reference_order, range(0, len(reference_order))))

        refs = getReferences(view)
        flatrefs = []
        flatfns = []
        sel = view.sel()
        sel.clear()
        for name in refs:
            for link_reg in refs[name].regions:
                line_reg = view.full_line(link_reg)
                if name[0] == "^":
                    flatfns.append((name, view.substr(line_reg).strip("\n")))
                else:
                    flatrefs.append((name, view.substr(line_reg).strip("\n")))
                sel.add(line_reg)

        sorting_funcs = {
            "reference_order": lambda x: reference_order[x[0].lower()]
            if x[0].lower() in reference_order
            else 9999,
            "alphabetical": lambda x: x[0].lower(),
            "numeric": lambda x: [
                int(p) if p.isnumeric() else p for p in re.split(r"[ _.-]", x[0].lower())
            ],
        }
        settings = view.settings()

        flatfns.sort(key=operator.itemgetter(0))
        flatrefs.sort(
            key=sorting_funcs[settings.get("mde.ref_organize_sort", "reference_order")],
            reverse=settings.get("mde.ref_organize_sort_reverse", False),
        )

        view.run_command("left_delete")
        if view.size() >= 2 and view.substr(sublime.Region(view.size() - 2, view.size())) == "\n\n":
            view.erase(edit, sublime.Region(view.size() - 1, view.size()))
        for fn_tuple in flatfns:
            view.insert(edit, view.size(), fn_tuple[1])
            view.insert(edit, view.size(), "\n")
        view.insert(edit, view.size(), "\n")

        for ref_tuple in flatrefs:
            view.insert(edit, view.size(), ref_tuple[1])
            view.insert(edit, view.size(), "\n")

        # delete duplicate / report conflict
        sel.clear()
        refs = getReferences(view)
        conflicts = {}
        unique_links = {}
        output = ""

        for name in refs:
            if name[0] == "^":
                continue
            n_links = len(refs[name].regions)
            if n_links > 1:
                for ref in refs[name].regions:
                    link_begin = findScopeFrom(view, ref.end(), ref_link_scope_name)
                    link = view.substr(getCurrentScopeRegion(view, link_begin))
                    if name in unique_links:
                        if link == unique_links[name]:
                            output += "%s has duplicate value of %s\n" % (refs[name].label, link)
                            sel.add(view.full_line(ref.begin()))
                        elif name in conflicts:
                            conflicts[name].append(link)
                        else:
                            conflicts[name] = [link]
                    else:
                        unique_links[name] = link

        # view.run_command("left_delete")

        for name in conflicts:
            output += "%s has conflict values: %s with %s\n" % (
                refs[name].label,
                unique_links[name],
                ", ".join(conflicts[name]),
            )

        # report missing
        refs = getReferences(view)
        lower_refs = [ref.lower() for ref in refs]
        missings = []
        for ref in refs:
            if ref not in reference_order:
                missings.append(refs[ref].label)
        if len(missings) > 0:
            if len(missings) > 1:
                noun, verb = "Definitions", "have"
            else:
                noun, verb = "Definition", "has"

            output += "Error: %s %s %s no reference\n" % (
                noun,
                repr(missings),
                verb,
            )

        missings = []
        for marker in markers:
            if marker not in lower_refs:
                missings.append(markers[marker].label)
        if len(missings) > 0:
            if len(missings) > 1:
                noun, verb = "References", "have"
            else:
                noun, verb = "Reference", "has"

            output += "Error: %s %s %s no definition\n" % (
                noun,
                repr(missings),
                verb,
            )

        # sel.clear()
        if len(output) == 0:
            output = "All references are well defined :)\n"

        output += "===================\n"

        def get_times_string(n):
            if n == 0:
                return "0 time"
            elif n == 1:
                return "1 time"
            else:
                return "%i times" % n

        output += "\n".join(
            (
                "[%s] is referenced %s"
                % (markers[m].label, get_times_string(len(markers[m].regions)))
            )
            for m in markers
        )

        window = view.window()
        output_panel = window.create_output_panel("mde")
        output_panel.run_command("erase_view")
        output_panel.run_command("append", {"characters": output})
        window.run_command("show_panel", {"panel": "output.mde"})


class MdeGatherMissingLinkMarkersCommand(MdeTextCommand):
    """Gather all missing references and creates them."""

    def run(self, edit):
        """Run command callback."""
        view = self.view
        refs = getReferences(view)
        markers = getMarkers(view)
        missings = []
        for marker in markers:
            if marker not in refs:
                missings.append(marker)
        if len(missings):
            # Remove all whitespace at the end of the file
            whitespace_at_end = view.find(r"\s*\z", 0)
            view.replace(edit, whitespace_at_end, "\n")

            # If there is not already a reference list at the end, insert a new line at the end
            if not view.find(r"\n\s*\[[^\]]*\]:.*\s*\z", 0):
                view.insert(edit, view.size(), "\n")

            for link in missings:
                view.insert(edit, view.size(), "[%s]: \n" % link)


def convert2ref(view, edit, link_span, name, omit_name=False):
    """Convert single link to reference."""
    view.sel().clear()
    link = view.substr(sublime.Region(link_span.a + 1, link_span.b - 1))
    if omit_name:
        view.replace(edit, link_span, "[]")
        link_span = sublime.Region(link_span.a + 1, link_span.a + 1)
        offset = len(link)
    else:
        view.replace(edit, link_span, "[%s]" % name)
        link_span = sublime.Region(link_span.a + 1, link_span.a + 1 + len(name))
        offset = len(link) - len(name)
    view.sel().add(link_span)
    view.show_at_center(link_span)

    link_for_name = getReferences2(view).get(name)
    if link_for_name:
        if link_for_name != link:
            raise Exception("Tried to insert a different link with the same name")
        else:
            # Skip insertion (no need, name already exists with same link)
            return 0  # No insertion, no offset.
    else:
        _viewsize = view.size()
        view.insert(edit, _viewsize, "[%s]: %s\n" % (name, link))
        reference_span = sublime.Region(_viewsize + 1, _viewsize + 1 + len(name))
        view.sel().add(reference_span)

        return offset


class MdeConvertInlineLinkToReferenceCommand(MdeTextCommand):
    """Convert an inline link to reference."""

    def is_visible(self):
        """Return True if cursor is on a marker or reference."""
        for sel in self.view.sel():
            if self.view.match_selector(sel.b, "meta.link.inline"):
                return True
        return False

    def run(self, edit, name=None):
        """Run command callback."""
        view = self.view
        re_link_or_embed = r"\[([^\]]+)\]\((?!#)([^\)]+)\)"

        # Remove all whitespace at the end of the file
        whitespace_at_end = view.find(r"\s*\z", 0)
        view.replace(edit, whitespace_at_end, "\n")

        # If there is not already a reference list at the end, insert a new line at the end
        if not view.find(r"\n\s*\[[^\]]*\]:.*\s*\z", 0):
            view.insert(edit, view.size(), "\n")

        link_spans = []
        links_by_name = getReferences2(view)
        names_by_link = {v: k for k, v in links_by_name.items()}

        for sel in view.sel():
            if not view.match_selector(sel.b, "meta.link.inline"):
                continue
            start = findScopeFrom(view, sel.b, marker_begin_scope_name, backwards=True)
            end = findScopeFrom(view, sel.b, marker_end_scope_name) + 1
            text = view.substr(sublime.Region(start, end))
            m = re.match(re_link_or_embed, text)
            if m is None:
                continue
            text = m.group(1)
            link = m.group(2)
            link_span = sublime.Region(start + m.span(2)[0] - 1, start + m.span(2)[1] + 1)
            if is_url(link):
                link = mangle_url(link)
            if len(link) <= 0:
                continue
            # Set name based on link.
            # If link already exists, reuse existing reference
            name = None
            if names_by_link.get(link):
                name = names_by_link.get(link)
            else:
                # Link is not referenced. Generate name.
                is_image = view.substr(start - 1) == "!" if start > 0 else False
                name = name or suggest_default_link_name(text, link, is_image)
            # If name is already in use by a different link, change our name.
            i = 1
            name_ = name
            while links_by_name.get(name, link) != link and i < 999:
                i += 1
                name = name_ + str(i)

            link_spans.append((link_span, name, name == text))
            # Update local dict for batch operations
            links_by_name[name] = link
            names_by_link[link] = name

        offset = 0
        for span, name, name_is_text in link_spans:
            _link_span = sublime.Region(span.a + offset, span.b + offset)
            offset -= convert2ref(view, edit, _link_span, name, name_is_text)


class MdeConvertInlineLinksToReferencesCommand(MdeTextCommand):
    """Convert inline links to references."""

    def run(self, edit):
        """Run command callback."""
        view = self.view
        pattern = r"(?<=\]\()(?!#)([^\)]+)(?=\))"

        _sel = []
        for sel in view.sel():
            _sel.append(sel)
        view.sel().clear()
        view.sel().add_all(view.find_all(pattern))
        view.run_command("mde_convert_inline_link_to_reference")


class MdeAddNumberedReferenceDefinitionCommand(MdeTextCommand):
    """
    The `mde_add_numbered_reference_definition` command adds a new line with a numbered reference
    definition if the current line's one contains a label. Otherwise the current line is deleted.

    The added reference uses the next bigger number which does not yet exist in the document.

    The command works for unnamed, named definitions as well as for footnotes.

    ```markdown
    [^1]: footnote
    [1]: unnamed_reference
    [name1]: named_reference
    ```

    **Note:**

    Implementation uses regexp functions as Markdown syntax doesn't scope reference definitions atm.
    A future change might make use of `view.find_by_selector("...")` to create the list of existing
    references.
    """

    REFERENCE_DEFINITION_PATTERN = r"^([ \t]{0,3})\[(.*?)(\d+)\]:[ \t]*(\S)?"

    def run(self, edit):
        view = self.view
        pattern = re.compile(self.REFERENCE_DEFINITION_PATTERN)

        refs = {}

        # find all existing reference definitions and group them by name
        for ref in view.find_all(self.REFERENCE_DEFINITION_PATTERN):
            _, name, num, _ = pattern.search(view.substr(ref)).groups()
            refs.setdefault(name, set()).add(int(num))

        for sel in view.sel():
            line = view.line(sel)
            match = pattern.search(view.substr(line))
            if not match:
                continue

            indent, name, num, label = match.groups()
            if label:
                # calculate next none-existing reference number
                num = int(num)
                while num in refs.get(name, {}):
                    num += 1
                view.insert(edit, sel.begin(), "\n%s[%s%d]: " % (indent, name, num))
            else:
                view.erase(edit, line)


def shorten(string, n):
    return string if len(string) <= n else string[: n - 1] + "…"


if hasattr(sublime, "KIND_ID_MARKUP"):

    class MdeReferenceCompletionsProvider(MdeViewEventListener):
        KIND_REFERENCE = (sublime.KIND_ID_MARKUP, "R", "Ref")

        re_reflinks = re.compile(
            r"^[ \t>]*\[(?P<id>[^\^][^\]]*)\]:\s+(?P<link>\S*)(?:\s+(?P<desc>.*))?$",
            re.MULTILINE,
        )

        def on_query_completions(self, _, locations):
            if not self.view.match_selector(
                locations[0],
                "text.html.markdown meta.link.reference, "
                "text.html.markdown meta.image.reference",
            ):
                return None

            completions = []
            for ref in self.view.find_by_selector("meta.link.reference.def"):
                for match in self.re_reflinks.finditer(self.view.substr(ref)):
                    completions.append(
                        sublime.CompletionItem(
                            trigger=match.group("id"),
                            completion=match.group("id"),
                            completion_format=sublime.COMPLETION_FORMAT_TEXT,
                            kind=self.KIND_REFERENCE,
                            annotation=shorten((match.group("link") or "No link"), 30),
                            details=(match.group("desc") or "No title").strip(" \t\v\f\r\n'\""),
                        )
                    )
            return sublime.CompletionList(
                completions,
                sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS,
            )

else:

    class MdeReferenceCompletionsProvider(MdeViewEventListener):
        re_reflinks = re.compile(
            r"^[ \t>]*\[(?P<id>[^\^][^\]]*)\]:\s+(?P<link>\S*)(?:\s+(?P<desc>.*))?$",
            re.MULTILINE,
        )

        def on_query_completions(self, _, locations):
            if not self.view.match_selector(
                locations[0],
                "text.html.markdown meta.link.reference, "
                "text.html.markdown meta.image.reference",
            ):
                return None

            completions = []
            for ref in self.view.find_by_selector("meta.link.reference.def"):
                for match in self.re_reflinks.finditer(self.view.substr(ref)):
                    completions.append(
                        [
                            match.group("id")
                            + "\t"
                            + shorten((match.group("link") or "No link"), 30),
                            match.group("id"),
                        ]
                    )

            return (
                completions,
                sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS,
            )
