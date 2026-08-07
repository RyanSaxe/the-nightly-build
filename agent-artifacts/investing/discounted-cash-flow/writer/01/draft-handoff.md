# Draft handoff: investing/discounted-cash-flow (01)

## Original work
The lesson re-runs one illustrative firm one input at a time to show that the
same terminal value is at once the largest share of the answer (70-82% of firm
value across the whole r/g grid) and the most sensitive (a single-point move in
r or g swings firm value about a seventh), so "the terminal value dominates" and
"a DCF is an argument about assumptions" become one computed fact the reader can
reproduce from the page, not two asserted ones. The evidence supplied the grids;
the article's act is to fuse dominance and fragility into a single reading and
land the verdict on the tool rather than on any security.

## Proof
`./nb check ... --series investing` (links included): BLOCK: 0, WARN: 0,
PUBLISHABLE. Stamped words=2097 (band 1200-2200), reading 9 min, sources 6 (all
primary, first-citation order). No warnings left standing.

## Build decisions worth the editor's eye
- One chart (chart-1.py beside the article): firm value vs stable growth g, one
  line per discount rate r in {8,9,10}%, base case (r=9%, g=2.5%, ~$1,845M)
  marked. Explicit forecast held fixed, so the whole fan-out is the terminal
  value. Inspected the rendered PNG; axes labeled, growth kept below every r.
- One annotated equation (the DCF identity, colored FCFF_t / r / TV_n) and one
  bare equation (the Gordon terminal value). One worked buildup table (base case
  in four lines). One verdict note (nb-note-strong) for the tool verdict.
- The three live disagreements are weighed, not listed: exit-multiple vs
  perpetuity (in the terminal-value section, with the illustrative 25% method
  swing and Damodaran's "Trojan Horse" against Mauboussin's report of common
  practice); how to pick g (in the sensitivity section, the risk-free cap vs the
  purists' zero-growth camp); tool-vs-hand (its own closing section, Mauboussin
  and Fernandez and Damodaran's concession, resolved to the inputs).
- Real corroboration is cited as Damodaran's teaching cases, not filings: Tube
  Investments (~two-thirds terminal share) and the DaimlerChrysler firm-to-equity
  bridge. Built on the illustrative firm only; Costco and Apple avoided.

## Open question (modeling convention, for the editor)
The chart's data is this lesson's own computation on invented inputs, but the
proof's B-CHART requires the caption to cite a source *entry*. I cited s1
(Damodaran, the identity/terminal-value formula) for the *method* and used a
`data-nb-note` to state plainly that the figures are this lesson's own
computation. That keeps the numbers honestly attributed to the lesson while
satisfying the proof, but if the press wants a cleaner convention for
"own-computation" charts, this is the place it surfaces.

## Note on inspection
`nb render-check` reports no Chrome in this environment, so the rendered
equation/table/bookend layout could not be screenshotted; the chart PNG was
inspected directly and the structural proof (classes resolve, figure sized and
cited, KaTeX source present) passed clean.
