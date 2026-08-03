# writer brief: investing/present-value (02)

Inputs:
- editorial-direction.md (artifact root) — the standard
- commission.md (artifact root) — the concept, syllabus placement, sourcing floor (6)
- writing-coach/01/voice-guide.md — the voice (unchanged from round 01)
- researcher/02/evidence.md — the COMPLETE new evidence record (8 sources; carries the round-01 entries forward and adds OpenStax Principles of Finance 9.1/8.1/15.3 and FRED DGS10). This is now your claim set.
- writer/01/draft-handoff.md — your prior draft handoff
- The article you already wrote at `library/investing/present-value.html` (workspace root) and `.nb-context/`
Output: writer/02/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/investing/present-value/library/investing/present-value.html`   (file arg only; no --series)
  `./nb check .nb-work/investing/present-value/library/investing/present-value.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Run until `BLOCK: 0` and clear W-SOURCES-MIN.

This round's focus (evidence expansion only — do NOT expand the claim set):
- The prior draft passed BLOCK:0 but warned W-SOURCES-MIN (4 vs floor 6).
  Round-02 evidence adds independent authorities that OWN claims the lesson
  already makes. Attach them to EXISTING load-bearing statements so the piece
  clears 6 sources honestly, not by adding new claims or decoration:
  - OpenStax 9.1 (Timing of Cash Flows) is a second owner of PV = FV/(1+i)^n
    and the discount-each-flow-then-sum method (your worked table).
  - OpenStax 8.1 (Perpetuities) is a second owner of PV = C/r and PV = C/(r−g).
  - OpenStax 15.3 (CAPM) OWNS the bridge Re = Rf + risk premium and names
    Treasury securities as the risk-free proxy — cite it exactly where the piece
    builds the discount rate as risk-free floor + risk premium (this closes the
    round-01 gap; keep the framing that the Treasury rate is the floor, not a
    company's cost of capital).
  - FRED DGS10 is a second, independent owner of the 10-year Treasury anchor
    (4.68% constant-maturity 07/30/2026). Attribute each rate to its owner:
    4.75% par yield (Treasury, 07/31) vs 4.68% constant-maturity (FRED, 07/30)
    — a construction/date difference, not an error; do not blur them.
- Preserve all settled prose. Renumber sources in first-citation order.
- Re-run the full proof (links on) until BLOCK: 0 with no W-SOURCES-MIN. Write
  writer/02/draft-handoff.md with one line per change and the (unchanged)
  original-work sentence.
