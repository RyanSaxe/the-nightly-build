# Commission: current-events/2026-08-10 (rolling)

## The brief

Select the day's most consequential developments in the United States for
2026-08-10: four to six items that change law, public policy, public
institutions, or people's material conditions. Do not fill a topic quota, and do
not include routine political theater or merely-popular stories. Include an
international item only where leaving it out would make the brief misleading, at a
weight that matches its importance. Technology belongs here only when its public
consequences are the news; developments in the field itself go to Tech News.

## Candidate raw material (verify and select; not a required list)

The day's record around this date includes: a shift in the September Federal
Reserve rate outlook after a weak hiring print; a federal restriction barring
harm-reduction grant money from paying for drug-checking test strips; a review of
the country's measles-elimination status after a surge of 2026 outbreaks; and a
fight over who pays to expand energy infrastructure for data centers that each
draw as much power as a midsize city. These are leads to confirm against primary
records, not items to publish on trust. Select by consequence, not by this list.

## Do not re-report

The 2026-08-08 and 2026-08-09 briefs already led on the Todd Blanche attorney-
general confirmation, the July payrolls print (a 23,000 decline with downward
revisions), and the birthright-citizenship / birth-tourism executive order. Cover
a genuinely new development of the day, or a materially new turn in a running
story, rather than restating what those briefs carried.

## Required contribution

Each item earns its place by consequence and carries the reader to what actually
changed and why it matters, with the primary record cited. The brief reads as one
selective front page, not a feed.

## Template, sources, furniture

Template: `brief`. Each item is its own section with `nb-brief-item`; the lead
item sets the brief's headline and dek. Per the source policy, every item carries
exactly one primary record and at least one independent account. Use `nb-table`
only where an item's numbers are clearer shown than told.

## Recent habits not to inherit

Recent briefs headline the lead item as a plain subject-verb-surprise claim, which
is right; write each item's headline and dek fresh against `spec/headlines.md` and
avoid the negative-parallelism and comma-triad dek molds. Vary how item headings
are built across the brief.

## Runtime

Harness `claude-code-routine`; model Opus 4.8 for every role. Production policy
asks researcher/high, writer/medium, writing-coach/low, editor/high (required).
Per-invocation reasoning effort is not separately settable through this runtime's
child launches, so each role runs at the session's effort; the editor gate is
preserved in full. Writer records `harness: claude-code-routine` and
`model: Opus 4.8` in nb-meta.
