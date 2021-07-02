# Text Formatting

MarkdownEditing supports formatting text by

*	auto-pairing corresponding markup characters
*	special purpose key bindings

## Auto Pairing

MarkdownEditing extends extends ST's auto pairing capabilities.

*   Asterisks (<kbd>*</kbd>), backticks (<kbd>`</kbd>) and underscores (<kbd>_</kbd>) are auto-paired and wrap selected text
*   <kbd>~</kbd> wraps selected text with `~~` (strike-through)
*   <kbd>Backspace</kbd> deletes an empty pair
*   <kbd>Space</kbd> or <kbd>Tab</kbd> deletes right element of empty pair of asterisks or underscores

This feature is controlled by global `auto_match_enabled` setting.

## Key Bindings

These are bound to bold and italic. They work both with and without selections. If there is no selection, they will just transform the word under the cursor. These key bindings will unbold/unitalicize selection if it is already bold/italic.

| markup       | rendered   | Linux/Windows                 | MacOS
|--------------|------------|-------------------------------|---------------------------------------------
\*\*bold\*\*   | **bold**   | <kbd>Alt</kbd> + <kbd>B</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>B</kbd>
\_italic\_     | _italic_   | <kbd>Alt</kbd> + <kbd>I</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>I</kbd>
\~\~strike\~\~ | ~~strike~~ |                               |
\`code\`       | `code`     |                               |

# Headings

## Headings Styles

### ATX style

MarkdownEditing assists with maintaining desired ATX headings style by keeping closing hashes balanced or by removing them automatically.

_This feature can be disabled by setting `"mde.auto_match_heading_hashes": false`._

You can switch between open and closed heading style for the active view via Command Palette:

*   **MarkdownEditing: Add Closing Heading Hashes**  
    Sets: `"mde.match_heading_hashes": true` and adds closing hashes to all headings.

*   **MarkdownEditing: Remove Closing Heading Hashes**  
    Sets: `"mde.match_heading_hashes": false` and removes closing hashes to all headings.

*   **MarkdownEditing: Fix Closing Heading Hashes**  
    Adds or removes closing hashes according to value of `"mde.match_heading_hashes"` without modifying it.

By default heading style is detected when loading or saving a file and stored in view specific settings.

A value of `"mde.match_heading_hashes": false` means _"open style"_:

```markdown
## ATX heading

Open style without closing hashes.
```

A value of `"mde.match_heading_hashes": true` means _"closed style"_:

```markdown

## ATX heading ##

Closed style with closing hashes.
```

_Auto-detection can be disabled by `"mde.detect_heading_style": false`._

In that case you can manually enforce a style via `"mde.match_heading_hashes"` in user preferences or project specific settings.

### Setext style

MarkdownEditing assists with maintaining width of underlined headings during typing.

Just hit <kbd>tab</kbd> after `-` or `=` and underline width is adjusted to headings text length.

![headings-setext](img/headings-setext.png)

All headings can be fixed or converted at once via Command Palette:

*   **MarkdownEditing: Fix Underlined Headings**  
    Adjusts every setext-style header to add or remove `=` or `-` characters as needed to match the lengths of their header text.

*   **MarkdownEditing: Convert Underlined Headings to ATX**  
    Converts every setext-style header into an ATX style header. If something is selected only the headers in the selections will be converted, otherwise the conversion will be applied to the whole view.

## Headings Levels

Headings levels can be modified by placing caret to desired lines and run a command via Command Palette:

*   **MarkdownEditing: Convert Heading to Text**  
    Removes all hashes.

*   **MarkdownEditing: Set Headings Level x**  
    Replaces any number of existing hashes by `x` hashes.

*   **MarkdownEditing: Increase Headings Level**  
    Add one additional hash.

*   **MarkdownEditing: Decrease Headings Level**  
    Remove one hash.

or use one of the following bindings:

| Linux/Windows | MacOS | Description
|---------------|-------|-------------
| <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>0</kbd> | <kbd>⌘</kbd> + <kbd>^</kbd> + <kbd>0</kbd> | convert headings into normal text
| <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>1..6</kbd> | <kbd>⌘</kbd> + <kbd>^</kbd> + <kbd>1..6</kbd> | set headings level to 1..6
| <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>,</kbd> | <kbd>⌘</kbd> + <kbd>^</kbd> + <kbd>,</kbd> | reduce headings level by one
| <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>.</kbd> | <kbd>⌘</kbd> + <kbd>^</kbd> + <kbd>.</kbd> | increase headings level by one

Adding or removing `#` at the beginning of lines also modifies heading levels implicitly while maintaining open or closed heading styles.

### Constraints

1.  Unordered lists are not converted to headings.
    
    ```
    * item
    * [ ] task
    ```

2.  All functions work with multiple selections.
3.  If a selection spans multiple lines a heading is created for each line
    separately.

## Folding Sections

Irrelevant sections of documents can be folded/collapsed via Command Palette:

*   **MarkdownEditing: Toggle Folding Current Section**  
    Folds/unfolds current section.

*   **MarkdownEditing: Fold Level 1-6 Sections**  
    Fold all sections under headers of specific level.

*   **MarkdownEditing: Fold/Unfold All Sections**  
    Self explanatory.

Folding is bound to following keys by default:

| Linux/Windows | MacOS | Description
|---------------|-------|-------------
| <kbd>ctrl</kbd> + <kbd>k</kbd>, <kbd>ctrl</kbd> + <kbd>0</kbd> | <kbd>⌥</kbd> + <kbd>k</kbd>, <kbd>⌥</kbd> + <kbd>0</kbd> | Unfold all sections
| <kbd>ctrl</kbd> + <kbd>k</kbd>, <kbd>ctrl</kbd> + <kbd>1..6</kbd> | <kbd>⌥</kbd> + <kbd>k</kbd>, <kbd>⌥</kbd> + <kbd>1..6</kbd> | Fold sections of level 1..6
| <kbd>Shift</kbd> + <kbd>Tab</kbd> | <kbd>⇧</kbd> + <kbd>Tab</kbd> | Fold/Unfold current section.
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Tab</kbd> | <kbd>^</kbd> + <kbd>⇧</kbd> + <kbd>Tab</kbd> | Fold all sections under headings of a certain level.

## Navigation

MarkdownEditing provides various ways to navigate between sections.

Headings are listed via

*   Goto Symbol (<kbd>Ctrl</kbd> + <kbd>R</kbd>)
*   Goto Symbol in Project (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd>)

Relevant commands are exposed via Command Palette:

*   **MarkdownEditing: Goto Previous/Next Heading (Any Level)**  
    Jump to very previous or next heading

*   **MarkdownEditing: Goto Previous/Next Heading (Same or higher Level)**  
    Jump to previous or next heading of same or higher level

Navigation is bound to following keys by default:

| Linux/Windows | MacOS | Description
|---------------|-------|-------------
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>PageUp/PageDown</kbd> | <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>PageUp/PageDown</kbd> | Go to the previous/next heading of any level
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>PageUp/PageDown</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>PageUp/PageDown</kbd> | Go to the previous/next heading of the same or higher level

# Lists and Tasks

List bullets are automatically changed when indenting or unindenting list items by default. This behavior can be disabled via `"mde.list_indent_auto_switch_bullet": false`.

Markdown can support with keeping list item text aligned at tab width if `"mde.list_align_text": true` is set.

Following commands are provided via Command Palette:

*   **Switch List Bullet Type**
    Switches the highlighted list between numbered and bulleted style.

# References

Following commands are provided via Command Palette:

*   **Add Missing Link Labels**  
    Scans document for referenced link usages (`[some link][some_ref]` and `[some link][]`) and checks if they are all defined. If there are undefined link references, command will automatically create their definition snippet at the bottom of the file.

*   **Magic Footnotes Command**  
    Adds a footnote after the word under cursor. If cursor is already on a footnote, jumps to its definition or reference.

*   **Gather Missing Footnotes**  
    Add definition stubs (if there is none) for all footnotes references.

*   **Jump Reference**  
    Jumps cursor between definitions and references.

*   **New Reference**  
    Adds a new link under cursor.

*   **New Inline Link**  
    Adds a new inline link under cursor.

*   **New Inline Image**  
    Adds a new inline image under cursor.

*   **New Image**  
    Adds a new image under cursor.

*   **New Footnote**  
    Adds a footnote under cursor.

*   **Delete Reference**  
    Deletes the definition and references of a link.

*   **Organize References**  
    Sorts and gives a report on current link references usage.


Important functions are bound to following keys by default:

| Linux/Windows | MacOS | Description
|---------------|-------|-------------
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>V</kbd>  | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>V</kbd> | Creates or pastes the contents of the clipboard as an inline link on selected text.
| <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>R</kbd>  | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>R</kbd> | Creates or pastes the contents of the clipboard as a reference link.
| <kbd>Shift</kbd> + <kbd>Win</kbd> + <kbd>K</kbd> | <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>K</kbd> | Creates or pastes the contents of the clipboard as an inline image on selected text.
| <kbd>Alt</kbd> + <kbd>Shift</kbd> + <kbd>6</kbd> | <kbd>⌥</kbd> + <kbd>⇧</kbd> + <kbd>6</kbd> | Inserts a footnote.

# Wiki

Wiki links are defined by surrounding a (wiki) word with double square brackets, for example:

    [[SampleWikiPage]]

The user can `open` wiki page using a sublime command. This will search the current open file's directory (and sub-directories) for a file with a matching name and a markdown extension. For example, opening the previous wiki link
will look for and open a file named:

    SampleWikiPage.md

Note that, if the wiki page does *not* yet exist, if will be created with a header matching the page name. However the file will only actually be created on the file system, when it is saved by the user. 

The user can `list back links` and of course to open them. Back links are pages that reference the current page. This allows pages to be tied together into a personal wiki. A common technique is to define *tag* wiki pages and to list any tags for a page as references to the tag pages at the bottom of the page, for example:
    
    [[TagSyntax]] [[TagDev]] [[TagPython]]

This allows the user to list all pages with a specific tag, by opening the tag page and list all back links.

Journal wiki pages are also supported. A journal page is just a wiki page with a name matching the current date.

Lastly the command to open the *home* page is provided, where the home page is just a wiki page named `HomePage`.


| Linux/Windows | MacOS | Description
|---------------|-------|-------------
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>H</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>H</kbd> | Open home page
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>D</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>D</kbd> | Open wiki page under the cursor
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>J</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>J</kbd> | Open journal page for today
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>B</kbd> | <kbd>⌘</kbd> + <kbd>⌥</kbd> + <kbd>B</kbd> | List back links
