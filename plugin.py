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
    from .plugins.indent_list_item import (
        MdeIndentListItemCommand,
        MdeIndentListMultiitemCommand,
    )
    from .plugins.lint import (
        MdeMarkdownLintCommand,
        MdeMarkdownLintMdlCommand,
    )
    from .plugins.numbered_list import (
        MdeNumberListCommand,
        MdeNumberListReferenceCommand,
    )
    from .plugins.prepare_from_template import (
        PrepareFromTemplateCommand,
    )
    from .plugins.quote_indenting import (
        DeindentQuote,
        IndentQuote,
    )
    from .plugins.references import (
        ConvertInlineLinksToReferencesCommand,
        ConvertInlineLinkToReferenceCommand,
        GatherMissingLinkMarkersCommand,
        ReferenceDeleteReference,
        ReferenceJumpCommand,
        ReferenceJumpContextCommand,
        ReferenceNewFootnote,
        ReferenceNewImage,
        ReferenceNewInlineImage,
        ReferenceNewInlineLinkCommand,
        ReferenceNewReferenceCommand,
        ReferenceOrganize,
    )
    from .plugins.switch_list_bullet_type import (
        SwitchListBulletTypeCommand,
    )
    from .plugins.underlined_headers import (
        CompleteUnderlinedHeaderCommand,
        ConvertToAtxCommand,
        FixAllUnderlinedHeadersCommand,
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
