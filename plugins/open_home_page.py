from .mdeutils import MDETextCommand
from .wiki_page import WikiPage, DEFAULT_HOME_PAGE


class OpenHomePageCommand(MDETextCommand):
    def run(self, edit):
        print("Running OpenHomePageCommand")
        home_page = self.view.settings().get("mde.wikilinks.homepage", DEFAULT_HOME_PAGE)

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(home_page)