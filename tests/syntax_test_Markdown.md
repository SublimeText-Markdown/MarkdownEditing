<!-- SYNTAX TEST "Packages/MarkdownEditing/Markdown (Standard).tmLanguage" -->

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
