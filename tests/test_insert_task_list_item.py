from MarkdownEditing.tests import DereferrablePanelTestCase


class InsertTaskListItemTestCase(DereferrablePanelTestCase):

    def setUp(self):
        self.setBlockText("")

    def test_insert_unaligned_task_with_asterisk(self):
        self.view.settings().set("mde.list_align_text", False)
        self.view.settings().set("mde.list_indent_bullets", ["*", "-", "+"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            * [ ]\x20
            """
        )

    def test_insert_unaligned_task_with_minus(self):
        self.view.settings().set("mde.list_align_text", False)
        self.view.settings().set("mde.list_indent_bullets", ["-", "*", "+"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            - [ ]\x20
            """
        )

    def test_insert_unaligned_task_with_plus(self):
        self.view.settings().set("mde.list_align_text", False)
        self.view.settings().set("mde.list_indent_bullets", ["+", "-", "*"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            + [ ]\x20
            """
        )

    def test_insert_aligned_task_with_asterisk(self):
        self.view.settings().set("mde.list_align_text", True)
        self.view.settings().set("mde.list_indent_bullets", ["*", "-", "+"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            * [ ]\t
            """
        )

    def test_insert_aligned_task_with_minus(self):
        self.view.settings().set("mde.list_align_text", True)
        self.view.settings().set("mde.list_indent_bullets", ["-", "*", "+"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            - [ ]\t
            """
        )

    def test_insert_aligned_task_with_plus(self):
        self.view.settings().set("mde.list_align_text", True)
        self.view.settings().set("mde.list_indent_bullets", ["+", "-", "*"])

        self.setCaretTo(1, 1)
        self.view.run_command("mde_insert_task_list_item")
        self.assertEqualBlockText(
            """
            + [ ]\t
            """
        )
