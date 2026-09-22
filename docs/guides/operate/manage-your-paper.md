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
`nb duty` never returns it as due. A manual open series admits any slug because
the owner requests each article. Its `items` field suggests topics and does not
restrict commissions.

You can request several articles for one series on the same day. Scheduled work
follows a different rule. `nb duty` treats a series with an article dated today
as complete for that run. A requested article therefore counts as that day's
scheduled article.

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
