| SYNTAX TEST "Packages/Markdown/Markdown.sublime-syntax"

# Heading
| <- markup.heading.1 punctuation.definition.heading
|^^^^^^^^ markup.heading
|        ^ meta.whitespace.newline.markdown

## Second Heading #
| <- markup.heading.2 punctuation.definition.heading
|^^^^^^^^^^^^^^^^ markup.heading
|  ^^^^^^^^^^^^^^ entity.name.section
|                ^ - entity.name.section
|                 ^ punctuation.definition.heading.end.markdown
http://spec.commonmark.org/0.28/#example-43
## Example 43 (trailing spaces!) #####    
|                                    ^ punctuation.definition.heading.end.markdown
|                                         ^ meta.whitespace.newline.markdown
http://spec.commonmark.org/0.28/#example-44
## Example 44 ####    >
|^^^^^^^^^^^^^^^^^^^^^^ markup.heading
|             ^ - punctuation.definition.heading.end.markdown

Alternate Heading
=================
|^^^^^^^^^^^^^^^^ markup.heading.1 punctuation.definition

heading underlined with dashes
------------------------------
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.2 punctuation.definition.heading

underlined heading followed by a separator
-------------------
------
| <- meta.block-level meta.separator - markup.heading

underlined heading followed by another one that should be treated as a normal paragraph
==================
=====
| <- - markup.heading

Paragraph of text that should be scoped as meta.paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph
A [link](https://example.com){ :_attr = value }, *italic text* and **bold**.
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline
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

Here is a [reference link][name].
|         ^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference
|                         ^ punctuation.definition.constant.begin
|                          ^^^^ constant.other.reference.link
|                              ^ punctuation.definition.constant.end

Here is a [reference link][name]{_attr='value' :att2}.
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference
|                         ^ punctuation.definition.constant.begin
|                          ^^^^ constant.other.reference.link
|                              ^ punctuation.definition.constant.end
|                               ^ punctuation.definition.attributes.begin.markdown
|                                ^^^^^ entity.other.attribute-name.markdown
|                                     ^ punctuation.separator.key-value.markdown
|                                      ^^^^^^^ string.quoted.single.markdown
|                                              ^^^^^ entity.other.attribute-name.markdown
|                                                   ^ punctuation.definition.attributes.end.markdown

Here is a [blank reference link][]{}.
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference
|                               ^ punctuation.definition.constant.begin
|                                ^ punctuation.definition.constant.end
|                                 ^ punctuation.definition.attributes.begin.markdown
|                                  ^ punctuation.definition.attributes.end.markdown

Here is a ![](https://example.com/cat.gif).
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline
|          ^ punctuation.definition.image.begin
|           ^ punctuation.definition.image.end - string
|            ^ punctuation.definition.metadata
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                        ^ punctuation.definition.metadata

Here is a ![](https://example.com/cat.gif){_at"r=value :att2}.
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline
|          ^ punctuation.definition.image.begin
|           ^ punctuation.definition.image.end - string
|            ^ punctuation.definition.metadata
|             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                        ^ punctuation.definition.metadata
|                                         ^ punctuation.definition.attributes.begin.markdown
|                                          ^^^^^ entity.other.attribute-name.markdown
|                                             ^ invalid.illegal.attribute-name.markdown
|                                               ^ punctuation.separator.key-value.markdown
|                                                ^^^^^ string.unquoted.markdown
|                                                      ^^^^^ entity.other.attribute-name.markdown
|                                                           ^ punctuation.definition.attributes.end.markdown

Here is a ![Image Alt Text](https://example.com/cat.gif).
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline
|          ^ punctuation.definition.image.begin
|                         ^ punctuation.definition.image.end - string
|                          ^ punctuation.definition.metadata
|                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                                      ^ punctuation.definition.metadata

Here is a ![Image Alt Text](  https://example.com/cat.gif  ).
|         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.image.inline
|          ^ punctuation.definition.image.begin
|                         ^ punctuation.definition.image.end - string
|                          ^ punctuation.definition.metadata
|                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                                          ^ punctuation.definition.metadata

Here is a ![Image Alt Text](
  https://example.com/cat.gif  ).
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                              ^ punctuation.definition.metadata

Here is a ![Image Alt Text](
  https://example.com/cat.gif
 "hello"   ).
|^^^^^^^ meta.image.inline string.other.link.description.title
|       ^^^^ meta.image.inline
|          ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  <https://example.com/cat.gif> "hello"   ).
| ^ punctuation.definition.link.begin
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                             ^ punctuation.definition.link.end
|                               ^^^^^^^ string.other.link.description.title
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.image.inline
|                                         ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  <https://example .com /cat.gif> (hello)   ).
| ^ punctuation.definition.link.begin
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                 ^ invalid.illegal.unexpected-whitespace
|                      ^ invalid.illegal.unexpected-whitespace
|                               ^ punctuation.definition.link.end
|                                 ^^^^^^^ string.other.link.description.title
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.image.inline
|                                           ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  https://example .com /cat.gif (hello)   ).
| ^^^^^^^^^^^^^^^ markup.underline.link.image
|                ^ invalid.illegal.unexpected-whitespace
|                 ^^^^ markup.underline.link.image
|                     ^ invalid.illegal.unexpected-whitespace
|                      ^^^^^^^^ markup.underline.link.image
|                               ^^^^^^^ string.other.link.description.title
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.image.inline
|                                         ^ punctuation.definition.metadata.end

Here is a ![Image Ref Alt][1].
|         ^^^^^^^^^^^^^^^^^^^ meta.image.reference
|         ^^ punctuation.definition.image.begin
|                        ^ punctuation.definition.image.end
|                         ^ punctuation.definition.constant
|                          ^ constant.other.reference.link
|                           ^ punctuation.definition.constant

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca/documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.inline markup.underline.link
|                                                 ^ - invalid
|                                                  ^ meta.link.inline punctuation.definition.metadata.end

now you can access the [The Ever Cool Site: Documentation about Sites](
  www.thecoolsite.com.ca /documentations/about/cool ) for more information about...
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inline
| ^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                       ^ invalid.illegal.unexpected-whitespace
|                        ^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                  ^ - invalid
|                                                   ^ punctuation.definition.metadata.end

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

--------
|^^^^^^^^ meta.block-level meta.separator.thematic-break
|^^^^^^^ punctuation.definition.thematic-break

[1]: https://google.com
| <- meta.link.reference.def
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def
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

> Quote
| <- meta.block-level markup.quote punctuation.definition.blockquote
| ^^^^^^ meta.block-level markup.quote

> Quote followed by an empty block quote line
>
| <- meta.block-level markup.quote punctuation.definition.blockquote

> Quote followed by an empty block quote line
>
> Followed by more quoted text
| <- meta.block-level markup.quote punctuation.definition.blockquote

> > Nested quote
| <- meta.block-level markup.quote punctuation.definition.blockquote
| ^ meta.block-level markup.quote markup.quote punctuation.definition.blockquote

> > Nested quote
> Followed by more quoted text that is not nested
| <- meta.block-level markup.quote punctuation.definition.blockquote - markup.quote markup.quote

> Here is a quote block
This quote continues on.  Line breaking is OK in markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.block-level markup.quote
> Here it is again
| <- punctuation.definition.blockquote

paragraph
| <- meta.paragraph - meta.block-level

>     > this is code in a quote block, not a nested quote
| <- punctuation.definition.blockquote
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block - markup.quote markup.quote

>=
| <- punctuation.definition.blockquote.markdown 
  >=
| ^ punctuation.definition.blockquote.markdown
    >=
|   ^^ - punctuation.definition.blockquote.markdown

Code block below:

    this is code!
| ^^^^^^^^^^^^^^^^ meta.block-level markup.raw.block

    more code
    spanning multiple lines
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.block-level markup.raw.block

paragraph
| <- meta.paragraph - meta.block-level

- - - -
| ^^^^^^ meta.block-level meta.separator
| ^ punctuation.definition.thematic-break
|   ^ punctuation.definition.thematic-break
|     ^ punctuation.definition.thematic-break
|  ^ - punctuation
* * * * *
| ^^^^^^^^ meta.block-level meta.separator

_ _ _ _ _ _ _
| ^^^^^^^^^^^^ meta.block-level meta.separator
| ^ punctuation.definition.thematic-break
|   ^ punctuation.definition.thematic-break
|  ^ - punctuation

-  -  -  - 
| <- meta.block-level meta.separator.thematic-break punctuation.definition.thematic-break
|^^ - punctuation
|  ^ punctuation
|        ^ punctuation

<mailto:test+test@test.com>
| ^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.email.lt-gt markup.underline.link
<http://www.test.com/>
| ^^^^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet markup.underline.link
<https://test.com/>
| ^^^^^^^^^^^^^^^^ meta.paragraph meta.link.inet markup.underline.link
<ftp://test.com/>
| ^^^^^^^^^^^^^^ meta.paragraph meta.link.inet markup.underline.link

Visit www.commonmark.org/help for more information.
|     ^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                            ^^^^^^^^^^^^^^^^^^^^^^^ - markup.underline.link
Visit www.commonmark.org.
|     ^^^^^^^^^^^^^^^^^^ meta.paragraph markup.underline.link
|                       ^^ - markup.underline.link
Visit www.commonmark.org/a.b.
|     ^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph markup.underline.link
|                           ^ - markup.underline.link
www.google.com/search?q=(business))+ok
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                     ^ - markup.underline.link
www.google.com/search?q=Markup+(business)
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
www.commonmark.org/he<lp>
|^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                    ^ - markup.underline.link
http://commonmark.org
|^^^^^^^^^^^^^^^^^^^^ markup.underline.link
www.google.com/search?q=commonmark&hl=en
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                       ^ - markup.underline.link
www.google.com/search?q=commonmark&hl;
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                 ^^^^ constant.character.entity.named.html - markup.underline.link
(Visit https://encrypted.google.com/search?q=Markup+(business))
|      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                             ^^ - markup.underline.link
Anonymous FTP is available at ftp://foo.bar.baz.
|                             ^^^^^^^^^^^^^^^^^ markup.underline.link
|                                              ^^ - markup.underline.link
(see http://www.google.com/search?q=commonmark&hl=en)
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                   ^^ - markup.underline.link

foo@bar.baz
|^^^^^^^^^^ markup.underline.link
hello@mail+xyz.example isn't valid, but hello+xyz@mail.example is.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.underline.link
|                                       ^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
 a.b-c_d@a.b
|^^^^^^^^^^^ markup.underline.link
|           ^ - markup.underline.link
a.b-c_d@a.b.
|^^^^^^^^^^ markup.underline.link
|          ^^ - markup.underline.link
 a.b-c_d@a.b-
|^^^^^^^^^^^^^ - markup.underline.link
 a.b-c_d@a.b_
|^^^^^^^^^^^^^ - markup.underline.link
 test@test.test.me
|^^^^^^^^^^^^^^^^^ markup.underline.link

this is a raw ampersand & does not require HTML escaping
|                       ^ meta.other.valid-ampersand

this is a raw bracket < <= <- << does not require HTML escaping
|                     ^ meta.other.valid-bracket
|                       ^^ - meta.other-valid-bracket - meta.tag
|                          ^^ - meta.other-valid-bracket - meta.tag
|                             ^^ - meta.other-valid-bracket - meta.tag

[2]: https://github.com/sublimehq/Packages "Packages Repo"
| <- meta.link.reference.def
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def
|^ entity.name.reference.link
|  ^ punctuation.separator.key-value
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                          ^^^^^^^^^^^^^^^ string.other.link.description.title
|                                          ^ punctuation.definition.string.begin
|                                                        ^ punctuation.definition.string.end

[3]: https://github.com/sublimehq/Packages/issues/ 'Issues on Packages Repo'
| <- meta.link.reference.def
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def
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
| ^ meta.block-level markup.quote punctuation.definition.list_item
> - list item 2
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
| ^^^^^^^^^^^^^^ meta.block-level markup.quote markup.list.unnumbered
|   ^^^^^^^^^^^^ meta.paragraph.list
>   1. sub list item
| <- meta.block-level markup.quote punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^^^ meta.block-level markup.quote
|    ^ punctuation.definition.list_item
|   ^^ markup.list.numbered.bullet
| ^^^^^^^^^^^^^^^^^^^ markup.list.numbered
|      ^^^^^^^^^^^^^^ meta.paragraph.list

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
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
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
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
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
|                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                                           ^^^^^^^^^^^^^^^^^ string.other.link.description.title
|                                                           ^ punctuation.definition.string.begin
|                                                                           ^ punctuation.definition.string.end
|                                                                            ^ punctuation.definition.metadata

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

```js
| <- punctuation.definition.raw.code-fence.begin
|  ^^ constant.other.language-name
for (var i = 0; i < 10; i++) {
| ^ source.js keyword.control.loop
    console.log(i);
}
```
| <- punctuation.definition.raw.code-fence.end

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

https://github.github.com/gfm/#example-469
~Hi~ Hello, world!
| <- punctuation.definition.strikethrough.begin
|^^^ meta.paragraph markup.strikethrough
|  ^ punctuation.definition.strikethrough.end
|   ^^^^^^^^^^^^^^^ meta.paragraph - markup

https://github.github.com/gfm/#example-470
This ~text~~~~ is ~~~~curious~.
|    ^^^^^^^^^ meta.paragraph markup.strikethrough
|                 ^^^^^^^^^^^^ meta.paragraph markup.strikethrough
|                             ^^ meta.paragraph - markup
|    ^ punctuation.definition.strikethrough.begin
|         ^^^^ punctuation.definition.strikethrough.end
|                 ^^^^ punctuation.definition.strikethrough.begin
|                            ^ punctuation.definition.strikethrough.end

https://github.github.com/gfm/#example-471
This ~~has a
|    ^^^^^^^^ meta.paragraph markup.strikethrough

| <- meta.paragraph markup.strikethrough invalid.illegal.non-terminated.bold-italic
new paragraph~~.
|            ^^ meta.paragraph markup.strikethrough punctuation.definition.strikethrough.begin

| <- invalid.illegal.non-terminated.bold-italic

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
|                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image
|                                                                                     ^ punctuation.definition.metadata.end
|                                                                                       ^ punctuation.definition.metadata.begin
|                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                                                                                                                                          ^ punctuation.definition.metadata.end

[img-example]: http://www.sublimetext.com/anim/rename2_packed.png
|^^^^^^^^^^^ meta.link.reference.def entity.name.reference.link
|            ^ punctuation.separator.key-value
|              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link

[//]: # (This is a comment without a line-break.)
|     ^ meta.link.reference.def markup.underline.link
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.other.link.description.title

[//]: # (This is a comment with a
|     ^ meta.link.reference.def markup.underline.link
|       ^ punctuation.definition.string.begin
        line-break.)
|                  ^ punctuation.definition.string.end

[//]: # (testing)blah
|       ^ punctuation.definition.string.begin
|^^^^^^^^^^^^^^^^ meta.link.reference.def
|               ^ punctuation.definition.string.end
|                ^^^^ invalid.illegal.expected-eol

[//]: # (testing
blah
| <- meta.link.reference.def string.other.link.description.title

| <- invalid.illegal.non-terminated.link-title
text
| <- meta.paragraph - meta.link.reference.def

[foo]: <bar> "test"
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|            ^^^^^^ string.other.link.description.title

[foo]: <bar>> "test"
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|           ^^^^^^^^ invalid.illegal.expected-eol

https://michelf.ca/projects/php-markdown/extra/#footnotes
That's some text with a footnote.[^1]
|                                ^^^^ meta.paragraph meta.link.reference.footnote.markdown-extra
|                                ^^ punctuation.definition.link.begin
|                                  ^ meta.link.reference.literal.footnote-id
|                                   ^ punctuation.definition.link.end

 [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
|^ punctuation.definition.constant.begin
|   ^ punctuation.definition.constant.end
| ^^ entity.name.reference.link
|    ^ punctuation.separator.key-value

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
|^^^^^^^^^^^^^ meta.block-level meta.table.header
| <- punctuation.separator.table-cell
|     ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
| ^^^^ - punctuation.separator.table-cell
| --- | --- |
| baz | bim <kbd>Ctrl+C</kbd> |
| <- meta.block-level meta.table punctuation.separator.table-cell
|           ^^^^^ meta.tag.inline.any
|                             ^ punctuation.separator.table-cell

| <- - meta.block-level - meta.table

| abc | defghi |
:-: | -----------:
|^^^^^^^^^^^^^^^^^ meta.block-level meta.table.header-separator
| <- punctuation.definition.table-cell-alignment
|^ punctuation.section.table-header
|   ^ punctuation.separator.table-cell
|     ^^^^^^^^^^^ punctuation.section.table-header
|                ^ punctuation.definition.table-cell-alignment - punctuation.section.table-header
bar | baz
|   ^ meta.block-level meta.table punctuation.separator.table-cell

| f\|oo  |
| <- meta.block-level meta.table punctuation.separator.table-cell
|  ^^ meta.block-level meta.table constant.character.escape - punctuation.separator.table-cell
|        ^ meta.block-level meta.table punctuation.separator.table-cell
| ------ |
| b `|` az |
|   ^^^ meta.block-level meta.table markup.raw.inline - meta.table.header-separator
|          ^ meta.block-level meta.table punctuation.separator.table-cell
| b **|** im |
| <- meta.block-level meta.table punctuation.separator.table-cell
|   ^^^^^ meta.block-level meta.table markup.bold - punctuation.separator.table-cell
|            ^ meta.block-level meta.table punctuation.separator.table-cell

| abc | def |
| --- | --- |
| bar | baz |
|^^^^^^^^^^^^^ meta.block-level meta.table
test
|^^^^ meta.block-level meta.table
> bar
| <- meta.block-level markup.quote punctuation.definition.blockquote - meta.table

`|` this `|` example `|` is not a table `|`
| ^ punctuation.definition.raw.end - meta.table
| nor is this | because it is not at block level, it immediately follows a paragraph |
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - meta.table

| First Header  | Second Header | Third Header         |
| :------------ | :-----------: | -------------------: |
| First row     | Data          | Very long data entry |
| Second row    | **Cell**      | *Cell*               |
| Third row     | Cell that spans across two columns  ||
| ^^^^^^^^^^^^^^ meta.block-level meta.table
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
| ^^^^ meta.block-level meta.table - meta.table.header

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
| ^^^^^^^ meta.disable-markdown meta.tag.sgml.doctype.html keyword.declaration.doctype.html
okay
| <- - meta.disable-markdown

http://spec.commonmark.org/0.28/#example-149

<![CDATA[
| ^^^^^^^^ meta.disable-markdown meta.tag.sgml.cdata.html
function matchwo(a,b)
{
  if (a < b && a < 0) then {
    return 1;

  } else {

    return 0;
  }
}
]]>
|^ meta.disable-markdown meta.tag.sgml.cdata.html
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
|   ^^^^ keyword.control.flow.pass.python
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
|^^^ meta.paragraph meta.code-fence.definition.end.regexp - markup
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
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta - constant - keyword - variable - punctuation

    -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.block-level markup.raw - constant - keyword - variable - punctuation

>  -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.block-level - constant - keyword - variable

> > -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^ meta.block-level.markdown markup.quote.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.block-level - constant - keyword - variable
