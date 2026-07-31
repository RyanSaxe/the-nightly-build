# Revise a published article

Revisions correct the article in place without erasing its production history.
They always open a human-reviewed PR and never auto-merge.

Choose the smallest honest review tier:

- **Mechanical:** formatting, spelling, a broken link, or another change that
  does not alter meaning. A fresh editor review is required.
- **Substantive:** meaning, framing, or prose changes. Run a fresh writer and
  editor; add a researcher whenever evidence, claims, figures, numbers, or
  sources change.
- **Full rework:** the article is being reconceived. Run writing coach,
  researcher, writer, and editor again.

The assistant should initialize current authoring context with
`nb start-article`, replace the skeleton and asset folder with the published
article's exact current contents, apply the approved work, preview it, and add
the next numbered artifact pair for every role used. It then runs:

```sh
nb prepare-pr library/SERIES/SLUG.html \
  --library PATH-TO-LIBRARY-CHECKOUT \
  --revision
```

CI requires exactly one modified article, matching asset changes, and only new
numbered role artifacts. A fresh editor pair is mandatory. Existing artifacts
cannot be modified or deleted; a legacy article with none starts at `01`.

The revision cannot change `series`, `slug`, `date`, `mode`, or `order`. CI
reruns the current full proof and render check. It permits a correction to a
paused or already-published series, but the series must still exist and the
article's template must still be allowed.
