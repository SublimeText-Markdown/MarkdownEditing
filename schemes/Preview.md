---
meta:
    author: Jon Doe
    topic: Samples
---
# A sample Markdown document

This is a sample document so you can preview the color schemes.

## Text Formatting

Markdown supports _italics_, __bold__, and ___bold italics___ style using underscores.

Markdown supports *italics*, **bold**, and ***bold italics*** style using asterisks.

There are also inline styles like `inline code in monospace font` and ~~strikethrough style~~.

__There may be ~~strikethroughed text~~ or `code text` inside bold text.__

_And There may be ~~strikethroughed text~~ or `code text` inside italic text._

> __Here is some quotation__. Lorem ~~ipsum~~ dolor sit amet, consectetur  
> adipisicing elit, *sed* do eiusmod tempor incididunt ut labore et
> dolore magna aliqua. Ut enim <b>ad</b> minim <kbd>veniam</kbd>, quis nostrud exercitation.
> 
> <code>
>   code block
> </code>

Inline <kbd>key</kbd> or ~~<kbd>key</kbd>~~ other <b>bold html</b> tags.

<table align="center">
    <tr width="85%">
        <td>column&nbsp;text</td>
    </tr>
</table>

## Links and References

To reference something from a URL, [Named Links][links],
[Inline links](https://example.com/index.html "Description") and direct link like <https://example.com/>
are of great help. Sometimes ![A picture][sample image] is worth a thousand words.

---

This [[SamplePage]] is a wiki link.

## Lists

There are two types of lists, ordered and unordered.

1. Item 1 
   <kbd>key</kbd>
2. Item 2
3. Item 3

1) Item 1
2) Item 2
3) Item 3

* Item A
    - Sub list
        + Sub sub list
        + Sub sub list 2
    - Sub list 2
* Item B
* Item C

## Tables

Col 1 | Col 2
-----:|-------
what  | else

## Code Blocks

Anything indented more than 3 characters is treated as raw code block.

    function fibo(n) {
        fibo.mem = fibo.mem || []; // I am some comment
        return fibo.mem[n] || fibo.mem[n] = n <= 1 ? 1 : fibo(n - 1) + fibo(n - 2);

Fenced code blocks support syntax highlighting and are wrapped in triple backticks.

```javascript
function fibo(n) {
    fibo.mem = fibo.mem || []; // I am some comment
    return fibo.mem[n] || fibo.mem[n] = n <= 1 ? 1 : fibo(n - 1) + fibo(n - 2);
}
```

```diff
diff --git a/schemes/Preview.md b/schemes/Preview.md
index 3d4b1fe..a85a22a 100644
--- a/schemes/Preview.md
+++ b/schemes/Preview.md
@@ -89,6 +89,12 @@ function fibo(n) {
 
-## Deleted
+## Inserted
```

## CriticMarkup

This is {++ inserted ++} and {-- deleted --} or {== highlighted ==}{>> comment <<} text.

We can also {~~ substitute ~> something ~~}.

## Reference Definitions

[^1]: This is a footnote definition

[links]: https://example.com/index.html
[sample image]: https://example.com/sample.png
