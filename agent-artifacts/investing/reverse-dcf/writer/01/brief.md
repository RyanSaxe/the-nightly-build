# writer brief: investing/reverse-dcf (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md (house standard, press voice, series prompt, lesson-template identity)
- commission.md            ../../commission.md (concept, syllabus place, form, boundaries)
- voice-guide.md           ../writing-coach/01/voice-guide.md (how this lesson should sound; exemplar passages)
- evidence.md              ../researcher/01/evidence.md (method sources + the Mastercard worked example; read Numbers and Contradictions closely)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/investing/reverse-dcf/library/investing/reverse-dcf.html
- effective contract       /home/user/the-nightly-build/.nb-work/investing/reverse-dcf/.nb-context

Output: /home/user/the-nightly-build/.nb-work/investing/reverse-dcf/agent-artifacts/investing/reverse-dcf/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/investing/reverse-dcf/library/investing/reverse-dcf.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/b3d5d9d7-6994-5933-851f-0ef1bb302a4b/scratchpad/library-checkout

This round's focus (decisions the evidence carries and must not be lost):
- Teach only the inversion and how to reason about the expectations it exposes; rely on the prior lessons (DCF, terminal value, cost of capital, FCF, margin of safety) rather than re-deriving them. Locate the lesson between margin of safety's conservative/optimistic values: reverse DCF reads what the current price already assumes.
- Use one company (the evidence supplies a fully verifiable Mastercard example: FCF base $16,433M, 876.0M shares, $569.29 price as of Aug 14 2026, with balance-sheet cash and debt) to make the inversion concrete, but keep the method transferable. Do not make it Peloton, and do not turn it into a single-company valuation or a compare-two-companies piece.
- The core caveat IS the lesson: the implied-growth number is not unique. On the same stock it swings ~5.5% (single-stage) to ~8.8% (two-stage, 9% cost of equity, 4% terminal) to ~10.5% (3% terminal). Always present implied growth as conditional on the assumed discount rate, terminal growth, and horizon. The value-vs-growth sensitivity series is the natural chart (nb chart, verified series only).
- The FCF base is itself contestable (the earlier FCF lesson's point): Mastercard's operating cash flow includes a non-cash stock-comp add-back, and whether to subtract capitalized software moves the base ~$726M. Name that different defensible bases yield different implied growth.
- Dated inputs (the $569.29 price, the 4.69% 10-year Treasury) must be labeled as of their date. Do not cite "Everything Is a DCF Model" as read — it was gated; cite the authors' own Expectations Investing site and Damodaran for the framing.

Form: lesson template. Its two bookend cards may address the reader directly (the only allowed self-address); each such sentence must still say something. Word band 1200-2200; source floor at least 6. Vary the dek from the recent "at $X, company is Y" numeric-reveal mold. Fill nb-meta harness and writer-model fields; nb stamp writes counts.
