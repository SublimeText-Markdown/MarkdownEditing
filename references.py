import sublime
import sublime_plugin
import re
from MarkdownEditing.mdeutils import *

refname_scope_name = "constant.other.reference.link.markdown"
definition_scope_name = "meta.link.reference.def.markdown"
marker_scope_name = "meta.link.reference.markdown"
marker_image_scope_name = "meta.image.reference.markdown"
ref_link_scope_name = "markup.underline.link.markdown"
marker_begin_scope_name = "punctuation.definition.string.begin.markdown"
marker_text_end_scope_name = "punctuation.definition.string.end.markdown"
marker_text_scope_name = "string.other.link.title.markdown"
refname_start_scope_name = "punctuation.definition.constant.begin.markdown"
marker_end_scope_name = "punctuation.definition.constant.end.markdown"


def hasScope(scope_name, to_find):
    return to_find in scope_name.split(" ")


def getMarkers(view, name=''):
    # returns {name -> Region}
    markers = []
    name = re.escape(name)
    if name == '':
        markers.extend(view.find_all(r"(?<=\]\[)([^\]]+)(?=\])", 0))  # ][???]
        markers.extend(view.find_all(r"(?<=\[)([^\]]*)(?=\]\[\])", 0))  # [???][]
        markers.extend(view.find_all(r"(?<=\[)(\^[^\]]+)(?=\])", 0))  # [^???]
    else:
        # ][name]
        markers.extend(view.find_all(r"(?<=\]\[)(%s)(?=\])" % name, 0))
        markers.extend(view.find_all(r"(?<=\[)(%s)(?=\]\[\])" % name, 0))  # [name][]
        if name[0] == '^':
            # [(^)name]
            markers.extend(view.find_all(r"(?<=\[)(%s)(?=\])" % name, 0))
    regions = []
    for x in markers:
        scope_name = view.scope_name(x.begin())
        if (hasScope(scope_name, refname_scope_name) or hasScope(scope_name, marker_text_scope_name)) and \
                not hasScope(view.scope_name(x.begin()), definition_scope_name):
            regions.append(x)
    ids = {}
    for reg in regions:
        name = view.substr(reg).strip()
        if name in ids:
            ids[name].append(reg)
        else:
            ids[name] = [reg]
    return ids


def getReferences(view, name=''):
    # returns {name -> Region}
    refs = []
    name = re.escape(name)
    if name == '':
        refs.extend(view.find_all(r"(?<=^\[)([^\]]+)(?=\]:)", 0))
    else:
        refs.extend(view.find_all(r"(?<=^\[)(%s)(?=\]:)" % name, 0))
    regions = refs
    ids = {}
    for reg in regions:
        name = view.substr(reg).strip()
        if name in ids:
            ids[name].append(reg)
        else:
            ids[name] = [reg]
    return ids


def isMarkerDefined(view, name):
    # returns bool
    return len(getReferences(view, name)) > 0


def getCurrentScopeRegion(view, pt):
    # returns Region
    scope = view.scope_name(pt)
    l = pt
    while l > 0 and view.scope_name(l-1) == scope:
        l -= 1
    r = pt
    while r < view.size() and view.scope_name(r) == scope:
        r += 1
    return sublime.Region(l, r)


def findScopeFrom(view, pt, scope, backwards=False):
    # returns number
    if backwards:
        while pt >= 0 and not hasScope(view.scope_name(pt), scope):
            pt -= 1
    else:
        while pt < view.size() and not hasScope(view.scope_name(pt), scope):
            pt += 1
    return pt


class ReferenceJumpCommand(MDETextCommand):
    # reference_jump command

    def run(self, edit):
        view = self.view
        edit_regions = []
        markers = getMarkers(view)
        refs = getReferences(view)
        missingMarkers = []
        missingRefs = []
        for sel in view.sel():
            scope = view.scope_name(sel.begin()).split(" ")
            if definition_scope_name in scope:
                if refname_scope_name in scope:
                    # Definition name
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()))
                elif refname_start_scope_name in scope:
                    # Starting "["
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()+1))
                else:
                    # URL
                    marker_pt = findScopeFrom(view, sel.begin(), refname_scope_name, True)
                    defname = view.substr(getCurrentScopeRegion(view, marker_pt))
                if defname in markers:
                    edit_regions.extend(markers[defname])
                else:
                    missingMarkers.append(defname)
            elif marker_scope_name in scope or marker_image_scope_name in scope:
                if refname_scope_name in scope:
                    # defname name
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()))
                else:
                    # Text
                    marker_pt = findScopeFrom(view, sel.begin(), refname_scope_name)
                    defname = view.substr(getCurrentScopeRegion(view, marker_pt))
                if defname in refs:
                    edit_regions.extend(refs[defname])
                else:
                    missingRefs.append(defname)
        if len(edit_regions) > 0:
            sels = view.sel()
            sels.clear()
            sels.add_all(edit_regions)
        if len(missingRefs) + len(missingMarkers) > 0:
            # has something missing
            if len(missingMarkers) == 0:
                sublime.status_message("The definition%s of %s cannot be found." %
                                       ("" if len(missingRefs) == 1 else "s", ", ".join(missingRefs)))
            elif len(missingRefs) == 0:
                sublime.status_message("The marker%s of %s cannot be found." %
                                       ("" if len(missingMarkers) == 1 else "s", ", ".join(missingMarkers)))
            else:
                sublime.status_message("The definition%s of %s and the marker%s of %s cannot be found." %
                                       ("" if len(missingRefs) == 1 else "s", ", ".join(missingRefs),
                                        "" if len(missingMarkers) == 1 else "s", ", ".join(missingMarkers)))


def is_url(contents):
    # Returns if contents contains an URL
    re_match_urls = re.compile(r"""((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.‌​][a-z]{2,4}/)(?:[^\s()<>]+|(([^\s()<>]+|(([^\s()<>]+)))*))+(?:(([^\s()<>]+|(‌​([^\s()<>]+)))*)|[^\s`!()[]{};:'".,<>?«»“”‘’]))""", re.DOTALL)
    m = re_match_urls.search(contents)
    return True if m else False


def mangle_url(url):
    url = url.strip()
    if re.match(r'^([a-z0-9-]+\.)+\w{2,4}', url, re.IGNORECASE):
        url = 'http://' + url
    return url


def append_reference_link(edit, view, name, url):
    # Detect if file ends with \n
    if view.substr(view.size() - 1) == '\n':
        nl = ''
    else:
        nl = '\n'
    # Append the new reference link to the end of the file
    edit_position = view.size() + len(nl) + 1
    view.insert(edit, view.size(), '{0}[{1}]: {2}\n'.format(nl, name, url))
    return sublime.Region(edit_position, edit_position + len(name))


def suggest_default_link_name(name, image):
    # Camel case impl.
    ret = ''
    name_segs = name.split()
    if len(name_segs) > 1:
        for word in name_segs:
            ret += word.capitalize()
            if len(ret) > 30:
                break
        return ('image' if image else 'link') + ret
    else:
        return name


def check_for_link(view, link):
    refs = getReferences(view)
    link = link.strip()
    for name in refs:
        link_begin = findScopeFrom(view, refs[name][0].begin(), ref_link_scope_name)
        reg = getCurrentScopeRegion(view, link_begin)
        found_link = view.substr(reg).strip()
        if found_link == link:
            return name
    return None


class ReferenceNewReferenceCommand(MDETextCommand):
    # reference_new_reference command

    def run(self, edit, image=False):
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
                suggested_link_name = suggest_default_link_name(text, image)
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


class ReferenceNewInlineLinkCommand(MDETextCommand):
    # reference_new_inline_link command

    def run(self, edit, image=False):
        view = self.view
        edit_regions = []
        suggested_name = False
        contents = sublime.get_clipboard().strip()
        link = mangle_url(contents) if is_url(contents) else ""
        for sel in view.sel():
            text = view.substr(sel)
            edit_position = sel.end() + 3
            if image:
                edit_position += 1
                view.replace(edit, sel, "![" + text + "](" + link + ")")
            else:
                view.replace(edit, sel, "[" + text + "](" + link + ")")
            edit_regions.append(sublime.Region(edit_position, edit_position + len(link)))
        if len(edit_regions) > 0:
            selection = view.sel()
            selection.clear()
            selection.add_all(edit_regions)


class ReferenceNewInlineImage(MDETextCommand):
    # reference_new_inline_image command

    def run(self, edit):
        self.view.run_command("reference_new_inline_link", {"image": True})


class ReferenceNewImage(MDETextCommand):
    # reference_new_image command

    def run(self, edit):
        self.view.run_command("reference_new_reference", {"image": True})


def get_next_footnote_marker(view):
    refs = getReferences(view)
    footnotes = [int(ref[1:]) for ref in refs if view.substr(refs[ref][0])[0] == "^"]

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
        if footnotes[i] != i+1:
            return i+1
    return len(footnotes) + 1


class ReferenceNewFootnote(MDETextCommand):
    # reference_new_footnote command

    def run(self, edit):
        view = self.view
        markernum = get_next_footnote_marker(view)
        markernum_str = '[^%s]' % markernum
        for sel in view.sel():
            startloc = sel.end()
            if bool(view.size()):
                targetloc = view.find('(\s|$)', startloc).begin()
            else:
                targetloc = 0
            view.insert(edit, targetloc, markernum_str)
        if len(view.sel()) > 0:
            view.insert(edit, view.size(), '\n' + markernum_str + ': ')
            view.sel().clear()
            view.sel().add(sublime.Region(view.size(), view.size()))


class ReferenceDeleteReference(MDETextCommand):
    # reference_delete_reference command

    def run(self, edit):
        view = self.view
        edit_regions = []
        markers = getMarkers(view)
        refs = getReferences(view)
        for sel in view.sel():
            scope = view.scope_name(sel.begin()).split(" ")
            if definition_scope_name in scope:
                if refname_scope_name in scope:
                    # Definition name
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()))
                elif refname_start_scope_name in scope:
                    # Starting "["
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()+1))
                else:
                    # URL
                    marker_pt = findScopeFrom(view, sel.begin(), refname_scope_name, True)
                    defname = view.substr(getCurrentScopeRegion(view, marker_pt))
            elif marker_scope_name in scope or marker_image_scope_name in scope:
                if refname_scope_name in scope:
                    # defname name
                    defname = view.substr(getCurrentScopeRegion(view, sel.begin()))
                else:
                    # Text
                    marker_pt = findScopeFrom(view, sel.begin(), refname_scope_name)
                    defname = view.substr(getCurrentScopeRegion(view, marker_pt))
            else:
                defname = None
            if defname and defname in markers:
                for marker in markers[defname]:
                    if defname[0] == "^":
                        edit_regions.append(sublime.Region(marker.begin()-1, marker.end()+1))
                    else:
                        l = findScopeFrom(view, marker.begin(), marker_begin_scope_name, True)
                        if l > 0 and view.substr(sublime.Region(l-1, l)) == "!":
                            edit_regions.append(sublime.Region(l-1, l+1))
                        else:
                            edit_regions.append(sublime.Region(l, l+1))
                        r = findScopeFrom(view, marker.begin(), marker_text_end_scope_name, True)
                        edit_regions.append(sublime.Region(r, marker.end()+1))
            if defname in refs:
                for ref in refs[defname]:
                    edit_regions.append(view.full_line(ref.begin()))

        if len(edit_regions) > 0:
            sel = view.sel()
            sel.clear()
            sel.add_all(edit_regions)

            def delete_all(index):
                if index == 0:
                    view.run_command("left_delete")
            view.window().show_quick_panel(["Delete the References", "Preview the Changes"], delete_all, sublime.MONOSPACE_FONT)


class ReferenceOrganize(MDETextCommand):
    # reference_organize command

    def run(self, edit):
        view = self.view

        # reorder
        refs = getReferences(view)
        flatrefs = []
        flatfns = []
        sel = view.sel()
        sel.clear()
        for name in refs:
            for link_reg in refs[name]:
                line_reg = view.full_line(link_reg)
                if name[0] == "^":
                    flatfns.append((name, view.substr(line_reg)))
                else:
                    flatrefs.append((name, view.substr(line_reg)))
                sel.add(line_reg)
        flatfns.sort(key=lambda r: r[0])
        flatrefs.sort(key=lambda r: r[0])
        view.run_command("left_delete")
        if view.size() >= 2 and view.substr(sublime.Region(view.size()-2, view.size())) == "\n\n":
            view.erase(edit, sublime.Region(view.size()-1, view.size()))
        for fn_tuple in flatfns:
            view.insert(edit, view.size(), fn_tuple[1])
        view.insert(edit, view.size(), "\n")
        for ref_tuple in flatrefs:
            view.insert(edit, view.size(), ref_tuple[1])

        # delete duplicate / report conflict
        sel.clear()
        refs = getReferences(view)
        conflicts = {}
        unique_links = {}
        output = ""

        for name in refs:
            if name[0] == '^':
                continue
            n_links = len(refs[name])
            if n_links > 1:
                for ref in refs[name]:
                    link_begin = findScopeFrom(view, ref.end(), ref_link_scope_name)
                    link = view.substr(getCurrentScopeRegion(view, link_begin))
                    if name in unique_links:
                        if link == unique_links[name]:
                            output += "%s has duplicate value of %s\n" % (name, link)
                            sel.add(view.full_line(ref.begin()))
                        elif name in conflicts:
                            conflicts[name].append(link)
                        else:
                            conflicts[name] = [link]
                    else:
                        unique_links[name] = link

        # view.run_command("left_delete")

        for name in conflicts:
            output += "%s has conflict values: %s with %s\n" % (name, unique_links[name], ", ".join(conflicts[name]))

        # report missing
        refs = getReferences(view)
        markers = getMarkers(view)
        print(markers)
        missings = []
        for ref in refs:
            if ref not in markers:
                missings.append(ref)
        if len(missings) > 0:
            output += "definition [%s] %s no reference\n" % (", ".join(missings), "have" if len(missings) > 1 else "has")

        missings = []
        for marker in markers:
            if marker not in refs:
                missings.append(marker)
        if len(missings) > 0:
            output += "[%s] %s no definition\n" % (", ".join(missings), "have" if len(missings) > 1 else "has")

        # sel.clear()
        if len(output) > 0:
            window = view.window()
            output_panel = window.create_output_panel("mde")
            output_panel.run_command('erase_view')
            output_panel.run_command('append', {'characters': output})
            window.run_command("show_panel", {"panel": "output.mde"})
