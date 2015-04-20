
import sublime
import sublime_plugin
import re


class mddef(object):
    flag = 0
    gid = 0
    desc = "default"
    finish = False

    def __init__(self, settings, view):
        self.settings = settings

    def __str__(self):
        return self.__class__.__name__.upper() + ' - ' + self.desc


class md001(mddef):
    flag = re.M
    desc = 'Header levels should only increment by one level at a time'
    locator = r'^#{1,6}(?!#)'

    lastMatch = None

    def test(self, text, s, e):
        ret = {}
        if self.lastMatch:
            n1 = len(self.lastMatch)
            n2 = e - s
            if n2 > n1:
                if n2 != n1 + 1:
                    ret[s] = 'expected %d, %d found' % (n1 + 1, n2)
        self.lastMatch = text[s: e]
        return ret


class md002(mddef):
    flag = re.M
    desc = 'First header should be a h1 header'
    locator = r'^(?:#{1,6}(?!#))|(?:-+|=+)'

    def test(self, text, s, e):
        ret = {}
        # print (text[s:e])
        self.finish = True
        if re.match(r'#{1,6}(?!#)', text[s:e]):
            if e - s != 1:
                ret[s] = 'level %d found' % (e - s)
        elif re.match('-+|=+', text[s:e]):
            if not re.match('=+', text[s:e]):
                ret[s] = 'level 2 found'
        return ret


class md003(mddef):
    flag = re.M
    desc = 'Header style'
    locator = r'^((?:-+|=+)|(?:#{1,6}(?!#).*))$'
    gid = 1

    ratx = r'^(#{1,6}(?!#)).*$'
    ratxc = r'^(#{1,6}(?!#)).*?(#+)$'
    rsetext = r'[\-\=]+'

    def test(self, text, s, e):
        ret = {}
        t = text[s:e]
        if self.settings == 'atx':
            if not re.match(self.ratx, t) or\
                    re.match(self.ratxc, t):
                ret[s] = 'expected atx'
        elif self.settings == 'atx_closed':
            if not re.match(self.ratxc, t):
                ret[s] = 'expected atx_closed'
        elif self.settings == 'setext':
            if not re.match(self.rsetext, t):
                ret[s] = 'expected setext'
        elif self.settings == 'any':
            if re.match(self.ratx, t):
                if re.match(self.ratxc, t):
                    self.settings = 'atx_closed'
                else:
                    self.settings = 'atx'
                return self.test(text, s, e)
            elif re.match(self.rsetext, t):
                self.settings = 'setext'
                return self.test(text, s, e)
        return ret


class md004(mddef):
    flag = re.M
    desc = 'Unordered list style'
    locator = r'^([ ]{0,3})[*+-](?=\s)'
    eol = r'^(?=\S)'
    gid = 1
    lastSym = None
    lastpos = -1

    def __init__(self, settings, view):
        super(md004, self).__init__(settings, view)
        self.lvs = [None, None, None]

    def test(self, text, s, e):
        if self.lastpos > s:
            return {}
        self.lastpos = e

        ret = {}
        lvstack = []
        basenspaces = e - s
        sym = text[e:e + 1]
        (ans, exp) = self.testsingle(sym)
        if ans is None:
            (ans, exp) = self.testcyc(sym, -1)
            if ans is False:
                ret[e] = '%s expected, %s found' % (exp, sym)
        elif ans is False:
            ret[e] = '%s expected, %s found' % (exp, sym)

        rest = text[e + 1:]
        mr = re.search(self.eol, rest, re.M)
        end = mr.start(0) if mr else len(rest)
        block = rest[:end]
        # print('====')
        # print(block)
        # print('====')
        mrs = re.finditer(r'^(\s*)([*\-+])\s+', block, re.M)
        for mr in mrs:
            # print('====')
            # print(mr.group(2))
            # print('====')
            self.lastpos = e + 1 + mr.end(0)
            sym = mr.group(2)
            (ans, exp) = self.testsingle(sym)
            if ans is None:
                # cyclic or any
                nspaces = len(mr.group(1))
                if nspaces < basenspaces:
                    lv = 0
                elif nspaces == basenspaces:
                    lv = -1
                else:
                    while len(lvstack) > 0:
                        n = lvstack.pop()
                        if n < nspaces:
                            lvstack.append(n)
                            break
                    lv = len(lvstack)
                    lvstack.append(nspaces)
                # print(sym)
                # print(lv)
                # print(self.lvs)
                (ans, exp) = self.testcyc(sym, lv)
                if ans is False:
                    ret[e + 1 +
                        mr.start(2)] = '%s expected, %s found' % (exp, sym)
            else:
                if not ans:
                    ret[e + 1 +
                        mr.start(2)] = '%s expected, %s found' % (exp, sym)
        return ret

    def testsingle(self, sym):
        if self.settings == 'asterisk':
            return (sym == '*', '*')
        if self.settings == 'plus':
            return (sym == '+', '+')
        if self.settings == 'dash':
            return (sym == '-', '-')
        if self.settings == 'single':
            if self.lastSym:
                return (self.lastSym == sym, self.lastSym)
            else:
                self.lastSym = sym
                return (True, None)
        return (None, None)

    def testcyc(self, sym, lv):
        if self.settings == 'cyclic':
            if self.lvs[lv]:
                return (self.lvs[lv] == sym, self.lvs[lv])
            else:
                if (sym not in self.lvs):
                    self.lvs[lv] = sym
                    return (True, None)
                else:
                    return (False, None)
        if self.settings == 'any':
            if self.lvs[lv]:
                return self.lvs[lv] == sym
            else:
                self.lvs[lv] = sym
                return (True, None)
        return (None, None)


class md005(mddef):
    flag = re.M
    desc = 'Inconsistent indentation for list items at the same level'
    locator = r'^([ ]{0,3})[*+-](?=\s)'
    eol = r'^(?=\S)'
    gid = 1
    lastpos = -1

    def __init__(self, settings, view):
        super(md005, self).__init__(settings, view)
        self.lvs = {}

    def spacecheck(self, lv, nspaces):
        if lv in self.lvs:
            if self.lvs[lv] != nspaces:
                return (False, self.lvs[lv])
        else:
            self.lvs[lv] = nspaces
        return (True, nspaces)

    def test(self, text, s, e):
        # print(self.lastpos)
        if self.lastpos > s:
            return {}
        self.lastpos = e

        ret = {}
        lvstack = []
        sym = text[e:e + 1]
        nspaces = e - s
        basenspaces = e - s
        (ans, exp) = self.spacecheck(-1, nspaces)
        if not ans:
            ret[s] = '%s expected, %s found' % (exp, nspaces)

        rest = text[e + 1:]
        mr = re.search(self.eol, rest, re.M)
        end = mr.start(0) if mr else len(rest)
        block = rest[:end]
        # print('====')
        # print(block)
        # print('====')
        mrs = re.finditer(r'^( *)([*\-+])\s+', block, re.M)
        for mr in mrs:
            # print('----')
            # print(mr.group(2))
            # print('----')
            self.lastpos = e + 1 + mr.end(0)
            sym = mr.group(2)
            nspaces = len(mr.group(1))
            if nspaces < basenspaces:
                lv = 0
            elif nspaces == basenspaces:
                lv = -1
            else:
                while len(lvstack) > 0:
                    n = lvstack.pop()
                    if n < nspaces:
                        lvstack.append(n)
                        break
                lv = len(lvstack)
                lvstack.append(nspaces)
            (ans, exp) = self.spacecheck(lv, nspaces)
            if ans is False:
                ret[e + 1 +
                    mr.start(2)] = '%s expected, %s found' % (exp, nspaces)
        return ret


class md006(mddef):
    flag = re.M
    desc = 'Consider starting bulleted lists at the beginning of the line'
    locator = r'^([ ]{0,3})[*+-](?=\s)'
    eol = r'^(?=\S)'
    gid = 1
    lastpos = -1

    def test(self, text, s, e):
        # print(self.lastpos)
        if self.lastpos > s:
            return {}
        self.lastpos = e

        ret = {}
        lvstack = []
        sym = text[e:e + 1]
        nspaces = e - s
        if nspaces > 0:
            ret[s] = '%d found' % nspaces

        rest = text[e + 1:]
        mr = re.search(self.eol, rest, re.M)
        end = mr.start(0) if mr else len(rest)
        block = rest[:end]
        # print('====')
        # print(block)
        # print('====')
        mrs = re.finditer(r'^(\s*)([*\-+])\s+', block, re.M)
        for mr in mrs:
            # print('----')
            # print(mr.group(2))
            # print('----')
            self.lastpos = e + 1 + mr.end(0)
        return ret


class md007(mddef):
    flag = re.M
    desc = 'Unordered list indentation'
    locator = r'^([ ]{0,3})[*+-](?=\s)'
    eol = r'^(?=\S)'
    gid = 1
    lastpos = -1

    def __init__(self, settings, view):
        if settings == 0:
            self.settings = view.settings().get("tab_size", 4)
        else:
            self.settings = settings

    def spacecheck(self, nspaces):
        return (nspaces % self.settings == 0, '%d*n' % self.settings)

    def test(self, text, s, e):
        # print(self.lastpos)
        if self.lastpos > s:
            return {}
        self.lastpos = e

        ret = {}
        nspaces = e - s
        (ans, exp) = self.spacecheck(nspaces)
        if not ans:
            ret[s] = '%s expected, %s found' % (exp, nspaces)

        rest = text[e + 1:]
        mr = re.search(self.eol, rest, re.M)
        end = mr.start(0) if mr else len(rest)
        block = rest[:end]
        # print('====')
        # print(block)
        # print('====')
        mrs = re.finditer(r'^( *)([*\-+])\s+', block, re.M)
        for mr in mrs:
            # print('----')
            # print(mr.group(2))
            # print('----')
            self.lastpos = e + 1 + mr.end(0)
            nspaces = len(mr.group(1))
            (ans, exp) = self.spacecheck(nspaces)
            if ans is False:
                ret[e + 1 +
                    mr.start(2)] = '%s expected, %s found' % (exp, nspaces)
        return ret


class md009(mddef):
    flag = re.M
    desc = 'Trailing spaces'
    locator = r' +$'

    def test(self, text, s, e):
        return {s: '%d spaces' % (e - s)}


class md010(mddef):
    flag = re.M
    desc = 'Hard tabs'
    locator = r'\t'

    def test(self, text, s, e):
        return {s: 'hard tab found'}


class md011(mddef):
    flag = re.M
    desc = 'Reversed link syntax'
    locator = r'\(.*?\)\[.*?\]'

    def test(self, text, s, e):
        return {s: 'reversed link syntax found'}


class md012(mddef):
    desc = 'Multiple consecutive blank lines'
    locator = r'\n{3,}'

    def test(self, text, s, e):
        return {s + 1: '%d blank lines' % (e - s - 1)}


class md013(mddef):
    flag = re.M
    desc = 'Line length'
    locator = r'^.+$'

    def __init__(self, settings, view):
        if settings == 0:
            self.settings = view.settings().get("wrap_width", 80)
        else:
            self.settings = settings

    def test(self, text, s, e):
        t = text[s:e]
        if not re.match(r'^[ ]*[>\+\-\*].+$', t):
            if e - s > self.settings:
                return {s: '%d characters' % (e - s)}
        return {}


class md018(mddef):
    flag = re.M
    desc = 'No space after hash on atx style header'
    locator = r'^#{1,6}(?![#\s]).*(?<!#)$'

    def test(self, text, s, e):
        return {s: 'no space'}


class md019(mddef):
    flag = re.M
    desc = 'Multiple spaces after hash on atx style header'
    locator = r'^#{1,6}(?=\s{2,}).*(?<!#)$'

    def test(self, text, s, e):
        return {s: 'too many spaces'}


class md020(mddef):
    flag = re.M
    desc = 'No space inside hashes on closed atx style header'
    locator = r'^(#{1,6}(?!#))(.*?)(#+)$'
    gid = 2

    def test(self, text, s, e):
        t = text[s:e]
        if t[0] != ' ':
            return {s: 'no space on the left'}
        elif t[-1] != ' ':
            return {s: 'no space on the right'}
        return {}


class md021(mddef):
    flag = re.M
    desc = 'Multiple spaces inside hashes on closed atx style header'
    locator = r'(#{1,6}(?!#))(.*?)(#+)'
    gid = 2

    def test(self, text, s, e):
        t = text[s:e]
        if len(t) > 1 and ((t[0] == ' ' and t[1] == ' ') or
                           (t[-1] == ' ' and t[-2] == ' ')):
            return {s: 'too many spaces'}
        return {}


class md022(mddef):
    flag = re.M
    desc = 'Headers should be surrounded by blank lines'
    locator = r'^((?:-+|=+)|(?:#{1,6}(?!#).*))$'

    def test(self, text, s, e):
        if re.match(r'-+|=+', text[s:e]):
            st = text.rfind('\n', 0, s - 1)
            s = st + 1

        if s > 1 and text[s - 2] != '\n':
            return {s: 'blank line required before this line'}

        if e < len(text) - 2 and text[e + 1] != '\n':
            return {s: 'blank line required after this line'}
        return {}


class md023(mddef):
    flag = re.M
    desc = 'Headers must start at the beginning of the line'
    locator = r'^( +)((?:-+|=+)|(?:#{1,6}(?!#).*))$'
    gid = 1

    def test(self, text, s, e):
        return {s: '%d spaces found' % (e - s)}


class md024(mddef):
    flag = re.M
    desc = 'Multiple headers with the same content'
    locator = r'^((?:-+|=+)|(?:#{1,6}(?!#).*))$'
    gid = 1

    ratx = r'(#{1,6}(?!#)) *(.*?) *$'
    ratxc = r'(#{1,6}(?!#)) *(.*?) *(#+)$'

    def __init__(self, settings, view):
        super(md024, self).__init__(settings, view)
        self.storage = []

    def test(self, text, s, e):
        ret = {}
        title = text[s:e]
        if re.match(r'-+|=+', title):
            st = text.rfind('\n', 0, s - 1)
            title = text[st + 1: s - 1]
        else:
            mr = re.match(self.ratxc, title)
            if mr:
                title = mr.group(2)
            else:
                mr = re.match(self.ratx, title)
                title = mr.group(2)
        if title in self.storage:
            ret[s] = '%s duplicated' % repr(title)
        else:
            self.storage.append(title)
        return ret


class md025(mddef):
    flag = re.M
    desc = 'Multiple top level headers in the same document'
    locator = r'^(={3,}|#(?!#).*)$'
    count = 0

    def test(self, text, s, e):
        ret = {}
        self.count += 1
        if self.count > 1:
            ret[s] = '%d found' % self.count
        return ret


class md026(mddef):
    flag = re.M
    desc = 'Trailing punctuation in header'
    locator = r'^((?:-+|=+)|(?:#{1,6}(?!#).*))$'
    gid = 1

    ratx = r'(#{1,6}(?!#)) *(.*?) *$'
    ratxc = r'(#{1,6}(?!#)) *(.*?) *?(#+)$'

    def test(self, text, s, e):
        ret = {}
        title = text[s:e]
        if re.match(r'-+|=+', title):
            st = text.rfind('\n', 0, s - 1)
            title = text[st + 1: s - 1]
        else:
            mr = re.match(self.ratxc, title)
            if mr:
                title = mr.group(2)
            else:
                mr = re.match(self.ratx, title)
                title = mr.group(2)
        if title[-1] in self.settings:
            ret[s] = '%s found' % repr(title[-1])
        return ret


class md027(mddef):
    flag = re.M
    desc = 'Multiple spaces after blockquote symbol'
    locator = r'^ {0,4}> {2,}'

    def test(self, text, s, e):
        return {s: 'too many spaces'}


class md028(mddef):
    flag = re.M
    desc = 'Blank line inside blockquote'
    locator = r'^ {0,4}>.*$'
    lastQuoteEnd = None

    def test(self, text, s, e):
        ret = {}
        if self.lastQuoteEnd:
            if re.match(r'(\n *){2,}', text[self.lastQuoteEnd:s]):
                ret[self.lastQuoteEnd] = 'found one'
        self.lastQuoteEnd = e
        return ret


class md029(mddef):
    flag = re.M
    desc = 'Ordered list item prefix'
    locator = r'^ {0,3}([0-9]+)\.(?=\s)'
    gid = 1
    eol = r'^\s*$'
    lastpos = -1

    def test(self, text, s, e):
        if self.lastpos > s:
            return {}
        self.lastpos = e

        sym = text[s:e]
        if self.settings == 'any':
            if sym == '1':
                style = None
            else:
                style = 'ordered'
        elif self.settings == 'one':
            style = 'one'
        elif self.settings == 'ordered':
            style = 'ordered'

        rest = text[e + 1:]
        mr = re.search(self.eol, rest, re.M)
        end = mr.start(0) if mr else len(rest)
        block = rest[:end]
        mrs = re.finditer(r'^ {0,3}([0-9]+)\.(?=\s)', block, re.M)
        lastSym = sym
        ret = {}
        for mr in mrs:
            self.lastpos = e + 1 + mr.end(0)
            sym = mr.group(1)
            if style is None:
                if sym == '1':
                    style = 'one'
                else:
                    style = 'ordered'

            if style == 'one':
                if sym != '1':
                    ret[mr.start(
                        1) + e + 1] = '%s found, \'1\' expected' % repr(sym)
            else:
                if int(sym) != int(lastSym) + 1:
                    ret[mr.start(1) + e + 1] = ('%s found, \'%d\' expected' %
                                                (repr(sym), int(lastSym) + 1))
                lastSym = sym
        return ret


class MarkdownLintCommand(sublime_plugin.TextCommand):

    blockdef = []
    scope_block = 'markup.raw.block.markdown'

    def run(self, edit):
        mddef = globals()['mddef']
        text = self.view.substr(sublime.Region(0, self.view.size()))
        st = self.view.settings().get('mde.lint', {})
        uselist = []
        disablelist = st['disable']
        for cl in mddef.__subclasses__():
            if cl.__name__ not in disablelist:
                uselist.append(cl)
        result = []
        for mddef in uselist:
            r = self.test(mddef(st[mddef.__name__] if mddef.__name__ in st
                                else None, self.view), text)
            result.extend(r)
        sublime.status_message('MarkdownLint: %d error(s) found' % len(result))
        if len(result) > 0:
            result = sorted(result, key=lambda t: t[0])
            outputtxt = ''
            for t in result:
                (row, col) = self.view.rowcol(t[0])
                outputtxt += 'line %d: %s, %s\n' % (row + 1, t[1], t[2])
            window = sublime.active_window()
            output = window.create_output_panel("mde")
            output.run_command('erase_view')
            output.run_command('append', {'characters': outputtxt})
            window.run_command("show_panel", {"panel": "output.mde"})

    def test(self, tar, text):
        loc = tar.locator
        # print(tar)
        # print(repr(loc))
        it = re.finditer(loc, text, tar.flag)
        ret = []
        for mr in it:
            # print('find %d,%d' % (mr.start(tar.gid), mr.end(tar.gid)))
            if self.scope_block in self.view.scope_name(mr.start(0)):
                if tar.__class__ not in self.blockdef:
                    continue
            ans = tar.test(text, mr.start(tar.gid), mr.end(tar.gid))
            for p in ans:
                ret.append((p, str(tar), ans[p]))
                # (row, col) = self.view.rowcol(p)
                # print('line %d: %s, %s' % (row + 1, tar, ans[p]))

            # if not ans:
            #     ret = False
            #     (row, col) = self.view.rowcol(mr.start(tar.gid))
            #     print('line %d: %s ' % (row + 1, tar))
            if tar.finish:
                break

        return ret
