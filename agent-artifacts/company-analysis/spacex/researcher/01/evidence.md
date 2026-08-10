# Evidence record: company-analysis/spacex (01)

The primary filings support a detailed picture of SpaceX's first public quarter,
its IPO terms, and its balance sheet, but they do not support the commission's
central structure. SpaceX reports **three** operating segments under ASC 280 —
Space, Connectivity, and AI — not the two the commission assumes (an operating
launch-and-Starlink business versus a Starship-and-Mars program). Starship is
never a reporting unit: it sits inside the Space segment, which is the smallest
of the three by revenue, and no Starship revenue, R&D, or capex line appears
anywhere in the accessible filings. The segment note discloses revenue by
segment but I could not confirm it discloses operating income or loss by
segment, so even a three-way *profit* split may not be cleanly available. The
capital-consuming frontier the filings actually document is the **AI segment**
(Grok, the X platform, orbital-AI and data-center compute), which absorbed
$15.8B of the quarter's $18.4B of capital expenditure, not Starship. The AI
segment was folded in through an all-stock SpaceX–xAI combination that closed in
February 2026, months before the June IPO. So the decomposition the commission
asks for has to be *reconstructed* from partial disclosure, and even then it
cannot isolate Starship; the honest decomposition runs Space / Connectivity / AI
and treats Starship as an unquantified sub-item inside Space.

The record is thin in three places, all flagged below: (1) the IPO prospectus
(Form 424B4) body exceeds the fetch size limit, so lock-up terms, use of
proceeds, and risk-factor language rest on secondary reporting that attributes
itself to that prospectus, not on the primary itself; (2) segment-level
profitability is not confirmed present in the filing; (3) all GAAP line items
below revenue and the segment split were read through the fetch tool's
HTML-to-text conversion of very large filings — revenue and the segment
structure were cross-corroborated across two independent documents, but any
single load-bearing line (net loss, adjusted EBITDA, a specific capex figure)
should be reconfirmed against the filing before it carries a headline.

## Sources

```text
URL:         https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412&type=&dateb=&owner=include&count=100
Kind:        primary (EDGAR filing index for the registrant itself, CIK 0001181412)
Establishes: Space Exploration Technologies Corp is an SEC registrant that filed
             an original S-1 (2026-05-20), amendments, a 424B4 prospectus
             (2026-06-12), 8-A12B listing (2026-06-10), and its first 10-Q
             (2026-08-04, period ended 2026-06-30). Confirms the IPO and first
             public quarter are real filings, not coverage.
Paraphrase:  The registrant's filing history shows the S-1 -> 424B4 -> 8-A12B ->
             10-Q sequence of a completed IPO in June 2026 and a first quarterly
             report in August 2026.
Locators:    Filing list, forms S-1 / 424B4 / 8-A12B / 10-Q / 8-K, May–Aug 2026.
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1181412/000162828026052535/spcx-20260630.htm
Kind:        primary (SpaceX's own 10-Q for the quarter ended June 30, 2026)
Establishes: Three reportable segments; consolidated revenue and its
             disaggregation; GAAP profitability; cash; H1 cash flows; shares
             outstanding.
Paraphrase:  SpaceX reports three ASC 280 segments. Q2 2026 revenue was $7,814M
             (Q2 2025 $4,071M). Cost of revenue $3,495M, gross profit $4,319M,
             operating loss $(143)M, net loss $(541)M. R&D was $3,548M for the
             quarter ($7,062M for the six months). Cash and cash equivalents were
             $93,522M at June 30, 2026; construction-in-progress $12,554M. H1 2026
             operating cash flow was $3,466M and investing cash flow $(34,487)M.
Locators:    Cover page (share counts); statements of operations; balance sheet;
             cash-flow statement; Segment Information note.
Quote:       "operate three segments – (i) the Space segment designs,
             manufactures, and launches reusable rockets ... (ii) the Connectivity
             segment operates a worldwide high-speed, low-latency broadband network
             powered by thousands of Starlink satellites ... and (iii) the AI
             segment operates a vertically integrated AI platform spanning a
             frontier LLM Grok, AI solutions ..., X — a real-time information,
             entertainment, and free speech platform — and AI computational
             infrastructure."
             "As of July 28, 2026, the registrant had 7,696,293,669 shares of
             Class A common stock and 5,485,486,276 shares of Class B common stock
             outstanding."
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm
Kind:        primary (SpaceX's Q2 2026 earnings press release, EX-99.1 to the 8-K)
Establishes: Segment and within-segment revenue detail; operating KPIs; adjusted
             EBITDA; capital expenditure BY SEGMENT; the cash headline.
Paraphrase:  Q2 2026 revenue $7.8B, up 92% from $4.1B. Segment revenue: Space
             $962M (Launch services $648M + Launch & development $314M),
             Connectivity $4,291M (Consumer $2,485M + Enterprise & government
             $1,806M), AI $2,561M (Advertising $367M + AI solutions &
             infrastructure $2,194M). Net loss $541M; operating loss $143M;
             Adjusted EBITDA $3.5B, up 191% from $1.2B. KPIs: 12.0M Starlink
             subscribers at quarter end; 38 total launches in the quarter;
             Starship Flight 12 (first V3 suborbital) in May and Flight 13 in July
             (deployed 20 production V3 satellites). Capex $18,369M for the quarter,
             split Space $1,174M / Connectivity $1,367M / AI $15,828M. Ended the
             quarter with $100B of cash, cash equivalents, and marketable
             securities.
Locators:    Revenue-by-segment table; operating-metrics section; capex table;
             non-GAAP reconciliation (Adjusted EBITDA).
Quote:       "Reached 12.0 million Starlink Subscribers as of the end of Q2 2026";
             "Total launches (#) 38"; "Adjusted EBITDA of $3.5 billion, up 191%
             from $1.2 billion".
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1181412/000162828026042466/spaceexplorationtechnologi.htm
Kind:        primary (IPO pricing term-sheet free writing prospectus, filed 2026-06-11)
Establishes: Final IPO price and offering size; ticker/exchange; underwriters.
Paraphrase:  The IPO priced at $135.00 per share. The company offered 555,555,555
             shares of Class A common stock (all primary) plus a greenshoe of
             83,333,333 shares, raising $74,999,999,925 in the base offering.
             Ticker SPCX on Nasdaq and Nasdaq Texas. Lead book-runners Goldman
             Sachs, Morgan Stanley, BofA Securities, Citigroup, J.P. Morgan,
             Barclays, Deutsche Bank, RBC, UBS, Wells Fargo.
Locators:    Pricing term sheet, offering-size and price fields.
Quote:       "$135.00 per share"; "555,555,555 shares of Class A common stock
             (100% Primary)"; "SPCX (Nasdaq and Nasdaq Texas)".
```

```text
URL:         https://sacra.com/c/spacex/
Kind:        secondary (Sacra, an independent research firm; not the company)
Establishes: Private-market valuation ladder and a segment revenue history for
             years before the filings begin.
Paraphrase:  Sacra records private marks of $350B in Dec 2024 ($185/share, a
             $1.25B secondary), $400B in Jul 2025 ($212/share), and $800B in Dec
             2025 ($421/share, insider sale). It estimates 2025 revenue at $18.7B
             (up 43%), with Starlink $11.4B (61% of revenue, up 48% from $7.7B in
             2024) and Launch Services $4.1B; 2024 revenue $13.1B. Sacra states
             Starlink is the only segment generating operating profit. Sacra
             labels its own figures estimates drawn from the draft prospectus and
             company disclosures, "not official company filings."
Locators:    Valuation-history and revenue sections of the company page.
```

```text
URL:         https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html
Kind:        secondary (CNBC reporting on the first trading day)
Establishes: First-day trading, which the filings do not own.
Paraphrase:  SPCX opened at $150, about 11% above the $135 IPO price, and closed
             its first day at $160.95, a 19% gain.
Locators:    Live-updates close-of-day summary.
```

```text
URL:         https://www.fool.com/investing/2026/08/05/spacexs-lockup-expires-on-aug-6-heres-why-9115-mil/
Kind:        secondary (The Motley Fool; attributes its figures to the prospectus)
Establishes: The lock-up event the commission calls "this week," which I could
             not read in the primary prospectus (see Discarded).
Paraphrase:  The first lock-up tranche expires August 6, 2026, releasing up to
             roughly 911.5 million insider shares — "up to the first 20% of
             eligible shares." The article says the existing public float stands
             below 280.1 million shares, so the unlock is roughly three times the
             float. It attributes to the prospectus a staggered release schedule
             and an early-release condition allowing an additional 10% of shares
             to be sold if the stock traded 30% above the IPO price (i.e., above
             $175.50). It does not itself give a dollar value.
Locators:    Lock-up schedule paragraphs.
```

```text
URL:         https://www.investing.com/news/stock-market-news/spacex-ipo-lockup-expiry-123b-in-shares-set-to-unlock-in-early-august-2026-93CH-4796311
Kind:        secondary (Investing.com)
Establishes: A dollar sizing for the same unlock, and confirms the early-August
             timing from a second outlet.
Paraphrase:  Reports roughly $123B of shares set to unlock in early August 2026.
             The dollar figure is price-dependent and diverges from other outlets'
             (one later quote page implied ~$99B at a lower price), which confirms
             these are secondary estimates around one underlying event.
Locators:    Headline and lede.
```

```text
URL:         https://techjournal.org/spacex-xai-merger
Kind:        secondary (trade coverage of the SpaceX–xAI combination)
Establishes: The provenance of the AI segment — why a segment with no earnings
             record and enormous capex appears in the filings.
Paraphrase:  On February 2, 2026, SpaceX acquired xAI in an all-stock deal that
             valued SpaceX at $1T and xAI at $250B, a combined $1.25T, folding xAI
             in as a wholly owned subsidiary. Grok, the X platform, and early
             orbital-AI research were consolidated into a SpaceX AI unit. Reporting
             describes xAI as burning roughly $1B per month, and names capital and
             compute as the motives for the combination. Corroborated in outline by
             Kalkine and Value Add VC coverage of the same deal (one origin —
             counts as one).
Locators:    Deal-terms and structure sections.
```

```text
URL:         https://www.cnbc.com/2026/07/27/amazon-satellite-internet-network.html
Kind:        secondary (CNBC on Amazon's satellite network)
Establishes: The competitive threat to the Connectivity (Starlink) segment, the
             operating engine the valuation leans on.
Paraphrase:  Amazon's Leo/Kuiper constellation had roughly 329+ production
             satellites across about 12 missions by mid-2026 and had not yet
             launched consumer service (beta waitlist open), against an FCC
             requirement to deploy 1,618 satellites (half the constellation) by
             July 30, 2026. Amazon agreed to acquire Globalstar in April 2026 for
             spectrum and direct-to-device capability. Starlink remains far ahead,
             but a capitalized competitor is scaling and pursuing direct-to-device.
Locators:    Deployment-status and regulatory-deadline paragraphs.
```

```text
URL:         https://www.cnbc.com/quotes/SPCX  (and equivalent quote pages)
Kind:        secondary (market quote; read via search summary, not opened directly)
Establishes: Where the price sits as of the article's date, which the valuation
             question turns on.
Paraphrase:  As of August 9, 2026, SPCX traded around $133.11 with a market
             capitalization near $1.77T and a 52-week range of $104.83 to $225.64;
             the post-IPO low was $104.83. The price is at or slightly below the
             $135 IPO price and well below the first-day $160.95 close. Treat as a
             live quote to reconfirm at draft time.
Locators:    Quote header; 52-week range.
```

## Contradictions

- **Two segments vs three.** The commission's spine is "SpaceX is really two
  businesses" — an operating launch-and-Starlink business and a Starship-and-Mars
  program. The 10-Q's own segment note reports three segments (Space,
  Connectivity, AI) and no Starship unit. This is the deepest conflict with the
  commission and it is load-bearing: the requested operating-vs-Starship split is
  not a reporting reality.
- **Starship is not the cash sink the commission names; AI is.** The commission
  frames Starship-and-Mars as the segment that "consumes cash against revenue
  that does not yet exist." The filings show Q2 capex of $18,369M, of which
  $15,828M (86%) is AI and only $1,174M is the entire Space segment (which
  contains Starship). Independent reporting puts xAI's burn near $1B/month. The
  frontier the price is underwriting is AI infrastructure, with Starship a much
  smaller line inside Space.
- **Starlink is the operating engine, launch is small.** The commission pairs
  "launch-and-Starlink" as the cash business. In the filings, Connectivity
  (Starlink) is $4,291M of revenue while the whole Space segment (launch plus
  Starship) is $962M. Launch is not a co-equal pillar; it is roughly a tenth of
  the quarter's revenue.
- **GAAP loss under a large adjusted number.** Adjusted EBITDA is $3.5B, but the
  company reports an operating loss of $(143)M and a net loss of $(541)M for the
  quarter. Any valuation lean on "cash generation today" must reconcile a
  positive non-GAAP figure with GAAP losses and $18.4B of quarterly capex.
- **Market-cap figure is not single-valued.** Basic shares (13,181,779,945 from
  the 10-Q cover) times the ~$133 price give roughly $1.75T; multiple outlets say
  ~$1.75–1.8T; Sacra states ~$2.3T post-IPO (implying a fully diluted count near
  17B shares). The denominator the whole decomposition divides is itself
  contested — the writer must pick basic vs fully diluted and say which.
- **Valuation step-up is not like-for-like.** The last private mark was $800B
  (Dec 2025) and the IPO valued the company near $1.75T (June 2026), more than
  double in six months. But the IPO entity includes the xAI/X business (marked at
  ~$250B in the Feb 2026 combination) that the $800B mark did not, so the step-up
  is partly a change in what "SpaceX" contains, not pure re-rating.
- **Starlink subscriber figures diverge in secondary sources.** The company's
  12.0M (Q2 2026) is corroborated by Statista and Yahoo, but competitor-comparison
  articles cite 6M or "4+ million" — stale or real-time lags of one underlying
  company disclosure. Two retellings of one origin count as one; the 12.0M origin
  is the company's own release.
- **Segment profitability may not be disclosed.** The segment note discloses
  revenue by segment; I could not confirm it discloses operating income or loss
  per segment. If it does not, the decomposition cannot assign earnings (or
  losses) to Connectivity vs AI vs Space from the filing, only revenue.

## Numbers

```text
Figure: Q2 2026 total revenue $7,814M (release: "$7.8 billion, up 92%")
Owner:  10-Q (statements of operations); Q2 2026 earnings release
Scope:  Three months ended June 30, 2026; prior-year comp $4,071M (Q2 2025)
```

```text
Figure: Segment revenue Q2 2026 — Space $962M; Connectivity $4,291M; AI $2,561M
Owner:  10-Q Segment Information note; earnings release revenue table
Scope:  Three months ended June 30, 2026 (Q2 2025: Space $746M, Connectivity
        $2,588M, AI $737M)
```

```text
Figure: Within-segment — Space: Launch services $648M, Launch & development
        $314M. Connectivity: Consumer $2,485M, Enterprise & government $1,806M.
        AI: Advertising $367M, AI solutions & infrastructure $2,194M.
Owner:  Q2 2026 earnings release
Scope:  Three months ended June 30, 2026
```

```text
Figure: Cost of revenue $3,495M; gross profit $4,319M; operating loss $(143)M;
        net loss $(541)M; R&D $3,548M (Q2) / $7,062M (H1)
Owner:  10-Q statements of operations
Scope:  Three months ended June 30, 2026 (R&D H1 = six months)
```

```text
Figure: Adjusted EBITDA $3.5B (up 191% from $1.2B)
Owner:  Q2 2026 earnings release (non-GAAP)
Scope:  Three months ended June 30, 2026; non-GAAP, reconcile before use
```

```text
Figure: Capex $18,369M total — Space $1,174M; Connectivity $1,367M; AI $15,828M
Owner:  Q2 2026 earnings release
Scope:  Three months ended June 30, 2026
```

```text
Figure: Cash & cash equivalents $93,522M; "~$100B cash, equivalents & marketable
        securities"; construction-in-progress $12,554M
Owner:  10-Q balance sheet; earnings release (the $100B headline)
Scope:  As of June 30, 2026
```

```text
Figure: H1 2026 operating cash flow $3,466M; investing cash flow $(34,487)M
Owner:  10-Q cash-flow statement
Scope:  Six months ended June 30, 2026
```

```text
Figure: Shares outstanding 7,696,293,669 Class A + 5,485,486,276 Class B
        = 13,181,779,945 (basic)
Owner:  10-Q cover page
Scope:  As of July 28, 2026
```

```text
Figure: IPO price $135.00/share; 555,555,555 Class A offered; greenshoe
        83,333,333; base gross proceeds $74,999,999,925
Owner:  IPO pricing term-sheet FWP (2026-06-11)
Scope:  Base offering (pre-greenshoe)
```

```text
Figure: Implied market cap ~$1.75T (basic shares x ~$133) to ~$1.77T (reported);
        Sacra ~$2.3T (implies ~17B fully diluted shares)
Owner:  Computed (price x share count); not owned by any single filing
Scope:  As of ~Aug 9, 2026; denominator choice contested (see Contradictions)
```

```text
Figure: KPIs — 12.0M Starlink subscribers; 38 launches; Starship Flight 12 (May),
        Flight 13 (July, 20 V3 satellites deployed)
Owner:  Q2 2026 earnings release
Scope:  As of / during three months ended June 30, 2026
```

```text
Figure: Private-market marks — Dec 2024 $350B ($185/sh); Jul 2025 $400B
        ($212/sh); Dec 2025 $800B ($421/sh)
Owner:  Sacra (independent estimate), not a filing
Scope:  Secondary/insider transactions; label as estimates
```

```text
Figure: Lock-up first tranche Aug 6, 2026 — up to ~911.5M shares (up to first 20%
        of eligible), ~$123B (price-dependent); public float below ~280.1M;
        early-release if price >30% above $135 IPO (i.e., >$175.50); Musk ~6.4B
        shares locked to June 12, 2027; full 180-day expiry Dec 8, 2026
Owner:  Secondary (Motley Fool, Investing.com), attributed to the prospectus;
        primary prospectus not directly read (see Discarded)
Scope:  Post-IPO lock-up schedule
```

## Source assets

```text
Asset: The revenue-by-segment table (Space / Connectivity / AI, with the
       within-segment lines) in the Q2 2026 earnings release and the 10-Q
       Segment Information note.
Shows: That there are three segments and that Connectivity, not launch, is the
       revenue engine, with launch a small slice of Space. This carries the
       "the company is not two businesses" correction better than prose.
Crop:  Keep both years (Q2 2026 and Q2 2025) so growth is visible; keep the
       within-segment lines. Do not crop away the AI segment — its presence is
       the point.
```

```text
Asset: The capital-expenditure-by-segment table in the Q2 2026 earnings release
       ($1,174M Space / $1,367M Connectivity / $15,828M AI).
Shows: That 86% of quarterly capital spending is AI infrastructure, redirecting
       the "what consumes the cash" question away from Starship.
Crop:  Retain all three segment figures and the total; the contrast is the
       evidence.
```

```text
Asset: The operating-metrics/KPI block (12.0M subscribers, 38 launches, Starship
       flight log) in the earnings release.
Shows: The operating cadence behind the Connectivity and Space segments, for a
       Starlink-trajectory or launch-cadence chart if paired with a verified
       multi-quarter series (the filings here give one quarter; a trajectory
       chart needs additional verified points, which this record does not supply).
Crop:  n/a — tabular KPIs.
```

```text
Asset: The absence of any Starship-specific revenue, R&D, or capex line.
Shows: That a Starship carve-out cannot be drawn from the filing; the "missing
       table" is itself the evidence for the decomposition limitation.
Crop:  n/a.
```

## Discarded

```text
URL: https://www.sec.gov/Archives/edgar/data/1181412/000162828026042639/spaceexplorationtechnologi.htm — the 424B4 prospectus main document (~11.95MB) exceeds the fetch tool's 10MB limit; could not read the primary lock-up, use-of-proceeds, or risk-factor sections. This is the record's main primary-source gap.
URL: https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX_PricingAnnouncement.pdf — company pricing announcement PDF returned undecodable binary via the fetch tool; pricing was instead confirmed from the SEC pricing-term-sheet FWP.
URL: https://efts.sec.gov/LATEST/search-index (EDGAR full-text search endpoint) — returned unrelated/hallucinated hits (other issuers' lock-up exhibits); not used for any claim.
URL: Aggregator "Starlink statistics 2026" pages (axis-intelligence, theglobalstatistics, etc.) — restate the company's subscriber figure without independent measurement; not opened or cited to avoid laundering one origin into apparent corroboration.
URL: S-1 exhibit index (000162828026036936) — no standalone EX-1.1 underwriting agreement or "form of lock-up agreement" exhibit; lock-up language lives in the prospectus body, which is the gap above.
```
