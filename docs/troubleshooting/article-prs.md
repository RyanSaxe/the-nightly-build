# Troubleshoot Article PRs

Start with the `BLOCK` code and message in the proof comment. Reproduce against
the exact proposed branch with the checkout-owned `nb check`; do not edit
`library` directly to make the error disappear.

## `B-DIFF-SHAPE`

A normal Article PR may add one HTML article plus matching assets and its full
artifact tree. A revision may modify one existing HTML article, change only
matching assets, and add only fresh role artifacts. Move configuration or
engine changes to a separate PR against `main`.

## `B-AGENT-ARTIFACTS`

Check the expected role file pair and invocation number. New articles require
the complete production record. Revisions require at least the next numbered
editor pair; any other fresh role must also contain its exact pair. Do not edit
an invocation already on `library`.

## `B-REVISION-IDENTITY`

Restore the published `series`, `slug`, `date`, `mode`, and `order`. A change to
one of those creates a different publication identity and cannot be smuggled
through an in-place revision.

## The local proof passes but the render probe fails

Build from the PR head with the current engine and inspect the browser result.
Look for missing local assets, overflow, theme contrast, or furniture that only
works at one width. The file-level proof cannot substitute for rendering.

## Delivery reports `NB_ARTICLE_PR_REQUIRED`

The generated branch is complete and proved, but the environment lacks a
working GitHub CLI path. Use the runtime's connected GitHub tool to open or
update exactly the reported base, head, title, and body. Do not recreate or
edit the generated commit.
