from MarkdownEditing.tests import DereferrablePanelTestCase


class TestMdeReferenceNewFootnoteCommand(DereferrablePanelTestCase):

    def test_new_footnote_in_first_line(self):
        self.setBlockText(
            """
            # Test 1

            First inline.
            Second inline.

            Third inline.

            # Test 2

            paragraph
            """
        )
        self.setCaretTo(3,6)
        self.view.run_command("mde_reference_new_footnote")
        self.assertEqualBlockText(
            """
            # Test 1

            First[^1] inline.
            Second inline.

            Third inline.

            # Test 2

            paragraph
            [^1]:\x20
            """
        )

    def test_new_footnote_in_second_line(self):
        self.setBlockText(
            """
            # Test 1

            First[^1] inline.
            Second inline.

            Third inline.

            # Test 2

            paragraph

            [^1]:
                Footnote text
                with second line
            """
        )
        self.setCaretTo(4,7)
        self.view.run_command("mde_reference_new_footnote")
        self.assertEqualBlockText(
            """
            # Test 1

            First[^1] inline.
            Second[^2] inline.

            Third inline.

            # Test 2

            paragraph

            [^1]:
                Footnote text
                with second line
            [^2]:\x20
            """
        )
