T: SYNTAX TEST "Packages/MarkdownEditing/syntaxes/MultiMarkdown.sublime-syntax"
T: <- meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
Title:   A Sample MultiMarkdown Document
T: ^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:   ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:    ^^^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown
T:       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Author:  Fletcher T. Penney
T:^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:    ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:     ^^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown
T:       ^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Date:    February 9, 2011
Comment: This is a comment intended to demonstrate
         metadata that spans multiple lines, yet
         is treated as a single value.
T:      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
Test:    And this is a new key-value pair
With-Dash: Test
T: ^^^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:       ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:        ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown
T:         ^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
With Space: Test
T: ^^^^^^^ meta.frontmatter.multimarkdown meta.mapping.key.multimarkdown entity.other.attribute-name.multimarkdown
T:        ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown punctuation.separator.key-value.multimarkdown
T:         ^ meta.frontmatter.multimarkdown meta.mapping.multimarkdown
T:          ^^^^^ meta.frontmatter.multimarkdown meta.mapping.value.multimarkdown
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
