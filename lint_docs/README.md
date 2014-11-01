# Lint feature for MarkdownEditing

This feature is still experimental. Use at your own risk.

Open a markdown document and press `<kbd>ctrl</kbd>(<kbd>⌘</kbd>)+<kbd>shift</kbd>(<kbd>⇧</kbd>)+<kbd>M</kbd>` or input `MarkdownEditing: Markdown Lint` in command pallette to try it.

## Editing rules

All rules are described in `lint_docs/RULES.md`, and implemented in `lint.py`. When you edit a rule, remember to edit the description in `RULES.md`.

### How rules work

All rules are implemented as seperated subclasses of `mddef` class defined in `lint.py`. The lifespan of a rule instance is one lint process. There are several important fields in every rule class:

| Name | Type | Comment |
|------|------|---------|
| flag | int | the flag used to search for locator (default: 0) |
| desc | str | description of the rule |
| locator | str | a regex that will be used to locate the targets |
| gid | int | the id of the group in locator that will be passed to test method (default: 0) |
| finish | bool | the linter will stop scanning the rest of the document if it is true (default: false) |

and a "test" method like this:

```python
def test(self, text, s, e):
    if isIllegal(text[s:e]):
        return {the_offset: "additional information"}
    else:
        return {}
```

The linter will search for all occcurences of `locator` with regex flag equals to `flag` in the document. Then it passes the document itself and the begin position and the end position of target captured group to `test` method. The `test` method will return a dictionary of "offset:information" key-value pairs. That offset will decide the displayed line number of the occurence of the error.

### Editing an existing rule

First you need to know the name of that rule (e.g. MD001), and search for the class with the same name in `lint.py` (e.g. `md001`). You may want to change the `locator` to narrow down (or expand) the applied domain first before editing `test` method.

### Creating new rules

Every rule is a subclass of `mdddef`. Here is an example:

```python
class md001(mddef):
    flag = re.M # re.M is for multiline mode
    desc = 'Header levels should only increment by one level at a time'
    locator = r'^#{1,6}(?!#)' # This is for atx and atx_closed style headers

    lastMatch = None # We are comparing two successive headers, so we
                     # need to store the previous one

    def test(self, text, s, e):
        ret = {}
        if self.lastMatch:
            n1 = len(self.lastMatch) # the length of the captured group
            n2 = e - s               # is the level of the header
            if n2 > n1 and n2 != n1 + 1:
                ret[s] = 'expected %d, %d found' % (n1 + 1, n2)
        self.lastMatch = text[s: e]
        return ret
```

You can create new settings as well. Just follow the examples of existing rules and the value of settings are stored as `self.settings`.

## Discussion

You can share your opinions through [issues](https://github.com/SublimeText-Markdown/MarkdownEditing/issues).