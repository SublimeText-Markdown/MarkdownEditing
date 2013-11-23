# Contributing

## General Guidelines

* If your contribution needs to be clarified in `README.md`, please do so. Preferably in the same commit with your modifications.
* If you want to add screenshots to `README.md`, put your images under `screenshots/` directory. For creating your screenshots, you can use markdown files under `samples/` directory.
* For testing your changes, you can use the test files under `tests/`. You can extend those files to add new tests and edge cases.
* We create changelog files for Package Manager updates. They are under `messages/` directory.
    If your edits deserve a place under one of the "Bug Fixes", "New Features", "Changes" titles, please do so. Preferably in the same commit with your modifications.

    You have to edit the _next_ changelog for this. You can determine which changelog is the _next_ under `messages/` directory via the last published git tag. If the last published git tag is for example `2.0.1`, then the next changelog file will probably be `2.0.2.md`.

    If the changelog file doesn't exist yet, create it based on the `messages/template.md`. Don't forget to remove unnecessary headers from it. For example if you will use only "New Features" header, remove other two empty headers.
* If you want to introduce a new setting key for one of the `.sublime-settings` files, use `mde_` prefix in your setting keys.
* Commits to `master` branch aren't immediately published to Package Manager. They will be published when a new version tag is created.
