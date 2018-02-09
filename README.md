# MarkdownEditing

Markdown plugin for Sublime Text. Provides a decent Markdown color scheme (light and dark) with more __robust__ syntax highlighting and useful Markdown editing features for Sublime Text. 3 flavors are supported: Standard Markdown, __GitHub flavored Markdown__, MultiMarkdown.

![MarkdownEditing][LightTheme]

[Dark][DarkTheme] and [Yellow][YellowTheme] and [ArcDark][ArcDarkTheme] theme available, plus [thirdparty themes](#additional-color-themes). See [configuration](#configuration) section to learn **how to change the theme**.

## Overview

<!-- MarkdownTOC autolink="true" bracket="round" markdown_preview="markdown" -->

- [Installation](#installation)
    - [Package Control](#package-control)
    - [Manual Installation](#manual-installation)
- [Features](#features)
    - [Markdown features](#markdown-features)
    - [Wiki features](#wiki-features)
- [Key Bindings](#key-bindings)
- [GFM Specific Features](#gfm-specific-features)
- [Commands for Command Palette](#commands-for-command-palette)
    - [General Commands](#general-commands)
    - [Links, References and Footnotes](#links-references-and-footnotes)
    - [Folding and Navigation](#folding-and-navigation)
- [Configuration](#configuration)
    - [Additional color themes:](#additional-color-themes)
- [Tips](#tips)
- [Enable WYSIWYG](#enable-wysiwyg)
- [Troubleshooting](#troubleshooting)
    - [Error loading syntax file...](#error-loading-syntax-file)
    - [Roll back to an older version](#roll-back-to-an-older-version)
- [Related Plugins](#related-plugins)
- [Known Bugs](#known-bugs)
- [Contributing](#contributing)
- [Credits](#credits)
- [Donation](#donation)
- [License](#license)

<!-- /MarkdownTOC -->

## Installation

You can install MarkdownEditing either from Package Control (recommended) or manually. Package Control automatically download the package and keeps it up-to-date. Manual installation is required if you need to tweak the code.

If you are using Sublime Text 2, you have to disable the native package _manually_. To do that, add `Markdown` to your `ignored_packages` list in ST user settings:

    "ignored_packages": [..., "Markdown"],

> Getting "Error loading syntax file..."? See [this](#error-loading-syntax-file).

### Package Control

The preferred method of installation is via [Sublime Package Control][PackageControl].

1. [Install Sublime Package Control][InstallPackageControl]
2. From inside Sublime Text, open Package Control's Command Pallet: <kbd>CTRL</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> (Windows, Linux) or <kbd>CMD</kbd> <kbd>SHIFT</kbd> <kbd>P</kbd> on Mac.
3. Type `install package` and hit Return. A list of available packages will be displayed.
4. Type `MarkdownEditing` and hit Return. The package will be downloaded to the appropriate directory.
5. Restart Sublime Text to complete installation. Open a Markdown file and this custom theme. The features listed below should now be available.

### Manual Installation

1. In Sublime Text, open the menu "Preferences" -> "Browse Packages...". This is the Sublime Text Packages directory.
2. [Download and unzip](https://github.com/SublimeText-Markdown/MarkdownEditing/archive/master.zip) or [clone](https://help.github.com/articles/cloning-a-repository/) this repository to a directory `MarkdownEditing` in the Sublime Text Packages directory.
3. The folder structure should look like `.../Sublime Text 3/Packages/MarkdownEditing/[files]`.
4. Restart Sublime Text to complete installation. Open a Markdown file. The features listed below should now be available.

## Features

You can access most features through Command Palette. You can launch it from `Tools -> Command Palette...`. MarkdownEditing commands start with `MarkdownEditing:`. And they are only visible when a markdown file is open and active.

### Markdown features

* __Pairing__
    - Asterisks and underscores are autopaired and will wrap selected text.
    - If you start an empty pair and hit backspace, both elements are deleted.
    - If you start an empty pair and hit space, the right element is deleted.
    - Backticks are paired. So entering `` ` `` will expand to `` `(cursor here)` ``.
* __List__
    - At the end of a list item, pressing <kbd>Enter</kbd> will automatically insert the new list item bullet.
    - Pressing <kbd>Tab</kbd> on the blank list item will indent it and switch the list bullet to another one (Order is `*`, `-`, `+` in a cycle).
    - Pressing <kbd>Shift</kbd> <kbd>Tab</kbd> on the blank list item will unindent it in the same way as above.
    - Sequential <kbd>Tab</kbd> s or <kbd>Shift</kbd> <kbd>Tab</kbd> s are supported.
    - You can disable automatic bullet switching or choose which bullets to be used, in your settings file (`mde.list_indent_bullets`).
    - If a list item contains a [GFM task][], pressing <kbd>Enter</kbd> at the end of the line will continue with a new blank task.
* __Blockquote__
    - At the end of a blockquote line, pressing <kbd>Enter</kbd> will automatically extend blockquote.
    - Selecting some text and pressing <kbd>&gt;</kbd> will convert it to blockquote. The first and the last line don't have to be fully selected; partial select works, too.
* __Link__
    - Left bracket pairing is modified to eliminate the selection and leave the cursor at a point where you can insert a `[]` or `()` pair for a link.
    - If you leave the cursor on a link, you can right click and jump between reference and url.
* __Navigation__
    - Displays Markdown headers in the Project Symbol List (`Goto -> Goto Symbol in Project...`). They will start with `#`, so you will know they belong to markdown files at a glance. Also they will be on top of the list because of the precedence of `#`.
    - Headers also appear in Document Symbol List (`Goto -> Goto Symbol...`)
    - You can fold current section with <kbd>Ctrl</kbd> <kbd>Tab</kbd>
    - You can navigate between adjacent headers with `Find Next(Previous) Heading` command.
* __Strikethrough__
    - <kbd>~</kbd> wraps selected text with `~~` (strikethrough). When you for instance select the word "foo" and hit  `~`, the result will be `~~foo~~`.
* __Header__
    - Typing `#` when there's a selection will surround it with `#` to make it a headline. Multiple presses add additional hashes, increasing the level of the header. Once you hit 6 hashes, it will reset to 0 on the next press. The `mde.match_header_hashes` will determine if the `#` are mirrored on both sides or just at the beginning of the line.
    - Typing return at the end of a line that begins with hashmarks will insert closing hashmarks on the headline. They're not required for Markdown, it's just aesthetics, and you can change the `mde.match_header_hashes` option in your settings to enable (disabled by default).
    - Setext-style headers can be completed with `Tab`. That is, typing `Tab` on a line containing only `=` or `-` characters will add or remove enough characters to it to match the length of the line above.
    - New documents will be named automatically based on the first header.

### Wiki features

Wiki links are defined by surrounding a (wiki) word with double square brackets, for example:

    [[SampleWikiPage]]

The user can `open` wiki page using a sublime command.  This will search the current open file's directory (and sub-directories) for a file with a matching name and a markdown extension.  For example, opening the previous wiki link
will look for and open a file named:

    SampleWikiPage.md

Note that, if the wiki page does *not* yet exist, if will be created with a header matching the page name.  However the file will only actually be created on the file system, when it is saved by the user.  

The user can `list back links` and of course to open them.  Back links are pages that reference the current page.  This allows pages to be tied together into a personal wiki.   A common technique is to define *tag* wiki pages and to list any tags for a page as references to the tag pages at the bottom of the page, for example:
    
    [[TagSyntax]] [[TagDev]] [[TagPython]]

This allows the user to list all pages with a specific tag, by opening the tag page and list all back links.

Journal wiki pages are also supported.  A journal page is just a wiki page with a name matching the current date.

Lastly the command to open the *home* page is provided, where the home page is just a wiki page named `HomePage`.

## Key Bindings

| OS X | Windows/Linux | Description |
|------|---------------|-------------|
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>V</kbd> | <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>V</kbd> | Creates or pastes the contents of the clipboard as an inline link on selected text.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>R</kbd> | <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>R</kbd> | Creates or pastes the contents of the clipboard as a reference link.
| <kbd>⌘</kbd><kbd>⇧</kbd><kbd>K</kbd> | <kbd>Shift</kbd><kbd>Win</kbd><kbd>K</kbd> | Creates or pastes the contents of the clipboard as an inline image on selected text.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>B</kbd> <kbd>⌘</kbd><kbd>⌥</kbd><kbd>I</kbd> | <kbd>Alt</kbd><kbd>B</kbd> <kbd>Alt</kbd><kbd>I</kbd> | These are bound to bold and italic. They work both with and without selections. If there is no selection, they will just transform the word under the cursor. These keybindings will unbold/unitalicize selection if it is already bold/italic.
| <kbd>⌘</kbd><kbd>^</kbd><kbd>1...6</kbd> | <kbd>Ctrl</kbd><kbd>1...6</kbd> | These will add the corresponding number of hashmarks for headlines. Works on blank lines and selected text in tandem with the above headline tools. If you select an entire existing headline, the current hashmarks will be removed and replaced with the header level you requested. This command respects the `mde.match_header_hashes` preference setting.
| <kbd>⌥</kbd><kbd>⇧</kbd><kbd>6</kbd> | <kbd>Alt</kbd><kbd>Shift</kbd><kbd>6</kbd> | Inserts a footnote.
| <kbd>⇧</kbd><kbd>Tab</kbd> | <kbd>Shift</kbd><kbd>Tab</kbd> | Fold/Unfold current section.
| <kbd>^</kbd><kbd>⇧</kbd><kbd>Tab</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>Tab</kbd> | Fold all sections under headings of a certain level.
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>PageUp</kbd> <kbd>⌘</kbd><kbd>⌥</kbd><kbd>PageDown</kbd> | <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Shift</kbd><kbd>PageUp</kbd> <kbd>Ctrl</kbd><kbd>Alt</kbd><kbd>Shift</kbd><kbd>PageDown</kbd> | Go to the previous/next heading of the same or higher level
| <kbd>⌘</kbd><kbd>⇧</kbd><kbd>PageUp</kbd> <kbd>⌘</kbd><kbd>⇧</kbd><kbd>PageDown</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>PageUp</kbd> <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>PageDown</kbd> |  Go to the previous/next heading
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>H</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>H</kbd> | Open home page
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>D</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>D</kbd> | Open wiki page under the cursor
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>J</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>J</kbd> | Open journal page for today
| <kbd>⌘</kbd><kbd>⌥</kbd><kbd>B</kbd> | <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>B</kbd> | List back links


## GFM Specific Features

[GFM][] means GitHub Flavored Markdown is the dialect of Markdown that is currently supported for user content on GitHub.com and GitHub Enterprise. It has [some unique features][GFMFeatures]:

Underscores in words doesn't mess with bold or italic style:

![underscore-in-words][GFM-UnderscoreInWords]

Fenced code blocks gets syntax highlighting inside:

![fenced-code-block][GFM-FencedCodeBlock]

Keyboard shortcuts gets highlighted like in GitHub:

![keyboard-shortcut][GFM-KeyboardShortcut]

Strikethrough is supported:

![strikethrough][GFM-Strikethrough]

## Commands for Command Palette

You can launch Command Palette from `Tools -> Command Palette...`. MarkdownEditing commands start with `MarkdownEditing:`. And they are only visible when a markdown file is open and active.

### General Commands

* __Fix Underlined Headers__
    Adjusts every setext-style header to add or remove `=` or `-` characters as needed to match the lengths of their header text.
* __Convert Underlined Headers to ATX__
    Converts every setext-style header into an ATX style header. If something is selected only the headers in the selections will be converted, otherwise the conversion will be applied to the whole view.
* __Markdown Lint__
    Performs lint on current Markdown file using a local linter. See [lint rules](lint_docs/RULES.md). Some of the linting rules are customizable via user settings file.
* __Run markdownlint__
    Run mdl command from [markdownlint](https://github.com/markdownlint/markdownlint) package. You need to install it by yourself.
* __Change color scheme...__
    Lists built-in Markdown color schemes for you to preview and use.
* __Switch List Bullet Type__
    Switches the highlighted list between numbered and bulleted style.

### Links, References and Footnotes

* __Add Missing Link Labels__
    Scans document for referenced link usages (`[some link][some_ref]` and `[some link][]`) and checks if they are all defined. If there are undefined link references, command will automatically create their definition snippet at the bottom of the file.
* __Magic Footnotes Command__
    Adds a footnote after the word under cursor. If cursor is already on a footnote, jumps to its definition or reference.
* __Gather Missing Footnotes__
    Add definition stubs (if there is none) for all footnotes references.
* __Jump Reference__
    Jumps cursor between definitions and references.
* __New Reference__
    Adds a new link under cursor.
* __New Inline Link__
    Adds a new inline link under cursor.
* __New Inline Image__
    Adds a new inline image under cursor.
* __New Image__
    Adds a new image under cursor.
* __New Footnote__
    Adds a footnote under cursor.
* __Delete Reference__
    Deletes the definition and references of a link.
* __Organize References__
    Sorts and gives a report on current link references usage.

### Folding and Navigation

Remeber you can <kbd>Ctrl</kbd> <kbd>R</kbd> (in document) and <kbd>Ctrl</kbd> <kbd>Shift</kbd> <kbd>R</kbd> (project-wise) for quick navigation for all headers.

* __Toggle Folding Current Section__
    Folds/unfolds current section.
* __Fold Level 1-4 Sections__
    Fold all sections under headers of specific level.
* __Fold/Unfold All Sections__
    Self explanatory.
* __Find Next/Previous Heading__
    You have option to find just same or higher level or any level

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
    "color_scheme": "Packages/MarkdownEditing/MarkdownEditor-ArcDark.tmTheme",
    

If you want to go with your already existing theme, you can reenable it with the same method as above. Keep in mind that, that theme may not cover all the parts of the Markdown syntax that this plugin defines.

### Additional color themes:

- [Blackboard theme][linkBlackboardTheme] by [@mdesantis][mdesantis]
- [monokaiC](https://github.com/avivace/monokaiC) by [@avivace][avivace]

By default, when you install the plugin, files with these extensions will be assigned to Markdown syntax: "md", "txt", "mdown", "markdown", "markdn". If you want to prevent any of these extensions to be opened as Markdown, follow these steps:

1. Click on the language menu at bottom right
2. Select "Open all with current extension as"
3. Choose your preferred syntax for that extension

## Tips

We are maintaining a [tips section][tips] in our [Wiki][]. Jump there to learn from others or share your experiences with others.

## Enable WYSIWYG

Sublime can be configured into a WYSIWYG (what you see is what you get) editor with two other plugins:

1. Markdown Preview (https://packagecontrol.io/packages/Markdown%20Preview)
1. Livereload (https://packagecontrol.io/packages/LiveReload)

Install them if you haven't. Then

1. Open Palette
1. LiveReload: Enable/Disable Plugins
1. Enable Simple Reload.

Now open palette and choose "Preview in Browser" and you will get a WYSIWYG editor.

## Troubleshooting

### Error loading syntax file...

__Are you getting this error after installation: _**Error loading syntax file** "Packages/Markdown/Markdown.tmLanguage": Unable to open Packages/Markdown/Markdown.tmLanguage_?__

>  This is caused by open markdown files at the install time. You have to __manually change their syntax to your newly installed Markdown syntax__. Read the below paragraph for more details on this.

_Note_: Sublime text has a native tiny package for Markdown. However, when MarkdownEditing is enabled, native package causes some conflicts. For this reason, MarkdownEditing will automatically disable it. Since it doesn't bring anything new over MarkdownEditing, this is not a loss. But remember, when you disable MarkdownEditing, you have to reenable the native one manually (if you want).

### Roll back to an older version

When you notice any undesired behavior introduced by the latest update, your feedback is always welcome in our [issue page](https://github.com/SublimeText-Markdown/MarkdownEditing/issues). However before it's fixed, you can rollback to [an earlier version](https://github.com/SublimeText-Markdown/MarkdownEditing/releases). Find the desired version and download the zip file, then follow [manual installation guide](#manual-installation)

## Related Plugins

* [Knockdown][]

     Knockdown offers useful Markdown features and a custom Markdown theme. All of its unique features except its theme are ported to MarkdownEditing and some of them are actually improved further in MarkdownEditing.
* [Sublime Markdown Extended][]
* [SmartMarkdown][]
* [MarkdownTOC][]
    - Sublime Text 3 plugin for generating a Table of Contents (TOC) in a Markdown document.
* See https://packagecontrol.io/search/markdown for more.

## Known Bugs

* Setext-style headers (`===` and `---`) do not show up in the symbol list. This is due to a Sublime Text limitation (see [#158][]). However, we are able to put a placeholder to indicate the existence of the header. We encourage you to use Atx-style headers (`#`).

* Installing for the first time while having markdown files opened may cause MarkdownEditing to behave unexpectedly on those files. Close and reopen those files to fix it.

## Contributing

See `CONTRIBUTING.md` file.

## Credits

MarkdownEditing was originally created by [Brett Terpstra][brettterpstra] and has become a community project with the goal of consolidating the best features from the varied collection of Markdown packages for Sublime Text. Current development is headed up by [Ali Ayas][maliayas] and [Felix Hao][felixhao28].

Related blog posts from Brett:
* http://brettterpstra.com/2012/05/17/markdown-editing-for-sublime-text-2-humble-beginnings/
* http://brettterpstra.com/2013/11/23/markdownediting-for-sublime-text-updates/

This plugin contains portions of code from [Knockdown][].

Footnote commands were submitted by [J. Nicholas Geist][] and originated at [geekabouttown][geekabouttown].

## Donation

You can support [contributors](https://github.com/SublimeText-Markdown/MarkdownEditing/graphs/contributors) of this project individually. Every contributor is welcomed to add his/her line below with any content. Ordering shall be alphabetically by GitHub username.

* [@felixhao28][felixhao28]: <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=9QV2RFV2J8UZS"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="[paypal]" /></a>
* [@maliayas][maliayas]: <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_donations&amp;business=W2NXRPD43YSCU&amp;lc=TR&amp;item_name=open-source&amp;item_number=markdown-editing&amp;currency_code=USD&amp;bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHosted"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" alt="[paypal]" /></a> ![donation received](http://maliayas.com/business/donation/badge.php?project=markdown_editing)

## License

MarkdownEditing is released under the [MIT License][opensource].

[LightTheme]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/light.png
[DarkTheme]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/dark.png
[YellowTheme]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/yellow.png
[ArcDarkTheme]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/arcdark.png
[PackageControl]: http://wbond.net/sublime_packages/package_control
[InstallPackageControl]: http://wbond.net/sublime_packages/package_control/installation
[GFM task]: https://github.github.com/gfm/#task-list-items-extension-
[GFM]: https://github.github.com/gfm/
[GFMFeatures]: https://guides.github.com/features/mastering-markdown/
[GFM-UnderscoreInWords]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/underscore-in-words.png
[GFM-FencedCodeBlock]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/fenced-code-block.png
[GFM-KeyboardShortcut]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/keyboard-shortcut.png
[GFM-Strikethrough]: https://raw.github.com/SublimeText-Markdown/MarkdownEditing/master/screenshots/strikethrough.png
[linkBlackboardTheme]: https://github.com/mdesantis/MarkdownEditing/blob/blackboard-theme/MarkdownEditor-Blackboard.tmTheme
[mdesantis]: https://github.com/mdesantis
[avivace]: https://github.com/avivace
[tips]: https://github.com/SublimeText-Markdown/MarkdownEditing/wiki/Tips
[Wiki]: https://github.com/SublimeText-Markdown/MarkdownEditing/wiki
[Knockdown]: https://github.com/aziz/knockdown/
[Sublime Markdown Extended]: https://github.com/jonschlinkert/sublime-markdown-extended
[SmartMarkdown]: https://github.com/demon386/SmartMarkdown
[MarkdownTOC]: https://github.com/naokazuterada/MarkdownTOC
[#158]: https://github.com/SublimeText-Markdown/MarkdownEditing/issues/158
[brettterpstra]: http://brettterpstra.com
[maliayas]: https://github.com/maliayas
[felixhao28]: https://github.com/felixhao28
[J. Nicholas Geist]: https://github.com/jngeist
[geekabouttown]: http://geekabouttown.com/posts/sublime-text-2-markdown-footnote-goodness
[opensource]: http://www.opensource.org/licenses/MIT
