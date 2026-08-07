# editor review-brief: investing/discounted-cash-flow (editor/01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../writer/01/brief.md                — the exact writer brief (leakage check)
  ../../writing-coach/01/voice-guide.md   — the craft standard
  ../../researcher/01/evidence.md         — the evidence record (with the grid)
  ../../writer/01/draft-handoff.md        — original-work sentence + open questions
  ../../../../library/investing/discounted-cash-flow.html   — the lesson to review
  ../../../../.nb-context/                 — effective template contract + furniture
Output: editor/01/editorial-review.md

Round focus:
- Arithmetic is the top risk. RECOMPUTE the illustrative firm yourself: FCFF
  $100M growing 8%/yr for 5 explicit years, r=9%, g=2.5% — the explicit-period
  PV, the Gordon terminal value TV=FCF_6/(r−g), its discounted value, the sum
  (enterprise value), and the terminal-value share. Check the claimed grid
  (TV share 70-82% across r∈{8,9,10}%, g∈{1.5,2.5,3.5}%) and the "~1/7 swing per
  point" against your own numbers. Any mismatch between prose, table, chart, and
  evidence is a required fix.
- Chart (chart-1.py): read its committed provenance and compare its numbers to
  the computation and the evidence grid; read the image as a reader (axes,
  legend, g kept below r, honest scale). Judge the own-computation caption
  convention (s1 for method + data-nb-note stating the figures are the lesson's
  own computation) against the citation standard — honest and passing is fine;
  do not invent a stricter rule late.
- Sourcing: Tube Investments (~66% TV) and DaimlerChrysler (bridge) cited as
  Damodaran teaching cases, not filings; Mauboussin & Callahan 70-80% anchors
  "terminal value typically dominates," not a false constant. Contradictions
  (how to pick g; exit multiples in a DCF; sensitivity indicts method or users)
  are weighed, not just listed.
- Continuity/teach: builds on prior lessons (PV, FCF, WACC) by reference without
  re-deriving; enterprise→equity bridge correct; no Costco/Apple. Verdict on the
  tool, not a security. Formula/display: headline off the recent "single concrete
  company fact" mold; dek commits.
Make surgical cuts directly; run ./nb stamp after direct cuts. Route new prose,
markup, chart, or proof to the writer. Decide approve | revise.
