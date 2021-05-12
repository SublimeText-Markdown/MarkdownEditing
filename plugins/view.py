from .mdeutils import MDEViewEventListener


class MdeKeepCurrentLineCentered(MDEViewEventListener):
    """
    This class keeps caret in vertical center position.
    These features can be enabled/disabled via settings files.
    In order to target "distraction free" mode, FullScreenStatus plugin must be installed:
    https://github.com/maliayas/SublimeText_FullScreenStatus
    """

    def on_selection_modified_async(self):
        sel = self.view.sel()
        if sel and len(sel) != 1:
            return

        settings = self.view.settings()
        if self.view.window().settings().get('fss_on_distraction_free'):
            if not settings.get('mde.distraction_free_mode', {}).get('mde.keep_centered', True):
                return
        elif not settings.get('mde.keep_centered', False):
            return

        self.view.show_at_center(sel[0].begin())


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
