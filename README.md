# MarkdownEditing

Markdown plugin for Sublime Text. Provides a decent Markdown color scheme (light and dark) with more __robust__ syntax highlighting and useful Markdown editing features for Sublime Text. 3 flavors are supported: Standard Markdown, __GitHub flavored Markdown__, MultiMarkdown.

![MarkdownEditing][github]

[Dark][github 2] and [yellow][github 3] theme available.

## Overview

* [Features](#features)
* [Key Bindings](#key-bindings)
* [GFM Specific Features](#gfm-specific-features)
* [Commands for Command Palette](#commands-for-command-palette)
* [Installation](#installation)
* [Configuration](#configuration)
* [Tips](#tips)
* [Similar Plugins](#similar-plugins)
* [Known Bugs](#known-bugs)
* [Contributing](#contributing)
* [Credits](#credits)
* [Donation](#donation)
* [License](#license)

## Features

* Asterisks and underscores are autopaired and will wrap selected text
    - If you start an empty pair and hit backspace, both elements are deleted
    - If you start an empty pair and hit space, the right element is deleted
* Backticks are paired
* At the end of a list item, pressing <kbd>Enter</kbd> will automatically insert the new list item bullet.
    - Pressing <kbd>Tab</kbd> on the blank list item will indent it and switch the list bullet to another one (Order is `*`, `-`, `+` in a cycle).
    - Pressing <kbd>Shift</kbd> <kbd>Tab</kbd> on the blank list item will unindent it in the same way as above.
    - Sequential <kbd>Tab</kbd> s or <kbd>Shift</kbd> <kbd>Tab</kbd> s are supported.
    - You can disable automatic bullet switching or choose which bullets to be used, in your settings file.
    - If a list item contains a [GFM task][GFM], pressing <kbd>Enter</kbd> at the end of the line will continue with a new blank task.
* At the end of a blockquote line, pressing <kbd>Enter</kbd> will automatically extend blockquote.
* Selecting some text and pressing <kbd>&gt;</kbd> will convert it to blockquote. The first and the last line don't have to be fully selected; partial select works, too.
* Left bracket pairing is modified to eliminate the selection and leave the cursor at a point where you can insert a `[]` or `()` pair for a link
* Displays Markdown headers in the Project Symbol List (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd>). They will start with `#`, so you will know they belong to markdown files at a glance. Also they will be on top of the list because of the presedence of `#`.
* <kbd>~</kbd> wraps selected text with `~~` (strikethrough).
* Typing `#` when there's a selection will surround it with `#` to make it a headline. Multiple presses add additional hashes, increasing the level of the header. Once you hit 6 hashes, it will reset to 0 on the next press. The `mde.match_header_hashes` will determine if the `#` are mirrored on both sides or just at the beginning of the line.
* Typing return at the end of a line that begins with hashmarks will insert closing hashmarks on the headline. They're not required for Markdown, it's just aesthetics, and you can change the `mde.match_header_hashes` option in your settings to disable.
* Setext-style headers can be completed with `Tab`. That is, typing `Tab` on a line containing only `=` or `-` characters will add or remove enough characters to it to match the length of the line above.

## Key Bindings

| OS X | Windows/Linux | Description |
|------|---------------|-------------|
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>V</kbd> | <kbd>Ctrl</kbd><kbd>Win</kbd><kbd>V</kbd> | Pastes the contents of the clipboard as an inline link on selected text.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>R</kbd> | <kbd>Ctrl</kbd><kbd>Win</kbd><kbd>R</kbd> | Pastes the contents of the clipboard as a reference link.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>K</kbd> | <kbd>Ctrl</kbd><kbd>Win</kbd><kbd>K</kbd> | Inserts a standard inline link.
| <kbd>⌘</kbd><kbd>⇧</kbd><kbd>K</kbd> | <kbd>Shift</kbd><kbd>Win</kbd><kbd>K</kbd> | Inserts an inline image.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>B</kbd> <kbd>⌘</kbd><kbd>⌥</kbd><kbd>I</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>B</kbd> <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>I</kbd> | These are bound to bold and italic. They work both with and without selections. If there is no selection, they will just transform the word under the cursor. These keybindings will unbold/unitalicize selection if it is already bold/italic.
| <kbd>⌘</kbd><kbd>^</kbd><kbd>1...6</kbd> | <kbd>Ctrl</kbd><kbd>1...6</kbd> | These will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command respects the `mde.match_header_hashes` preference setting.
| <kbd>⌘</kbd><kbd>⇧</kbd><kbd>6</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>6</kbd> | Inserts a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.
| <kbd>⌥</kbd><kbd>⇧</kbd><kbd>F</kbd> | <kbd>Alt</kbd><kbd>Shift</kbd><kbd>F</kbd> | Locates footnote markers without definitions and inserts their markers for the definition.
| <kbd>⌥</kbd><kbd>⇧</kbd><kbd>G</kbd> | <kbd>Alt</kbd><kbd>Shift</kbd><kbd>G</kbd> | Locates link references without definitions and inserts their labels at the bottom for the definition.
| <kbd>⌘</kbd><kbd>⇧</kbd><kbd>M</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>M</kbd> | Performs lint on current Markdown file. See [lint rules](lint_docs/RULES.md).

## GFM Specific Features

Underscores in words doesn't mess with bold or italic style:

![underscore-in-words][github 5]

Fenced code blocks gets syntax highlighting inside:

![fenced-code-block][github 6]

Keyboard shortcuts gets highlighted like in GitHub:

![keyboard-shortcut][github 7]

Strikethrough is supported:

![strikethrough][github 8]

## Commands for Command Palette

### Fix Underlined Headers

Adjusts every setext-style header to add or remove `=` or `-` characters as needed to match the lengths of their header text.

### Convert Underlined Headers to ATX

Converts every setext-style header into an ATX style header. If something is selected only the headers in the selections will be converted, otherwise the conversion will be applied to the whole view.

### Add Missing Link Labels

Scans document for referenced link usages (`[some link][some_ref]` and `[some link][]`) and checks if they are all defined. If there are undefined link references, command will automatically create their definition snippet at the bottom of the file.

## Installation

> __Important Note About Installation__
> 
> Are you getting this error after installation: _**Error loading syntax file** "Packages/Markdown/Markdown.tmLanguage": Unable to open Packages/Markdown/Markdown.tmLanguage_? This is caused by open markdown files at the install time. You have to __manually change their syntax to your newly installed Markdown syntax__. Read the below paragraph for more details on this.

_Note_: Sublime text has a native tiny package for Markdown. However, when MarkdownEditing is enabled, native package causes some conflicts. For this reason, MarkdownEditing will automatically disable it. Since it doesn't bring anything new over MarkdownEditing, this is not a loss. But remember, when you disable MarkdownEditing, you have to reenable the native one manually (if you want).

If you are using Sublime Text 2, you have to disable the native package _manually_. To do that, add `Markdown` to your `ignored_packages` list in ST user settings:

    "ignored_packages": [..., "Markdown"],

### Package Control

The preferred method of installation is via [Sublime Package Control][wbond].

1. [Install Sublime Package Control][wbond 2]
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>CTRL</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> (Windows, Linux) or <kbd>CMD</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `MarkdownEditing` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.

### Manual Installation

1. Download or clone this repository to a directory `MarkdownEditing` in the Sublime Text Packages directory for your platform:
    * Mac: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/MarkdownEditing`
    * Windows: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git %APPDATA%\Sublime/ Text/ 2/\MarkdownEditing`
    * Linux: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git ~/.Sublime\ Text\ 2/Packages/MarkdownEditing`
2. Restart Sublime Text to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.

## Configuration

The plugin contains 3 different Markdown flavors: Standard Markdown, GitHub flavored Markdown, MultiMarkdown. Default is GitHub flavored Markdown. If you want to set another one as default, open a Markdown file and select your flavor from the menu: `View > Syntax > Open all with current extension as`. You're done.

You may want to have a look at the default settings files. They are located at:

    Packages/MarkdownEditing/Markdown.sublime-settings         [GitHub flavored Markdown]
    Packages/MarkdownEditing/Markdown (Standard).sublime-settings
    Packages/MarkdownEditing/MultiMarkdown.sublime-settings

If you want to override any of the default settings, you can open the appropriate user settings file using the `Preferences > Package Settings > Markdown Editing` menu. Each flavor has a different settings file.

Bold and italic markers are configurable through ST shell variables. You can use `Preferences > Package Settings > Markdown Editing` menu to see the default settings file. In order to override it, copy & paste its content into the user settings file (`Packages/User/Bold and Italic Markers.tmPreferences`) from the menu and make your edits. It is pretty straightforward.

In order to activate the dark or the yellow theme, put one of these lines to your user settings file of the flavor (`Packages/User/[flavor].sublime-settings`):

    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme",
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Yellow.tmTheme",

If you want to go with your already existing theme, you can reenable it with the same method as above. Keep in mind that, that theme may not cover all the parts of the Markdown syntax that this plugin defines.

By default, when you install the plugin, files with these extensions will be assigned to Markdown syntax: "md", "txt", "mdown", "markdown", "markdn". If you want to prevent any of these extensions to be opened as Markdown, follow these steps:

1. Click on the language menu at bottom right
2. Select "Open all with current extension as"
3. Choose your preferred syntax for that extension

## Tips

We are maintaining a [tips section][tips] in our [Wiki][]. Jump there to learn from others or share your experiences with others.

## Similar Plugins

* [Knockdown][]

     Knockdown offers useful Markdown features and a custom Markdown theme. All of its unique features except its theme are ported to MarkdownEditing and some of them are actually improved further in MarkdownEditing.
* [Sublime Markdown Extended][]
* [SmartMarkdown][]

## Known Bugs

* Setext-style headers (`===` and `---`) do not show up in the symbol list. This is due to a Sublime Text limitation (see [#158][]). However, we are able to put a placeholder to indicate the existence of the header. We encourage you to use Atx-style headers (`#`).

* Installing for the first time while having markdown files opened may cause MarkdownEditing to behave unexpectedly on those files. Close and reopen those files to fix it.

## Contributing

See `CONTRIBUTING.md` file.

## Credits

MarkdownEditing was originally created by [Brett Terpstra][brettterpstra] and has become a community project with the goal of consolidating the best features from the varied collection of Markdown packages for Sublime Text. Current development is headed up by [Ali Ayas][github 9].

Related blog posts from Brett:
* http://brettterpstra.com/2012/05/17/markdown-editing-for-sublime-text-2-humble-beginnings/
* http://brettterpstra.com/2013/11/23/markdownediting-for-sublime-text-updates/

This plugin contains portions of code from [Knockdown][].

Footnote commands were submitted by [J. Nicholas Geist][github 4] and originated at [geekabouttown][geekabouttown].

## Donation

You can support [contributors](https://github.com/SublimeText-Markdown/MarkdownEditing/graphs/contributors) of this project individually. Every contributor is welcomed to add his/her line below with any content. Ordering shall be alphabetically by GitHub username.

* [@maliayas](https://github.com/maliayas): <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=W2NXRPD43YSCU&amp;lc=TR&amp;item_name=open-source&amp;item_number=markdown-editing&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="[paypal]" /></a> ![donation received](http://maliayas.com/business/donation/badge.php?project=markdown_editing)

## License

MarkdownEditing is released under the [MIT License][opensource].

[TableEditor]:                 https://github.com/vkocubinsky/SublimeTableEditor
[Knockdown]:                   https://github.com/aziz/knockdown/
[Sublime Markdown Extended]:   https://github.com/jonschlinkert/sublime-markdown-extended
[SmartMarkdown]:               https://github.com/demon386/SmartMarkdown
[Typewriter]:                  https://github.com/alehandrof/Typewriter
[OpenUrl]:                     https://github.com/noahcoad/open-url
[brettterpstra]: http://brettterpstra.com
[geekabouttown]: http://geekabouttown.com/posts/sublime-text-2-markdown-footnote-goodness
[github]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/light.png
[github 2]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/dark.png
[github 3]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/yellow.png
[github 4]: https://github.com/jngeist
[github 5]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/underscore-in-words.png
[github 6]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/fenced-code-block.png
[github 7]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/keyboard-shortcut.png
[github 8]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/strikethrough.png
[github 9]: https://github.com/maliayas
[opensource]: http://www.opensource.org/licenses/MIT
[wbond]: http://wbond.net/sublime_packages/package_control
[wbond 2]: http://wbond.net/sublime_packages/package_control/installation
[FullScreenStatus]: https://github.com/maliayas/SublimeText_FullScreenStatus
[macstories]: http://www.macstories.net/roundups/sublime-text-2-and-markdown-tips-tricks-and-links/
[tips]: https://github.com/SublimeText-Markdown/MarkdownEditing/wiki/Tips
[Wiki]: https://github.com/SublimeText-Markdown/MarkdownEditing/wiki
[GFM]: https://help.github.com/articles/github-flavored-markdown
[#158]: https://github.com/SublimeText-Markdown/MarkdownEditing/issues/158
