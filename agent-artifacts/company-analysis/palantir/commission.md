# Commission: company-analysis/palantir

## Subject
**Palantir Technologies (PLTR)** and the market question its August 5, 2026
second-quarter report forces: *when a business is genuinely accelerating, what
has to be true for a valuation this large to be right — and what breaks it?*
Palantir reported Q2 2026 revenue up ~93% year over year (~$1.94B), U.S.
commercial revenue up ~149%, and raised full-year guidance to ~$8.15B (~82%
growth), yet trades at extraordinary multiples (reported around ~40x+ forward
sales, a triple-digit P/E). The stock jumped double digits after hours. Use this
record to investigate the general question of how to value hyper-growth software
when growth and price are both at extremes.

## Why this company, why now
The current record makes the question answerable: a fresh quarter with an
unusually clean acceleration (commercial re-acceleration, not just government),
paired with a valuation the market itself debates. It is chosen because the day
makes the question instructive, not because Palantir is due for a profile. It
also lets the piece do something the recent desk has not: prior company-analysis
pieces dissected cash-flow and capex mechanics (Alphabet, CoreWeave, Vertiv,
Boeing); this one is a valuation-vs-growth question, a different market lesson.

## The analysis to build (writer/researcher own the route and shape)
- Teach the business as part of the analysis, not as a boxed overview: what
  Palantir actually sells (Gotham/Foundry and the AIP platform), how its
  government vs. U.S.-commercial segments differ, and why the U.S. commercial
  acceleration is the number the valuation leans on. Place the teaching where it
  clarifies the argument.
- Anchor on the primary financials: the Q2 2026 release and the 10-Q — revenue,
  segment growth (U.S. commercial vs. government vs. international), margins,
  net dollar retention, remaining deal value / RPO, and any customer-count or
  concentration figures. Separate GAAP from adjusted.
- Charts carry the comparison (spec/charts.md; committed Plotly provenance):
  strong candidates are (a) revenue growth by segment over recent quarters
  showing the U.S. commercial inflection, and (b) a valuation-in-context chart
  (EV/forward-sales or P/S vs. a set of high-growth software peers), honestly
  labeled. Build charts only from researcher-verified series.
- The market question answered on the evidence: what set of forward assumptions
  (growth durability, margin path, dilution/stock-comp) the current price
  embeds, and what in the actual record would falsify the bull case. Steelman
  both the "priced for perfection, one stumble away" read and the "durable
  compounder the market keeps underrating" read.

## Boundaries
- `article` template; word band 1500-4000; min_sources 8.
- **Do not issue a buy, sell, or allocation call** (series rule). Analyze the
  valuation question; do not resolve it into advice.
- Read the filing itself before the coverage of it (series `consult`:
  sec.gov). Verify every financial figure against the primary (release / 10-Q).
  Stock-comp and dilution must be handled honestly, not waved past.
- Not a tech-news item and not a product review. The AI-industry news of the day
  belongs to the tech-news desk; this is a market-question analysis.

## Neighbors in this run
Tech-news (2026-08-08) covers the day's AI developments. To avoid duplication,
**tech-news will not feature Palantir's earnings as an item** — this desk owns
the Palantir story today. No other overlap.

## Habits not to inherit (recent company-analysis)
Recent deks used contradiction molds heavily: "X's Y masks a slowing Z,"
"X came from A, not B," "X keeps rising as Y keeps falling." Do not reuse those
exact shapes. The headline should state this piece's specific finding about the
growth-vs-valuation question, not a generic "priced for perfection" cliché. Vary
section-heading shapes from the recent run.

## Production
Harness: claude-code, isolated role subagents. Models by resolved policy —
writing-coach (low), researcher (high), writer (medium) at capable tier; editor
(high) required, inherits. No deviation. Writer sets `nb-meta` harness/model to
match the current published library exactly.
