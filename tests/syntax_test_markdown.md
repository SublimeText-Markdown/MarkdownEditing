| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"

# TEST: Tabs ##################################################################

## https://spec.commonmark.org/0.30/#example-1

	foo	baz		bim
| <- markup.raw.block.markdown
|^^^^^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-2

  	foo	baz		bim
| <- markup.raw.block.markdown
|^^^^^^^^^^^^^ markup.raw.block.markdown

   	foo	baz		bim
| <- markup.raw.block.markdown
|^^^^^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-3

    a	a
    ὐ	a
| <- markup.raw.block.markdown
|^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-4

  - foo

	bar
| <- markup.list.unnumbered.markdown
|^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-5

- foo

		bar
| <- markup.list.unnumbered.markdown - markup.raw.block.markdown
|^^^^^ markup.list.unnumbered.markdown - markup.raw.block.markdown

> Note: `bar` should be indented code block, but ST can't reliably highlight it!

## https://spec.commonmark.org/0.30/#example-6

>		foo
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^^ markup.quote.markdown markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-7

-		foo
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown


## https://spec.commonmark.org/0.30/#example-8

    foo
	bar
| <- markup.raw.block.markdown
|^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-9

 - foo
   - bar
	 - baz
|^ markup.list.unnumbered.markdown
| ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|   ^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-10

#	Foo
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^ markup.heading.1.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-11

*	*	*	
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^ meta.separator.thematic-break.markdown
| ^ punctuation.definition.thematic-break.markdown
|   ^ punctuation.definition.thematic-break.markdown

-	-	-	
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^ meta.separator.thematic-break.markdown
| ^ punctuation.definition.thematic-break.markdown
|   ^ punctuation.definition.thematic-break.markdown

_	_	_	
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^ meta.separator.thematic-break.markdown
| ^ punctuation.definition.thematic-break.markdown
|   ^ punctuation.definition.thematic-break.markdown


# TEST: LIGATURES #############################################################

this is a raw ampersand & does not require HTML escaping
|                       ^ - entity - illegal

this is a raw bracket < > does not require HTML escaping
|                     ^^^ - meta.tag - punctuation

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

-= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  - constant - keyword - variable

    -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
|   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw - constant - keyword - variable - punctuation

>  -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable

> > -= += /= %= -- ++ ** !~ =~ ~~ <= >= => <=> // && == !=
| ^ markup.quote.markdown punctuation.definition.blockquote.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - constant - keyword - variable


# TEST: BACKSLASH ESCAPES #####################################################

## https://spec.commonmark.org/0.30/#example-12

\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~
| <- constant.character.escape.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ constant.character.escape.markdown

## https://spec.commonmark.org/0.30/#example-13

\	\A\a\ \3\φ\«
| <- - constant.character.escape
|^^^^^^^^^^^^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-14

\*not emphasized*
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^^^^^^^^ - markup.italic

\<br/> not a tag
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^ - markup.tag

\<br/\> not a tag
| <- constant.character.escape.markdown
|^^^^^^ - meta.tag
|    ^^ constant.character.escape

\[not a link](/foo)
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^^^^^^^^^^ - markup.link

\`not code`
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^ - markup.raw

1\. not a list
|^^ constant.character.escape.markdown
|^^^^^^^^^^^^^ - markup.list

\* not a list
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^^^^ - markup.list

\# not a heading
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^^^^^^^ - markup.heading

\[foo]: /url "not a reference"
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.link

\&ouml; not a character entity
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
|^^^^^^ - entity

\~/.bashrc
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown

## https://spec.commonmark.org/0.30/#example-15

\\*emphasis*
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
| ^^^^^^^^^^ markup.italic.markdown

\\_emphasis_
| <- constant.character.escape.markdown
|^ constant.character.escape.markdown
| ^^^^^^^^^^ markup.italic.markdown

## https://spec.commonmark.org/0.30/#example-16

foo\
|  ^ meta.hard-line-break.markdown constant.character.escape.markdown
|   ^ meta.hard-line-break.markdown - constant
bar

## https://spec.commonmark.org/0.30/#example-17

`` \[\` ``
|^^^^^^^^^ markup.raw.inline.markdown - constant.character.escape

## https://spec.commonmark.org/0.30/#example-18

    \[\]
|^^^^^^^^ markup.raw.block.markdown - constant.character.escape

## https://spec.commonmark.org/0.30/#example-19

~~~
\[\]
|^^^^ markup.raw.code-fence.markdown-gfm - constant.character.escape
~~~

## https://spec.commonmark.org/0.30/#example-20

<http://example.com?find=\*>
|                        ^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-21

<a href="/bar\/)">
|            ^^ - constant.character.escape

## https://spec.commonmark.org/0.30/#example-22

[foo](/bar\* "ti\*tle")
|         ^^ markup.underline.link.markdown constant.character.escape
|               ^^ constant.character.escape

## https://spec.commonmark.org/0.30/#example-23

[foo]

[foo]: /bar\* "ti\*tle"
|          ^^ markup.underline.link.markdown constant.character.escape
|                ^^ constant.character.escape

## https://spec.commonmark.org/0.30/#example-24

Note: current design doesn't support highlighting escapes in info strings
``` foo\+bar
|      ^^ - constant.character.escape
foo
```


# TEST: HTML ENTITIES #########################################################

## https://spec.commonmark.org/0.30/#example-25

  &nbsp; &amp; &copy; &AElig; &Dcaron;
| ^^^^^^ constant.character.entity.named.html
|       ^ - constant
|        ^^^^^ constant.character.entity.named.html
|             ^ - constant
|              ^^^^^^ constant.character.entity.named.html
|                    ^ - constant
|                     ^^^^^^^ constant.character.entity.named.html
|                            ^ - constant
|                             ^^^^^^^^ constant.character.entity.named.html
|                                     ^ - constant
  
  &frac34; &HilbertSpace; &DifferentialD;
| ^^^^^^^^ constant.character.entity.named.html
|         ^ - constant
|          ^^^^^^^^^^^^^^ constant.character.entity.named.html
|                        ^ - constant
|                         ^^^^^^^^^^^^^^^ constant.character.entity.named.html
|                                        ^ - constant

  &ClockwiseContourIntegral; &ngE;
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ constant.character.entity.named.html
|                           ^ - constant
|                            ^^^^^ constant.character.entity.named.html
|                                 ^ - constant

## https://spec.commonmark.org/0.30/#example-26

  &#35; &#1234; &#992; &#0;
| ^^^^^ constant.character.entity.decimal.html
|      ^ - constant
|       ^^^^^^^ constant.character.entity.decimal.html
|              ^ - constant
|               ^^^^^^ constant.character.entity.decimal.html
|                     ^ - constant
|                      ^^^^ constant.character.entity.decimal.html
|                          ^ - constant

## https://spec.commonmark.org/0.30/#example-27

  &#X22; &#XD06; &#xcab;
| ^^^^^^ constant.character.entity.hexadecimal.html
|       ^ - constant
|        ^^^^^^^ constant.character.entity.hexadecimal.html
|               ^ - constant
|                ^^^^^^^ constant.character.entity.hexadecimal.html
|                       ^ - constant

## https://spec.commonmark.org/0.30/#example-28

  &
| ^ - constant - invalid

  &nbsp &x; &#; &#x;
| ^^^^^^ - constant
|       ^^^ constant.character.entity.named.html
|          ^^^^^^^^^ - constant

  &#87654321;

  &#abcdef0;
| ^^^^^^^^^^ - constant

  &hi?;
| ^^^^^ - constant

Note: ST's HTML or Markdown don't maintain a full list of valid html5 entities
      for simplicity reasons and therefore invalid entities are highlighted.

## https://spec.commonmark.org/0.30/#example-29

Although HTML5 does accept some entity references without a trailing semicolon
(such as &copy), these are not recognized here, because it makes the grammar
too ambiguous:

  &copy
| ^^^^^ - constant

## https://spec.commonmark.org/0.30/#example-30

Strings that are not on the list of HTML5 named entities are not recognized as
entity references either:

  &MadeUpEntity;
| ^^^^^^^^^^^^^^ constant.character.entity.named.html

Note: ST's HTML or Markdown don't maintain a full list of valid html5 entities
      for simplicity reasons and therefore invalid entities are highlighted.

## https://spec.commonmark.org/0.30/#example-31

<a href="&ouml;&ouml;.html">
|        ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-32

[foo](/f&ouml;&ouml; "f&ouml;&ouml;")
|       ^^^^^^^^^^^^ constant.character.entity.named.html
|                      ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-33

[foo]

[foo]: /f&ouml;&ouml; "f&ouml;&ouml;"
|        ^^^^^^^^^^^^ constant.character.entity.named.html
|                       ^^^^^^^^^^^^ constant.character.entity.named.html

## https://spec.commonmark.org/0.30/#example-34

``` f&ouml;&ouml;
foo
```
Note: current design doesn't support highlighting entities in info strings

## https://spec.commonmark.org/0.30/#example-35

`f&ouml;&ouml;`
|^^^^^^^^^^^^^ - constant.character.entity

## https://spec.commonmark.org/0.30/#example-36

    f&ouml;f&ouml;
|   ^^^^^^^^^^^^^^ - constant.character.entity

## https://spec.commonmark.org/0.30/#example-37

&#42;foo&#42;
| <- meta.paragraph.markdown constant.character.entity.decimal.html
|^^^^^^^^^^^^^ meta.paragraph.markdown - markup.italic
|^^^^ constant.character.entity.decimal.html
|       ^^^^^ constant.character.entity.decimal.html

*foo*
| <- meta.paragraph.markdown markup.italic.markdown
|^^^^ meta.paragraph.markdown markup.italic.markdown

## https://spec.commonmark.org/0.30/#example-38

&#42; foo
| <- meta.paragraph.markdown constant.character.entity.decimal.html
|^^^^^^^^^ meta.paragraph.markdown
|^^^^ constant.character.entity.decimal.html

* foo
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-39

foo&#10;&#10;bar
| <- meta.paragraph.markdown
|^^^^^^^^^^^^^^^^ meta.paragraph.markdown
|  ^^^^^^^^^^ constant.character.entity.decimal.html

## https://spec.commonmark.org/0.30/#example-40

&#9;foo
| <- meta.paragraph.markdown constant.character.entity.decimal.html
|^^^ meta.paragraph.markdown constant.character.entity.decimal.html
|   ^^^^ meta.paragraph.markdown - constant

## https://spec.commonmark.org/0.30/#example-41

[a](url &quot;tit&quot;)
|       ^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - meta.link
|       ^^^^^^ constant.character.entity.named.html
|             ^^^ - constant
|                ^^^^^^ constant.character.entity.named.html


# TEST: THEMATIC BREAKS #######################################################

## https://spec.commonmark.org/0.30/#example-43

***
|^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown

---
|^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown

___
|^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown

## https://spec.commonmark.org/0.30/#example-44

+++
| <- - meta.separator
|^^^ - meta.separator

## https://spec.commonmark.org/0.30/#example-45

===
| <- - meta.separator
|^^^ - meta.separator

## https://spec.commonmark.org/0.30/#example-46

**
| <- - meta.separator
|^ - meta.separator

--
| <- - meta.separator
|^ - meta.separator

__
| <- - meta.separator
|^ - meta.separator

## https://spec.commonmark.org/0.30/#example-47

 ***
|<- meta.separator.thematic-break.markdown - punctuation
|^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

  ***
|<- meta.separator.thematic-break.markdown - punctuation
|^ meta.separator.thematic-break.markdown - punctuation
| ^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

   ***
|<- meta.separator.thematic-break.markdown - punctuation
|^^ meta.separator.thematic-break.markdown - punctuation
|  ^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

## https://spec.commonmark.org/0.30/#example-48

    ***
|<- markup.raw.block.markdown
|^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-49

Foo
    ***
| <- meta.paragraph.markdown
|^^^^^^^ meta.paragraph.markdown

## https://spec.commonmark.org/0.30/#example-50

**************************************
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

--------------------------------------
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

_____________________________________
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

## https://spec.commonmark.org/0.30/#example-51

 * * *
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown
|^ punctuation.definition.thematic-break.markdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation

 - - -
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown
|^ punctuation.definition.thematic-break.markdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation

 _ _ _
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^ meta.separator.thematic-break.markdown
|^ punctuation.definition.thematic-break.markdown
| ^ - punctuation
|  ^ punctuation.definition.thematic-break.markdown
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation

## https://spec.commonmark.org/0.30/#example-52

 **  * ** * ** * **
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown
|                  ^ - punctuation

 --  - -- - -- - --
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown
|                  ^ - punctuation

 __  _ __ _ __ _ __
| <- meta.separator.thematic-break.markdown - punctuation
|^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^ punctuation.definition.thematic-break.markdown
|  ^^ - punctuation
|    ^ punctuation.definition.thematic-break.markdown
|     ^ - punctuation
|      ^^ punctuation.definition.thematic-break.markdown
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break.markdown
|          ^ - punctuation
|           ^^ punctuation.definition.thematic-break.markdown
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break.markdown
|               ^ - punctuation
|                ^^ punctuation.definition.thematic-break.markdown
|                  ^ - punctuation

## https://spec.commonmark.org/0.30/#example-53

*     *      *      *
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown 
|                    ^ - punctuation

-     -      -      -
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown 
|                    ^ - punctuation

_     _      _      _
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|^^^^^ - punctuation
|     ^ punctuation.definition.thematic-break.markdown 
|      ^^^^^^ - punctuation
|            ^ punctuation.definition.thematic-break.markdown 
|             ^^^^^^ - punctuation
|                   ^ punctuation.definition.thematic-break.markdown 
|                    ^ - punctuation

## https://spec.commonmark.org/0.30/#example-54

* * * *
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^ meta.separator.thematic-break.markdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

- - - -
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^ meta.separator.thematic-break.markdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

_ _ _ _
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^^^ meta.separator.thematic-break.markdown
|^ - punctuation
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation

## https://spec.commonmark.org/0.30/#example-55

_ _ _ _ a
| <- meta.paragraph.markdown - meta.separator
|^^^^^^^^^ meta.paragraph.markdown - meta.separator

a------
| <- meta.paragraph.markdown - meta.separator
|^^^^^^^ meta.paragraph.markdown - meta.separator

---a---
| <- meta.paragraph.markdown - meta.separator
|^^^^^^^ meta.paragraph.markdown - meta.separator

## https://spec.commonmark.org/0.30/#example-56

 *-*
| <- meta.paragraph.markdown - meta.separator
|^^^ meta.paragraph.markdown - meta.separator

## https://spec.commonmark.org/0.30/#example-57

- foo
***
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
- bar
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

## https://spec.commonmark.org/0.30/#example-58

Foo
***
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
bar
| <- meta.paragraph.markdown

## https://spec.commonmark.org/0.30/#example-59

Foo
---
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
bar
| <- meta.paragraph.markdown

## https://spec.commonmark.org/0.30/#example-60

* Foo
* * *
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^^^ meta.separator.thematic-break.markdown
| ^ punctuation.definition.thematic-break.markdown
|   ^ punctuation.definition.thematic-break.markdown
* Bar
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

## https://spec.commonmark.org/0.30/#example-61

- Foo
- * * *
| ^^^^^^ markup.list.unnumbered.markdown meta.separator.thematic-break.markdown


# TEST: ATX HEADINGS ##########################################################

## https://spec.commonmark.org/0.30/#example-62

# foo
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^ markup.heading.1.markdown - punctuation

## foo
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown
|^ markup.heading.2.markdown punctuation.definition.heading.begin.markdown
| ^^^^^ markup.heading.2.markdown - punctuation

### foo
| <- markup.heading.3.markdown punctuation.definition.heading.begin.markdown
|^^ markup.heading.3.markdown punctuation.definition.heading.begin.markdown
|  ^^^^^ markup.heading.3.markdown - punctuation

#### foo
| <- markup.heading.4.markdown punctuation.definition.heading.begin.markdown
|^^^ markup.heading.4.markdown punctuation.definition.heading.begin.markdown
|   ^^^^^ markup.heading.4.markdown - punctuation

##### foo
| <- markup.heading.5.markdown punctuation.definition.heading.begin.markdown
|^^^^ markup.heading.5.markdown punctuation.definition.heading.begin.markdown
|    ^^^^^ markup.heading.5.markdown - punctuation

###### foo
| <- markup.heading.6.markdown punctuation.definition.heading.begin.markdown
|^^^^^ markup.heading.6.markdown punctuation.definition.heading.begin.markdown
|     ^^^^^ markup.heading.6.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-63

####### foo
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^^^^^ meta.paragraph.markdown - markup.heading

## https://spec.commonmark.org/0.30/#example-64

#5 bolt
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^ meta.paragraph.markdown - markup.heading

#hashtag
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^^ meta.paragraph.markdown - markup.heading

## https://spec.commonmark.org/0.30/#example-65

\## foo
| <- meta.paragraph.markdown constant.character.escape.markdown - markup
|^ meta.paragraph.markdown constant.character.escape.markdown - markup
| ^^^^^^ meta.paragraph.markdown - constant - markup

## https://spec.commonmark.org/0.30/#example-66

# foo *bar* \*baz\*
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^ markup.heading.1.markdown - entity.name - markup.italic
| ^^^^ markup.heading.1.markdown entity.name.section.markdown - markup.italic
|     ^^^^^ markup.heading.1.markdown entity.name.section.markdown markup.italic.markdown
|          ^^^^^^^^ markup.heading.1.markdown entity.name.section.markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-67

#                  foo                     
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown - entity.name
|                  ^^^ markup.heading.1.markdown entity.name.section.markdown
|                     ^^^^^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown - entity.name

## https://spec.commonmark.org/0.30/#example-68

 ### foo
| <- markup.heading.3.markdown
|^^^^^^^^ markup.heading.3.markdown 
  ## foo
| <- markup.heading.2.markdown
|^^^^^^^^ markup.heading.2.markdown  
   # foo
| <- markup.heading.1.markdown
|^^^^^^^^ markup.heading.1.markdown   

## https://spec.commonmark.org/0.30/#example-69

    # foo
| <- markup.raw.block.markdown
|^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-70

foo
    # bar
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^^^ meta.paragraph.markdown - markup.heading

## https://spec.commonmark.org/0.30/#example-71

## foo ##
  ###   bar    ###
| <- markup.heading.3.markdown
|^^^^^^^^^^^^^^^^^^ markup.heading.3.markdown
| ^^^ punctuation.definition.heading.begin.markdown
|    ^^^ - entity - punctuation 
|       ^^^ entity.name.section.markdown
|          ^^^^ - entity - punctuation 
|              ^^^ punctuation.definition.heading.end.markdown
|                 ^ - punctuation 

## https://spec.commonmark.org/0.30/#example-72

# foo ##################################
##### foo ##
| <- markup.heading.5.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^ markup.heading.5.markdown
|^^^^ punctuation.definition.heading.begin.markdown
|    ^ - entity - punctuation 
|     ^^^ entity.name.section.markdown
|        ^ - entity - punctuation 
|         ^^ punctuation.definition.heading.end.markdown
|           ^ - punctuation 

## https://spec.commonmark.org/0.30/#example-73

### foo ###     
| <- markup.heading.3.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^^^^ markup.heading.3.markdown
|^^ punctuation.definition.heading.begin.markdown
|  ^ - entity - punctuation 
|   ^^^ entity.name.section.markdown
|      ^ - entity - punctuation 
|       ^^^ punctuation.definition.heading.end.markdown
|          ^^^^^^ - punctuation 

## https://spec.commonmark.org/0.30/#example-74

### foo ### b
| <- markup.heading.3.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^ markup.heading.3.markdown
|^^ punctuation.definition.heading.begin.markdown
|  ^ - entity - punctuation 
|   ^^^^^^^^^ entity.name.section.markdown
|            ^ - entity

## https://spec.commonmark.org/0.30/#example-75

# foo#
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^ markup.heading.1.markdown
|^ - entity - punctuation 
| ^^^^ entity.name.section.markdown
|     ^ - entity

# foo# #
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^ markup.heading.1.markdown
|^ - entity - punctuation 
| ^^^^ entity.name.section.markdown
|     ^ - entity - punctuation 
|      ^ punctuation.definition.heading.end.markdown
|       ^ - punctuation

## https://spec.commonmark.org/0.30/#example-76

### foo \###
| <- markup.heading.3.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^ markup.heading.3.markdown
|^^ punctuation.definition.heading.begin.markdown
|   ^^^^^^^^ entity.name.section.markdown
|       ^^ constant.character.escape.markdown
|           ^ - constant - entity - punctuation

## foo #\##
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^ markup.heading.2.markdown
|^ punctuation.definition.heading.begin.markdown
|  ^^^^^^^^ entity.name.section.markdown
|       ^^ constant.character.escape.markdown
|          ^ - constant - entity - punctuation

# foo \#
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^ markup.heading.1.markdown
| ^^^^^^ entity.name.section.markdown
|     ^^ constant.character.escape.markdown
|       ^ - constant - entity - punctuation

## https://spec.commonmark.org/0.30/#example-77

****
## foo
| <- markup.heading.2.markdown punctuation.definition.heading.begin.markdown
|^^^^^^ markup.heading.2.markdown

****
## foo
****
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

## https://spec.commonmark.org/0.30/#example-78

Foo bar
# baz
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^ markup.heading.1.markdown

Foo bar
# baz
Bar foo
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^ meta.paragraph.markdown - markup.heading

Foo **bar
# baz
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.bold
|^^^^^ markup.heading.1.markdown
this must not be bold**
| <- - meta.bold
|^^^^^^^^^^^^^^^^^^^^^^ - meta.bold

Foo *bar
# baz
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.italic
|^^^^ markup.heading.1.markdown
this must not be italic*
| <- - meta.italic
|^^^^^^^^^^^^^^^^^^^^^^^ - meta.italic

Foo ***bar
# baz
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.bold - markup.italic
|^^^^^ markup.heading.1.markdown
this must not be bold italic***
| <- - meta.bold - markup.italic
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - meta.bold - markup.italic

## https://spec.commonmark.org/0.30/#example-79

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


# TEST: SETEXT HEADINGS #######################################################

SETEXT Heading Level 1
| <- markup.heading.1.markdown entity.name.section.markdown
=================
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|                ^ markup.heading.1.markdown meta.whitespace.newline.markdown

SETEXT Heading Level 2
| <- markup.heading.2.markdown entity.name.section.markdown
------------------------------
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|                             ^ markup.heading.2.markdown meta.whitespace.newline.markdown - punctuation

underlined heading followed by a separator
-------------------
------
| <- meta.separator.thematic-break.markdown - markup.heading

underlined heading followed by another one that should be treated as a normal paragraph
==================
=====
| <- meta.paragraph.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-80

Foo *bar*
| <- markup.heading.1.markdown entity.name.section.markdown
|^^^^^^^^^ markup.heading.1.markdown entity.name.section.markdown
|   ^^^^^ markup.italic.markdown
=========
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|^^^^^^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|        ^ markup.heading.1.markdown meta.whitespace.newline.markdown

Foo *bar*
| <- markup.heading.2.markdown entity.name.section.markdown
|^^^^^^^^^ markup.heading.2.markdown entity.name.section.markdown
|   ^^^^^ markup.italic.markdown
---------
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^^^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|        ^ markup.heading.2.markdown meta.whitespace.newline.markdown

Foo *bar
| <- markup.heading.1.markdown entity.name.section.markdown
|^^^^^^^^^ markup.heading.1.markdown entity.name.section.markdown
|   ^^^^^ markup.italic.markdown
=========
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown - markup.italic
|^^^^^^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown - markup.italic
|        ^ markup.heading.1.markdown meta.whitespace.newline.markdown - markup.italic

Foo *bar
| <- markup.heading.2.markdown entity.name.section.markdown
|^^^^^^^^^ markup.heading.2.markdown entity.name.section.markdown
|   ^^^^^ markup.italic.markdown
---------
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown - markup.italic
|^^^^^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown - markup.italic
|        ^ markup.heading.2.markdown meta.whitespace.newline.markdown - markup.italic

https://spec.commonmark.org/0.30/#example-81

Foo *bar
baz*
| <- markup.heading.1.markdown entity.name.section.markdown markup.italic.markdown
|^^^ markup.heading.1.markdown entity.name.section.markdown markup.italic.markdown
|   ^ markup.heading.1.markdown entity.name.section.markdown - markup.italic
====
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|   ^ markup.heading.1.markdown meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-82

  Foo *bar
baz*  
| <- markup.heading.1.markdown entity.name.section.markdown markup.italic.markdown
|^^^ markup.heading.1.markdown entity.name.section.markdown markup.italic.markdown
|   ^^ markup.heading.1.markdown entity.name.section.markdown - markup.italic
====
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|   ^ markup.heading.1.markdown meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-83

Foo
=
| <- markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|^ markup.heading.1.markdown meta.whitespace.newline.markdown

Foo
-
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^ markup.heading.2.markdown meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-84

   Foo
---
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|  ^ markup.heading.2.markdown meta.whitespace.newline.markdown

  Foo
-----
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|    ^ markup.heading.2.markdown meta.whitespace.newline.markdown

  Foo
  ===
| <- markup.heading.1.markdown - punctuation
|^ markup.heading.1.markdown - punctuation
| ^^^ markup.heading.1.markdown punctuation.definition.heading.setext.markdown
|    ^ markup.heading.1.markdown meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-85

    Foo
    ---
|^^^^^^^ markup.raw.block.markdown

    Foo
---
| <- meta.separator.thematic-break.markdown - markup.heading
|^^^ meta.separator.thematic-break.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-86

Foo
   ----      
|^^^^^^^^^^^^^ markup.heading.2.markdown
|^^ - punctuation
|  ^^^^ punctuation.definition.heading.setext.markdown
|      ^^^^^^^ - punctuation
|            ^ meta.whitespace.newline.markdown

https://spec.commonmark.org/0.30/#example-87

Foo
    ---
| <- meta.paragraph.markdown - markup.heading
|^^^^^^^ meta.paragraph.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-88

Foo
= =
| <- meta.paragraph.markdown - markup.heading
|^^^ meta.paragraph.markdown - markup.heading

Foo
--- -
| <- meta.separator.thematic-break.markdown - markup.heading
|^^^^^ meta.separator.thematic-break.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-89

Foo  
|  ^^ markup.heading.2.markdown entity.name.section.markdown - meta.hard-line-break
-----
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

https://spec.commonmark.org/0.30/#example-90

Foo\
|  ^ markup.heading.2.markdown entity.name.section.markdown - meta.hard-line-break
----
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

https://spec.commonmark.org/0.30/#example-91

`Foo
----
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

`Foo`
----
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

https://spec.commonmark.org/0.30/#example-92

> Foo
---
| <- meta.separator.thematic-break.markdown - markup.heading
|^^^ meta.separator.thematic-break.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-93

> foo
bar
===
| <- markup.quote.markdown - markup.heading
|^^^ markup.quote.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-94
- Foo
---
| <- meta.separator.thematic-break.markdown - markup.heading
|^^^ meta.separator.thematic-break.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-95

Foo
Bar
---
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

https://spec.commonmark.org/0.30/#example-96

---
Foo
---
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

---
Foo
---
Bar
---
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown
Baz

---
Foo
---
Bar
---
Baz
| <- meta.paragraph.markdown
|^^^ meta.paragraph.markdown

https://spec.commonmark.org/0.30/#example-97

====
| <- meta.paragraph.markdown
|^^^^ meta.paragraph.markdown

https://spec.commonmark.org/0.30/#example-98

---
---
| <- meta.separator.thematic-break.markdown - markup.heading
|^^^ meta.separator.thematic-break.markdown - markup.heading

https://spec.commonmark.org/0.30/#example-102

\> foo
------
| <- markup.heading.2.markdown punctuation.definition.heading.setext.markdown
|^^^^^ markup.heading.2.markdown punctuation.definition.heading.setext.markdown

```
Fenced codeblocks are no no setext heading
```
---
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown


# TEST: INDENTED CODE BLOCKS ##################################################

Code block below:

    this is code!
| ^^^^^^^^^^^^^^^^ markup.raw.block

    more code
    spanning multiple lines
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block

paragraph
| <- meta.paragraph


# TEST: FENCED CODE BLOCKS ####################################################

## https://spec.commonmark.org/0.30/#example-119

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
<
| <- markup.raw.code-fence.markdown-gfm - punctuation
 >
|^^ markup.raw.code-fence.markdown-gfm - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-120

~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
<
| <- markup.raw.code-fence.markdown-gfm - punctuation
 >
|^^ markup.raw.code-fence.markdown-gfm - punctuation
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-121

``
foo
``
| <- - meta.code-fence - punctuation.definition.raw.code-fence
|^ - meta.code-fence - punctuation.definition.raw.code-fence

## https://spec.commonmark.org/0.30/#example-122

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
~~~
| <- markup.raw.code-fence.markdown-gfm - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-123

~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
```
| <- markup.raw.code-fence.markdown-gfm - punctuation
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

~~~~ 
| <- punctuation.definition.raw.code-fence.begin
 ~~~~
| ^^^ punctuation.definition.raw.code-fence.end

## https://spec.commonmark.org/0.30/#example-124

````
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|   ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
```
| <- markup.raw.code-fence.markdown-gfm - punctuation
``````
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-125

~~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|   ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
|
aaa
~~~
| <- markup.raw.code-fence.markdown-gfm - punctuation
~~~~
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|   ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-128

> ```
> aaa
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - markup.raw
| ^^^^ markup.quote.markdown markup.raw.code-fence.markdown-gfm

bbb
| <- meta.paragraph.markdown - markup.raw

## https://spec.commonmark.org/0.30/#example-129

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation

  
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-130

```
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-131

 ```
 aaa
aaa
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-132

  ```
aaa
  aaa
aaa
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-133

   ```
   aaa
    aaa
  aaa
   ```
| <- meta.code-fence.definition.end.text.markdown-gfm - punctuation
|^^ meta.code-fence.definition.end.text.markdown-gfm - punctuation
|  ^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-134

    ```
    aaa
    ```
| <- markup.raw.block.markdown
|^^^^^^^ markup.raw.block.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-135

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-136

   ```
| <- meta.code-fence.definition.begin.text.markdown-gfm - punctuation
|^^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
|  ^^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|     ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm
  ```
| <- meta.code-fence.definition.end.text.markdown-gfm - punctuation
|^ meta.code-fence.definition.end.text.markdown-gfm - punctuation
| ^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|    ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-137

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
aaa
| <- markup.raw.code-fence.markdown-gfm
    ```
| <- meta.code-fence.definition.end.text.markdown-gfm - punctuation
|^^^ meta.code-fence.definition.end.text.markdown-gfm - punctuation
|   ^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|      ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-138

``` ```
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^ markup.raw.inline.markdown

``` ```
aaa
| <- meta.paragraph.markdown - meta.code-fence - markup
|^^ meta.paragraph.markdown - meta.code-fence - markup

## https://spec.commonmark.org/0.30/#example-139

~~~~~~
aaa
~~~ ~~
| <- markup.raw.code-fence.markdown-gfm - punctuation
|^^^^^^ markup.raw.code-fence.markdown-gfm - punctuation

~~~~~~
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|     ^ meta.code-fence.definition.end.text.markdown-gfm - punctuation

## https://spec.commonmark.org/0.30/#example-140

foo
```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
bar
```
baz
| <- meta.paragraph.markdown - meta.code-fence - markup
|^^ meta.paragraph.markdown - meta.code-fence - markup

## https://spec.commonmark.org/0.30/#example-140-including-emphasis-termination

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

## https://spec.commonmark.org/0.30/#example-141

foo
---
~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
bar
|^^^ markup.raw.code-fence.markdown-gfm
~~~
# baz
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^ markup.heading.1.markdown

## https://spec.commonmark.org/0.30/#example-142

```ruby
| <- meta.code-fence.definition.begin.ruby.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.ruby.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|  ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm constant.other.language-name.markdown
|      ^ meta.code-fence.definition.begin.ruby.markdown-gfm - constant
def foo(x)
| <- markup.raw.code-fence.ruby.markdown-gfm source.ruby meta.function
  return 3
end
| <- markup.raw.code-fence.ruby.markdown-gfm source.ruby keyword
```
| <- meta.code-fence.definition.end.ruby.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.ruby.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://spec.commonmark.org/0.30/#example-143

~~~~    ruby startline=3 $%@#$
| <- meta.code-fence.definition.begin.ruby.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^^ meta.code-fence.definition.begin.ruby.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|   ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm - punctuation - constant
|       ^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm constant.other.language-name.markdown
|           ^^^^^^^^^^^^^^^^^^^ meta.code-fence.definition.begin.ruby.markdown-gfm - constant
def foo(x)
| <- markup.raw.code-fence.ruby.markdown-gfm source.ruby meta.function
  return 3
end
| <- markup.raw.code-fence.ruby.markdown-gfm source.ruby keyword
~~~~~~~
| <- meta.code-fence.definition.end.ruby.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^^^^^ meta.code-fence.definition.end.ruby.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://spec.commonmark.org/0.30/#example-144

````;
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|   ^^ meta.code-fence.definition.begin.text.markdown-gfm
````
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://spec.commonmark.org/0.30/#example-145

``` aa ```
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^^^^ meta.paragraph.markdown markup.raw.inline.markdown
|^^ punctuation.definition.raw.begin.markdown
|      ^^^ punctuation.definition.raw.end.markdown
foo
| <- meta.paragraph.markdown - markup

## https://spec.commonmark.org/0.30/#example-146

~~~ aa ``` ~~~
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|   ^^ meta.code-fence.definition.begin.text.markdown-gfm constant.other.language-name.markdown
|     ^^^^^^^^^ meta.code-fence.definition.begin.text.markdown-gfm - punctuation
foo
~~~
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

~~~~~foo~
|^^^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|    ^^^^ meta.code-fence.definition.begin.text.markdown-gfm constant.other.language-name.markdown

~~~~~
|^^^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://spec.commonmark.org/0.30/#example-147

```
| <- meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|^^ meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
``` aaa
| <- markup.raw.code-fence.markdown-gfm - punctuation
```
| <- meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://fenced-code-block-embedded-syntaxes-tests

```bash
# test
| ^^^^^ source.shell comment.line.number-sign
echo hello, \
|           ^^ punctuation.separator.continuation.line
echo This is a smiley :-\) \(I have to escape the parentheses, though!\)
|                       ^^ constant.character.escape
```
| <- meta.code-fence.definition.end.shell-script punctuation.definition.raw.code-fence.end
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```clojure
|^^^^^^^^^ meta.code-fence.definition.begin.clojure
|  ^^^^^^^ constant.other.language-name
 (/ 10 3.0)
| <- source.clojure
|^^^^^^^^^^ source.clojure
```
| <- meta.code-fence.definition.end.clojure.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.clojure.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```cmd

| <- markup.raw.code-fence.dosbatch.markdown-gfm source.dosbatch
```
| <- meta.code-fence.definition.end.dosbatch.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.dosbatch.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```css

| <- markup.raw.code-fence.css.markdown-gfm source.css
```
| <- meta.code-fence.definition.end.css.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.css.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```diff
+ inserted
| <- source.diff markup.inserted.diff punctuation.definition.inserted.diff
- deleted
| <- source.diff markup.deleted.diff punctuation.definition.deleted.diff
```
| <- meta.code-fence.definition.end.diff.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.diff.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```Graphviz
graph n {}
| ^^^ storage.type.dot
```
| <- meta.code-fence.definition.end.graphviz.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.graphviz.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```haskell

| <- markup.raw.code-fence.haskell.markdown-gfm source.haskell
```
| <- meta.code-fence.definition.end.haskell.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.haskell.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```html
  <html>
| <- markup.raw.code-fence.html.markdown-gfm text.html
| ^^^^^^ text.html meta.tag
```
| <- meta.code-fence.definition.end.html.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.html.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```html+php
<div></div>
|^^^ entity.name.tag.block.any.html
<?php
| <- markup.raw.code-fence.html-php.markdown-gfm embedding.php text.html.basic meta.embedded.block.php punctuation.section.embedded.begin.php
var_dump(expression);
| <- markup.raw.code-fence.html-php.markdown-gfm embedding.php text.html.basic meta.embedded.block.php source.php meta.function-call
```
| <- meta.code-fence.definition.end.html-php.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.html-php.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```js
| <- punctuation.definition.raw.code-fence.begin
|  ^^ constant.other.language-name
for (var i = 0; i < 10; i++) {
| ^ source.js keyword.control.loop
    console.log(i);
}
```
| <- meta.code-fence.definition.end.javascript.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.javascript.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```jsx

| <- markup.raw.code-fence.jsx.markdown-gfm
```
| <- meta.code-fence.definition.end.jsx.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.jsx.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```lisp

| <- markup.raw.code-fence.lisp.markdown-gfm source.lisp
```
| <- meta.code-fence.definition.end.lisp.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.lisp.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```lua

| <- markup.raw.code-fence.lua.markdown-gfm source.lua
```
| <- meta.code-fence.definition.end.lua.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.lua.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```matlab

| <- markup.raw.code-fence.matlab.markdown-gfm source.matlab
```
| <- meta.code-fence.definition.end.matlab.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.matlab.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```ocaml

| <- markup.raw.code-fence.ocaml.markdown-gfm source.ocaml
```
| <- meta.code-fence.definition.end.ocaml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.ocaml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```php
var_dump(expression);
| <- markup.raw.code-fence.php.markdown-gfm source.php meta.function-call.php
```
| <- meta.code-fence.definition.end.php.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.php.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

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
| <- meta.code-fence.definition.end.python.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.python.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```regex
(?x)
\s+
| <- markup.raw.code-fence.regexp.markdown-gfm source.regexp
```
| <- meta.code-fence.definition.end.regexp.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.regexp.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```scala

| <- markup.raw.code-fence.scala.markdown-gfm source.scala
```
| <- meta.code-fence.definition.end.scala.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.scala.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```sh

| <- markup.raw.code-fence.shell-script.markdown-gfm source.shell.bash
```
| <- meta.code-fence.definition.end.shell-script.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```shell
function foo () {
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown meta.function.shell keyword.declaration.function.shell 
}
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown meta.function.shell meta.compound.shell punctuation.section.compound.end.shell

$ ls ~
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive comment.other.shell
| ^^ meta.function-call.identifier.shell variable.function.shell
|   ^^ meta.function-call.arguments.shell

output.txt
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive - meta.function-call - variable
|^^^^^^^^^ markup.raw.code-fence.shell.markdown-gfm source.shell.interactive - meta.function-call - variable

$ ls \
> /foo/
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown comment.other.shell
|^^^^^^^ markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown

$ ls \
> /foo/
bar
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown - meta.function-call
|^^^ markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown - meta.function-call

function foo () {}
| <- markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown - meta.function
|^^^^^^^^^^^^^^^^^^ markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown - meta.function
```
| <- meta.code-fence.definition.end.shell.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.shell.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

   ```shell
   $ ls
|  ^^^^^ markup.raw.code-fence.shell.markdown-gfm source.shell.interactive.markdown
|  ^ comment.other.shell
|    ^^ meta.function-call.identifier.shell variable.function.shell
   ```

```shell-script

| <- markup.raw.code-fence.shell-script.markdown-gfm source.shell.bash
```
| <- meta.code-fence.definition.end.shell-script.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.shell-script.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```sql
|^^^^^ meta.code-fence.definition.begin.sql
|  ^^^ constant.other.language-name
SELECT TOP 10 *
|^^^^^^^^^^^^^^^ markup.raw.code-fence.sql source.sql
FROM TableName
```
| <- meta.code-fence.definition.end.sql.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.sql.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```ts
declare type foo = 'bar'
| <- markup.raw.code-fence.typescript.markdown-gfm source.ts
```
| <- meta.code-fence.definition.end.typescript.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.typescript.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

```tsx

| <- markup.raw.code-fence.tsx.markdown-gfm
```
| <- meta.code-fence.definition.end.tsx.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.tsx.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

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
| <- meta.code-fence.definition.end.xml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.xml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

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


# TEST: HTML BLOCKS ###########################################################

## https://spec.commonmark.org/0.30/#example-148

<table><tr><td>
<pre>
**Hello**,
| ^^^^^^^^^ meta.disable-markdown - markup

_world_.
| ^^^^ markup.italic - meta.disable-markdown
</pre>
</td></tr></table>

## https://spec.commonmark.org/0.30/#example-149

<table>
  <tr>
    <td>
           hi
|^^^^^^^^^^^^^ meta.disable-markdown
    </td>
  </tr>
</table>

okay.
| <- meta.paragraph.markdown
|^^^^^ meta.paragraph.markdown

## https://spec.commonmark.org/0.30/#example-150

 <div>
  *hello*
         <foo><a>
| <- meta.disable-markdown
|^^^^^^^^^^^^^^^^^ meta.disable-markdown
|        ^^^^^^^^ meta.tag

## https://spec.commonmark.org/0.30/#example-151

</div>
*foo*
| <- meta.disable-markdown - markup.italic
|^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-152

<DIV CLASS="foo">
| ^^^^^^^^^^^^^^^^ meta.disable-markdown

*Markdown*
| ^^^^^^^ meta.paragraph markup.italic - meta.disable-markdown

</DIV>
| ^^^ meta.disable-markdown meta.tag.block.any.html

## https://spec.commonmark.org/0.30/#example-153

<div id="foo"
  class="bar">
|^^^^^^^^^^^^^ meta.disable-markdown meta.tag.block  
</div>
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-154

<div id="foo" class="bar
  baz">
|^^^^^^ meta.disable-markdown meta.tag.block  
</div>
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-155

<div>
*foo*
| <- meta.disable-markdown - markup.italic

<div>
*foo*

*bar*
| <- meta.paragraph.markdown markup.italic.markdown punctuation.definition.italic.begin.markdown

## https://spec.commonmark.org/0.30/#example-159

<div><a href="bar">*foo*</a></div>
|                  ^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-161

<div></div>
``` c
int x = 33;
```
|^^^ meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-162

<a href="foo">
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</a>

## https://spec.commonmark.org/0.30/#example-163

<Warning>
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</Warning>
| ^^^^^^^ meta.disable-markdown meta.tag.other.html entity.name.tag.other.html

## https://spec.commonmark.org/0.30/#example-164

<i class="foo">
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</i>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^ meta.disable-markdown meta.tag
|   ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-165

</ins>
*bar*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic

## https://spec.commonmark.org/0.30/#example-166

<del>
*foo*
| <- meta.disable-markdown - markup.italic - punctuation
|^^^^^ meta.disable-markdown - markup.italic
</del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^^ meta.disable-markdown meta.tag
|     ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-167

<del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^ meta.disable-markdown meta.tag
|    ^ meta.disable-markdown - meta.tag

*foo*
| <- meta.paragraph.markdown markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^ meta.paragraph.markdown markup.italic.markdown - punctuation
|   ^ meta.paragraph.markdown markup.italic.markdown punctuation.definition.italic.end.markdown

</del>
| <- meta.disable-markdown meta.tag punctuation.definition.tag
|^^^^^ meta.disable-markdown meta.tag
|     ^ meta.disable-markdown - meta.tag

## https://spec.commonmark.org/0.30/#example-168

<del>*foo*</del>
|^^^^^^^^^^^^^^^ meta.paragraph - meta.disable-markdown
|^^^^ meta.tag.inline
|    ^^^^^ markup.italic
|         ^^^^^^ meta.tag.inline

## https://spec.commonmark.org/0.30/#example-169

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

## https://spec.commonmark.org/0.30/#example-170

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

## https://spec.commonmark.org/0.30/#example-171

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

## https://spec.commonmark.org/0.30/#example-172

<style
  type="text/css">
h1 {color:red;}
| <- meta.disable-markdown source.css.embedded.html meta.selector.css entity.name.tag

p {color:blue;}
| <- meta.disable-markdown source.css.embedded.html meta.selector.css entity.name.tag
</style>
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-174

> <div>
> foo

bar
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-175

- <div>
- foo
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-176

<style>p{color:red;}</style>
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown
*foo*
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-177

<!-- foo -->*bar*
| ^^^^^^^^^^ comment.block.html
|           ^^^^^ meta.disable-markdown
*baz*
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-178

<script>
foo
</script>1. *bar*
| ^^^^^^^^^^^^^^^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-179

<!-- Foo
| ^^ meta.disable-markdown comment.block.html punctuation.definition.comment

bar
   baz -->
| ^^^^^^^^ meta.disable-markdown comment.block.html
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-180

<?php
| ^^^^ meta.disable-markdown

  echo '>';

?>
|^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-181

<!DOCTYPE html>
| ^^^^^^^ meta.disable-markdown meta.tag.sgml.doctype.html
okay
| <- - meta.disable-markdown

<!ENTITY html>
| ^^^^^^^^^^^^^ meta.disable-markdown
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-182

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
|^^ meta.disable-markdown meta.tag.sgml
okay
| <- - meta.disable-markdown

## https://spec.commonmark.org/0.30/#example-183

  <!-- foo -->
| ^^^^^^^^^^^^ meta.disable-markdown comment.block.html

    <!-- foo -->
|^^^^^^^^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-184

  <div>

    <div>
|^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-188

<div>

*Emphasized* text.
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^ markup.italic.markdown

</div>
| <- meta.disable-markdown meta.tag.block
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-189

<div>
*Emphasized* text.
| <- meta.disable-markdown - markup.italic
|^^^^^^^^^^^^^^^^^^ meta.disable-markdown - markup.italic
</div>
| <- meta.disable-markdown meta.tag.block
|^^^^^ meta.disable-markdown meta.tag.block

## https://spec.commonmark.org/0.30/#example-190

<table>
| <- meta.disable-markdown meta.tag
|^^^^^^ meta.disable-markdown meta.tag

<tr>
| <- meta.disable-markdown meta.tag
|^^^ meta.disable-markdown meta.tag

<td>
Hi
</td>
| <- meta.disable-markdown meta.tag
|^^^^ meta.disable-markdown meta.tag

</tr>
| <- meta.disable-markdown meta.tag
|^^^^ meta.disable-markdown meta.tag

</table>
| <- meta.disable-markdown meta.tag
|^^^^^^^ meta.disable-markdown meta.tag

## https://spec.commonmark.org/0.30/#example-191

<table>
| <- meta.disable-markdown meta.tag
|^^^^^^ meta.disable-markdown meta.tag

  <tr>
| <- meta.disable-markdown
|^^^^^^^ meta.disable-markdown

    <td>
      Hi
    </td>
| <- markup.raw.block.markdown
|^^^^^^^^^ markup.raw.block.markdown

  </tr>
| <- meta.disable-markdown
|^^^^^^^ meta.disable-markdown

</table>
| <- meta.disable-markdown meta.tag
|^^^^^^^ meta.disable-markdown meta.tag

## https://custom-tests/html-blocks

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


# TEST: LINK REFERENCE DEFINITIONS ############################################

## https://spec.commonmark.org/0.30/#example-192

[foo]: /url "title"
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|    ^ punctuation.separator.key-value
|      ^^^^ markup.underline.link
|           ^^^^^^^ string.quoted.double

## https://spec.commonmark.org/0.30/#example-193

   [foo]: 
      /url  
           'the title'  
|^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|          ^^^^^^^^^^^ string.quoted.single

## https://spec.commonmark.org/0.30/#example-194

 [Foo*bar\]]:my_(url) 'title (with parens)'
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^ punctuation.definition.reference.begin.markdown
| ^^^^^^^^^ entity.name.reference.link.markdown - punctuation
|          ^ punctuation.definition.reference.end.markdown
|           ^ punctuation.separator.key-value.markdown
|            ^^^^^^^^ markup.underline.link
|                    ^ - markup - string
|                     ^^^^^^^^^^^^^^^^^^^^^ string.quoted.single

## https://spec.commonmark.org/0.30/#example-195

[Foo bar]:
<my url>
| <- meta.link.reference.def.markdown punctuation.definition.link.begin.markdown
|^^^^^^ meta.link.reference.def.markdown markup.underline.link.markdown
|      ^ meta.link.reference.def.markdown punctuation.definition.link.end.markdown

[Foo bar]:
<my url>
'title'
| <- meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
|^^^^^^ meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown

## https://spec.commonmark.org/0.30/#example-196

[foo]: /url '
|           ^ meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown punctuation.definition.string.begin.markdown
title
| <- meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
|^^^^^ meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
line1
| <- meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
|^^^^^ meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
line2
| <- meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
|^^^^^ meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown
'
| <- meta.link.reference.def.markdown meta.string.title.markdown string.quoted.single.markdown punctuation.definition.string.end.markdown

## https://spec.commonmark.org/0.30/#example-197

[foo]: /url 'title

with blank line'
| <- meta.paragraph.markdown - meta.link
|^^^^^^^^^^^^^^^ meta.paragraph.markdown - meta.link

## https://spec.commonmark.org/0.30/#example-198

[foo]:
/url
| <- meta.link.reference.def.markdown markup.underline.link.markdown punctuation.separator.path.markdown
|^^^ meta.link.reference.def.markdown markup.underline.link.markdown

## https://spec.commonmark.org/0.30/#example-199

[foo]:
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^ meta.link.reference.def.markdown entity.name.reference.link.markdown
|   ^ meta.link.reference.def.markdown punctuation.definition.reference.end.markdown
|    ^ meta.link.reference.def.markdown punctuation.separator.key-value.markdown
|     ^ meta.link.reference.def.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-200

[foo]: <>
|^^^^^^^^ meta.link.reference.def.markdown
|    ^ punctuation.separator.key-value
|      ^ punctuation.definition.link.begin
|       ^ punctuation.definition.link.end

## https://spec.commonmark.org/0.30/#example-201

[foo]: <bar>(baz)
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^ punctuation.definition.link.begin.markdown
|       ^^^ markup.underline.link.markdown
|          ^ punctuation.definition.link.end.markdown
|           ^^^^^ meta.string.title.markdown string.quoted.other.markdown
|           ^ punctuation.definition.string.begin.markdown
|               ^ punctuation.definition.string.end.markdown

## https://spec.commonmark.org/0.30/#example-202

[foo]: /url\bar\*baz "foo\"bar\baz"
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^^^^^^^^^^^^^ markup.underline.link.markdown
|      ^ punctuation.separator.path.markdown
|          ^^ - constant.character.escape
|              ^^ constant.character.escape.markdown
|                    ^^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown
|                    ^ punctuation.definition.string.begin.markdown
|                        ^^ constant.character.escape.markdown
|                             ^^ - constant.character.escape
|                                 ^ punctuation.definition.string.end.markdown

## https://spec.commonmark.org/0.30/#example-203

[foo]: url
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^^^ markup.underline.link.markdown

## https://spec.commonmark.org/0.30/#example-204

[foo]: first
[foo]: second
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^^^^^^ markup.underline.link.markdown

## https://spec.commonmark.org/0.30/#example-205

[FOO]: /url
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^^^^ markup.underline.link.markdown

## https://spec.commonmark.org/0.30/#example-206

[ΑΓΩ]: /φου
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^ meta.link.reference.def.markdown
|^^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown
|      ^^^^ markup.underline.link.markdown

## https://spec.commonmark.org/0.30/#example-208

[
foo
]: /url
bar
| <- meta.paragraph.markdown - meta.link
|^^^ meta.paragraph.markdown - meta.link

## https://spec.commonmark.org/0.30/#example-209

This is not a link reference definition, because there are characters other than spaces or tabs after the title:

[foo]: /url "title" ok
|^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|                   ^^ invalid.illegal.expected-eol.markdown

## https://spec.commonmark.org/0.30/#example-210

This is a link reference definition, but it has no title:

[foo]: /url
"title" ok
|^^^^^^^^^ meta.link.reference.def.markdown
|       ^^ invalid.illegal.expected-eol.markdown

[foo]: <bar> "baz" 
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|            ^^^^^ string.quoted.double
|                 ^ - invalid.illegal.expected-eol

[foo]: <bar>> "baz" 
|^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|      ^ punctuation.definition.link.begin
|       ^^^ markup.underline.link
|          ^ punctuation.definition.link.end
|           ^^^^^^^ invalid.illegal.expected-eol.markdown

## https://spec.commonmark.org/0.30/#example-211

This is not a link reference definition, because it is indented four spaces:

    [foo]: /url "title"
|^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block.markdown - meta.link

## https://spec.commonmark.org/0.30/#example-212

This is not a link reference definition, because it occurs inside a code block:

```
[foo]: /url
| <- markup.raw.code-fence.markdown-gfm - meta.link
|^^^^^^^^^^^ markup.raw.code-fence.markdown-gfm - meta.link
```

## https://spec.commonmark.org/0.30/#example-213

A link reference definition cannot interrupt a paragraph.

Foo
[bar]: /baz
| <- meta.paragraph.markdown meta.link.reference.description.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^ meta.paragraph.markdown
|^^^^ meta.link.reference.description.markdown
|    ^^^^^^^ - punctuation - markup.underline

## https://spec.commonmark.org/0.30/#example-214

### [Foo]
[foo]: /url
| <- meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
|^^^^^^^^^^^ meta.link.reference.def.markdown

### [Foo]
[foo]: /url
> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-218

> [foo]: /url
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.link
| ^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown
| ^ punctuation.definition.reference.begin.markdown
|  ^^^ entity.name.reference.link.markdown
|     ^ punctuation.definition.reference.end.markdown
|      ^ punctuation.separator.key-value.markdown
|        ^^^^ markup.underline.link.markdown

## https://custom-tests/link-reference-definitions/in-block-quotes

> [foo]: /url "description"
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown
| ^ punctuation.definition.reference.begin.markdown
|  ^^^ entity.name.reference.link.markdown
|     ^ punctuation.definition.reference.end.markdown
|      ^ punctuation.separator.key-value.markdown
|        ^^^^ markup.underline.link.markdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> [foo]: 
> /url
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown meta.link.reference.def.markdown - markup.underline
| ^^^^ markup.quote.markdown meta.link.reference.def.markdown markup.underline.link.markdown

> [foo]: 
> /url
> "description"
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown meta.link.reference.def.markdown - meta.string - string
| ^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown

> [foo]:
> </url-with
> -continuation>
| <- markup.quote.markdown meta.link.reference.def.markdown markup.underline.link.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown
|^^^^^^^^^^^^^^ markup.underline.link.markdown
|              ^ punctuation.definition.link.end.markdown

> [foo]: 
  /url
| <- markup.quote.markdown - markup.underline - punctuation
|^ markup.quote.markdown meta.link.reference.def.markdown - markup.underline
| ^^^^ markup.quote.markdown meta.link.reference.def.markdown markup.underline.link.markdown

> [foo]: 
  /url
  "description"
| <- markup.quote.markdown - meta.string - string - punctuation
|^ markup.quote.markdown meta.link.reference.def.markdown - meta.string - string
| ^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown

> [foo]:
  </url-with
  -continuation>
| <- markup.quote.markdown meta.link.reference.def.markdown markup.underline.link.markdown
|^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.markdown
|^^^^^^^^^^^^^^ markup.underline.link.markdown
|              ^ punctuation.definition.link.end.markdown

## https://custom-tests/link-reference-definitions

[//]: # (This is a comment without a line-break.)
|     ^ meta.link.reference.def.markdown markup.underline.link
|       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ string.quoted.other

[//]: # (This is a comment with a
|     ^ meta.link.reference.def.markdown markup.underline.link
|       ^ punctuation.definition.string.begin
        line-break.)
|                  ^ punctuation.definition.string.end

[//]: # (testing)blah
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.markdown
|       ^ punctuation.definition.string.begin
|               ^ punctuation.definition.string.end
|                ^^^^ invalid.illegal.expected-eol
|                    ^ - invalid

[//]: # (testing
blah
| <- meta.link.reference.def.markdown string.quoted.other

| <- invalid.illegal.non-terminated.link-title
text
| <- meta.paragraph - meta.link.reference.def.markdown

## https://custom-tests/footnote-reference-definitions

 [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
|^ punctuation.definition.reference.begin.markdown
| ^^ entity.name.reference.link.markdown
|   ^ punctuation.definition.reference.end.markdown
|    ^ punctuation.separator.key-value.markdown

  [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
| ^ punctuation.definition.reference.begin.markdown
|  ^^ entity.name.reference.link.markdown
|    ^ punctuation.definition.reference.end.markdown
|     ^ punctuation.separator.key-value.markdown

   [^1]: And that's the footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
|  ^ punctuation.definition.reference.begin.markdown
|   ^^ entity.name.reference.link.markdown
|     ^ punctuation.definition.reference.end.markdown
|      ^ punctuation.separator.key-value.markdown

     [^1]: And that's no footnote.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block.markdown

[^1]:
    And that's the footnote
with a *second* line.
|^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra - markup.raw

[^1]:
    And that's the footnote.

    That's the *second* footnote paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra - markup.raw
|              ^^^^^^^^ markup.italic

[^1]:
    And that's the footnote.

   Not a footnote paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - meta.link

[^1]:
    And that's the footnote
with a *second* line.
[^2]: second
| <- meta.link.reference.def.footnote.markdown-extra punctuation.definition.reference.begin.markdown
|^^^^^^^^^^^^ meta.link.reference.def.footnote.markdown-extra
|^^ entity.name.reference.link.markdown
|  ^ punctuation.definition.reference.end.markdown
|   ^ punctuation.separator.key-value.markdown

## https://custom-tests/footnote-reference-definitions/in-block-quotes

> [^1]: And that's the footnote.
|^ markup.quote.markdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.footnote.markdown-extra
| ^ punctuation.definition.reference.begin.markdown
|  ^^ entity.name.reference.link.markdown
|    ^ punctuation.definition.reference.end.markdown
|     ^ punctuation.separator.key-value.markdown

>  [^1]: And that's the footnote.
|^ markup.quote.markdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.footnote.markdown-extra
|  ^ punctuation.definition.reference.begin.markdown
|   ^^ entity.name.reference.link.markdown
|     ^ punctuation.definition.reference.end.markdown
|      ^ punctuation.separator.key-value.markdown

>   [^1]: And that's the footnote.
|^ markup.quote.markdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.footnote.markdown-extra
|   ^ punctuation.definition.reference.begin.markdown
|    ^^ entity.name.reference.link.markdown
|      ^ punctuation.definition.reference.end.markdown
|       ^ punctuation.separator.key-value.markdown

>     [^1]: And that's no footnote.
|^ markup.quote.markdown - meta.link - markup.raw
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.raw.block.markdown

> [^1]: And that's the footnote.
> with a *second* line.
| <- markup.quote.markdown meta.link.reference.def.footnote.markdown-extra punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.footnote.markdown-extra

> [^1]:
>     And that's the footnote.
> 
>     That's the *second* paragraph.
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown meta.link.reference.def.footnote.markdown-extra
|                ^^^^^^^^ markup.italic

> [^1]:
>     And that's the footnote.
> 
>    Not a footnote paragraph.
| <- markup.quote.markdown punctuation.definition.blockquote.markdown - markup.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.paragraph.markdown - markup.link

>   [^1]: And that's the footnote.
> 
>     code block
| <- markup.quote.markdown punctuation.definition.blockquote.markdown - markup.raw
|^ markup.quote.markdown - markup.raw
| ^^^^^^^^^^^^^^^ markup.quote.markdown markup.raw.block.markdown

> [^1]:
>     And that's the footnote.
> 
      That's not a *second* paragraph.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block.markdown

# TEST: TABLES ################################################################

| foo | bar |
|^^^^^^^^^^^^^ meta.table.header
| <- punctuation.separator.table-cell
|     ^ punctuation.separator.table-cell
|           ^ punctuation.separator.table-cell
| ^^^^ - punctuation.separator.table-cell

| foo | bar |
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

| f\|oo  |
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
paragraph
| <- meta.paragraph.markdown
|^^^^^^^^^ meta.paragraph.markdown

| table | followed by
https://foo.bar/baz
| <- meta.paragraph.markdown meta.link.inet.markdown markup.underline.link.markdown-gfm
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inet.markdown markup.underline.link.markdown-gfm

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


# TEST: BLOCK QUOTES ##########################################################

## https://spec.commonmark.org/0.30/#example-228

> # Foo
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - markup.heading
| ^^^^^^ markup.quote.markdown markup.heading.1.markdown
| ^ punctuation.definition.heading.begin.markdown
|   ^^^ entity.name.section.markdown

> # Foo
bar
| <- meta.paragraph.markdown - markup.quote
|^^ meta.paragraph.markdown - markup.quote

> # Foo
> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

> # Foo
> bar
> baz
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-229

># Foo
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^^ markup.quote.markdown markup.heading.1.markdown
|^ punctuation.definition.heading.begin.markdown
|  ^^^ entity.name.section.markdown

># Foo
>bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^ markup.quote.markdown

># Foo
>bar
> baz
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-230

   > # Foo
| <- markup.quote.markdown
|^^^^^^^^^^ markup.quote.markdown
|  ^ punctuation.definition.blockquote.markdown
|    ^^^^^^ markup.heading.1.markdown
|    ^ punctuation.definition.heading.begin.markdown
|      ^^^ entity.name.section.markdown

   > # Foo
   > bar
| <- markup.quote.markdown - punctuation
|^^ markup.quote.markdown - punctuation
|  ^ markup.quote.markdown punctuation.definition.blockquote.markdown
|   ^^^^^ markup.quote.markdown - punctuation

   > # Foo
   > bar
 > baz
| <- markup.quote.markdown - punctuation
|^ markup.quote.markdown punctuation.definition.blockquote.markdown
| ^^^^^ markup.quote.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-231

    > # Foo
    > bar
    > baz
| <- markup.raw.block.markdown
|^^^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-232

> # Foo
> bar
baz
| <- markup.quote.markdown
|^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-233

> bar
baz
| <- markup.quote.markdown
|^^^ markup.quote.markdown
> foo
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-234

> foo
***
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote

> foo
---
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote

> foo
___
| <- meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote
|^^ meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown - markup.quote

## https://spec.commonmark.org/0.30/#example-235

> - foo
- bar
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown - markup.quote
|^^^^^ markup.list.unnumbered.markdown - markup.quote

## https://spec.commonmark.org/0.30/#example-236

>     foo
    bar
| <- markup.raw.block.markdown
|^^^^^^^ markup.raw.block.markdown

## https://spec.commonmark.org/0.30/#example-237

> ```
foo
| <- meta.paragraph.markdown - markup.quote - markup.raw
|^^^ meta.paragraph.markdown - markup.quote - markup.raw

## https://spec.commonmark.org/0.30/#example-238

> foo
    - bar
| <- markup.quote.markdown - markup.list - markup.raw
|^^^^^^^^^ markup.quote.markdown - markup.list - markup.raw

## https://spec.commonmark.org/0.30/#example-239

>
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-240

>
>  
> 
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-241

>
> foo
>  
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-242

> foo

| <- - markup.quote
> foo

> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-243

> foo
> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-244

> foo
>
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown

## https://spec.commonmark.org/0.30/#example-245

foo
> bar
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-246

> aaa
***
> bbb
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-247

> bar
baz
| <- markup.quote.markdown
|^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-248

> bar

baz
| <- meta.paragraph.markdown - markup.quote
|^^ meta.paragraph.markdown - markup.quote

## https://spec.commonmark.org/0.30/#example-249

> bar
>
baz
| <- meta.paragraph.markdown - markup.quote
|^^ meta.paragraph.markdown - markup.quote

## https://spec.commonmark.org/0.30/#example-250

> > > foo
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^ markup.quote.markdown
| ^ punctuation.definition.blockquote.markdown
|   ^ punctuation.definition.blockquote.markdown
|    ^^^^^ - punctuation

> > > foo
bar
| <- markup.quote.markdown
|^^^ markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-251

>>> foo
> bar
>>baz
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown punctuation.definition.blockquote.markdown
| ^^^^ markup.quote.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-252

>     code
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown - markup.raw
| ^^^^^^^^^ markup.quote.markdown markup.raw.block.markdown

>    not code
| <- markup.quote.markdown punctuation.definition.blockquote.markdown - markup.raw
|^^^^^^^^^^^^^ markup.quote.markdown - markup.raw

## https://custom-tests/block-quotes/block-quote-starts

>=
| <- punctuation.definition.blockquote.markdown 

>==
| <- punctuation.definition.blockquote.markdown

  >=
| ^ punctuation.definition.blockquote.markdown
    >=
| ^^^^^ markup.quote.markdown - punctuation

    >=
|   ^^ markup.raw.block.markdown - markup.quote - punctuation

## https://custom-tests/block-quotes/block-quote-nesting

> > Nested block quote
| <- markup.quote punctuation.definition.blockquote
| ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown
|^ - punctuation
| ^ punctuation.definition.blockquote
|  ^ - punctuation

> > Nested quote
> Followed by more quoted text that is not nested
| <- markup.quote punctuation.definition.blockquote - markup.quote markup.quote

>    > this is a nested quote but no code in a block quote
| <- punctuation.definition.blockquote
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown

>    > this is a nested quote but no code in a block quote
>     > with a second line of content
| <- punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.paragraph.markdown
|     ^ - punctuation

>     > this is code in a block quote, not a nested quote
| <- punctuation.definition.blockquote
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block - markup.quote markup.quote

## https://custom-tests/block-quotes/block-quote-terminations

> Block quote followed by heading
# heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^ markup.heading.1.markdown - meta.quote
| ^^^^^^^ entity.name.section.markdown

> Block quote followed by unordered list
* list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by unordered list
+ list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by unordered list
- list item
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^ markup.list.unnumbered.markdown - meta.quote

> Block quote followed by ordered list
1. list item
| <- markup.list.numbered.bullet.markdown - punctuation
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

> Block quote followed by ordered list
2. list item
| <- markup.list.numbered.bullet.markdown - punctuation
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

> Block quote followed by invalid list
1234567890. no list item
| <- markup.quote.markdown - markup.list
|^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown - markup.list

> Block quote followed by html block
<p>*no-markdown</p>
| <- meta.disable-markdown meta.tag.block
|^^^^^^^^^^^^^^^^^^^ meta.disable-markdown

## https://custom-tests/block-quotes/thematic-breaks

> * * *
paragraph
| <- meta.paragraph.markdown - markup.quote

> - - -
paragraph
| <- meta.paragraph.markdown - markup.quote

> _ _ _
paragraph
| <- meta.paragraph.markdown - markup.quote

> paragraph
> * * *
| ^^^^^^ markup.quote.markdown meta.separator.thematic-break.markdown

> paragraph
> - - -
| ^^^^^^ markup.quote.markdown meta.separator.thematic-break.markdown

> paragraph
> _ _ _
| ^^^^^^ markup.quote.markdown meta.separator.thematic-break.markdown

## https://custom-tests/block-quotes/fenced-code-blocks

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
|              ^^^ - punctuation

> > 2nd level quoted fenced code block
> > ```
> > code block ```
> > ```
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^ markup.quote.markdown - meta.code-fence
|   ^^^ markup.quote.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

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

> > ```
> This is a paragraph highlight as code,
> because nested block quotes can't be counted.
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown

## https://custom-tests/block-quotes/list-blocks/basics

> Block quote with lists
> - list item 1
| ^ markup.quote punctuation.definition.list_item
> - list item 2
| ^ markup.list.unnumbered.bullet punctuation.definition.list_item
| ^^^^^^^^^^^^^^ markup.quote markup.list.unnumbered
>   1. sub list item
| <- markup.quote punctuation.definition.blockquote
|^^^^^^^^^^^^^^^^^^ markup.quote
| ^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered
|    ^ punctuation.definition.list_item
|   ^^ markup.list.numbered.bullet
> - list item 3
  continued
| ^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown

## https://custom-tests/block-quotes/list-blocks/items-with-line-continuation

> * list item
> second line
| <- markup.quote.markdown markup.list.unnumbered.markdown punctuation.definition.blockquote.markdown
>   + subitem
> second line
| <- markup.quote.markdown markup.list.unnumbered.markdown punctuation.definition.blockquote.markdown
>     - subitem
> second line
| <- markup.quote.markdown markup.list.unnumbered.markdown punctuation.definition.blockquote.markdown
>       - subitem
> second line
| <- markup.quote.markdown markup.list.unnumbered.markdown punctuation.definition.blockquote.markdown

> * list item
second line
| <- markup.quote.markdown markup.list.unnumbered.markdown
>   + subitem
  second line
| <- markup.quote.markdown markup.list.unnumbered.markdown
>     - subitem
   second line
| <- markup.quote.markdown markup.list.unnumbered.markdown
>       - subitem
     second line
| <- markup.quote.markdown markup.list.unnumbered.markdown

> 1. list item
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>    2. subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>       3. subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>          4. subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown

> 1. list item
second line
| <- markup.quote.markdown markup.list.numbered.markdown
>    2. subitem
  second line
| <- markup.quote.markdown markup.list.numbered.markdown
>       3. subitem
   second line
| <- markup.quote.markdown markup.list.numbered.markdown
>          4. subitem
    second line
| <- markup.quote.markdown markup.list.numbered.markdown

> 1. list item
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>    + subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>      - subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
>        - subitem
> second line
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown

> 1. list item
second line
| <- markup.quote.markdown markup.list.numbered.markdown
>    + subitem
  second line
| <- markup.quote.markdown markup.list.numbered.markdown
>      - subitem
   second line
| <- markup.quote.markdown markup.list.numbered.markdown
>        - subitem
    second line
| <- markup.quote.markdown markup.list.numbered.markdown

## https://custom-tests/block-quotes/list-blocks/items-with-thematic-breaks

> - * * * * * * *
| ^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered
| ^ punctuation.definition.list_item.markdown
|   ^^^^^^^^^^^^^^ meta.separator.thematic-break.markdown
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation
|               ^ punctuation.definition.thematic-break
|                ^ - punctuation

> - * * * * * * *
>   still a list item
|   ^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown

> - - * * * * * *
| ^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered
| ^ punctuation.definition.list_item.markdown
|   ^ punctuation.definition.list_item.markdown
|    ^ - punctuation
|     ^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.separator.thematic-break.markdown
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation
|               ^ punctuation.definition.thematic-break
|                ^ - punctuation

> - - * * * * * *
>     still a list item
| <- markup.quote.markdown markup.list.unnumbered.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.unnumbered.markdown - meta.paragraph
| ^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown meta.paragraph.list.markdown

> 1. * * * * * * *
| ^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered
| ^^ markup.list.numbered.bullet.markdown
|    ^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.separator.thematic-break.markdown
|    ^ punctuation.definition.thematic-break
|     ^ - punctuation
|      ^ punctuation.definition.thematic-break
|       ^ - punctuation
|        ^ punctuation.definition.thematic-break
|         ^ - punctuation
|          ^ punctuation.definition.thematic-break
|           ^ - punctuation
|            ^ punctuation.definition.thematic-break
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break
|               ^ - punctuation
|                ^ punctuation.definition.thematic-break
|                 ^ - punctuation

> 1. * * * * * * *
>    still a list item
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.numbered.markdown - meta.paragraph
| ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.paragraph.list.markdown

## https://custom-tests/block-quotes/list-blocks/unordered-items-with-atx-headings

> * list item
> # global heading
  | <- markup.quote.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.list
  |^^^^^^^^^^^^^^^^ markup.quote.markdown markup.heading.1.markdown - markup.list
> 
> * list item
>  # global heading (matched as list item heading)
   | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
   |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown
>
> * list item
>   # list item heading
    | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown
> * list item
>   ## list item heading
    | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown
>   + list item
>     ### list item heading
      | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.3.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.3.markdown
>   + list item
>     ### list item heading
>     + list item
>       #### list item heading
        | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.4.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.4.markdown

> * 
>   # list item heading
    | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown  
>   + 
>     # list item heading
      | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown  
>   + 
>     # list item heading
>     - 
>       # list item heading 1
        | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown   
>   + 
>     # list item heading
>     - 
>       # list item heading 1
>
>       ## list item heading 2
        | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown

>       ## not a list item heading
        | <- markup.quote.markdown markup.raw.block.markdown
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.raw.block.markdown

> * 
> 
>   # list item heading
    | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown  
> 
>   + 
> 
>     # list item heading
      | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown  
>   + 
> 
>     # list item heading
> 
>     - 
> 
>       # list item heading 1
        | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.1.markdown  
>   + 
> 
>     # list item heading
> 
>     - 
> 
>       # list item heading 1
> 
>       ## list item heading 2
        | <- markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.unnumbered.markdown markup.heading.2.markdown

>       ## not a list item heading
        | <- markup.quote.markdown markup.raw.block.markdown
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.raw.block.markdown

## https://custom-tests/block-quotes/list-blocks/ordered-items-with-atx-headings

> 
> 1. list item
> # global heading
  | <- markup.quote.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.list
  |^^^^^^^^^^^^^^^^ markup.quote.markdown markup.heading.1.markdown - markup.list
> 
> 2. list item
>  # global heading (matched as list item heading)
   | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
>  |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
> 
> 3. list item
>    # list item heading
     | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. list item
>       # list item heading
        | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    2. list item
>       # list item heading
>       1. list item
>          # list item heading
           | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
           |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    3. list item
>       # list item heading
        | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown

> 1. 
>    # list item heading
     | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. 
>       # list item heading
        | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. 
>       # list item heading
>       1. 
>          # list item heading
           | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
           |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. 
>       # list item heading
>       1. 
>          # list item heading
> 
>          ## list item heading 2
           | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
           |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.2.markdown
  
> 1. 
> 
>    # list item heading
     | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
     |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
> 
>    1. 
> 
>       # list item heading
        | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
        |^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. 
> 
>       # list item heading
> 
>       1. 
> 
>          # list item heading 1
           | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
           |^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown
>    1. 
> 
>       # list item heading
> 
>       1. 
> 
>          # list item heading 1
>
>          ## list item heading 2
           | <- markup.quote.markdown markup.list.numbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
           |^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.2.markdown

## https://custom-tests/block-quotes/list-blocks/items-with-fenced-code-blocks

> 1. item
>    + item
>      - item
>        ```C++
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.numbered.markdown - meta.code-fence
| ^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.code-fence.definition.begin.text.markdown-gfm
|        ^^^ punctuation.definition.raw.code-fence.begin.markdown
|           ^^^ constant.other.language-name.markdown

> 1. item
>    + item
>      - item
>        ```C++
>        code
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.numbered.markdown - meta.code-fence
| ^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.raw.code-fence.markdown-gfm

> 1. item
>    + item
>      - item
>        ```C++
>        code
>        ```
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.numbered.markdown - meta.code-fence
| ^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.code-fence.definition.end.text.markdown-gfm
|        ^^^ punctuation.definition.raw.code-fence.end.markdown

## https://custom-tests/block-quotes/list-blocks/unordered-items-with-reference-definitions

> * list item [ref]
    |         ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown
>
>   + sub item [ref]
      |        ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown
> 
>     [ref]: /url
      | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
      |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
      |^^^ entity.name.reference.link.markdown
      |   ^ punctuation.definition.reference.end.markdown
      |    ^ punctuation.separator.key-value.markdown
      |      ^^^^ markup.underline.link.markdown
>
>   + sub item [ref]
>     - sub item [ref]
        |        ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown
>     
>       [ref]: /url
        | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
        |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
        |^^^ entity.name.reference.link.markdown
        |   ^ punctuation.definition.reference.end.markdown
        |    ^ punctuation.separator.key-value.markdown
        |      ^^^^ markup.underline.link.markdown
>
>   + sub item [ref]
>     - sub item [ref]
>     
>       [ref]: /url
>
>  [ref]: /url
   | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
   |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
   |^^^ entity.name.reference.link.markdown
   |   ^ punctuation.definition.reference.end.markdown
   |    ^ punctuation.separator.key-value.markdown
   |      ^^^^ markup.underline.link.markdown

## https://custom-tests/block-quotes/list-blocks/ordered-items-with-reference-definitions

> 1. list item [ref]
     |         ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown
>
>    2. sub item [ref]
>       |        ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown
>
>       [ref]: /url
        | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
        |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
        |^^^ entity.name.reference.link.markdown
        |   ^ punctuation.definition.reference.end.markdown
        |    ^ punctuation.separator.key-value.markdown
        |      ^^^^ markup.underline.link.markdown
>
>    2. sub item [ref]
>       3. sub item [ref]
>          |        ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown
>        
>          [ref]: /url
           | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
           |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
           |^^^ entity.name.reference.link.markdown
           |   ^ punctuation.definition.reference.end.markdown
           |    ^ punctuation.separator.key-value.markdown
           |      ^^^^ markup.underline.link.markdown
>
>    2. sub item [ref]
>       3. sub item [ref]
>        
>          [ref]: /url
>          
>    [ref]: /url
     | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
     |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
     |^^^ entity.name.reference.link.markdown
     |   ^ punctuation.definition.reference.end.markdown
     |    ^ punctuation.separator.key-value.markdown
     |      ^^^^ markup.underline.link.markdown

## https://custom-tests/block-quotes/list-blocks/items-with-reference-definitions

> 1. item
>    + item
>      - item [foo]
>
>        [foo]: /url "description"
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
|^ markup.quote.markdown markup.list.numbered.markdown - meta.link
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|        ^ punctuation.definition.reference.begin.markdown
|         ^^^ entity.name.reference.link.markdown
|            ^ punctuation.definition.reference.end.markdown
|             ^ punctuation.separator.key-value.markdown
|               ^^^^ markup.underline.link.markdown
|                    ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        /url "description"
| <- markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|        ^^^^ markup.underline.link.markdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        /url
>        "description"
| <- markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|        ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
>        </url-with
>        -continuation>
| <- markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown
|                     ^ punctuation.definition.link.end.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         /url "description"
|<- markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|        ^^^^ markup.underline.link.markdown
|             ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         /url
         "description"
| <- markup.quote.markdown - meta.string - string - punctuation
|^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|        ^^^^^^^^^^^^^ meta.string.title.markdown string.quoted.double.markdown

> 1. item
>    + item
>      - item [foo]
>
>        [foo]:
         </url-with
         -continuation>
| <- markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown
|^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.markdown
|^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown
|                     ^ punctuation.definition.link.end.markdown

## https://custom-tests/block-quotes/list-blocks/items-with-footnote-definitions

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.footnote.markdown-extra

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>        [^2]:
|        ^^^^^^ markup.quote.markdown markup.list.numbered.markdown meta.link.reference.def.footnote.markdown-extra
|        ^ punctuation.definition.reference.begin.markdown
|         ^^ entity.name.reference.link.markdown
|           ^ punctuation.definition.reference.end.markdown
|            ^ punctuation.separator.key-value.markdown

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>        # header
|^ markup.quote.markdown markup.list.numbered.markdown - markup.heading
| ^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown

> 1. list item
>    + sub item
>      - sub item [^1]
>      
>        [^1]:
>            This is a foot note
>            with a second line
>      - sub item
|^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown
|      ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

## https://custom-tests/block-quotes#gfm-tasks

> Block quote with GFM tasks
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

## https://custom-tests/block-quotes#emphasis

> Blcok quotes support markup,
> like *italics*, **bold**, ***bold italic*** and ~~strikethrough~~.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown
|      ^^^^^^^^^ markup.italic.markdown
|                 ^^^^^^^^ markup.bold.markdown
|                           ^^ markup.bold.markdown punctuation.definition.bold.begin.markdown
|                             ^ markup.bold.markdown markup.italic.markdown punctuation.definition.italic.begin.markdown
|                              ^^^^^^^^^^^ markup.bold.markdown markup.italic.markdown - punctuation
|                                         ^ markup.bold.markdown markup.italic.markdown punctuation.definition.italic.end.markdown
|                                          ^^ markup.bold.markdown punctuation.definition.bold.end.markdown
|                                                 ^^^^^^^^^^^^^^^^^ markup.strikethrough.markdown-gfm


# TEST: LIST BLOCKS ###########################################################

## https://spec.commonmark.org/0.30/#example-253

A paragraph
with two lines.

    indented code

> A block quote.
| <- markup.quote.markdown punctuation.definition.blockquote.markdown - markup.raw
|^^^^^^^^^^^^^^^^ markup.quote.markdown - markup.raw

## https://spec.commonmark.org/0.30/#example-254

1.  A paragraph
    with two lines.

        indented code

    > A block quote.
| <- markup.list.numbered.markdown markup.quote.markdown
|^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown
|   ^ punctuation.definition.blockquote.markdown

## https://spec.commonmark.org/0.30/#example-255

- one

 two
| <- markup.list.unnumbered.markdown
|^^^^ markup.list.unnumbered.markdown

> Note: `two` is not a part of the list item, but ST can't handle it!

## https://spec.commonmark.org/0.30/#example-256

- one

  two
| <- markup.list.unnumbered.markdown
|^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-257

 -    one

     two
| <- markup.list.unnumbered.markdown
|^^^^^^^^ markup.list.unnumbered.markdown

> Note: `two` is not a part of the list item, but ST can't handle it!

## https://spec.commonmark.org/0.30/#example-258

 -    one

      two
| <- markup.list.unnumbered.markdown
|^^^^^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-261

Note that at least one space or tab is needed between the list marker
and any following content, so these are not list items:

-one
| <- meta.paragraph.markdown - markup.list
|^^^^ meta.paragraph.markdown - markup.list

2.two
| <- meta.paragraph.markdown - markup.list
|^^^^^ meta.paragraph.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-262

A list item may contain blocks that are separated by more than one blank line.

- foo


  bar
  | <- markup.list.unnumbered.markdown
  |^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-263

1.  foo

    ```
    | <- markup.list.numbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
    bar
    | <- markup.list.numbered.markdown markup.raw.code-fence.markdown-gfm - punctuation
    ```
    | <- markup.list.numbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

    baz
    | <- markup.list.numbered.markdown

    > bam
    | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
    |^^^^^ markup.list.numbered.markdown markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-265

Note that ordered list start numbers must be nine digits or less:

123456789. ok
| <- markup.list.numbered.bullet.markdown
|^^^^^^^^^ markup.list.numbered.bullet.markdown
|         ^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-266

1234567890. not ok
| <- meta.paragraph.markdown - markup.list
|^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-267

0. ok
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-268

003. ok
| <- markup.list.numbered.bullet.markdown
|^^^ markup.list.numbered.bullet.markdown
|  ^ punctuation.definition.list_item.markdown
|   ^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-269

-1. not ok
| <- meta.paragraph.markdown - markup.list
|^^^^^^^^^^ meta.paragraph.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-282

- foo
-   
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^ markup.list.unnumbered.markdown

- foo
-   
- bar
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-283

1. foo
2.
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^ markup.list.numbered.markdown - punctuation

1. foo
2.
3. bar
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^ markup.list.numbered.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-284

*
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^ markup.list.unnumbered.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-285

foo
*
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^ markup.list.unnumbered.markdown - punctuation

foo
1.
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^ markup.list.numbered.markdown - punctuation 

## https://spec.commonmark.org/0.30/#example-286

 1.  A paragraph
     with two lines.
     |^^^^^^^^^^^^^^^ markup.list.numbered.markdown

         indented code (but ST can't reliably highlight it!)
     |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown - markup.raw
     
     > A block quote.
     |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-287

  1.  A paragraph
      with two lines.
      |^^^^^^^^^^^^^^^ markup.list.numbered.markdown

          indented code (but ST can't reliably highlight it!)
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown - markup.raw

      > A block quote.
      | ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-288

   1.  A paragraph
       with two lines.
       |^^^^^^^^^^^^^^^ markup.list.numbered.markdown

            indented code (but ST can't reliably highlight it!)
       |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown - markup.raw

       > A block quote.
       |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-289

    1.  A paragraph
        with two lines.
        |^^^^^^^^^^^^^^^ markup.raw.block.markdown - markup.list

            indented code
        |^^^^^^^^^^^^^^^^^ markup.raw.block.markdown - markup.list

        > A block quote.
        |^^^^^^^^^^^^^^^^ markup.raw.block.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-290

  1.  A paragraph
with two lines.
| <- markup.list.numbered.markdown
|^^^^^^^^^^^^^^^ markup.list.numbered.markdown

          indented code (but ST can't reliably highlight it!)
      |^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown - markup.raw

      > A block quote.
      | ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown

## https://spec.commonmark.org/0.30/#example-291

  1.  A paragraph
    with two lines.
    |^^^^^^^^^^^^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-292

> 1. > Blockquote > text
|    ^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown
|    ^ punctuation.definition.blockquote.markdown
|                 ^ - punctuation

> 1. > Blockquote
continued here.
| <- markup.quote.markdown markup.list.numbered.markdown
|^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-293

> 1. > Blockquote
> continued here.
| <- markup.quote.markdown markup.list.numbered.markdown punctuation.definition.blockquote.markdown
|^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-294

So, in this case we need two spaces indent:

- foo
  - bar
    - baz
      - boo
| <- markup.list.unnumbered.markdown
|^^^^^ markup.list.unnumbered.markdown
|     ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|      ^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-295

One is not enough:

- foo
 - bar
  - baz
   - boo
| <- markup.list.unnumbered.markdown
|^^ markup.list.unnumbered.markdown
|  ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|   ^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-296

Here we need four, because the list marker is wider:

10) foo
    - bar
| <- markup.list.numbered.markdown
|^^^ markup.list.numbered.markdown
|   ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|    ^^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-297

Three is not enough:

10) foo
   - bar
| <- markup.list.numbered.markdown
|^^ markup.list.numbered.markdown
|  ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|   ^^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-298

A list may be the first block in a list item:

- - foo
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^ markup.list.unnumbered.markdown
| ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|  ^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-299

A list may be the first block in a list item:

1. - 2. foo 3. bar
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^ markup.list.numbered.markdown
|  ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|   ^ markup.list.unnumbered.markdown
|    ^^ markup.list.numbered.bullet.markdown
|      ^^^^^^^^^^^^^ markup.list.numbered.markdown - punctuation

## https://spec.commonmark.org/0.30/#example-300

A list item can contain a heading:

- # Foo
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^ markup.list.unnumbered.markdown
| ^^^^^^ markup.heading.1.markdown
| ^ punctuation.definition.heading.begin.markdown
|   ^^^ entity.name.section.markdown


- Should be a setext heading!
  ---
| ^^^ markup.list.unnumbered.markdown meta.separator.thematic-break.markdown punctuation.definition.thematic-break.markdown

- Bar
  ---
  baz
| <- markup.list.unnumbered.markdown
|^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-301

Changing the bullet or ordered list delimiter starts a new list:

- foo
- bar
+ baz
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-302

Changing the bullet or ordered list delimiter starts a new list:

1. foo
2. bar
3) baz
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-303

In CommonMark, a list can interrupt a paragraph. 
That is, no blank line is needed to separate a paragraph from a following list:

Foo
- bar
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

Foo
- bar
- baz
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

## https://spec.commonmark.org/0.30/#example-304

In order to solve of unwanted lists in paragraphs with hard-wrapped numerals, 
we allow only lists starting with 1 to interrupt paragraphs.

The number of windows in my house is
14.  The number of doors is 6.
| <- meta.paragraph.markdown - markup.list
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-305

We may still get an unintended result in cases like

The number of windows in my house is
1.  The number of doors is 6.
| <- markup.list.numbered.bullet.markdown
|^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-306

There can be any number of blank lines between items:

- foo

- bar
  |^^^ markup.list.unnumbered.markdown


- baz
  |^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-307

- foo
  - bar
    - baz


      bim
      |^^^ markup.list.unnumbered.markdown - markup.raw

## https://spec.commonmark.org/0.30/#example-308

To separate consecutive lists of the same type,
you can insert a blank HTML comment:

- foo
- bar

<!-- -->
| <- meta.disable-markdown comment.block.html
|^^^^^^^ meta.disable-markdown comment.block.html

- baz
- bim

## https://spec.commonmark.org/0.30/#example-309

To separate a list from an indented code block that would otherwise 
be parsed as a subparagraph of the final list item,
you can insert a blank HTML comment:

-   foo

    notcode
    |^^^^^^^ markup.list.unnumbered.markdown - markup.raw

-   foo

<!-- -->

    code
    |^^^^ markup.raw.block.markdown - markup.list

## https://spec.commonmark.org/0.30/#example-311

List items need not be indented to the same level.

1. a
   | <- markup.list.numbered.markdown - markup.raw

 2. b
    | <- markup.list.numbered.markdown - markup.raw

  3. c
     | <- markup.list.numbered.markdown - markup.raw

1) a
   | <- markup.list.numbered.markdown - markup.raw

 2) b
    | <- markup.list.numbered.markdown - markup.raw

  3) c
     | <- markup.list.numbered.markdown - markup.raw

## https://spec.commonmark.org/0.30/#example-313

And here, `3. c` should be treated as in indented code block, 
because it is indented four spaces and preceded by a blank line.

1. a
   | <- markup.list.numbered.markdown - markup.raw

  2. b
     | <- markup.list.numbered.markdown - markup.raw

    3. c
       | <- markup.list.numbered.markdown - markup.raw

1) a
   | <- markup.list.numbered.markdown - markup.raw

  2) b
     | <- markup.list.numbered.markdown - markup.raw

    3) c
       | <- markup.list.numbered.markdown - markup.raw

> Note: ST's syntax engine and the implementation of this syntax don't support that.

## https://spec.commonmark.org/0.30/#example-314

This is a loose list, because there is a blank line between two of the list items:

- a
- b

- c
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-315

So is this, with a empty second item:

* a
*
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^ markup.list.unnumbered.markdown
* c
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^ markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-317

- a
- b [ref]
  | ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown

  [ref]: /url
  | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
  |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
  |^^^ entity.name.reference.link.markdown
  |   ^ punctuation.definition.reference.end.markdown
  |    ^ punctuation.separator.key-value.markdown
  |      ^^^^ markup.underline.link.markdown
- d
  | <- markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-318

- a
- ```
  | <- markup.list.unnumbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
  |^^ markup.list.unnumbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
  b
  | <- markup.list.unnumbered.markdown markup.raw.code-fence.markdown-gfm


  ```
  | <- markup.list.unnumbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
  |^^ markup.list.unnumbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

- a
- ```
  b


  ```
- c
  | <- markup.list.unnumbered.markdown - markup.raw

## https://spec.commonmark.org/0.30/#example-319

- a
  - b

    c
    | <- markup.list.unnumbered.markdown
- d
  | <- markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-320

* a
  > b
  >
  | <- markup.list.unnumbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
  |^ markup.list.unnumbered.markdown markup.quote.markdown - punctuation

* a
  > b
  >
* c
  | <- markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-321

- a
  > b
  ```
  | <- markup.list.unnumbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
  |^^ markup.list.unnumbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
  c
  ```
  | <- markup.list.unnumbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
  |^^ markup.list.unnumbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

- a
  > b
  ```
  c
  ```
- d
  | <- markup.list.unnumbered.markdown

## https://spec.commonmark.org/0.30/#example-324

1. ```
   | <- markup.list.numbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
   |^^ markup.list.numbered.markdown meta.code-fence.definition.begin.text.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
   foo
   | <- markup.list.numbered.markdown markup.raw.code-fence.markdown-gfm
   ```
   | <- markup.list.numbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
   |^^ markup.list.numbered.markdown meta.code-fence.definition.end.text.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

   bar
   | <- markup.list.numbered.markdown

## https://spec.commonmark.org/0.30/#example-325

* foo
  * bar

  baz
  | <- markup.list.unnumbered.markdown
  |^^^ markup.list.unnumbered.markdown

## https://custom-tests/list-blocks/gfm-tasks

* [ ] Unticked GitHub-flavored-markdown checkbox
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

* [X] Another ticked checkbox
    + [ ] Sub-item with checkbox
|     ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|      ^ markup.checkbox.mark.markdown-gfm - punctuation
|       ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm

* [] Not a checkbox
| ^^ - markup.checkbox

* [/] Not a checkbox
| ^^^ - markup.checkbox

* Not [ ] a [x] checkbox [X]
| ^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.checkbox

* [ ] [Checkbox][] with next word linked
| ^ markup.checkbox.begin.markdown-gfm punctuation.definition.checkbox.begin.markdown-gfm
|  ^ markup.checkbox.mark.markdown-gfm - punctuation
|   ^ markup.checkbox.end.markdown-gfm punctuation.definition.checkbox.end.markdown-gfm
|     ^^^^^^^^^^^^ meta.link

## https://custom-tests/list-blocks/items-with-thematic-breaks

- * * * * * * *
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.separator.thematic-break.markdown
| ^ punctuation.definition.thematic-break
|  ^ - punctuation
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation

- * * * * * * *
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

- - * * * * * *
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
| ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|  ^ - punctuation
|   ^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.separator.thematic-break.markdown
|   ^ punctuation.definition.thematic-break
|    ^ - punctuation
|     ^ punctuation.definition.thematic-break
|      ^ - punctuation
|       ^ punctuation.definition.thematic-break
|        ^ - punctuation
|         ^ punctuation.definition.thematic-break
|          ^ - punctuation
|           ^ punctuation.definition.thematic-break
|            ^ - punctuation
|             ^ punctuation.definition.thematic-break
|              ^ - punctuation

- - * * * * * *
    still a list item
|   ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

1. * * * * * * *
| <- markup.list.numbered.bullet.markdown
|  ^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.separator.thematic-break.markdown
|  ^ punctuation.definition.thematic-break
|   ^ - punctuation
|    ^ punctuation.definition.thematic-break
|     ^ - punctuation
|      ^ punctuation.definition.thematic-break
|       ^ - punctuation
|        ^ punctuation.definition.thematic-break
|         ^ - punctuation
|          ^ punctuation.definition.thematic-break
|           ^ - punctuation
|            ^ punctuation.definition.thematic-break
|             ^ - punctuation
|              ^ punctuation.definition.thematic-break
|               ^ - punctuation

1. * * * * * * *
   still a list item
|  ^^^^^^^^^^^^^^^^^^ markup.list.numbered

## https://custom-tests/list-blocks/items-with-atx-headings

* list item
# global heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.list
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown - markup.list

* list item
 # global heading (matched as list item heading)
 | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
 |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown

* list item
  # list item heading
  | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown
* list item
  ## list item heading
  | <- markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
  |^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.2.markdown
  + list item
    ### list item heading
    | <- markup.list.unnumbered.markdown markup.heading.3.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.3.markdown
    + list item
      #### list item heading
      | <- markup.list.unnumbered.markdown markup.heading.4.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.4.markdown

* 
  # list item heading
  | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  
  + 
    # list item heading
    | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  
    - 
      # list item heading 1
      | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  

      ## list item heading 2
      | <- markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.2.markdown

* 

  # list item heading
  | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  

  + 

    # list item heading
    | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  

    - 

      # list item heading 1
      | <- markup.list.unnumbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.1.markdown  

      ## list item heading 2
      | <- markup.list.unnumbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown markup.heading.2.markdown

1. list item
# global heading
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown - markup.list
|^^^^^^^^^^^^^^^^ markup.heading.1.markdown - markup.list

2. list item
 # global heading (matched as list item heading)
 | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
 |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

3. list item
   # list item heading
   | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
   1. list item
      # list item heading
      | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
      1. list item
         # list item heading
         | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
   2. list item
      # list item heading
      | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
      1. list item
         # list item heading
         | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

1. 
   # list item heading
   | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
   1. 
      # list item heading
      | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown
      1. 
         # list item heading
         | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

         ## list item heading 2
         | <- markup.list.numbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.2.markdown

1. 

   # list item heading
   | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
   |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

   1. 

      # list item heading
      | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
      |^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

      1. 

         # list item heading 1
         | <- markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

         ## list item heading 2
         | <- markup.list.numbered.markdown markup.heading.2.markdown punctuation.definition.heading.begin.markdown
         |^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.2.markdown

## https://custom-tests/list-blocks/items-with-fenced-code-blocks-indented-by-tabs

  * foo
	```xml
|^^^ markup.list.unnumbered.markdown meta.code-fence.definition.begin.xml.markdown-gfm punctuation.definition.raw.code-fence.begin.markdown
|    ^^ markup.list.unnumbered.markdown meta.code-fence.definition.begin.xml.markdown-gfm constant.other.language-name.markdown
	<tag>
|^^^^^ markup.list.unnumbered.markdown markup.raw.code-fence.xml.markdown-gfm text.xml meta.tag.xml
	```
|^^^ markup.list.unnumbered.markdown meta.code-fence.definition.end.xml.markdown-gfm punctuation.definition.raw.code-fence.end.markdown

## https://custom-tests/list-blocks/items-with-html-blocks

* list item
  
  <p>*no-markdown*</p>
  |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown - meta.paragraph
  |               ^^^^ meta.tag

  + sub item

    <p>*no-markdown*</p>
    |^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown - meta.paragraph
    |               ^^^^ meta.tag

    <style>
        h1 {
            font-family: Helvetica;
        |^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown source.css.embedded.html meta.property-list.css
        }

        p {
            font-family: "Ubuntu Sans";
        |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown source.css.embedded.html meta.property-list.css
        }
    </style>
    | <- markup.list.unnumbered.markdown meta.disable-markdown meta.tag.style.end.html punctuation.definition.tag.begin.html
    |^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown meta.tag.style.end.html
    |       ^ markup.list.unnumbered.markdown meta.disable-markdown - mata.tag

    Further sub item text.
    | <- markup.list.unnumbered.markdown
    |^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown

  + sub item
    <p>
    | <- markup.list.unnumbered.markdown meta.disable-markdown meta.tag
    |^^ markup.list.unnumbered.markdown meta.disable-markdown meta.tag
      *no-markodwn*
    |^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown - markup.italic
    </p>
    - not a list item
    | <- markup.list.unnumbered.markdown meta.disable-markdown - punctuation
    |^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.disable-markdown - punctuation

## https://custom-tests/list-blocks/items-with-reference-definitions

* list item [ref]
  |         ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown

  + sub item [ref]
    |        ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown
  
    [ref]: /url
    | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
    |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
    |^^^ entity.name.reference.link.markdown
    |   ^ punctuation.definition.reference.end.markdown
    |    ^ punctuation.separator.key-value.markdown
    |      ^^^^ markup.underline.link.markdown

    - sub item [ref]
      |        ^^^^^ markup.list.unnumbered.markdown meta.link.reference.description.markdown
    
      [ref]: /url
      | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
      |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
      |^^^ entity.name.reference.link.markdown
      |   ^ punctuation.definition.reference.end.markdown
      |    ^ punctuation.separator.key-value.markdown
      |      ^^^^ markup.underline.link.markdown
 
      [ref]:
      /url
      | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown
      |^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown

      [ref]: /url
      "title"
      | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown
      |^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown

      [ref]: /url
      no title
      | <- markup.list.unnumbered.markdown meta.paragraph.list.markdown - meta.link
      |^^^^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown - meta.link

  [ref]: /url
  | <- markup.list.unnumbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
  |^^^^^^^^^^^ markup.list.unnumbered.markdown meta.link.reference.def.markdown
  |^^^ entity.name.reference.link.markdown
  |   ^ punctuation.definition.reference.end.markdown
  |    ^ punctuation.separator.key-value.markdown
  |      ^^^^ markup.underline.link.markdown

1. list item [ref]
   |         ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown

   2. sub item [ref]
      |        ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown
    
      [ref]: /url
      | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
      |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
      |^^^ entity.name.reference.link.markdown
      |   ^ punctuation.definition.reference.end.markdown
      |    ^ punctuation.separator.key-value.markdown
      |      ^^^^ markup.underline.link.markdown

      3. sub item [ref]
         |        ^^^^^ markup.list.numbered.markdown meta.link.reference.description.markdown
       
         [ref]: /url
         | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
         |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
         |^^^ entity.name.reference.link.markdown
         |   ^ punctuation.definition.reference.end.markdown
         |    ^ punctuation.separator.key-value.markdown
         |      ^^^^ markup.underline.link.markdown

         [ref]:
         /url
         | <- markup.list.numbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown
         |^^^ markup.list.numbered.markdown meta.link.reference.def.markdown markup.underline.link.markdown

         [ref]: /url
         "title"
         | <- markup.list.numbered.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown
         |^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown meta.string.title.markdown string.quoted.double.markdown

         [ref]: /url
         no title
         | <- markup.list.numbered.markdown meta.paragraph.list.markdown - meta.link
         |^^^^^^^^ markup.list.numbered.markdown meta.paragraph.list.markdown - meta.link

   [ref]: /url
   | <- markup.list.numbered.markdown meta.link.reference.def.markdown punctuation.definition.reference.begin.markdown
   |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.markdown
   |^^^ entity.name.reference.link.markdown
   |   ^ punctuation.definition.reference.end.markdown
   |    ^ punctuation.separator.key-value.markdown
   |      ^^^^ markup.underline.link.markdown

## https://custom-tests/list-blocks/items-with-footnote-definitions

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
| <- markup.list.numbered.markdown meta.link.reference.def.footnote.markdown-extra
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.link.reference.def.footnote.markdown-extra

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
       [^2]:
       ^^^^^^ markup.list.numbered.markdown meta.link.reference.def.footnote.markdown-extra
       ^ punctuation.definition.reference.begin.markdown
        ^^ entity.name.reference.link.markdown
          ^ punctuation.definition.reference.end.markdown
           ^ punctuation.separator.key-value.markdown

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
       # header
|^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.heading.1.markdown

1. list item
   + sub item
     - sub item [^1]
     
       [^1]:
           This is a foot note
           with a second line
     - sub item
|^^^^^^^^^^^^^^ markup.list.numbered.markdown
|    ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

## https://custom-tests/list-blocks/items-with-line-continuation

* list item
second line
| <- markup.list.unnumbered.markdown
  + subitem
second line
| <- markup.list.unnumbered.markdown
    - subitem
second line
| <- markup.list.unnumbered.markdown
      - subitem
second line
| <- markup.list.unnumbered.markdown

paragraph
| <- meta.paragraph.markdown

1. list item
second line
| <- markup.list.numbered.markdown
   2. subitem
second line
| <- markup.list.numbered.markdown
      3. subitem
second line
| <- markup.list.numbered.markdown
         4. subitem
second line
| <- markup.list.numbered.markdown

paragraph
| <- meta.paragraph.markdown

1. list item
second line
| <- markup.list.numbered.markdown
   + subitem
second line
| <- markup.list.numbered.markdown
     - subitem
second line
| <- markup.list.numbered.markdown
       - subitem
second line
| <- markup.list.numbered.markdown

paragraph
| <- meta.paragraph.markdown

## https://custom-tests/list-blocks/items-with-block-quotes/basics

* list item

   > This is a blockquote.
   | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

  + subitem

    > This is a blockquote.
    | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

    - subitem
  
      > This is a blockquote.
      | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

      - subitem
    
        > This is a blockquote.
        | <- markup.list.unnumbered markup.quote punctuation.definition.blockquote

  This is a paragraph still part of the 
  list item
 |^^^^^^^^^^ markup.list.unnumbered.markdown - meta.paragraph meta.paragraph

1. list item

   > This is a blockquote.
   | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown

   2. subitem

      > This is a blockquote.
      | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
    
      3. subitem
    
         > This is a blockquote.
         | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown

   This is a paragraph still part of the 
   list item
   |^^^^^^^^^ markup.list.numbered.markdown - meta.paragraph meta.paragraph

## https://custom-tests/list-blocks/items-with-block-quotes/block-quote-terminations

1. item
   + item
     - item
       > Block quote followed by heading
       # heading
       | <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
       |^^^^^^^^^ markup.heading.1.markdown - meta.quote
       | ^^^^^^^ entity.name.section.markdown

       > Block quote followed by unordered list
       * list item
       | <- markup.list.numbered.markdown markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
       |^^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

       > Block quote followed by unordered list
       + list item
       | <- markup.list.numbered.markdown markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
       |^^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

       > Block quote followed by unordered list
       - list item
       | <- markup.list.numbered.markdown markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
       |^^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

       > Block quote followed by ordered list
       1. list item
       | <- markup.list.numbered.markdown markup.list.numbered.bullet.markdown
       |^ markup.list.numbered.markdown markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
       | ^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

       > Block quote followed by ordered list
       2. list item
       | <- markup.list.numbered.bullet.markdown - punctuation
       |^ markup.list.numbered.bullet.markdown punctuation.definition.list_item.markdown
       | ^^^^^^^^^^ markup.list.numbered.markdown - meta.quote

       > Block quote followed by invalid list
       1234567890. no list item
       | <- markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown
       |^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown

       > Block quote followed by html block
       <p>*no-markdown</p>
       | <- meta.disable-markdown meta.tag.block
       |^^^^^^^^^^^^^^^^^^^ meta.disable-markdown

## https://custom-tests/list-blocks/items-with-block-quotes/headings-and-paragraphs

1. item
   + item
     - item
       > # Foo
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^ markup.quote.markdown - markup.heading
       | ^^^^^^ markup.quote.markdown markup.heading.1.markdown
       | ^ punctuation.definition.heading.begin.markdown
       |   ^^^ entity.name.section.markdown
       
       > # Foo
       bar
       | <- meta.paragraph.list.markdown - markup.quote
       |^^ meta.paragraph.list.markdown - markup.quote
       
       > # Foo
       > bar
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^ markup.quote.markdown
       
       > # Foo
       > bar
       > baz
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^ markup.quote.markdown

       ># Foo
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^^ markup.quote.markdown markup.heading.1.markdown
       |^ punctuation.definition.heading.begin.markdown
       |  ^^^ entity.name.section.markdown
       
       ># Foo
       >bar
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^ markup.quote.markdown
       
       ># Foo
       >bar
       > baz
       | <- markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^ markup.quote.markdown

## https://custom-tests/list-blocks/items-with-block-quotes/paragraphs-vs-codeblocks

1. item
   + item
     - item
       >foo 1
       >foo 2
       |^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown
       
       > foo 1
       > foo 2
       | ^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown
       
       >  foo 1
       >  foo 2
       | ^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown
       
       >   foo 1
       >   foo 2
       | ^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.paragraph.markdown

       >       foo 1
       >       foo 2
       | ^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.raw.block.markdown

## https://custom-tests/list-blocks/items-with-nested-block-quotes

1. item
   + item
     - item
       > > Nested block quote
       | <- markup.quote punctuation.definition.blockquote
       | ^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown
       |^ - punctuation
       | ^ punctuation.definition.blockquote
       |  ^ - punctuation
       
       > > Nested quote
       > Followed by more quoted text that is not nested
       | <- markup.quote punctuation.definition.blockquote - markup.quote markup.quote
       
       >    > this is a nested quote but no code in a block quote
       | <- punctuation.definition.blockquote
       |    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown
       
       >    > this is a nested quote but no code in a block quote
       >     > with a second line of content
       | <- punctuation.definition.blockquote
       |^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.quote.markdown markup.paragraph.markdown
       |     ^ - punctuation
       
       >     > this is code in a block quote, not a nested quote
       | <- punctuation.definition.blockquote
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.block - markup.quote markup.quote

## https://custom-tests/list-blocks/items-with-block-quotes/list-blocks

1. item
   + item
     - item
       > Block
       > 1. item
       | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown
       | ^^ markup.list.numbered.bullet.markdown

       > Block
       > 1. item
       >    + item
       | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.list.numbered.markdown
       |    ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

       > Block
       > 1. item
       >    + item
       >      - item
       | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.list.numbered.markdown
       |      ^ markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown

       > Block
       > 1. item
       >    + item
       >      - item
       >        > quote
       >        > quote
       | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
       |^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.list.numbered.markdown meta.paragraph.list.markdown
       |        ^ punctuation.definition.blockquote.markdown

       > Block
       > 1. item
       >    + item
       >      - item
       >      # heading
              | <- markup.list.numbered.markdown markup.quote.markdown markup.list.numbered.markdown markup.heading.1.markdown punctuation.definition.heading.begin.markdown
       > # heading
       | <- markup.list.numbered.markdown markup.quote.markdown punctuation.definition.blockquote.markdown
       |^ markup.list.numbered.markdown markup.quote.markdown - markup.heading
       | ^^^^^^^^^^ markup.list.numbered.markdown markup.quote.markdown markup.heading.1.markdown
       | ^ punctuation.definition.heading.begin.markdown
       |   ^^^^^^^ entity.name.section.markdown

## https://custom-tests/list-blocks/items-with-code-spans

- `<foo>` | `<bar>` (foo/bar.baz)
- `<foo>` | `<my-bar>` | (foo/bar-baz.foo)
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown - markup.table

1. Open `Command Palette` using menu item `Tools → Command Palette...`
   |    ^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.raw.inline.markdown
   |                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.raw.inline.markdown
2. Choose `Package Control: Install Package`
   |      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown markup.raw.inline.markdown

## https://custom-tests/list-blocks/items-with-emphasis

- test *testing
blah*
|   ^ markup.list.unnumbered markup.italic punctuation.definition.italic.end
- fgh
- *ghgh
| ^ markup.list.unnumbered markup.italic punctuation.definition.italic.begin
- fgfg
| <- markup.list.unnumbered.bullet punctuation.definition.list_item
- _test

| <- markup.list.unnumbered markup.italic invalid.illegal.non-terminated.bold-italic
  still a list item
| ^^^^^^^^^^^^^^^^^^ markup.list.unnumbered

## https://custom-tests/list-blocks/items-with-inline-html-tags

- `code` - <a name="demo"></a>
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown
| ^^^^^^ markup.raw.inline.markdown
| ^ punctuation.definition.raw.begin.markdown
|      ^ punctuation.definition.raw.end.markdown
|        ^ - punctuation
|          ^^^^^^^^^^^^^^^^^^^ meta.tag.inline.a.html 

- list item

  <span>*no-markdown*</span>
  |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown
  |                  ^^^^^^^ meta.tag

  - list item
  
    <span>*no-markdown*</span>
    |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown
    |                  ^^^^^^^ meta.tag

    - list item
      
      <span>*no-markdown*</span>
      |^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.unnumbered.markdown meta.paragraph.list.markdown
      |                  ^^^^^^^ meta.tag

## https://custom-tests/list-blocks/items-with-links-and-references

 1. [see `demo`](#demo "demo")
    | <- markup.list.numbered.markdown meta.link.inline.description.markdown punctuation.definition.link.begin.markdown
    |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.description.markdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.metadata.markdown
    |           ^ punctuation.definition.metadata.begin.markdown
    |                  ^ punctuation.definition.string.begin.markdown
    |                       ^ punctuation.definition.string.end.markdown
    |                        ^ punctuation.definition.metadata.end.markdown

    [see `demo`](#demo (demo))
    | <- markup.list.numbered.markdown meta.link.inline.description.markdown punctuation.definition.link.begin.markdown
    |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.description.markdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.metadata.markdown
    |           ^ punctuation.definition.metadata.begin.markdown
    |                  ^ punctuation.definition.string.begin.markdown
    |                       ^ punctuation.definition.string.end.markdown
    |                        ^ punctuation.definition.metadata.end.markdown

    [see `demo`](#demo 'demo')
    | <- markup.list.numbered.markdown meta.link.inline.description.markdown punctuation.definition.link.begin.markdown
    |^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.description.markdown
    |           ^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.link.inline.metadata.markdown
    |           ^ punctuation.definition.metadata.begin.markdown
    |                  ^ punctuation.definition.string.begin.markdown
    |                       ^ punctuation.definition.string.end.markdown
    |                        ^ punctuation.definition.metadata.end.markdown

    Here is a ![example image](https://test.com/sublime.png "A demonstration").
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.description.markdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.metadata.markdown
    |                                                                         ^^ markup.list.numbered.markdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown
    |                        ^ punctuation.definition.image.end.markdown
    |                         ^ punctuation.definition.metadata.begin.markdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.double.markdown
    |                                                       ^ punctuation.definition.string.begin.markdown
    |                                                                       ^ punctuation.definition.string.end.markdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown

    Here is a ![example image](https://test.com/sublime.png 'A demonstration').
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.description.markdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.metadata.markdown
    |                                                                         ^^ markup.list.numbered.markdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown
    |                        ^ punctuation.definition.image.end.markdown
    |                         ^ punctuation.definition.metadata.begin.markdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.single.markdown
    |                                                       ^ punctuation.definition.string.begin.markdown
    |                                                                       ^ punctuation.definition.string.end.markdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown

    Here is a ![example image](https://test.com/sublime.png (A demonstration)).
    |         ^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.description.markdown
    |                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.list.numbered.markdown meta.image.inline.metadata.markdown
    |                                                                         ^^ markup.list.numbered.markdown - meta.image
    |         ^^ punctuation.definition.image.begin.markdown
    |                        ^ punctuation.definition.image.end.markdown
    |                         ^ punctuation.definition.metadata.begin.markdown
    |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
    |                                                       ^^^^^^^^^^^^^^^^^ string.quoted.other.markdown
    |                                                       ^ punctuation.definition.string.begin.markdown
    |                                                                       ^ punctuation.definition.string.end.markdown
    |                                                                        ^ punctuation.definition.metadata.end.markdown


# TEST: CODE SPANS ############################################################

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

## https://spec.commonmark.org/0.30/#example-327

`hi`lo`
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^ markup.raw.inline.markdown
|  ^ punctuation.definition.raw.end.markdown
|   ^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-328

`foo`
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^ meta.paragraph.markdown markup.raw.inline.markdown
|   ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-329

`` foo ` bar  ``
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^^^^^^^^^^ markup.raw.inline.markdown
|^ punctuation.definition.raw.begin.markdown
|      ^ - punctuation
|             ^^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-330

` `` `
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^ markup.raw.inline.markdown
| ^^ - punctuation
|    ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-331

`  ``  `
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^^ markup.raw.inline.markdown
|  ^^ - punctuation
|      ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-332

` a`
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^ markup.raw.inline.markdown
|  ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-333

` b `
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^ markup.raw.inline.markdown
|   ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-334

` `
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^ markup.raw.inline.markdown
| ^ punctuation.definition.raw.end.markdown
|  ^ - markup 

`  `
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^ markup.raw.inline.markdown
|  ^ punctuation.definition.raw.end.markdown
|   ^ - markup 

## https://spec.commonmark.org/0.30/#example-335

``
foo
bar  
baz
``
| <- markup.raw.inline.markdown punctuation.definition.raw.end.markdown
|^ markup.raw.inline.markdown punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-336

``
foo 
``
| <- markup.raw.inline.markdown punctuation.definition.raw.end.markdown
|^ markup.raw.inline.markdown punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-337

`foo   bar
  baz`
|^^^^^ markup.raw.inline.markdown
|    ^ punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-338

`foo\`bar`
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^ markup.raw.inline.markdown
|     ^^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-339

``foo`bar``
| <- meta.paragraph.markdown markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^^^^^ meta.paragraph.markdown markup.raw.inline.markdown
|^ punctuation.definition.raw.begin.markdown
| ^^^^^^^ - punctuation
|        ^^ punctuation.definition.raw.end.markdown

````bar```` baz
|^^^^^^^^^^ markup.raw.inline.markdown
|          ^^^^^ - markup.raw

## https://spec.commonmark.org/0.30/#example-340

`foo `` bar`
| <- markup.raw.inline.markdown punctuation.definition.raw.begin.markdown
|^^^^^^^^^^ markup.raw.inline.markdown - punctuation
|          ^ markup.raw.inline.markdown punctuation.definition.raw.end.markdown

## https://spec.commonmark.org/0.30/#example-341

*foo`*`
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|   ^^^ markup.italic.markdown markup.raw.inline.markdown

| <- invalid.illegal.non-terminated.bold-italic

## https://spec.commonmark.org/0.30/#example-342

[not a `link](/foo`)
|^^^^^^^^^^^^^^^^^^^ - meta.link
|      ^^^^^^^^^^^^ markup.raw.inline.markdown

## https://spec.commonmark.org/0.30/#example-343

`<a href="`">`
|^^^^^^^^^^ markup.raw.inline.markdown
|          ^^ - markup.raw

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-344

<a href="`">`
| ^^^^^^^^^ meta.tag.inline.a
|           ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-345

`<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^ markup.raw.inline
|                     ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw

## https://spec.commonmark.org/0.30/#example-346

<http://foo.bar.`baz>`
|^^^^^^^^^^^^^^^^^^^ markup.underline.link
|                    ^ punctuation.definition.raw.begin

| <- invalid.illegal.non-terminated.raw


# TEST: EMPHASIS ##############################################################

## https://spec.commonmark.org/0.30/#example-350

*foo bar*
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^ markup.italic.markdown
|       ^ punctuation.definition.italic.end

## https://spec.commonmark.org/0.30/#example-351

This is not emphasis, because the opening `*` is followed by whitespace, and hence not part of a left-flanking delimiter run:

a * foo bar*
| ^^^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-352

a*"foo"*
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-353

* a *
| <- markup.list.unnumbered.bullet.markdown punctuation.definition.list_item.markdown - markup.italic
|^^^^^ markup.list.unnumbered.markdown - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-354

Intraword emphasis with `*` is permitted:

foo*bar*
| <- - markup.italic
|^^ - markup.italic
|  ^^^^^ markup.italic.markdown
|  ^ punctuation.definition.italic.begin.markdown
|      ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-355

5*6*78
| <- - markup.italic
|^^^ markup.italic.markdown
|^ punctuation.definition.italic.begin.markdown
|  ^ punctuation.definition.italic.end.markdown
|   ^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-356

_foo bar_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^ meta.paragraph.markdown markup.italic.markdown
|       ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-357

This is not emphasis, because the opening `_` is followed by whitespace:

_ foo bar_
| <- - markup.italic - punctuation
|^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-358

This is not emphasis, because the opening `_` is preceded by an alphanumeric and followed by punctuation:

a_"foo"_
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-359

Emphasis with `_` is not allowed inside words:

foo_bar_
| <- - markup.italic - punctuation
|^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-360

5_6_78
| <- - markup.italic - punctuation
|^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-361

пристаням_стремятся_
| <- - markup.italic - punctuation
|^^^^^^^^^^^^^^^^^^^ - markup.italic - punctuation

## https://spec.commonmark.org/0.30/#example-362

Here `_` does not generate emphasis, because the first delimiter run is right-flanking
and the second left-flanking:

aa_"bb"_cc
| <- - markup.italic - punctuation
|^^^^^^ - markup.italic - punctuation

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-363

This is emphasis, even though the opening delimiter is both left- and right-flanking,
because it is preceded by punctuation:

foo-_(bar)_
| <- - markup.italic - punctuation
|^^^ - markup.italic - punctuation
|   ^^^^^^^ markup.italic.markdown
|   ^ punctuation.definition.italic.begin.markdown
|         ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-365

This is not emphasis, because the closing `*` is preceded by whitespace:

*foo bar *
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^ markup.italic.markdown

| <- markup.italic.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-366

A line ending also counts as whitespace:

*foo bar *
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^ markup.italic.markdown
|        ^ - punctuation
*
| <- markup.italic.markdown - punctuation
abc*
| <- markup.italic.markdown
|^^^ meta.paragraph.markdown markup.italic.markdown
|  ^ punctuation.definition.italic.end.markdown
|   ^ - markup.italic

## https://spec.commonmark.org/0.30/#example-367

This is not emphasis, because the second `*` is preceded by punctuation and followed
by an alphanumeric (hence it is not part of a right-flanking delimiter run):

*(*foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-368

The point of this restriction is more easily appreciated with this example:

*(*foo*)*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-369

Intraword emphasis with `*` is allowed:

*foo*bar
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^ markup.italic.markdown
|   ^ punctuation.definition.italic.end.markdown
|    ^^^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-370

This is not emphasis, because the closing `_` is preceded by whitespace:

_foo bar _
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^ markup.italic.markdown
|        ^ - punctuation

| <- markup.italic.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

_foo bar _
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^ markup.italic.markdown
|        ^ - punctuation
_
| <- markup.italic.markdown - punctuation
abc_
| <- markup.italic.markdown
|^^^ markup.italic.markdown
|  ^ punctuation.definition.italic.end
|   ^ - markup.italic

## https://spec.commonmark.org/0.30/#example-371

This is not emphasis, because the second `_` is preceded by punctuation and followed
by an alphanumeric (hence it is not part of a right-flanking delimiter run):

_(_foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-371

The point of this restriction is more easily appreciated with this example:

_(_foo_)_

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-373

Intraword emphasis is disallowed for `_`:

_foo_bar
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^ markup.italic.markdown
|   ^ - punctuation
abc_
| <- markup.italic.markdown
|^^^ markup.italic.markdown
|  ^ punctuation.definition.italic.end.markdown
|   ^ - markup.italic

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-374

Intraword emphasis is disallowed for `_`:

_пристаням_стремятся
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^^^^^^^^^^ markup.italic.markdown

| <- markup.italic.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-375

_foo_bar_baz_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^^ markup.italic.markdown
|   ^^^^^ - punctuation
|           ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-376

This is emphasis, even though the closing delimiter is both left- and right-flanking,
because it is followed by punctuation:

_(bar)_.
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^ markup.italic.markdown
|     ^ punctuation.definition.italic.end.markdown
|      ^^ - markup.italic

## https://spec.commonmark.org/0.30/#example-377

**foo bar**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown
|        ^^ punctuation.definition.bold.end.markdown

## https://spec.commonmark.org/0.30/#example-378

** foo bar**
| <- - markup - punctuation
|^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-379

This is not strong emphasis, because the opening `**` is preceded by an alphanumeric
and followed by punctuation, and hence not part of a left-flanking delimiter run:

a**"foo"**
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-380

Intraword strong emphasis with `**` is permitted:

foo**bar**
| <- - markup
|^^ - markup
|  ^^^^^^^ meta.paragraph.markdown markup.bold.markdown
|  ^^ punctuation.definition.bold.begin.markdown
|       ^^ punctuation.definition.bold.end.markdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-381

__foo bar__
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown
|        ^^ punctuation.definition.bold.end.markdown

## https://spec.commonmark.org/0.30/#example-382

This is not strong emphasis, because the opening delimiter is followed by whitespace:
__ foo bar__
| <- - markup - punctuation
|^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-383

__
| <- - punctuation
|^ - punctuation

## https://spec.commonmark.org/0.30/#example-384

a__"foo"__
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-385

Intraword strong emphasis is forbidden with `__`:
foo__bar__
| <- - markup - punctuation
|^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-386

5__6__78
| <- - markup - punctuation
|^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-387

пристаням__стремятся__
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-389

foo-__(bar)__
| <- - markup
|^^^ - markup
|   ^^^^^^^^^ markup.bold.markdown
|   ^^ punctuation.definition.bold.begin.markdown
|          ^^ punctuation.definition.bold.end.markdown
|            ^ - markup

## https://spec.commonmark.org/0.30/#example-390

**foo bar **
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|         ^^ - punctuation

| <- markup.bold.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-394

**foo "*bar*" foo**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^ markup.bold.markdown - markup.italic
|^ punctuation.definition.bold.begin.markdown
|      ^^^^^ markup.bold.markdown markup.italic.markdown
|      ^ punctuation.definition.italic.begin.markdown
|          ^ punctuation.definition.italic.end.markdown
|           ^^^^^^^ markup.bold.markdown - markup.italic
|                ^^ punctuation.definition.bold.end.markdown
|                  ^ - markup

## https://spec.commonmark.org/0.30/#example-395

Intraword emphasis:
 
**foo**bar
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^ markup.bold.markdown
|    ^^ punctuation.definition.bold.end.markdown
|      ^^^^ - markup

## https://spec.commonmark.org/0.30/#example-396

__foo bar __
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|         ^^ - punctuation

| <- markup.bold.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-397

This is not strong emphasis, because the second `__` 
is preceded by punctuation and followed by an alphanumeric:

__(__foo)

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-398

_(__foo__)_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
| ^^^^^^^ markup.italic.markdown markup.bold.markdown
| ^^ punctuation.definition.bold.begin.markdown
|      ^^ punctuation.definition.bold.end.markdown
|         ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-399

Intraword strong emphasis is forbidden with `__`:
__foo__bar
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|    ^^ - punctuation

| <- markup.bold.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-400

__пристаням__стремятся
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|          ^^ - punctuation

| <- markup.bold.markdown invalid.illegal.non-terminated.bold-italic.markdown

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-401

__foo__bar__baz__
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|    ^^^^^^^ - punctuation
|              ^^ punctuation.definition.bold.end.markdown

## https://spec.commonmark.org/0.30/#example-402

This is strong emphasis, even though the closing delimiter is both left- and right-flanking,
because it is followed by punctuation:

__(bar)__.
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown 
|      ^^ punctuation.definition.bold.end.markdown
|        ^^ - markup

## https://spec.commonmark.org/0.30/#example-403

Any nonempty sequence of inline elements can be the contents of an emphasized span.

*foo [bar](/url)*
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^^^^^^^^^^^^ markup.italic.markdown
|    ^^^^^^^^^^^ meta.link.inline
|               ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-404

*foo
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^ markup.italic.markdown
bar*
| <- markup.italic.markdown
|^^^ markup.italic.markdown
|  ^ punctuation.definition.italic.end
|   ^ - markup

## https://spec.commonmark.org/0.30/#example-405

_foo __bar__ baz_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^ markup.italic.markdown - markup markup
|    ^^ punctuation.definition.bold.begin.markdown
|    ^^^^^^^ markup.italic.markdown markup.bold.markdown
|         ^^ punctuation.definition.bold.end.markdown
|           ^^^^^ markup.italic.markdown - markup markup
|               ^ punctuation.definition.italic.end.markdown
|                ^ - markup

## https://spec.commonmark.org/0.30/#example-418

*foo [*bar*](/url)*
| <-  markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^ markup.italic.markdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown markup.italic.markdown
|          ^^^^^^^ markup.italic.markdown - markup.italic markup.italic

*foo [_bar_](/url)*
| <-  markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^ markup.italic.markdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown markup.italic.markdown
|          ^^^^^^^ markup.italic.markdown - markup.italic markup.italic

_foo [_bar_](/url)_
| <-  markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^ markup.italic.markdown - markup.italic markup.italic
|    ^^^^^^^^^^^^^ meta.link.inline
|     ^^^^^ markup.italic.markdown markup.italic.markdown
|          ^^^^^^^ markup.italic.markdown - markup.italic markup.italic

_foo [**bar**](/url)_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^ markup.italic.markdown - markup.italic markup.bold
|    ^^^^^^^^^^^^^^^ meta.link.inline
|     ^^ punctuation.definition.bold.begin.markdown
|     ^^^^^^^ markup.italic.markdown markup.bold.markdown
|          ^^ punctuation.definition.bold.end.markdown
|            ^^^^^^^^ markup.italic.markdown - markup.italic markup.bold
|                   ^ punctuation.definition.italic.end.markdown

_foo [__bar__](/url)_
| <- markup.italic.markdown punctuation.definition.italic.begin.markdown
|^^^^^ markup.italic.markdown - markup.italic markup.bold
|    ^^^^^^^^^^^^^^^ meta.link.inline
|     ^^ punctuation.definition.bold.begin.markdown
|     ^^^^^^^ markup.italic.markdown markup.bold.markdown
|          ^^ punctuation.definition.bold.end.markdown
|            ^^^^^^^^ markup.italic.markdown - markup.italic markup.bold
|                   ^ punctuation.definition.italic.end.markdown

## https://spec.commonmark.org/0.30/#example-419

** is not an empty emphasis
| <- - punctuation
|^ - punctuation

## https://spec.commonmark.org/0.30/#example-420

**** is not an empty strong emphasis
| <- - punctuation
|^^^ - punctuation

## https://spec.commonmark.org/0.30/#example-421

**foo [bar](/url)**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^^^^^^^^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown
|     ^^^^^^^^^^^ meta.link.inline
|                ^^ punctuation.definition.bold.end.markdown

## https://spec.commonmark.org/0.30/#example-422

**foo
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown
bar**
| <- markup.bold.markdown
|^^^^ markup.bold.markdown
|  ^^ punctuation.definition.bold.end
|    ^ - markup

## https://spec.commonmark.org/0.30/#example-423

__foo _bar_ baz__
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^ markup.bold.markdown - markup markup
|^ punctuation.definition.bold.begin.markdown
|     ^ punctuation.definition.italic.begin.markdown
|     ^^^^^ markup.bold.markdown markup.italic.markdown
|         ^ punctuation.definition.italic.end.markdown
|          ^^^^^^ markup.bold.markdown - markup markup
|               ^ punctuation.definition.bold.end.markdown
|                ^ - markup

## https://spec.commonmark.org/0.30/#example-432

**foo [*bar*](/url)**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^ markup.bold.markdown - markup.bold markup.italic
|     ^^^^^^^^^^^^^ meta.link.inline
|^ punctuation.definition.bold.begin.markdown
|      ^ punctuation.definition.italic.begin.markdown
|      ^^^^^ markup.bold.markdown markup.italic.markdown
|          ^ punctuation.definition.italic.end.markdown
|           ^^^^^^^^^ markup.bold.markdown - markup.bold markup.italic
|                  ^^ punctuation.definition.bold.end.markdown

**foo [_bar_](/url)**
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^ markup.bold.markdown - markup.bold markup.italic
|     ^^^^^^^^^^^^^ meta.link.inline
|^ punctuation.definition.bold.begin.markdown
|      ^ punctuation.definition.italic.begin.markdown
|      ^^^^^ markup.bold.markdown markup.italic.markdown
|          ^ punctuation.definition.italic.end.markdown
|           ^^^^^^^^^ markup.bold.markdown - markup.bold markup.italic
|                  ^^ punctuation.definition.bold.end.markdown

## https://spec.commonmark.org/0.30/#example-433

__ is not an empty emphasis
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-434

____ is not an empty strong emphasis
| <- - markup - punctuation
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-435

foo ***
|   ^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-436

foo *\**
|^^^ - markup
|   ^^^^ markup.italic.markdown
|   ^ punctuation.definition.italic.begin.markdown
|    ^^ constant.character.escape.markdown
|      ^ punctuation.definition.italic.end.markdown
|       ^ - markup

## https://spec.commonmark.org/0.30/#example-437

foo *_*
|^^^ - markup
|   ^^^ markup.italic.markdown
|   ^punctuation.definition.italic.begin.markdown
|     ^ punctuation.definition.italic.end.markdown
|      ^ - markup

## https://spec.commonmark.org/0.30/#example-439

foo **\***
|^^^ - markup
|   ^^^^^^ markup.bold.markdown
|   ^^ punctuation.definition.bold.begin.markdown
|     ^^ constant.character.escape.markdown
|       ^^ punctuation.definition.bold.end.markdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-440

foo **_**
|^^^ - markup
|   ^^^^^ markup.bold.markdown
|   ^^punctuation.definition.bold.begin.markdown
|      ^^ punctuation.definition.bold.end.markdown
|        ^ - markup

## https://spec.commonmark.org/0.30/#example-441

**foo*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-442

*foo**

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-443

***foo**

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-444

****foo*

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-445

**foo***
| <- markup.bold.markdown punctuation.definition.bold.begin.markdown
|^^^^^^ markup.bold.markdown
|^ punctuation.definition.bold.begin.markdown
|    ^^ punctuation.definition.bold.end.markdown
|      ^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-446

*foo****

> Note: Needs ST4's branching to get it right!

## https://spec.commonmark.org/0.30/#example-447

foo ___
|   ^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-448

foo _\__
|^^^ - markup
|   ^^^^ markup.italic.markdown
|   ^ punctuation.definition.italic.begin.markdown
|    ^^ constant.character.escape.markdown
|      ^ punctuation.definition.italic.end.markdown
|       ^ - markup

## https://spec.commonmark.org/0.30/#example-449

foo _*_
|^^^ - markup
|   ^^^ markup.italic.markdown
|   ^punctuation.definition.italic.begin.markdown
|     ^ punctuation.definition.italic.end.markdown
|      ^ - markup

## https://spec.commonmark.org/0.30/#example-450

foo _____
|   ^^^^^ - markup - punctuation

## https://spec.commonmark.org/0.30/#example-451

foo __\___
|^^^ - markup
|   ^^^^^^ markup.bold.markdown
|   ^^ punctuation.definition.bold.begin.markdown
|     ^^ constant.character.escape.markdown
|       ^^ punctuation.definition.bold.end.markdown
|         ^ - markup

## https://spec.commonmark.org/0.30/#example-452

foo __*__
|^^^ - markup
|   ^^^^^ markup.bold.markdown
|   ^^punctuation.definition.bold.begin.markdown
|      ^^ punctuation.definition.bold.end.markdown
|        ^ - markup

## https://custom-tests/emphasis

This text is _italic_, but this__text__is neither bold_nor_italic
|            ^ punctuation.definition.italic
|             ^^^^^^ markup.italic
|                   ^ punctuation.definition.italic
|                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ - markup.bold - markup.italic

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

# TEST: STRIKETHROUGH #########################################################

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
| <- - punctuation.definition.strikethrough
|^^^^^^^^^^^^^^^^^ meta.paragraph - markup
|  ^ - punctuation.definition.strikethrough

This ~text~~~~ is ~~~~curious~.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph - markup
|    ^ - punctuation.definition.strikethrough
|         ^^^^ - punctuation.definition.strikethrough
|                 ^^^^ - punctuation.definition.strikethrough
|                            ^ - punctuation.definition.strikethrough

This ~~text~~~~ is ~~~~curious~~.
|^^^^ meta.paragraph - markup
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph markup.strikethrough
|                               ^^ meta.paragraph - markup
|    ^^ punctuation.definition.strikethrough.begin
|          ^^^^ - punctuation.definition.strikethrough
|                  ^^^^ - punctuation.definition.strikethrough
|                             ^^ punctuation.definition.strikethrough.end

This ~~has a
|    ^^^^^^^^ meta.paragraph markup.strikethrough

| <- meta.paragraph markup.strikethrough invalid.illegal.non-terminated.bold-italic
new paragraph~~.
|            ^^ meta.paragraph markup.strikethrough punctuation.definition.strikethrough.begin

| <- invalid.illegal.non-terminated.bold-italic

A ~~[striked](https://link-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.strikethrough.markdown-gfm

A ~~![striked](https://image-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.strikethrough.markdown-gfm

A ~~[![striked](image-url)](link-url)~~
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.strikethrough.markdown-gfm


# TEST: LINKS #################################################################

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
|                        ^ punctuation.definition.link.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^^^^ markup.underline.link.markdown
|                              ^ punctuation.definition.metadata.end.markdown

Here is a [reference link][name]{_attr='value' :att2}.
|         ^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                         ^^^^^^ meta.link.reference.metadata.markdown
|                               ^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.attributes.markdown
|                                ^^^^^^^^^^^^^ meta.attribute-with-value.markdown
|                                             ^ - meta.attribute-with-value
|                                              ^^^^^ meta.attribute-with-value.markdown
|         ^ punctuation.definition.link.begin.markdown
|                        ^ punctuation.definition.link.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^^^^ markup.underline.link.markdown
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
|                              ^ punctuation.definition.link.end.markdown
|                               ^ punctuation.definition.metadata.begin.markdown
|                                ^ punctuation.definition.metadata.end.markdown
|                                 ^ punctuation.definition.attributes.begin.markdown
|                                  ^ punctuation.definition.attributes.end.markdown

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
| ^^^^^^^ string.quoted.other.markdown

link with a single underscore inside the text : [@_test](http://example.com)
|                                                ^^^^^^ meta.paragraph meta.link.inline.description - punctuation.definition
|                                                      ^ meta.paragraph meta.link.inline punctuation.definition.link.end

[foo]
|<- meta.link.reference punctuation.definition.link.begin
|^^^ meta.paragraph meta.link.reference
|   ^ meta.link.reference punctuation.definition.link.end

This is literal [Foo*bar\]] but [ref][Foo*bar\]]
|               ^^^^^^^^^^^ meta.link.reference.description.markdown
|               ^ punctuation.definition.link.begin.markdown
|                ^^^^^^^ - constant
|                       ^^ constant.character.escape.markdown
|                         ^ punctuation.definition.link.end.markdown
|                               ^^^^^ meta.link.reference.description.markdown
|                                    ^^^^^^^^^^^ meta.link.reference.metadata.markdown

[**Read more &#8594;**][details]
|^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                      ^^^^^^^^^ meta.link.reference.metadata.markdown
|^^ punctuation.definition.bold.begin.markdown
|            ^^^^^^^ constant.character.entity.decimal.html
|                   ^^ punctuation.definition.bold.end.markdown
|                       ^^^^^^^ markup.underline.link.markdown

[Read more &#8594;][details]
|^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                  ^^^^^^^^^ meta.link.reference.metadata.markdown
|          ^^^^^^^ constant.character.entity.decimal.html
|                   ^^^^^^^ markup.underline.link

[Read more <span style="font-weight: bold;">&#8594;</span>][details]
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                                                          ^^^^^^^^^ meta.link.reference.metadata.markdown
|          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.tag
|                       ^^^^^^^^^^^^^^^^^^ source.css
|                                           ^^^^^^^ constant.character.entity.decimal.html - meta.tag
|                                                  ^^^^^^^ meta.tag
|                                                           ^^^^^^^ markup.underline.link

[![Cool ★ Image - Click to Enlarge][img-example]][img-example]
| <- meta.link.reference.description.markdown punctuation.definition.link.begin.markdown
|^^ meta.link.reference.description.markdown meta.image.reference.description.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.link.reference.description.markdown meta.image.reference.description.markdown
|                                  ^^^^^^^^^^^^^^ meta.link.reference.description.markdown
|                                                ^^^^^^^^^^^^^ meta.link.reference.metadata.markdown
|^^ punctuation.definition.image.begin.markdown
|                                 ^ punctuation.definition.image.end.markdown
|                                  ^ punctuation.definition.metadata.begin.markdown
|                                   ^^^^^^^^^^^ markup.underline.link
|                                              ^ punctuation.definition.metadata.end.markdown
|                                               ^ punctuation.definition.link.end.markdown
|                                                ^ punctuation.definition.metadata.begin.markdown
|                                                 ^^^^^^^^^^^ markup.underline.link
|                                                            ^ punctuation.definition.metadata.end.markdown

[![Cool ★ Image - Click to Enlarge](http://www.sublimetext.com/anim/rename2_packed.png)](http://www.sublimetext.com/anim/rename2_packed.png)
| <- meta.paragraph.markdown meta.link.inline.description.markdown punctuation.definition.link.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inline.description.markdown meta.image.inline.description.markdown
|                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inline.description.markdown meta.image.inline.metadata.markdown
|                                                                                      ^ meta.paragraph.markdown meta.link.inline.description.markdown
|                                                                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.link.inline.metadata.markdown
|^^ punctuation.definition.image.begin.markdown
|                                 ^ punctuation.definition.image.end.markdown
|                                  ^ punctuation.definition.metadata.begin.markdown
|                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                                                                                     ^ punctuation.definition.metadata.end.markdown
|                                                                                      ^ punctuation.definition.link.end.markdown
|                                                                                       ^ punctuation.definition.metadata.begin.markdown
|                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.markdown
|                                                                                                                                          ^ punctuation.definition.metadata.end.markdown

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


# TEST: IMAGES ################################################################

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
|^^^^^^^ meta.image.inline string.quoted.double
|       ^^^^ meta.image.inline
|          ^ punctuation.definition.metadata.end

Here is a ![Image Alt Text](
  <https://example.com/cat.gif> "hello"   ).
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.image.inline.metadata.markdown
|                                          ^^ meta.paragraph.markdown - meta.image
| ^ punctuation.definition.link.begin.markdown
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.underline.link.image.markdown
|                             ^ punctuation.definition.link.end.markdown
|                               ^^^^^^^ string.quoted.double.markdown
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
|                                 ^^^^^^^ string.quoted.other.markdown
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
|                        ^ punctuation.definition.image.end.markdown
|                         ^ punctuation.definition.metadata.begin.markdown
|                          ^ markup.underline.link.markdown
|                           ^ punctuation.definition.metadata.end.markdown


# TEST: FOOTNOTES #############################################################

## https://michelf.ca/projects/php-markdown/extra/#footnotes

That's some text with a footnote.[^1]
|                                ^^^^ meta.paragraph meta.link.reference.footnote.markdown-extra
|                                ^ punctuation.definition.link.begin
|                                 ^^ meta.link.reference.literal.footnote-id
|                                   ^ punctuation.definition.link.end

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


# TEST: COMMONMARK AUTOLINKS ##################################################

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


# TEST: GFM AUTOLINKS #########################################################

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


# TEST: HARD LINE BREAKS ######################################################

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


# TEST: CRITIC MARKUP #########################################################

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

No striked {~~~>~~} critics.
|          ^^^^^^^^ markup.critic.substitution.markdown
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^^ punctuation.separator.critic.markdown
|               ^^^ punctuation.definition.critic.end.markdown
|                  ^^^^^^^^^^ - markup.critic

No striked {~~~~>~~~} critics.
|          ^^^^^^^^^^ markup.critic.substitution.markdown
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^ - punctuation
|              ^^ punctuation.separator.critic.markdown
|                ^ - punctuation
|                 ^^^ punctuation.definition.critic.end.markdown
|                    ^^^^^^^^^^ - markup.critic

No striked {~~~~~>~~~~} critics.
|          ^^^^^^^^^^^^ markup.critic.substitution.markdown
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^^ - punctuation
|               ^^ punctuation.separator.critic.markdown
|                 ^^ - punctuation
|                   ^^^ punctuation.definition.critic.end.markdown
|                      ^^^^^^^^^^ - markup.critic

No striked {~~~~~~>~~~~~} critics.
|          ^^^^^^^^^^^^^^ markup.critic.substitution.markdown
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^^^ - punctuation
|                ^^ punctuation.separator.critic.markdown
|                  ^^^ - punctuation
|                     ^^^ punctuation.definition.critic.end.markdown
|                        ^^^^^^^^^^ - markup.critic

No striked {~~~~~~~>~~~~~~} critics.
|          ^^^^^^^^^^^^^^^^ markup.critic.substitution.markdown
|          ^^^ punctuation.definition.critic.begin.markdown
|             ^^^^ - punctuation
|                 ^^ punctuation.separator.critic.markdown
|                   ^^^^ - punctuation
|                       ^^^ punctuation.definition.critic.end.markdown
|                          ^^^^^^^^^^ - markup.critic

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
|                    ^^ punctuation.definition.link.end.markdown
