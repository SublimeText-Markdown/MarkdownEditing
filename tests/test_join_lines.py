from MarkdownEditing.tests import DereferrablePanelTestCase


class JoinListItemsTestCase(DereferrablePanelTestCase):

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
        self.assertEqualText("1) item 1 foo bar item 2")

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
        self.assertEqualText("1) item 1 foo bar item 2")

    def test_join_selected_unordered_list_with_text(self):
        self.setBlockText(
            """
            * foo
              bar
              baz
            * item
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualText("* foo bar baz item")


class JoinBlockQuoteLinesTestCase(DereferrablePanelTestCase):

    def test_join_blockquote_text(self):
        self.setBlockText(
            """
            > foo
            > bar
            > baz
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualText("> foo bar baz")

    def test_join_blockquote2_text(self):
        self.setBlockText(
            """
            > > foo
            > > bar
            > baz
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualText("> > foo bar baz")

    def test_join_selected_unordered_list_with_text(self):
        self.setBlockText(
            """
            > * foo
            >   bar
            >   baz
            > * item
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualText("> * foo bar baz item")

        self.setBlockText(
            """
            > > * foo
            > >   bar
            > >   baz
            > > * item
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_join_lines")
        self.assertEqualText("> > * foo bar baz item")
