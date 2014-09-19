
import sublime
import sublime_plugin
import re


class mddef(object):
    flag = 0
    gid = 0

    def __init__(self, settings):
        pass

    def __str__(self):


class md001_atx(mddef):
    flag = re.M
    desc = 'Header levels should only increment by one level at a time'
    locator = '^#{1,6}(?!#)'

    lastMatch = None

    def test(self, text, s, e):
        if self.lastMatch:
            n1 = len(self.lastMatch)
            n2 = e - s
            return n2 == n1 + 1 if n2 > n1 else True
        self.lastMatch = text[s: e]
        return True


class md001_setext(mddef):
    flag = re.M
    desc = 'Header levels should only increment by one level at a time'
    locator = '^([\-\=]+)$'
    gid = 1

    lastMatch = None

    def test(self, text, s, e):
        if self.lastMatch and re.match('\-+', self.lastMatch):
            return re.match('\=+', text[s: e]) is None
        self.lastMatch = text[s: e]
        return True


class md002_atx(mddef):
    flag = re.S
    desc = 'First header should be a h1 header'
    locator = '^.*?(#{1,6}(?!#))'
    gid = 1

    def test(self, text, s, e):
        return e - s == 1


class md002_setext(mddef):
    flag = re.S
    desc = 'First header should be a h1 header'
    locator = '^([\-\=]+)$'
    gid = 1

    def test(self, text, s, e):
        return re.match('\=+', text[s: e]) is not None


class md003(mddef):
    flag = re.M
    desc = 'Header style'
    locator = '^([\-\=]+)|(#{1,6}(?!#).*)$'
    gid = 1

    def __init__(self, settings):
        self.settings = settings

    def test(self, text, s, e):
        t = text[s:e]
        if self.settings == 'atx':
            if not re.match('(#{1,6}(?!#)).*', t) or\
                    re.match('(#{1,6}(?!#)).*((?<!#)\1)', t):
                return False
        elif self.settings == 'atx_closed':
            if not re.match('(#{1,6}(?!#)).*((?<!#)\1)', t):
                return False
        elif self.settings == 'setext':
            if not re.match('[\-\=]+', t):
                return False
        elif self.settings == 'any':
            if re.match('(#{1,6}(?!#)).*', t):
                if re.match('(#{1,6}(?!#)).*((?<!#)\1)', t):
                    self.settings = 'atx_closed'
                else:
                    self.settings = 'atx'
            elif re.match('[\-\=]+', t):
                self.settings = 'setext'
            return self.test(text, s, e)
        return True


class LintCommand(sublime_plugin.TextCommand):

    deflist = [md001_atx, md001_setext, md002_atx, md002_setext]

    def run(self, edit):
        text = self.view.substr(sublime.Region(0, self.view.size()))
        st = self.view.settings().get('lint')
        print('================lint start================')
        for mddef in self.deflist:
            self.test(mddef(st[mddef.__name__] if mddef.__name__ in st
                            else None), text)
        print('=================lint end=================')

    def test(self, tar, text):
        loc = tar.locator
        print(tar.desc)
        print(repr(loc))
        it = re.finditer(loc, text, tar.flag)
        ret = True
        for mr in it:
            # print('find %d,%d' % (mr.start(tar.gid), mr.end(tar.gid)))
            ans = tar.test(text, mr.start(tar.gid), mr.end(tar.gid))
            if not ans:
                ret = False
                (row, col) = self.view.rowcol(mr.start(tar.gid))
                print('line %d: %s ' %
                      (row + 1, tar.__class__.__name__.upper()) + tar.desc)

        return ret
