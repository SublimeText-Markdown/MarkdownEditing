import sublime

from MarkdownEditing.tests import DereferrablePanelTestCase
from MarkdownEditing.plugin import MdeReferenceCompletionsProvider

class TestReferenceCompletions(DereferrablePanelTestCase):

    @classmethod
    def setUpClass(cls):
        """
        Create output panel and load text from `test_folding.md` into.
        """
        super().setUpClass()
        with open(__file__[:-2] + "md") as f:
            cls.setText(f.read().replace("\r\n", "\n").replace("\r", "\n"))

    def test_st3_reference_completions(self):
        if hasattr(sublime, "KIND_ID_MARKUP"):
            return

        expected_items = (
            [
                ['main-page\thttps://github.com/SublimeTex…', 'main-page'],
                ['issues\thttps://github.com/SublimeTex…', 'issues'],
                ['preview-url\thttps://github.com/SublimeTex…', 'preview-url'],
                ['list-ref\tdocs/configuration.html', 'list-ref'],
                ['quoted-list-ref\tdocs/configuration.html', 'quoted-list-ref'],
                ['quoted-image\tassets/images/foo.png', 'quoted-image']
            ],
            24
        )

        provider = MdeReferenceCompletionsProvider(self.view)
        completion_list = provider.on_query_completions("", [34])
        self.assertEqual(completion_list, expected_items)

    def test_st4_reference_completions(self):
        if not hasattr(sublime, "KIND_ID_MARKUP"):
            return

        expected_items = [
            sublime.CompletionItem('main-page', annotation='https://github.com/SublimeTex…', completion='main-page', completion_format=0, kind=(6, 'R', 'Ref'), details='reference description'),
            sublime.CompletionItem('issues', annotation='https://github.com/SublimeTex…', completion='issues', completion_format=0, kind=(6, 'R', 'Ref'), details='Create issues here!'),
            sublime.CompletionItem('preview-url', annotation='https://github.com/SublimeTex…', completion='preview-url', completion_format=0, kind=(6, 'R', 'Ref'), details='Main Preview Image'),
            sublime.CompletionItem('list-ref', annotation='docs/configuration.html', completion='list-ref', completion_format=0, kind=(6, 'R', 'Ref'), details='No title'),
            sublime.CompletionItem('quoted-list-ref', annotation='docs/configuration.html', completion='quoted-list-ref', completion_format=0, kind=(6, 'R', 'Ref'), details='No title'),
            sublime.CompletionItem('quoted-image', annotation='assets/images/foo.png', completion='quoted-image', completion_format=0, kind=(6, 'R', 'Ref'), details='No title')
        ]

        provider = MdeReferenceCompletionsProvider(self.view)
        completion_list = provider.on_query_completions("", [34])
        self.assertEqual(completion_list.completions, expected_items)
