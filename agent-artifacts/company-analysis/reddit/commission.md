# Commission: company-analysis/reddit

## Assignment
- Series: company-analysis (Company Analysis). Template: `article`. Mode: open.
- Slug: `reddit`. Company: **Reddit, Inc. (NYSE: RDDT)**.
- Authorized by the 2026-08-03 `nb duty` result. One article only.

## The market question
Use Reddit's most recent quarter to investigate a larger market question:
**why the market can sell off a company that beat estimates and raised
guidance.** Reporting around the late-July/early-August 2026 print described
Reddit shares falling sharply (roughly -13%) despite solid results and guidance.
The instructive question is how markets price *expectations and forward
signals* (guidance quality, user-growth trajectory, ad-pricing durability,
valuation multiple) rather than the reported quarter itself. Teach the business
as part of the analysis. Do NOT issue a buy/sell/allocation call.

## Verify before building (researcher owns this)
The exact figures and the size/existence of the drop must be verified against
the primary record before the writer builds on them. If the freshest verifiable
quarter or the market reaction differs from the ~-13% framing above, the
research governs and the writer adjusts the question to what the record
supports. Consult the SEC filing itself (10-Q / 8-K / earnings release on
sec.gov) before the coverage of it (series `consult`: https://www.sec.gov/).
If Reddit's latest quarter turns out not to support a rich expectations-vs-
results piece, report that to the orchestrator before drafting rather than
padding.

## Required contribution
- Establish, chart-forward, the gap between what Reddit reported (revenue, DAUq,
  ARPU, profitability) and what the stock did, then explain the gap through
  expectations: the guide, the deceleration or acceleration in the numbers the
  market actually watches, and the multiple those numbers have to justify.
- Teach the mechanics generally enough that the lesson transfers beyond Reddit:
  a beat is measured against expectations, and price reacts to the change in
  expectations, not the level of results.

## Charts (this is the chart-forward desk)
Build charts ONLY from series the researcher verified against the owning
primary. Use `nb chart` and commit the `chart-N.py` provenance beside the
article. Candidate charts: quarterly revenue and/or DAUq trend with the
YoY growth rate; the guidance range vs. consensus; the stock's reaction. Label
axes, cite the data source in the caption, note any non-linear scale. Do not
chart a number that is not in the evidence record.

## Sources
- min_sources: 8 (article template floor). Primary: Reddit's SEC filing /
  earnings release (owns the financials); Reddit IR. Secondary: reputable US
  newsrooms for the market reaction and consensus context. Contested figures
  (consensus estimates, the exact % drop, intraday numbers) need a primary or
  clearly-owned source. Classify each source primary/secondary honestly. Every
  URL must resolve to the source's own page.

## Neighbors in this edition
investing/present-value runs tonight in the same Investing section and teaches
discounting/valuation from first principles. Keep this piece a market-reaction
case study; do not turn it into a valuation lesson or overlap its worked
example. Alphabet's AI-capex piece (2026-07-27) and Apple's services piece
(2026-08-01) are recent in this desk — Reddit's consumer-internet /
expectations angle is distinct; keep it so.

## Prior coverage — do not repeat, and break these shapes
Recent company-analysis: apple, boeing, alphabet, vertiv, coreweave. Deks state
a specific finding with a figure ("Boeing collected $4.7 billion of new customer
deposits..."). Keep that specificity but do not copy a prior structure or a
"masks / already exceeds" dek mold. Vary heading shapes.

## Form
Article template: `orientation` required + 2-6 flexible sections + Sources.
Word band 1500-4000. Charts and a stat strip fit this desk; a table for the
beat-vs-guide comparison is natural. Furniture carries evidence, not decoration.

## Harness / model record
Harness: Claude Code (Agent SDK), scheduled publication run. Roles run as
isolated subagents on `claude-opus-4-8` (satisfies `capable`/`inherit`).
Per-role reasoning effort is not independently settable through the subagent
interface; each role runs at the session's effort, the closest available option
to the policy's guidance. Editor: model inherit -> `claude-opus-4-8`, effort
target high (ran at session effort). Recorded as a deviation on effort only.

## Research correction (orchestrator, after researcher/01)
Research governs and sharpens the angle:
- The sell-off was ~**-21% close-to-close** (RDDT $178.04 -> $140.67, Jul 30->31,
  2026), not ~-13%. The -13% was the smaller after-hours way-station on the
  evening of the report. The writer states the ~-21% close-to-close figure and
  may note -13% as the after-hours way-station.
- The paradox holds but with a specific cause the headline hides: it was a real
  beat-and-raise (rev $804.9M +61%, EPS $1.25, Q3 guide above Street), yet US
  DAUq (53.2M) both MISSED consensus and fell SEQUENTIALLY (from 53.5M) — the
  first sequential US decline in the five-quarter series — with management citing
  "choppy" Google search referrals. The real story is a growth-durability signal,
  so the honest read is a plausibly rational reaction, not irrational punishment.
  Steelman both reads. This is the angle; do not frame it as "market punished a
  clean beat" without the DAU-durability cause.
