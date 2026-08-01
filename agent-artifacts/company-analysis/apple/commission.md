# Commission — company-analysis/apple

## Assignment
One Company Analysis on the `article` template (1500–4000 words), chart-forward.
Public company: **Apple Inc. (AAPL)**, using its fiscal Q3 2026 results (quarter
ended June 27, 2026, reported 2026-07-30) as the occasion. **No buy/sell/
allocation call.**

## Market question (the real subject)
Is Apple a services compounder or a hardware-cycle company, and what does this
quarter say? The record makes the question answerable now: total revenue set a
June-quarter record (~$109.4B, +16% YoY) but the mix tells two stories. iPhone
revenue jumped (~+21.7%) on an upgrade cycle, and EPS/margins were flattered by
a one-time tariff-refund benefit (~$0.11 EPS; ~2pts of the 50.1% gross margin),
while **Services — the segment the bull case treats as a durable compounder —
decelerated (~+12.1%) and missed analyst expectations** (~$30.7B vs ~$31.2B).
The valuation debate rests on whether Services keeps compounding; this quarter
the cyclical hardware carried the record and the compounder slowed. Teach the
business through that question. Apple's near-absence from the frontier-AI capex
race is context (the inverse of the hyperscalers), relevant only insofar as it
bears on the services/hardware question — do not turn the piece into an AI take.

## Intended reader
House reader (math/CS, ML-eng, well-read). Assume no prior knowledge of Apple's
financials; teach the segments and the margin mechanics as part of the argument,
placed where they clarify it, not confined to an overview paragraph.

## Contribution (what this piece adds beyond its sources)
Separate the record quarter's *sources* — an iPhone upgrade cycle and a one-time
tariff refund — from the *recurring* engine the valuation depends on, and show
what the Services deceleration and miss mean for the "compounder" thesis. A
reader should finish able to read Apple's segment mix and margin bridge, not
just the headline beat.

## Source obligations & consult
- Template `article`, min_sources 8. Series `consult`: **read the SEC filing
  itself before the coverage of it** (https://www.sec.gov/). Pull Apple's actual
  8-K / press-release financial statements and, if filed, the 10-Q for the
  quarter ended 2026-06-27 (CIK 0000320193) — segment/product revenue, gross
  margin, cash flow, and any disclosure of the tariff-refund impact. Primary =
  Apple's filings and newsroom release; secondary = reporting/analysis.
- Every contested figure needs the primary. Verify the tariff-refund EPS/margin
  impact and the Services miss against Apple's own statements + analyst-estimate
  reporting. Distinguish reported fact, estimate, and synthesis.

## Furniture / charts
Chart-forward desk. Build charts with `nb chart` from verified numbers with
committed Plotly provenance (docs/charts.md) — e.g., revenue mix by segment over
recent quarters, or Services YoY growth decelerating, or the margin bridge for
this quarter. Honest axes, cited data source in caption. A stat strip may carry
the headline numbers. No fabricated data points; transcribe from filings.

## Relevant prior coverage / habits not to inherit
Recent Company Analysis: Boeing (cash from customer deposits, 2026-07-30),
Alphabet (FCF turns negative on AI capex, 2026-07-27), Vertiv, CoreWeave. Do NOT
reuse the "the cash came from X, not Y" headline mold from the Boeing piece, and
do NOT make this another AI-capex story (that was Alphabet). Different company,
different question. Vary opener and section shapes; no colon-subtitle headline.

## Neighboring articles tonight (edition cohesion)
Tonight also runs two technical AI pieces (grokking, speculative decoding), the
two daily briefs, an opinion, and word-of-the-day. This is the markets piece;
keep it in the business lane, no forced ties.

## Output paths
- Article: `.nb-work/company-analysis/apple/library/company-analysis/apple.html`
- Assets/chart provenance under `library/company-analysis/apple/`
- Role artifacts under `agent-artifacts/company-analysis/apple/`

## Harness / model
- harness `claude-code`; writer runtime `claude-sonnet-5` (capable/medium);
  editor opus/high (required).
