# Commission: tech-news/2026-08-03

## Assignment
- Series: tech-news (Tech News). Template: `brief`. Mode: rolling.
- Slug: `2026-08-03` (the selected UTC date, unpublished).
- Authorized by the 2026-08-03 `nb duty` result. One brief only.

## What the brief is
The daily technology front page for 2026-08-03: **4 to 6 items**. Artificial
intelligence is central, but significance decides the mix. Product promotion,
incremental releases, and online attention do not qualify on their own. Science
and health belong when a result changes technical knowledge or practice enough
to deserve attention here; treat the research itself as the development.

## Item selection (researcher owns this)
The day's record decides the items. Select the most consequential technology
developments datelined on or freshly developing around 2026-08-03 (a
paper/preprint, a model or system release that matters, a security disclosure, a
regulatory/standards action with technical weight, a funding or corporate move
that changes the field). Verify each against its primary record. Search for what
the announcement leaves out; a brief that repeats a press release has underused
the record.

## Per-item sourcing (strict)
Each item carries **exactly one primary source** (the paper, the vendor's own
release/model card, the disclosure, the filing) and **at least one independent
secondary account**. The headline links to the primary; item prose carries the
detail. Two retellings of one origin count as one. Prefer a reputable US
newsroom for independent reporting when quality is comparable; use the primary
regardless of country. Every URL must resolve to the source's own page.
- Template floor min_sources: 5 overall; the per-item rule is the real
  constraint (4-6 items x >=2 sources).

## Coordinate with tonight's Current Events brief
current-events/2026-08-03 runs tonight and takes technology only when its
public/policy consequence is the story. Keep Tech News on the field's own
developments and do not run the same development in both briefs.

## Prior coverage — do not repeat, and break these shapes
Recent tech-news briefs (2026-07-27 .. 2026-08-02) centered on: Claude finding
cryptographic weaknesses in post-quantum candidates (HAWK/NIST), GPT-5.6 and an
80% price cut, the Ruflo agent CVSS-10 disclosure, Nvidia's AI-security alliance
and its SSI investment, Kimi K3. Do not re-run these unless a genuinely new,
day-dated development advances the story; if so, report what changed on
2026-08-03. Vary dek/headline shapes; avoid the semicolon-reversal and
comma-triad dek molds and the "triad of paired adjectives" headline.

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
