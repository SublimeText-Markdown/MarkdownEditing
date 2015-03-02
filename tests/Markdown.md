Source: https://github.com/textmate/markdown.tmbundle/blob/master/Tests/test-minimal.markdown

Inline styles
===============

_italic_

_italic one_ not italic _italic two_

_italic\__

_italic \__

stuff * not italic*

*italic__*

_all _ italic_

_italic
end italic_

\\\\_italic\\_

\\\\_italic\\\_\\\\_

\\\\_italic\\_

\_ not italic _

_not italic _

\\\\_not italic\_

_not italic \_

\\\_not italic\\_

_not italic

not end italic_

__bold__

**bold\***

___bold_and_italic___

***bold_and_italic***

`raw more`

``dobule ` raw``

`raw \` more`

Headings
================

heading 2
----------

## heading 2

### heading 3

###### heading 6

Horizontal lines
=================

***

* * *

___

__ __ __

- - - 

----------------


Block formatting
================

Lists
----------------

 * This *is a list!*
 * This is another list item.
   But this one spans *two* lines. 
 * Another list item with __inline__ formatting
 * This one is tricky  
 * *This is a list*

   Because this should still be a list item.

1. This is a list item too
2. This list is numbered

1986\. This shouldn't be a list.

Code block
---------------

	asdfsdafasdf
	This is code.
	Isn't it pretty!

Quotes
---------------

> Here is a quote block
This quote continues on.  Line breaking is OK in markdown
> Here it is again
> Lah-di-dah
> I should really match headings in here too:
> ## This is a heading in a block quote
