# Contributing

## Where to Begin

Development is proceeding in development branches for compatible ST builds:

| develop branch  | target branch | ST builds
| ---             | ---           | ---
| st3-develop     | ST3176        | 3176 - 4106
| st4-develop     | master        | 4107...

> **Note**
>
> Currently main difference between ST3 and ST4 branches
> is syntax definition using `version: 2` in ST4.

Common improvements for ST3 and ST4 should be based on and merged into `st3-develop`.
It is frequently merged into `st4-develop`, if required.

Only changes, which require ST4, are based on and merged directly into `st4-develop`.

New releases will be created, if enough or critical fixes are available.

Release version number will be determined based on amount and kind of changes.

## General Guidelines

* Code formatting:
    - __Indentation__: 4 spaces
    - __Line endings__: `\n`

* If your contribution deserves a place in `README.md`, please do so. 
  Preferably in the same commit with your modifications.

  Consider updating 

* We create __changelog__ files for Package Manager updates. 
  They are under `messages/` directory.

    If your contribution deserves a place under one of 
    the "Bug Fixes", "New Features", "Changes" titles, 
    please do so. 
    Preferably in the same commit with your modifications.

    Changelog is created in `messages/next.md`.
    It will be renamed to match release version number
    as part of the release workflow.

* If you are defining a new __key binding__, 
  please define for all the 3 OSs in their own `.sublime-keymap` files. 
  You have to insert your edits into the exactly same place in the 3 files.

* Setting keys are added to one of the `.sublime-settings` files,
  using `mde.` prefix and a description comment.

* For testing your changes, you can use the test files under `tests/`. 
  You can extend those files to add new tests and edge cases.

## Publishing to Package Control

> **Note**
>
> For push-access users, only!

For each target:

1. check and update changelog.
2. determine version number.
3. rename changelog `messages/next.md` to `messages/<version>.md`
4. add a corresponding entry in `messages.json`
5. merge development branch into target branch (e.g.: `st3-develop` => `st3176`)
6. create and push a tag in form `<build>-<version>` (e.g. `3176-2.3.4`)

The update process may take __up to an hour__ 
depending on the crawl frequency by the Package Control.

## Contributing to themes

Here are the used scopes under 3 different markdown flavors.
If you are not sure about how the scopes are used, 
checkout .sublime-syntax files or ask in issues.
__Unique__ scopes are marked as bold.

### ScopeName: text.html.markdown

* constant.character.escape.markdown
* constant.other.reference.link.markdown
* invalid.illegal.whitespace.markdown
* markup.bold.markdown
* markup.bold_italic.markdown
* markup.heading.1.markdown
* markup.heading.2.markdown
* markup.heading.markdown
* markup.italic.markdown
* markup.list.numbered.markdown
* markup.list.unnumbered.markdown
* markup.quote.markdown
* markup.raw.block.markdown
* markup.raw.inline.content.markdown
* markup.raw.inline.markdown
* markup.underline.link.image.markdown
* markup.underline.link.markdown
* meta.block-level.markdown
* meta.disable-markdown
* meta.dummy.line-break
* meta.image.inline.markdown
* meta.image.reference.markdown
* meta.link.email.lt-gt.markdown
* meta.link.inet.markdown
* meta.link.inline.markdown
* meta.link.reference.def.markdown
* meta.link.reference.literal.markdown
* meta.link.reference.markdown
* meta.other.valid-ampersand.markdown
* meta.other.valid-bracket.markdown
* meta.paragraph.list.markdown
* meta.paragraph.markdown
* meta.separator.markdown
* punctuation.definition.blockquote.markdown
* punctuation.definition.bold.markdown
* punctuation.definition.constant.begin.markdown
* punctuation.definition.constant.end.markdown
* punctuation.definition.constant.markdown
* punctuation.definition.heading.markdown
* punctuation.definition.italic.markdown
* punctuation.definition.link.markdown
* punctuation.definition.list_item.markdown
* __punctuation.definition.list_item.number.markdown__
* punctuation.definition.metadata.markdown
* punctuation.definition.raw.markdown
* punctuation.definition.string.begin.markdown
* punctuation.definition.string.end.markdown
* punctuation.definition.string.markdown
* punctuation.separator.key-value.markdown

### ScopeName: text.html.markdown.gfm

* constant.character.escape.markdown
* constant.other.reference.link.markdown
* __entity.name.tag.other.html__
* invalid.illegal.whitespace.markdown
* markup.bold.markdown
* markup.bold_italic.markdown
* markup.heading.1.markdown
* markup.heading.2.markdown
* markup.heading.markdown
* markup.italic.markdown
* __markup.kbd.content.markdown__
* __markup.kbd.markdown__
* markup.list.numbered.markdown
* markup.list.unnumbered.markdown
* markup.quote.markdown
* __markup.raw.block.fenced.markdown__
* markup.raw.block.markdown
* markup.raw.inline.content.markdown
* markup.raw.inline.markdown
* __markup.strikethrough.markdown__
* markup.underline.link.image.markdown
* markup.underline.link.markdown
* meta.block-level.markdown
* meta.disable-markdown
* meta.dummy.line-break
* meta.image.inline.markdown
* meta.image.reference.markdown
* meta.link.email.lt-gt.markdown
* meta.link.inet.markdown
* meta.link.inline.markdown
* meta.link.reference.def.markdown
* meta.link.reference.literal.markdown
* meta.link.reference.markdown
* meta.other.valid-ampersand.markdown
* meta.other.valid-bracket.markdown
* meta.paragraph.list.markdown
* meta.paragraph.markdown
* meta.separator.markdown
* __meta.tag.other.html__
* punctuation.definition.blockquote.markdown
* punctuation.definition.bold.markdown
* punctuation.definition.constant.begin.markdown
* punctuation.definition.constant.end.markdown
* punctuation.definition.constant.markdown
* punctuation.definition.heading.markdown
* punctuation.definition.italic.markdown
* punctuation.definition.link.markdown
* punctuation.definition.list_item.markdown
* punctuation.definition.metadata.markdown
* punctuation.definition.raw.markdown
* __punctuation.definition.strikethrough.markdown__
* punctuation.definition.string.begin.markdown
* punctuation.definition.string.end.markdown
* punctuation.definition.string.markdown
* __punctuation.definition.tag.begin.html__
* __punctuation.definition.tag.end.html__
* punctuation.separator.key-value.markdown

### ScopeName: text.html.markdown.multimarkdown

* &lt;All scopes under text.html.markdown.gfm&gt;
* __keyword.other.multimarkdown__
* __punctuation.separator.key-value.multimarkdown__
* __meta.header.multimarkdown__
* __string.unquoted.multimarkdown__
* __meta.content.multimarkdown__