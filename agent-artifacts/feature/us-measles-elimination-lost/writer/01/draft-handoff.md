# writer handoff: feature/us-measles-elimination-lost (01)

## The original work

The article separates the one segment of the chain that public documents put past
12 months, Utah's from 19 June 2025, from the West Texas antecedent that exists
only as ProPublica's genomic inference against CDC and HHS denials, and dates both
on a single timeline that marks which links a health department recorded and which
an analyst inferred. No source does this: the CDC's own report is confidential, and
each public document covers only its own outbreak.

That work is visible in Fig. 2, where the Texas-to-Utah arrow is dashed and labelled
as an inference while the Utah-Arizona connector is a recorded joint investigation,
and in the closing table, which grades each candidate chain by what joins it.

## Proof

`nb check ... --series feature --repo /home/user/the-nightly-build` with link
checking: **BLOCK: 0, WARN: 0, PUBLISHABLE**. 1,185 words against the 600-1,200
strict band, 20 sources, four flex-eligible sections (one anchor plus three).

No warning left standing.

## Judgement calls the record does not carry

- **Headline.** "The measles chain that ran a full year is Utah's" states the finding
  the piece defends and does not assert PAHO has announced anything. The dek carries
  the status ("PAHO has not announced the decision"). The commission's framing of a
  chain starting in Texas is treated as the disputed antecedent, per the production
  decision.
- **The 12-month crossing is attributed, not asserted as PAHO's.** Brewer (STAT),
  KFF and CNN put it on Utah; PAHO's own wording is not public, so the piece never
  says PAHO found Utah's chain specifically.
- **Fig. 1 carries the case totals as context only**, and the prose says in two
  sentences that the totals are why the review happened and not what it measured.
- **South Carolina's duration** is given as "about five months" rather than as a
  distance from the threshold: SC DPH gives October 2025 (no day) to 15 March 2026,
  which does not support a precise gap.
- **Genome schematic (Fig. 3).** Positions along the genome are drawn for legibility
  and the drawing says so, because ProPublica's published analysis gives the count of
  differing positions and not their coordinates. The five shared mutations are drawn
  taller as well as coloured, so the distinction survives in both themes.
- **MMR coverage was omitted.** The verified endpoints alone would have made a
  coverage visual without a trend, and the piece has no room for a fourth visual
  inside the band.
- **PAHO Situation Report 15** (the Rt of 1.49, the communication-coordination bullet)
  was cut for the word band. It is the best primary evidence that a conclusion existed
  before any announcement, and an editor who wants that point can have it in the
  closing section if something else goes.

## Visuals checked

Rendered through `nb preview` and captured with Playwright at 390px and 1280px, in
light and dark, full page plus each figure and the table. Two label collisions in the
timeline (the ProPublica arrow label, the Utah-Arizona connector label) and clipped
row labels in the genome schematic were found that way and fixed. The table scrolls
horizontally on a phone, which is the runtime's own behaviour for `nb-table`; the
date columns were shortened so the argument column starts closer to the left edge.
No console errors in any theme or width.

## Open questions

None blocking. One for the editor: the piece cites 20 sources against a floor of
five, which is heavy for a five-minute read. If that reads as padding, the NBC entry
(O'Neill) and the AP entry (HHS) are the two whose claims could be carried by the
Reuters January 2026 report instead, at the cost of two named rebuttals losing their
owning document.
