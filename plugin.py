"""Load and Unload all MarkdownEditing modules.

This module exports __all__ modules, which Sublime Text needs to know about.
"""
import sublime

if int(sublime.version()) < 3176:
    print(__package__ + " requires ST3 3176+")
else:
    import sys

    # clear modules cache if package is reloaded (after update?)
    prefix = __package__ + "."  # don't clear the base package
    for module_name in [
        module_name
        for module_name in sys.modules
        if module_name.startswith(prefix) and module_name != __name__
    ]:
        del sys.modules[module_name]
    prefix = None

    # import all published Commands and EventListeners
    from .plugins.bootstrap import (
        on_after_install,
        on_before_uninstall,
    )
    from .plugins.color_schemes import (
        MdeSelectColorSchemeCommand,
    )
    from .plugins.folding import (
        MdeFoldAllSectionsCommand,
        MdeFoldLinksCommand,
        MdeFoldLinksListener,
        MdeFoldSectionCommand,
        MdeShowFoldAllSectionsCommand,
        MdeUnfoldAllSectionsCommand,
        MdeUnfoldSectionCommand,
    )
    from .plugins.footnotes import (
        MdeGatherMissingFootnotesCommand,
        MdeGotoFootnoteDefinitionCommand,
        MdeGotoFootnoteReferenceCommand,
        MdeInsertFootnoteCommand,
        MdeMagicFootnotesCommand,
        MdeSortFootnotesCommand,
        MdeSwitchToFromFootnoteCommand,
        MdeMarkFootnotesListener,
    )
    from .plugins.headings import (
        MdeChangeHeadingsLevelCommand,
        MdeCompleteUnderlinedHeadingsCommand,
        MdeConvertUnderlinedHeadingsToAtxCommand,
        MdeFixUnderlinedHeadingsCommand,
        MdeGotoNextHeadingCommand,
        MdeGotoPreviousHeadingCommand,
        MdeMatchHeadingHashesCommand,
        MdeMatchHeadingHashesDetector,
        MdeUnsavedViewNameSetter,
    )
    from .plugins.lists import (
        MdeIndentListItemCommand,
        MdeUnindentListItemCommand,
        MdeNumberListCommand,
        MdeSwitchListBulletTypeCommand,
        MdeInsertTaskListItemCommand,
        MdeToggleTaskListItemCommand,
        MdeJoinLines,
    )
    from .plugins.lint import (
        MdeMarkdownLintCommand,
        MdeMarkdownLintMdlCommand,
    )
    from .plugins.logging import (
        load_logger,
        unload_logger
    )
    from .plugins.quotes import (
        MdeIndentQuote,
        MdeUnindentQuote,
    )
    from .plugins.references import (
        MdeConvertInlineLinksToReferencesCommand,
        MdeConvertInlineLinkToReferenceCommand,
        MdeGatherMissingLinkMarkersCommand,
        MdeReferenceDeleteReferenceCommand,
        MdeReferenceJumpCommand,
        MdeReferenceJumpContextCommand,
        MdeReferenceNewFootnoteCommand,
        MdeReferenceNewImageCommand,
        MdeReferenceNewInlineImageCommand,
        MdeReferenceNewInlineLinkCommand,
        MdeReferenceNewReferenceCommand,
        MdeReferenceOrganizeCommand,
        MdeAddNumberedReferenceDefinitionCommand,
        MdeReferenceCompletionsProvider,
    )
    from .plugins.view import (
        MdeReplaceSelectedCommand,
        MdeToggleCenteredLineCommand,
        MdeCenteredLineKeeper,
    )
    from .plugins.wiki_page import (
        MdeListBackLinksCommand,
        MdeMakePageReferenceCommand,
        MdeOpenHomePageCommand,
        MdeOpenJournalCommand,
        MdeOpenPageCommand,
        MdePrepareFromTemplateCommand,
    )

    def plugin_loaded():
        def worker():
            load_logger()
            on_after_install()

        sublime.set_timeout(worker, 10)

    def plugin_unloaded():
        unload_logger()
        on_before_uninstall()
