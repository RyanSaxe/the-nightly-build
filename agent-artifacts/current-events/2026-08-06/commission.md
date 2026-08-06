# Commission: current-events/2026-08-06

## Authorized work
Scheduled duty for 2026-08-06 returned `current-events` (rolling, daily) with
slug 2026-08-06 unpublished. This run commissions exactly that dated brief.

## Subject and selection
The US-focused general-news front page for Thursday, 2026-08-06. Select the
day's most consequential developments: favor events that change law, public
policy, public institutions, or people's material conditions. No topic quota,
no routine political theater, nothing merely popular. Include an international
story only when leaving it out would make the brief misleading, sized to its
importance. Put a technology story here only when its public consequences are
the news; developments in the field itself belong to the sibling Tech News
brief this same run (see coordination below).

## Template and geometry
Template `brief` (shortread). Items band [4, 6]. Cite rule per-item. Each item
is a full-sentence claim headline that says why it matters, then explains it —
this is an itemized roundup, not a prose essay. Use nb-brief-item per item;
add nb-stat / nb-table / rs-docket only where an item's evidence has that shape.

## Sources (per item)
Per-item floor: primary [1,1] (exactly one primary record that owns the event)
and secondary [1, null] (at least one independent account). Template brief floor
min_sources 5 overall. For independent reporting prefer a reputable US newsroom
of comparable quality; use the primary record regardless of country, and use
non-US reporting when it holds important original reporting or is closer to the
event. Every number verified against the primary that owns it.

## Coordination with the sibling Tech News brief (same run, same date)
Both briefs publish for 2026-08-06. Do not double-cover the same story. This
brief owns public-consequence news (law, policy, institutions, material
conditions, elections, courts, economy, public health, disasters). Field/
industry technology and AI research developments go to tech-news. If a tech
story's public consequence is the news (e.g. a regulation, a breach affecting
the public), it may live here; the underlying field development does not.

## Production policy (resolved via `nb production-policy`)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model inherit, effort high, REQUIRED

Actual harness: roles run as isolated Claude subagents on model
`claude-opus-4-8` (capable tier; required editor "inherit" resolves to this
correspondent model). Deviation recorded: this runtime's subagent launcher does
not expose a per-invocation reasoning-effort control, so the required editor
"high effort" is approximated by the most capable available model at the harness
default effort. No model was traded down.

## Neighboring articles this run
tech-news/2026-08-06 (sibling brief), company-analysis/eli-lilly,
paper-of-the-day/instructgpt, parenting-research/teething,
word-of-the-day/luddite.

## Recent current-events coverage and habits not to inherit
Recent editions (2026-08-01..05) covered: the record lettuce/Cyclospora
outbreak deaths, Spokane wildfire and arson arrest, 25 states suing over new
tariffs, Trump's mail-ballot Supreme Court request, the Iran strike
reversal, Q2 GDP 1.5% and Fed dissents. Do not recap or re-lead with a story
already covered unless there is a genuinely new development on 2026-08-06.
Habits to break:
- Recent deks use a "from X to Y" span / comma-triad shape ("from Spokane's
  arson arrest to 25 states suing"). The headlines guide bans the comma-triad
  dek; write a dek that commits to one stance, not a tour.
- Vary item-headline cadence; do not stack same-shaped clauses.
Required furniture (nb-brief-item, Sources) is not a habit to avoid.

## Original contribution expected
A selective, correctly-sourced front page that tells the reader what actually
mattered on 2026-08-06 and why, each item resting on the primary record plus an
independent account.
