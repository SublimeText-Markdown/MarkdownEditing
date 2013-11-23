# MarkdownEditing

Markdown plugin for Sublime Text. Provides a decent Markdown color scheme (light and dark) with more __robust__ syntax highlighting and useful Markdown editing features for Sublime Text. 3 flavors are supported: Standard Markdown, __GitHub flavored Markdown__, MultiMarkdown.

![MarkdownEditing][github]

[Dark][github 2] and [yellow][github 3] theme available.

## Overview

* [Features](#features)
* [GFM Spesific features](#gfm-spesific-features)
* [Commands](#commands)
* [Installation](#installation)
* [Configuration](#configuration)
* [Tips](#tips)
* [Similar Plugins](#similar-plugins)
* [Contributing](#contributing)
* [Credits](#credits)
* [License](#license)

## Features

* Asterisks and underscores are autopaired and will wrap selected text
* If you start an empty pair and hit backspace, both elements are deleted
* If you start an empty pair and hit space, the right element is deleted
* backticks are paired
* Left bracket pairing is modified to eliminate the selection and leave the cursor at a point where you can insert a `[]` or `()` pair for a link
* Displays Markdown headers in the Project Symbol List (<kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd>). They will start with `#`, so you will know they belong to markdown files at a glance. Also they will be on top of the list because of the presedence of `#`.
* <kbd>⌘</kbd> <kbd>⌥</kbd> <kbd>V</kbd> will paste the contents of the clipboard as an inline link on selected text
* <kbd>⌘</kbd> <kbd>⌥</kbd> <kbd>R</kbd> will paste the contents of the clipboard as a reference link
* <kbd>⌘</kbd> <kbd>⌥</kbd> <kbd>K</kbd> inserts a standard inline link, <kbd>⌘</kbd> <kbd>⇧</kbd> <kbd>K</kbd> inserts an inline image
* <kbd>Ctrl</kbd> <kbd>B</kbd> and <kbd>Ctrl</kbd> <kbd>I</kbd> are bound to bold and italic. They work both with and without selections. If there is no selection, they will just transform the word under the cursor. These keybindings will unbold/unitalicize selection if it is already bold/italic.
* <kbd>~</kbd> surrounds selected text with `~~` (strikethrough).
* Typing `#` when there's a selection will surround it with `#` to make it a headline. Multiple presses add additional hashes, increasing the level of the header. Once you hit 6 hashes, it will reset to 0 on the next press. The `mde_match_header_hashes` will determine if the `#` are mirrored on both sides or just at the beginning of the line.
* Typing return at the end of a line that begins with hashmarks will insert closing hashmarks on the headline. They're not required for Markdown, it's just aesthetics, and you can change the `mde_match_header_hashes` option in your settings to disable.
* <kbd>⌘</kbd> <kbd>^</kbd> <kbd>1</kbd>  through <kbd>⌘</kbd> <kbd>^</kbd> <kbd>6</kbd>  will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command now respects the `mde_match_header_hashes` preference setting.
* <kbd>⌘</kbd> <kbd>⇧</kbd> <kbd>6</kbd> will insert a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.
* <kbd>⌥</kbd> <kbd>⇧</kbd> <kbd>F</kbd> will locate footnote markers without definitions and insert the marker for the definition
* <kbd>⌥</kbd> <kbd>⇧</kbd> <kbd>G</kbd> will do the same for missing reference links

Keymap for Windows and Linux. Most of them are similar with the keymap on Mac OS X.

* <kbd>Ctrl</kbd> <kbd>Win</kbd> <kbd>V</kbd> will paste the contents of the clipboard as an inline link on selected text
* <kbd>Ctrl</kbd> <kbd>Win</kbd> <kbd>R</kbd> will paste the contents of the clipboard as a reference link
* <kbd>Ctrl</kbd> <kbd>Win</kbd> <kbd>K</kbd> inserts a standard inline link, <kbd>Shift</kbd> <kbd>Win</kbd> <kbd>K</kbd> inserts an inline image
* <kbd>Ctrl</kbd> <kbd>1</kbd> through <kbd>Ctrl</kbd> <kbd>6</kbd> will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command now respects the `mde_match_header_hashes` preference setting.
* <kbd>Ctrl</kbd> <kbd>⇧</kbd> <kbd>6</kbd> will insert a footnote and jump to its definition. If your cursor is in a definition, it will jump back to the marker.

Footnote commands submitted by [J. Nicholas Geist][github 4] and originated at [geekabouttown][geekabouttown]

## GFM Spesific Features

Underscores in words doesn't mess with bold or italic style:

![underscore-in-words][github 5]

Fenced code blocks gets syntax highlighting inside:

![fenced-code-block][github 6]

Keyboard shortcuts gets highlighted like in GitHub:

![keyboard-shortcut][github 7]

Strikethrough is supported:

![strikethrough][github 8]

## Commands

#### Fix Underlined Markdown Headers

[TODO]

## Installation

_Note_: Sublime text has a native tiny package for Markdown. However, when MarkdownEditing is enabled, native package causes some conflicts. For this reason, MarkdownEditing will automatically disable it. Since it doesn't bring anything new over MarkdownEditing, this is not a loss. But remember, when you disable MarkdownEditing, you have to reenable the native one manually (if you want).

#### [Package Control][wbond]

The preferred method of installation is via [Sublime Package Control][wbond].

1. [Install Sublime Package Control][wbond 2]
2. From inside Sublime Text 2, open Package Control's Command Pallet: <kbd>CTRL</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> (Windows, Linux) or <kbd>CMD</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `MarkdownEditing` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text 2 to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.

#### Manual Installation

1. Download or clone this repository to a directory `MarkdownEditing` in the Sublime Text 2 Packages directory for your platform:
    * Mac: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/MarkdownEditing`
    * Windows: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git %APPDATA%\Sublime/ Text/ 2/\MarkdownEditing`
    * Linux: `git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git ~/.Sublime\ Text\ 2/Packages/MarkdownEditing`
2. Restart Sublime Text 2 to complete installation. Open a Markdown file and this custom theme. The features listed above should now be available.

## Configuration

The plugin contains 3 different Markdown flavors: Standard Markdown, GitHub flavored Markdown, MultiMarkdown. Default is GitHub flavored Markdown. If you want to set another one as default, open a Markdown file and select your flavor from the menu: `View > Syntax > Open all with current extension as`. You're done.

You may want to have a look at the default settings files. They are located at:

    Packages/MarkdownEditing/Markdown.sublime-settings [GitHub flavored Markdown]
    Packages/MarkdownEditing/Markdown (Standard).sublime-settings
    Packages/MarkdownEditing/MultiMarkdown.sublime-settings

Bold and italic markers are configurable through ST shell variables. You can use `Preferences > Package Settings > Markdown Editing` menu to see the default settings file. In order to override it, copy & paste its content into the user settings file (`Bold and Italic Markers.tmPreferences`) from the menu and make your edits. It is pretty straightforward.

In order to activate the dark or the yellow theme, put one of these lines to your user settings file of the flavor:

    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Dark.tmTheme",
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-Yellow.tmTheme",

If you want to go with your already existing theme, you can reenable it with the same method as dark theme. Keep in mind that, that theme may not cover all the parts of the Markdown syntax that this plugin defines.

## Tips

* Sublime Text has a _Distraction Free_ mode which is great with Markdown writing. Key binding for it: <kbd>Shift</kbd> <kbd>F11</kbd>.

* If you work with Markdown tables too often, you may want to have a look at another plugin named [TableEditor][]. It brings huge improvements for table editing. Several table formats are supported.

* There is a plugin named [Typewriter][] which provides a typewriter like writing environment. Excerpt from its homepage:

    > __Typewriter Typing__ disables your cursor keys and all bindings that move the cursor and/or select text, leaving you only with letters, numbers, symbols, <kbd>Backspace</kbd>, <kbd>Delete</kbd> and <kbd>Enter</kbd>.

* Markdown files usually contains URLs. If you want to open URLs under the cursor with a keybinding, you may want to install [OpenUrl][] plugin. It will work on other file types, too.

## Similar Plugins

* [Knockdown][]

     Knockdown offers useful Markdown features and a custom Markdown theme. All of its unique features except its theme are ported to MarkdownEditing and some of them are actually improved further in MarkdownEditing.
* [Sublime Markdown Extended][]
* [SmartMarkdown][]

## Contributing

See `CONTRIBUTING.md` file.

## Credits

MarkdownEditing was originally created by [Brett Terpstra][brettterpstra] and has become a community project with the goal of consolidating the best features from the varied collection of Markdown packages for Sublime Text. Current development is headed up by [Ali Ayas][github 9].

This plugin contains portions of code from [Knockdown][].

Footnote commands were submitted by [J. Nicholas Geist][github 4] and originated at [geekabouttown][geekabouttown].

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
