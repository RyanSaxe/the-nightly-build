# Your first article

You ask, the paper publishes. This is what happens in between.

## Where it goes

A fresh paper has three series, and an article you ask for goes to Dispatches.
It is open and manual: it takes any article, never runs on a schedule, and needs
no change to `press/` before an article can start. The other two, News Brief and
Feature, run once you schedule the paper. The assistant uses one of them instead
when the request fits and that series admits the article, and says which it
chose.

## What the assistant settles

It turns your request into a commission: the question the piece answers, what it
must establish rather than mention, what you supplied and what research remains,
prior coverage to avoid repeating, the template, and a slug. A link, a topic, a
question, or a pasted document is starting material, never the whole of the
evidence. It asks only what would change the piece.

## Who writes it

Four roles produce the article, each from an exact brief and each leaving its
record: a writing coach settles how the piece should sound, a researcher reads
and records the sources, a writer drafts and proves the article against the
engine's check, and an editor reads it three times and cuts what the evidence
does not support. Nothing is cited that nobody opened.

## How it publishes

`nb prepare-pr` turns the finished article into one pull request against
`library`. CI validates it with the engine from `main` and no secrets. A clean
new-article PR merges itself, the site rebuilds, and the article is live at your
Pages URL under `library/<series>/<slug>.html`. The production record sits
beside it under `agent-artifacts/`.

Add "let me read it first" to your request and the PR opens as a draft instead.
CI validates it and nothing merges until you press "Ready for review" on the
pull request, which runs the check again and publishes.

## What it costs

One asked-for article took about 45 minutes of agent time across the four roles
and roughly half a million to a million tokens before any repair round.
[Production cost and role models](../reference/production.md) has the per-role
figures and the levers.

If a pull request fails validation,
[Troubleshoot Article PRs](../troubleshooting/article-prs.md) names the
boundaries.
