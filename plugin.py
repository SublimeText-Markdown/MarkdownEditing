"""Load and Unload all MarkdownEditing modules.

This module exports __all__ modules, which Sublime Text needs to know about.
"""

__version__ = "3.6.4"

import sys

# clear modules cache if package is reloaded (after update?)
prefix = __spec__.parent + "."  # don't clear the base package
for module_name in [
    module_name
    for module_name in sys.modules
    if module_name.startswith(prefix) and module_name != __spec__.name
]:
    del sys.modules[module_name]
del globals()["prefix"]
del globals()["sys"]

# import all published Commands and EventListeners
from .plugins.color_schemes import (
    MdeSelectColorSchemeCommand,
)
from .plugins.critic import MdeGotoNextCriticCommand, MdeGotoPrevCriticCommand
from .plugins.folding import (
    MdeAutoFoldListener,
    MdeFoldAllSectionsCommand,
    MdeFoldLinksCommand,
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
    MdeMarkFootnotesListener,
    MdeSortFootnotesCommand,
    MdeSwitchToFromFootnoteCommand,
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
from .plugins.lint import (
    MdeMarkdownLintCommand,
    MdeMarkdownLintMdlCommand,
)
from .plugins.lists import (
    MdeIndentListItemCommand,
    MdeInsertTaskListItemCommand,
    MdeJoinLines,
    MdeNumberListCommand,
    MdeResetTaskListItemsCommand,
    MdeSwitchListBulletTypeCommand,
    MdeToggleTaskListItemCommand,
    MdeUnindentListItemCommand,
)
from .plugins.quotes import (
    MdeIndentQuote,
    MdeUnindentQuote,
)
from .plugins.references import (
    MdeAddNumberedReferenceDefinitionCommand,
    MdeConvertInlineLinksToReferencesCommand,
    MdeConvertInlineLinkToReferenceCommand,
    MdeGatherMissingLinkMarkersCommand,
    MdeReferenceCompletionsProvider,
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
    MdeCenteredLineKeeper,
    MdeReplaceSelectedCommand,
    MdeToggleCenteredLineCommand,
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
        from .plugins.bootstrap import on_after_install
        from .plugins.logging import load_logger

        load_logger()
        on_after_install()

    from sublime import set_timeout

    set_timeout(worker, 100)


def plugin_unloaded():
    from .plugins.bootstrap import on_before_uninstall
    from .plugins.logging import unload_logger

    unload_logger()
    on_before_uninstall()
