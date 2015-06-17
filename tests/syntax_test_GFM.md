<!-- SYNTAX TEST "Packages/MarkdownEditing/Markdown.tmLanguage" -->

Inline styles
=============

_italic_
<!-- <- punctuation.definition.italic.markdown -->
<!-- ^ markup.italic.markdown -->
<!--   ^ punctuation.definition.italic.markdown -->

<!-- !!Currently ST3 syntax testing has no "not equal/contain" test -->
_italic one_ not italic _italic two_
<!-- <- punctuation.definition.italic.markdown -->
<!-- ^ markup.italic.markdown -->
<!--       ^ punctuation.definition.italic.markdown -->
<!--           ^ meta.paragraph.markdown -->
<!--                    ^ punctuation.definition.italic.markdown -->
<!--                        ^ markup.italic.markdown -->
<!--                               ^ punctuation.definition.italic.markdown -->

_italic\__
<!--   ^ constant.character.escape.markdown -->
<!--    ^ constant.character.escape.markdown -->

_italic \__
<!--    ^ constant.character.escape.markdown -->
<!--     ^ constant.character.escape.markdown -->

stuff * not italic*
<!--  ^ meta.paragraph.markdown -->
<!--      ^ meta.paragraph.markdown -->
<!--              ^ meta.paragraph.markdown -->

*italic__*
<!--    ^ markup.italic.markdown -->

_all _ italic_
<!--^ markup.italic.markdown -->
<!-- ^ markup.italic.markdown -->
<!--  ^ markup.italic.markdown -->

_italic
end italic_
<!-- !!Not supported, see issue #103 -->

\\\\_italic\\_
<!--    ^ markup.italic.markdown -->

\\\\_italic\\\_\\\\_
<!--    ^ markup.italic.markdown -->

\\\\_italic\\_
<!--    ^ markup.italic.markdown-->

\_ not italic _
<!--    ^ meta.paragraph.markdown -->

_not italic _
<!--    ^ meta.paragraph.markdown -->

\\\\_not italic\_
<!--    ^ meta.paragraph.markdown -->

_not italic \_
<!--    ^ meta.paragraph.markdown -->

\\\_not italic\\_
<!--    ^ meta.paragraph.markdown -->

_not italic
<!--    ^ meta.paragraph.markdown -->

not end italic_
<!--    ^ meta.paragraph.markdown -->

__bold__
<!-- <- punctuation.definition.bold.markdown -->
<!--^ markup.bold.markdown -->
<!--   ^ punctuation.definition.bold.markdown -->

**bold\***
<!-- <- punctuation.definition.bold.markdown -->
<!--     ^ punctuation.definition.bold.markdown -->
<!-- ^ markup.bold.markdown -->
<!--   ^ markup.bold.markdown -->
<!--   ^ constant.character.escape.markdown -->

___bold_and_italic___
<!--       ^ markup.bold_italic.markdown -->

***bold_and_italic***
<!--   ^ markup.bold_italic.markdown -->

`raw more`
<!-- <- punctuation.definition.raw.markdown -->
<!-- ^ markup.raw.inline.content.markdown -->
<!--     ^ punctuation.definition.raw.markdown -->

``dobule ` raw``
<!-- <- punctuation.definition.raw.markdown -->
<!--     ^ markup.raw.inline.content.markdown -->
<!--           ^ punctuation.definition.raw.markdown -->

Headings
================
<!-- ^ markup.heading.1.markdown -->
<!-- ^ punctuation.definition.heading.markdown -->

heading 2
----------
<!-- ^ markup.heading.2.markdown -->
<!-- ^ punctuation.definition.heading.markdown -->

## heading 2
<!--<- punctuation.definition.heading.markdown -->
<!--^ entity.name.section.markdown -->

### heading 3
<!--<- punctuation.definition.heading.markdown -->
<!--  ^ entity.name.section.markdown -->

###### heading 6
<!--<- punctuation.definition.heading.markdown -->
<!--           ^ entity.name.section.markdown -->

Horizontal lines
=================

***
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->

* * *
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->

___
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->

__ __ __
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->
<!--   ^ meta.separator.markdown -->

- - - 
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->
<!--^ meta.separator.markdown -->

----------------
<!-- <- meta.separator.markdown -->
 <!-- <- meta.separator.markdown -->
  <!-- <- meta.separator.markdown -->
<!--           ^ meta.separator.markdown -->

Block formatting
================

Lists
----------------

 * This *is a list!*
 <!-- <- punctuation.definition.list_item.markdown -->
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
 <!--      ^ markup.list.unnumbered.markdown -->
 <!--      ^ meta.paragraph.list.markdown -->
 * This is another list item.
   But this one spans *two* lines. 
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
 <!--                   ^ markup.list.unnumbered.markdown -->
 <!--                   ^ meta.paragraph.list.markdown -->
 * Another list item with __inline__ formatting
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
 <!--                        ^ markup.list.unnumbered.markdown -->
 <!--                        ^ meta.paragraph.list.markdown -->
 <!--                        ^ markup.bold.markdown -->
 * This one is tricky  
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
 <!--                 ^ meta.dummy.line-break -->
 * *This is a list*
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
 <!-- ^ markup.italic.markdown -->

   Because this should still be a list item.
 <!-- ^ markup.list.unnumbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->

1. This is a list item too
 <!-- ^ markup.list.numbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->
2. This list is numbered
 <!-- ^ markup.list.numbered.markdown -->
 <!-- ^ meta.paragraph.list.markdown -->

1986\. This shouldn't be a list.
<!-- ^ meta.paragraph.markdown -->

Code block
---------------

    asdfsdafasdf
    This is code.
    Isn't it pretty!
<!-- ^ markup.raw.block.markdown -->
Quotes
---------------

> Here is a quote block
<!-- <- punctuation.definition.blockquote.markdown -->
<!-- ^ markup.quote.markdown -->
This quote continues on.  Line breaking is OK in markdown
<!-- ^ markup.quote.markdown -->
> Here it is again
> Lah-di-dah
> I should really match headings in here too:
> ## This is a heading in a block quote
<!-- ^ markup.quote.markdown -->
<!-- ^ markup.heading.markdown -->

# Strikethrough

~~This text should be parsed as _strikethroughed_.~~
<!-- <- punctuation.definition.strikethrough.markdown -->
<!--                                               ^ punctuation.definition.strikethrough.markdown -->
<!-- ^ markup.strikethrough.markdown -->

~~There may be __bold__ or _italic_ text inside strikethroughed text.~~
<!--              ^ markup.bold.markdown -->
<!--              ^ markup.strikethrough.markdown -->
<!--                            ^ markup.italic.markdown -->
<!--                            ^ markup.strikethrough.markdown -->

~~There may be a keyboard shortcut like <kbd>Enter</kbd> inside strikethroughed text.~~
<!--                                            ^ markup.strikethrough.markdown -->
<!--                                            ^ markup.kbd.markdown -->
<!--                                            ^ markup.kbd.content.markdown -->

__There may be ~~strikethroughed text~~ inside bold text.__
<!--                  ^ markup.bold.markdown -->
<!--                  ^ markup.strikethrough.markdown -->

_There may be ~~strikethroughed text~~ inside italic text._
<!--                  ^ markup.italic.markdown -->
<!--                  ^ markup.strikethrough.markdown -->

~~ If there is a space in the beginning or end, it won't work as per the [GFM][GFM] docs ~~
<!-- ^ meta.paragraph.markdown -->

~~Strikethrough can be applied to
multiple lines. Just keep in mind
not to put any space in the beginning or end.~~
<!-- ^ markup.strikethrough.markdown -->

# Underscore In Words

The word `complicated` must be neither bold nor italic below:

perform_complicated_task
<!--      ^ meta.paragraph.markdown -->
perform__complicated__task
<!--        ^ meta.paragraph.markdown -->

But the first part below is italic and bold respectively:

_perform_complicated_task
<!-- ^ markup.italic.markdown -->
__perform__complicated__task
<!-- ^ markup.bold.markdown -->

# Keyboard Shortcuts

Keyboard shortcuts below should be highlighted:

---

A keyboard shortcut <kbd>Enter</kbd> can be in paragraph.
<!--                  ^ markup.kbd.markdown -->
<!--                  ^ meta.tag.other.html -->
<!--                  ^ entity.name.tag.other.html -->
<!--                      ^ markup.kbd.content.markdown -->
<!--                             ^ markup.kbd.markdown -->
<!--                             ^ meta.tag.other.html -->
<!--                             ^ entity.name.tag.other.html -->

* A keyboard shortcut <kbd>Enter</kbd> can be in list.
<!--                    ^ markup.kbd.markdown -->
<!--                    ^ meta.tag.other.html -->
<!--                    ^ entity.name.tag.other.html -->
<!--                        ^ markup.kbd.content.markdown -->
<!--                               ^ markup.kbd.markdown -->
<!--                               ^ meta.tag.other.html -->
<!--                               ^ entity.name.tag.other.html -->
<!--                        ^ meta.paragraph.list.markdown -->

_A keyboard shortcut <kbd>Enter</kbd> can be in italic._
<!--                    ^ markup.kbd.markdown -->
<!--                    ^ meta.tag.other.html -->
<!--                    ^ entity.name.tag.other.html -->
<!--                        ^ markup.kbd.content.markdown -->
<!--                               ^ markup.kbd.markdown -->
<!--                               ^ meta.tag.other.html -->
<!--                               ^ entity.name.tag.other.html -->
<!--                        ^ markup.italic.markdown -->

__A keyboard shortcut <kbd>Enter</kbd> can be in bold.__
<!--                    ^ markup.kbd.markdown -->
<!--                    ^ meta.tag.other.html -->
<!--                    ^ entity.name.tag.other.html -->
<!--                        ^ markup.kbd.content.markdown -->
<!--                               ^ markup.kbd.markdown -->
<!--                               ^ meta.tag.other.html -->
<!--                               ^ entity.name.tag.other.html -->
<!--                        ^ markup.bold.markdown -->

~~A keyboard shortcut <kbd>Enter</kbd> can be in deleted text.~~
<!--                    ^ markup.kbd.markdown -->
<!--                    ^ meta.tag.other.html -->
<!--                    ^ entity.name.tag.other.html -->
<!--                        ^ markup.kbd.content.markdown -->
<!--                               ^ markup.kbd.markdown -->
<!--                               ^ meta.tag.other.html -->
<!--                               ^ entity.name.tag.other.html -->
<!--                        ^ markup.strikethrough.markdown -->

<p>A keyboard shortcut <kbd>Enter</kbd> can be in HTML.</p>
<!--                     ^ markup.kbd.markdown -->
<!--                     ^ meta.tag.other.html -->
<!--                     ^ entity.name.tag.other.html -->
<!--                         ^ markup.kbd.content.markdown -->
<!--                                ^ markup.kbd.markdown -->
<!--                                ^ meta.tag.other.html -->
<!--                                ^ entity.name.tag.other.html -->
<!--                         ^ meta.disable-markdown -->

<div>
    A keyboard shortcut <kbd>Enter</kbd> can be in block level tags.
<!--                      ^ markup.kbd.markdown -->
<!--                      ^ meta.tag.other.html -->
<!--                      ^ entity.name.tag.other.html -->
<!--                          ^ markup.kbd.content.markdown -->
<!--                                 ^ markup.kbd.markdown -->
<!--                                 ^ meta.tag.other.html -->
<!--                                 ^ entity.name.tag.other.html -->
<!--                          ^ meta.disable-markdown -->
</div>

# Fenced Code Blocks

## In / Near List Items

Below fenced code blocks _should_ be highlighted.

---

* List item

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```
<!-- ^ markup.raw.block.fenced.markdown -->

* List item

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```
<!-- <- markup.raw.block.fenced.markdown -->
---

Below are _not_ valid fenced code blocks according to the [GFM docs][GFM]. It says there must be a blank line before the code block. However, GitHub highlights them. So, they _should_ be highlighted.
<!-- Unsupported, see issue #286 -->

---

    - List item
        ```js
        for (var i = 0; i < 10; i++) {
            console.log(i);
        }
        ```
<!--      ^ meta.block-level.markdown -->

    - List item
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```
<!-- ^ meta.block-level.markdown -->

## In / Near Paragraphs

Below is _not_ a _fenced_ code block, just a normal code block.

---

Paragraph

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```
<!-- ^ meta.block-level.markdown -->
---

Below 2 blocks are fenced code blocks. They _should_ be highlighted.

---

Paragraph

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```
<!-- <- markup.raw.block.fenced.markdown -->

Paragraph
```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```
<!-- <- markup.raw.block.fenced.markdown -->

---

Below is not any type of code block. It _should not_ be highlighted.

---

Paragraph
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```
<!-- ^ meta.paragraph.markdown -->

[GFM]: https://help.github.com/articles/github-flavored-markdown
