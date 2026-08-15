# Commission: company-analysis/super-micro

## The market question

Super Micro Computer (SMCI) reported fiscal Q4 2026 (quarter ended June 30,
2026) on or about August 11-12, 2026. Gross margin jumped to about 17.5% from
roughly 9.9% the prior quarter and about 9.5% a year earlier, after years of the
company earning a thin single-digit margin as the assembler sitting between the
chip vendors and the datacenters. The market question the record now makes
answerable: is that margin step durable, and does the revenue surge turn into
cash, or does an assembler's growth mostly tie up working capital? Answer that.
Do not issue a buy, sell, or allocation call.

## Teach the business as part of the argument

Assume no prior knowledge. Teach what SMCI actually is: a server integrator that
buys GPUs, CPUs, memory, and other parts and assembles configured systems
(increasingly with direct-liquid-cooling for AI racks), so its margin is the
spread it keeps on parts it largely passes through. Place that explanation where
it clarifies the margin and cash questions, not in a fixed overview box. The
accounting history is part of the skeptical frame and must be handled with care:
the 2024 Hindenburg short report, the delayed annual report, the resignation of
its then-auditor, the near-delisting from Nasdaq, and the later refiling. State
only what the record supports, with primary sourcing, and do not imply
wrongdoing the record does not establish.

## What the analysis must resolve

- The margin jump's cause. Read the filing itself, not the coverage of it. Is
  the 17.5% a mix shift toward higher-value liquid-cooled systems, a one-off
  (inventory reserve release, a favorable settlement, a large high-margin deal),
  or a durable step? Weigh the evidence and say what is unknown.
- Cash conversion. Compare revenue and reported profit against operating cash
  flow, and against the working-capital line the business turns on (inventory
  and receivables). Boeing and Alphabet pieces in this series turned on exactly
  this gap between reported profit and cash; make SMCI's own version concrete.
- The guidance. FY2027 guidance in the tens of billions and a record backlog are
  the bull case; treat them as claims to weigh against the cash and margin
  record, not as findings.

## Sources to begin from (researcher confirms and reads the primary)

- SMCI fiscal Q4 2026 results: the SEC Form 8-K and its Exhibit 99.1 on EDGAR
  (CIK 0001375365), and the investor-relations press release. This is the
  primary for revenue, gross margin, net income, EPS, and guidance.
- The most recent SMCI 10-K/10-Q available for the cash-flow statement and the
  inventory and receivables lines, and prior quarters for the margin trend.
- The `consult` source https://www.sec.gov/ : read the filing before any
  coverage of it. Secondary reporting (reputable market press) is context only.

Verify every figure against the filing that owns it. The 17.5% margin and the
guidance figures are contested/market-moving, so they need the primary.

## Furniture opportunities

This is the chart-forward desk. Charts must be committed Plotly provenance
(`nb chart`, spec/charts.md) built only from series the researcher verified:
gross margin by quarter (the story), and revenue by quarter or the guidance
ramp. A `nb-stat-strip` can carry the headline quarter figures. A `nb-table` may
compare reported profit with operating cash flow. Furniture carries evidence.

## Habits to break (from the recent company-analysis record)

The Cerebras piece (2026-08-13) opened on a stat strip, ran several charts, used
a colon "same quarter, two gross margins" heading, and closed on "What would
actually have to change" with an `nb-note-strong` verdict box. Do not copy the
colon "two numbers, same quarter" heading mold, the "what would have to change"
closer, or the closing `nb-note-strong` verdict box, all of which are recurring
across recent pieces. This desk has run several AI-infrastructure names lately
(Cerebras on customer concentration, Alphabet on free cash flow, SpaceX on
valuation); keep this piece distinct by keeping the question distinct: it is
about an assembler's margin durability and cash conversion, not concentration or
capex. Vary how headings are built and end on the conclusion the filing earned.

## Reader, boundaries, record

Reader: the paper's declared audience (mathematics/CS, ML-engineering career,
well-read); teach the business and the accounting without condescending. Word
band 1500-4000, 2 to 6 flex sections, at least 8 sources. No buy/sell/allocation
call. No overlap with the other six articles this edition.

Models and effort actually used (Agent runtime; effort not separately settable,
so intended effort is recorded and model tier plus prompt emphasis carry it):
writing-coach — capable (sonnet), low; researcher — capable (sonnet), high;
writer — capable (sonnet), medium; editor — inherited (opus), high, required.
