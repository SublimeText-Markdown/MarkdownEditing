from .mdeutils import MDEViewEventListener


class MdeUnsavedViewNameSetter(MDEViewEventListener):
    """
    This view event listener prints the first heading as tab title of unsaved documents.
    """

    MAX_NAME = 50

    def on_modified_async(self):
        if self.view.file_name() is not None:
            return

        headings = self.view.find_by_selector('text.html.markdown markup.heading - punctuation')
        region = headings[0] if headings else self.view.line(0)
        if len(region) > self.MAX_NAME:
            region.b = region.a + self.MAX_NAME
            suffix = '…'
        else:
            suffix = ''

        self.view.set_name(self.view.substr(region).strip() + suffix)
