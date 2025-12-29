# MarkdownEditing {version} Changelog

Your _MarkdownEditing_ plugin is updated. Enjoy new version. For any type of
feedback you can use [GitHub issues][issues].

## Bug Fixes

- disable `mde_show_fold_all_sections` binding by default (fixes #807)
- Insert new list items on enter only on empty selection (fixes #810)
- fix "extend list" binding constraints (fixes #812)
- fix code-spans not properly terminated in tables

## New Features

## Changes

- embedded linter no longer complains on Bash- and Python-style comments in code blocks 
  (previously it triggered the `MD023` rule)
- refactor syntax definitions of fenced code blocks to work around a crash 
  caused by unbalanced fences

[issues]: https://github.com/SublimeText-Markdown/MarkdownEditing/issues
