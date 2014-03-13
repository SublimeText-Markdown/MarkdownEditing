"""Commands for working with with setext-style (underlined) Markdown headers.

Header dashes can be completed with <tab>. For example:

	This is an H2
	-<tab>

Becomes:

	This is an H2
	-------------

Inspired by the similar TextMate command.

Also adds "Fix Underlined Markdown Headers" to Tools > Command Palette. After modifying
header text, this command will re-align the underline dashes with the new text length.

"""
import sublime, sublime_plugin
import re, itertools

SETEXT_DASHES_RE = re.compile( r'''
	(?: =+ | -+ ) # A run of ---- or ==== underline characters.
	\s*           # Optional trailing whitespace.
	$             # Must fill the while line. Don't match "- list items"
	''', re.X )

SETEXT_HEADER_RE = re.compile( r'''
	^(.+)\n
	( =+ | -+ ) # A run of ---- or ==== underline characters.
	[ \t]*        # Optional trailing whitespace.
	$             # Must fill the while line. Don't match "- list items"
	''', re.X | re.M )

def fix_dashes(view, edit, text_region, dash_region):
	"""Replaces the underlined "dash" region of a setext header with a run of
	dashes or equal-signs that match the length of the header text."""

	if len(view.substr(text_region).strip()) == 0:
		# Ignore dashes not under text. They are HRs.
		return

	old_dashes = view.substr(dash_region)
	first_dash = old_dashes[0]
	new_dashes = first_dash * text_region.size()
	view.replace(edit, dash_region, new_dashes)


class CompleteUnderlinedHeaderCommand(sublime_plugin.TextCommand):
	"""If the current selection is looks like a setext underline of - or = ,
	then inserts enough dash characters to match the length of the previous
	(header text) line."""

	def run(self, edit):
		for region in self.view.sel():
			dashes_line = self.view.line(region)
			# Ignore first list
			if dashes_line.begin() == 0: continue

			text_line = self.view.line(dashes_line.begin() - 1)
			if text_line.begin() < 0: continue

			text = self.view.substr(text_line)
			dashes = self.view.substr(dashes_line)

			# ignore, text_line is a list item
			if text.lstrip().startswith("-") and len(dashes.strip()) < 2:
				settings = self.view.settings()
				use_spaces = bool(settings.get('translate_tabs_to_spaces'))
				tab_size = int(settings.get('tab_size', 8))
				indent_characters = '\t'
				if use_spaces:
					    indent_characters = ' ' * tab_size
				self.view.insert(edit, dashes_line.begin(), indent_characters)
				break

			m = SETEXT_DASHES_RE.match(dashes)
			if m:
				fix_dashes(self.view, edit, text_line, dashes_line)

	def is_enabled(self):
		return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))


class FixAllUnderlinedHeadersCommand(sublime_plugin.TextCommand):
	"""Searches for all setext headings resize them to match the preceding
	header text."""

	def description(self):
		# Used as the name for Undo.
		return 'Fix Underlined Markdown Headers'

	def run(self, edit):
		lines = self.view.split_by_newlines(sublime.Region(0, self.view.size()))
		if len(lines) < 2: return

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

	def is_enabled(self):
		return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))

class ConvertToAtxCommand(sublime_plugin.TextCommand):

	def run(self, edit, closed=False):
		regions =  list(self.view.sel())
		if len(regions) == 1 and regions[0].size() == 0:
			regions = [sublime.Region(0, self.view.size())]
		regions.reverse()
		for region in regions:
			txt = self.view.substr(region)
			matches = list(SETEXT_HEADER_RE.finditer(txt))
			matches.reverse()
			for m in matches:
				mreg = sublime.Region(region.begin()+m.start(), region.begin()+m.end())
				atx = "# "
				if '-' in m.group(2):
					atx = "#" + atx
				closing = atx[::-1] if closed else ""
				self.view.replace(edit, mreg, atx + m.group(1) + closing)

	def is_enabled(self):
		return bool(self.view.score_selector(self.view.sel()[0].a, "text.html.markdown"))
