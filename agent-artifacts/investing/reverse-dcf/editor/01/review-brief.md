# editor review-brief: investing/reverse-dcf (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md
- commission.md            ../../commission.md
- writer brief             ../writer/01/brief.md
- voice-guide.md           ../writing-coach/01/voice-guide.md
- evidence.md              ../researcher/01/evidence.md
- draft-handoff.md         ../writer/01/draft-handoff.md (original-work sentence; the one intentional warning)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/investing/reverse-dcf/library/investing/reverse-dcf.html
- effective contract       /home/user/the-nightly-build/.nb-work/investing/reverse-dcf/.nb-context

Recent-pattern notes (compare dek, headings, edges against these for formula):
- Recent investing lessons anchor on a numeric reveal about a named company and repeatedly use a two-company comparison (Copart/Crocs, Coca-Cola/Verizon, Costco/peer). The writer used one company (Mastercard) and varied the dek; confirm it did not slip into a compare-two frame or a single-company valuation, and that the dek is not the "at $X, company is Y" mold.

This round's focus:
- The lesson's core is that market-implied growth is NOT a single number: verify the prose never presents it as a figure the market "quotes," and always attaches its frame (the piece shows 5.5% single-stage, 8.8% two-stage at 4% terminal, 10.5% at 3% terminal, plus discount-rate points). Confirm the contestable FCF base (stock-comp add-back, +/-$726M capitalized software) is named, per the earlier FCF lesson.
- One intentional proof warning stands: W-SENTENCE-DENSITY fires on the annotated reverse-DCF equation because the engine's density heuristic reads the `nb-math-eq` LaTeX as a sentence (nb-math-eq is not in its skip tags). Confirm this is the documented equation markup and that every genuine prose sentence clears the heuristic; treat the warning as a known engine false-positive, not a prose defect to fix.
- Inspect the value-vs-growth chart: compare its committed provenance numbers against the evidence record, and read the image as a reader (labels, scale, honesty). Route any chart correction to the writer, who holds the tooling.
- Dated inputs ($569.29 close 2026-08-14; 4.69% Treasury; ERP) are labeled as-of; that is correct. (If publication date slips materially, the price/yield refresh is an orchestrator/writer step at prepare-pr time, not your edit.)
- The lesson template allows its two bookend cards to address the reader; judge those sentences like any other (they must say something), but do not flag them for addressing the reader.
