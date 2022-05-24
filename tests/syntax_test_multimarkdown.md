| SYNTAX TEST "Packages/MarkdownEditing/syntaxes/MultiMarkdown.sublime-syntax"

# MultiMarkdown without frontmatter
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown

# MathJax Tests

An example of math within a paragraph --- \\( {e}^{i\pi }+1=0 \\) --- easy enough.
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.math
|                                         ^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
|                                         ^^^ punctuation.definition.math.begin.multimarkdown
|                                            ^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
|                                                             ^^^ punctuation.definition.math.end.multimarkdown
|                                                                 ^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.math

And an equation on it's own:

   \\( {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\)
|^^ meta.paragraph.markdown - markup.math
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
|  ^^^ punctuation.definition.math.begin.multimarkdown
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
|                                                    ^^^ punctuation.definition.math.end.multimarkdown
|                                                       ^ meta.paragraph.markdown - markup.math

   \\[ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\]
|^^ meta.paragraph.markdown - markup.math
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
|  ^^^ punctuation.definition.math.begin.multimarkdown
|     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
|                                                    ^^^ punctuation.definition.math.end.multimarkdown
|                                                       ^ meta.paragraph.markdown - markup.math

   $$ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} $$
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.math.block.markdown
|  ^^ punctuation.definition.math.begin.latex
|    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.markdown
|                                                   ^^ punctuation.definition.math.end.latex
