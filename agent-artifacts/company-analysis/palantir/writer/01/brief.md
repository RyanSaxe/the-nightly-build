# writer brief: company-analysis/palantir (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the company, the market question, boundaries, shapes to break
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this piece
  ../../researcher/01/evidence.md           the complete evidence record; the only claim set available
  the initialized article and its .nb-context (article template contract + furniture catalogs)
Output: agent-artifacts/company-analysis/palantir/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/company-analysis/palantir/library/company-analysis/palantir.html --series company-analysis --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/company-analysis/palantir/library/company-analysis/palantir.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus (1500-4000 words; chart-forward; NO buy/sell/allocation call):
- The evidence corrects several framing points from the commission — follow the evidence,
  not the commission, wherever they differ: the report date is **August 3, 2026** (not
  Aug 5); do **not** claim a "triple-digit P/E" (forward P/E ~85x is secondary and the
  company gives no EPS guidance) — anchor valuation on the **forward EV/sales ~41–45x**
  computed from the 10-Q share count and a dated price. The acceleration is **U.S.-only**
  (international grew ~34% YoY); GAAP net income is flattered by a ~1.4% effective tax rate
  and adjusted net income is actually below GAAP; and the stock entered the print ~40%
  below its 52-week high, which complicates a simple "priced for perfection" read. Engage
  that complication rather than ignoring it.
- Chart: the verified U.S. commercial revenue series ($306M → $764M across Q2'25–Q2'26) is
  chart-ready and honest — build it with `nb chart` from the evidence's verified series,
  inspect the rendered PNG, commit the provenance script (spec/charts.md), and caption with
  the source. For a valuation-in-context chart the evidence has **no** clean single-as-of-
  date peer set (peer multiples are scattered/gated) — either source one properly yourself
  and cite it, or omit that chart and make the valuation point in prose or a small table
  with the forward EV/sales figure. Do not fabricate or mismatch-date peer multiples.
- Teach the business (Gotham/Foundry/AIP, government vs. U.S.-commercial) where it clarifies
  the argument, not in a boxed overview. Keep GAAP and adjusted distinct. NDR is not
  disclosed — do not cite one.
- Answer the market question on the evidence: what forward assumptions the price embeds and
  what in the record would falsify the bull case; steelman both the durable-compounder and
  the one-stumble-away reads. Close without advice.
- Break the recent CA dek molds ("X masks Y," "X came from A not B," "X keeps rising as Y
  keeps falling"). Read the filing before any coverage. Outline before naming flex sections.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8".
