import sublime

from MarkdownEditing.tests import DereferrablePanelTestCase

# test assets

from MarkdownEditing.plugins.headings import (
    all_headings
)
from MarkdownEditing.plugins.folding import (
    section_region_and_level
)


class FoldingTestCase(DereferrablePanelTestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create output panel and load text from `test_folding.md` into.
        """
        super().setUpClass()
        with open(__file__[:-2] + "md") as f:
            cls.setText(f.read().replace("\r\n", "\n").replace("\r", "\n"))

    def setUp(self):
        self.view.settings().set("mde.auto_fold_link.enabled", True)

    def tearDown(self):
        self.view.settings().erase("mde.auto_fold_link.enabled")
        self.view.settings().erase("mde.folding.target_level")

    def assertFoldedRegions(self, region_tuples):
        self.assertEqual(
            self.view.folded_regions(),
            list(map(lambda x: sublime.Region(*x), region_tuples))
        )

    # all_headings() unittests

    def test_all_headings(self):
        self.assertEqual(
            list(all_headings(self.view)),
            [
                (0, 11, 1),
                (84, 98, 2),
                (100, 117, 3),
                (138, 158, 4),
                (203, 223, 4),
                (275, 292, 3),
                (358, 391, 2),
                (436, 450, 2),
                (471, 482, 1),
                (503, 522, 1),
                (524, 547, 2),
                (568, 591, 2),
                (611, 630, 1)
            ]
        )

    # test section region of atx heading level 1

    def test_section_region_and_level__heading_1_bol(self):
        self._test_section_region_and_level(1, 1, 11, 470, 1)

    def test_section_region_and_level__heading_1_mol(self):
        self._test_section_region_and_level(1, 2, 11, 470, 1)

    def test_section_region_and_level__heading_1_eol(self):
        self._test_section_region_and_level(1, 10, 11, 470, 1)

    # test section region of atx heading level 2

    def test_section_region_and_level__heading_1_1_bol(self):
        self._test_section_region_and_level(9, 1, 98, 357, 2)

    def test_section_region_and_level__heading_1_1_mol(self):
        self._test_section_region_and_level(9, 5, 98, 357, 2)

    def test_section_region_and_level__heading_11__eol(self):
        self._test_section_region_and_level(9, 15, 98, 357, 2)

    # test section region of atx heading level 4

    def test_section_region_and_level__heading_1_1_1_2_bol(self):
        self._test_section_region_and_level(19, 1, 223, 274, 4)

    def test_section_region_and_level__heading_1_1_1_2_mol(self):
        self._test_section_region_and_level(19, 2, 223, 274, 4)

    def test_section_region_and_level__heading_11__1_2_eol(self):
        self._test_section_region_and_level(19, 15, 223, 274, 4)

    # test section region of setext heading level 1

    def test_section_region_and_level__setext_heading_3_text_bol(self):
        self._test_section_region_and_level(45, 1, 522, 610, 1)

    def test_section_region_and_level__setext_heading_3_underline_bol(self):
        self._test_section_region_and_level(46, 1, 522, 610, 1)

    def test_section_region_and_level__setext_heading_3_text_mol(self):
        self._test_section_region_and_level(45, 5, 522, 610, 1)

    def test_section_region_and_level__setext_heading_3_underline_mol(self):
        self._test_section_region_and_level(46, 5, 522, 610, 1)

    def test_section_region_and_level__setext_heading_3_text_eol(self):
        self._test_section_region_and_level(45, 10, 522, 610, 1)

    def test_section_region_and_level__setext_heading_3_underline_eol(self):
        self._test_section_region_and_level(46, 10, 522, 610, 1)

    # test section region of setext heading level 2

    def test_section_region_and_level__setext_heading_3_1_text_bol(self):
        self._test_section_region_and_level(48, 1, 547, 567, 2)

    def test_section_region_and_level__setext_heading_3_1_underline_bol(self):
        self._test_section_region_and_level(49, 1, 547, 567, 2)

    def test_section_region_and_level__setext_heading_3_1_text_mol(self):
        self._test_section_region_and_level(48, 5, 547, 567, 2)

    def test_section_region_and_level__setext_heading_3_1_underline_mol(self):
        self._test_section_region_and_level(49, 5, 547, 567, 2)

    def test_section_region_and_level__setext_heading_3_1_text_eol(self):
        self._test_section_region_and_level(48, 12, 547, 567, 2)

    def test_section_region_and_level__setext_heading_3_1_underline_eol(self):
        self._test_section_region_and_level(49, 12, 547, 567, 2)

    def _test_section_region_and_level(self, row, col, begin, end, level):
        self.assertEqual(
            section_region_and_level(self.view, self.textPoint(row, col), -1),
            (sublime.Region(begin, end), level)
        )

    # test folding and unfolding atx heading level 1

    def test_fold_section__heading_1_bol(self):
        self._test_fold_section__heading_1(1, 1)

    def test_fold_section__heading_1_mol(self):
        self._test_fold_section__heading_1(1, 5)

    def test_fold_section__heading_1_eol(self):
        self._test_fold_section__heading_1(1, 12)

    def _test_fold_section__heading_1(self, row, col):
        # setup test
        self.setCaretTo(row, col)
        self.view.run_command("unfold_all")

        # fold heading
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([(11, 470)])

        # unfold heading
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([(37, 52), (184, 199), (367, 382), (417, 432)])

        # setup test
        self.setCaretTo(row, col)
        self.view.settings().set("mde.auto_fold_link.enabled", False)

        # fold heading
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([(11, 470)])

        # unfold heading
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([])

    # test folding and unfolding setext heading level 1

    def test_fold_section__heading_3_text_bol(self):
        self._test_fold_section__heading_3(45, 1)

    def test_fold_section__heading_3_text_mol(self):
        self._test_fold_section__heading_3(45, 5)

    def test_fold_section__heading_3_text_eol(self):
        self._test_fold_section__heading_3(45, 10)

    def test_fold_section__heading_3_underline_bol(self):
        self._test_fold_section__heading_3(46, 1)

    def test_fold_section__heading_3_underline_mol(self):
        self._test_fold_section__heading_3(46, 2)

    def test_fold_section__heading_3_underline_eol(self):
        self._test_fold_section__heading_3(46, 10)

    def _test_fold_section__heading_3(self, row, col):
        # setup test
        self.setCaretTo(row, col)
        self.view.settings().set("mde.auto_fold_link.enabled", False)
        self.view.run_command("unfold_all")

        # fold heading
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([(522, 610)])

        # unfold heading
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([])

    # test folding and unfolding setext heading level 2

    def test_fold_section__heading_3_1_text_bol(self):
        self._test_fold_section__heading_3_1(48, 1)

    def test_fold_section__heading_3_1_text_mol(self):
        self._test_fold_section__heading_3_1(48, 5)

    def test_fold_section__heading_3_1_text_eol(self):
        self._test_fold_section__heading_3_1(48, 10)

    def test_fold_section__heading_3_1_underline_bol(self):
        self._test_fold_section__heading_3_1(49, 1)

    def test_fold_section__heading_3_1_underline_mol(self):
        self._test_fold_section__heading_3_1(49, 2)

    def test_fold_section__heading_3_1_underline_eol(self):
        self._test_fold_section__heading_3_1(49, 10)

    def _test_fold_section__heading_3_1(self, row, col):
        # setup test
        self.setCaretTo(row, col)
        self.view.settings().set("mde.auto_fold_link.enabled", False)
        self.view.run_command("unfold_all")

        # fold heading
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([(547, 567)])

        # unfold heading
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([])

    # test folding and unfolding by level

    def test_fold_all_sections__level_0_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(0, [
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_fold_all_sections__level_1_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(1, [
            (11, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

    def test_fold_all_sections__level_2_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(2, [
            (98, 357),
            (391, 435),
            (450, 470),
            (547, 567),
            (591, 610)
        ])

    def test_fold_all_sections__level_3_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(3, [
            (117, 274),
            (292, 357)
        ])

    def test_fold_all_sections__level_4_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(4, [
            (158, 202),
            (223, 274)
        ])

    def test_fold_all_sections__level_5_without_auto_link_folding(self):
        self._test_fold_all_sections_without_auto_link_folding(5, [])

    def _test_fold_all_sections_without_auto_link_folding(self, level, expected_regions):
        self.view.settings().set("mde.auto_fold_link.enabled", False)
        self.view.run_command("mde_fold_all_sections", {"target_level": level})
        self.assertFoldedRegions(expected_regions)

    def test_fold_all_sections__level_0_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(0, [
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_fold_all_sections__level_1_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(1, [
            (11, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

    def test_fold_all_sections__level_2_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(2, [
            (37, 52),
            (98, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (547, 567),
            (591, 610)
        ])

    def test_fold_all_sections__level_3_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(3, [
            (37, 52),
            (117, 274),
            (292, 357),
            (367, 382),
            (417, 432)
        ])

    def test_fold_all_sections__level_4_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(4, [
            (37, 52),
            (158, 202),
            (223, 274),
            (367, 382),
            (417, 432)
        ])

    def test_fold_all_sections__level_5_with_auto_link_folding(self):
        self._test_fold_all_sections_with_auto_link_folding(5, [
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

    def _test_fold_all_sections_with_auto_link_folding(self, level, expected_regions):
        self.view.run_command("mde_fold_all_sections", {"target_level": level})
        self.assertFoldedRegions(expected_regions)

    def test_unfold_section__heading_1_with_folding_tartet_level_0(self):
        # unfold and then fold "1 Heading"
        self._test_unfold_section__heading_x_with_folding_tartet_level_0(1, [
            (37, 52),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_unfold_section__heading_1_1_with_folding_tartet_level_0(self):
        # unfold and then fold "1.1 Heading"
        self._test_unfold_section__heading_x_with_folding_tartet_level_0(9, [
            (11, 83),
            # (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_unfold_section__heading_1_1_1_with_folding_tartet_level_0(self):
        # unfold and then fold "1.1.1 Heading"
        self._test_unfold_section__heading_x_with_folding_tartet_level_0(11, [
            (11, 83),
            (98, 99),
            # (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_unfold_section__heading_3_with_folding_tartet_level_0(self):
        # unfold and then fold "3 Heading"
        self._test_unfold_section__heading_x_with_folding_tartet_level_0(45, [
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            # (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_unfold_section__heading_3_2_with_folding_tartet_level_0(self):
        # unfold and then fold "3.2 Heading"
        self._test_unfold_section__heading_x_with_folding_tartet_level_0(53, [
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            # (591, 610),
            (630, 649)
        ])

    def _test_unfold_section__heading_x_with_folding_tartet_level_0(self, row, expected_regions):
        # prepare test by folding sections by target_level 0 (outline mode)
        # outline mode: Only fold a section up to very next heading!
        self.view.run_command("mde_fold_all_sections", {"target_level": 0})

        # unfold heading
        self.setCaretTo(row, 1)
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions(expected_regions)

        # fold heading
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_unfold_section__heading_1_with_folding_tartet_level_1(self):
        # prepare test by folding sections by target_level 1
        self.view.run_command("mde_fold_all_sections", {"target_level": 1})

        # unfold "1 Heading" with caret before folding marker
        self.setCaretTo(1, 11)
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([
            (37, 52),
            (98, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

        # fold "1 Heading"
        self.setCaretTo(1, 11)
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([
            (11, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

        # unfold "1 Heading" with caret after folding marker
        self.setCaretTo(40, 1)
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([
            (37, 52),
            (98, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

        # unfold "1.1 Heading"
        self.setCaretTo(9, 9)
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([
            (37, 52),
            (117, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

        # unfold "1.1.2 Heading"
        self.setCaretTo(25, 9)
        self.view.run_command("mde_unfold_section")
        self.assertFoldedRegions([
            (37, 52),
            (117, 274),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

        # fold "1.1 Heading"
        self.setCaretTo(9, 9)
        self.view.run_command("mde_fold_section")
        self.assertFoldedRegions([
            (37, 52),
            (98, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ])

    def test_fold_links_command__target_level_none(self):
        # setup initial state with all sections unfolded
        self.setCaretTo(1, 1)
        self.view.run_command("mde_unfold_all_sections")

        # disable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": False})
        self.assertFoldedRegions([])

        # enable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

    def test_fold_links_command__target_level_0(self):
        # prepare test by folding sections by target_level 0 (outline-mode)
        self.setCaretTo(1, 1)
        self.view.run_command("mde_fold_all_sections", {"target_level": 0})

        # disable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": False})
        self.assertFoldedRegions([
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            # (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

        # enable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            (11, 83),
            (98, 99),
            (117, 137),
            (158, 202),
            (223, 274),
            (292, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (482, 502),
            (522, 523),
            (547, 567),
            (591, 610),
            (630, 649)
        ])

    def test_fold_links_command__target_level_1(self):
        # no link is visible, thus folded regions must not change
        expected_regions = [
            (11, 470),
            (482, 502),
            (522, 610),
            (630, 649)
        ]

        # prepare test by folding sections by target_level 1
        self.setCaretTo(1, 1)
        self.view.run_command("mde_fold_all_sections", {"target_level": 1})

        # disable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": False})
        self.assertFoldedRegions(expected_regions)

        # enable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions(expected_regions)

    def test_fold_links_command__target_level_2(self):
        # prepare test by folding sections by target_level 1
        self.setCaretTo(1, 1)
        self.view.run_command("mde_fold_all_sections", {"target_level": 2})

        # disable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": False})
        self.assertFoldedRegions([
            (98, 357),
            (391, 435),
            (450, 470),
            (547, 567),
            (591, 610)
        ])

        # enable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            (37, 52),
            (98, 357),
            (367, 382),
            (391, 435),
            (450, 470),
            (547, 567),
            (591, 610)
        ])

    def test_fold_links_command__target_level_3(self):
        # prepare test by folding sections by target_level 1
        self.setCaretTo(1, 1)
        self.view.run_command("mde_fold_all_sections", {"target_level": 3})

        # disable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": False})
        self.assertFoldedRegions([
            (117, 274),
            (292, 357)
        ])

        # enable automatic link folding
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            (37, 52),
            (117, 274),
            (292, 357),
            (367, 382),
            (417, 432)
        ])

    def test_auto_fold_links__target_level_none(self):
        # setup initial state with all sections unfolded
        self.setCaretTo(1, 1)
        self.view.run_command("mde_unfold_all_sections")

        # caret not within a link url, all folded
        self.setCaretTo(1, 1)
        self.assertFoldedRegions([
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

        # caret at beginning of url in line 3 (unfolded)
        self.setCaretTo(3, 25)
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            # (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

        # caret at end of url in line 3 (unfolded)
        self.setCaretTo(3, 40)
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            # (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

        # select url in line 3 (unfolded)
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(self.textPoint(3, 25), self.textPoint(3, 40)))
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            # (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

        # select line 3 (all folded)
        self.view.sel().clear()
        self.view.sel().add(self.view.line(self.textPoint(3, 25)))
        self.view.run_command("mde_fold_links", {"fold": True})
        self.assertFoldedRegions([
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

    def test_folded_links_when_editing_content(self):
        # setup initial state with all sections unfolded
        self.setCaretTo(3, 2)
        self.view.run_command("mde_unfold_all_sections")
        self.assertFoldedRegions([
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])

        # caret between "A" and "paragraph" and insert "new "
        # make sure following regions move accordingly
        self.view.run_command("insert", {"characters": "new "})
        self.assertFoldedRegions([
            (41, 56),
            (188, 203),
            (371, 386),
            (421, 436)
        ])

        # delete "new " again to restore previous state
        self.view.sel().clear()
        self.view.sel().add(sublime.Region(self.textPoint(3, 2), self.textPoint(3, 6)))
        self.view.run_command("left_delete")
        self.assertFoldedRegions([
            (37, 52),
            (184, 199),
            (367, 382),
            (417, 432)
        ])
