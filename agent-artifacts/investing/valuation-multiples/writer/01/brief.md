# writer brief: investing/valuation-multiples (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson template, series prompt
- ../../commission.md — the ideas taught, the order, and the worked contrast
- ../../writing-coach/01/voice-guide.md — how this lesson should sound
- ../../researcher/01/evidence.md — the definitions, the justified-multiple derivation, the three companies' verified figures, and the cautions
- article: .nb-work/investing/valuation-multiples/library/investing/valuation-multiples.html (initialized; edit it)
- template context: .nb-work/investing/valuation-multiples/.nb-context/ (contract, runtime assets, furniture)

Output: draft-handoff.md (this directory)

Proof: ./nb check .nb-work/investing/valuation-multiples/library/investing/valuation-multiples.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

This round's focus:
- 1200 to 2200 words. Teach two or three ideas completely: what a multiple is and how comparables valuation works; the justified multiple as a DCF compressed into one number; and why a low multiple is not automatically cheap. Fixed order: Why-this-matters bookend, body, The-takeaway bookend, bookends written after the body. Link the discounted-cash-flow, cost-of-capital, and free-cash-flow lessons in Background rather than re-teaching them.
- Set the derivation with the template's math furniture. Use the evidence's three companies (NVIDIA, Coca-Cola, Verizon), not Costco or Apple.
- Two cautions from the evidence you must honor in the prose:
  1. Name the denominator every time a multiple appears. NVIDIA is 46x on last full fiscal year, ~34x trailing, ~22x forward, and all three are legitimately "the P/E." A multiple without its denominator is ambiguous.
  2. The derivation gives the multiple a business deserves from its fundamentals; it is not proof that the market's quoted multiple equals that justified number. Relative valuation inherits the market's mispricing. The lesson's safe claim is that different fundamentals justify different multiples, not that the observed multiple is always fundamentally correct. Verizon is the "cheap is not cheap" case: a low multiple on a business whose EPS fell and which carries heavy debt.
- Entity precision: all Coca-Cola figures are The Coca-Cola Company (KO), not Coca-Cola Consolidated (COKE, the bottler). Keep KO's EV/EBITDA out of the core contrast; the evidence marks it approximate.
- If a chart earns its place (for instance justified multiple against growth, or the three companies' multiple against their fundamentals), build it only from the evidence record's verified series with `nb chart`, inspect the image, and commit its provenance.
- Do not open on the DCF lesson's shapes (a share-of-value number, or a "is the tool broken or the hand" turn). Name the piece's one act of original work in the handoff. Run the display-text pass, then `nb stamp` and the exact `nb check` (links included) until BLOCK: 0.
