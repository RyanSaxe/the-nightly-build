# Draft handoff: current-events/2026-08-02 (writer, invocation 01)

## Original-work sentence

Where every independent secondary on the Iran item repeats Trump's "deal"
claim without checking it, this piece traces that claim to its single source
(Trump's own post), stacks it against his own documented history of making
the same false Hormuz claim, and — for measles — separates two determinations
almost every outlet conflates (the Americas region's lost status vs. the
U.S.'s own status, still under review) into a two-row timeline so the
correction is visible at a glance, not just asserted in prose.

## Paths changed

- Article: `/home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html`
- No assets or charts added (no verified series existed for a chart; no
  exact cited visual existed for an asset capture, per the evidence record's
  own "Source assets" section).
- Furniture used: `rs-docket` (item 2, TPS case) and `nb-timeline` (item 3,
  region-vs-US elimination dates) — both directly requested or suggested by
  the evidence record as carrying a shape prose would hide.

## Proof result

`nb check ... --series current-events --library /home/user/library` (default
link-checking on, matching the brief's exact command):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

No warnings left standing.

## Source-kind judgment call (flag for editor)

The series' `per_item_sources` policy caps every item at exactly one
`primary`. Two items had two genuinely primary-type sources in the evidence
record:

- **Item 1 (Iran):** both Trump's Truth Social post and the U.S. Embassy
  Jerusalem security alert are self-owned government/party statements. I kept
  Trump's post as the item's sole tagged primary (it is the item's central,
  disputed claim) and dropped the embassy alert as a separately numbered
  source rather than mislabel it — NBC (secondary) already carries the
  travel-warning facts independently, so no claim lost its citation.
- **Item 3 (measles):** both CDC's case data and PAHO's elimination-status
  determination are self-owned primary documents. The brief explicitly
  designated "Primary: CDC data" for this item, so I followed that and tagged
  PAHO `secondary` in `data-nb-kind`, even though PAHO's page is, in
  isolation, a primary statement by the body that owns that determination.
  Every PAHO-sourced claim in the prose still names PAHO as the authority
  making it. Flagging this explicitly since it is a judgment call under a
  hard per-item ceiling, not a claim about PAHO's actual authority.

## Evidence caveats obeyed

- Iran "deal": reported throughout as Trump's own unconfirmed claim, never as
  settled fact; his prior false Hormuz claims are stated as a documented
  pattern (Washington Post, via RawStory).
- Somalia TPS: the Aug. 1 stay is attributed to court reporting (Fox News,
  corroborated by yourNEWS), not to a document read directly — the order
  itself was gated behind PACER.
- Measles: the piece states plainly that the U.S. has not lost elimination
  status; only the Americas region has (driven by Canada), and the U.S.'s own
  review is due November 2026 — carried in both prose and the timeline.
- travel.state.gov (403-gated) is never cited directly; NBC's independent
  reading of it is used instead, as the brief instructed.

## Remaining questions

None. All four items cleared with a primary plus independent secondary(s),
every name/title verified against the owning primary and cross-checked
against each outlet's live page (Murguía/UnidosUS, Proaño/LULAC Institute,
Sanchez Barba/Mi Familia en Acción, Pichardo/Latino Victory Foundation;
Burroughs/D. Mass.; Percival/DHS; Noem/DHS), and nb-meta reflects measured
values (13 sources, 1,081 words, 5 min read).
