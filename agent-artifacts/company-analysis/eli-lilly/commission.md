# Commission: company-analysis/eli-lilly

## Authorized work
Scheduled duty for 2026-08-06 returned `company-analysis` as an open section:
choose a topic within the beat, do not repeat a published slug. This run
commissions exactly one company-analysis article: Eli Lilly (NYSE: LLY).

## Subject and market question
Eli Lilly reported Q2 2026 on 2026-08-05: total revenue up ~48% to ~$23.0B,
driven by Mounjaro and Zepbound; the first quarter to include revenue from its
oral GLP-1 pill; US revenue up ~33% to ~$14.4B while ex-US revenue jumped ~80%
to ~$8.6B on ~113% volume growth partly offset by a ~36% drop in realized
prices; full-year guidance raised to $85-87B.

The market question: **as GLP-1 medicines move from premium, cash-pay demand
into reimbursed and mass-market channels, can volume outrun falling realized
price?** The revenue line is growing while price per unit erodes sharply
outside the US (China state reimbursement of Mounjaro is one named driver) and
an oral pill changes the manufacturing and access economics against injectables.
The raised guidance is the crowd's read; the article's job is to decompose it
into volume, price, and mix and judge how durable each leg is. The 100%
branded-drug tariff that took effect this week (covered in current-events
2026-08-04) is a live overhang on the US price leg and belongs in the analysis
where it bears on the question, not as a separate topic.

Teach the business as part of the analysis: what Lilly sells, how tirzepatide
(Mounjaro/Zepbound) and the oral agent differ, and why price realization and
volume can move in opposite directions. Assume no prior knowledge of the
company. Do not issue a buy, sell, or allocation call (series rule).

## Template and geometry
Template `article` (longread). Series word band 1500-4000. Flex sections 2-6.
Cite rule per-section. This is the chart-forward market-and-business desk:
a chart or table is expected where a trend or decomposition is the point
(price vs volume, revenue mix, guidance walk). Charts are committed Plotly
provenance scripts rendered with `nb chart` (spec/charts.md); tables are
furniture. Furniture carries evidence, never decoration.

## Sources
Source floor: min 8 (template article default; see `nb source-policy`).
Series `consult`: https://www.sec.gov/ — read the filing itself (the Q2 2026
10-Q and the earnings release/8-K exhibit) before the coverage of it. Contested
figures need the primary. The price/volume decomposition and any per-product
revenue must be verified against Lilly's own 10-Q / press release, not headlines.

## Production policy (resolved via `nb production-policy`)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model inherit, effort high, REQUIRED

Actual harness: roles run as isolated Claude subagents on model
`claude-opus-4-8` (capable tier; the required editor model "inherit" resolves to
this correspondent model). Deviation recorded: this runtime's subagent
launcher does not expose a per-invocation reasoning-effort control, so the
required editor "high effort" is approximated by the most capable available
model at the harness default effort. No model was traded down.

## Neighboring articles this run (keep the edition coherent, non-redundant)
paper-of-the-day/instructgpt, parenting-research/teething,
word-of-the-day/luddite, current-events/2026-08-06, tech-news/2026-08-06.
Eli Lilly is the edition's only markets/business longread and its only
non-AI, non-tech company piece; lean into that distinctness.

## Recent company-analysis coverage and habits not to inherit
Recent slugs: reddit, apple, boeing, alphabet-free-cash-flow, vertiv,
coreweave (heavily AI-infrastructure and big-tech). This piece is pharma and
should not read like the AI-capex pieces. Habits to break, not to copy:
- Recent openers lead with a single quarter's beat/miss headline number
  (Reddit "raised guidance and lost a fifth"; Apple "iPhone cycle masks a
  slowing services engine"). Find this piece's own entry into the price/volume
  question rather than reusing the beat-versus-bar opener.
- Recent outlines march quarter-metric by quarter-metric ("What the record
  quarter actually contained" → segment → segment → "next quarter" →
  thesis-check). Let the volume-vs-price question drive the route instead.
- Recent closers pose "two ways to read" the quarter or run a compounder
  thesis-check. Do not reuse either closing shape.
These are content/structure habits only; required furniture and the Sources
section are not habits to avoid.

## Original contribution expected
A decomposition the headlines do not give the reader: separate the raised
guidance into volume, price, and mix, name where realized price is falling and
why, and judge whether the growth is a durable volume ramp or a pull-forward
against eroding price. The analysis, not the beat, is the article.
