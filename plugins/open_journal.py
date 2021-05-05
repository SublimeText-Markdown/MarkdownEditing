from datetime import date

from .mdeutils import *
from .wiki_page import *

DEFAULT_DATE_FORMAT = '%Y-%m-%d'


class OpenJournalCommand(MDETextCommand):
    def run(self, edit):
        print("Running OpenJournalCommand")
        today = date.today()
        date_format = self.view.settings().get("mde.journal.dateformat", DEFAULT_DATE_FORMAT)
        name = today.strftime(date_format)

        wiki_page = WikiPage(self.view)
        wiki_page.select_page(name)
