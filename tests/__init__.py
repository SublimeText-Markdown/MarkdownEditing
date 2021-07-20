import sublime

from textwrap import dedent
from unittesting import DeferrableTestCase


class DereferrablePanelTestCase(DeferrableTestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up global test environment once for all tests owned by this class.
        """
        cls.window = sublime.active_window()
        cls.view = cls.window.create_output_panel("MarkdownUnitTests", unlisted=True)
        settings = cls.view.settings()
        settings.set("detect_indentation", False)
        settings.set("fold_buttons", False)
        settings.set("gutter", False)
        settings.set("line_numbers", False)
        settings.set("scroll_past_end", False)
        settings.set("syntax", "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax")
        settings.set("word_wrap", False)
        cls.view = cls.window.create_output_panel("MarkdownUnitTests", unlisted=True)

    @classmethod
    def tearDownClass(cls):
        """
        Teardown global test environment once all tests finished.
        """
        cls.view = cls.window.destroy_output_panel("MarkdownUnitTests")

    @classmethod
    def setCaretTo(cls, row, col):
        """
        Move caret to given point

        :param row:  The natural 1-based row number. 1=first row
        :param col:  The natural 1-based column number. 1=first column
        """
        pt = cls.textPoint(row, col)
        cls.view.sel().clear()
        cls.view.sel().add(sublime.Region(pt, pt))

    @classmethod
    def setBlockText(cls, text):
        """
        Replace everything with given block text

        :param text:  The triple quoted block text to put into scratch view.
        """
        cls.setText(dedent(text.strip()))

    @classmethod
    def setText(cls, text):
        """
        Replace everything with given text

        :param text:  The text to put into scratch view.
        """
        cls.view.run_command("select_all")
        cls.view.run_command("right_delete")
        cls.view.run_command("insert", {"characters": text})

    @classmethod
    def getRow(cls, row):
        """
        Return row's text content.

        :param row:  The natural 1-based row number. 1=first row
        """
        return cls.view.substr(cls.view.line(cls.textPoint(row, 0)))

    @classmethod
    def textPoint(cls, row, col):
        """
        Return textpoint for given row,col coordinats.

        :param row:  The natural 1-based row number. 1=first row
        :param col:  The natural 1-based column number. 1=first column
        """
        return cls.view.text_point(row - 1, col - 1)
