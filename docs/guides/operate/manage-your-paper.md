# Manage your paper

Day-to-day changes belong on `main` under `press/`. Ask your AI in plain
language; it should translate the request into the smallest configuration
change, run `nb validate`, show the effect, and commit it for review.

Common requests include:

- pause or resume a series with `paused`;
- change its schedule with `cadence`;
- commission or reorder configured items;
- refine a beat in `prompt.md`;
- change paper-wide voice in `editorial.md`;
- adjust role model guidance in `production.yaml`;
- change appearance or add carefully designed furniture.

Use `cadence: manual` for a series that should publish only when someone asks.
It is never returned as due by `nb duty`. In a manual open series, every new
article's slug must be a configured item; both article initialization and CI
enforce that.

Configuration changes do not edit the published archive. To correct an article
already on `library`, use [Revise an article](../publish/revise-an-article.md).

To retract an article, open a PR against `library` that only deletes
`library/SERIES/SLUG.html` and its matching `library/SERIES/SLUG/` assets. CI
accepts that shape only when the PR author is the repository owner, and a
curation PR never auto-merges; you review and merge it yourself. The next
build removes the article from every index, feed, and the catalog.

The exact series fields live in [Series reference](../../reference/series.md).
