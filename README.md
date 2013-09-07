# MarkdownEditing

### Better Markdown Editing features for Sublime Text 2

This package will make MarkdownEditor your default theme for Markdown/MultiMarkdown files. Adjust it to your liking or remove the line from the .sublime-settings files


* Asterisks and underscores are autopaired and will wrap selected text
* If you start an empty pair and hit backspace, both elements are deleted
* If you start an empty pair and hit space, the right element is deleted
* backticks are paired
* Left bracket pairing is modified to eliminate the selection and leave the cursor at a point where you can insert a `[]` or `()` pair for a link
* ⌘⌥V will paste the contents of the clipboard as an inline link on selected text
* ⌘⌥R will paste the contents of the clipboard as a reference link
* ⌘⌥K inserts a standard inline link, ⌘⇧K inserts an inline image
* ⌘⌥B and ⌘⌥I are bound to bold and italics (Markdown).
* `~` triggers HTML `<del></del>` tags (strikethrough) to selected text
* Typing "#" when there's a selection will surround it with "#" to make it a headline. Multiple presses add additional hashes, increasing the level of the header. Once you hit 6 hashes, it will reset to 0 on the next press. The `match_header_hashes` will determine if the `#` are mirrored on both sides or just at the beginning of the line.
* Typing return at the end of a line that begins with hashmarks will insert closing hashmarks on the headline. They're not required for Markdown, it's just aesthetics, and you can change the `match_header_hashes" option in your settings to disable.
* ⌘^1 through ⌘^6 will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command now respects the "match\_header\_hashes" preference setting.
* ⌘⇧6 will insert a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.
* ⌥⇧F will locate footnote markers without definitions and insert the marker for the definition
* ⌥⇧G will do the same for missing reference links

Keymap for Windows and Linux. Most of them are similar with the keymap on Mac OS X.

* Ctrl + Win + V will paste the contents of the clipboard as an inline link on selected text
* Ctrl + Win + R will paste the contents of the clipboard as a reference link
* Ctrl + Win + K inserts a standard inline link, Shift + Win + K inserts an inline image
* Alt + Win + B and Alt + Win + I are bound to bold and italics (Markdown).
* Ctrl + 1 through Ctrl + 6 will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command now respects the "match\_header\_hashes" preference setting.
* Ctrl + ⇧6 will insert a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.

Footnote commands submitted by [J. Nicholas Geist](https://github.com/jngeist) and originated at [geekabouttown](http://geekabouttown.com/posts/sublime-text-2-markdown-footnote-goodness)

There's a long way to go and I have a lot of Python to learn.

### Installation

#### Sublime Package Control

The preferred method of installation is via [Sublime Package Control](http://wbond.net/sublime_packages/package_control).

1. [Install Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation)
2. From inside Sublime Text 2, open Package Control's Command Pallet: CTRL+SHIFT+P (Windows, Linux) or CMD+SHIFT+P on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `MarkdownEditing` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text 2 to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.

#### Manual Installation

1. Download or clone this repository to a directory `MarkdownEditing` in the Sublime Text 2 Packages directory for your platform:
    * Mac: `git clone https://github.com/ttscoff/MarkdownEditing.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/MarkdownEditing`
    * Windows: `git clone https://github.com/ttscoff/MarkdownEditing.git %APPDATA%\Sublime/ Text/ 2/\MarkdownEditing`
    * Linux: `git clone https://github.com/ttscoff/MarkdownEditing.git ~/.Sublime\ Text\ 2/Packages/MarkdownEditing`
2. Restart Sublime Text 2 to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.
