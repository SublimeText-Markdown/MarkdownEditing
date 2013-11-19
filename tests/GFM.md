# Strikethrough

~~This text should be parsed as _strikethroughed_.~~

~~There may be __bold__ or _italic_ text inside strikethroughed text.~~

~~There may be a keyboard shortcut like <kbd>Enter</kbd> inside strikethroughed text.~~

__There may be ~~strikethroughed text~~ inside bold text.__
_There may be ~~strikethroughed text~~ inside italic text._

~~ If there is a space in the beginning or end, it won't work as per the [GFM][GFM] docs ~~

~~Strikethrough can be applied to
multiple lines. Just keep in mind
not to put any space in the beginning or end.~~

# Underscore In Words

The word `complicated` must be neither bold nor italic below:

perform_complicated_task
perform__complicated__task

But the first part below is italic and bold respectively:

_perform_complicated_task
__perform__complicated__task

# Keyboard Shortcuts

Keyboard shortcuts below should be highlighted:

---

A keyboard shortcut <kbd>Enter</kbd> can be in paragraph.

* A keyboard shortcut <kbd>Enter</kbd> can be in list.

_A keyboard shortcut <kbd>Enter</kbd> can be in italic._
__A keyboard shortcut <kbd>Enter</kbd> can be in bold.__

~~A keyboard shortcut <kbd>Enter</kbd> can be in deleted text.~~

<p>A keyboard shortcut <kbd>Enter</kbd> can be in HTML.</p>

<div>
    A keyboard shortcut <kbd>Enter</kbd> can be in block level tags.
</div>

# Fenced Code Blocks

## In / Near List Items

Below fenced code blocks _should_ be highlighted.

---

* List item

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

* List item

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

---

Below are _not_ valid fenced code blocks according to the [GFM docs][GFM]. It says there must be a blank line before the code block. However, GitHub highlights them. So, they _should_ be highlighted.

---

* List item
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

* List item
```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

## In / Near Paragraphs

Below is _not_ a _fenced_ code block, just a normal code block.

---

Paragraph

    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

---

Below 2 blocks are fenced code blocks. They _should_ be highlighted.

---

Paragraph

```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

Paragraph
```js
for (var i = 0; i < 10; i++) {
    console.log(i);
}
```

---

Below is not any type of code block. It _should not_ be highlighted.

---

Paragraph
    ```js
    for (var i = 0; i < 10; i++) {
        console.log(i);
    }
    ```

[GFM]: https://help.github.com/articles/github-flavored-markdown
