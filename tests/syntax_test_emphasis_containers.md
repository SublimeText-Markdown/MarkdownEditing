| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"

# Block quote paragraphs may continue across lines

> block _italic
> test_
| <- markup.quote.markdown punctuation.definition.blockquote.markdown
| ^^^^^ markup.italic.markdown
|     ^ punctuation.definition.italic.end.markdown

> block *italic
> test*
| ^^^^^ markup.italic.markdown
|     ^ punctuation.definition.italic.end.markdown

> block __bold
> test__
| ^^^^^^ markup.bold.markdown
|     ^^ punctuation.definition.bold.end.markdown

> block **bold
> test**
| ^^^^^^ markup.bold.markdown
|     ^^ punctuation.definition.bold.end.markdown

> block ***bold italic
> test***
| ^^^^^^^ markup.bold.markdown
| ^^^^^ markup.italic.markdown

> block _unclosed

outside_
|^^^^^^^ - markup.italic.markdown - markup.bold.markdown

# Separate list items are separate paragraphs

1. _italic
2. test_
|  ^^^^^ - markup.italic.markdown - markup.bold.markdown

1. *italic
2. test*
|  ^^^^^ - markup.italic.markdown - markup.bold.markdown

1. __bold
2. test__
|  ^^^^^^ - markup.italic.markdown - markup.bold.markdown

1. **bold
2. test**
|  ^^^^^^ - markup.italic.markdown - markup.bold.markdown

1. ***bold italic
2. test***
|  ^^^^^^^ - markup.italic.markdown - markup.bold.markdown

1. ~~strike
|  ^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
2. test~~
|  ^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

# Nested block quote/list paragraphs

> 1. _italic
> 2. test_
|    ^^^^^ - markup.italic.markdown - markup.bold.markdown

1. > _italic
   > test_
|    ^^^^^ markup.italic.markdown

# Footnote paragraphs

[^one]: _italic
    continued_
|   ^^^^^^^^^^ markup.italic.markdown

[^one]: _italic
[^two]: test_
|        ^^^^^ - markup.italic.markdown - markup.bold.markdown

> [^one]: _italic
>     continued_
|     ^^^^^^^^^^ markup.italic.markdown

> [^one]: _italic
> [^two]: test_
|          ^^^^^ - markup.italic.markdown - markup.bold.markdown

# Line-bounded inline containers

# _unclosed
| ^^^^^^^^^ - markup.italic.markdown - markup.bold.markdown
outside_
|^^^^^^^ - markup.italic.markdown - markup.bold.markdown

_unclosed
=========
| <- punctuation.definition.heading.setext.markdown - markup.italic.markdown
outside_
|^^^^^^^ - markup.italic.markdown - markup.bold.markdown

1. _unclosed
   =========
outside_
|^^^^^^^ - markup.italic.markdown - markup.bold.markdown

!!! note "_unclosed
|         ^^^^^^^^^ - markup.italic.markdown - markup.bold.markdown
outside_
|^^^^^^^ - markup.italic.markdown - markup.bold.markdown

# Table cells are independently balanced

| _italic | test_ |
| ------- | ----- |
| ^^^^^^^ - markup.italic.markdown - markup.bold.markdown

# Strikethrough commits only within its current container

> ~~strike
| ^^^^^^^^ markup.strikethrough.markdown-gfm
> continued~~
| ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

> ~~unclosed
| ^^^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

outside~~
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

1. ~~strike
|  ^^^^^^^^ markup.strikethrough.markdown-gfm
   continued~~
|  ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

> 1. ~~strike
|    ^^^^^^^^ markup.strikethrough.markdown-gfm
>    continued~~
|    ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

> 1. ~~strike
|    ^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
> 2. test~~
|    ^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

1. > ~~strike
|    ^^^^^^^^ markup.strikethrough.markdown-gfm
   > continued~~
|    ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

[^strike]: ~~strike
|          ^^^^^^^^ markup.strikethrough.markdown-gfm
    continued~~
|   ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

[^strike]: ~~strike
|          ^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
[^other]: test~~
|         ^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

> [^strike]: ~~strike
|            ^^^^^^^^ markup.strikethrough.markdown-gfm
>     continued~~
|     ^^^^^^^^^^^ markup.strikethrough.markdown-gfm

> [^strike]: ~~strike
|            ^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
> [^other]: test~~
|           ^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

# ~~unclosed
| ^^^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
outside~~
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

~~unclosed
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
==========
| <- punctuation.definition.heading.setext.markdown - markup.strikethrough
outside~~
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

1. ~~unclosed
|  ^^^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
   ==========
outside~~
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

!!! note "~~unclosed
|         ^^^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
outside~~
| <- - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

| ~~strike | test~~ |
| -------- | ------ |
| ^^^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal
|            ^^^^^^ - markup.strikethrough - punctuation.definition.strikethrough - invalid.illegal

The End.
| <- - markup.italic.markdown - markup.bold.markdown - markup.strikethrough
