# editor review-brief: investing/present-value (editor/01)

Inputs:
- editorial-direction.md (artifact root) — the standard to enforce
- writer/02/brief.md and writer/01/brief.md (the exact writer briefs — for instruction-leakage detection)
- commission.md (artifact root) — the concept, syllabus placement, and the CRITICAL risk-free-vs-cost-of-capital framing
- writing-coach/01/voice-guide.md — the voice, licenses, do-not-reuse list
- researcher/02/evidence.md — the current evidence record (8 sources); researcher/01 is the prior
- writer/02/draft-handoff.md — open the original-work sentence only on the third read
- The article at `library/investing/present-value.html` (workspace root) and `.nb-context/` template context
Output: editor/01/editorial-review.md

Recent-pattern notes: recent lessons lean on a Costco/AEP figure in the opener/dek;
that reflex is barred here. Vary heading shapes from prior lessons.

Round focus:
- CRITICAL: verify the piece never calls the Treasury yield "the cost of
  capital." It must present the Treasury/FRED rate as the risk-free FLOOR, with
  a company's cost of capital = risk-free + risk premium (cited to OpenStax
  15.3/CAPM), linking to the prior WACC lesson without reteaching it. If the
  worked table discounts risky cash flows at the risk-free rate and calls it the
  cost of capital, that is a required fix.
- Recompute the worked-table arithmetic ($100/yr x 4 at 4.75% -> ~$356.67; the
  one-year $95.47) and check the annotated PV equation and the growing-perpetuity
  form (PV = CF1/(r-g), r>g, CF1 = next year). Confirm the two rate figures are
  attributed to distinct owners (4.75% par yield Treasury 07/31 vs 4.68%
  constant-maturity FRED 07/30) and not blurred.
- Confirm the round-02 sources attach to claims the lesson actually makes (not
  padding to hit the floor), and every data-nb-kind is right.
- Lesson bookends: "Why this matters" opens and "The takeaway" closes, both
  written to fit the body and both citation-exempt. Confirm the takeaway names
  what is deferred to a later DCF lesson without overreaching.
- Open every citation href as printed; it must resolve. Make surgical cuts;
  route any redraft. After direct cuts run `./nb stamp <article-path>` (file arg).
