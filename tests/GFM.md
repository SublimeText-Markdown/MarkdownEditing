# Strikethrough

Below text should be parsed as _strikethroughed_.

~~ Mistaken text. ~~

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
