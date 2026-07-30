# Commission — company-analysis/boeing

## Assignment
Use Boeing (NYSE: BA) as a timely case to answer one market question: **does
Boeing's cash-flow and delivery record show a genuine commercial-aircraft
recovery, or is reported operational progress still outrunning the cash the
business generates?** Choose the exact quarter that makes the question
answerable from the primary filing; if Boeing's most recent 10-Q/8-K makes a
sharper adjacent question answerable (e.g., the gap between accounting profit
and free cash flow, or defense-segment charges dragging the recovery), take it,
but keep the question about cash conversion, not a stock call.

## Angle
Teach the business as part of the analysis, not as a preamble: the three
segments (Boeing Commercial Airplanes, Boeing Defense Space & Security, Boeing
Global Services), how commercial-jet economics work (order book vs. deliveries
vs. cash collected on delivery), and why free cash flow — not net income — is
the number that governs a manufacturer clearing a backlog. Route the article by
the question; place each explanation where it does work.

## Reader & register
House reader (mathematics/CS, ML-engineering career, well-read); assume no prior
knowledge of Boeing specifically. Calm, first-principles register (press voice).
Do not assume the reader follows aerospace.

## Mode / template / geometry
- mode: `open`  · template: `article` · order: null
- words 1500–4000; flex_sections 2–6, each cited; anchors: orientation, sources.
- No buy/sell/allocation call (series rule). Report + earned analysis only.

## Source obligations
- min_sources: 8. Series `consult`: **read the SEC filing itself before any
  coverage of it** (https://www.sec.gov/ — EDGAR: the latest 10-Q and 8-K/press
  release with financial exhibits). The cash-flow statement, the order/delivery
  tables, and management's segment commentary are primary.
- A primary owns the claim (the filing, the delivery data from Boeing/its
  regulators, a party's own statement). Secondary = independent reporting/
  analysis. Contested figures need the primary. Record kind + locator per
  citation; carry into `data-nb-kind`.
- Verify every number against the filing that owns it; do not trust a
  secondary's restatement.

## Starting sources (verify; not a floor)
- SEC EDGAR Boeing filings (10-Q, 8-K earnings exhibits, 10-K for segment/
  program-accounting background).
- Boeing investor-relations quarterly release and order/delivery website.
- Independent coverage for context only (Reuters/Bloomberg/WSJ/FT/Air Current).

## Prevent repetition (recent company-analysis coverage)
Do NOT reprise the AI-capex trio or their shape: alphabet-free-cash-flow
(2026-07-27, capex vs. FCF at a hyperscaler), vertiv (2026-07-25, backlog vs.
guidance), coreweave (2026-07-23, depreciation/interest vs. revenue). Boeing is
a deliberately different lane (aerospace turnaround, cash conversion of a
backlog). Avoid inheriting their openers, their "backlog vs. X" framing as a
template, and any recurring section shape. Retest the headline against
spec/headlines.md (no colon-subtitle, no hedged question).

## Tonight's neighbors (avoid collision)
current-events (US news brief), tech-news (tech brief), paper-of-the-day
(knowledge-distillation), parenting-research (nirsevimab), word-of-the-day
(bowdlerize). Keep Boeing squarely a business/markets analysis.

## Output paths
- Article: `.nb-work/company-analysis/boeing/library/company-analysis/boeing.html`
- Artifacts: `.nb-work/company-analysis/boeing/agent-artifacts/company-analysis/boeing/`

## Runtime for nb-meta
harness: `claude-code` · writer model: `claude-opus-4-8` (tier capable, high
effort) · editor: inherited `claude-opus-4-8`, high effort, required.

## Required contribution (why this is worth publishing)
A reader finishes able to read a manufacturer's cash-flow statement against its
order book and say whether a "recovery" is real cash or accounting. If a chart
earns its place (e.g., FCF vs. net income by quarter, or deliveries vs. cash),
build it with `nb chart` from verified filing numbers with committed provenance.
