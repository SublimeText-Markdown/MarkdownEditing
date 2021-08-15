from MarkdownEditing.tests import DereferrablePanelTestCase


class MdeToggleTaskListItemTestCase(DereferrablePanelTestCase):

    def test_set_task_with_asterisk_done_col1(self):
        self._test_set_task_with_asterisk_done(1)

    def test_set_task_with_asterisk_done_col2(self):
        self._test_set_task_with_asterisk_done(2)

    def test_set_task_with_asterisk_done_col4(self):
        self._test_set_task_with_asterisk_done(4)

    def test_set_task_with_asterisk_done_col8(self):
        self._test_set_task_with_asterisk_done(8)

    def test_set_task_with_asterisk_done_col12(self):
        self._test_set_task_with_asterisk_done(12)

    def _test_set_task_with_asterisk_done(self, col):
        self.setBlockText(
            """
            * [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            * [X] task 1
            """
        )

    def test_set_task_with_asterisk_undone_col1(self):
        self._test_set_task_with_asterisk_undone(1)

    def test_set_task_with_asterisk_undone_col2(self):
        self._test_set_task_with_asterisk_undone(2)

    def test_set_task_with_asterisk_undone_col4(self):
        self._test_set_task_with_asterisk_undone(4)

    def test_set_task_with_asterisk_undone_col8(self):
        self._test_set_task_with_asterisk_undone(8)

    def test_set_task_with_asterisk_undone_col12(self):
        self._test_set_task_with_asterisk_undone(12)

    def _test_set_task_with_asterisk_undone(self, col):
        self.setBlockText(
            """
            * [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            * [ ] task 1
            """
        )

    def test_set_task_with_minus_done_col1(self):
        self._test_set_task_with_minus_done(1)

    def test_set_task_with_minus_done_col2(self):
        self._test_set_task_with_minus_done(2)

    def test_set_task_with_minus_done_col4(self):
        self._test_set_task_with_minus_done(4)

    def test_set_task_with_minus_done_col8(self):
        self._test_set_task_with_minus_done(8)

    def test_set_task_with_minus_done_col12(self):
        self._test_set_task_with_minus_done(12)

    def _test_set_task_with_minus_done(self, col):
        self.setBlockText(
            """
            - [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            - [X] task 1
            """
        )

    def test_set_task_with_minus_undone_col1(self):
        self._test_set_task_with_minus_undone(1)

    def test_set_task_with_minus_undone_col2(self):
        self._test_set_task_with_minus_undone(2)

    def test_set_task_with_minus_undone_col4(self):
        self._test_set_task_with_minus_undone(4)

    def test_set_task_with_minus_undone_col8(self):
        self._test_set_task_with_minus_undone(8)

    def test_set_task_with_minus_undone_col12(self):
        self._test_set_task_with_minus_undone(12)

    def _test_set_task_with_minus_undone(self, col):
        self.setBlockText(
            """
            - [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            - [ ] task 1
            """
        )

    def test_set_task_with_plus_done_col1(self):
        self._test_set_task_with_plus_done(1)

    def test_set_task_with_plus_done_col2(self):
        self._test_set_task_with_plus_done(2)

    def test_set_task_with_plus_done_col4(self):
        self._test_set_task_with_plus_done(4)

    def test_set_task_with_plus_done_col8(self):
        self._test_set_task_with_plus_done(8)

    def test_set_task_with_plus_done_col12(self):
        self._test_set_task_with_plus_done(12)

    def _test_set_task_with_plus_done(self, col):
        self.setBlockText(
            """
            + [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            + [X] task 1
            """
        )

    def test_set_task_with_plus_undone_col1(self):
        self._test_set_task_with_plus_undone(1)

    def test_set_task_with_plus_undone_col2(self):
        self._test_set_task_with_plus_undone(2)

    def test_set_task_with_plus_undone_col4(self):
        self._test_set_task_with_plus_undone(4)

    def test_set_task_with_plus_undone_col8(self):
        self._test_set_task_with_plus_undone(8)

    def test_set_task_with_plus_undone_col12(self):
        self._test_set_task_with_plus_undone(12)

    def _test_set_task_with_plus_undone(self, col):
        self.setBlockText(
            """
            + [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            + [ ] task 1
            """
        )

    def test_set_task_with_asterisk_in_quote_done_col1(self):
        self._test_set_task_with_asterisk_in_quote_done(1)

    def test_set_task_with_asterisk_in_quote_done_col2(self):
        self._test_set_task_with_asterisk_in_quote_done(2)

    def test_set_task_with_asterisk_in_quote_done_col4(self):
        self._test_set_task_with_asterisk_in_quote_done(4)

    def test_set_task_with_asterisk_in_quote_done_col6(self):
        self._test_set_task_with_asterisk_in_quote_done(6)

    def test_set_task_with_asterisk_in_quote_done_col12(self):
        self._test_set_task_with_asterisk_in_quote_done(12)

    def _test_set_task_with_asterisk_in_quote_done(self, col):
        self.setBlockText(
            """
            > * [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > * [X] task 1
            """
        )

    def test_set_task_with_asterisk_in_quote_undone_col1(self):
        self._test_set_task_with_asterisk_in_quote_undone(1)

    def test_set_task_with_asterisk_in_quote_undone_col2(self):
        self._test_set_task_with_asterisk_in_quote_undone(2)

    def test_set_task_with_asterisk_in_quote_undone_col4(self):
        self._test_set_task_with_asterisk_in_quote_undone(4)

    def test_set_task_with_asterisk_in_quote_undone_col6(self):
        self._test_set_task_with_asterisk_in_quote_undone(6)

    def test_set_task_with_asterisk_in_quote_undone_col12(self):
        self._test_set_task_with_asterisk_in_quote_undone(12)

    def _test_set_task_with_asterisk_in_quote_undone(self, col):
        self.setBlockText(
            """
            > * [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > * [ ] task 1
            """
        )

    def test_set_task_with_minus_in_quote_done_col1(self):
        self._test_set_task_with_minus_in_quote_done(1)

    def test_set_task_with_minus_in_quote_done_col2(self):
        self._test_set_task_with_minus_in_quote_done(2)

    def test_set_task_with_minus_in_quote_done_col4(self):
        self._test_set_task_with_minus_in_quote_done(4)

    def test_set_task_with_minus_in_quote_done_col6(self):
        self._test_set_task_with_minus_in_quote_done(6)

    def test_set_task_with_minus_in_quote_done_col12(self):
        self._test_set_task_with_minus_in_quote_done(12)

    def _test_set_task_with_minus_in_quote_done(self, col):
        self.setBlockText(
            """
            > - [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > - [X] task 1
            """
        )

    def test_set_task_with_minus_in_quote_undone_col1(self):
        self._test_set_task_with_minus_in_quote_undone(1)

    def test_set_task_with_minus_in_quote_undone_col2(self):
        self._test_set_task_with_minus_in_quote_undone(2)

    def test_set_task_with_minus_in_quote_undone_col4(self):
        self._test_set_task_with_minus_in_quote_undone(4)

    def test_set_task_with_minus_in_quote_undone_col6(self):
        self._test_set_task_with_minus_in_quote_undone(6)

    def test_set_task_with_minus_in_quote_undone_col12(self):
        self._test_set_task_with_minus_in_quote_undone(12)

    def _test_set_task_with_minus_in_quote_undone(self, col):
        self.setBlockText(
            """
            > - [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > - [ ] task 1
            """
        )

    def test_set_task_with_plus_in_quote_done_col1(self):
        self._test_set_task_with_plus_in_quote_done(1)

    def test_set_task_with_plus_in_quote_done_col2(self):
        self._test_set_task_with_plus_in_quote_done(2)

    def test_set_task_with_plus_in_quote_done_col4(self):
        self._test_set_task_with_plus_in_quote_done(4)

    def test_set_task_with_plus_in_quote_done_col6(self):
        self._test_set_task_with_plus_in_quote_done(6)

    def test_set_task_with_plus_in_quote_done_col12(self):
        self._test_set_task_with_plus_in_quote_done(12)

    def _test_set_task_with_plus_in_quote_done(self, col):
        self.setBlockText(
            """
            > + [ ] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > + [X] task 1
            """
        )

    def test_set_task_with_plus_in_quote_undone_col1(self):
        self._test_set_task_with_plus_in_quote_undone(1)

    def test_set_task_with_plus_in_quote_undone_col2(self):
        self._test_set_task_with_plus_in_quote_undone(2)

    def test_set_task_with_plus_in_quote_undone_col4(self):
        self._test_set_task_with_plus_in_quote_undone(4)

    def test_set_task_with_plus_in_quote_undone_col6(self):
        self._test_set_task_with_plus_in_quote_undone(6)

    def test_set_task_with_plus_in_quote_undone_col12(self):
        self._test_set_task_with_plus_in_quote_undone(12)

    def _test_set_task_with_plus_in_quote_undone(self, col):
        self.setBlockText(
            """
            > + [X] task 1
            """
        )
        self.setCaretTo(1, col)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            > + [ ] task 1
            """
        )

    def test_toggle_multi_caret_tasks(self):
        self.setBlockText(
            """
            * [X] task 1
                - [X] sub task
                    + [X] sub task
            * [ ] task 1
                - [ ] sub task
                    + [ ] sub task
            > * [X] task 1
            >     - [X] sub task
            >         + [X] sub task
            > * [ ] task 1
            >     - [ ] sub task
            >         + [ ] sub task
            """
        )
        self.setCaretTo(1, 1)
        for i in range(2, 13):
            self.addCaretAt(i, 1)
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            * [ ] task 1
                - [ ] sub task
                    + [ ] sub task
            * [X] task 1
                - [X] sub task
                    + [X] sub task
            > * [ ] task 1
            >     - [ ] sub task
            >         + [ ] sub task
            > * [X] task 1
            >     - [X] sub task
            >         + [X] sub task
            """
        )

    def test_toggle_selected_tasks(self):
        self.setBlockText(
            """
            * [X] task 1
                - [X] sub task
                    + [X] sub task
            * [ ] task 1
                - [ ] sub task
                    + [ ] sub task
            > * [X] task 1
            >     - [X] sub task
            >         + [X] sub task
            > * [ ] task 1
            >     - [ ] sub task
            >         + [ ] sub task
            """
        )
        self.view.run_command("select_all")
        self.view.run_command("mde_toggle_task_list_item")
        self.assertEqualBlockText(
            """
            * [ ] task 1
                - [ ] sub task
                    + [ ] sub task
            * [X] task 1
                - [X] sub task
                    + [X] sub task
            > * [ ] task 1
            >     - [ ] sub task
            >         + [ ] sub task
            > * [X] task 1
            >     - [X] sub task
            >         + [X] sub task
            """
        )
