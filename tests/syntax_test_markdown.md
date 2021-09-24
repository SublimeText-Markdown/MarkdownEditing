| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"

# Heading
| <- markup.heading.1 punctuation.definition.heading
|^^^^^^^^^ markup.heading.1.markdown
|^ - entity.name.section
|  ^^^^^^ entity.name.section
|        ^ meta.whitespace.newline.markdown - entity.name.section

## Second Heading #
| <- markup.heading.2 punctuation.definition.heading
|^^^^^^^^^^^^^^^^^^^ markup.heading.2.markdown
|^^ - entity.name.section
|  ^^^^^^^^^^^^^^ entity.name.section
|                ^^ - entity.name.section
|                 ^ punctuation.definition.heading.end.markdown

https://spec.commonmark.org/0.30/#example-71

  ## Heading ##
|^^^^^^^^^^^^^^^ markup.heading.2.markdown
|^ - punctuation
| ^^ punctuation.definition.heading.begin.markdown
|   ^^^^^^^^^ - punctuation
|            ^^ punctuation.definition.heading.end.markdown
|              ^ - punctuation
|^^^^ - entity.name.section
|    ^^^^^^^ entity.name.section.markdown
|           ^^^^ - entity.name.section

https://spec.commonmark.org/0.30/#example-73
## Example 73 (trailing spaces!) #####    
|                                    ^ punctuation.definition.heading.end.markdown
|                                         ^ meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-74
## Example 74 ####    >
|^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.2.markdown
|^^ - entity.name.section
|  ^^^^^^^^^^^^^^^^^^^^ entity.name.section.markdown
|                      ^ - entity.name.section

https://spec.commonmark.org/0.30/#example-75
# #heading# #
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^ markup.heading.1.markdown
|^ - entity.name.section
| ^^^^^^^^^ entity.name.section.markdown
|          ^^ - entity.name.section
|           ^ punctuation.definition.heading.end.markdown

https://spec.commonmark.org/0.30/#example-76
## heading \##
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^^ markup.heading.2.markdown
|^^ - entity
|  ^^^^^^^^^^^ entity.name.section.markdown
|          ^^ constant.character.escape.markdown
|          ^^^ - punctuation
|             ^ - entity.name.section

https://spec.commonmark.org/0.30/#example-79
#
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown

# #
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^ markup.heading.1.markdown - entity.name.section
| ^ punctuation.definition.heading.end.markdown

## 
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown - entity.name.section
|^ markup.heading.2.markdown punctuation.definition.heading.begin.markdown - entity.name.section

## ##
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown - entity.name.section
|^^^^^ markup.heading.2.markdown - entity.name.section
|^ punctuation.definition.heading.begin.markdown
|  ^^ punctuation.definition.heading.end.markdown

### ###
| <- markup.heading.3.markdown  - entity.name.sectionpunctuation.definition.heading.begin.markdown
|^^^^^^^ markup.heading.3.markdown - entity.name.section
|^^ punctuation.definition.heading.begin.markdown
|   ^^^ punctuation.definition.heading.end.markdown

# #### #
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^ markup.heading.1.markdown
|^ - entity.name.section
| ^^^^ entity.name.section.markdown
|     ^^ - entity.name.section
|      ^ punctuation.definition.heading.end.markdown

## #### ##
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^ markup.heading.2.markdown
|^ - entity.name.section
|  ^^^^ entity.name.section.markdown
|      ^^^ - entity.name.section
|       ^^ punctuation.definition.heading.end.markdown

#NotAHeading
| <- - markup.heading
|^^^^^^^^^^^^ - markup.heading

Headings terminate paragraphs
# Heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.bold
|^^^^^^^^ markup.heading.1.markdown

Headings terminate **bold text
# Heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.bold
|^^^^^^^^ markup.heading.1.markdown
this must not be bold**
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Headings terminate *italic text
# Heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.italic
|^^^^^^^^ markup.heading.1.markdown
this must not be italic*
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.italic

Headings terminate ***bold italic text
# Heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.bold - markup.italic
|^^^^^^^^ markup.heading.1.markdown
this must not be bold italic***
| <- - meta.bold - markup.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - markup.italic

Alternate Heading
=================
|^^^^^^^^^^^^^^^^ markup.heading.1 punctuation.definition
|                ^ meta.whitespace.newline

heading underlined with dashes
------------------------------
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.2 punctuation.definition.heading

underlined heading followed by a separator
-------------------
------
| <- meta.separator - markup.heading

underlined heading followed by another one that should be treated as a normal paragraph
==================
=====
| <- - markup.heading

```
Fenced codeblocks are no no setext heading
```
---
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown


Paragraph of text that should be scoped as meta.paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph
A [link](https://example.com){ :_attr = value }, *italic text* and **bold**.
| ^^^^^^ meta.link.inline.description.markdown
| ^ punctuation.definition.link.begin
|      ^ punctuation.definition.link.end
|       ^ punctuation.definition.metadata
|        ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                           ^ punctuation.definition.metadata
|                            ^ punctuation.definition.attributes.begin.markdown
|                              ^^^^^^^^^^^^^^ meta.attribute-with-value.markdown
|                              ^^^^^^ entity.other.attribute-name.markdown
|                                     ^ punctuation.separator.key-value.markdown
|                                       ^^^^^ string.unquoted.markdown
|                                             ^ punctuation.definition.attributes.end.markdown
|                                                ^^^^^^^^^^^^^ markup.italic
|                                                ^ punctuation.definition.italic
|                                                            ^ punctuation.definition.italic
|                                                                  ^^ punctuation.definition.bold
|                                                                  ^^^^^^^^ markup.bold
|                                                                        ^^ punctuation.definition.bold

Inline `code sample`.
|      ^^^^^^^^^^^^^ markup.raw.inline
|      ^ punctuation.definition.raw
|                  ^ punctuation.definition.raw

Here is a [](https://example.com).
|         ^^ meta.link.inline
|         ^ punctuation.definition.link.begin
|          ^ punctuation.definition.link.end
|           ^ punctuation.definition.metadata
|            ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                               ^ punctuation.definition.metadata

Here is a [](https://example.com){_attr="value"}.
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
|         ^ punctuation.definition.link.begin
|          ^ punctuation.definition.link.end
|           ^ punctuation.definition.metadata
|            ^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                               ^ punctuation.definition.metadata
|                                ^ punctuation.definition.attributes.begin.markdown
|                                 ^^^^^^^^^^^^^ meta.attribute-with-value.markdown
|                                 ^^^^^ entity.other.attribute-name.markdown
|                                      ^ punctuation.separator.key-value.markdown
|                                       ^^^^^^^ string.quoted.double.markdown
|                                              ^ punctuation.definition.attributes.end.markdown

Here is a [link](#with_(parens/inside)_urls).
|         ^^^^^^ meta.link.inline.description.markdown
|               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown
|                                           ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown
|                ^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown
|                                          ^ punctuation.definition.metadata.end.markdown

Here is a [link](\(foo\)).
|         ^^^^^^ meta.link.inline.description.markdown
|               ^^^^^^^^^ meta.link.inline.metadata.markdown
|                        ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown
|                ^^^^^^^ markup.underline.link.markdown
|                ^^ constant.character.escape.markdown
|                     ^^ constant.character.escape.markdown
|                       ^ punctuation.definition.metadata.end.markdown

Here is a [link](foo\)\:).
|         ^^^^^^ meta.link.inline.description.markdown
|               ^^^^^^^^^ meta.link.inline.metadata.markdown
|                        ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown
|                ^^^^^^^ markup.underline.link.markdown
|                   ^^ constant.character.escape.markdown
|                       ^ punctuation.definition.metadata.end.markdown

Here is a [link](<foo(and(bar)>).
|         ^^^^^^ meta.link.inline.description.markdown
|               ^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown
|                               ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown
|                ^ punctuation.definition.link.begin.markdown
|                 ^^^^^^^^^^^^ markup.underline.link.markdown
|                             ^ punctuation.definition.link.end.markdown
|                              ^ punctuation.definition.metadata.end.markdown

Here is a [link](http://example.com?foo=3#frag).
|         ^^^^^^ meta.link.inline.description.markdown
|               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown
|                                              ^^ - meta.link
|               ^ punctuation.definition.metadata.begin.markdown
|                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown
|                    ^^^ punctuation.separator.path.markdown
|                                  ^ punctuation.separator.path.markdown
|                                        ^ punctuation.separator.path.markdown
|                                             ^ punctuation.definition.metadata.end.markdown

Not a [link] (url) due to space.
|     ^^^^^^ meta.link.reference.description.markdown
|           ^^^^^^^^^^^^^^^^^^^^^ - meta.link

Here is a [reference link][name].
|         ^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                         ^^^^^^ meta.link.reference.metadata.markdown
|         ^ punctuation.definition.link.begin.markdown
|          ^^^^^^^^^^^^^^ string.other.link.title.markdown
|                        ^ punctuation.definition.link.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^^^^ constant.other.reference.link.markdown
|                              ^ punctuation.definition.metadata.end.markdown

Here is a [reference link][name]{_attr='value' :att2}.
|         ^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                         ^^^^^^ meta.link.reference.metadata.markdown
|                               ^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.attributes.markdown
|                                ^^^^^^^^^^^^^ meta.attribute-with-value.markdown
|                                             ^ - meta.attribute-with-value
|                                              ^^^^^ meta.attribute-with-value.markdown
|         ^ punctuation.definition.link.begin.markdown
|          ^^^^^^^^^^^^^^ string.other.link.title.markdown
|                        ^ punctuation.definition.link.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^^^^ constant.other.reference.link.markdown
|                              ^ punctuation.definition.metadata.end.markdown
|                               ^ punctuation.definition.attributes.begin.markdown
|                                ^^^^^ entity.other.attribute-name.markdown
|                                     ^ punctuation.separator.key-value.markdown
|                                      ^^^^^^^ string.quoted.single.markdown
|                                              ^^^^^ entity.other.attribute-name.markdown
|                                                   ^ punctuation.definition.attributes.end.markdown

Here is a [blank reference link][]{}.
|         ^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.literal.description.markdown
|                               ^^ meta.link.reference.literal.metadata.markdown
|                                 ^^ meta.link.reference.literal.attributes.markdown
|         ^ punctuation.definition.link.begin.markdown
|          ^^^^^^^^^^^^^^^^^^^^ string.other.link.title.markdown
|                              ^ punctuation.definition.link.end.markdown
|                               ^ punctuation.definition.metadata.begin.markdown
|                                ^ punctuation.definition.metadata.end.markdown
|                                 ^ punctuation.definition.attributes.begin.markdown
|                                  ^ punctuation.definition.attributes.end.markdown

Here is a footnote[^1][link][] or long[^longnote][link][].
|                 ^^^^ meta.link.reference.footnote.markdown-extra
|                     ^^^^^^ meta.link.reference.literal.description.markdown
|                           ^^ meta.link.reference.literal.metadata.markdown
|                                     ^^^^^^^^^^^ meta.link.reference.footnote.markdown-extra
|                                                ^^^^^^^^ meta.link.reference.literal

Here is a footnote [^footnote](not_link_dest).
|                  ^^^^^^^^^^^ meta.paragraph.markdown meta.link.reference.footnote.markdown-extra
|                  ^ punctuation.definition.link.begin.markdown
|                   ^^^^^^^^^ meta.link.reference.literal.footnote-id.markdown
|                            ^ punctuation.definition.link.end.markdown
|                             ^^^^^^^^^^^^^^^ meta.paragraph.markdown - meta.link

Here is a ![](https://example.com/cat.gif).
|         ^^^ meta.image.inline.description.markdown
|            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown
|                                         ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown
|           ^ punctuation.definition.image.end.markdown - string
|            ^ punctuation.definition.metadata.begin.markdown
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                        ^ punctuation.definition.metadata.end.markdown

Here is a ![](https://example.com/cat.gif){_at"r=value :att2}.
|         ^^^ meta.image.inline.description.markdown
|            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown
|                                         ^^^^^^^^^^^^^^^^^^^ meta.image.inline.attributes.markdown
|                                                            ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown
|           ^ punctuation.definition.image.end.markdown - string
|            ^ punctuation.definition.metadata.begin.markdown
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                        ^ punctuation.definition.metadata
|                                         ^ punctuation.definition.attributes.begin.markdown
|                                          ^^^^^ entity.other.attribute-name.markdown
|                                             ^ invalid.illegal.attribute-name.markdown
|                                               ^ punctuation.separator.key-value.markdown
|                                                ^^^^^ string.unquoted.markdown
|                                                      ^^^^^ entity.other.attribute-name.markdown
|                                                           ^ punctuation.definition.attributes.end.markdown

Here is a ![Image Alt Text](https://example.com/cat.gif).
|         ^^^^^^^^^^^^^^^^^ meta.image.inline.description.markdown
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown
|                                                       ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown
|                         ^ punctuation.definition.image.end.markdown - string
|                          ^ punctuation.definition.metadata.begin.markdown
|                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                      ^ punctuation.definition.metadata.end.markdown

Here is a ![Image Alt Text](  https://example.com/cat.gif  ).
|         ^^^^^^^^^^^^^^^^^ meta.image.inline.description.markdown
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown
|                                                           ^^ - meta.image
|         ^^ punctuation.definition.image.begin.markdown
|                         ^ punctuation.definition.image.end - string
|                          ^ punctuation.definition.metadata.begin.markdown
|                           ^^ - markup.underline
|                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                        ^^ - markup.underline
|                                                          ^ punctuation.definition.metadata.end.markdown

Here is a ![Image Alt Text](
  https://example.com/cat.gif  ).
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                              ^ punctuation.definition.metadata.end.markdown

Here is a ![Image Alt Text](
  https://example.com/cat.gif
 "hello"   ).
|^^^^^^^ meta.image.inline string.other.link.description.title
|       ^^^^ meta.image.inline
|          ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  <https://example.com/cat.gif> "hello"   ).
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.image.inline.metadata.markdown
|                                          ^^ meta.paragraph.markdown - meta.image
| ^ punctuation.definition.link.begin.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                             ^ punctuation.definition.link.end.markdown
|                               ^^^^^^^ string.other.link.description.title.markdown
|                               ^ punctuation.definition.string.begin.markdown
|                                     ^ punctuation.definition.string.end.markdown
|                                         ^ punctuation.definition.metadata.end.markdown

Here is a ![Image Alt Text](
  <https://example .com /cat.gif> (hello)   ).
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.image.inline.metadata.markdown
|                                            ^^ meta.paragraph.markdown - meta.image
| ^ punctuation.definition.link.begin.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                               ^ punctuation.definition.link.end.markdown
|                                 ^^^^^^^ string.other.link.description.title.markdown
|                                 ^ punctuation.definition.string.begin.markdown
|                                       ^ punctuation.definition.string.end.markdown
|                                           ^ punctuation.definition.metadata.end.markdown

Here is a ![Image Alt Text](
  https://example .com /cat.gif (hello)   ).
|^ meta.paragraph.markdown meta.image.inline.metadata.markdown - markup.underline
| ^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.image.inline.metadata.markdown markup.underline.link.image.markdown
|                ^ meta.paragraph.markdown meta.image.inline.metadata.markdown - markup.underline
|                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - meta.image - markup.underline

Here is a ![Image Ref Alt][1].
|         ^^^^^^^^^^^^^^^^ meta.image.reference.description.markdown
|                         ^^^ meta.image.reference.metadata.markdown
|         ^^ punctuation.definition.image.begin.markdown
|           ^^^^^^^^^^^^^ string.other.link.title.markdown
|                        ^ punctuation.definition.image.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^ constant.other.reference.link.markdown
|                           ^ punctuation.definition.metadata.end.markdown

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca/documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline markup.underline.link
|                                                 ^ - invalid
|                                                  ^ meta.link.inline punctuation.definition.metadata.end

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca /documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inline markup.underline.link
|                       ^ meta.paragraph meta.link.inline - markup.underline.link
|                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - meta.link.inline

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca/documentations/about/cool
  (title)) for more information about...
| ^^^^^^^^ meta.paragraph meta.link.inline
|        ^ punctuation.definition.metadata.end
| ^^^^^^^ string.other.link.description.title.markdown

  1. Ordered list item
| ^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered
| ^^ markup.list.numbered.bullet - markup.list.numbered markup.list.numbered
|  ^ punctuation.definition.list_item
  2. Ordered list item #2
| ^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered - markup.list.numbered markup.list.numbered
| ^^ markup.list.numbered.bullet
|  ^ punctuation.definition.list_item
     1. Subitem
     2. Another subitem
|^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered
|    ^^ markup.list.numbered.bullet
|     ^ punctuation.definition.list_item
|       ^^^^^^^^^^^^^^^^ meta.paragraph.list - meta.paragraph.list meta.paragraph.list

Paragraph break.

  - Unordered list item
| ^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered - markup.list.unnumbered markup.list.unnumbered
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
  - Unordered list item #2
| ^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered - markup.list.unnumbered markup.list.unnumbered
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item

Paragraph break.

- `<Logo>` | `<logo>` (components/Logo.vue)
- `<MyComponent>` | `<my-component>` | (components/my-component.vue)
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown

Paragraph break.

  * Unordered list item
| ^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered - markup.list.unnumbered markup.list.unnumbered
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
  + Unordered list item #2
| ^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered - markup.list.unnumbered markup.list.unnumbered
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
    + Subitem 1
|   ^ punctuation.definition.list_item
  + Item
    + Subitem
    + Another subitem
|   ^ markup.list.unnumbered.bullet punctuation.definition.list_item - meta.paragraph.list
|     ^^^^^^^^^^^^^^^ meta.paragraph.list
      + Nested Subitem
|     ^ markup.list.unnumbered.bullet punctuation.definition.list_item - markup.list.unnumbered markup.list.unnumbered
        + Nested + Subitem
|       ^ markup.list.unnumbered.bullet punctuation.definition.list_item
|                ^ - punctuation.definition.list_item

  * Unsorted list item
	```xml
|^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown meta.code-fence.definition.begin.xml.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|    ^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown meta.code-fence.definition.begin.xml.markdown-gfm constant.other.language-name.markdown
	<tag>
|^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown markup.raw.code-fence.xml.markdown-gfm text.xml meta.tag.xml
	```
|^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown meta.code-fence.definition.end.xml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

Paragraph break.

> This is a block quote. It contains markup.
> Including things like *italics*
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote
|                       ^^^^^^^^^ markup.italic

Paragraph break.

---
|^^^ meta.separator.thematic-break
|^^ punctuation.definition.thematic-break

Paragraph break.

--------
|^^^^^^^^ meta.separator.thematic-break
|^^^^^^^ punctuation.definition.thematic-break

[1]: https://google.com
| <- meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^ entity.name.reference.link
|  ^ punctuation.separator.key-value
|    ^^^^^^^^^^^^^^^^^^ markup.underline.link

<div>this is HTML until <span>there are two</span> blank lines</div>
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<div>this is HTML until there are two blank lines
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
still <span>HTML</span>
|      ^^^^ meta.tag.inline.any.html entity.name.tag.inline.any.html
</div>
| ^^^^ meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<pre>nested tags don't count <pre>test</pre>
|                                     ^^^^^^ meta.disable-markdown meta.tag.block.any.html
non-disabled markdown
| <- - meta.disable-markdown

<div>nested tags don't count <div>test
|                                 ^^^^^ meta.disable-markdown
</div>
| ^^^ meta.disable-markdown entity.name.tag.block.any.html

non-disabled markdown
| <- - meta.disable-markdown

<div>two blank lines needed</div> to stop disabled markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

<div>another</div> <span>disable</span> test
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
|                  ^^^^^^ meta.tag.inline.any.html
disabled markdown
| <- meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown

*a*
| ^ markup.italic
<p>*a*</p>
| ^^^^^^^^^ meta.disable-markdown - markup.italic
*a*
| ^^ meta.disable-markdown

non-disabled markdown
| <- - meta.disable-markdown


# Block Quote Tests ###########################################################

>=
| <- punctuation.definition.blockquote.markdown 

>==
| <- punctuation.definition.blockquote.markdown

  >=
| ^ punctuation.definition.blockquote.markdown
    >=
|   ^^ - punctuation.definition.blockquote.markdown

    >=
|   ^^ - punctuation.definition.blockquote.markdown

> Block quote
| <- markup.quote punctuation.definition.blockquote
| ^^^^^^^^^^^ markup.quote

> Block quote followed by an empty block quote line
>
| <- markup.quote punctuation.definition.blockquote

> Block quote followed by an empty block quote line
>
> Followed by more quoted text
| <- markup.quote punctuation.definition.blockquote

> > Nested block quote
| <- markup.quote punctuation.definition.blockquote
| ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.quote.markdown
|^ - punctuation
| ^ punctuation.definition.blockquote
|  ^ - punctuation

> > Nested quote
> Followed by more quoted text that is not nested
| <- markup.quote punctuation.definition.blockquote - markup.quote markup.quote

> Here is a block quote
This quote continues on. Line breaking is OK in markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote
> Here it is again
| <- punctuation.definition.blockquote

paragraph
| <- meta.paragraph

>    > this is a nested quote but no code in a block quote
| <- punctuation.definition.blockquote
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.quote.markdown

>     > this is code in a block quote, not a nested quote
| <- punctuation.definition.blockquote
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block - markup.quote markup.quote

> CommonMark expects following line to be indented code block (see: example 326)
    > but all common parsers handle it as continued text.
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown - markup.raw
|   ^ - punctuation

> Quoted fenced code block begin
> ```
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.code-fence
| ^^^^ markup.quote.markdown meta.code-fence.definition.begin.text.markdown-gfm
| ^^^ punctuation.definition.raw.code-fence.begin.markdown

> Quoted fenced code block language identifier
> ```C++
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.code-fence
| ^^^^^^^ markup.quote.markdown meta.code-fence.definition.begin.text.markdown-gfm
|    ^^^ constant.other.language-name.markdown

> Quoted fenced code block language identifier
> ```C++ info string
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.code-fence
| ^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.code-fence.definition.begin.text.markdown-gfm
|    ^^^ constant.other.language-name.markdown
|       ^^^^^^^^^^^^^ - constant

> Quoted fenced code block content
> ```
> code block
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.code-fence
| ^^^^^^^^^^^ markup.quote.markdown markup.raw.code-fence.markdown-gfm

> Quoted fenced code block end
> ```
> ```
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.code-fence
| ^^^^ markup.quote.markdown meta.code-fence.definition.end.text.markdown-gfm
| ^^^ punctuation.definition.raw.code-fence.end.markdown

> > 2nd level quoted fenced code block
> > ```
> > code block ```
> > ```
| <- markup.quote.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^ markup.quote.markdown markup.quote.markdown - meta.code-fence
|   ^^^^ markup.quote.markdown markup.quote.markdown meta.code-fence.definition.end.text.markdown-gfm

> Block quote followed by fenced code block
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown - meta.quote
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown - meta.quote

> Quoted fenced code block is terminated by missing > at bol
> ```
no code block
| <- meta.paragraph.markdown - meta.quote - meta.code-fence
|^^^^^^^^^^^^^ meta.paragraph.markdown - meta.quote - meta.code-fence

> Quoted fenced code block is terminated by missing > at bol
> ```
> content
no code block
| <- meta.paragraph.markdown - meta.quote - meta.code-fence
|^^^^^^^^^^^^^ meta.paragraph.markdown - meta.quote - meta.code-fence

> Unterminated quoted fenced code block followed by unquoted fenced code block
> ```
```
| <- meta.code-fence.definition.begin.text.markdown-gfm - markup.quote
```
| <- meta.code-fence.definition.end.text.markdown-gfm - markup.quote

> Block quote followed by heading
# heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^ markup.heading.1.markdown - meta.quote
| ^^^^^^^ entity.name.section.markdown

> Block quote followed by list
* list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by list
+ list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by list
- list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by list
1. list item
| <- markup.list.numbered.bullet.markdown - punctuation
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

> Block quote followed by thematic break
***
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - meta.quote

> Block quote followed by thematic break
- - -
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - meta.quote

Code block below:

    this is code!
| ^^^^^^^^^^^^^^^^ markup.raw.block

    more code
    spanning multiple lines
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block

paragraph
| <- meta.paragraph

- - - -
| ^^^^^^ meta.separator
| ^ punctuation.definition.thematic-break
|   ^ punctuation.definition.thematic-break
|     ^ punctuation.definition.thematic-break
|  ^ - punctuation
* * * * *
| ^^^^^^^^ meta.separator

_ _ _ _ _ _ _
| ^^^^^^^^^^^^ meta.separator
| ^ punctuation.definition.thematic-break
|   ^ punctuation.definition.thematic-break
|  ^ - punctuation

-  -  -  - 
| <- meta.separator.thematic-break punctuation.definition.thematic-break
|^^ - punctuation
|  ^ punctuation
|        ^ punctuation

###[ COMMONMARK AUTOLINKS ]###################################################

<mailto:test+test@test.com>
| <- meta.link.email.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown
|                         ^ meta.link.email.markdown - markup.underline
|      ^ punctuation.separator.path.markdown
|                ^ punctuation.separator.path.markdown
|                         ^ punctuation.definition.link.end.markdown

<foo#bar?@mail.test.com>
| <- meta.link.email.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown
|                      ^ meta.link.email.markdown - markup.underline
|        ^ punctuation.separator.path.markdown
|                      ^ punctuation.definition.link.end.markdown

<http://www.test.com/>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                    ^ meta.link.inet.markdown - markup.underline
|    ^^^ punctuation.separator.path.markdown
|                   ^ punctuation.separator.path.markdown
|                    ^ punctuation.definition.link.end.markdown

<https://test.com/>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                 ^ meta.link.inet.markdown - markup.underline
|     ^^^ punctuation.separator.path.markdown
|                ^ punctuation.separator.path.markdown
|                 ^ punctuation.definition.link.end.markdown

<ftp://test.com/>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|               ^ meta.link.inet.markdown - markup.underline
|   ^^^ punctuation.separator.path.markdown
|              ^ punctuation.separator.path.markdown
|               ^ punctuation.definition.link.end.markdown

<irc://foo%20bar.com:2233/baz>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown - markup.underline
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                            ^ meta.link.inet.markdown - markup.underline
|   ^^^ punctuation.separator.path.markdown
|         ^ constant.character.escape.url.markdown punctuation.definition.escape.markdown
|          ^^ constant.character.escape.url.markdown - punctuation
|                        ^ punctuation.separator.path.markdown

<a+b+c:d>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|       ^ meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.end.markdown

<made-up-scheme://foo,bar>
| <- meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inet.markdown markup.underline.link.markdown
|                        ^ meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.end.markdown
|              ^^^ punctuation.separator.path.markdown

<http://../>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|          ^ meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.end.markdown
|    ^^^ punctuation.separator.path.markdown
|         ^ punctuation.separator.path.markdown

<localhost:5001/foo>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                  ^ meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.end.markdown
|         ^ punctuation.separator.path.markdown
|              ^ punctuation.separator.path.markdown

<http://foo.bar/baz bim>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                  ^^^^^^ - meta.link
|    ^^^ punctuation.separator.path.markdown
|              ^ punctuation.separator.path.markdown

<http://example.com/\[\>
| <- meta.link.inet.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link.markdown
|                      ^ meta.paragraph.markdown meta.link.inet.markdown punctuation.definition.link.end.markdown
|    ^^^ punctuation.separator.path.markdown
|                  ^ punctuation.separator.path.markdown

###[ GFM AUTOLINKS ]##########################################################

Visit ftp://intra%20net
|     ^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|        ^^^ punctuation.separator.path.markdown
|               ^ - constant
|                ^ constant.character.escape.url.markdown punctuation.definition.escape.markdown
|                 ^^ constant.character.escape.url.markdown - punctuation
|                   ^^^ - constant

Visit http://intra%20net
|     ^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|         ^^^ punctuation.separator.path.markdown
|                ^ - constant
|                 ^ constant.character.escape.url.markdown punctuation.definition.escape.markdown
|                  ^^ constant.character.escape.url.markdown - punctuation
|                    ^^^ - constant

Visit https://intra%20net
|     ^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|          ^^^ punctuation.separator.path.markdown
|                 ^ - constant
|                  ^ constant.character.escape.url.markdown punctuation.definition.escape.markdown
|                   ^^ constant.character.escape.url.markdown - punctuation
|                     ^^^ - constant

Visit www.intra%20net
|     ^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ - constant
|              ^ constant.character.escape.url.markdown punctuation.definition.escape.markdown
|               ^^ constant.character.escape.url.markdown - punctuation
|                 ^^^ - constant

Visit www.commonmark.org/help for more information.
|     ^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|                       ^ punctuation.separator.path.markdown
|                            ^^^^^^^^^^^^^^^^^^^^^^^ - markup.underline.link

Visit www.commonmark.org.
|     ^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet.markdown markup.underline.link
|                       ^^ - markup.underline.link

Visit www.commonmark.org/a.b.
|     ^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet.markdown markup.underline.link
|                           ^ - markup.underline.link
|                       ^ punctuation.separator.path.markdown

www.google.com/search?q=(business))+ok
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                     ^ - markup.underline.link

www.google.com/search?q=Markup+(business)
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown

www.commonmark.org/he<lp>
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|                 ^ punctuation.separator.path.markdown
|                    ^ - markup.underline.link

http://commonmark.org
|^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|   ^^^ punctuation.separator.path.markdown

www.google.com/search?q=commonmark&hl=en
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                 ^ punctuation.separator.path.markdown
|                                       ^ - markup.underline.link

www.google.com/search?q=commonmark&hl;
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                 ^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;&hl;
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                 ^^^^^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;!
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|                                 ^^^^^^ - meta.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                 ^^^^ constant.character.entity.named.html - markup.underline.link

www.google.com/search?q=commonmark&hl;f
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|                                      ^ - meta.link
|             ^ punctuation.separator.path.markdown
|                    ^ punctuation.separator.path.markdown
|                                 ^^^^ - constant.character

(Visit https://encrypted.google.com/search?q=Markup+(business))
|      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|           ^^^ punctuation.separator.path.markdown
|                                  ^ punctuation.separator.path.markdown
|                                         ^ punctuation.separator.path.markdown
|                                                             ^^ - markup.underline.link

Anonymous FTP is available at ftp://foo.bar.baz.
|                             ^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|                                ^^^ punctuation.separator.path.markdown
|                                              ^^ - markup.underline.link

(see http://www.google.com/search?q=commonmark&hl=en)
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inet.markdown markup.underline.link
|        ^^^ punctuation.separator.path.markdown
|                         ^ punctuation.separator.path.markdown
|                                ^ punctuation.separator.path.markdown
|                                             ^ punctuation.separator.path.markdown
|                                                   ^^ - markup.underline.link

foo@bar.baz
| <- meta.link.email.markdown markup.underline.link.markdown
|^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown
|  ^ punctuation.separator.path.markdown
|          ^ - meta.link - markup.underline.link

hello@mail+xyz.example isn't valid, but hello+xyz@mail.example is.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.link - markup.underline.link
|                                       ^^^^^^^^^^^^^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown

 test@test.test.me
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown
|    ^ punctuation.separator.path.markdown
|                 ^ - meta.link - markup.underline.link

 a.b-c_d@a.b
| <- - meta.link - markup.underline
|^^^^^^^^^^^ meta.link.email.markdown markup.underline.link.markdown
|       ^ punctuation.separator.path.markdown
|           ^ - meta.link - markup.underline.link

a.b-c_d@a.b.
|^^^^^^^^^^ markup.underline.link
|          ^^ - markup.underline.link

 a.b-c_d@a.b-
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^ - meta.link - markup.underline.link

 a.b-c_d@a.b_
| <- - meta.link - markup.underline
|^^^^^^^^^^^^^ - meta.link - markup.underline.link

###[ LIGATURES ]##############################################################

this is a raw ampersand & does not require HTML escaping
|                       ^ meta.other.valid-ampersand

this is a raw bracket < > does not require HTML escaping
|                     ^^^ - meta.tag 
|                     ^ meta.other.valid-bracket
|                       ^ - meta.other.valid-bracket

these are raw ligatures << <<< <<<< <<<<< >>>>> >>>> >>> >>
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures <- <-- <--- <---- <-< <--< <---< <----<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures -> --> ---> ----> >-> >--> >---> >---->
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >- >-- >--- >---- ----< ---< --< -<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >< >-< >--< >---< <---> <--> <-> <>
|                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures <= <== <=== <==== <=< <==< <===< <====<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures => ==> ===> ====> >=> >==> >===> >====>
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >= >== >=== >==== ====< ===< ==< =<
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures >< >=< >==< >===< <===> <==> <=> <>
|                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

these are raw ligatures - -- --- ---- ----- ===== ==== === == =
|                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.other.valid-bracket - meta.tag

[2]: https://github.com/sublimehq/Packages "Packages Repo"
| <- meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^ entity.name.reference.link
|  ^ punctuation.separator.key-value
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                          ^^^^^^^^^^^^^^^ string.other.link.description.title
|                                          ^ punctuation.definition.string.begin
|                                                        ^ punctuation.definition.string.end

[3]: https://github.com/sublimehq/Packages/issues/ 'Issues on Packages Repo'
| <- meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^ entity.name.reference.link
|  ^ punctuation.separator.key-value
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                  ^^^^^^^^^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                  ^ punctuation.definition.string.begin
|                                                                          ^ punctuation.definition.string.end

Paragraph followed immediately by a list, no blank line in between
- list item 1
| <- markup.list.unnumbered punctuation.definition.list_item

Paragraph followed immediately by a numbered list, no blank line in between
 1. list item 1
|^^^^^^^^^^^^^^^ markup.list.numbered
|^^ markup.list.numbered.bullet
| ^ punctuation.definition.list_item
|   ^^^^^^^^^^^^ meta.paragraph.list
  more text - this punctuation should be ignored 2.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered meta.paragraph.list
|           ^ - punctuation.definition.list_item
|                                                 ^ - punctuation.definition.list_item

Paragraph not followed immediately by a numbered list,
because it doesn't begin with the number one:
 2. text
| ^ - markup.list.numbered - punctuation.definition.list_item


> Block quote with list items
> - list item 1
| ^ markup.quote punctuation.definition.list_item
> - list item 2
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
| ^^^^^^^^^^^^^^ markup.quote markup.list.unnumbered
|   ^^^^^^^^^^^^ meta.paragraph.list
>   1. sub list item
| <- markup.quote punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^^^ markup.quote
|    ^ punctuation.definition.list_item
|   ^^ markup.list.numbered.bullet
| ^^^^^^^^^^^^^^^^^^^ markup.list.numbered
|      ^^^^^^^^^^^^^^ meta.paragraph.list
> - list item 3
  continued
| ^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown meta.paragraph.list.markdown

* this is a list

   > This is a blockquote.
|  ^ markup.list.unnumbered markup.quote punctuation.definition.blockquote

 This is a paragraph still part of the 
 list item
| ^^^^^^^^^ markup.list.unnumbered meta.paragraph.list - meta.paragraph.list meta.paragraph.list

* Lorem ipsum

        This is a code block
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered markup.raw.block
* list continues
| <- markup.list.unnumbered punctuation.definition.list_item - markup.raw.block
* list continues
* [ ] Unticked GitHub-flavored-markdown checkbox
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered
| ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|  ^ markup.checkbox.mark.markdown-gfm - punctuation
|   ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
* [x] Ticked GFM checkbox
| ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|  ^ markup.checkbox.mark.markdown-gfm - punctuation
|   ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
* [X] Another ticked checkbox
| ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|  ^ markup.checkbox.mark.markdown-gfm - punctuation
|   ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
    + [ ] Sub-item with checkbox
|     ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|      ^ markup.checkbox.mark.markdown-gfm - punctuation
|       ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
* [] Not a checkbox
| ^^^^^^^^^^^^^^^^^ - storage - constant
* [/] Not a checkbox
| ^^^^^^^^^^^^^^^^^^ - storage
* Not [ ] a [x] checkbox [X]
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ - storage - constant
* [ ] [Checkbox][] with next word linked
| ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|  ^ markup.checkbox.mark.markdown-gfm - punctuation
|   ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
|     ^^^^^^^^^^^^ meta.link
* list has `unclosed code
* list continues
| ^^^^^^^^^^^^^^^ - markup.raw

> * [ ] task
| ^^^^^^^^^^^ markup.quote.markdown
| ^ markup.list.unnumbered.bullet.markdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown
| ^ punctuation.definition.list_item.markdown
|   ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|    ^ markup.checkbox.mark.markdown-gfm - punctuation
|     ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
> * [x] task
| ^^^^^^^^^^^ markup.quote.markdown
| ^ markup.list.unnumbered.bullet.markdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown
| ^ punctuation.definition.list_item.markdown
|   ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|    ^ markup.checkbox.mark.markdown-gfm - punctuation
|     ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
> * [X] task
| ^^^^^^^^^^^ markup.quote.markdown
| ^ markup.list.unnumbered.bullet.markdown
|  ^^^^^^^^^^ markup.list.unnumbered.markdown
| ^ punctuation.definition.list_item.markdown
|   ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|    ^ markup.checkbox.mark.markdown-gfm - punctuation
|     ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
> * [X] task
>   - [ ] task
| ^^^^^^^^^^^^^ markup.quote.markdown
|   ^ markup.list.unnumbered.bullet.markdown
|    ^^^^^^^^^^ markup.list.unnumbered.markdown
|   ^ punctuation.definition.list_item.markdown
|     ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|      ^ markup.checkbox.mark.markdown-gfm - punctuation
|       ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm


- `code` - <a name="demo"></a>
| ^ markup.list.unnumbered meta.paragraph.list markup.raw.inline punctuation.definition.raw
|          ^^^^^^^^^^^^^^^^^^^ meta.tag.inline.a.html
 3. [see `demo`](#demo "demo")
| ^ punctuation.definition.list_item
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
|    ^^^^^^^^^^ meta.link.inline.description
|               ^ punctuation.definition.metadata.begin
|                      ^ punctuation.definition.string.begin
|                           ^ punctuation.definition.string.end
|                            ^ punctuation.definition.metadata.end
    [see `demo`](#demo (demo))
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
|    ^^^^^^^^^^ meta.link.inline.description
|               ^ punctuation.definition.metadata.begin
|                      ^ punctuation.definition.string.begin
|                           ^ punctuation.definition.string.end
|                            ^ punctuation.definition.metadata.end
    [see `demo`](#demo 'demo')
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
|    ^^^^^^^^^^ meta.link.inline.description
|               ^ punctuation.definition.metadata.begin
|                      ^ punctuation.definition.string.begin
|                           ^ punctuation.definition.string.end
|                            ^ punctuation.definition.metadata.end
    Here is a ![example image](https://test.com/sublime.png "A demonstration").
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list meta.image.inline
|             ^^ punctuation.definition.image.begin
|               ^^^^^^^^^^^^^ meta.image.inline.description
|                            ^ punctuation.definition.image.end
|                             ^ punctuation.definition.metadata
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                           ^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                           ^ punctuation.definition.string.begin
|                                                                           ^ punctuation.definition.string.end
|                                                                            ^ punctuation.definition.metadata
    Here is a ![example image](https://test.com/sublime.png 'A demonstration').
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list meta.image.inline
|             ^^ punctuation.definition.image.begin
|               ^^^^^^^^^^^^^ meta.image.inline.description
|                            ^ punctuation.definition.image.end
|                             ^ punctuation.definition.metadata
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                           ^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                           ^ punctuation.definition.string.begin
|                                                                           ^ punctuation.definition.string.end
|                                                                            ^ punctuation.definition.metadata
    Here is a ![example image](https://test.com/sublime.png (A demonstration)).
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list meta.image.inline
|             ^^ punctuation.definition.image.begin
|               ^^^^^^^^^^^^^ meta.image.inline.description
|                            ^ punctuation.definition.image.end
|                             ^ punctuation.definition.metadata
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                           ^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                           ^ punctuation.definition.string.begin
|                                                                           ^ punctuation.definition.string.end
|                                                                            ^ punctuation.definition.metadata

1) numberd item
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^^^^^ markup.list.numbered.markdown

 2) numberd item
| <- markup.list.numbered.markdown
|^^ markup.list.numbered.bullet.markdown
|  ^^^^^^^^^^^^^^ markup.list.numbered.markdown

  3) numberd item
| <- markup.list.numbered.markdown
|^ markup.list.numbered.markdown
| ^^ markup.list.numbered.bullet.markdown
|   ^^^^^^^^^^^^^^ markup.list.numbered.markdown

   4) numberd item
| <- markup.list.numbered.markdown
|^^ markup.list.numbered.markdown
|  ^^ markup.list.numbered.bullet.markdown
|    ^^^^^^^^^^^^^^ markup.list.numbered.markdown

  <!-- HTML comment -->
| ^^^^^^^^^^^^^^^^^^^^^ comment.block.html

*italic text <span>HTML element</span> end of italic text*
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

_italic text <SPAN>HTML element</SPAN> end of italic text_
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

**bold text <span>HTML element</span> end of bold text**
| <- punctuation.definition.bold
|                                                     ^^ punctuation.definition.bold
|           ^^^^^^ meta.tag.inline.any.html
|                             ^^^^^^^ meta.tag.inline.any.html

__bold text <span>HTML element</span> end of bold text__
| <- punctuation.definition.bold
|                                                     ^^ punctuation.definition.bold
|           ^^^^^^ meta.tag.inline.any.html
|                             ^^^^^^^ meta.tag.inline.any.html

*italic text <span>HTML element</span> end of italic text*
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

_italic text <span>HTML element</span> end of italic text_
| <- punctuation.definition.italic
|                                                        ^ punctuation.definition.italic
|            ^^^^^^ meta.tag.inline.any.html
|                              ^^^^^^^ meta.tag.inline.any.html

[link [containing] [square] brackets](#backticks)
|<- punctuation.definition.link.begin
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|                                   ^ punctuation.definition.link.end
[link `containing square] brackets] in backticks`[]](#wow)
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|     ^ punctuation.definition.raw.begin
|                                               ^ punctuation.definition.raw.end
|                                                  ^ punctuation.definition.link.end
[link ``containing square]` brackets[[][] in backticks``](#wow)
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline.description
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.inline
|     ^^ punctuation.definition.raw.begin
|                                                     ^^ punctuation.definition.raw.end
|                                                       ^ punctuation.definition.link.end
`inline markup <span></span>`
|              ^^^^^^^^^^^^^ markup.raw.inline - meta.tag.inline.any.html
escaped backtick \`this is not code\`
|                ^^ constant.character.escape
|                                  ^^ constant.character.escape
|                  ^^^^^^^^^^^^^^^^ - markup.raw.inline

This is a [reference] ()
|         ^^^^^^^^^^^ meta.link.reference
|                    ^^^^ - meta.link

This is a [reference] (followed by parens)
|         ^^^^^^^^^^^ meta.link.reference
|                    ^^^^^^^^^^^^^^^^^^^^^ - meta.link

This is a [reference] []
|         ^^^^^^^^^^^ meta.link.reference
|                    ^ - meta.link
|                     ^^ meta.link.reference

This is a ![reference] ()
|         ^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^^^^ - meta.link

This is a ![reference] (followed by parens)
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^^^^^^^^^^^^^^^^^^^^^ - meta.link

This is a ![reference] []
|         ^^^^^^^^^^^^^^^ - meta.image
|          ^^^^^^^^^^^ meta.link.reference
|                     ^ - meta.link
|                      ^^ meta.link.reference

http://spec.commonmark.org/0.28/#example-322
*foo`*`
|^^^^^^^ markup.italic
|   ^^^ markup.raw.inline

| <- invalid.illegal.non-terminated.bold-italic

http://spec.commonmark.org/0.28/#example-323
[not a `link](/foo`)
|^^^^^^^^^^^^^^^^^^^ - meta.link
|      ^^^^^^^^^^^^ markup.raw.inline

http://spec.commonmark.org/0.28/#example-324
`<a href="`">`
|^^^^^^^^^^ markup.raw.inline
|          ^^ - markup.raw

| <- invalid.illegal.non-terminated.raw

http://spec.commonmark.org/0.28/#example-325
<a href="`">`
| ^^^^^^^^^ meta.tag.inline.a
|           ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

http://spec.commonmark.org/0.28/#example-326
`<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^ markup.raw.inline
|                     ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

http://spec.commonmark.org/0.28/#example-327
<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                    ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

http://spec.commonmark.org/0.27/#example-328
*foo bar*
| <- punctuation.definition.italic.begin
|       ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-329
This is not emphasis, because the opening `*` is followed by whitespace, and hence not part of a left-flanking delimiter run:
a * foo bar*
| ^^^^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-332
Intraword emphasis with `*` is permitted:
foo*bar*
|  ^ punctuation.definition.italic.begin
|      ^ punctuation.definition.italic.end
http://spec.commonmark.org/0.27/#example-333
5*6*78
|^ punctuation.definition.italic.begin
|  ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-334
_foo bar_
| <- punctuation.definition.italic.begin
|       ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-335
This is not emphasis, because the opening `_` is followed by whitespace:
_ foo bar_
| <- - punctuation
| ^^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-336
This is not emphasis, because the opening `_` is preceded by an alphanumeric and followed by punctuation:
a_"foo"_
|^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-337
Emphasis with `_` is not allowed inside words:
foo_bar_
|  ^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-338
5_6_78
|^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-339
пристаням_стремятся_
|        ^^^^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-341
foo-_(bar)_
|   ^ punctuation.definition.italic.begin
|         ^ punctuation.definition.italic.end

*foo bar *
| <- punctuation.definition.italic.begin
|        ^ - punctuation
*
| <- - punctuation
abc*
|  ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-347
*foo*bar
| <- punctuation.definition.italic.begin
|   ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-348
_foo bar _
| <- punctuation.definition.italic.begin
|        ^ - punctuation
_
| <- - punctuation
abc_
|  ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-351
Intraword emphasis is disallowed for `_`:
_foo_bar
| <- punctuation.definition.italic.begin
|   ^ - punctuation
abc_
|  ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-353
_foo_bar_baz_
| <- punctuation.definition.italic.begin
|   ^^^^^ - punctuation
|           ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-354
_(bar)_.
| <-  punctuation.definition.italic.begin
|     ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-355
 **foo bar**
|^^ punctuation.definition.bold.begin
|         ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-356
** foo bar**
| <- - punctuation
|         ^^ - punctuation

http://spec.commonmark.org/0.27/#example-358
foo**bar**
|  ^^ punctuation.definition.bold.begin
|       ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-359
 __foo bar__
|^^ punctuation.definition.bold.begin
|         ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-360
This is not strong emphasis, because the opening delimiter is followed by whitespace:
__ foo bar__
| <- - punctuation
|         ^^ - punctuation

http://spec.commonmark.org/0.27/#example-361
__
| <- - punctuation

http://spec.commonmark.org/0.27/#example-362
a__"foo"__
|^^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-363
Intraword strong emphasis is forbidden with `__`:
foo__bar__
|  ^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-364
5__6__78
|^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-367
foo-__(bar)__
|   ^^ punctuation.definition.bold.begin
|          ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-368
**foo bar **
| <- punctuation.definition.bold.begin
|         ^^ - punctuation
abc**
|  ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-373
Intraword emphasis:
 **foo**bar
|^^ punctuation.definition.bold.begin
|     ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-374
 __foo bar __
|^^ punctuation.definition.bold.begin
|          ^^ - punctuation
abc__
|  ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-376
_(__foo__)_
| <- punctuation.definition.italic.begin
| ^^ punctuation.definition.bold.begin
|      ^^ punctuation.definition.bold.end
|         ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-377
Intraword strong emphasis is forbidden with `__`:
__foo__bar
| <- punctuation.definition.bold.begin
|    ^^ - punctuation
abc__
|  ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-379
__foo__bar__baz__
| <- punctuation.definition.bold.begin
|              ^^ punctuation.definition.bold.end
|    ^^^^^^^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-380
This is strong emphasis, even though the closing delimiter is both left- and right-flanking, because it is followed by punctuation:
__(bar)__.
| <- punctuation.definition.bold.begin
|      ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-381
*foo [bar](/url)*
| <- punctuation.definition.italic.begin
|               ^ punctuation.definition.italic.end
|    ^^^^^^^^^^^ meta.link.inline

http://spec.commonmark.org/0.27/#example-382
*foo
| <- punctuation.definition.italic.begin
bar*
|  ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-383
_foo __bar__ baz_
| <- punctuation.definition.italic.begin
|    ^^ punctuation.definition.bold.begin
|         ^^ punctuation.definition.bold.end
|               ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-394
** is not an empty emphasis
| <- - punctuation
|^ - punctuation

http://spec.commonmark.org/0.27/#example-395
**** is not an empty strong emphasis
| <- - punctuation
|^^^ - punctuation

http://spec.commonmark.org/0.27/#example-396
**foo [bar](/url)**
| <- punctuation.definition.bold.begin
|     ^^^^^^^^^^^ meta.link.inline
|                ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-397
**foo
| <- punctuation.definition.bold.begin
bar**
|  ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-398
__foo _bar_ baz__
| <- punctuation.definition.bold.begin
|     ^ punctuation.definition.italic.begin
|         ^ punctuation.definition.italic.end
|              ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-408
__ is not an empty emphasis
| <- - punctuation
|^ - punctuation

http://spec.commonmark.org/0.27/#example-409
____ is not an empty strong emphasis
| <- - punctuation
|^^^ - punctuation


http://spec.commonmark.org/0.27/#example-410
foo ***
|   ^^^ - punctuation

http://spec.commonmark.org/0.27/#example-411
foo *\**
|   ^ punctuation.definition.italic.begin
|    ^^ constant.character.escape
|      ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-412
foo *_*
|   ^ punctuation.definition.italic.begin
|    ^ - punctuation
|     ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-414
foo **\***
|   ^^ punctuation.definition.bold.begin
|     ^^ constant.character.escape
|       ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-415
foo **_**
|   ^^ punctuation.definition.bold.begin
|     ^ - punctuation
|      ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-422
foo ___
|   ^^^^ - punctuation

http://spec.commonmark.org/0.27/#example-423
foo _\__
|   ^ punctuation.definition.italic.begin
|    ^^ constant.character.escape
|      ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-424
foo _*_
|   ^ punctuation.definition.italic.begin
|    ^ - punctuation
|     ^ punctuation.definition.italic.end

http://spec.commonmark.org/0.27/#example-426
foo __\___
|   ^^ punctuation.definition.bold.begin
|     ^^ constant.character.escape
|       ^^ punctuation.definition.bold.end

http://spec.commonmark.org/0.27/#example-427
foo __*__
|   ^^ punctuation.definition.bold.begin
|     ^ - punctuation
|      ^^ punctuation.definition.bold.end

This text is _bold_, but this__text__is neither bold_nor_italic
|            ^ punctuation.definition.italic
|             ^^^^ markup.italic
|                 ^ punctuation.definition.italic
|                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.bold - markup.italic

the following is italic *and doesn't end here * but does end here*
|                       ^ punctuation.definition.italic.begin
|                                             ^ - punctuation.definition.italic
|                                                                ^ punctuation.definition.italic.end
the following is bold **and doesn't end here ** but does end here**
|                     ^^ punctuation.definition.bold.begin
|                                            ^^ - punctuation.definition.bold
|                                                                ^^ punctuation.definition.bold.end
the following is not bold ** test ****
|                         ^^ - punctuation.definition.bold.begin
|                                 ^^^^ - punctuation.definition.bold
the following is not italic _ test ____
|                           ^ - punctuation.definition.italic.begin
|                                  ^^^^ - punctuation.definition.italic

more **tests *** ** here**
|    ^^ punctuation.definition.bold.begin
|            ^^^^^^ - punctuation.definition
|                       ^^ punctuation.definition.bold.end
more __tests *** ** example __ here__
|    ^^ punctuation.definition.bold.begin
|            ^^^^^^^^^^^^^^^^^^^^^^ - punctuation.definition
|                                  ^^ punctuation.definition.bold.end
more _tests <span class="test_">here</span>_
|    ^ punctuation.definition.italic.begin
|                            ^ - punctuation.definition
|                                          ^ punctuation.definition.italic.end
more _tests <span class="test_">_here</span>_
|    ^ punctuation.definition.italic.begin
|                            ^ - punctuation.definition
|                               ^ - punctuation
|                                           ^ punctuation.definition.italic.end
_more `tests_` here_
| <- punctuation.definition.italic.begin
|     ^^^^^^^^ markup.raw.inline
|                  ^ punctuation.definition.italic.end
__more `tests__` here__
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end
**more `tests__` here**
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end
**more `tests**` here**
| <- punctuation.definition.bold.begin
|      ^^^^^^^^^ markup.raw.inline
|                    ^^ punctuation.definition.bold.end
*more `tests__` here**
| <- punctuation.definition.italic.begin
|                   ^^ - punctuation
abc*
|  ^ punctuation.definition.italic.end

_test <span>text_ foobar</span>
| <- punctuation
|               ^ punctuation.definition.italic.end
__test <span>text__ not formatted</span>
| <- punctuation
|                ^^ punctuation.definition.bold.end
*test <span>text* not formatted</span>
| <- punctuation
|               ^ punctuation.definition.italic.end
**test <span>text** not formatted</span>
| <- punctuation
|                ^^ punctuation.definition.bold.end
_test <span>text **formatted**</span>_
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation
*test <span>text __formatted__</span>*
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation
*test <span>text __formatted__</span>* **more** _text_
| <- punctuation
|                ^^ punctuation
|                           ^^ punctuation
|                                    ^ punctuation
|                                      ^^ punctuation
|                                            ^^ punctuation
|                                               ^ punctuation
|                                                    ^ punctuation
*test <span>text* __formatted</span>__
| <- punctuation
|               ^ punctuation
|                 ^^ punctuation
|                                   ^^ punctuation

__test <span>text__ *formatted</span>*
| <- punctuation
|                ^^ punctuation
|                   ^ punctuation
|                                    ^ punctuation

This is ***bold italic***
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ***bold italic* and just bold**
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^^^^^^^^^^^^^^^ - markup.italic
|                                    ^^ punctuation.definition.bold.end

The next scope overlap funny because we have to pick one order
to scope three indicators in a row
This is ***bold italic** and just italic*
|       ^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.italic
|         ^ punctuation.definition.italic.begin
|                     ^^ punctuation.definition.bold.end
|                       ^^^^^^^^^^^^^^^^^ - markup.bold
|                                       ^ punctuation.definition.italic.end

This is **_bold italic_**
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is __*bold italic*__
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ___bold italic___
|       ^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^ punctuation.definition.bold.end

This is ___bold italic_ and just bold__
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^ punctuation.definition.italic.begin
|         ^^^^^^^^^^^^^ markup.italic
|                     ^ punctuation.definition.italic.end
|                      ^^^^^^^^^^^^^^^^ - markup.italic
|                                    ^^ punctuation.definition.bold.end

The next scope overlap funny because we have to pick one order
to scope three indicators in a row
This is ___bold italic__ and just italic_
|       ^^^^^^^^^^^^^^^ markup.bold
|       ^^ punctuation.definition.bold.begin
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.italic
|         ^ punctuation.definition.italic.begin
|                     ^^ punctuation.definition.bold.end
|                       ^^^^^^^^^^^^^^^^^ - markup.bold
|                                       ^ punctuation.definition.italic.end

This is _**italic bold**_
|       ^^^^^^^^^^^^^^^^^ markup.italic
|       ^ punctuation.definition.italic.begin
|        ^^^^^^^^^^^^^^^ markup.bold
|        ^^ punctuation.definition.bold.begin
|                     ^^ punctuation.definition.bold.end
|                       ^ punctuation.definition.italic.end

This is *__italic bold__*
|       ^^^^^^^^^^^^^^^^^ markup.italic
|       ^ punctuation.definition.italic.begin
|        ^^^^^^^^^^^^^^^ markup.bold
|        ^^ punctuation.definition.bold.begin
|                     ^^ punctuation.definition.bold.end
|                       ^ punctuation.definition.italic.end

**test!_test** Issue 1163
|^^^^^^^^^^^^^ markup.bold
|      ^ - punctuation.definition.italic
|           ^^ punctuation.definition.bold.end

__test!*test__ Issue 1163
|^^^^^^^^^^^^^ markup.bold
|      ^ - punctuation.definition.italic
|           ^^ punctuation.definition.bold.end

# Strikethrough Tests

__~~bold striked~~__
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^ markup.bold.markdown - markup.strikethrough
| ^^^^^^^^^^^^^^^^ markup.bold.markdown markup.strikethrough.markdown-gfm
|                 ^^ markup.bold.markdown - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown
| ^^ punctuation.definition.strikethrough.begin.markdown
|               ^^ punctuation.definition.strikethrough.end.markdown 
|                 ^^ punctuation.definition.bold.end.markdown

**~~bold striked~~**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^ markup.bold.markdown - markup.strikethrough
| ^^^^^^^^^^^^^^^^ markup.bold.markdown markup.strikethrough.markdown-gfm
|                 ^^ markup.bold.markdown - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown
| ^^ punctuation.definition.strikethrough.begin.markdown
|               ^^ punctuation.definition.strikethrough.end.markdown 
|                 ^^ punctuation.definition.bold.end.markdown

_~~italic striked~~_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^^^^^^^^ markup.italic.markdown markup.strikethrough.markdown-gfm
|                  ^ markup.italic.markdown - markup.strikethrough
|^^ punctuation.definition.strikethrough.begin.markdown
|                ^^ punctuation.definition.strikethrough.end.markdown 
|                  ^ punctuation.definition.italic.end.markdown

*~~italic striked~~*
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^^^^^^^^ markup.italic.markdown markup.strikethrough.markdown-gfm
|                  ^ markup.italic.markdown - markup.strikethrough
|^^ punctuation.definition.strikethrough.begin.markdown
|                ^^ punctuation.definition.strikethrough.end.markdown 
|                  ^ punctuation.definition.italic.end.markdown

___~~bold italic striked~~___
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^ markup.bold.markdown - markup.italic - markup.strikethrough
| ^ markup.bold.markdown markup.italic.markdown - markup.strikethrough
|  ^^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown markup.italic.markdown markup.strikethrough.markdown-gfm
|                         ^ markup.bold.markdown markup.italic.markdown - markup.strikethrough
|                          ^^ markup.bold.markdown - markup.italic - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown
| ^ punctuation.definition.italic.begin.markdown
|  ^^ punctuation.definition.strikethrough.begin.markdown
|                       ^^ punctuation.definition.strikethrough.end.markdown 
|                         ^ punctuation.definition.italic.end.markdown
|                          ^^ punctuation.definition.bold.end.markdown

***~~bold italic striked~~***
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^ markup.bold.markdown - markup.italic - markup.strikethrough
| ^ markup.bold.markdown markup.italic.markdown - markup.strikethrough
|  ^^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown markup.italic.markdown markup.strikethrough.markdown-gfm
|                         ^ markup.bold.markdown markup.italic.markdown - markup.strikethrough
|                          ^^ markup.bold.markdown - markup.italic - markup.strikethrough
|^ punctuation.definition.bold.begin.markdown
| ^ punctuation.definition.italic.begin.markdown
|  ^^ punctuation.definition.strikethrough.begin.markdown
|                       ^^ punctuation.definition.strikethrough.end.markdown 
|                         ^ punctuation.definition.italic.end.markdown
|                          ^^ punctuation.definition.bold.end.markdown

~Hi~ Hello, world!
| <- punctuation.definition.strikethrough.begin
|^^^ meta.paragraph markup.strikethrough
|  ^ punctuation.definition.strikethrough.end
|   ^^^^^^^^^^^^^^^ meta.paragraph - markup

This ~text~~~~ is ~~~~curious~.
|    ^^^^^^^^^ meta.paragraph markup.strikethrough
|                 ^^^^^^^^^^^^ meta.paragraph markup.strikethrough
|                             ^^ meta.paragraph - markup
|    ^ punctuation.definition.strikethrough.begin
|         ^^^^ punctuation.definition.strikethrough.end
|                 ^^^^ punctuation.definition.strikethrough.begin
|                            ^ punctuation.definition.strikethrough.end

This ~~has a
|    ^^^^^^^^ meta.paragraph markup.strikethrough

| <- meta.paragraph markup.strikethrough invalid.illegal.non-terminated.bold-italic
new paragraph~~.
|            ^^ meta.paragraph markup.strikethrough punctuation.definition.strikethrough.begin

| <- invalid.illegal.non-terminated.bold-italic


# Fenced Code Block Tests

Paragraph is terminated by fenced code blocks.
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

Code blocks terminate **bold text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be bold**
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Code blocks terminate __bold text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be bold__
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Code blocks terminate *italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be italic*
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.italic

Code blocks terminate _italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be italic_
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate ***bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be bold italic***
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate ___bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be bold italic___
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

Code blocks terminate **_bold italic text
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
this must not be bold italic_**
| <- - meta.bold - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - meta.italic

```js
| <- punctuation.definition.raw.code-fence.begin
|  ^^ constant.other.language-name
for (var i = 0; i < 10; i++) {
| ^ source.js keyword.control.loop
    console.log(i);
}
```
| <- punctuation.definition.raw.code-fence.end

```ts
|  ^^ constant.other.language-name
declare type foo = 'bar'
```

```R%&?! weired language name
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm
|  ^^^^^ constant.other.language-name.markdown
|        ^^^^^^^^^^^^^^^^^^^^^ - constant
```

```{key: value}
|^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm
|  ^^^^^^^^^^^^ - constant
```

``` {key: value}
|^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm
|   ^^^^^^^^^^^^ - constant
```

```testing``123```
| <- punctuation.definition.raw.begin
|         ^^ - punctuation
|              ^^^ punctuation.definition.raw.end
```testing``123````
| <- punctuation.definition.raw.begin
|        ^ - punctuation
|            ^^^^ - punctuation
```
| <- punctuation.definition.raw.end
``testing`123````
| <- punctuation.definition.raw.begin
|        ^ - punctuation
|            ^^^^ - punctuation
more text``
|        ^^ punctuation.definition.raw.end
``text

| <- invalid.illegal.non-terminated.raw
text
| <- - markup.raw

http://spec.commonmark.org/0.28/#example-315
`` foo ` bar  ``
|^ punctuation.definition.raw.begin
|^^^^^^^^^^^^^^^ markup.raw.inline
|      ^ - punctuation
|             ^^ punctuation.definition.raw.end

http://spec.commonmark.org/0.28/#example-316
` `` `
|<- punctuation.definition.raw.begin
|^^^^^ markup.raw.inline
| ^^ - punctuation
|    ^ punctuation.definition.raw.end

http://spec.commonmark.org/0.28/#example-318
`foo   bar
  baz`
|^^^^^ markup.raw.inline
|    ^ punctuation.definition.raw.end

~~~~ 
| <- punctuation.definition.raw.code-fence.begin
 ~~~~
| ^^^ punctuation.definition.raw.code-fence.end

~~~~~test~
| ^^^^^^^^^ meta.paragraph - constant - markup.raw

~~~~~~test
| ^^^^ punctuation.definition.raw.code-fence.begin
|     ^^^^ constant.other.language-name
~~~~~~
| ^^^^ punctuation.definition.raw.code-fence.end

```test
|  ^^^^ constant.other.language-name
  ```
| ^^^ punctuation.definition.raw.code-fence.end

hello world ````test````
|           ^^^^^^^^^^^^ markup.raw.inline
|                       ^ - markup.raw

`foo `` bar`
|    ^^^^^^ markup.raw.inline - punctuation
|          ^ punctuation.definition.raw.end

hard line break  
|              ^^ meta.hard-line-break punctuation.definition.hard-line-break
hard line break\
|              ^ meta.hard-line-break constant.character.escape
hard line break     
|              ^^^^^ meta.hard-line-break punctuation.definition.hard-line-break
soft line break 
|              ^^ - meta.hard-line-break
soft line break
|             ^^ - meta.hard-line-break

### foo  
|      ^^^ - meta.hard-line-break
### foo\
|      ^ - meta.hard-line-break

`inline code with trailing spaces  
|                                ^^^ - meta.hard-line-break
not a hard line break`

*test

| <- invalid.illegal.non-terminated.bold-italic
abc*
|  ^ - punctuation

_test

| <- invalid.illegal.non-terminated.bold-italic
abc_
|  ^ - punctuation

**test

| <- invalid.illegal.non-terminated.bold-italic
abc**
|  ^^ - punctuation

__test

| <- invalid.illegal.non-terminated.bold-italic
abc__
|  ^^ - punctuation

__test\
|     ^ meta.hard-line-break constant.character.escape
testing__

- test *testing
blah*
|   ^ markup.list.unnumbered meta.paragraph.list markup.italic punctuation.definition.italic.end - meta.paragraph.list meta.paragraph.list
- fgh
- *ghgh
| ^ markup.list.unnumbered meta.paragraph.list markup.italic punctuation.definition.italic.begin - meta.paragraph.list meta.paragraph.list
- fgfg
| <- markup.list.unnumbered.bullet punctuation.definition.list_item
- _test

| <- markup.list.unnumbered meta.paragraph.list markup.italic invalid.illegal.non-terminated.bold-italic
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list
- * * * * * * *
| <- punctuation.definition.list_item
| ^^^^^^^^ markup.list.unnumbered meta.paragraph.list meta.separator.thematic-break - meta.paragraph.list meta.paragraph.list
| ^ punctuation.definition.thematic-break
|   ^ punctuation.definition.thematic-break
|     ^ punctuation.definition.thematic-break
|       ^ punctuation.definition.thematic-break
|         ^ punctuation.definition.thematic-break
|           ^ punctuation.definition.thematic-break
|             ^ punctuation.definition.thematic-break
|  ^ - punctuation.definition.thematic-break
|    ^ - punctuation.definition.thematic-break
|      ^ - punctuation.definition.thematic-break
|        ^ - punctuation.definition.thematic-break
|          ^ - punctuation.definition.thematic-break
|            ^ - punctuation.definition.thematic-break
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list - meta.paragraph.list meta.paragraph.list

http://spec.commonmark.org/0.27/#example-407
**foo [*bar*](/url)**
| <- punctuation.definition.bold.begin
|     ^^^^^^^^^^^^^ markup.bold meta.link.inline
|                  ^^ punctuation.definition.bold.end
|      ^ punctuation.definition.italic.begin
|          ^ punctuation.definition.italic.end
**foo [_bar_](/url)**
| <- punctuation.definition.bold.begin
|     ^^^^^^^^^^^^^ markup.bold meta.link.inline
|                  ^^ punctuation.definition.bold.end
|      ^ punctuation.definition.italic.begin
|          ^ punctuation.definition.italic.end
_foo [**bar**](/url)_
| <- punctuation.definition.italic.begin
|    ^^^^^^^^^^^^^^^ markup.italic meta.link.inline
|                   ^ punctuation.definition.italic.end
|     ^^ punctuation.definition.bold.begin
|          ^^ punctuation.definition.bold.end


1. Open `Command Palette` using menu item `Tools → Command Palette...`
|^ markup.list.numbered punctuation.definition.list_item
|                                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered meta.paragraph.list markup.raw.inline
2. Choose `Package Control: Install Package`

[**Read more &#8594;**][details]
|^^ punctuation.definition.bold.begin
|            ^^^^^^^ constant.character.entity.decimal.html
|                   ^^ punctuation.definition.bold.end
|                       ^^^^^^^ constant.other.reference.link

[Read more &#8594;][details]
|          ^^^^^^^ constant.character.entity.decimal.html
|                   ^^^^^^^ constant.other.reference.link

[Read more <span style="font-weight: bold;">&#8594;</span>][details]
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description
|                       ^^^^^^^^^^^^^^^^^^ source.css
|                                           ^^^^^^^ constant.character.entity.decimal.html
|                                                           ^^^^^^^ constant.other.reference.link

[![Cool ★ Image - Click to Enlarge][img-example]][img-example]
|^ punctuation.definition.image.begin
|                                   ^^^^^^^^^^^ constant.other.reference.link
|                                               ^ punctuation.definition.link.end
|                                                 ^^^^^^^^^^^ constant.other.reference.link

[![Cool ★ Image - Click to Enlarge](http://www.sublimetext.com/anim/rename2_packed.png)](http://www.sublimetext.com/anim/rename2_packed.png)
|^ punctuation.definition.image.begin
|                                  ^ punctuation.definition.metadata.begin
|                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                                                     ^ punctuation.definition.metadata.end
|                                                                                       ^ punctuation.definition.metadata.begin
|                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                                                                                                          ^ punctuation.definition.metadata.end

[img-example]: http://www.sublimetext.com/anim/rename2_packed.png
|^^^^^^^^^^^ meta.link.reference.def.markdown entity.name.reference.link
|            ^ punctuation.separator.key-value
|              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                                ^ - meta.link - markup

[//]: # (This is a comment without a line-break.)
|     ^ meta.link.reference.def.markdown markup.underline.link
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                ^ - meta.link

[//]: # (This is a comment with a
|     ^ meta.link.reference.def.markdown markup.underline.link
|       ^ punctuation.definition.string.begin
        line-break.)
|                  ^ punctuation.definition.string.end
|                   ^ - meta.link

[//]: # (testing)blah
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|       ^ punctuation.definition.string.begin
|               ^ punctuation.definition.string.end
|                ^^^^ invalid.illegal.expected-eol
|                    ^ - meta.link - invalid

[//]: # (testing
blah
| <- meta.link.reference.def.markdown string.other.link.description.title

| <- invalid.illegal.non-terminated.link-title
text
| <- meta.paragraph - meta.link.reference.def.markdown

[foo]: <bar> "test" 
|^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|                   ^ - meta.link
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|            ^^^^^^ string.other.link.description.title
|                  ^ - invalid.illegal.expected-eol

[foo]: <bar>> "test" 
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|                    ^ - meta.link
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|           ^^^^^^^^ invalid.illegal.expected-eol
|                   ^ - invalid.illegal.expected-eol

https://michelf.ca/projects/php-markdown/extra/#footnotes
That's some text with a footnote.[^1]
|                                ^^^^ meta.paragraph meta.link.reference.footnote.markdown-extra
|                                ^ punctuation.definition.link.begin
|                                 ^^ meta.link.reference.literal.footnote-id
|                                   ^ punctuation.definition.link.end

 [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
|^ punctuation.definition.reference.begin.markdown
| ^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown

[^1]:
    And that's the footnote.

    That's the *second* paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra - markup.raw
|              ^^^^^^^^ markup.italic

- a
  - b
    - c
      - d
|     ^ markup.list.unnumbered.bullet punctuation.definition.list_item
        text here
|       ^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list - markup.raw.block - meta.paragraph.list meta.paragraph.list

            code here
            | ^^^^^^^^ markup.raw.block

      - e
|     ^ markup.list.unnumbered.bullet punctuation.definition.list_item

            code here

            >     block quote code here
|           ^ markup.list.unnumbered markup.quote punctuation.definition.blockquote
|                 ^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered markup.quote markup.raw.block

            > > test
|           ^ markup.list.unnumbered markup.quote punctuation.definition.blockquote
|             ^ markup.list.unnumbered markup.quote markup.quote punctuation.definition.blockquote - markup.raw.block

      - f
|     ^ markup.list.unnumbered.bullet punctuation.definition.list_item
        1. test
|       ^^ markup.list.numbered.bullet
|        ^ punctuation.definition.list_item

abc
| <- meta.paragraph - markup.list

| foo | bar |
|^^^^^^^^^^^^^ meta.table.header
| <- punctuation.separator.table-cell
|     ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
| ^^^^ - punctuation.separator.table-cell
| --- | --- |
| baz | bim <kbd>Ctrl+C</kbd> |
| <- meta.table punctuation.separator.table-cell
|           ^^^^^ meta.tag.inline.any
|                             ^ punctuation.separator.table-cell

| <- - meta.table

| abc | defghi |
:-: | -----------:
|^^^^^^^^^^^^^^^^^ meta.table.header-separator
| <- punctuation.definition.table-cell-alignment
|^ punctuation.section.table-header
|   ^ punctuation.separator.table-cell
|     ^^^^^^^^^^^ punctuation.section.table-header
|                ^ punctuation.definition.table-cell-alignment - punctuation.section.table-header
bar | baz
|   ^ meta.table punctuation.separator.table-cell

| f\|oo  |
| <- meta.table punctuation.separator.table-cell
|  ^^ meta.table constant.character.escape - punctuation.separator.table-cell
|        ^ meta.table punctuation.separator.table-cell
| ------ |
| b `|` az |
|   ^^^ meta.table markup.raw.inline - meta.table.header-separator
|          ^ meta.table punctuation.separator.table-cell
| b **|** im |
| <- meta.table punctuation.separator.table-cell
|   ^^^^^ meta.table markup.bold - punctuation.separator.table-cell
|            ^ meta.table punctuation.separator.table-cell

| abc | def |
| --- | --- |
| bar | baz |
|^^^^^^^^^^^^^ meta.table
test
|^^^^ meta.table
> bar
| <- markup.quote punctuation.definition.blockquote - meta.table

`|` this `|` example `|` is not a table `|`
| ^ punctuation.definition.raw.end - meta.table
| nor is this | because it is not at block level, it immediately follows a paragraph |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - meta.table

| First Header  | Second Header | Third Header         |
| :------------ | :-----------: | -------------------: |
| First row     | Data          | Very long data entry |
| Second row    | **Cell**      | *Cell*               |
| Third row     | Cell that spans across two columns  ||
| ^^^^^^^^^^^^^^ meta.table
|                                                     ^^ punctuation.separator.table-cell

 | table that doesn't start at column 0 |
  | ---- |
  | blah |
| ^^^^^^^^ meta.table
| ^ punctuation.separator.table-cell

not a table | 
| ^^^^^^^^^^^^^ - meta.table

 abc | def
 --- | ---
 --- | ---
| ^^^^ meta.table - meta.table.header

 a | b
 - | -
|^^^^^^ meta.table.header-separator.markdown-gfm
|^ punctuation.section.table-header.markdown
|  ^ punctuation.separator.table-cell.markdown
|    ^ punctuation.section.table-header.markdown
 - | -
|^^^^^^ meta.table.markdown-gfm

 a | b
 -:| -
|^^^^^^ meta.table.header-separator.markdown-gfm
|^ punctuation.section.table-header.markdown
| ^ punctuation.definition.table-cell-alignment.markdown
|  ^ punctuation.separator.table-cell.markdown
|    ^ punctuation.section.table-header.markdown
 - | -
|^^^^^^ meta.table.markdown-gfm

| test | me |
|------|----|
|^^^^^^ punctuation.section.table-header
|*test | me |
|^^^^^^ - markup.bold
|      ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
|`test | me |
|^ invalid.deprecated.unescaped-backticks
|      ^ punctuation.separator.table-cell

| table | followed by
# heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^ markup.heading.1.markdown

| table | followed by
> quote
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^^^ markup.quote.markdown

| table | followed by
    quote
| <- markup.raw.block.markdown
|^^^^^^^^^ markup.raw.block.markdown

| table | followed by
```fenced
| <- meta.code-fence.definition.begin.text.markdown-gfm
|^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm
code block
```
| <- meta.code-fence.definition.end.text.markdown-gfm
|^^ meta.code-fence.definition.end.text.markdown-gfm

A line without bolded |
|                     ^ - punctuation.separator.table-cell

A line with bolded **|**
|                    ^ - punctuation.separator.table-cell

1. test
|  ^^^^^ markup.list.numbered meta.paragraph.list
   - test
|^^^^^^^^^ markup.list.unnumbered
|  ^ markup.list.unnumbered.bullet punctuation.definition.list_item
|    ^^^^^ meta.paragraph.list
   - test
|^^^^^^^^^ markup.list.unnumbered
|  ^ markup.list.unnumbered.bullet punctuation.definition.list_item
|    ^^^^^ meta.paragraph.list
   test
|^^^^^^^ markup.list.numbered meta.paragraph.list
 ****test****
|^^^^^^^^^^^^^ markup.list.numbered meta.paragraph.list - punctuation

 - - test
|^ punctuation.definition.list_item
|  ^^^^^^^ markup.list.unnumbered meta.paragraph.list - punctuation
- - - - test
| <- punctuation.definition.list_item
| ^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list - punctuation

paragraph

  * List Item 1
    Text under Item 1
  * List Item 2
    Text under Item 2

  * List Item 3
    Text under Item 3
|   ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered meta.paragraph.list - markup.raw

 1. fenced code block inside a list item
| ^ punctuation.definition.list_item
    ```language
|^^^^^^^^^^^^^^^ meta.paragraph.list
|   ^^^ punctuation.definition.raw.code-fence.begin
|      ^^^^^^^^ constant.other.language-name
|   ^^^^^^^^^^^ meta.code-fence
    
|^^^^ meta.paragraph.list markup.raw.code-fence
    ```
|   ^^^ punctuation.definition.raw.code-fence.end
    test
|   ^^^^^ meta.paragraph.list - markup.raw.code-fence

 2. test
| ^ punctuation.definition.list_item

Normal paragraph
| <- meta.paragraph - markup

1. List
    1. Nested list
    2. Second item

    This line is still list item 1
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered - markup.raw.block

Test
| <- meta.paragraph - markup.list

http://spec.commonmark.org/0.28/#example-116

<table><tr><td>
<pre>
**Hello**,
| ^^^^^^^^^ meta.disable-markdown

_world_.
| ^^^^ markup.italic - meta.disable-markdown
</pre>
</td></tr></table>

http://spec.commonmark.org/0.28/#example-120

<DIV CLASS="foo">
| ^^^^^^^^^^^^^^^^ meta.disable-markdown

*Markdown*
| ^^^^^^^ meta.paragraph markup.italic - meta.disable-markdown

</DIV>
| ^^^ meta.disable-markdown meta.tag.block.any.html

http://spec.commonmark.org/0.28/#example-127

<div><a href="bar">*foo*</a></div>
|                  ^^^^^ meta.disable-markdown - markup.italic

http://spec.commonmark.org/0.28/#example-129

<div></div>
``` c
int x = 33;
```
| ^^ meta.disable-markdown

http://spec.commonmark.org/0.28/#example-130

<a href="foo">
*bar*
|^^^^^ meta.disable-markdown
</a>

http://spec.commonmark.org/0.28/#example-131

<Warning>
*bar*
|^^^^^ meta.disable-markdown
</Warning>
| ^^^^^^^ meta.disable-markdown meta.tag.other.html entity.name.tag.other.html

http://spec.commonmark.org/0.28/#example-135

<del>
| ^^ meta.disable-markdown meta.tag.inline.any.html entity.name.tag.inline.any.html

*foo*
| ^^ meta.paragraph markup.italic

</del>
| ^^^ meta.disable-markdown meta.tag.inline.any.html entity.name.tag.inline.any.html

<del>
*foo*
|^^^^^ meta.disable-markdown
</del>

http://spec.commonmark.org/0.28/#example-136

<del>*foo*</del>
| ^^ meta.tag.inline.any.html entity.name.tag.inline.any.html
|    ^^^^^ markup.italic
|           ^^^ meta.tag.inline.any.html entity.name.tag.inline.any.html
|^^^^^^^^^^^^^^^ meta.paragraph - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-137

<pre language="haskell"><code>
| ^^ meta.disable-markdown meta.tag.block.any.html entity.name.tag.block.any.html
import Text.HTML.TagSoup

main :: IO ()
| ^^^^^^^^^^^^ meta.disable-markdown
main = print $ parseTags tags
</code></pre>
| ^^^^^^^^^^^ meta.disable-markdown
|        ^^^ meta.tag.block.any.html entity.name.tag.block.any.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-138

<script type="text/javascript">
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.script.begin.html
// JavaScript example
| ^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown source.js.embedded.html comment.line.double-slash.js

document.getElementById("demo").innerHTML = "Hello JavaScript!";
| ^^^^^^ meta.disable-markdown source.js.embedded.html support.type.object.dom.js
</script>
| ^^^^^^ meta.disable-markdown meta.tag.script.end.html entity.name.tag.script.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-139

<style
  type="text/css">
| ^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.style.begin.html meta.attribute-with-value.html
h1 {color:red;}
|   ^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.property-name.css support.type.property-name.css

p {color:blue;}
|  ^^^^^ meta.disable-markdown source.css.embedded.html meta.property-list.css meta.property-name.css support.type.property-name.css
</style>
| ^^^^^ meta.disable-markdown meta.tag.style.end.html entity.name.tag.style.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-143

<style>p{color:red;}</style>
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
*foo*
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-144

<!-- foo -->*bar*
| ^^^^^^^^^^ comment.block.html
|           ^^^^^ meta.disable-markdown
*baz*
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-145

<script>
foo
</script>1. *bar*
| ^^^^^^^^^^^^^^^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-146

<!-- Foo
| ^^ meta.disable-markdown comment.block.html punctuation.definition.comment

bar
   baz -->
| ^^^^^^^^ meta.disable-markdown comment.block.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-147

<?php
| ^^^^ meta.disable-markdown

  echo '>';

?>
|^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-148

<!DOCTYPE html>
| ^^^^^^^ meta.disable-markdown meta.tag.sgml.doctype.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-149

<![CDATA[
| ^^^^^^^^ meta.disable-markdown meta.tag.sgml
function matchwo(a,b)
{
  if (a < b && a < 0) then {
    return 1;

  } else {

    return 0;
  }
}
]]>
|^ meta.disable-markdown meta.tag.sgml
okay
| <- - meta.disable-markdown

1. Test

   ```python
|  ^^^ markup.list.numbered meta.code-fence punctuation.definition.raw.code-fence.begin
       Test

| <- - invalid
       Test
   ```
|  ^^^ punctuation.definition.raw.code-fence.end

1. Test 2
|^ markup.list.numbered.bullet punctuation.definition.list_item

```clojure
|^^^^^^^^^ meta.code-fence.definition.begin.clojure
|  ^^^^^^^ constant.other.language-name
 (/ 10 3.0)
|<- source.clojure
|^^^^^^^^^^ source.clojure
```
|^^ meta.code-fence.definition.end.clojure punctuation.definition.raw.code-fence.end

```diff
+ inserted
| <- source.diff markup.inserted.diff punctuation.definition.inserted.diff
- deleted
| <- source.diff markup.deleted.diff punctuation.definition.deleted.diff
```

```haskell

| <- markup.raw.code-fence.haskell.markdown-gfm source.haskell
```

```html
  <html>
| <- markup.raw.code-fence.html.markdown-gfm text.html
| ^^^^^^ text.html meta.tag
```

```jsx

| <- markup.raw.code-fence.jsx.markdown-gfm
```

```lisp

| <- markup.raw.code-fence.lisp.markdown-gfm source.lisp
```

```lua

| <- markup.raw.code-fence.lua.markdown-gfm source.lua
```

```matlab

| <- markup.raw.code-fence.matlab.markdown-gfm source.matlab
```

```ocaml

| <- markup.raw.code-fence.ocaml.markdown-gfm source.ocaml
```

```scala

| <- markup.raw.code-fence.scala.markdown-gfm source.scala
```

```sh

| <- markup.raw.code-fence.shell-script.markdown-gfm source.shell.bash
```

```shell

| <- markup.raw.code-fence.shell-script.markdown-gfm source.shell.bash
```

```shell-script

| <- markup.raw.code-fence.shell-script.markdown-gfm source.shell.bash
```

```tsx

| <- markup.raw.code-fence.tsx.markdown-gfm
```

```xml
|^^^^^ meta.code-fence.definition.begin.xml
|  ^^^ constant.other.language-name
<?xml version="1.0" ?>
|^^^^^^^^^^^^^^^^^^^^^^ markup.raw.code-fence.xml
|     ^^^^^^^ meta.tag.preprocessor.xml entity.other.attribute-name.localname.xml
<example>
    <foobar />
</example>
```
|^^ punctuation.definition.raw.code-fence.end

```sql
|^^^^^ meta.code-fence.definition.begin.sql
|  ^^^ constant.other.language-name
SELECT TOP 10 *
|^^^^^^^^^^^^^^^ markup.raw.code-fence.sql
|^^^^^^^^^ keyword.other.DML.sql
FROM TableName
```
|^^ meta.code-fence.definition.end.sql punctuation.definition.raw.code-fence.end - markup

```python
|^^ punctuation.definition.raw.code-fence.begin
|^^^^^^^^^ meta.code-fence.definition.begin.python - markup
|  ^^^^^^ constant.other.language-name
def function():
    pass
|   ^^^^ keyword.control.flow
unclosed_paren = (
|                ^ meta.group.python punctuation.section.group.begin.python
```
|^^ meta.code-fence.definition.end.python punctuation.definition.raw.code-fence.end

```Graphviz
graph n {}
| ^^^ storage.type.dot
```

| <- - markup.raw

```php
var_dump(expression);
| ^^^^^^ support.function.var.php
```

```html+php
<div></div>
|^^^ entity.name.tag.block.any.html
<?php
|^^^^ punctuation.section.embedded.begin.php
var_dump(expression);
| ^^^^^^ support.function.var.php
```
|^^ punctuation.definition.raw.code-fence.end.markdown

```regex
(?x)
\s+
```
|^^^ meta.code-fence.definition.end.regexp - markup
|^^ punctuation.definition.raw.code-fence.end

```bash
# test
| ^^^^^ source.shell comment.line.number-sign
echo hello, \
|           ^^ punctuation.separator.continuation.line
echo This is a smiley :-\) \(I have to escape the parentheses, though!\)
|                       ^^ constant.character.escape
```
| <- meta.code-fence.definition.end.shell-script punctuation.definition.raw.code-fence.end

```     bash
| <- punctuation.definition.raw.code-fence.begin
|  ^^^^^ meta.code-fence.definition.begin.shell-script.markdown-gfm
|       ^^^^ constant.other.language-name
# test
| ^^^^^ source.shell comment.line.number-sign
```
| <- meta.code-fence.definition.end.shell-script punctuation.definition.raw.code-fence.end

~~~~    ruby startline=3 $%@#$
| <- punctuation.definition.raw.code-fence.begin
|   ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm
|       ^^^^ constant.other.language-name
|           ^^^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm
def foo(x)
  return 3
end
~~~~~~~
| <- meta.code-fence.definition.end.ruby punctuation.definition.raw.code-fence.end

\~/.bashrc
|^ constant.character.escape

  -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  - constant - keyword - variable

    -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw - constant - keyword - variable - punctuation

>  -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable

> > -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^ markup.quote.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable

\<div>
|<- constant.character.escape
|^ constant.character.escape
|^^^^^^ - meta.tag

\<div\>
|^ constant.character.escape
|^^^^^^ - meta.tag
|    ^^ constant.character.escape

link with a single underscore inside the text : [@_test](http://example.com)
|                                                ^^^^^^ meta.paragraph meta.link.inline.description - punctuation.definition
|                                                      ^ meta.paragraph meta.link.inline punctuation.definition.link.end

# h1
- list
## h2
|^ punctuation.definition.heading.begin
1. list
### h3
|^^ punctuation.definition.heading.begin

1. list [001]blah
|       ^^^^^ meta.link.reference
|       ^ punctuation.definition.link.begin
|           ^ punctuation.definition.link.end
|            ^^^^^ - meta.link

  [001]: https://en.wikipedia.org/wiki/Root-mean-square_deviation "Wikipedia - RMSE"
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered meta.link.reference.def.markdown
1. another list item

[foo]: /url "title"
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|    ^ punctuation.separator.key-value
|      ^^^^ markup.underline.link
|           ^^^^^^^ string.other.link.description.title

[foo]
|<- meta.link.reference punctuation.definition.link.begin
|^^^ meta.paragraph meta.link.reference
|   ^ meta.link.reference punctuation.definition.link.end

This is literal [Foo*bar\]] but [ref][Foo*bar\]]
|               ^^^^^^^^^^^ meta.link.reference.description.markdown
|               ^ punctuation.definition.link.begin.markdown
|                ^^^^^^^ string.other.link.title.markdown - constant
|                       ^^ string.other.link.title.markdown constant.character.escape.markdown
|                         ^ punctuation.definition.link.end.markdown
|                               ^^^^^ meta.link.reference.description.markdown
|                                    ^^^^^^^^^^^ meta.link.reference.metadata.markdown

 [Foo*bar\]]:my_(url) 'title (with parens)'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^ punctuation.definition.reference.begin.markdown
| ^^^^^^^^^ entity.name.reference.link.markdown - punctuation
|          ^ punctuation.definition.reference.end.markdown
|           ^ punctuation.separator.key-value.markdown
|            ^^^^^^^^ markup.underline.link
|                    ^ - markup - string
|                     ^^^^^^^^^^^^^^^^^^^^^ string.other.link.description.title

 [foo]: <>
|^^^^^^^^^ meta.link.reference.def.markdown
|     ^ punctuation.separator.key-value
|       ^ punctuation.definition.link.begin
|        ^ punctuation.definition.link.end

# CriticMarkup ################################################################

This is an {++additional++} word in {++**bold**++}.
|          ^^^^^^^^^^^^^^^^ markup.critic.addition.markdown
|          ^^^ punctuation.definition.critic.begin.markdown - markup.inserted
|             ^^^^^^^^^^ markup.inserted.critic.markdown
|                       ^^^ punctuation.definition.critic.end.markdown - markup.inserted
|                                   ^^^ markup.critic.addition.markdown - markup.inserted - markup.bold
|                                      ^^^^^^^^ markup.critic.addition.markdown markup.inserted.critic.markdown markup.bold.markdown
|                                              ^^^ markup.critic.addition.markdown - markup.inserted
|                                   ^^^ punctuation.definition.critic.begin.markdown
|                                      ^^ punctuation.definition.bold.begin.markdown
|                                            ^^ punctuation.definition.bold.end.markdown 
|                                              ^^^ punctuation.definition.critic.end.markdown

This is an {++ multiline
addition ++} test.
| <- markup.critic.addition.markdown
|^^^^^^^^ markup.critic.addition.markdown markup.inserted.critic.markdown
|        ^^^ markup.critic.addition.markdown - markup.inserted
|        ^^^ punctuation.definition.critic.end.markdown
|           ^^^^^^ - markup.critic

Additional {++[Link](https://foo.bar)++} and {++![Image](images/image.png)++}.
| ^^^^^^^^^ - markup.critic
|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.addition.markdown
|                                        ^^^^ - markup.critic
|                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.addition.markdown
|                                                                            ^^ - markup.critic
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^^^^^^ meta.link.inline.description.markdown
|                   ^^^^^^^^^^^^^^^^^ meta.link.inline.metadata.markdown
|                                    ^^^ punctuation.definition.critic.end.markdown
|                                            ^^^ punctuation.definition.critic.begin.markdown
|                                               ^^^^^^^^ meta.image.inline.description.markdown
|                                                       ^^^^^^^^^^^^^^^^^^ meta.image.inline.metadata.markdown
|                                                                         ^^^ punctuation.definition.critic.end.markdown

This is a {-- deletion --} and {~~substitute~>with~~striked~~text~~} or {~~~~old~~~>~~new~~~~}.
|         ^^^^^^^^^^^^^^^^ markup.critic.deletion.markdown
|         ^^^ punctuation.definition.critic.begin.markdown - markup.deleted
|            ^^^^^^^^^^ markup.deleted.critic.markdown
|                      ^^^ punctuation.definition.critic.end.markdown - markup.deleted
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown
|                                                                    ^^^ - markup.critic
|                                                                       ^^^^^^^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown
|                                                                                             ^^ - markup.critic
|                              ^^^ punctuation.definition.critic.begin.markdown - markup.deleted
|                                 ^^^^^^^^^^ markup.deleted.critic.markdown
|                                           ^^ punctuation.separator.critic.markdown - markup.deleted - markup.inserted
|                                              ^^^^^^^^^^^^^^^^^^ markup.inserted.critic.markdown
|                                                  ^^^^^^^^^^ markup.strikethrough.markdown-gfm
|                                                                ^^^ punctuation.definition.critic.end.markdown - markup.inserted
|                                                                       ^^^ punctuation.definition.critic.begin.markdown
|                                                                          ^^ punctuation.definition.strikethrough.begin.markdown
|                                                                          ^^^^^^^ markup.deleted.critic.markdown markup.strikethrough.markdown-gfm
|                                                                               ^^ punctuation.definition.strikethrough.end.markdown
|                                                                                 ^^ punctuation.separator.critic.markdown
|                                                                                   ^^ punctuation.definition.strikethrough.begin.markdown
|                                                                                   ^^^^^^^ markup.inserted.critic.markdown markup.strikethrough.markdown-gfm
|                                                                                        ^^ punctuation.definition.strikethrough.end.markdown
|                                                                                          ^^^ punctuation.definition.critic.end.markdown


This is a {>> comment <<}.
|         ^^^^^^^^^^^^^^^ markup.critic.comment.markdown
|         ^^^ punctuation.definition.critic.begin.markdown - comment
|            ^^^^^^^^^ comment.critic.markdown
|                     ^^^ punctuation.definition.critic.end.markdown - comment
|                        ^ - markup.critic

This is an {== information ==}{>> comment <<}.
|          ^^^^^^^^^^^^^^^^^^^ markup.critic.highlight.markdown
|                             ^^^^^^^^^^^^^^^ markup.critic.comment.markdown
|          ^^^ punctuation.definition.critic.begin.markdown -  markup.info
|             ^^^^^^^^^^^^^ markup.info.critic.markdown
|                          ^^^ punctuation.definition.critic.end.markdown -  markup.info
|                             ^^^ punctuation.definition.critic.begin.markdown - comment
|                                ^^^^^^^^^ comment.critic.markdown
|                                         ^^^ punctuation.definition.critic.end.markdown - comment
|                                            ^^ - markup.critic

This is a [[wiki link]].
|         ^^^^^^^^^^^^^ meta.link.reference.wiki.description.markdown
|         ^^ punctuation.definition.link.begin.markdown
|           ^^^^^^^^^ string.other.link.title.markdown
|                    ^^ punctuation.definition.link.end.markdown
