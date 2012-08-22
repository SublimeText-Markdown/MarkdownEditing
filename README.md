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
* Typing "#" when there's a selection will surroung it with "#" to make it a headline. Multiple presses add additional hashes, increasing the level of the header. Once you hit 6 hashes, it will reset to 0 on the next press.
* Typing return at the end of a line that begins with hasmarks will insert closing hashmarks on the headline. They're not required for Markdown, it's just aesthetics, and you can comment out that command in the Default (OSX).sublime-keymap file if needed. I'll turn that into a plugin and add an option for it eventually.
* ⌘⇧6 will insert a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.
* ⌥⇧F will locate footnote markers without definitions and insert the marker for the definition
* ⌥⇧G will do the same for missing reference links

Footnote commands submitted by [J. Nicholas Geist](https://github.com/jngeist) and originated at [geekabouttown](http://geekabouttown.com/posts/sublime-text-2-markdown-footnote-goodness)

There's a long way to go and I have a lot of Python to learn.

