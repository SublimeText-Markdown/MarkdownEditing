from MarkdownEditing.tests import DereferrablePanelTestCase


class MdeNumberListTestCase(DereferrablePanelTestCase):

    def setUp(self):
        self.view.settings().set("mde.auto_increment_ordered_list_number", True)

    def test_add_2nd_item_with_dot_and_one_space(self):
        self.setBlockText(
            """
            1. item 1
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1
            2.\x20
            """
        )

    def test_add_2nd_item_with_dot_and_two_spaces(self):
        self.setBlockText(
            """
            1.  item 1
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1.  item 1
            2.\x20\x20
            """
        )

    def test_add_2nd_item_with_paren_and_one_space(self):
        self.setBlockText(
            """
            1) item 1
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1) item 1
            2)\x20
            """
        )

    def test_add_2nd_item_with_paren_and_two_spaces(self):
        self.setBlockText(
            """
            1)  item 1
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1)  item 1
            2)\x20\x20
            """
        )

    def test_add_10th_item_with_dot_and_one_space(self):
        self.setBlockText(
            """
            9. item 9
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            9. item 9
            10.\x20
            """
        )

    def test_add_10th_item_with_dot_and_two_spaces(self):
        self.setBlockText(
            """
            9.  item 9
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            9.  item 9
            10.\x20
            """
        )

    def test_add_10th_item_with_paren_and_one_space(self):
        self.setBlockText(
            """
            9) item 9
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            9) item 9
            10)\x20
            """
        )

    def test_add_10th_item_with_paren_and_two_spaces(self):
        self.setBlockText(
            """
            9)  item 9
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            9)  item 9
            10)\x20
            """
        )

    def test_insert_2nd_item_with_dot_and_one_space(self):
        self.setBlockText(
            """
            1. item 1
            2. item 2
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1
            2.\x20
            2. item 2
            """
        )

    def test_insert_2nd_item_with_dot_and_two_spaces(self):
        self.setBlockText(
            """
            1.  item 1
            2.  item 2
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1.  item 1
            2.\x20\x20
            2.  item 2
            """
        )

    def test_insert_2nd_item_with_paren_and_one_space(self):
        self.setBlockText(
            """
            1) item 1
            2) item 2
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1) item 1
            2)\x20
            2) item 2
            """
        )

    def test_insert_2nd_item_with_paren_and_two_spaces(self):
        self.setBlockText(
            """
            1)  item 1
            2)  item 2
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1)  item 1
            2)\x20\x20
            2)  item 2
            """
        )

    def test_move_2nd_item_with_dot_and_one_space_caret_at_col3(self):
        self.setBlockText(
            """
            1. item 1
            2. item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1
            2.
            3. item 2
            """
        )

    def test_move_2nd_item_with_dot_and_one_space_caret_at_col4(self):
        self.setBlockText(
            """
            1. item 1
            2. item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1
            2.\x20
            3. item 2
            """
        )

    def test_move_2nd_item_with_paren_and_one_space_caret_at_col3(self):
        self.setBlockText(
            """
            1) item 1
            2) item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1) item 1
            2)
            3) item 2
            """
        )

    def test_move_2nd_item_with_paren_and_one_space_caret_at_col4(self):
        self.setBlockText(
            """
            1) item 1
            2) item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1) item 1
            2)\x20
            3) item 2
            """
        )

    def test_move_9th_item_with_dot_and_one_space_caret_at_col3(self):
        self.setBlockText(
            """
            8. item 1
            9. item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8. item 1
            9.
            10. item 2
            """
        )

    def test_move_9th_item_with_dot_and_one_space_caret_at_col4(self):
        self.setBlockText(
            """
            8. item 1
            9. item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8. item 1
            9.\x20
            10. item 2
            """
        )

    def test_move_9th_item_with_dot_and_two_spaces_caret_at_col3(self):
        # TODO: first two spaces after number need special treatment
        #       to keep item 2 aligned
        self.setBlockText(
            """
            8.  item 1
            9.  item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8.  item 1
            9.
            10.  item 2
            """
        )

    def test_move_9th_item_with_dot_and_two_spaces_caret_at_col4(self):
        self.setBlockText(
            """
            8.  item 1
            9.  item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8.  item 1
            9.\x20
            10. item 2
            """
        )

    def test_move_9th_item_with_dot_and_two_spaces_caret_at_col5(self):
        self.setBlockText(
            """
            8.  item 1
            9.  item 2
            """
        )
        self.setCaretTo(2, 5)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8.  item 1
            9.\x20\x20
            10. item 2
            """
        )

    def test_move_9th_item_with_paren_and_one_space_caret_at_col3(self):
        self.setBlockText(
            """
            8) item 1
            9) item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8) item 1
            9)
            10) item 2
            """
        )

    def test_move_9th_item_with_paren_and_one_space_caret_at_col4(self):
        self.setBlockText(
            """
            8) item 1
            9) item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8) item 1
            9)\x20
            10) item 2
            """
        )

    def test_move_9th_item_with_paren_and_two_spaces_caret_at_col3(self):
        # TODO: first two spaces after number need special treatment
        #       to keep item 2 aligned
        self.setBlockText(
            """
            8)  item 1
            9)  item 2
            """
        )
        self.setCaretTo(2, 3)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8)  item 1
            9)
            10)  item 2
            """
        )

    def test_move_9th_item_with_paren_and_two_spaces_caret_at_col4(self):
        self.setBlockText(
            """
            8)  item 1
            9)  item 2
            """
        )
        self.setCaretTo(2, 4)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8)  item 1
            9)\x20
            10) item 2
            """
        )

    def test_move_9th_item_with_paren_and_two_spaces_caret_at_col5(self):
        self.setBlockText(
            """
            8)  item 1
            9)  item 2
            """
        )
        self.setCaretTo(2, 5)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8)  item 1
            9)\x20\x20
            10) item 2
            """
        )

    def test_split_1st_item_with_dot_and_one_space_before_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            1. item 1 item 2
            """
        )
        self.setCaretTo(1, 10)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1
            2.  item 2
            """
        )

    def test_split_1st_item_with_dot_and_one_space_after_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            1. item 1 item 2
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1. item 1\x20
            2. item 2
            """
        )

    def test_split_1st_item_with_dot_and_two_spaces_before_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            1.  item 1 item 2
            """
        )
        self.setCaretTo(1, 11)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1.  item 1
            2.   item 2
            """
        )

    def test_split_1st_item_with_dot_and_two_spaces_after_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            1.  item 1 item 2
            """
        )
        self.setCaretTo(1, 12)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            1.  item 1\x20
            2.  item 2
            """
        )

    def test_split_multiple_items_with_dot_and_one_space_before_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            8. item 8 item 9 item 10
            """
        )
        self.setCaretTo(1, 10)
        self.addCaretAt(1, 17)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8. item 8
            9.  item 9
            10.  item 10
            """
        )

    def test_split_multiple_items_with_dot_and_one_space_after_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            8. item 8 item 9 item 10
            """
        )
        self.setCaretTo(1, 11)
        self.addCaretAt(1, 18)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8. item 8\x20
            9. item 9\x20
            10. item 10
            """
        )

    def test_split_multiple_items_with_dot_and_two_space_before_space(self):
        # Note: doesn't trim white spaces
        # TODO: spaces after numbers need better treatment
        self.setBlockText(
            """
            8.  item 8 item 9 item 10
            """
        )
        self.setCaretTo(1, 11)
        self.addCaretAt(1, 18)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8.  item 8
            9.   item 9
            10.   item 10
            """
        )

    def test_split_multiple_items_with_dot_and_two_space_after_space(self):
        # Note: doesn't trim white spaces
        self.setBlockText(
            """
            8.  item 8 item 9 item 10
            """
        )
        self.setCaretTo(1, 12)
        self.addCaretAt(1, 19)
        self.view.run_command("mde_number_list")
        self.assertEqualBlockText(
            """
            8.  item 8\x20
            9.  item 9\x20
            10. item 10
            """
        )

