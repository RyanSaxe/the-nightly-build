# writer brief: investing/present-value (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `lesson` template identity, series prompt
- commission.md (artifact root) — the concept, where it sits in the syllabus, and shapes to break
- writing-coach/01/voice-guide.md — the voice, licenses, and do-not-reuse list for this piece
- researcher/01/evidence.md — the ONLY claim set available to you; use its Sources/Numbers/Contradictions exactly
- The initialized article at `library/investing/present-value.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/investing/present-value/library/investing/present-value.html --series investing`
  `./nb check .nb-work/investing/present-value/library/investing/present-value.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- CRITICAL framing correction from the evidence: the only real rate sourced is
  the U.S. Treasury 10-year par yield (4.75% as of 07/31/2026), which is the
  **risk-free floor**, not a company's cost of capital. Do NOT discount risky
  business cash flows at 4.75% and call it "the cost of capital" — that would
  contradict the prior WACC lesson. Present the Treasury yield as the risk-free
  anchor the discount rate is built up from, and note that a real cost of
  capital adds a risk premium (connect explicitly to the cost-of-capital lesson
  without reteaching it).
- The worked-table cash flows are teaching inventions; the evidence says so.
  Present them as illustrative, and flag the flat-rate / no-tax choices as
  teaching simplifications (Damodaran flags the tax point himself).
- Use the annotated equation furniture for the core PV identity
  PV = CF/(1+r)^t (at most one annotated equation), and a small table for the
  multi-year worked discounting. Set the growing-perpetuity form
  PV = CF/(r-g) with its r > g constraint to set up terminal value, and name
  what is deferred to a later DCF lesson.
- Lesson template: "Why this matters" opens, "The takeaway" closes (both
  written after the body, both citation-exempt); 0-4 flexible sections between.
  Word band 1200-2200. Keep it transferable; do not default to Costco.
