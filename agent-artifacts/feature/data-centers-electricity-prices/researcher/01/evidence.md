# Evidence record: feature/data-centers-electricity-prices (researcher 01)

Checked 6 November 2026. Sections: Sources, Contradictions, Numbers, Limits, Source assets, Discarded.

The evidence supports most of the commissioned angle and breaks one part of it. Estimates do measure different prices (wholesale energy, PJM capacity, average retail rate), different customer classes, different exposure units, and different periods and geographies, and the documents let those be laid out side by side. The part that breaks: two papers measure the same price (average residential retail rate, annual, state or utility level, data centers up to 2024) with instrumental variables on cumulative data-center capacity and still get opposite signs (Watten et al. negative, Meeks et al. positive), so "different things measured" does not explain every disagreement. Identification choices, sample and the utilities that drive each result do. One paper (Elhai and Zhou, Harvard, 4 Nov 2026 version) tests two reduced-form retail designs on its own data and calls both not credible. The news peg is thin: the Harvard/Penn study (Rana, Kaps, Netessine) was read only as an abstract, and its full text could not be opened. Its residential figure is a share of an observed price increase, not a percent price effect, which does not line up with the other studies without conversion. The record is strongest on the mechanism (Dallas Fed, Watten et al., Meeks et al., Elhai and Zhou, IMM), on PJM capacity (IMM primary), and on the study-by-study table. It is thinnest on the peg, the CEPR/VoxEU paper (abstract only), and the USC study (secondary summary only).

## Sources

### The news peg

```text
URL:         https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580459
Kind:        primary (abstract only). The authors own the claim. The SSRN page returned 403 to a plain fetch. The abstract text was read from the Crossref record of DOI 10.2139/ssrn.7580459. Full text NOT opened.
Establishes: "The Cost of Intelligence: Impacts of AI Data Centers on US Electricity Prices", Vishrut Rana, Christian Kaps, Serguei Netessine. Working paper on SSRN, 2026 (Crossref gives only the year; search summaries say September 2026, unverified).
Paraphrase:  Links quarterly data-center capacity additions to local electricity price and utility sales data and uses a single-anchor synthetic-control design with cumulative, repeated treatment. Data centers built in the US between 2020 and 2025 raised their region's industrial price by an average of 5.4 $/MWh, "explaining 15% of the total observed increase in prices". Residential spillovers are "significant but small", an average of 1.7 $/MWh, "4% of the observed increase since 2020". Additions by Big Tech firms show no discernible price increase. Co-location data centers do. Utilities with higher prior infrastructure utilization and a history of serving large industrial customers have lower residential spillovers. The authors conclude the public discourse is overstated and the average residential effect is small and concentrated among co-location developers and specific utilities.
Locators:    Abstract only (Crossref record). Design details, sample size, region definition, exposure unit, standard errors, and tables not seen.
```

```text
URL:         https://vishrutrana.com/
Kind:        primary (author's own page), for the paper's status and the authors' affiliations only.
Establishes: Rana is a fifth-year PhD candidate in Operations Management at the Wharton School, University of Pennsylvania, working with Netessine and Kaps. The paper is listed as his "Job Market Paper", "Available at SSRN", with INFORMS Annual Meeting talks on 1 and 3 November 2026.
Locators:    Home page, Research Working Papers and Upcoming Talks.
```

```text
URL:         https://christiankaps.com/
Kind:        primary (author's own page), for affiliation only.
Establishes: Kaps is an Assistant Professor in the Technology and Operations Management unit at Harvard Business School. He lists the paper with Rana and Netessine and links the same SSRN abstract.
Locators:    Home page, Research.
```

```text
URL:         https://www.washingtonpost.com/climate-environment/2026/11/06/data-centers-may-not-be-raising-americans-electricity-bills-that-much/
Kind:        secondary. Reports on the Rana et al. study from outside the authoring party.
Establishes: Only that the Post ran the story on 6 Nov 2026. The Post page was not opened (403 and connection errors to a plain fetch). Content below was read through a syndicated copy at https://www.yahoo.com/news/us/articles/americans-hate-data-centers-might-100000713.html via WebFetch, which summarizes through a small model, so wording is paraphrase from that summary and was not checked against the Post's text.
Paraphrase:  By the summary: byline Shannon Osaka; cites a study by researchers at Harvard and Penn linked to the same SSRN abstract id; names Netessine as a Wharton professor; says data centers account for 4 percent of utility rate increases over five years and 15 percent of the industrial price increase from 2020 to 2025; says data centers are "probably" having a small residential effect; says PJM territory differs, with some costs pushed onto residential customers; says residential prices could be affected more if demand keeps growing. The article does not say which authors are at Harvard.
Locators:    Whole article, via summary. Do not quote.
```

```text
URL:         https://magazine.wharton.upenn.edu/issues/spring-summer-2026/wharton-studies-the-impact-of-data-centers/
Kind:        secondary, background only.
Establishes: Spring/Summer 2026 note that Rana had "recently began" studying how data-center entry affects regional consumer rates. No results.
```

### Retail-rate causal designs

```text
URL:         https://arxiv.org/abs/2606.19777  (PDF: https://arxiv.org/pdf/2606.19777v1)
Kind:        primary. Authors own the estimate. Preprint, v1 18 Jun 2026, not peer reviewed. Affiliations as printed: Asa Watten (EPRI), John Bistline (Watershed), Geoffrey Blanford (EPRI). The paper does not state a funder. EPRI is the Electric Power Research Institute.
Establishes: Title "Have Data Centers Raised Your Electric Bill? Causal Evidence from the United States". Average retail rates fell modestly with data-center growth, 2015 to 2024.
Paraphrase:  State-year panel (480 observations, 2014-2024 sales, EIA-861 bundled service, S&P Global data-center capacity added 2015-2024, 21.3 GW in total, crypto excluded). Outcome is log residential revenue holding log residential sales fixed, so the coefficient reads as a change in average residential price at fixed demand. Exposure is the inverse hyperbolic sine of cumulative data-center capacity. Instrument is the length of the 1947 Interstate Highway Plan in the state, conditional on GDP and population, with region fixed effects (state fixed effects are collinear with a time-invariant instrument). Preferred IV coefficient is -0.035 (Anderson-Rubin 95% CI -0.121 to -0.014, first-stage F 7.869, below the usual 10). The 2019-24 subsample gives -0.017 (CI -0.034 to -0.006, F 21.6). The first-difference estimate is "precisely zero". OLS coefficients are -0.001 to -0.010. The text reads the preferred estimate as "a doubling of data center capacity causes residential retail prices to fall by 3.5% for a fixed level of residential demand", and says the average residential customer lived in a state where capacity grew 160% (a mean difference of 1.6 in the transformed variable), which "caused their rates to fall by 6%". Commercial and industrial effects are "substantially smaller" (Supplemental Appendix). Mechanism offered: fixed network costs spread over more kWh, economies of scale in T&D and generation (Section II, Figure 1, Tables 1 and C1). Caveats stated: supply constraints, durability of demand, fuel costs; a possible reversal if load forecasts overshoot (Section IV).
Locators:    Abstract; Introduction p.3 (headline and F); Table 2 p.20; text on the doubling reading p.21; Figure 2 p.18 (state scatter); Figure 3 p.19 (highway plan vs data-center map); Discussion pp.22-24; Supplemental Appendix Figure C2 p.42 (industrial). Arithmetic flag: see Contradictions and Limits on the "doubling" reading.
```

```text
URL:         https://ceepr.mit.edu/workingpaper/who-pays-for-growth-evidence-from-datacenters-and-the-grid/  (PDF: https://ceepr.mit.edu/wp-content/uploads/2026/06/MIT-CEEPR-WP-2026-13r.pdf)
Kind:        primary. Working paper, MIT CEEPR WP 2026-13, June 2026, revised 23 Oct 2026; CEEPR posts working papers without peer review. Authors: Robyn Meeks (Sanford School of Public Policy, Duke), Jacquelyn Pless (Rotman School of Management, University of Toronto), Zhiyuan Qi and Zhenxuan Wang (NC State). Data-purchase funding from the Institute for Humane Studies is acknowledged.
Establishes: Data-center entry raises average retail rates, with the largest effects at investor-owned utilities.
Paraphrase:  Utility-state-year panel (973 utilities, 14,733 observations), EIA-861 average retail price (revenue divided by sales), data-center entry 2010-2024 from Aterio records, a county-year counted only above 5 MW newly activated. Treatment is first activation in the utility's service area. Estimator is Callaway and Sant'Anna difference-in-differences with never-treated utilities as controls, plus a matched design and a capacity IV (log cumulative capacity instrumented with pre-period local data-processing employment or establishments interacted with capital spending by Google, Amazon, Meta and Microsoft). Average treatment effect on average retail price: +2.7% (all), +2.1% (residential), +2.8% (commercial), +4.2% (industrial). Investor-owned utilities +5.6% (residential +5.2%, commercial +4.6%, industrial +8%). "Much smaller among public utilities and absent among cooperatives." Restructured states +3.8% average, smaller and not significant in non-restructured states. Bill translation: residential +2.1% is 0.32 cents/kWh, about $3.21 a month on a pre-treatment bill of about $153 a month; investor-owned residential +5.2% is about 0.88 cents/kWh, $7.34 a month. IV coefficient on log cumulative capacity: 0.073 and 0.078 for average retail price. The effect "reflects all data center growth following an initial entry rather than a single facility alone". Commercial and industrial effects mix pass-through to incumbents with the prices data centers themselves pay, because some data centers are classed as commercial or industrial. Mechanisms: authorized rate bases, construction and generation investment rise; price effects are lower where load factors improve (non-restructured states); larger where reserve margins are low.
Locators:    Abstract; Introduction pp.2-4; Table 2 p.50; Table 3 p.51 (ownership); Section 6.3 "Magnitude of Effects" p.28; IV paragraph p.30 and Appendix Table A9; Section 7 Mechanisms (7.1 to 7.5); Figure 2 p.44 (event study).
```

```text
URL:         https://cepr.org/publications/dp21854  (author listing: https://cameron-scalera.com/)
Kind:        primary (abstract only). CEPR Discussion Paper 21854, "Large-Load Electricity Customers and Spillovers on Household Prices: Evidence from U.S. Data Centers", Cameron Scalera, Valentina Bosetti, Filippo Pecci. The CEPR page returned a Cloudflare block. The abstract was read on Scalera's own page. A search summary dates the paper 19 Aug 2026, unverified. The paper PDF was NOT opened.
Establishes: The paper behind the CEPR/VoxEU column https://cepr.org/voxeu/columns/how-data-centres-affect-electricity-prices-and-whom (column also blocked, not opened; the search summary names its authors as Pecci and Bosetti, unverified).
Paraphrase:  Maps the data-center build-out after 2021 to utility territories and uses a shift-share design based on pre-AI fiber infrastructure. "A standard deviation of ten data centers raises household electricity prices by 13%, and a single hyperscaler facility increases prices by 4%." Demand-driven channels seem dominant, households bear a disproportionate burden, and nonprofit utilities, energy surplus and retail competition may mitigate. Per-facility cents per kWh and distribution-spending figures that appeared in a search summary were not seen in any opened document.
Locators:    Abstract only.
```

```text
URL:         https://energyanalytics.org/research/dont-blame-the-data-centers
Kind:        secondary for the USC estimate. The issue brief is by Shon R. Hiatt (a USC Marshall researcher and an author of the underlying study) and Mark P. Mills of the National Center for Energy Analytics (NCEA), an energy-policy think tank, dated 4 Aug 2026. It summarizes "Data Center Entry and U.S. Electricity Prices: From the Wholesale Market to the Power Bill", Angela Ryu and Shon R. Hiatt, USC Zage Business of Energy Initiative, 2026. The underlying USC paper was not found (it is not on https://beprojects.usc.edu/home/data-centers/) and not opened.
Establishes: What the brief says the USC study found. The brief's title and framing ("Don't Blame the Data Centers") carry its own stance.
Paraphrase:  Wholesale data 2020-25, retail data 2015-25. Difference-in-differences at three scales. CAISO nodes: data-center entry raises the congestion component of locational marginal price by $2.30/MWh in the first year after first entry and $1.45/MWh across all entries. Non-CAISO zones (55 zones, four grid operators, about 30 states): +$3.44/MWh total locational marginal price in the year after entry, with the energy component +$5.43/MWh, congestion and losses not significant. Retail: "doubling a utility's operating data-center capacity is associated with a 0.62% increase in residential electricity prices, or $1.00-$1.06 per MWh", "less than $1 per month" for a typical household, seen mainly at cooperatives and municipal utilities, with no statistically significant effect at investor-owned utilities (68% of customers). The brief's own limitations: retail estimates are conditional associations, not causal; entries are first-within-panel and many markets already hosted data centers; reserve margins were adequate in the sample. A RealClearEnergy op-ed by Hiatt reportedly gives 0.65%; not opened.
Locators:    "Retail Price Findings" and "Limitations" sections; Figures 1 and 2 captions (adapted from the USC paper, pp.8-9 of it).
```

### Wholesale, capacity and mechanism

```text
URL:         https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2606r1.pdf
Kind:        primary. Federal Reserve Bank of Dallas Working Paper 2606, March 2026, revised 9 Oct 2026. Owen Kay (Williams College), Robert Reaser (UC Davis), Reid Taylor (Federal Reserve Bank of Dallas). The Dallas Fed disclaimer says views are the authors' and the paper is a preliminary draft.
Establishes: Wholesale price effects from a dispatch model, and a framework for when load growth can lower retail rates.
Paraphrase:  Hourly, unit-level least-cost dispatch model, 23 regional markets trading over capacity-constrained interfaces, with and without data-center load, 2021-2025 and scenarios to 2028. Preferred scenario: data centers raised the load-weighted national wholesale price 6.9 percent by 2025 and 12.3 percent by 2028. Northern Virginia +$5.22/MWh (15.0%), Pacific Northwest +$5.68/MWh (15.4%), Florida and parts of the interior South as low as $0.42/MWh (1.0%) in 2025. About half of the roughly $186.7 billion increase in generator payments over 2021-2028 is a transfer to inframarginal generators. Retail section: with Assumption 1 (all fixed system costs stay fixed), the offset ratio is OR = ((1 - s) / s) x ((1 + d) / eta), with s the share of the retail rate that recovers fixed costs, d the percent increase in demand from data centers and eta the supply price elasticity. Load growth can lower retail rates only if s exceeds s* = (1 + d) / (1 + d + eta). The authors say Assumption 1 is "unlikely to hold in reality" and that the section likely understates retail effects. Accounting for spillovers through trade makes the outlook for retail rates "less promising". The March 2026 version reported 2 to 6 percent national wholesale effects. Cite the revision.
Locators:    Abstract p.1 (of paper); Introduction pp.2-3; Section 7 "Retail Price Effects", Equations 14 and 15, PDF pp.54-55; Figures 15 and 16 PDF pp.55-56.
```

```text
URL:         https://celhai.github.io/pdfs/Elhai_Zhou_data_centers.pdf
Kind:        primary. Coly Elhai and Yixin Zhou, Harvard University, "Data Centers: Location Choice and Grid Externalities", version dated 4 Nov 2026 (the file's creation date matches). Working paper. Acknowledges NSF Graduate Research Fellowship support.
Establishes: A wholesale and emissions dispatch model, plus an explicit rejection of reduced-form retail designs on this data.
Paraphrase:  Dispatch model of regional supply curves. In 2025 cumulative data centers raised wholesale prices about $1.63/MWh (range across placements $1.44 to $3.13), $2.3 billion a year for residential customers at full pass-through, an average of $0.33 to $0.41/MWh per GW of nameplate capacity. A 1 GW data center raises costs by over $3/MWh in New England and about $0.30/MWh in the upper Midwest. Data centers have located in regions with flatter supply curves, which attenuated price effects so far. Price effects scale more than linearly with load because supply curves are convex, so backward-looking reduced-form estimates "will tend to underpredict" later effects. Section 3.1 names the channels: wholesale energy, capacity markets (PJM named, with the effect called a result of PJM's mechanism design and interconnection backlogs, not inevitable), and infrastructure cost, which can fall before new build and rise after. Appendix A tests two retail designs. Event-stacked local-projections DiD (43 events): residential-price estimates "almost entirely insignificant", intervals "$30 or more" against prices of $100 to $200/MWh, leave-one-event-out estimates range from -10.0 to +2.6 and flip sign. Firm Bartik IV, per +1 GW added 2019-2024, 2018-2024 change: residential price -2.81 $/MWh (Anderson-Rubin set -15.01 to 0.31), non-residential -2.40 (set -9.35 to 0.64), OLS +1.48 and -3.14; first-stage F 7.7. Dominion Virginia is "responsible for 80% of the instrument's first stage covariance". Conclusion, A.3: "Both the Bartik and LP-DiD approaches suggest negative retail price impacts ... However, neither design is credible." The $2.59 and $3.49 per MWh per GW figures from the orchestrator's leads are NOT in this version (see Contradictions).
Locators:    Abstract and Introduction pp.1-4; Section 3.1 pp.8-12; Section 4.4 and Figure 6 pp.22-25; Appendix A pp.44-54 (Figure A.3 p.50, Table A.1 p.51, Table A.2 p.52, Takeaways p.54); Figure 1 p.11.
```

```text
URL:         https://www.monitoringanalytics.com/reports/Reports/2026/IMM_Analysis_of_the_20272028_RPM_Base_Residual_Auction_Part_A_20260105.pdf
Kind:        primary. Monitoring Analytics, LLC, PJM's Independent Market Monitor, "Analysis of the 2027/2028 RPM Base Residual Auction - Part A", 5 Jan 2026. The monitor is an independent market-surveillance contractor with a role under the PJM tariff and takes a stated position on market design.
Establishes: The increase in PJM capacity-market revenues attributable to data-center load, under the monitor's scenarios.
Paraphrase:  Capacity-market revenue increase from including data-center load in the peak load forecast, by delivery year, all data-center load: 2025/2026 $9,332,103,858; 2026/2027 $7,271,197,971; 2027/2028 $6,497,653,512 (65.5 percent of actual 2027/2028 auction revenues of $16,411,578,225); total $23,100,955,341. Above-embedded load only: $7,742,960,157, $7,271,197,971, $6,244,523,827; total $21,258,681,955. The 2027/2028 auction included 17,071 MW of existing and forecast data-center load, 13,018 MW of it new or forecast growth. The 2026/2027 and 2027/2028 auctions cleared short of the reliability requirement (208.7 and 6,516.6 MW UCAP). The price cap and floor from the Shapiro-PJM agreement ($333.44 and $179.55 per MW-day UCAP in the 2027/2028 auction) cut combined 2026/2027 and 2027/2028 revenues by $13,083,187,831 (28.7 percent) versus an unrestricted curve. The monitor's own caution: "The MMU presents the results of these sensitivities ... not forecasts". These are revenue increases to capacity sellers paid by load-serving entities. They are not retail bill increases.
Quote:       "data center load growth is the primary reason for recent and expected capacity market conditions" (Conclusions, p.5). The wording matters because E3, below, splits the cause differently.
Locators:    Table 1 p.4; Table 2 p.5; Conclusions p.5; revenue percentages p.6; restricted VRR curve p.15.
```

```text
URL:         https://www.ethree.com/wp-content/uploads/2026/05/Understanding-the-Drivers-of-Rising-Electricity-Rates-and-the-Role-of-Data-Centers_E3-2026.pdf
Kind:        secondary for the data-center price question (a literature review of 11 studies plus four expert interviews, with one original PJM decomposition), and sponsor-funded. "This report was funded by the Data Center Coalition, who reviewed the whitepaper prior to publication", with E3 stating its conclusions are its own. E3 is an economic consultancy. Authors listed: Beer, Chan, Patel, Picciano, Ramirez, Riu, Shah.
Establishes: A sponsor-side reading of the evidence, and one original calculation: E3's decomposition of PJM's capacity price rise between the 2024/2025 and 2025/2026 auctions.
Paraphrase:  Does not estimate a retail effect of its own. Reports "no evidence" that other customers subsidize data centers, "no clear relationship" between load growth and rate increases at state level (citing Bates White), PJM as an exception where load growth is "one of several factors". E3 computes that about 50% of the PJM 2025/2026 capacity price increase ($29 to $270 per MW-day nominal) is attributable to load growth, mostly data centers, and the other 50% to programme design, supply and the cost of new entry, by a Shapley-style attribution. The report's own words are "no evidence that data centers have historically been subsidized", which is narrower than "no evidence of increases". Primer pp.6-10 sets out how a utility builds a revenue requirement by function (generation, transmission, distribution, customer), classifies and allocates it to classes, and why average rates fall when sales grow faster than costs and rise when costs grow faster.
Locators:    Acknowledgments PDF p.2; Executive Summary p.3; PJM section and Figure 6 PDF p.25 (the footnote on page 25 describes the method); Figure 2 PDF p.10 (illustrative, adapted from LBNL).
```

```text
URL:         https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
Kind:        primary. U.S. Energy Information Administration owns the price series.
Establishes: 2025 U.S. average retail prices by class and the reason industrial prices sit near wholesale.
Paraphrase:  2025 annual average retail price 13.63 cents/kWh; residential 17.30, commercial 13.41, industrial 8.62, transportation 13.83. Retail prices are highest for residential and commercial because it costs more to distribute to them. The industrial retail price "is generally close to the wholesale price". Prices range from 35.72 cents/kWh in Hawaii to 8.20 in North Dakota. Cites Electric Power Monthly Tables 5.3 and 5.6.B, Feb 2026 preliminary data.
Locators:    "Electricity prices vary by type of customer" and "by locality".
```

### Abstract-only primaries, not used for figures

```text
URL:         https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6930258  (Calvin Zhang, "AI Data Centers and Electricity Prices: Much ado About Something?")
Kind:        primary, abstract only (Crossref record).
Paraphrase:  Staggered difference-in-differences on wholesale prices, 2019-2026, PJM and WEIM: a county's first AI data center raises local wholesale prices by $5.3/MWh against a sample mean of $47/MWh. The author says this is higher than retail effects in the literature and modest against some press claims.
```

```text
URL:         https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7028658  (Hosein Hamisheh Bahar and Lilian Ng, "Powering AI at Local Costs")
Kind:        primary, abstract only (Crossref record).
Paraphrase:  Compares nearby counties across balancing-authority borders. After data-center operations begin, prices rise in nearby counties served by the same balancing authority, for residential and for industrial and commercial customers. No magnitudes in the abstract.
```

## Contradictions

1. Sign on average residential retail price, same price type, same kind of design. Watten et al. (arXiv 2606.19777): IV on cumulative capacity, 2015-2024, 48 states, coefficient -0.035 (Table 2, column 4), instrument F 7.9. Meeks et al. (CEEPR WP 2026-13r): +2.1% residential after first entry (Table 2) and IV on log cumulative capacity +0.073 to +0.078 for the average retail price (p.30). Both use instruments for cumulative capacity and both condition on a form of fixed effects. They differ in unit (state versus utility-state), sample (2015-24 versus 2010-24), instrument (highway plan versus pre-period data-processing employment times cloud capital spending), control for demand (Watten holds residential sales fixed, Meeks does not), and customer base (Watten uses bundled service providers, 93% of residential sales; Meeks uses 973 utilities). The documents do not say which difference produces the sign flip. This is evidence against the commissioned angle in its strong form.

2. Which customer class bears more. Rana et al.: industrial effect (5.4 $/MWh, 15% of the increase) larger than residential (1.7 $/MWh, 4%). Meeks et al.: industrial +4.2%, commercial +2.8%, residential +2.1%, with the caveat that data centers sit in those classes. Watten et al.: effects for commercial and industrial "substantially smaller" than residential. Scalera et al.: households "bear a disproportionate burden". Elhai and Zhou Bartik IV: non-residential -2.40 and residential -2.81, both with intervals that include zero.

3. Which utilities. Meeks et al.: effects concentrated at investor-owned utilities (+5.6%), "absent among cooperatives". USC via NCEA: residential effect "mainly" at cooperatives and municipal utilities, no significant effect at investor-owned utilities. Opposite ownership pattern, different designs and price definitions. Rana et al. report instead that co-location data centers raise prices and Big Tech additions do not, and that utilities with higher prior utilization and a history of serving large industrial customers have smaller residential spillovers, which resembles Meeks's utilization result.

4. Which wholesale component moves. USC via NCEA: energy component +$5.43/MWh in non-CAISO zones, congestion and losses insignificant. Meeks et al., Section 7.4: entry raises the congestion and loss components of wholesale prices rather than the energy component. Different grids, different data, different years. Neither is a retail measure.

5. Is the negative retail result credible. Watten et al. read their IV as causal. Elhai and Zhou test two reduced-form retail designs on their own data and conclude "neither design is credible", on three grounds: few treated units (1,149 of 1,360 utility-states host no data center capacity; about 20 events survive in the long-horizon design), results that flip sign when one event is dropped, and an instrument carried by one utility (Dominion Virginia, 80% of first-stage covariance). Their critique covers their own designs. It does not test Watten's highway-plan instrument. Watten et al. report a state-level scatter where Virginia sits near the average price change (Figure 2), and a first-stage F of 7.9 for the preferred specification.

6. Magnitude of the "doubling" reading in Watten et al. The paper says a doubling of capacity lowers residential prices 3.5% (p.21) and that "every 10% increase" lowers them about 0.4% (p.3). The regressor is the inverse hyperbolic sine of cumulative capacity and the coefficient is -0.035. Since the inverse hyperbolic sine behaves like a natural log, a doubling adds about ln 2 = 0.69 to it, which gives about -2.4%, and a 10% increase adds about 0.095, which gives about -0.33%. The 160% to 6% reading on p.3 does match the coefficient times the stated 1.6 difference. This is the researcher's arithmetic and not a finding of the paper. The appendix figures C1 and C2 label the vertical axis "percent change in response to a doubling" by multiplying the coefficient by 100, so the paper's own convention treats the coefficient as the doubling effect. Unresolved. A writer who uses "doubling" should cite the coefficient and the paper's wording, and not convert.

7. E3 versus the commission's description. The commission says E3 "finds no evidence of increases". E3 states no evidence of historical subsidization or cost shifting, no clear state-level relationship between load growth and rate increases, and PJM as an exception, and attributes about half of the 2025/2026 PJM capacity price rise to load growth. It also says "the risk of increasing rates and cost shifting from load growth is real".

8. PJM capacity attribution. The IMM says data-center load growth is "the primary reason" for PJM capacity conditions and prices ("but for data center growth ... would not have seen the same ... high prices"), and prices out $23.1 billion over three auctions. E3 attributes about 50% of the one-year increase between the 2024/2025 and 2025/2026 auctions to load growth. Different counterfactuals: IMM removes all data-center load from the forecast and re-clears the auction. E3 decomposes the price change between two auctions across five drivers. Neither is a retail-bill measure.

9. Stale or unlocated leads. (a) "$2.59/MWh-per-GW decrease" and its companion $3.49 for non-residential: found only in a City Journal write-up (https://cityjournal.substack.com/p/data-centers-reduced-electricity, 8 Oct 2026, read through WebFetch summary) of an earlier version of the Elhai and Zhou paper at the same URL, which the write-up says used a firm-Bartik IV, found OLS +$1.83 residential and -$0.99 non-residential, and wholesale +$1 to $3/MWh. The 4 Nov 2026 version has different numbers (Table A.2: IV -2.81 and -2.40, OLS +1.48 and -3.14), moves the IV to the appendix, and calls it not credible. The earlier version could not be retrieved (the web archive copy returned 403). Do not cite $2.59 or $3.49. (b) "-3.5% for a doubling, 2015-2024" is Watten et al., not a separate paper. (c) "Harvard and Penn": the peg paper is Wharton (Rana, Netessine) plus Harvard Business School (Kaps). Elhai and Zhou are Harvard economics and not part of the peg.

## Numbers

### Estimates in a comparable form

Units. Prices in $/MWh unless stated. 1 cent/kWh = $10/MWh. 2025 EIA average residential price 17.30 cents/kWh = $173/MWh (EIA page). "Per GW" means gigawatts of data-center nameplate capacity.

```text
Figure: Peg paper. Industrial +5.4 $/MWh (15% of observed increase). Residential +1.7 $/MWh ("4% of the observed increase since 2020"). Big Tech additions: no discernible increase. Co-location additions: increase.
Owner:  Rana, Kaps, Netessine, SSRN 7580459, abstract.
Scope:  Retail price; "their region" (definition not seen); data centers built 2020-2025; synthetic control with cumulative repeated treatment; average over treated regions; exposure unit is cumulative additions (unit of the dose not seen). The percentages are shares of the observed price increase, not percent price effects.
```

Derived, researcher's arithmetic, rough scale only: 1.7 / 0.04 implies an observed residential increase of about $42.5/MWh since 2020, and 5.4 / 0.15 implies about $36/MWh for industrial. Against the 2025 EIA national residential average of $173/MWh, $1.7/MWh is about 1%. Regions and periods differ from EIA's national average, so state this only as a size comparison.

```text
Figure: EPRI. Residential average price at fixed residential sales: coefficient -0.035 on the inverse hyperbolic sine of cumulative capacity, Anderson-Rubin 95% CI [-0.121, -0.014], F 7.869 (2015-2024). 2019-24 subsample -0.017, CI [-0.034, -0.006], F 21.6. Paper's reading: -3.5% per doubling; -6% for the average residential customer, whose state's capacity grew 160%.
Owner:  Watten, Bistline, Blanford, arXiv 2606.19777v1, Table 2 p.20 and p.21.
Scope:  Average residential retail price (revenue, EIA-861 bundled service) conditional on residential sales; state-year panel; capacity added 2015-2024 (21.3 GW CONUS); 2SLS with region fixed effects, highway-plan instrument.
```

```text
Figure: Meeks et al. Average retail price after first data-center entry: +2.7% all, +2.1% residential (0.32 cents/kWh, about $3.21 a month on a $153 bill), +2.8% commercial, +4.2% industrial. Investor-owned utilities: +5.6% all, +5.2% residential (0.88 cents/kWh, about $7.34 a month on a $141 bill), +4.6% commercial, +8% industrial. IV on log cumulative capacity: 0.073 and 0.078 (average retail price).
Owner:  Meeks, Pless, Qi, Wang, CEEPR WP 2026-13r, Tables 2 and 3 pp.50-51; Section 6.3 p.28; p.30.
Scope:  Average retail price, utility-state-year, entry 2010-2024, first activation above 5 MW in a county, Callaway-Sant'Anna DiD, 973 utilities. Pre-treatment mean residential price 0.15 $/kWh.
```

```text
Figure: Scalera et al. Residential price +13% per standard deviation of ten data centers; +4% for a single hyperscaler facility.
Owner:  Scalera, Bosetti, Pecci, CEPR DP21854, abstract (read on https://cameron-scalera.com/).
Scope:  Household electricity price; utility territories; build-out after 2021; shift-share with pre-AI fiber. Full paper not opened, so the base, period and sample are unknown. A press quote in a search summary ("11-13% increase" for about ten data centers) was not opened.
```

```text
Figure: USC Marshall. Residential +0.62% per doubling of a utility's operating data-center capacity ($1.00 to $1.06 per MWh). Zone wholesale LMP +$3.44/MWh per entry (energy +$5.43). CAISO node congestion +$2.30/MWh first-year, +$1.45/MWh all entries.
Owner:  Ryu and Hiatt, USC Zage Business of Energy Initiative, 2026. The paper was not found. Figures read in the NCEA brief https://energyanalytics.org/research/dont-blame-the-data-centers.
Scope:  Retail utility level 2015-25; wholesale 2020-25. Brief calls the retail results conditional associations, not causal.
```

```text
Figure: Elhai and Zhou dispatch model. Wholesale price effect of cumulative data centers in 2025: +$1.63/MWh (range across placements $1.44 to $3.13); about $0.33 to $0.41/MWh per GW; $2.3 billion a year at full pass-through for residential customers. 1 GW raises costs over $3/MWh in New England and $0.30/MWh in the upper Midwest.
Owner:  Elhai and Zhou, 4 Nov 2026 version, Introduction pp.2-3, Section 4.4 pp.23-24.
Scope:  Wholesale energy price only, regional supply curves, load at 70% of nameplate, no capacity-market or infrastructure channel; 11 regions.
```

```text
Figure: Elhai and Zhou reduced-form retail estimates. Firm-Bartik IV, per +1 GW: residential -2.81 $/MWh (AR set -15.01 to +0.31), non-residential -2.40 (-9.35 to +0.64). OLS +1.48 and -3.14. LP-DiD residential average over h=0-3, unconditional -5.1 (leave-one-out -10.0 to +2.6), entropy-balanced +1.6 (-6.4 to +7.5).
Owner:  Elhai and Zhou, Table A.2 p.52, Table A.1 p.51. The authors call neither design credible.
Scope:  Residential and non-residential retail price change 2018-2024, utility-state level, 2019-24 additions, dispatch-region fixed effects.
```

```text
Figure: Dallas Fed. Wholesale price effect of data centers, preferred scenario: national +6.9% in 2025, +12.3% by 2028. Northern Virginia +$5.22/MWh (15.0%); Pacific Northwest +$5.68/MWh (15.4%); Florida and interior South as low as $0.42/MWh (1.0%) in 2025.
Owner:  Kay, Reaser, Taylor, Dallas Fed WP 2606r1, Introduction pp.2-3.
Scope:  Load-weighted wholesale price, 23 regions, hourly dispatch, 2021-2025 realized, 2026-2028 scenarios. Fixed costs assumed fixed in the retail section. The March version said 2 to 6 percent.
```

Series for a possible chart, PJM capacity (IMM Table 1, p.4), increase in capacity-market revenues due to data-center load, dollars, all data-center load (above-embedded in parentheses):

```text
2025/2026 delivery year  9,332,103,858  (7,742,960,157)
2026/2027 delivery year  7,271,197,971  (7,271,197,971)
2027/2028 delivery year  6,497,653,512  (6,244,523,827)
Total                   23,100,955,341 (21,258,681,955)
```

Owner IMM. Scope: PJM RTO capacity market, three base residual auctions, counterfactual with data-center load removed from the peak forecast, with the price cap and floor in place for the last two. The 2027/2028 figure is 65.5% of actual auction revenue of $16,411,578,225. PJM RTO capacity prices from E3 (nominal, $/MW-day): 28.92 (2024/2025), 269.92 (2025/2026). E3 gives these without a table citation in the text I read; confirm against PJM's auction reports before charting (PJM BRA report links appear in the IMM report footnotes 4 and 5).

```text
Figure: Class-average 2025 retail prices: residential 17.30, commercial 13.41, industrial 8.62 cents/kWh; all-customer average 13.63.
Owner:  EIA, Electric Power Monthly Table 5.3 (Feb 2026, preliminary), via the EIA page above.
Scope:  U.S., 2025 annual average.
```

### Components of a residential rate a new load can move

Each row names the direction the cited paper supports and who owns the claim. "Cited" means read in the document named.

```text
Component:  Wholesale energy cost of generation (dispatch up the supply curve)
Direction:  up. Short-run supply curves are convex, so effects are larger where supply is tight.
Owner:      Dallas Fed WP 2606r1 (national +6.9% by 2025, $0.42 to $5.68/MWh by region); Elhai and Zhou Section 4 ($1.63/MWh in 2025). Passes to retail through spot-linked supply and hedges with a lag (Dallas Fed footnote 3, p.3).
Component:  Capacity (resource adequacy) payments in capacity-market regions
Direction:  up where supply is short. IMM prices PJM data-center load at $23.1 billion over three auctions.
Owner:      IMM Part A Table 1; E3 Figure 6 for a lower attribution; Elhai and Zhou p.12 say PJM's effect also reflects market design and interconnection backlogs.
Component:  Fixed T&D and generation capital recovered per kWh of sales (fixed-cost spreading)
Direction:  down, if sales grow faster than costs and no new capacity must be built.
Owner:      Watten et al. Section II and the Supplemental Appendix model (concave cost-demand relationships; T&D and generation); Dallas Fed Equations 14 and 15 (the fixed-cost share s and break-even s*); E3 primer p.9.
Component:  New transmission, distribution and generation investment added to rate base
Direction:  up where investment is socialized across customers. Meeks et al. find construction, generation investment, distribution equipment and authorized rate bases rise after entry, at investor-owned utilities.
Owner:      Meeks et al. Section 7.1 and 7.2; Dallas Fed Assumption 1 caveat p.51; Elhai and Zhou p.12 (some paid directly by data centers under service contracts, some spread).
Component:  Cost allocation between customer classes and large-load tariffs (who pays the cost)
Direction:  either. Tariffs, minimum bills and up-front contributions assign cost to the load that causes it; E3 counts 38 new large-load tariffs between 2018 and 2026 (E3, sponsor-funded). Watten et al. Table 1 finds no evidence of cross-class subsidization of system costs in their state data.
Owner:      E3 pp.2, 8-10 (sponsor); Watten et al. Table 1 p.11; Meeks et al. Section 7.2.2.
Component:  Load-forecast error and stranded cost
Direction:  up if forecast data-center load does not materialize and capacity is overbuilt, spreading fixed costs over fewer kWh.
Owner:      Watten et al. Discussion p.23. IMM Part A p.2 (13,018 of the 17,071 MW of data-center load in the 2027/2028 auction was new or forecast growth, not existing load).
Component:  Natural-gas fuel price
Direction:  up, judged small by the authors; excluded from their estimates.
Owner:      Watten et al. pp.23-24 (back-of-envelope: about 2% of US gas consumption in 2024 goes to data centers via power generation). Not tested.
```

## Limits

- Full text of the Rana, Kaps, Netessine study could not be found or opened. SSRN (https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580459) and the HBS record (https://www.hbs.edu/faculty/Pages/item.aspx?num=69599) return 403 to a plain fetch, and the authors' own pages link only to SSRN. Only the abstract is read, via Crossref. Unknown: the sample (a co-author's LinkedIn summary reported 42 utilities in a search summary, not opened), the definition of "region", the exposure unit, the standard errors, the pre-trend evidence, whether the 4% and 15% shares are of nominal or real price increases, and whether the Big Tech versus co-location split is estimated or descriptive. The peg should be described only as far as the abstract and the Post's coverage reach.
- The Post article was not opened. Coverage was read through a syndicated copy and a small-model summary. Do not quote the Post.
- The CEPR/VoxEU column and CEPR DP21854 PDF were blocked. The commission's "larger effect on households" is consistent with the authors' abstract but the column itself was not read. Per-facility cents per kWh and distribution-spending figures seen in a search summary were not confirmed.
- The USC study (Ryu and Hiatt) was not found. The 0.62% figure is read in an NCEA issue brief co-authored by an author of the study. A secondary summary supports only that those words and numbers appear there. The brief says the retail result is not causal.
- The $2.59 and $3.49 per-GW figures are not in the current Elhai and Zhou paper and could not be traced to an earlier version.
- LBNL's "Retail Price Trends and Drivers" 2026 edition (Wiser et al.) returned 403, so it was not read. It is the standard source for state-level price drivers and the "load growth and prices" relationship (E3 and FactCheck.org cite it). No figure from it is used here. FactCheck.org's description of LBNL (https://www.factcheck.org/2026/10/data-centers-and-electricity-prices-its-not-as-simple-as-voters-may-think/) came from a small-model summary only.
- No document read gives the share of a typical residential bill that is energy, capacity, transmission, distribution and fees, for the US or for PJM. A figure of 10 to 20% of a typical PJM bill for capacity charges came only from the FactCheck.org summary and is unconfirmed. Dallas Fed Appendix G calibrates s by state from EIA-861 and the wholesale price (PDF pp.101-104 not read in detail). A rate-component graphic would need EIA or a state commission as owner.
- Which estimate the evidence supports most cannot be settled by one design ranking. For PJM capacity cost, the IMM is the primary and a mechanical re-clearing, with E3 giving a contested lower attribution. For retail rates nationwide, no document read shows a design that survives the critique Elhai and Zhou make of reduced-form approaches, and Watten and Meeks conflict in sign. The wholesale dispatch results (Dallas Fed, Elhai and Zhou) agree on sign and differ in size (Dallas Fed 6.9% national and $5.22/MWh in northern Virginia; Elhai and Zhou $1.63/MWh national average and $0.33 to $0.41/MWh per GW). Both are models, not measurements, and they ignore the fixed-cost channel.
- Period split between before and after the 2023 AI buildout: no document reads its results that way. Watten et al. report 2015-2024 and 2019-2024 (half the full-sample effect). Rana et al. cover 2020-2025. Meeks et al. cover 2010-2024. Dallas Fed covers 2021-2025. IMM covers three auctions for delivery years 2025/2026 to 2027/2028. The writer can state which window each estimate covers but not an effect "before versus after".
- Demand-side assumptions. Data-center load is mostly not observed: Watten et al. assume 50% utilization, Elhai and Zhou 70% of nameplate, Dallas Fed uses scenarios. S&P Global and Aterio capacity data are commercial and not public.
- Appendices not read in full: Meeks et al. appendices (Table A9 IV, Table A2); Dallas Fed Appendix G; Watten et al. Supplemental Appendix tables beyond C1, C2.
- State utility commission findings were not sought: the PJM and price results were enough for the mechanism. A commission decision on a large-load tariff is open for the writer if a state example is wanted, with the commission as owner.
- Fixed-cost spreading is the paper's explanation for the negative sign (Watten et al.). It is not tested directly against rate-case cost data: the cost-demand regressions are correlations, and Watten et al. say the concave pattern is also consistent with reverse causality (p.10).

## Source assets

```text
Asset: Elhai and Zhou Figure 1 (PDF p.11), four stylized supply-and-demand panels (steep or flat supply, large or small emissions externality) with the same added load K and the price change ΔP marked.
Shows: Why the same load moves the wholesale price by different amounts depending on the slope of the local supply curve.
Crop:  Keep all four panels, axis labels (P, Q), and the ΔP and MEE markers. Omit the emissions-externality curves if the article is only about price.
```

```text
Asset: Dallas Fed Equations 14 and 15 (PDF pp.54-55) and Figure 15 map (PDF p.55), "Threshold Fixed Cost Share Required for Rate Relief", with Figure 16 (PDF p.56) including spillovers.
Shows: The condition under which a new load can lower average rates: the fixed-cost share of the rate must exceed (1 + d) / (1 + d + eta). Darker regions need a higher fixed-cost share.
Crop:  Keep the equation with its symbol definitions and the map legend. The map is a model output with assumptions stated in its note, including Assumption 1 (no new fixed costs).
```

```text
Asset: Watten et al. Figure 2 (PDF p.18), state scatter of percent change in sectoral average price against data-center capacity added as a share of sectoral demand; and Table 2 (p.20).
Shows: The raw state-level pattern the IV result starts from (Virginia near the average, California the largest price rise with little data-center growth) and the OLS versus IV coefficients.
Crop:  Keep axis labels, the highlighted states, and circle-size legend. Panel (c) in levels can be dropped.
```

```text
Asset: Elhai and Zhou Figure A.3 (PDF p.50) and Table A.1 (PDF p.51), local-projections DiD estimates with 95% intervals, and the leave-one-event-out table.
Shows: Why a retail-price estimate from few treated utilities can be wide enough ("$30 or more") to include both signs, against prices of $100 to $200/MWh, and how one dropped event flips the sign.
Crop:  Keep the interval whiskers and the horizon axis for the residential row. Keep the "Sign flips" column of Table A.1.
```

```text
Asset: Elhai and Zhou Figure 6 (PDF p.25), cumulative data-center wholesale price effects, actual versus random and versus min and max placements.
Shows: Actual buildout's price effect sits near the price-minimizing placement because data centers went to flat supply curves.
Crop:  Keep both panels and the legend of random, minimum and maximum.
```

```text
Asset: Meeks et al. Figure 2 (PDF p.44), event-study estimates before and after first data-center activation; Table 3 (p.51) for the ownership split.
Shows: Price path relative to entry year and the investor-owned versus public versus cooperative contrast.
Crop:  Keep pre-period points to show pre-trends. Keep the customer-class panels if a class comparison is wanted.
```

```text
Asset: IMM Table 1 (PDF p.4), capacity-market revenue increase by delivery year attributed to data-center load.
Shows: The size and the decline across the three auctions ($9.3, $7.3, $6.5 billion), with the footnote that the decline reflects higher prices without data-center load.
Crop:  Keep both columns (all data-center load; above embedded) and the totals row.
```

```text
Asset: E3 Figure 6 (PDF p.25), waterfall of PJM capacity price change from $29 to $270 per MW-day by driver.
Shows: E3's split of the 2025/2026 rise into peak load, supply, programme design, cost of new entry and the FRR alternative.
Crop:  Keep driver labels and signs. Caption must name the Data Center Coalition as funder. Not an IMM figure. The footnote on the page states the Shapley-style method and that results "do not reflect unit-level bidding behavior".
```

```text
Asset: None found for the peg study itself (full text not opened).
```

## Discarded

```text
https://www.hbs.edu/faculty/Pages/item.aspx?num=69599: gated (403), listing only, no text read; the SSRN abstract is the record.
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7580459 (page itself): 403; abstract used via Crossref and recorded above.
https://cepr.org/voxeu/columns/how-data-centres-affect-electricity-prices-and-whom and https://cepr.org/publications/dp21854: blocked by Cloudflare; abstract read on the author's page.
https://www.nber.org/system/files/working_papers/w35100/w35100.pdf: returned a block page; title ("Measuring the Impact of Data Centers in the United States") seen only in a search result; not read.
https://emp.lbl.gov/sites/default/files/2026-03/Retail%20Price%20Trends_2026%20edition.pdf and the July update on eta-publications.lbl.gov: 403, not read (see Limits).
http://web.archive.org/web/20261008180112/https://celhai.github.io/pdfs/Elhai_Zhou_data_centers.pdf: 403; the earlier Elhai and Zhou version could not be retrieved.
https://www.washingtonpost.com/...: gated; coverage read through a syndicated copy (see Sources). A guessed Post URL also failed. The Yahoo copy returned 429 to a later plain fetch.
https://cityjournal.substack.com/p/data-centers-reduced-electricity: opinion outlet, read only through a small-model summary; used solely to trace where the $2.59 and $3.49 figures came from.
https://www.factcheck.org/2026/10/data-centers-and-electricity-prices-its-not-as-simple-as-voters-may-think/: read through a small-model summary only. Secondary; not used for any figure.
https://utilitydive.com/news/pjm-data-centers-capacity-auction-imm-bowring/825626 (and related Utility Dive pieces): coverage of IMM statements about a later auction ($6.3 billion of $16.4 billion, 38%) that the article says were from an email and interview with the monitor's president, with the report not yet published; superseded by the IMM Part A primary. The "$16.4 billion" in that coverage coincides with the 2027/2028 auction revenue in the IMM report ($16,411,578,225), so the delivery year is unresolved. Not used.
https://gizmodo.com/..., https://www.tomshardware.com/... (Bloomberg wholesale analysis, "up to 267 percent"), other news and substack summaries from search results: secondary coverage, not opened or not needed once the owning document was read.
https://hg.gatech.edu/node/689280: a Georgia Tech review of data-center flexibility; not the Georgia Tech retail-price working paper that E3 mentions; no price estimate.
https://hls.harvard.edu/today/how-data-centers-may-lead-to-higher-electricity-bills/ and the Harvard Electricity Law Initiative piece on special contracts: seen only as a search result; not opened. A candidate for the cost-allocation component if a writer wants it.
https://arxiv.org/pdf/2608.09882, https://www.tse-fr.eu/sites/default/files/TSE/documents/doc/wp/2026/wp_tse_1726.pdf, https://www.instituteforenergyresearch.org/..., and other search results: titles only, not opened.
Dallas Fed WP 2606 March 2026 version (https://www.dallasfed.org/~/media/documents/research/papers/2026/wp2606.pdf): read; superseded by the October revision (6.9% national in 2025 against 2 to 6% earlier).
```
