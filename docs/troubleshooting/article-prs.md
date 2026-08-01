# Troubleshoot Article PRs

Start with the `BLOCK` code and message in the proof comment. Reproduce against
the exact proposed branch with the checkout-owned `nb check`; do not edit
`library` directly to make the error disappear.

## `B-DIFF-SHAPE`

A normal Article PR may add one HTML article plus matching assets and its full
artifact tree. A revision may modify one existing HTML article, change only
matching assets, and add exactly one matching revision note. Move configuration
or engine changes to a separate PR against `main`.

## `B-AGENT-ARTIFACTS`

Check the expected role file pair and invocation number. New articles require
the complete production record. Do not edit an invocation already on
`library`.

## `B-REVISION-NOTE`

Add one nonempty UTF-8 Markdown file at
`agent-artifacts/SERIES/SLUG/revisions/NN.md`, where `NN` is the next two-digit
number. Start at `01.md` when no earlier note exists. Do not change or delete a
published note.

Revision notes do not share numbering with role invocations and do not require
a role or prose template.

## The local proof passes but the render probe fails

Build from the PR head with the current engine and inspect the browser result.
Look for missing local assets, overflow, theme contrast, or furniture that only
works at one width. The file-level proof cannot substitute for rendering.

## Delivery reports `NB_ARTICLE_PR_REQUIRED`

The generated branch is complete and proved, but the environment lacks a
working GitHub CLI path. Use the runtime's connected GitHub tool to open or
update exactly the reported base, head, title, and body. Do not recreate or
edit the generated commit.
