from .mdeutils import *
from .wiki_page import *


class ListBackLinksCommand(MDETextCommand):
    def run(self, edit):
        print("Running ListBackLinksCommand")
        wiki_page = WikiPage(self.view)

        file_list = wiki_page.find_files_with_ref()
        wiki_page.select_backlink(file_list)
