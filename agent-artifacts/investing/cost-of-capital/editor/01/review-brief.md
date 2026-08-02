# Editor review-brief: investing/cost-of-capital (01)

## Your job
Give this drafted `lesson` the three ordered reads (skeptic, cut, reader) and
either approve it (`DONE editor`, no required change) or route numbered repairs.
Cuts/small fixes go directly in the article; new prose past a word/clause returns
to the writer; evidence gaps to the researcher.

## Begin with these exact inputs
- This brief; `../../editorial-direction.md`; the exact writer brief
  `../../writer/01/brief.md` (prompt-leakage detection); voice guide
  `../../writing-coach/01/voice-guide.md` (read first); evidence record
  `../../researcher/01/evidence.md`; draft handoff `../../writer/01/draft-handoff.md`;
  article `/home/user/the-nightly-build/.nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html`;
  template context `../../../../.nb-context/` (incl. lesson furniture.md).

## What to check hardest (this lesson's risk surface)
- **Every number recomputed against the owning primary** (evidence record): the
  10-Yr Treasury yield 4.75% (2026-07-31); the implied ERP 4.23% — confirm it is
  framed as Damodaran's *dated* estimate, not "the" ERP, with the ~3.9-6.2%
  historical range noted; the worked cost of equity (~9%) with the β=1 assumption
  stated plainly; Costco's ROIC (~42% / ~39.5%); AEP's earned-vs-approved ROE
  (APCo/WPCo ~7.9-8.2% vs 9.75%; KPCo 4.4% vs 9.75%); AEP's 2025 debt issuance
  cost anchor (5.38-5.85%).
- **The basis-mismatch caveat (obey)**: confirm the lesson uses AEP's *earned ROE
  vs approved ROE* (equity basis) as the hurdle illustration and does NOT
  naively compare AEP's consolidated ROIC (total-capital basis) to its authorized
  ROE. The writer says it named and rejected that wrong comparison as a teaching
  moment — verify that reads as genuine teaching, not confusion.
- **No unverified claim**: the Feb 2026 WV PSC order / "$15M" detail must be
  ABSENT. AEP's 3.37% effective tax rate: the writer says no AEP ROIC/after-tax
  figure appears — verify.
- **Lesson form**: fixed order (Why this matters → body → The takeaway); bookends
  written for THIS lesson's particulars (the hurdle, Costco above it, AEP at/below
  it), resolving as setup and payoff, teaching nothing new in the takeaway. Fixed
  chrome (name lines, "Background"/"Go deeper", "optional reading") exact.
  Background links to `return-on-capital` (and the balance-sheet lesson) resolve
  and the lesson still works for a reader who opens none of them. ROIC restated in
  one plain sentence before use (built-before-used discipline).
- **Teach-completely**: 2-3 ideas taught fully; every abstraction grounded in a
  worked number; one term per idea kept (cost of capital / hurdle rate — check it
  doesn't drift). Reported fact, estimate, and synthesis kept distinct.

## Standards to apply in the cut
Full house prose/punctuation floor. Compare opener, headings, dek, and the
comparison table against the recent investing library (opening on a company fact
by reflex, a Costco/quarterly-earnings walkthrough, comma-and-clause heading
cadence). Cut prompt leakage (planning labels, "this lesson teaches").

## Output
Write `editorial-review.md` here with the three required lines, direct edits,
required work by owner, final decision. If you edit, note whether a re-proof is
needed
(`nb check .../cost-of-capital.html --series investing --library /home/user/library`).
Return `DONE editor <path>` only if no redraft is required, else a
`REQUEST writer/researcher <one-sentence>` line.
