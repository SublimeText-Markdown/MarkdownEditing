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
        MdeColorActivateCommand,
        on_after_install,
        on_before_uninstall,
    )
    from .plugins.custom_find_under_expand import (
        CustomFindUnderExpandCommand,
    )
    from .plugins.decide_title import (
        DecideTitle,
    )
    from .plugins.distraction_free_mode import (
        KeepCurrentLineCentered,
    )
    from .plugins.folding import (
        FoldAllLinkUrls,
        FoldAllSectionsCommand,
        FoldSectionCommand,
        FoldSectionContextCommand,
        GotoNextHeadingCommand,
        GotoPreviousHeadingCommand,
        ShowFoldAllSectionsCommand,
        UnfoldAllSectionsCommand,
        UnfoldSectionContextCommand,
    )
    from .plugins.footnotes import (
        GatherMissingFootnotesCommand,
        GoToFootnoteDefinitionCommand,
        GoToFootnoteReferenceCommand,
        InsertFootnoteCommand,
        MagicFootnotesCommand,
        MarkFootnotes,
        SortFootnotesCommand,
        SwitchToFromFootnoteCommand,
    )
    from .plugins.indent_list_item import (
        IndentListItemCommand,
    )
    from .plugins.indent_list_multiitem import (
        IndentListMultiitemCommand,
    )
    from .plugins.lint import (
        MarkdownLintCommand,
        MarkdownLintMdlCommand,
    )
    from .plugins.list_back_links import (
        ListBackLinksCommand,
    )
    from .plugins.make_page_reference import (
        MakePageReferenceCommand,
    )
    from .plugins.numbered_list import (
        NumberListCommand,
        NumberListReferenceCommand,
    )
    from .plugins.open_home_page import (
        OpenHomePageCommand,
    )
    from .plugins.open_journal import (
        OpenJournalCommand,
    )
    from .plugins.open_page import (
        OpenPageCommand,
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
    from .plugins.replace_selected_command import (
        ReplaceSelectedCommand,
    )
    from .plugins.switch_list_bullet_type import (
        SwitchListBulletTypeCommand,
    )
    from .plugins.underlined_headers import (
        CompleteUnderlinedHeaderCommand,
        ConvertToAtxCommand,
        FixAllUnderlinedHeadersCommand,
    )

    def plugin_loaded():
        on_after_install()

    def plugin_unloaded():
        on_before_uninstall()
