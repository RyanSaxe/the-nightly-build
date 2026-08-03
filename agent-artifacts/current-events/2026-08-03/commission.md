# Commission: current-events/2026-08-03

## Assignment
- Series: current-events (Current Events). Template: `brief`. Mode: rolling.
- Slug: `2026-08-03` (the selected UTC date, unpublished).
- Authorized by the 2026-08-03 `nb duty` result. One brief only.

## What the brief is
The US-focused general-news front page for 2026-08-03: **4 to 6 items**, kept
selective. Favor developments that change law, public policy, public
institutions, or people's material conditions. Routine political theater and
merely-popular stories do not qualify; do not fill a topic quota. Include an
international story only when leaving it out would make the brief misleading,
and size it by importance. Put technology here only when its *public
consequences* are the news; developments in the field itself belong to Tech
News (which also runs tonight — coordinate so items do not duplicate).

## Item selection (researcher owns this)
The day's record decides the items. Select the most consequential US
developments datelined on or freshly developing around 2026-08-03. For each
item verify what actually happened against its primary record before it is
written. Search for what complicates the obvious read; a brief that only
repeats a wire's framing has underused the record.

## Per-item sourcing (strict)
Each item carries **exactly one primary source** (the record that owns the
claim: the ruling, filing, agency release, official statement, transcript) and
**at least one independent secondary account** (prefer a reputable US newsroom
when quality is comparable; use non-US or the primary regardless of country
when it is closer to the event). The headline links to the primary; the item
prose carries the detail from the cited sources. Two retellings of one origin
count as one. Every URL must resolve to the source's own page.
- Template floor min_sources: 5 overall; the per-item rule above is the real
  constraint (4-6 items x >=2 sources).

## Coordinate with tonight's Tech News brief
tech-news/2026-08-03 covers the field's own developments. Current Events takes
a technology item only when its public/policy consequence is the story. Do not
run the same development in both briefs.

## Prior coverage — do not repeat, and break these shapes
Recent current-events briefs (2026-07-26 .. 2026-08-02) centered on: US-Iran
conflict and a canceled strike, the economy/Fed dissents, the Blanche AG
nomination fight, the voter-list order litigation, the Rogoff firing suit. Do
not re-run a prior day's item unless there is a genuine, newly-owned
development dated to 2026-08-03; if you carry a running story forward, the item
must report what changed on this date, cited to that day's record. Vary the dek
and headline shapes from recent briefs (avoid the semicolon-reversal and
comma-triad dek molds).

## Form
Brief template: `items` section (4-6 `nb-brief-item` blocks, each with a topic
tag, a headline linking to the primary, and 1-3 sentences) + Sources. Class
shortread. The dek is the night's through-line in one sentence, a stance not a
topic list.

## Harness / model record
Harness: Claude Code (Agent SDK), scheduled publication run. Roles run as
isolated subagents on `claude-opus-4-8` (satisfies `capable`/`inherit`).
Per-role reasoning effort is not independently settable through the subagent
interface; each role runs at the session's effort, the closest available option
to the policy's guidance. Editor: model inherit -> `claude-opus-4-8`, effort
target high (ran at session effort). Recorded as a deviation on effort only.
