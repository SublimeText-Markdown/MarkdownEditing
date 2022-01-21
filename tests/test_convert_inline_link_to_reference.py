from MarkdownEditing.tests import DereferrablePanelTestCase


class TestConvertInlineLinkToReference(DereferrablePanelTestCase):

    def setUp(self):
        self.setBlockText(
            """
            # Test 1
            First [GitHub](https://github.com) inline link.
            [Issues](https://github.com/user/repo/issues) go here.
            [GitHub](https://github.com)
            Just another paragraph with ![screenshot](assets/img/screenshot.png).
            """
        )

    def test_convert_link1_with_caret_in_description(self):
        self.setCaretTo(3, 10)
        self._test_convert_link1()

    def test_convert_link1_with_caret_in_url(self):
        self.setCaretTo(3, 25)
        self._test_convert_link1()

    def _test_convert_link1(self):
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            # Test 1
            First [GitHub][] inline link.
            [Issues](https://github.com/user/repo/issues) go here.
            [GitHub](https://github.com)
            Just another paragraph with ![screenshot](assets/img/screenshot.png).
            [GitHub]: https://github.com
            """
        )

    def test_convert_link2_with_caret_in_description(self):
        self.setCaretTo(5, 2)
        self._test_convert_link2()

    def test_convert_link2_with_caret_in_url(self):
        self.setCaretTo(5, 9)
        self._test_convert_link2()

    def _test_convert_link2(self):
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            # Test 1
            First [GitHub](https://github.com) inline link.
            [Issues][] go here.
            [GitHub](https://github.com)
            Just another paragraph with ![screenshot](assets/img/screenshot.png).
            [Issues]: https://github.com/user/repo/issues
            """
        )

    def test_convert_link3_with_caret_in_description(self):
        self.setCaretTo(7, 7)
        self._test_convert_link3()

    def test_convert_link3_with_caret_in_url(self):
        self.setCaretTo(7, 27)
        self._test_convert_link3()

    def _test_convert_link3(self):
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            # Test 1
            First [GitHub](https://github.com) inline link.
            [Issues](https://github.com/user/repo/issues) go here.
            [GitHub][]
            Just another paragraph with ![screenshot](assets/img/screenshot.png).
            [GitHub]: https://github.com
            """
        )

    def test_convert_link1_to_3(self):
        self.setCaretTo(3, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.setCaretTo(5, 2)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.setCaretTo(7, 7)
        self.view.run_command("mde_convert_inline_link_to_reference")
        # try to convert image
        self.setCaretTo(9, 50)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            # Test 1
            First [GitHub][] inline link.
            [Issues][] go here.
            [GitHub][]
            Just another paragraph with ![screenshot](assets/img/screenshot.png).
            [GitHub]: https://github.com
            [Issues]: https://github.com/user/repo/issues
            """
        )