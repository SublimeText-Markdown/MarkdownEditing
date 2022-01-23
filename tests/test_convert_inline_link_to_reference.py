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
        self.setCaretTo(2, 10)
        self._test_convert_link1()

    def test_convert_link1_with_caret_in_url(self):
        self.setCaretTo(2, 25)
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
        self.setCaretTo(3, 2)
        self._test_convert_link2()

    def test_convert_link2_with_caret_in_url(self):
        self.setCaretTo(3, 9)
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
        self.setCaretTo(4, 7)
        self._test_convert_link3()

    def test_convert_link3_with_caret_in_url(self):
        self.setCaretTo(4, 27)
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
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.setCaretTo(3, 2)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.setCaretTo(4, 7)
        self.view.run_command("mde_convert_inline_link_to_reference")
        # try to convert image
        self.setCaretTo(5, 50)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self._test_convert_all()

    def test_convert_all(self):
        self.view.run_command("mde_convert_inline_links_to_references")
        self._test_convert_all()

    def _test_convert_all(self):
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


class TestConvertInlineLinkToReferenceReuseExistingDefinitions(DereferrablePanelTestCase):
    def test_reuse_indented_definition(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

               [GitHub]: https://github.com
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

               [GitHub]: https://github.com
            """
        )

    def test_reuse_definition_with_multiple_spaces(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]:       https://github.com
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]:       https://github.com
            """
        )

    def test_reuse_multiline_definition(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]:
                https://github.com
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]:
                https://github.com
            """
        )

    def test_reuse_definition_with_quoted_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]: https://github.com "the page description"
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]: https://github.com "the page description"
            """
        )

    def test_reuse_multiline_definition_with_quoted_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]:
                https://github.com
                "the page description"
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]:
                https://github.com
                "the page description"
            """
        )

    def test_reuse_definition_with_parenthesed_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]: https://github.com (the page description)
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]: https://github.com (the page description)
            """
        )

    def test_reuse_multiline_definition_with_parenthesed_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]:
                https://github.com
                (the page description)
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]:
                https://github.com
                (the page description)
            """
        )

    def test_reuse_definition_with_angled_url(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]: <https://github.com>
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]: <https://github.com>
            """
        )

    def test_reuse_indended_definition_with_angled_url(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

               [GitHub]:    <https://github.com>
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

               [GitHub]:    <https://github.com>
            """
        )

    def test_reuse_multiline_definition_with_angled_url(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]:
            <https://github.com>
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]:
            <https://github.com>
            """
        )

    def test_reuse_definition_with_angled_url_and_quoted_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]: <https://github.com> "the page description"
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]: <https://github.com> "the page description"
            """
        )

    def test_reuse_definition_with_angled_url_and_parenthesed_description(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com) link.

            [GitHub]: <https://github.com> (the page description)
            """
        )
        self.setCaretTo(2, 10)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][] link.

            [GitHub]: <https://github.com> (the page description)
            """
        )

    def test_reuse_definition_in_blockquote(self):
        self.setBlockText(
            """
            > First [GitHub][] link.
            > Second [GitHub](https://github.com) link.
            >
            > [GitHub]: https://github.com
            """
        )
        self.setCaretTo(2, 12)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            > First [GitHub][] link.
            > Second [GitHub][] link.
            >
            > [GitHub]: https://github.com
            """
        )

    def test_reuse_definition_in_listitem(self):
        self.setBlockText(
            """
            - First [GitHub][] link.
              - Second [GitHub](https://github.com) link.

                [GitHub]: https://github.com
            """
        )
        self.setCaretTo(2, 15)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            - First [GitHub][] link.
              - Second [GitHub][] link.

                [GitHub]: https://github.com
            """
        )

    def test_reuse_definition_quoted_in_listitem(self):
        self.setBlockText(
            """
            > - First [GitHub][] link.
            >   - Second [GitHub](https://github.com) link.
            >
            >     [GitHub]: https://github.com
            """
        )
        self.setCaretTo(2, 15)
        self.view.run_command("mde_convert_inline_link_to_reference")
        self.assertEqualBlockText(
            """
            > - First [GitHub][] link.
            >   - Second [GitHub][] link.
            >
            >     [GitHub]: https://github.com
            """
        )

    def test_reuse_definition_but_create_new_for_differnt_url(self):
        self.setBlockText(
            """
            First [GitHub][] link.
            Second [GitHub](https://github.com/user) link.
            Third [GitHub](https://github.com) link.

            [GitHub]: https://github.com
            """
        )
        self.view.run_command("mde_convert_inline_links_to_references")
        self.assertEqualBlockText(
            """
            First [GitHub][] link.
            Second [GitHub][GitHub2] link.
            Third [GitHub][] link.

            [GitHub]: https://github.com
            [GitHub2]: https://github.com/user
            """
        )
