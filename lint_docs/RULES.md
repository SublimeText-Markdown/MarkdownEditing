# Rules

This document contains a description of all rules, what they are checking for,
as well as an examples of documents that break the rule and corrected
versions of the examples.

The rules are mostly [from markdownlint](https://github.com/mivok/markdownlint/blob/master/docs/RULES.md).

## MD001 - Header levels should only increment by one level at a time

This rule is triggered when you skip header levels in a markdown document, for
example:

    # Header 1

    ### Header 3

    We skipped out a 2nd level header in this document

When using multiple header levels, nested headers should increase by only one
level at a time:

    # Header 1

    ## Header 2

    ### Header 3

    #### Header 4

    ## Another Header 2

    ### Another Header 3

This rule only applies to atx and atx_closed styles of headers.

## MD002 - First header should be a h1 header

This rule is triggered when the first header in the document isn't a h1 header:

    ## This isn't a H1 header

    ### Another header

The first header in the document should be a h1 header:

    # Start with a H1 header

    ## Then use a H2 for subsections

This rule applies to all three styles of headers.

## MD003 - Header style

This rule is triggered when different header styles (atx, setext, and 'closed'
atx) are used in the same document:

    # ATX style H1

    ## Closed ATX style H2 ##

    Setext style H1
    ===============

Be consistent with the style of header used in a document:

    # ATX style H1

    ## ATX style H2

Note: the configured header style can be a specific style to use (atx,
atx_closed, setext), or simply require that the usage be consistent within the
document.

## MD004 - Unordered list style

This rule is triggered when the symbols used in the document for unordered
list items do not match the configured unordered list style:

    * Item 1
    + Item 2
    - Item 3

To fix this issue, use the configured style for list items throughout the
document:

    * Item 1
    * Item 2
    * Item 3

Note: the configured list style can be a specific symbol to use (asterisk,
plus, dash), or simply require that the usage be consistent within the
document, or require that the three different symbols to be used cyclically on different level or same symbol on same levels.

## MD005 - Inconsistent indentation for list items at the same level

This rule is triggered when list items are parsed as being at the same level,
but don't have the same indentation:

    * Item 1
        * Nested Item 1
        * Nested Item 2
       * A misaligned item

Usually this rule will be triggered because of a typo. Correct the indentation
for the list to fix it:

    * Item 1
      * Nested Item 1
      * Nested Item 2
      * Nested Item 3

## MD006 - Consider starting bulleted lists at the beginning of the line

This rule is triggered when top level lists don't start at the beginning of a
line:

    Some text

      * List item
      * List item

To fix, ensure that top level list items are not indented:


    Some test

    * List item
    * List item

Rationale: Starting lists at the beginning of the line means that nested list
items can all be indented by the same amount when an editor's indent function
or the tab key is used to indent. Starting a list 1 space in means that the
indent of the first nested list is less than the indent of the second level (3
characters if you use 4 space tabs, or 1 character if you use 2 space tabs).

## MD007 - Unordered list indentation

This rule is triggered when list items are not indented by the configured
number of spaces (default: current Sublime tab_size).

Example:

    * List item
       * Nested list item indented by 3 spaces

Corrected Example:

    * List item
      * Nested list item indented by 2 spaces

Rationale (2 space indent): indending by 2 spaces allows the content of a
nested list to be in line with the start of the content of the parent list
when a single space is used after the list marker.

Rationale (4 space indent): Same indent as code blocks, simpler for editors to
implement. See
<http://www.cirosantilli.com/markdown-styleguide/#indented-lists> for more
information.

In addition, this is a compatibility issue with multi-markdown parsers, which
require a 4 space indents. See
<http://support.markedapp.com/discussions/problems/21-sub-lists-not-indenting>
for a description of the problem.

## MD009 - Trailing spaces

This rule is triggered on any lines that end with whitespace. To fix this,
find the line that is triggered and remove any trailing spaces from the end.

Note: this rule can be triggered inside code/quote block.

## MD010 - Hard tabs

This rule is triggered any any lines that contain hard tab characters instead
of using spaces for indentation. To fix this, replace any hard tab characters
with spaces instead.

Example:

    Some text

        * hard tab character used to indent the list item

Corrected example:

    Some text

        * Spaces used to indent the list item instead

## MD011 - Reversed link syntax

This rule is triggered when text that appears to be a link is encountered, but
where the syntax appears to have been reversed (the `[]` and `()` are
reversed):

    (Incorrect link syntax)[http://www.example.com/]

To fix this, swap the `[]` and `()` around:

    [Correct link syntax](http://www.example.com/)

## MD012 - Multiple consecutive blank lines

Tags: whitespace, blank_lines

This rule is triggered when there are multiple consecutive blank lines in the
document:

    Some text here


    Some more text here

To fix this, delete the offending lines:

    Some text here

    Some more text here

Note: this rule will not be triggered if there are multiple consecutive blank
lines inside code blocks.

## MD013 - Line length

This rule is triggered when there are lines that are longer than the
configured line length (default: current Sublime wrap_width). To fix this, split the line
up into multiple lines.

This rule is disabled by default.

## MD018 - No space after hash on atx style header

This rule is triggered when when spaces are missing after the hash characters
in an atx style header:

    #Header 1

    ##Header 2

To fix this, separate the header text from the hash character by a single
space:

    # Header 1

    ## Header 2

## MD019 - Multiple spaces after hash on atx style header

This rule is triggered when when more than one space is used to separate the
header text from the hash characters in an atx style header:

    #  Header 1

    ##  Header 2

To fix this, separate the header text from the hash character by a single
space:

    # Header 1

    ## Header 2

## MD020 - No space inside hashes on closed atx style header

This rule is triggered when when spaces are missing inside the hash characters
in a closed atx style header:

    #Header 1#

    ##Header 2##

To fix this, separate the header text from the hash character by a single
space:

    # Header 1 #

    ## Header 2 ##

Note: this rule will fire if either side of the header is missing spaces.

## MD021 - Multiple spaces inside hashes on closed atx style header

This rule is triggered when when more than one space is used to separate the
header text from the hash characters in a closed atx style header:

    #  Header 1  #

    ##  Header 2  ##

To fix this, separate the header text from the hash character by a single
space:

    # Header 1 #

    ## Header 2 ##

Note: this rule will fire if either side of the header contains multiple
spaces.

## MD022 - Headers should be surrounded by blank lines

This rule is triggered when headers (any style) are either not preceded or not
followed by a blank line:

    # Header 1
    Some text

    Some more text
    ## Header 2

To fix this, ensure that all headers have a blank line both before and after
(except where the header is at the beginning or end of the document):

    # Header 1

    Some text

    Some more text

    ## Header 2

Rationale: Aside from asthetic reasons, some parsers, including kramdown, will
not parse headers that don't have a blank line before, and will parse them as
regular text.

## MD023 - Headers must start at the beginning of the line

This rule is triggered when a header is indented by one or more spaces:

    Some text

      # Indented header

To fix this, ensure that all headers start at the beginning of the line:

    Some text

    # Header

Rationale: Headers that don't start at the beginning of the line will not be
parsed as headers, and will instead appear as regular text.

## MD024 - Multiple headers with the same content

This rule is triggered if there are multiple headers in the document that have
the same text:

    # Some text

    ## Some text

To fix this, ensure that the content of each header is different:

    # Some text

    ## Some more text

Rationale: Some markdown parses generate anchors for headers based on the
header name, and having headers with the same content can cause problems with
this.

## MD025 - Multiple top level headers in the same document

This rule is triggered when a top level header is in use (the first line of
the file is a h1 header), and more than one h1 header is in use in the
document:

    # Top level header

    # Another top level header

To fix, structure your document so that there is a single h1 header that is
the title for the document, and all later headers are h2 or lower level
headers:

    # Title

    ## Header

    ## Another header

Rationale: A top level header is a h1 on the first line of the file, and
serves as the title for the document. If this convention is in use, then there
can not be more than one title for the document, and the entire document
should be contained within this header.

## MD026 - Trailing punctuation in header

This rule is triggered on any header that has a punctuation character as the
last character in the line:

    # This is a header.

To fix this, remove any trailing punctuation:

    # This is a header

Note: The punctuation parameter can be used to specify what characters class
as punctuation at the end of the header (defaults to `".,;:!"`). For example, you can set it to
`".,;:"` to allow headers with exclamation marks in them.

## MD027 - Multiple spaces after blockquote symbol

This rule is triggered when blockquotes have more than one space after the
blockquote (`>`) symbol:

    >  This is a block quote with bad indentation
    >  there should only be one.

To fix, remove any extraneous space:

    > This is a blockquote with correct
    > indentation.

## MD028 - Blank line inside blockquote

This rule is triggered when two blockquote blocks are separated by nothing
except for a blank line:

    > This is a blockquote
    > which is immediately followed by

    > this blockquote. Unfortunately
    > In some parsers, these are treated as the same blockquote.

To fix this, ensure that any blockquotes that are right next to each other
have some text in between:

    > This is a blockquote.

    And Jimmy also said:

    > This too is a blockquote.

Alternatively, if they are supposed to be the same quote, then add the
blockquote symbol at the beginning of the blank line:

    > This is a blockquote.
    >
    > This is the same blockquote.

Rationale: Some markdown parsers will treat two blockquotes separated by one
or more blank lines as the same blockquote, while others will treat them as
separate blockquotes.

## MD029 - Ordered list item prefix

This rule is triggered on ordered lists that do not either start with '1.' or
do not have a prefix that increases in numerical order (depending on the
configured style, which defaults to 'any').

Example valid list if the style is configured as 'one':

    1. Do this.
    1. Do that.
    1. Done.

Example valid list if the style is configured as 'ordered':

    1. Do this.
    2. Do that.
    3. Done.

Example valid list if the style is configured as 'any':

    1. Do this.
    1. Do that.
    1. Done.
    
    1. Do this.
    2. Do that.
    3. Done.
