T: SYNTAX TEST "Packages/MarkdownEditing/syntaxes/MultiMarkdown.sublime-syntax"
Title:   A Sample MultiMarkdown Document
T: ^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:   ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Author:  Fletcher T. Penney
T:^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:    ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:     ^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Date:    February 9, 2011
Comment: This is a comment intended to demonstrate
         metadata that spans multiple lines, yet
         is treated as a single value.
T:      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Test:    And this is a new key-value pair
With-Dash: Test
T: ^^^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:       ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:        ^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
With Space: Test
T: ^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:        ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:         ^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
HTML Header: <style>
             body { width:100ex; margin:auto; text-align:justify; }
T:           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown source.css.embedded.html
HTML Header: <style>
             body { width:100ex; margin:auto; text-align:justify; }
             /* Some more style. */
             </style>
T:           ^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown meta.tag.style.end.html

T: <- - meta.frontmatter.multimarkdown
# Heading
T: <- markup.heading punctuation.definition.heading - meta.frontmatter.multimarkdown
T:^^^^^^^ markup.heading - meta.frontmatter.multimarkdown

# MathJax Tests

An example of math within a paragraph --- \\( {e}^{i\pi }+1=0 \\) --- easy enough.
T:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.math
T:                                        ^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
T:                                        ^^^ punctuation.definition.math.begin.multimarkdown
T:                                           ^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
T:                                                            ^^^ punctuation.definition.math.end.multimarkdown
T:                                                                ^^^^^^^^^^^^^^^^^ meta.paragraph.markdown - markup.math

And an equation on it's own:

   \\( {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\)
T:^ meta.paragraph.markdown - markup.math
T: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
T: ^^^ punctuation.definition.math.begin.multimarkdown
T:    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
T:                                                   ^^^ punctuation.definition.math.end.multimarkdown
T:                                                      ^ meta.paragraph.markdown - markup.math

   \\[ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} \\]
T:^ meta.paragraph.markdown - markup.math
T: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown markup.math.inline.multimarkdown
T: ^^^ punctuation.definition.math.begin.multimarkdown
T:    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.multimarkdown
T:                                                   ^^^ punctuation.definition.math.end.multimarkdown
T:                                                      ^ meta.paragraph.markdown - markup.math

   $$ {x}_{1,2}=\frac{-b\pm \sqrt{{b}^{2}-4ac}}{2a} $$
T:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.math.block.markdown
T: ^^ punctuation.definition.math.begin.markdown
T:   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ text.tex.latex.embedded.markdown
T:                                                  ^^ punctuation.definition.math.end.markdown
