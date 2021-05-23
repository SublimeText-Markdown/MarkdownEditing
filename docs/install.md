# Installation

## Package Control

It is highly recommended to install MarkdownEditing with [Package Control](https://packagecontrol.io) as it automatically installs required dependencies and keeps all packages up to date.

1.   [Install Package Control][InstallPackageControl] if you haven't yet.
2.   Open Command Palette (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> (Windows, Linux) or
     <kbd>⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> on Mac)
3.   Type _Install Package_ and hit <kbd>Enter</kbd> to display a list of available packages.
4.   Type _MarkdownEditing_ and hit <kbd>Enter</kbd> to install the package.

### Pre-Releases

If you are interested in testing bleeding edge features you can set up Package Control
to install pre-releases by adding MarkdownEditing to `install_prereleases` key 
in the `Package Control.sublime-settings`.

```JSON
"install_prereleases":
[
  "MarkdownEditing"
],
```

## Manual installation

1.   In Sublime Text, open the menu _Preferences > Browse Packages..._. 
     This is the Sublime Text Packages directory.
2.   [Download and unzip][download] or [clone][] this repository to a directory _MarkdownEditing_ 
     in the Sublime Text Packages directory.
3.   The folder structure should look like `[...]/Packages/MarkdownEditing/[files]`.

### Cloning Repository

##### Mac OS

```shell
cd ~/Library/Application\ Support/Sublime\ Text/Packages/
git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git
```

##### Linux

```shell
cd ~/.config/sublime-text/Packages
git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git
```

##### Windows

```shell
cd "%APPDATA%\Sublime Text\Packages"
git clone https://github.com/SublimeText-Markdown/MarkdownEditing.git
```

!!! note
    Destination paths may differ depending on Sublime Text version.

[InstallPackageControl]: https://packagecontrol.io/installation
[download]: https://github.com/SublimeText-Markdown/MarkdownEditing/archive/master.zip
[clone]: https://help.github.com/articles/cloning-a-repository
