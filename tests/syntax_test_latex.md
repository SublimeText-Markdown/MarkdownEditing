| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/Markdown.sublime-syntax"

This is math $1+1$ expression.
|            ^^^^^ meta.paragraph.markdown text.tex.latex meta.environment.math.inline.dollar.latex
|            ^ string.other.math.latex punctuation.definition.string.begin.latex
|             ^ constant.numeric.math.tex
|              ^ keyword.operator.math.tex
|               ^ constant.numeric.math.tex
|                ^ string.other.math.latex punctuation.definition.string.begin.latex

$$
| <- text.tex.latex meta.environment.math.block.dollar.latex string.other.math.latex punctuation.definition.string.begin.latex
|^^ text.tex.latex meta.environment.math.block.dollar.latex
|^ string.other.math.latex punctuation.definition.string.begin.latex
foo = 1 + 2
$$
| <- text.tex.latex meta.environment.math.block.dollar.latex string.other.math.latex punctuation.definition.string.end.latex
|^ text.tex.latex meta.environment.math.block.dollar.latex string.other.math.latex punctuation.definition.string.end.latex

    $$
| <- markup.raw.block.markdown    
|^^^^^^ markup.raw.block.markdown

1. Numbered List

   $$
   | <- markup.list.numbered.markdown string.other.math.latex punctuation.definition.string.begin.latex
   |^ markup.list.numbered.markdown string.other.math.latex punctuation.definition.string.begin.latex
   foo = 1 + 2
   | <- markup.list.numbered.markdown text.tex.latex
   $$
   | <- markup.list.numbered.markdown string.other.math.latex punctuation.definition.string.end.latex
   |^ markup.list.numbered.markdown string.other.math.latex punctuation.definition.string.end.latex

   $$1+1$$
   | <- markup.list.numbered.markdown string.other.math.latex punctuation.definition.string.begin.latex
   |^^^^^^ markup.list.numbered.markdown text.tex.latex meta.environment.math.block.dollar.latex
   |^ string.other.math.latex punctuation.definition.string.begin.latex
   |    ^^ string.other.math.latex punctuation.definition.string.end.latex
