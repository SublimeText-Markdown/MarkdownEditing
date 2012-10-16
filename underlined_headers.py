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

			dashes = self.view.substr(dashes_line)
			m = SETEXT_DASHES_RE.match(dashes)
			if m:
				fix_dashes(self.view, edit, text_line, dashes_line)


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

		for text_line, dashes_line in itertools.izip(prev_lines, lines):
			dashes_text = self.view.substr(dashes_line)
			m = SETEXT_DASHES_RE.match(dashes_text)
			if m:
				fix_dashes(self.view, edit, text_line, dashes_line)
