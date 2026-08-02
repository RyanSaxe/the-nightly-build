# Publish an article now

Read `docs/guides/publish/publish-now.md`, `docs/reference/series.md`, and
[prompt authoring](../craft/prompt-authoring.md).

Accept the user's actual starting point, whatever its form (e.g., a bare
topic, a link, a set of documents, etc.). Never require a link and never
mistake a link for a sufficient commission.

## Turn intent into a configured commission

Inspect the press and identify the natural existing home. Clarify the desired
article only where different answers would change the series, angle, evidence,
or urgency. Synthesize:

- the contribution and central question
- what the article must establish rather than merely mention
- starting material and the research still required
- relevant prior coverage and what must be new
- the template and any furniture the subject genuinely needs
- a stable slug and whether the user wants to review before merge

Give the article a configured home before production. What that requires
depends on the mode. A scheduled open series usually needs nothing; add the
item only when a commission queue is pending or the user wants the record. A
manual open series always needs a matching item. A collection takes any
configured unpublished item and a sequence only its next. A rolling series
publishes one dated edition per UTC day, so publishing now means today's
edition early. Publishing now never consumes a future slot: the scheduled run
skips the series only when it already carries an article dated the same UTC
day. If no existing series fits, discuss whether the request reveals a durable
new series or is outside the paper. Do not create a throwaway series to
satisfy one topic.

When configuration changed, validate it and get it merged into `main`. Then read
`../../nb-orchestrator/SKILL.md` and continue in this same agent as the
orchestrator, supplying this configured article as the exact authorized work.
Do not run `nb duty`, copy the production sequence into this workflow, or weaken
the required artifacts. A valid new-article PR publishes automatically.
