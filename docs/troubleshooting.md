# Troubleshooting

## 3.0.0 Migration Guide

### Preferences need manual update

MarkdownEditing stores settings in _Preferences.sublime-settings_ as of version 3.0.0.

Thus all user specific syntax specific settings or overrides can or must be removed:

1. Open a Markdown file
2. Open Command Palette <kbd>ctrl+shift+p</kbd>
3. Execute `Preferences: Settings - Syntax Specific`
4. Remove everything judged useless from the right panel.

The following syntax specific settings have been removed:

```json
{
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor.tmTheme",

    "tab_size": 4,
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": false,
    "auto_match_enabled": true,

    // Layout
    "draw_centered": true,
    "word_wrap": true,
    "wrap_width": 80,
    "rulers": [],

    // Line
    "line_numbers": false,
    "highlight_line": false,
    "line_padding_top": 2,
    "line_padding_bottom": 2,

    // Caret
    "caret_style": "wide",
    "caret_extra_top": 3,
    "caret_extra_bottom": 3,
}
```

### Custom key bindings need manual update

Macro calls and key binding contexts have been changed heavily.

Commands have been renamed in order to avoid possible conflicts with other packages.
Others have been split to follow naming scheme of ST's built-in commands 
(e.g. indent/unindent commands).

Hints about required or optional arguments may be found in
_MarkdownEditing/Default (...).sublime-keymap_.

| old names                          | new names
|------------------------------------|--------------------------------------
| -                                  | mde_change_headings_level
| -                                  | mde_fold_links
| -                                  | mde_match_heading_hashes
| -                                  | mde_toggle_centered_line
| -                                  | mde_toggle_task_list_item
| -                                  | mde_unindent_list_item
| complete_underlined_header         | mde_complete_underlined_headings
| convert_inline_link_to_reference   | mde_convert_inline_link_to_reference
| convert_inline_links_to_references | mde_convert_inline_links_to_references
| convert_to_atx                     | mde_convert_underlined_headings_to_atx
| deindent_quote                     | mde_unindent_quote
| fix_all_underlined_headers         | mde_fix_underlined_headings
| fold_all_sections                  | mde_fold_all_sections
| fold_section                       | mde_fold_section
| gather_missing_footnotes           | mde_gather_missing_footnotes
| gather_missing_link_markers        | mde_gather_missing_link_markers
| goto_next_heading                  | mde_goto_next_heading
| goto_previous_heading              | mde_goto_previous_heading
| indent_list_item                   | mde_indent_list_item
| indent_list_multiitem              | _(use mde_indent_list_item instead)_
| indent_quote                       | mde_indent_quote
| list_back_links                    | mde_list_back_links
| magic_footnotes                    | mde_magic_footnotes
| make_page_reference                | mde_make_page_reference
| markdown_lint                      | mde_markdown_lint
| markdown_lint_mdl                  | mde_markdown_lint_mdl
| mde_color_activate                 | mde_select_color_scheme
| number_list                        | mde_number_list
| number_list_reference              | mde_add_numbered_reference_definition
| open_home_page                     | mde_open_home_page
| open_journal                       | mde_open_journal
| open_page                          | mde_open_page
| reference_delete_reference         | mde_reference_delete_reference
| reference_jump                     | mde_reference_jump
| reference_new_footnote             | mde_reference_new_footnote
| reference_new_image                | mde_reference_new_image
| reference_new_inline_image         | mde_reference_new_inline_image
| reference_new_inline_link          | mde_reference_new_inline_link
| reference_new_reference            | mde_reference_new_reference
| reference_organize                 | mde_reference_organize
| show_fold_all_sections             | mde_show_fold_all_sections
| switch_list_bullet_type            | mde_switch_list_bullet_type
| unfold_all_sections                | mde_unfold_all_sections

## Error loading syntax file

!!! warning
    Error loading syntax file "Packages/Markdown/Markdown.sublime-syntax": Unable to open Packages/Markdown/Markdown.sublime-syntax

MarkdownEditing does its best to reassign syntax of open files after installation or during upgrade.

However open markdown files at install time may cause this issue. You have to **manually change their syntax to your newly installed Markdown syntax** then.

!!! info _Note_
    The default _Markdown_ package shipped with Sublime Text is disabled automatically as it causes some conflicts. You may need to enable it manually after disabling or uninstalling MarkdownEditing.

## Roll back to an older version

When you notice any undesired behaviour introduced by the latest update, your feedback is always welcome at [issue page][mdeissues]. However before it's fixed, you can rollback to [an earlier version][mdereleases]. Find the desired version and download the zip file, then follow [manual installation guide](#manual-installation)

## Known Bugs

* Setext-style headers (`===` and `---`) do not show up in the symbol list. This is due to a Sublime Text limitation (see [#158][]). However, we are able to put a placeholder to indicate the existence of the header. We encourage you to use Atx-style headers (`#`).

* Installing for the first time while having markdown files opened may cause MarkdownEditing to behave unexpectedly on those files. Close and reopen those files to fix it.

[#158]: https://github.com/SublimeText-Markdown/MarkdownEditing/issues/158
[mdereleases]: https://github.com/SublimeText-Markdown/MarkdownEditing/releases
[mdeissues]: https://github.com/SublimeText-Markdown/MarkdownEditing/issues
