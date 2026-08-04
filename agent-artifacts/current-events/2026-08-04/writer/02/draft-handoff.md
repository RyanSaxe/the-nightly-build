# Draft handoff: current-events/2026-08-04 (writer/02)

Targeted repair round. Only items 1 and 2 were touched; items 3–5 and sources
s2, s3, s5, s6, s7–s12 are byte-for-byte the editor-approved text. Source
numbering is unchanged (no renumber): the s1 and s4 slots were repointed in
place to the owning primaries.

## Original work

Unchanged from writer/01: the piece gathers five rules reaching legal effect and
dates each against its own fixed clock, so their shared shape (a rule biting
against a deadline) is visible without being asserted.

## Editorial-review items resolved (editor/01, Required work)

- **Item 1 — Sauer quote re-sourced to its owning primary, wording corrected.**
  The Solicitor General quotation now cites s1, repointed to the government's
  Application for a Stay in SCOTUS docket 26A124 (supremecourt.gov DocketPDF,
  `data-nb-kind="primary"`, `data-nb-locator="printed page 5"`). The word was
  corrected from "deliberate" to the verified **"deliberative"** ("preempts the
  Executive's deliberative policymaking"), per researcher/02. Not conflated with
  the nearby "irreparably and impermissibly impedes…" sentence.
- **Item 2 — rescission quote and May 18, 2026 date re-sourced to the owning
  primary.** Both now cite s4, repointed to the DOJ's own signed order
  (justice.gov, `data-nb-kind="primary"`, `data-nb-locator="Paragraph A"`):
  "…is rescinded and shall have no force or effect," attached to "the May 18,
  2026 order establishing the fund." The rescinded May 18 fund-establishing order
  is kept distinct from the separate May 19 mutual-release order.

## Structural deviation forced by the per-item source contract (editor: please note)

The brief directed **two** primaries into each of items 1 and 2 (item 1: docket
*and* stay application; item 2: Senate Judiciary page *and* DOJ order). The
series contract `per_item_sources: primary: [1, 1]` is a hard block — two
primaries in one item fails `B-SOURCE-KIND` ("item cites 2 primary source(s);
this series asks every item for exactly 1"), confirmed empirically. Because the
task's binding requirement is that each flagged **quote** resolve to its **owning
primary** at BLOCK: 0, I made that owning primary each item's single primary and
re-homed the displaced facts to secondaries that genuinely own them:

- **Item 1:** s1 is now the stay application (owns the Sauer quote). The docket's
  procedural facts moved to honest secondaries — "Justice Jackson called for that
  response" and the Aug. 3 opposition filing → Votebeat (s3, the Aug. 3 report of
  Jackson's response order); the "California + 22 states + D.C." party count and
  "twelve states led by Alabama" → SCOTUSblog (s2). Consequence: the docket page
  is no longer a cited source, and the Jackson clause sits on Votebeat (secondary)
  rather than the docket (primary) as the brief preferred — the only way to keep
  the Sauer quote on its owning primary under [1,1]. The item headline now links
  to the stay application. The editor's flagged semicolon ("…that response; twelve
  states…") is resolved: it is now two sentences, which also cleanly separates the
  two sources.
- **Item 2:** s4 is now the DOJ rescission order (owns the quote + date). The
  Senate Judiciary nomination page is no longer a cited source; the committee-vote
  fact now rests on the Washington Post (s6, which owns it) and the item headline
  links to the rescission order. NPR (s5) is retained as the independent secondary
  for the framing it still supports (the Aug. 2 signing / $1.8B, the Cornyn/Tillis/
  Murkowski state of play, the durability caveat).

Each item still carries exactly one primary + two independent secondaries.

## Display-text self-test (two changed items)

- Quotes verbatim against researcher/02; item-1 word corrected to "deliberative";
  item-2 quote is an exact substring of the order's operative sentence.
- Dates unchanged and consistent (Nov. 3, Aug. 3, June 25; Aug. 2, May 18, Aug. 4).
- `data-nb-kind="primary"` on s1 and s4; both hrefs resolve to the source's own
  page (SCOTUS DocketPDF for 26A124; DOJ-hosted order) — probed 206/206.
- nb-meta `dek` and the rendered dekline are identical (untouched).

## Proof

`./nb check … --series current-events --library <checkout>` **with links** →
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** `nb stamp`: words=933,
reading_minutes=4, sources=12. No warnings left standing.

## Open question for the orchestrator/editor

The brief's "two owning primaries per item" cannot coexist with the series'
`primary:[1,1]` contract. I resolved it in favor of the contract + the flagged
quotes on their owning primaries, at the cost of dropping the docket and Senate
Judiciary pages as cited sources and moving the Jackson clause to a secondary. If
the intent was instead to keep the docket/Senate-Judiciary primaries and accept a
paraphrase for one of the quotes, that is a commission call — flag it and I will
re-run.
