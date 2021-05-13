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
    from .plugins.basic_ops import (
        MDEBoldCommand,
    )
    from .plugins.bootstrap import (
        on_after_install,
        on_before_uninstall,
    )
    from .plugins.color_schemes import (
        MdeSelectColorSchemeCommand,
    )
    from .plugins.folding import (
        MdeFoldAllLinkUrlsCommand,
        MdeFoldAllSectionsCommand,
        MdeFoldSectionCommand,
        MdeFoldSectionContextCommand,
        MdeGotoNextHeadingCommand,
        MdeGotoPreviousHeadingCommand,
        MdeShowFoldAllSectionsCommand,
        MdeUnfoldAllSectionsCommand,
        MdeUnfoldSectionContextCommand,
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
        MdeCompleteUnderlinedHeadingsCommand,
        MdeConvertUnderlinedHeadingsToAtxCommand,
        MdeFixUnderlinedHeadingsCommand,
    )
    from .plugins.lists import (
        MdeIndentListItemCommand,
        MdeIndentListMultiitemCommand,
        MdeNumberListCommand,
        MdeNumberListReferenceCommand,
        MdeSwitchListBulletTypeCommand,
    )
    from .plugins.lint import (
        MdeMarkdownLintCommand,
        MdeMarkdownLintMdlCommand,
    )
    from .plugins.prepare_from_template import (
        MdePrepareFromTemplateCommand,
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
    )
    from .plugins.view import (
        MdeReplaceSelectedCommand,
        MdeKeepCurrentLineCentered,
        MdeUnsavedViewNameSetter,
    )
    from .plugins.wiki_page import (
        MdeListBackLinksCommand,
        MdeMakePageReferenceCommand,
        MdeOpenHomePageCommand,
        MdeOpenJournalCommand,
        MdeOpenPageCommand,
    )

    def plugin_loaded():
        on_after_install()

    def plugin_unloaded():
        on_before_uninstall()
