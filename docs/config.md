# Configuration

Default MarkdownEditing related configuration is located in _Preferences.sublime-settings_ as of version 3.0.0 to take full advantage of [settings file loading hierarchies](https://www.sublimetext.com/docs/settings.html#settings_files).

It means you can specify

*   global preferences which apply to all Markdown flavours in `Preferences.sublime-settings`
*   project specific settings in your `[Project].sublime-project`
*   syntax specific settings for a certain Markdown flavour in `[Syntax Name].sublime-settings`
*   settings for distraction free mode in `Distraction Free.sublime-settings`

All MarkdownEditing related settings are prefixed with `mde.`.

!!!note "Migration Note"
    You may need or want to clean up existing syntax specific settings.

    _MarkdownEditing no longer modifies visual settings such as caret width or line paddings._

## Change Configuration

Configuration can be modified via main menu and Command Palette. Using the following commands displays default MarkdownEditing settings on the left and your user preferences on the right.

*   In _Main Menu_ navigate to: `Preferences > Package Preferences > MarkdownEditing`
*   In _Command Palette_ look for: `Preferences: MarkdownEditing ...`

!!!note "Package Recommendation"
    [PackageDev](https://packagecontrol.io/packages/PackageDev) may assist you by providing auto-completion for known preferences.

## Change Color Scheme

You can use your global color scheme or one of those shipped with MarkdownEditing for working in Markdown. To change color scheme:

1.   Open Command Palette (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> for Windows/Linux, <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> for Mac OS)
3.   Search for _MarkdownEditing: Select Color Scheme_ and hit <kbd>Enter</kbd>.
4.   Choose color scheme and press <kbd>Enter</kbd>.

#### Additional Color Schemes:

- [Blackboard theme](https://github.com/mdesantis/MarkdownEditing/blob/blackboard-theme/MarkdownEditor-Blackboard.tmTheme) by [@mdesantis](https://github.com/mdesantis)
- [monokaiC](https://github.com/avivace/MonokaiC/blob/master/themes/ME-MonokaiC.tmTheme) by [@avivace](https://github.com/avivace)

!!!note "Custom Color Schemes"
    MarkdownEditing lists all color schemes named like `MarkdownEditor-<The Name>.sublime-color-scheme`, no matter which package they are placed in.

## Assigning Syntax

The following file extensions are assigned with Markdown by default: `*.md`, `*.mdown`, `*.markdn`, `*.markdown`. If you want to prevent any of these extensions to be opened as Markdown or assign them another Markdown flavour:

1. Click on the language menu at bottom right of statusbar
2. Select _Open all with current extension as_
3. Choose your preferred syntax for that extension

or use main menu `View > Syntax > Open all with current extension as`.

## Markdown Preview

MarkdownEditing doesn't provide functions to preview or convert markdown to HTML. Automatic preview can be achieved with both of:

1.   [Markdown Preview](https://packagecontrol.io/packages/Markdown%20Preview)
2.   [Livereload](https://packagecontrol.io/packages/LiveReload)

Install them if you haven't. Then

1.   Open Command Palette (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> for Windows/Linux, <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> for Mac OS)
2.   Search for _LiveReload: Enable/Disable Plugins_
3.   Enable Simple Reload.
4.   Open Command Palette again
5.   Search for _Markdown Preview: Preview in Browser_
