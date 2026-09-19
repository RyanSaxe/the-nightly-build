# Publish an article now

Read `docs/guides/publish/publish-now.md`, `docs/reference/series.md`, and
[prompt authoring](../craft/prompt-authoring.md).

Take the request as it comes. A link, a topic, a question, a pasted document, a
brief: each is starting material, never a sufficient commission, and never
something to demand. It is not the moment to shape the paper either: the two
questions that make the default paper theirs belong to
[create paper](./create-paper.md), and the article goes ahead without them.

## Find the home

Inspect the press. An open series admits the article without a config change: a
scheduled one on any day, and a manual one, such as the scaffolded Dispatches,
always. A collection or sequence admits only its configured items. A rolling
series takes today's edition and no second one. Publish in an existing series
when it fits and admits the piece; otherwise in Dispatches. Say which home you
chose and why, in one line. Do not create a series for one article; when the
same kind of request arrives a third time, offer a series, with a name and a
cadence to accept or decline.

## Turn the request into a commission

Clarify only what would change the piece: the series, the angle, the evidence,
or the urgency. Then settle the contribution and the question it answers, what
the article must establish rather than mention, what the request supplied and
what research remains, prior coverage to check with `nb history` and what must
be new, the template and any furniture the subject needs, and a stable slug.

A link alone: read it, state the contribution and angle in one line, and confirm
only what would change the piece. Research continues past the link, and the
series' source floor applies.

A topic or a question alone: the same without the reading. Check prior coverage
with `nb history` before proposing the angle, so the paper does not repeat
itself.

A link that is paywalled or unreachable: say so. Offer to proceed from what is
readable, or from text the owner pastes as a required document. Never cite a
page that was not opened.

Ask whether the owner wants to read the article before it publishes. If so,
production ends with `nb prepare-pr --hold`: the PR opens as a draft that CI
validates and never merges, and marking it ready publishes.

## Produce it

When configuration changed, validate it and get it onto `main`. Then read
`../../nb-orchestrator/SKILL.md` and continue in this same agent as the
orchestrator, with this configured article as the exact authorized work. Do not
run `nb duty`. The commission is recorded in `commission.md` under the article's
artifacts, and `nb prepare-pr` fetches `origin/library` itself. When it prints
`NB_ARTICLE_PR_REQUIRED`, open the PR exactly as the handoff says with the
runtime's GitHub tool; with no such tool, hand the owner the printed base, head,
title, and body as one action. A handoff that says `draft=true` opens as a
draft, and the owner marks it ready on GitHub. A valid new-article PR publishes
automatically unless it was held.
