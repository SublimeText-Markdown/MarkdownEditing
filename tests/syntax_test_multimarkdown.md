T: SYNTAX TEST "Packages/Markdown/MultiMarkdown.sublime-syntax"
Title:   A Sample MultiMarkdown Document
T: ^^ meta.header.multimarkdown keyword.other.multimarkdown
T:   ^ meta.header.multimarkdown punctuation.separator.key-value.multimarkdown
T:       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.header.multimarkdown string.unquoted.multimarkdown
T:                                      ^ meta.header.multimarkdown - string
Author:  Fletcher T. Penney
T:^^^^ meta.header.multimarkdown keyword.other.multimarkdown
T:    ^ meta.header.multimarkdown punctuation.separator.key-value.multimarkdown
T:       ^^^^^^^^^^^^^^^^^^ meta.header.multimarkdown string.unquoted.multimarkdown
Date:    February 9, 2011
Comment: This is a comment intended to demonstrate
         metadata that spans multiple lines, yet
         is treated as a single value.
T:       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.header.multimarkdown string.unquoted.multimarkdown
T:                                    ^ meta.header.multimarkdown - string
Test:    And this is a new key-value pair
With-Dash: Test
T: ^^^^^^ meta.header.multimarkdown keyword.other.multimarkdown
T:       ^ meta.header.multimarkdown punctuation.separator.key-value.multimarkdown
T:         ^^^^ meta.header.multimarkdown string.unquoted.multimarkdown
With Space: Test
T: ^^^^^^^ meta.header.multimarkdown keyword.other.multimarkdown
T:        ^ meta.header.multimarkdown punctuation.separator.key-value.multimarkdown
T:          ^^^^ meta.header.multimarkdown string.unquoted.multimarkdown
HTML Header: <style>
             body { width:100ex; margin:auto; text-align:justify; }
             /* Some more style. */
             </style>
T:           ^^^^^^^^ meta.header.multimarkdown string.unquoted.multimarkdown

T: <- meta.content.multimarkdown - meta.header.multimarkdown
# Heading
| <- markup.heading punctuation.definition.heading
|^^^^^^^^ markup.heading
