from MarkdownEditing.tests import DereferrablePanelTestCase


class JoinListItemsTestCase(DereferrablePanelTestCase):

    def test_join_two_ordered_list_items_with_dot(self):
        self.setBlockText(
            """
            1. item 1
            2. item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1. item 1 item 2
            """
        )

    def test_join_two_ordered_list_items_with_paren(self):
        self.setBlockText(
            """
            1) item 1
            2) item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 item 2
            """
        )

    def test_join_two_unordered_list_items(self):
        self.setBlockText(
            """
            * item 1
            * item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            * item 1 item 2
            """
        )

    def test_join_ordered_list_with_subitems(self):
        self.setBlockText(
            """
            1) item 1
              - foo
              - bar
            2) item 2
            """
        )
        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1
              - foo bar
            2) item 2
            """
        )

        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1
              - foo bar item 2
            """
        )

        self.setCaretTo(1, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_subitems(self):
        self.setBlockText(
            """
            * item 1
              - foo
              - bar
            * item 2
            """
        )
        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            * item 1
              - foo bar
            * item 2
            """
        )

        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            * item 1
              - foo bar item 2
            """
        )

        self.setCaretTo(1, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            * item 1 foo bar item 2
            """
        )

    def test_join_ordered_list_with_subitems_multi_caret(self):
        self.setBlockText(
            """
            1) item 1
              - foo
              - bar
            2) item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_subitems_multi_caret(self):
        self.setBlockText(
            """
            * item 1
              - foo
              - bar
            * item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            * item 1 foo bar item 2
            """
        )
    def test_join_ordered_list_with_text_multi_caret(self):
        self.setBlockText(
            """
            1) item 1
               foo
               bar
            2) item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_text_multi_caret(self):
        self.setBlockText(
            """
            * item 1
              bar
              baz
            * item
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        * item 1 bar baz item
        """
    )

    def test_join_selected_ordered_list_with_subitems(self):
        self.setBlockText(
            """
            1) item 1
              - foo
              - bar
            2) item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 foo bar item 2
            """
        )

    def test_join_selected_unordered_list_with_subitems(self):
        self.setBlockText(
            """
            * item 1
              - foo
              - bar
            * item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        * item 1 foo bar item 2
        """
    )

    def test_join_selected_ordered_list_with_text(self):
        self.setBlockText(
            """
            1) item 1
               foo
               bar
            2) item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            1) item 1 foo bar item 2
            """
        )

    def test_join_selected_unordered_list_with_text(self):
        self.setBlockText(
            """
            * item 1
              bar
              baz
            * item
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        * item 1 bar baz item
        """
    )

    def test_join_lines_keep_ordered_list_bullet(self):
        self.setBlockText(
            """
            # Heading


            1. item 1
            """
        )
        self.setCaretTo(3, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            # Heading

            1. item 1
            """
        )

    def test_join_lines_keep_unordered_list_bullet(self):
        self.setBlockText(
            """
            # Heading


            * item 1
            """
        )
        self.setCaretTo(3, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            # Heading

            * item 1
            """
        )


class JoinBlockQuoteLinesTestCase(DereferrablePanelTestCase):

    def test_join_selected_text_level1(self):
        self.setBlockText(
            """
            > foo
            > bar
            > baz
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > foo bar baz
            """
        )

    def test_join_selected_text_level2(self):
        self.setBlockText(
            """
            > > foo
            > > bar
            > baz
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > > foo bar baz
        """
    )

    def test_join_two_ordered_list_items_with_dot(self):
        self.setBlockText(
            """
            > 1. item 1
            > 2. item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1. item 1 item 2
            """
        )

    def test_join_two_ordered_list_items_with_paren(self):
        self.setBlockText(
            """
            > 1) item 1
            > 2) item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 item 2
            """
        )

    def test_join_two_unordered_list_items(self):
        self.setBlockText(
            """
            > * item 1
            > * item 2
            """
        )
        self.setCaretTo(1, 8)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > * item 1 item 2
            """
        )

    def test_join_ordered_list_with_subitems(self):
        self.setBlockText(
            """
            > 1) item 1
            >   - foo
            >   - bar
            > 2) item 2
            """
        )
        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1
            >   - foo bar
            > 2) item 2
            """
        )

        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1
            >   - foo bar item 2
            """
        )

        self.setCaretTo(1, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_subitems(self):
        self.setBlockText(
            """
            > * item 1
            >   - foo
            >   - bar
            > * item 2
            """
        )
        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > * item 1
            >   - foo bar
            > * item 2
            """
        )

        self.setCaretTo(2, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > * item 1
            >   - foo bar item 2
            """
        )

        self.setCaretTo(1, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > * item 1 foo bar item 2
        """
    )

    def test_join_ordered_list_with_subitems_multi_caret(self):
        self.setBlockText(
            """
            > 1) item 1
            >   - foo
            >   - bar
            > 2) item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_subitems_multi_caret(self):
        self.setBlockText(
            """
            > * item 1
            >   - foo
            >   - bar
            > * item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > * item 1 foo bar item 2
        """
    )

    def test_join_ordered_list_with_text_multi_caret(self):
        self.setBlockText(
            """
            > 1) item 1
            >    foo
            >    bar
            > 2) item 2
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 foo bar item 2
            """
        )

    def test_join_unordered_list_with_text_multi_caret(self):
        self.setBlockText(
            """
            > * item 1
            >   bar
            >   baz
            > * item
            """
        )
        self.setCaretTo(1, 3)
        self.addCaretAt(2, 3)
        self.addCaretAt(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > * item 1 bar baz item
        """
    )

    def test_join_selected_ordered_list_with_subitems(self):
        self.setBlockText(
            """
            > 1) item 1
            >   - foo
            >   - bar
            > 2) item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 foo bar item 2
            """
        )

    def test_join_selected_unordered_list_with_subitems(self):
        self.setBlockText(
            """
            > * item 1
            >   - foo
            >   - bar
            > * item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > * item 1 foo bar item 2
        """
    )

    def test_join_selected_ordered_list_with_text(self):
        self.setBlockText(
            """
            > 1) item 1
            >    foo
            >    bar
            > 2) item 2
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > 1) item 1 foo bar item 2
            """
        )

    def test_join_selected_unordered_list_with_text(self):
        self.setBlockText(
            """
            > * item 1
            >   bar
            >   baz
            > * item
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
        """
        > * item 1 bar baz item
        """
    )

    def test_join_lines_keep_ordered_list_bullet_if_caret_after_blockquote_sign(self):
        self.setBlockText(
            """
            > # Heading
            >\x20
            >\x20
            > 1. item 1
            """
        )
        self.setCaretTo(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > # Heading
            >\x20
            > 1. item 1
            """
        )

    def test_join_lines_keep_unordered_list_bullet_if_caret_after_blockquote_sign(self):
        self.setBlockText(
            """
            > # Heading
            >\x20
            >\x20
            > * item 1
            """
        )
        self.setCaretTo(3, 3)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > # Heading
            >\x20
            > * item 1
            """
        )

    def test_join_lines_keep_ordered_list_bullet_if_caret_at_bol(self):
        self.setBlockText(
            """
            > # Heading
            >\x20
            >\x20
            > 1. item 1
            """
        )
        self.setCaretTo(3, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > # Heading
            >\x20
            > 1. item 1
            """
        )

    def test_join_lines_keep_unordered_list_bullet_if_caret_at_bol(self):
        self.setBlockText(
            """
            > # Heading
            >\x20
            >\x20
            > * item 1
            """
        )
        self.setCaretTo(3, 1)
        self.view.run_command("mde_join_lines")
        self.assertEqualBlockText(
            """
            > # Heading
            >\x20
            > * item 1
            """
        )
