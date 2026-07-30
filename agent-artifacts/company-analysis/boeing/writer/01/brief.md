# Writer brief — company-analysis/boeing (invocation 01)

## Role
Draft the article from the evidence and voice guide. Follow `skills/writer/SKILL.md`.
Edit the initialized HTML; do not recreate the skeleton.

## Exact inputs
- This brief.
- `editorial-direction.md` (house floor, headline standard, press voice, template
  identity, series prompt).
- `writing-coach/01/voice-guide.md`.
- `researcher/01/evidence.md` (the complete claim set — do not add claims).
- Initialized article: `.nb-work/company-analysis/boeing/library/company-analysis/boeing.html`.
- Template context under `.nb-context/` (contract: words 1500-4000; flex_sections
  2-6; anchors orientation + sources; cite_rule per-section).
- Furniture catalogs `.nb-context/furniture/{engine,press}.md`.
- Rendered chart already built: `library/company-analysis/boeing/chart-1.png` with
  provenance `chart-1.py`.

## The article
Question: does Boeing's Q2 2026 record show genuine commercial-aircraft cash
conversion, or is reported operational progress outrunning the cash the business
generates? Answer from the primary filings.

Thesis to carry (supported by evidence): the operational recovery is real
(revenue +8%, 171 deliveries, narrowing segment losses, record backlog), but the
reported swing to positive operating cash flow is accounted for by a $4,660M rise
in customer advances (a working-capital inflow), while inventories consumed
$3,859M and free cash flow for the half was still $(823)M. The cash is, for now,
borrowed from future deliveries, not converted from delivered-jet margin.

Teach the business where it does work, not as a preamble: the three segments; how
commercial-jet cash works (deposits and progress billings collected before and
during build, the large balance on delivery; advances as a liability drawn down as
jets deliver); why free cash flow, not net income, governs a manufacturer clearing
a backlog. Steelman the bull case (advances are the normal signature of a growing
order book and a real ramp) before weighing it. Note the seasonality (Q1 2026 FCF
was $(1.5)B) so no single quarter is read as a trend. No buy/sell/allocation call.

## Structure (outline reasoning first; do not inherit a stock outline)
Name flex sections for THIS argument. Suggested spine (2-6 flex allowed):
1. orientation (anchor): the quarter that reads as recovery — with a stat strip.
2. how a jet becomes cash (the mechanics + segments where they do work).
3. where the operating cash came from (the decomposition: table + the waterfall
   chart already rendered as chart-1.png).
4. what the advances are, and are not (steelman + weigh; seasonality; still burning).
5. what would make the cash real (the piece's own conclusion + a Verdict note).
Do not close on a pointer away or a reading list.

## Furniture (plan with prose; each must carry evidence)
- Stat strip in orientation (revenue, deliveries, backlog, Q2 FCF), each cited in
  nearby prose.
- One table comparing H1 2025 vs H1 2026 headline cash figures with the advances
  line (primary).
- The rendered waterfall figure (chart-1.png) in the decomposition section; caption
  states what it shows and carries the citation; useful alt text.
- One `nb-note nb-note-strong` "Verdict" at the end (at most one strong note).
Do not overbuild; the page must read as a continuous article.

## Sourcing rules
- Number sources in first-citation order. Carry `data-nb-kind` from the evidence
  record (S1-S6 primary; S7-S8 secondary). Eight sources are available and each
  owns a claim; do not pad and do not drop below the evidence you actually use.
- Every figure traces to the owning primary in the evidence Numbers section. Do
  not invent locators; add `data-nb-locator`/`data-nb-url`/`data-nb-note` only
  where the evidence supplies detail.
- The FAA 38->42 cap is secondary context (S7); never attach a Boeing financial
  figure to it. The recovery framing is S8 (secondary), stated then tested.

## Headline / dek (retest against spec/headlines.md)
State the finding with actors named; no colon-subtitle; no hedged question; no
semicolon-reversal / comma-triad dek. Lead with the surprise. Working direction:
the cash rebound ran on customer deposits, not delivered jets; dek supplies the
$4.7B advances figure and the still-negative free cash flow.

## nb-meta (actual measured values)
protocol "1.1"; series "company-analysis"; slug "boeing"; template "article";
mode "open"; order null; date "2026-07-30"; tags []; title/dek as written;
sources/words/reading_minutes measured after drafting; harness "claude-code";
model "claude-opus-4-8".

## Original work
Record in `draft-handoff.md` the one visible act of original work: reconciling
Boeing's reported operating-cash-flow swing to the single working-capital line
(customer advances) that produces it, and showing that ex-advances the business
consumed ~$3.5B while free cash flow stayed negative — a reading the filings
report piecemeal but never assemble.

## Prove
Run to BLOCK: 0:
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/company-analysis/boeing/library/company-analysis/boeing.html \
  --series company-analysis --repo . --library ../library
Treat WARN as revision notes; clear what you can. Every URL must resolve.

## Return
`DONE writer <draft-handoff-path>` after BLOCK: 0.
