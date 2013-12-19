# Contributing

## Where to Begin

Development is based on milestones. Each milestone will be implemented in its own branch (e.g. branch `v2.0.4`).

The first thing you should do is determining the branch to base your edits on.

If you are fixing an issue that already exists in the issue tracker, see which milestone it belongs to and commit your contribution to the branch with the same name as the milestone. If the issue doesn't belong to a milestone;

* __push-access users__: assign it to the closest milestone.
* __non-push-access users__: pick the closest milestone.

If your contribution is independent from the issue tracker, pick the closest milestone and create your commits in that branch.

If the milestone branch doesn't exist yet;

* __push-access users__: create it. The format is e.g. `v2.0.4` and increments decimally. It is _not semver_.
* __non-push-access users__: pick `master` branch.

After you've done with your commits;

* __push-access users__: push your local branch to the same named branch on GitHub.
* __non-push-access users__: send a pull request from your local branch to the same named branch on GitHub.

Each milestone will have a pull request that will be kept open until the milestone is completed. The purpose of this is having a showcase and discussion page for the milestone. You can describe there what you have implemented, preferably using screenshots. It's also an early feedback place for the users about your contribution.

## General Guidelines

* Code formatting:
    - __Indentation__: 4 spaces
    - __Line endings__: `\n`
* If your contribution deserves a place in `README.md`, please do so. Preferably in the same commit with your modifications.
* If you want to add screenshots to `README.md`, put your images under `screenshots/` directory. For creating your screenshots, you can use markdown files under `samples/` directory.
* We create __changelog__ files for Package Manager updates. They are under `messages/` directory.

    If your contribution deserves a place under one of the "Bug Fixes", "New Features", "Changes" titles, please do so. Preferably in the same commit with your modifications.

    You have to edit the changelog that belongs to the branch you've worked on. For example, if you have based your commits on branch `v2.0.4`, then the changelog you should edit is `messages/2.0.4.md`.

    If the changelog file doesn't exist yet, create it by copying `messages/template.md` as a template.

* If you are defining a new __key binding__, please define for all the 3 OSs in their own `.sublime-keymap` files. You have to insert your edits into the exacly same place in the 3 files.
* If you want to introduce a new setting key for one of the `.sublime-settings` files, use `mde.` prefix in your setting key.
* For testing your changes, you can use the test files under `tests/`. You can extend those files to add new tests and edge cases.

## Publishing to Package Control

When the milestone is completed, push-access users can publish the new version to the Package Control. Creating the new version __tag__ on the GitHub repository is enough for this. For example, if the name of the milestone is `v2.0.4`, the tag should be `2.0.4`.

The update process may take __up to an hour__ depending on the crawl frequency by the Package Control.
