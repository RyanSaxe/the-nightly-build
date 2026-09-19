# Manage your paper

Day-to-day changes belong on `main` under `press/`. Ask your AI in plain
language and expect the smallest configuration change that satisfies the
request, validated and committed for your review.

Common requests: "pause the docket series", "make the brief weekdays only",
"commission a deep dive on ASML", "less policy in the brief for a while", "use a
cheaper model for research", "give the paper a new look". Each lands as one
small diff under `press/`.

What a series covers is the paragraph that opens its prompt. "More health, less
policy" is an edit to that paragraph, and for the scaffolded News Brief and
Feature it is the same edit the two questions in
[Create your paper](../../getting-started/create-your-paper.md) make.

Use `cadence: manual` for a series that should publish only when someone asks.
It is never returned as due by `nb duty`, and a manual open series admits any
slug: every article in it was asked for, so its `items` are suggestions, not a
gate.

Articles you ask for are not held to one per series per day; several can land in
one series on one date. The schedule is the exception. `nb duty` treats a series
with an article dated today as done for that run, which is why an article you
asked for stands in for that day's scheduled one.

Configuration changes do not edit the published archive. To correct an article
already on `library`, use [Revise an article](../publish/revise-an-article.md).

To retract an article, open a PR against `library` that only deletes
`library/SERIES/SLUG.html`, its matching `library/SERIES/SLUG/` assets, and the
article's `agent-artifacts/SERIES/SLUG/` production record. CI accepts that
shape only when the PR author is the repository owner, and a curation PR never
auto-merges. You review and merge it yourself. The next build removes the
article from every index, feed, and the catalog. Git history preserves
everything a retraction deletes.

The exact series fields live in [Series reference](../../reference/series.md).
