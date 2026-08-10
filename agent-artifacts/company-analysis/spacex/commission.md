# Commission: company-analysis/spacex (2026-08-10)

## The question

SpaceX has reported its first quarterly results as a public company and its
post-IPO lockup is expiring this week. The company is really two businesses
under one ticker: an operating launch-and-Starlink business that generates cash
today, and a Starship-and-Mars program that consumes it against revenue that
does not yet exist. The analytical question is what the market price is actually
paying for. Separate the value that rests on the operating business the filings
document from the value that rests on Starship optionality, and show what has to
be true for today's price to be defensible on each. This is a market question
about valuing a company whose worth is dominated by a segment with no earnings
record, using a company whose current record finally makes that question
answerable.

Do not issue a buy, sell, or allocation call. The verdict the piece may reach is
what the price assumes, not what a reader should do.

## Boundaries

- Assume no prior knowledge of SpaceX. Teach the business as part of the
  argument, placed where it clarifies the reasoning, not in a fixed overview.
- The declared reader has a quantitative background but no assumed finance
  vocabulary beyond what the article builds. Define valuation terms in the
  sentence they first appear.
- Anchor every figure to the primary filing that owns it. Independent estimates
  (subscriber counts, launch cadence, private-market marks) are context and must
  be labeled as estimates, never as the filing's numbers.
- Segment economics are the spine: the piece fails if it treats SpaceX as one
  undifferentiated growth story.

## Required contribution

The article does something the filings and the coverage do not: it decomposes
the market capitalization into the part the operating business supports and the
part left over for Starship, and states what growth, margin, or cadence each
part demands. Reporting the quarter is not the contribution; the decomposition
and the stated conditions are.

## Template and furniture

Template: `article`. Outline the reasoning before naming sections; name flex
sections for this argument. A revenue-by-segment or Starlink-trajectory chart is
likely the right furniture if the evidence record supplies a verified series
(`nb chart`, committed provenance). A table comparing the two segments' unit
economics may carry more than prose. Furniture carries evidence, never
decoration.

## Recent company-analysis habits not to inherit

The last three pieces (palantir, reddit, vertiv) all opened on an `nb-stat` /
`nb-stat-strip` block and leaned on a valuation-vs-price frame with headings of
the form "What the price has already paid for" / "The quarter the price has to
justify" / "What 45 times sales requires". Two of them closed on a "two ways to
read it" section ("Two ways to read a one-fifth day", "Where the two reads
part"). The valuation lens is right for this beat, but do not reuse that opener
furniture reflexively, that heading mold, or the "two reads" closer. The
segment-decomposition angle should produce its own structure.

## Sources

Source policy: minimum 8 sources; `consult` obligation is `https://www.sec.gov/`
— read SpaceX's own registration statement (S-1) and its most recent periodic
filing (10-Q or 8-K with results) on EDGAR before any coverage of them.
Contested figures (segment revenue, Starlink subscribers, launch cadence,
lockup share counts, IPO price) need the primary that owns them.

## Recast from research (supersedes "The question" above)

The evidence record contradicts this commission's two-business spine, and the
article follows the record. The 10-Q's ASC 280 segment note reports three
segments, not two: Space (launch, and Starship inside it, $962M of $7,814M Q2
revenue), Connectivity (Starlink, $4,291M), and AI (Grok/X and orbital compute,
the balance), the AI unit arriving from an all-stock SpaceX–xAI combination that
closed February 2026. Starship is not a reporting unit and cannot be isolated.
The cash-consuming frontier the filings actually document is AI, not Starship: of
$18,369M Q2 capex, $15,828M (86%) is AI versus $1,174M for all of Space. The
company is GAAP-unprofitable (operating loss $143M, net loss $541M) under a
$3.5B adjusted-EBITDA headline, and the market-cap denominator is contested
(about $1.75–1.8T on basic shares versus roughly $2.3T fully diluted).

The recast question: SpaceX's first public quarter shows a connectivity business
that carries the revenue and an AI business that carries the spending, fused with
a launch business, under one contested market cap. Decompose the capitalization
across what the reported segments support and state what each part must assume —
above all, how much of the price rests on the profitable-at-EBITDA Connectivity
operation versus the AI unit that consumed 86% of last quarter's capital with no
profit record. Treat Starship as an unquantified sub-item of Space, named where it
matters but not given a number the filing does not supply. Still no buy, sell, or
allocation call.

Caveats the writer must honor: the IPO prospectus body (424B4) could not be
opened, so lock-up terms rest on secondary reporting attributing to it; segment
operating profit may not be disclosed, so a three-way profit split may be
unavailable; any single load-bearing GAAP line was read through a fetch
conversion of a very large filing and should be reconfirmed before it headlines;
the market-cap denominator is a range, not a point; and the launch-cadence
contradiction is lightly sourced. State the contested market cap as a range and
attribute the lock-up figures as reported, not as read from the prospectus.

## Runtime

Harness `claude-code-routine`; model Opus 4.8 for every role. Production policy
asks researcher/high, writer/medium, writing-coach/low, editor/high (required).
Per-invocation reasoning effort is not separately settable through this
runtime's child launches, so each role runs at the session's effort; the editor
gate (fresh-eyes review plus deterministic proof) is preserved in full. Writer
records `harness: claude-code-routine` and `model: Opus 4.8` in nb-meta.
