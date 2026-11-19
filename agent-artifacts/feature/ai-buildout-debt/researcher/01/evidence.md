# Evidence record: feature/ai-buildout-debt (researcher 01)

The November 2026 Financial Stability Report prints every figure in the commission, and each one checks against the page, with one change of meaning. The $680 billion is issuance in January to October 2026 alone, not a running total. Figure C (p. 24) carries the central comparison. For seven firms at 2026:Q2 it shows roughly $0.88 trillion of on-balance-sheet debt beside about $1.02 trillion of leases yet to start and about $2.07 trillion of "guarantees & contract commitments". The Fed says these undiscounted commitments are "not directly comparable" with discounted debt. The chain from hyperscaler to final holder is named on p. 25, without amounts for any link except the large bank holding companies' "close to $1 trillion", and that figure also covers utilities and big technology firms generally. The record is thin in four places. (1) No chart data has been published for the November report, so every series below was read from the vector geometry of the Fed's PDF charts, not taken from a Fed table. (2) The Fed does not split the $2 trillion between guarantees and take-or-pay purchase contracts. The filings I opened point to purchase commitments as the larger share: the identifiable credit guarantees come to under $200 billion. (3) Governor Barr's speech puts the seven firms' debt below $800 billion at the time he spoke, which conflicts with the figure-derived $879 billion. (4) Two Fed sources cut against the angle. The box itself says the large firms "may absorb losses ... mitigating their effects on the rest of the financial system", and Barr says he is "less concerned about direct losses" given "the still-limited amount of debt".

Method note for every value marked "figure-derived": I parsed the filled rectangles in the PDF's vector drawing layer (PyMuPDF `get_drawings`) and scaled each bar against the chart's own axis tick positions. Precision is about ±2 billion dollars on Figure A, about ±5 billion on Figure C, and about ±0.5 percentage point on Box 5.1. The Box 5.1 spring values agree with the Fed's own May 2026 chart descriptions, and the Figure A totals agree with the box text ($130 billion for 2023, more than $680 billion for 2026). Both checks support the method. Cite these as "Federal Reserve Board, FSR November 2026, figure X; values read from the published chart", never as Fed-published numbers.

## Sources

### 1. Federal Reserve Board, Financial Stability Report, November 2026

```text
URL:         https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf
Kind:        primary. Board of Governors of the Federal Reserve System authors the measurement and the assessment. Data as of October 28, 2026 (Contents page). PDF created 13 Nov 2026. Same file (md5 6c8acf07…) as the scratch copy.
Establishes: firsthand: Box 2.2 issuance, share, outstanding, obligations, holders and bank exposure; Box 5.1 survey results; figure notes.
Locators:    printed page = PDF page − 8. Box 2.2 = printed pp. 23–25 (PDF 31–33). Box 5.1 = pp. 49–50 (PDF 57–58). Figure notes for Box 2.2 = p. 55 (PDF 63); for Box 5.1 = p. 60 (PDF 68).
```

Paraphrase, Box 2.2 (p. 23): Debt issuance for "advanced computing infrastructure" rose to more than $680 billion by October 2026, "about a fivefold increase from $130 billion in all of 2023" (figure A). Investment-grade technology companies issued most of it. As a share of nonfinancial investment-grade corporate debt issuance it went from "less than 6 percent in 2023 to about 31 percent in 2026". Outstanding public debt related to advanced computing "is estimated at more than $1.1 trillion as of October 2026". Private credit transactions make "the exact magnitude of advanced computing–related debt outstanding more difficult to measure". The composition is moving "from mostly corporate bonds to a combination of public and private debt, structured credit, and project finance". Large technology firms are "rapidly increasing future lease commitments, backstop guarantees provided to other firms, and other complex and contingent obligations".

Footnote 2 (p. 23): the issuance estimate includes public deals and rule 144A private securities, "does not capture all of these private deals", and excludes section 4(a)(2) private placements. Footnote 3 defines hyperscalers for figure B as Amazon, Alphabet, Meta Platforms, Microsoft and Oracle.

Paraphrase, Box 2.2 (p. 24): "While debt balances have grown, other obligations have grown even more rapidly (figure C)." They are not-yet-commenced leases "(whose undiscounted values exceed $1 trillion)" and "other obligations such as take-or-pay contracts and residual value guarantees (whose undiscounted values exceed $2 trillion)". Footnote 5: these figures "are generally not discounted and therefore are not directly comparable with on-balance-sheet debt, which is discounted. This analysis includes Amazon, Alphabet, Broadcom, Meta Platforms, Microsoft, Nvidia, and Oracle." Figure C source line: SEC Forms 10-Q and 10-K; Bloomberg Finance L.P.; Federal Reserve Board staff estimates. Figure C legend: "Debt", "Leases yet to start", "Guarantees & contract commitments".

Paraphrase, Box 2.2 (p. 25), the chain as the Fed states it:
- Long-term contracts, leases and guarantees let strong-credit firms "support the financing of projects developed by weaker-credit firms without having an immediate, direct effect on the balance sheets of the stronger-credit firms."
- Hyperscalers sign long-term leases with third-party developers, and the developers use the leases "to secure financing for the data center's construction."
- GPU makers "often provide a guaranteed residual value of the GPU collateral" to support purchases by advanced computing or LLM firms. The debt links are often supplemented with equity investments, creating "a 'circular financing' dynamic."
- The large firms "may absorb losses in the event of a future downturn, mitigating their effects on the rest of the financial system. However, it also suggests that these firms' economic exposure to such a downturn may be substantially larger than suggested by their on-balance-sheet liabilities."
- Hyperscaler and GPU firms' on-balance-sheet debt is "held primarily in mutual funds, pension funds, and insurance companies."
- "A significant portion of these other obligations relate to financings that often involve special purpose entities (SPEs) that themselves issue both senior and subordinated debt. The riskier subordinated debt and equity tranches ... are held by high-yield bond funds, life insurance companies, BDCs, and other private debt vehicles."
- "the largest U.S. bank holding companies have close to $1 trillion of exposure to large technology firms, data center developers, advanced computing–related SPEs and private credit vehicles, and utility companies, and those exposures are evaluated during the annual supervisory stress test."

Quote (p. 25, exact wording matters because it limits the angle): "via these connections, the largest technology firms may absorb losses in the event of a future downturn, mitigating their effects on the rest of the financial system."

Paraphrase, elsewhere in the report:
- p. 22: "The complex interlinkages among firms engaged in the data center buildout, public credit markets, private lenders, and special purpose financing vehicles create vulnerabilities that necessitate close monitoring."
- p. 9: bond issuance "by the largest investment-grade firms involved in operating data centers was greater than $150 billion year to date and has been met with strong investor demand."
- p. 36: securitizations of digital infrastructure, data centers included, grew, "though the size of the outstanding market was small compared with the overall data center financing market."
- p. 47 (Section 5): most respondents cited risks from new computing technologies, including "vulnerabilities stemming from complex financing arrangements for data center investment". The first near-term risk listed is "Disappointing returns on U.S. business investment could decelerate the economy and trigger declines in asset prices".

Paraphrase, Box 5.1 (pp. 49–50): Federal Reserve Bank of New York staff ran the survey and received responses from 23 contacts in September and October. The box "should not be interpreted as representing the views of the Federal Reserve Board or the Federal Reserve Bank of New York." "AI was the top-cited risk", with concerns around equity valuations, AI-enabled cyberattacks and "complex forms of AI-related financing". "mentions of AI, higher long-term interest rates, and cyberattacks saw the greatest increase relative to the spring survey (figure B)." Figure B (spring) has 20 contacts, March–April. The survey question (p. 60) asks which shocks "would have the greatest negative impact on the functioning of the U.S. financial system". The Overview (p. 3) and Section 5 (p. 47) add that fewer participants cited private credit than in spring.

Figure notes (p. 55): Figure A data "begin in November 2022 and extend through October 2026", so the 2022 bar covers two months and the 2026 bar ten. Figure C "include[s] the hyperscaler firms Alphabet, Amazon, Meta Platforms, Microsoft, and Oracle, as well as graphics processing unit makers Broadcom and Nvidia."

### 2. Federal Reserve Board, Financial Stability Report, May 2026 (the "before")

```text
URL:         https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf
Kind:        primary. Board's own earlier assessment.
Establishes: no data-center leverage box in May. Its AI content is the survey and one issuance sentence.
Locators:    p. 9 (Asset Valuations, issuance sentence); Box 5.1 pp. 49–50.
```

Paraphrase: "Bond issuance among the largest investment-grade firms involved in cloud computing neared $100 billion in the first quarter and was met with strong investor demand" (p. 9). In the spring survey, geopolitical risks and an oil shock were top-cited. "aI-related risks were in focus as well, particularly concerns around equity valuations, debt-financed capital spending, and risks to the labor market." Under the survey's AI heading, respondents said capital expenditures "are increasingly funded by debt, creating leverage in the system" (p. 49).

### 3. Federal Reserve Board, May 2026 FSR chart data and descriptions

```text
URL:         https://www.federalreserve.gov/publications/2026-may-financial-stability-report-accessibility-tables.htm
Kind:        primary. The Board's own accessible description of its May figures.
Establishes: Fed's own approximate readings of the spring 2026 and fall 2025 survey bars. Used to check my geometry method.
Locators:    Box 5.1, Figure A (Spring 2026) and Figure B (Fall 2025) descriptions, near the end of the page.
```

Paraphrase: Spring 2026: geopolitical risks about 75 percent, oil shock about 70, "Artificial intelligence and private credit are both cited at about 50 percent", higher long-term rates and cyberattacks 20. Fall 2025: AI "about 30 percent". The Board's FSR index (https://www.federalreserve.gov/publications/financial-stability-report.htm, "2026" heading) lists only a PDF for November 2026, with no "Chart Data and Descriptions" link. Guessed URLs for a November 2026 data page returned 404 on 19 November.

### 4. Michael S. Barr, "Some Potential Financial Stability Implications of Artificial Intelligence", 16 November 2026

```text
URL:         https://www.federalreserve.gov/newsevents/speech/files/barr20261116a.pdf  (HTML: https://www.federalreserve.gov/newsevents/speech/barr20261116a.htm)
Kind:        primary for his own statements. Exact title on the cover: "Michael S. Barr, Member, Board of Governors of the Federal Reserve System", at the Seventh Annual ACM International Conference on Artificial Intelligence in Finance, Milan. Repeats FSR figures and adds one not printed in the FSR.
Establishes: firsthand: his judgment, and the "$800 billion" debt statement. Merely repeats: the FSR's obligations totals.
Locators:    speech pp. 4–7 (section "Leverage in the Data Center Buildout"); footnote 5 on p. 5.
```

Paraphrase: "On-balance-sheet debt of the seven largest AI firms has been growing significantly in 2026 and is expected to exceed $800 billion before year's end" (p. 4). "The FSR estimates that the potential maximum nominal value of these types of obligations, or off-balance-sheet liabilities, now exceeds $3 trillion" (p. 5). He lists them as energy supply contracts, long-term data center and compute leases, and "a wide variety of off-balance-sheet financing structures". Footnote 5: firms present these "before discounting, which complicates comparisons". Hyperscalers and GPU producers have "over $100 billion in cumulative equity investments in large language model (LLM) labs and cloud-computing start-ups" (p. 6). Firms dependent on external funding are shifting "from issuing corporate bonds to issuing asset-based financing". The larger firms "often guarantee the resale value for the data centers or GPUs that are used as collateral" (p. 6).

Quote (p. 7, the strongest statement against a debt-crisis reading, from a Board member): "Given the still-limited amount of debt backing the current boom, I'm less concerned about direct losses. However, with leverage at hedge funds and broader risk appetite apparently quite high, a sharp reversal could lead to rapid deleveraging and, potentially, self-reinforcing fire sales."

### 5. OCC, Semiannual Risk Perspective, Fall 2026 (12 November 2026)

```text
URL:         https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-fall-2026.pdf
Kind:        primary. Office of the Comptroller of the Currency, National Risk Committee; bank-supervisor view of OCC-supervised banks. Data as of June 30, 2026.
Establishes: supervisor's description of bank lending to the buildout and its seniority. No dollar amounts for that lending.
Locators:    Executive Summary p. 1; Part I, A. Credit Risk, pp. 2–3.
Note:        scripted requests to www.occ.gov got a 302 "Security Redirect" to the homepage (bot filter, gated not dead). The same file was served from occ.treas.gov. The OCC news release (https://www.occ.gov/news-issuances/news-releases/2026/nr-occ-2026-99.html) links the occ.gov address above.
```

The OCC's term: the report calls AI "Super Intelligence (SI)" throughout. Quote it as written, or say "what the OCC calls super intelligence". Do not silently substitute "AI" inside a quotation.

Paraphrase: Banks provide "project-based and other secured financing to investments in Super Intelligence (SI) infrastructure. Although OCC-supervised banks tend to hold senior positions in these structures, the rapid increase in funding needs ... and the use of novel financing structures warrant monitoring" (p. 1). Investment is "financed through project-level and other third-party financing structures via project and construction financing based on long-term lease obligations, purchase commitments, and guarantees". Specialized SI companies raise funds "from the non-investment grade bond market and private sources, typically with some backing from large tech companies". These arrangements "can be opaque due to the use of off-balance sheet and contingent financing commitments" (p. 3). Lending from large banks "is typically senior in the capital structure and often secured". The risks it names are construction delays, power availability, community sentiment and "technological depreciation or obsolescence occurring prior to loan amortization and refinancing". "The resilience of novel financial and contractual structures used in data center financing has limited performance under stressed conditions. To date, the quality of credit provided by banks is supported by their senior position as well as strong demand for processing power" (p. 3).

### 6. Meta Platforms, Form 10-Q for the quarter ended 30 September 2026 (filed 22 Oct 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm
Kind:        primary. Meta reports its own obligations; it has a stake in how they read.
Establishes: firsthand: its leases not yet commenced, its purchase commitments, its residual value guarantees to the data center ventures, and its serviceability claim.
Locators:    Note 5 "Data Center Ventures" pp. 17–18; Note 10 "Commitments and Contingencies" p. 21; MD&A "Liquidity and Capital Resources" pp. 49–50.
```

Paraphrase: Operating and finance leases not yet commenced as of 30 September 2026 "were approximately $355.73 billion, consisting of data centers, energy-related infrastructure, colocations, and certain network infrastructure", commencing from the remainder of 2026 through 2036 with terms of more than one year to 30 years (p. 21). Non-cancelable contractual commitments are $454.52 billion, "mostly" third-party cloud capacity, servers and network infrastructure, data center energy, and Reality Labs hardware. In addition there are contingent obligations of up to $14.72 billion to buy cloud capacity (p. 21).

Data center ventures (pp. 17–18): Meta holds 20% of a Louisiana venture (October 2025, about $27 billion estimated development cost) and of a Texas venture (July 2026, about $14 billion). It leases the campuses from them, from 2029 and 2028, on four-year initial terms renewable to 20 years. It has provided residual value guarantees: if it ends a lease, its maximum payment is the shortfall between fair value and the guarantee threshold. "RVG payments are not probable, and therefore no liability has been recorded to date." Meta does not consolidate either venture. The maximum exposure to loss table (p. 18): carrying value $4,732 million; lease commitments $18,476 million; future funding $3,703 million; "Maximum residual value guarantees" $41,493 million (December 2025: $28,091 million); total $68,404 million.

Rival position, Meta's own words (p. 49): "We currently anticipate that our available funds and cash flow from operations and financing activities will be sufficient to meet our operational cash needs and fund our cash commitments for investing and financing activities, including investments in infrastructure and AI initiatives ... over the next 12 months and thereafter for the foreseeable future." Supporting figures (pp. 48–49): nine-month operating cash flow $96.87 billion; capital expenditures including finance lease principal $85.82 billion; $84.00 billion of Notes outstanding (p. 50); 2026 capex guidance $135–145 billion.

### 7. Microsoft, Form 10-Q for the quarter ended 30 September 2026 (filed 28 Oct 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm
Kind:        primary. Its own obligations and its own liquidity claim.
Establishes: leases not yet commenced, and the serviceability statement.
Locators:    Note 12 "Leases", p. 22; MD&A "Liquidity and Capital Resources", p. 37; cash flow statement.
```

Paraphrase: "As of September 30, 2026, we had additional leases, primarily for datacenters, that had not yet commenced of $364.6 billion, with some arrangements subject to certain contractual conditions being met." They commence between fiscal 2027 and fiscal 2034 with terms of 1 to 20 years (p. 22). Quarter: cash from operations $58.0 billion; additions to property and equipment $39.4 billion.

Rival position, own words (p. 37): "We expect existing cash, cash equivalents, short-term investments, cash flows from operations, and access to capital markets to continue to be sufficient to fund our operating activities and cash commitments ... for at least the next 12 months and thereafter for the foreseeable future."

### 8. Oracle, Form 10-Q for the quarter ended 31 August 2026 (filed 11 Sep 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm
Kind:        primary. Its own obligations, cash flow and liquidity claim.
Establishes: leases not yet commenced, negative free cash flow, equity raise, and the market's discount on its bonds.
Locators:    Note on leases p. 13; Note on fair value (senior notes); MD&A "Liquidity and Capital Resources" pp. 34–35 and its free cash flow table.
```

Paraphrase: "$288 billion of additional lease commitments, substantially all related to data center arrangements", expected to commence between Q2 fiscal 2027 and fiscal 2029, terms of 15 to 19 years, not on the balance sheet (p. 13). Quarter: operating cash flow $23,103 million (including $11.4 billion of customer prepayments), capital expenditures $28,499 million, free cash flow −$5,396 million (MD&A free cash flow table). It fully used a $20 billion at-the-market equity program for net proceeds of $19.9 billion (p. 34). Senior notes and other long-term borrowings of $125.0 billion had an estimated fair value of $105.7 billion at 31 August 2026 (fair value note). Unconditional purchase obligations total $34,150 million.

Rival position, own words (p. 35): "We believe that our current cash, cash equivalents and marketable securities balances, together with cash generated from operations and available financing arrangements, will be sufficient to meet our working capital, committed capital expenditures and contractual obligations for at least the next twelve months. Thereafter, we expect that our existing sources of liquidity, together with potential access to additional financing, will continue to be sufficient for the foreseeable future."

### 9. Alphabet, Form 10-Q for the quarter ended 30 September 2026 (filed 29 Oct 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm
Kind:        primary. Its own obligations.
Establishes: leases not yet commenced, and credit-derivative backstops of third parties' data center lease payments.
Locators:    Note 3 derivatives pp. 20–21; Note 4 leases p. 25; Note 5 VIEs p. 25–26.
```

Paraphrase: Leases not yet commenced, "primarily related to data centers and energy infrastructure", have future payments of $130.5 billion, commencing 2026–2031 (p. 25). Alphabet has agreed "to backstop specified payment obligations relating to data centers, including data center lease payments and the associated energy costs". It accounts for these as credit derivatives whose notionals "represent the maximum potential exposure regarding future payments in the event of specified default scenarios", with remaining terms up to 15 years. On default it may assume the leases (p. 20). Credit derivative notional: $16,940 million at 31 Dec 2025 and $48,012 million at 30 Sep 2026 (p. 21). The VIE note (p. 25) lists "certain leases and credit derivatives with data center entities" among the unconsolidated VIEs, plus $10.0 billion of potential data center and energy backstops for the Crux AI joint venture.

### 10. Amazon, Form 10-Q for the quarter ended 30 September 2026 (filed 30 Oct 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm
Kind:        primary. Its own commitments table.
Establishes: leases not yet commenced.
Locators:    Note 4 "Commitments and Contingencies", commitments table, p. 15.
```

Paraphrase: "Leases not yet commenced" total $164,922 million in the principal contractual commitments table. The same table lists long-term debt principal and interest of $294,254 million and total commitments of $883,581 million.

### 11. Nvidia, Form 10-Q for the quarter ended 26 July 2026 (filed 26 Aug 2026)

```text
URL:         https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm
Kind:        primary. GPU maker's own guarantees and supply commitments. It is the most recent Nvidia 10-Q on EDGAR as of 19 Nov 2026.
Establishes: a named guarantee chain (Nvidia → OpenAI leases → SB Energy campus), and supply commitments.
Locators:    Note 10 commitments p. 18; Note 14 guarantees p. 19; MD&A risk discussion.
```

Paraphrase: In August 2026 Nvidia entered into guarantees "capped at a total of $105 billion" to provide credit support on a land, power and shell buildout with affiliates of SB Energy Corp. "on behalf of a customer, an affiliate of OpenAI Group PBC". They cover leases for about 4.25 GW at the PORTS Technology Campus, Pike County, Ohio. Each guarantee becomes effective as its lease commences, from fiscal 2029, and pays "upon certain tenant defaults". The guarantees end if OpenAI achieves "a satisfactory credit rating". Other land, power and shell guarantees for AI clouds total $3.5 billion. Maximum gross exposure is $108.5 billion (p. 19). Supply and capacity commitments rose "from $119 billion last quarter to $279 billion as of July 26, 2026" (p. 18). The exhibit list includes "Form of Residual Value Guaranty" (Exhibit 10.1).

### 12. Stijn Van Nieuwerburgh, "Financing the AI Buildout", BPEA conference draft, 4 September 2026

```text
URL:         https://www.brookings.edu/wp-content/uploads/2026/09/4c_Van-Nieuwerburgh.pdf
Kind:        primary for his own estimates and analysis (Columbia Business School; Brookings Papers on Economic Activity, Fall 2026; conference 24–25 Sep 2026). Secondary for deal terms of the Meta Hyperion/Beignet financing (he cites S&P's pre-sale report), for Moody's and for the WSJ tallies. Barr's speech (fn 6) and the OCC SRP (fn 5) both cite him.
Establishes: firsthand: capex overtaking hyperscaler operating cash flow in 2026 on current estimates; his reading of the Hyperion structure. Repeats: S&P, Moody's and WSJ figures.
Locators:    abstract p. 1; pp. 7–10 (Figure 1 discussion; Hyperion case, Figure 2, footnotes 3–5); p. 11 footnote 6.
```

Paraphrase: Combined capex of Oracle, Microsoft, Amazon, Meta and Alphabet rose from about $97 billion in 2020 to more than $400 billion in 2025 and is projected above $800 billion in 2026. "On current estimates, capex will surpass the five firms' combined operating cash flow for the first time in 2026." Hyperion: the Beignet vehicle raised $27 billion of debt (October 2025, rated A+ by S&P) against about $30 billion of asset value, a debt-to-asset ratio of "about 90 percent", debt service coverage 1.12×, yield 6.58%, through bankruptcy-remote SPVs. Meta leases the campus in four-year terms from 2029 with a residual value guarantee. The rival point sits in his own footnote 3: "Meta's operating cash flow of $130 billion is at least 18× its 2026 debt service." He describes a $500 billion credit facility from Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR to finance Nvidia chips, with an Nvidia 25% residual value guarantee of up to $125 billion (fn 6). He gives no source, and I did not find the facility in the Nvidia 10-Q I read (dated 26 July 2026, before the facility's August date). Treat it as unverified.

### 13. Aldasoro, Doerr and Rees, "Financing the AI boom: from cash flows to debt", BIS Bulletin No 120, 7 January 2026

```text
URL:         https://www.bis.org/publ/bisbull120.htm  (PDF: https://www.bis.org/publications/bulletin-120-financing-ai-boom-cash-flows-debt.pdf)
Kind:        primary for the authors' own estimates; the views are the authors', "not necessarily ... the BIS". Cited by the OCC SRP fn 6.
Establishes: a moderate-risk judgment and private credit exposure estimates, as of January 2026.
Locators:    key takeaways, p. 1; private credit section and Graph 3, p. 4; "Implications for financial stability and growth", pp. 4–5.
```

Paraphrase: "While macroeconomic and financial stability risks from the AI boom appear moderate, the boom's sustainability hinges on AI firms meeting high earnings expectations" (p. 1). Private credit loans to AI-related firms grew from near zero to "over $200 billion", almost 8% of outstanding private credit loans, and could reach "$300–600 billion by 2030". Spreads on these loans are close to those on non-AI loans (6.2 vs 6.1 pp). For the average fund AI loans are "only about 5%" of volumes (p. 4). "some of the financing structures ... might mask leverage by moving it off the balance sheet. Yet leverage does not disappear by being out of sight" (p. 4).

## Contradictions

1. **Seven-firm debt: figure-derived $879 billion at 2026:Q2 against Barr's "expected to exceed $800 billion before year's end".** Figure C's 2026:Q2 "Debt" bar reads about $879 billion. Barr, speaking three days after the report, puts the same seven firms' on-balance-sheet debt below $800 billion. Neither the FSR text nor the figure notes state what "Debt" counts, so either Figure C includes items Barr's figure excludes (lease liabilities, for instance) or one of them is wrong. I could not resolve it. The writer should not print both as the same quantity. The safest wording is the Fed's text: obligations "have grown even more rapidly" than debt. Give the chart's debt bar as "read from the chart" if used at all.
2. **"$1.1 trillion outstanding" against the Figure C debt bar.** These are different scopes. The $1.1 trillion is public debt "related to advanced computing" across all issuers. Figure C counts seven named firms' debt. Do not compare the $2–3 trillion of commitments against $1.1 trillion as if they covered the same firms.
3. **Discounted against undiscounted.** The commission's finding needs a comparison of off-balance-sheet with on-balance-sheet amounts. The Fed (p. 24 fn 5) and Barr (fn 5) both say the comparison is not like for like. A ratio such as "3.5 times debt" is mine, not the Fed's. The CSV omits it for that reason. Lease payments run 15–30 years (Meta, Oracle filings), so the present value of the $1 trillion is materially lower. Nobody I read computes it.
4. **What the $2 trillion is.** The commission, Fortune and the FSR text all lead with "guarantees". The figure label is "Guarantees & contract commitments", and the text says "such as take-or-pay contracts and residual value guarantees". The identifiable credit guarantees in the filings I opened are Nvidia $108.5 billion (July 2026), Alphabet credit derivatives $48.0 billion (Sep 2026) and Meta's maximum RVG $41.5 billion (Sep 2026). Together they are about $198 billion. The identifiable purchase commitments are larger: Meta $454.5 billion non-cancelable (mostly cloud capacity) and Nvidia $279 billion supply and capacity. The guarantees that reach lenders are a minority of the $2 trillion on this evidence. The Fed does not publish the split (see Limits). Some purchase commitments may run between firms in the seven-firm set, such as Meta buying cloud capacity, and the Fed does not say whether it nets them.
5. **The Fed's own mitigating reading.** The box says the large firms "may absorb losses ... mitigating their effects on the rest of the financial system" (p. 25). Barr is "less concerned about direct losses" (speech p. 7). The OCC says bank credit is "typically senior ... and often secured" and is supported by low data center vacancy (SRP p. 3). BIS calls the risks "moderate" (January 2026). All four cut against a reading in which lenders are the main bearers of loss. The Fed and OCC still say the structures warrant "close monitoring".
6. **Survey shift is partly a relabelling.** AI went from 50% (spring, n=20) to 87% (fall, n=23). Category lists differ between rounds: "Risk asset/valuations correction" in spring, "Risk asset correction" in fall; "Oil shock" and "Basis trade" disappear; "Higher energy prices" and "Inflation expectations de-anchoring" appear. Respondent pools differ in size and the Fed does not say whether they overlap. Private credit fell from 50% to 22% while the Fed's own box puts private debt vehicles in the chain. Box 5.1 is contacts' opinion, explicitly not the Board's view.
7. **May and November issuance sentences.** May (p. 9): issuance "among the largest investment-grade firms involved in cloud computing neared $100 billion in the first quarter". November (p. 9): "the largest investment-grade firms involved in operating data centers was greater than $150 billion year to date". Read together, these firms' bond issuance slowed after Q1, while Figure A shows total advanced computing issuance at $684 billion for January–October. The likely reading is the box's own: the growth moved to loans, non-USD bonds, project finance and securitization. The two sentences use different firm definitions, so the slowdown inference is soft.
8. **Lease totals across sources.** Figure C shows about $534 billion of leases yet to start for 2025 and about $1,019 billion for 2026:Q2, across seven firms. Moody's, as reported by Van Nieuwerburgh, put hyperscalers' future leases not yet on balance sheet at about $660 billion. Fortune's February coverage puts the figure at $662 billion at end-2025. The latest 10-Qs give $1,304 billion for five hyperscalers: Meta 355.73, Microsoft 364.6, Oracle 288 (31 Aug), Alphabet 130.5, Amazon 164.9. The gaps are consistent with different dates and the Fed using fiscal-year filings for 2025 (Microsoft June, Oracle May), but I did not confirm the Fed's dating convention. The 10-Q sum shows the leases figure grew by roughly $285 billion between the Fed's Q2 cut-off and the Q3 filings. Different firm sets and dates make this approximate.

## Numbers

```text
Figure: more than $680 billion (figure-derived 2026 bar: $684 billion)
Owner:  Fed FSR Nov 2026, Box 2.2 p. 23 and figure A; notes p. 55
Scope:  advanced computing–related debt issuance, January–October 2026; public deals plus rule 144A, excludes section 4(a)(2) private placements

Figure: $130 billion (figure-derived 2023 bar: $133 billion)
Owner:  Fed FSR Nov 2026, Box 2.2 p. 23
Scope:  same measure, calendar 2023; "about a fivefold increase"

Figure: under 6 percent (2023) to about 31 percent (2026)
Owner:  Fed FSR Nov 2026, Box 2.2 p. 23
Scope:  advanced computing borrowing as a share of nonfinancial investment-grade corporate debt issuance

Figure: more than $1.1 trillion
Owner:  Fed FSR Nov 2026, Box 2.2 p. 23
Scope:  outstanding public debt related to advanced computing, as of October 2026; excludes private credit, which the Fed says it cannot fully measure

Figure: more than $1 trillion (figure-derived 2026:Q2: $1,019 billion)
Owner:  Fed FSR Nov 2026, Box 2.2 p. 24 and figure C
Scope:  undiscounted not-yet-commenced leases, seven firms (Amazon, Alphabet, Broadcom, Meta, Microsoft, Nvidia, Oracle), 2026:Q2

Figure: more than $2 trillion (figure-derived 2026:Q2: $2,068 billion)
Owner:  Fed FSR Nov 2026, Box 2.2 p. 24 and figure C
Scope:  undiscounted "guarantees & contract commitments" (text: "such as take-or-pay contracts and residual value guarantees"), same seven firms, 2026:Q2

Figure: more than $3 trillion
Owner:  Barr speech 16 Nov 2026 p. 5, attributing it to the FSR ("potential maximum nominal value")
Scope:  sum of the two undiscounted categories; the FSR text itself prints only the two parts

Figure: about $879 billion (figure-derived; disputed, see Contradiction 1)
Owner:  Fed FSR Nov 2026, figure C "Debt" bar
Scope:  seven firms, 2026:Q2

Figure: "expected to exceed $800 billion before year's end"
Owner:  Barr speech p. 4
Scope:  on-balance-sheet debt of "the seven largest AI firms", 2026

Figure: close to $1 trillion
Owner:  Fed FSR Nov 2026, Box 2.2 p. 25
Scope:  largest U.S. bank holding companies' exposure to large technology firms, data center developers, advanced computing SPEs and private credit vehicles, AND utility companies; no date stated beyond the report's; not data-center-only

Figure: 87 percent (fall 2026, 20 of 23) against 50 percent (spring 2026, 10 of 20)
Owner:  Fed FSR Nov 2026, Box 5.1 figures A and B (figure-derived); spring value confirmed by May 2026 chart descriptions
Scope:  share of NY Fed survey respondents citing AI among most-cited shocks over the next 12–18 months

Figure: 30 percent (fall 2025)
Owner:  Fed May 2026 chart descriptions, Box 5.1 figure B ("about 30 percent")
Scope:  same question, 23 contacts, Sep–Oct 2025

Figure: $355.73 bn / $364.6 bn / $288 bn / $130.5 bn / $164.9 bn
Owner:  Meta, Microsoft, Oracle, Alphabet, Amazon 10-Qs (pp. 21 / 22 / 13 / 25 / 15)
Scope:  leases not yet commenced, undiscounted, at 30 Sep 2026 (Oracle 31 Aug 2026); sum about $1,304 bn

Figure: $41.49 bn (Dec 2025: $28.09 bn)
Owner:  Meta 10-Q p. 18
Scope:  maximum residual value guarantees to two unconsolidated data center ventures

Figure: $48.01 bn (Dec 2025: $16.94 bn)
Owner:  Alphabet 10-Q p. 21
Scope:  notional of credit derivatives backstopping third-party data center lease and energy payments

Figure: $105 bn cap; $108.5 bn total maximum gross exposure
Owner:  Nvidia 10-Q p. 19
Scope:  guarantees for OpenAI-affiliate leases at SB Energy campus (effective from FY2029 as leases commence) plus $3.5 bn other AI cloud lease guarantees, at 26 Jul 2026

Figure: $454.52 bn
Owner:  Meta 10-Q p. 21
Scope:  non-cancelable contractual commitments, mostly third-party cloud capacity, servers and network, energy, at 30 Sep 2026

Figure: $279 bn (prior quarter $119 bn)
Owner:  Nvidia 10-Q p. 18
Scope:  supply and capacity commitments at 26 Jul 2026

Figure: $96.87 bn operating cash flow; $85.82 bn capex incl. finance lease principal
Owner:  Meta 10-Q pp. 48–49
Scope:  nine months to 30 Sep 2026

Figure: $58.0 bn cash from operations; $39.4 bn additions to property and equipment
Owner:  Microsoft 10-Q cash flow statement
Scope:  quarter to 30 Sep 2026 (Q1 FY2027)

Figure: $23.1 bn operating cash flow; $28.5 bn capex; free cash flow −$5.4 bn
Owner:  Oracle 10-Q MD&A free cash flow table
Scope:  quarter to 31 Aug 2026 (Q1 FY2027); OCF includes $11.4 bn customer prepayments

Figure: $125.0 bn face; $105.7 bn estimated fair value
Owner:  Oracle 10-Q fair value note
Scope:  senior notes and other long-term borrowings at 31 Aug 2026 (Level 2)
```

Series for charts, all in this directory:

- `fig-a-issuance.csv`: Figure A by instrument and year, $ billions, figure-derived. 2022 = Nov–Dec only, 2026 = Jan–Oct. Totals: 23.0, 133.4, 201.4, 411.1, 684.4. 2026 composition: investment-grade corporate bonds 283.4, corporate loans 108.5, non-USD corporate 106.8, securitization 60.6, investment-grade project finance 45.6, high-yield project finance 41.8, high-yield corporate bonds 19.2, other not rated 18.5. Project finance first appears in 2025.
- `fig-c-obligations.csv`: Figure C, seven firms, $ billions, figure-derived:

| Period | Debt | Leases yet to start | Guarantees & contract commitments |
|---|---|---|---|
| 2020 | 346 | 47 | 80 |
| 2021 | 393 | 55 | 138 |
| 2022 | 447 | 58 | 173 |
| 2023 | 517 | 93 | 217 |
| 2024 | 502 | 231 | 306 |
| 2025 | 663 | 534 | 637 |
| 2026:Q2 | 879 | 1,019 | 2,068 |

  Debt bars are discounted; the other two are undiscounted (Fed fn 5). If charted, the caption must say so. Leases and guarantees each roughly doubled or tripled between 2025 and 2026:Q2.
- `box51-survey.csv`: every bar of both survey rounds with percent and implied respondent count.
- `lease-commitments-10q.csv`: the 10-Q figures above, with pages.

## Limits

- No Fed-published data table exists for the November 2026 FSR as of 19 November. Every series is read from the chart geometry and must be captioned that way. Exact Fed values for Figures A, B and C are not available.
- The Fed does not split the "more than $2 trillion" into guarantees, take-or-pay contracts and other purchase commitments. It does not say whether it nets commitments between firms inside the seven-firm set. The article cannot state how much of the $2 trillion is credit support to lenders.
- The Fed gives no amount for any link of the chain except the large bank holding companies' "close to $1 trillion", which also covers big tech firms generally and utilities. There are no Fed figures for SPE debt outstanding, for the share of subordinated tranches held by life insurers or BDCs, or for private credit to the buildout. BIS's "over $200 billion" of private credit to AI-related firms (January 2026, PitchBook-defined AI, big data and cloud verticals) is the only sized private credit figure I found, and it predates the report.
- The Fed says it cannot measure outstanding advanced computing debt exactly because of private credit, and its issuance count excludes section 4(a)(2) private placements.
- No source I found discounts the commitments to present value, so the on-balance against off-balance comparison stays nominal.
- The conflict between Figure C's debt bar and Barr's "$800 billion" is unresolved (Contradiction 1).
- OCC gives no dollar amounts for bank lending to data centers.
- An analyst arguing serviceability "in their own words": I found the companies' own statements (Meta, Microsoft, Oracle), Van Nieuwerburgh's "at least 18×" debt-service footnote, and the BIS "moderate" judgment. Moody's view that the hyperscalers are not overleveraged reached me only through secondary coverage. The Moody's report is not public, so it cannot be cited as a primary source.
- Broadcom's filings were not opened. Nvidia's latest 10-Q predates the report's data cut-off by three months.

## Source assets

```text
Asset: Box 2.2 figure C "Debt and other obligations", Fed FSR Nov 2026 p. 24 (PDF page 32)
Shows: the leases and guarantees bars overtaking the debt bar after 2023, and the 2026:Q2 jump
Crop:  must retain the legend, the y-axis "Billions of dollars", the 2026:Q2 label and the source line; the caption must carry the Fed's fn 5 undiscounted caveat

Asset: Box 2.2 figure A "Debt issuance for advanced computing infrastructure", p. 23 (PDF 31)
Shows: issuance by instrument 2022–2026; project finance appearing from 2025
Crop:  retain the full eight-item legend and axis; caption must state 2022 = Nov–Dec and 2026 = Jan–Oct (figure notes p. 55)

Asset: Box 2.2 figure B "Investment and debt issue cycle comparison", p. 24 (PDF 32)
Shows: hyperscaler cumulative capex and debt issuance (share of GDP) against the 1995 telecom cycle
Crop:  retain legend and the year-0 definition from the notes; outside the commission's chosen visuals, so optional

Asset: Box 5.1 figures A and B, p. 50 (PDF 58)
Shows: AI first among fall shocks at 87%, against third in spring at 50%
Crop:  keep both panels and both source lines (n=23 and n=20); category lists differ, so a crop must not imply matched categories

Asset: Van Nieuwerburgh Figure 2 "Structure of the Hyperion (Beignet) Data Center Financing", BPEA draft p. 9
Shows: the SPV chain Meta (Iris Crossing) / Blue Owl (Beignet Investor) → Project Beignet Holdings → Laidley LLC, with the Entergy power agreement
Crop:  retain the author's notes line naming S&P's pre-sale report and Entergy's 10-K as sources. It is a third-party drawing, so a drawn diagram for the article may be the better route.

Meta, Microsoft, Oracle, Alphabet, Amazon and Nvidia 10-Qs: None found. The values are in text and tables, better re-set than cropped.
OCC SRP Fall 2026: None found for this topic.
Barr speech, BIS Bulletin 120: None found that carries the argument better than the Fed's own figures.
```

## Discarded

```text
https://fortune.com/2026/11/17/fed-financial-stability-report-ai-data-center-3-trillion-off-balance-sheet-nvidia/: secondary coverage (Nick Lichtenberg); every figure traces to the FSR or the Barr speech, both read directly. It led me to the Barr speech.
https://www.federalreserve.gov/publications/financial-stability-report.htm: read only to confirm no November 2026 chart-data page; not a content source.
https://www.occ.gov/publications-and-resources/publications/semiannual-risk-perspective/files/semiannual-risk-perspective-fall-2026.html: the address search returned. It serves a generic OCC page, not the report.
Search-result summaries only, not opened, and not citable: fourweekmba.com, en.spaziocrypto.com, aiweekly.co, metirai.com, americanbanker.com, nationthailand.com (FSR coverage); dc.fortune.com and allwork.space (Moody's $662 bn, February 2026; mentioned in Contradiction 8 only as a pointer to the Moody's figure, which Van Nieuwerburgh also reports); advisorperspectives.com (Nikkei estimate); thenextweb.com (Google guarantees). The Google item is superseded by Alphabet's own 10-Q.
```

## Appendix: chart data files (inlined by the orchestrator)

The researcher recorded these as CSV files beside this record; they are inlined here verbatim because the artifact pair holds only brief.md and evidence.md. References above to a .csv file name the section below.

### box51-survey.csv

```csv
survey,fieldwork,respondents,label,percent_of_respondents,implied_respondents
Fall 2026,Sep-Oct 2026,23,"Artificial intelligence",87.0,20
Fall 2026,Sep-Oct 2026,23,"Risk asset correction",52.0,12
Fall 2026,Sep-Oct 2026,23,"Higher long-term rates",48.0,11
Fall 2026,Sep-Oct 2026,23,"Cyberattacks",43.0,10
Fall 2026,Sep-Oct 2026,23,"Fiscal debt sustainability",43.0,10
Fall 2026,Sep-Oct 2026,23,"Higher energy prices",39.0,9
Fall 2026,Sep-Oct 2026,23,"Persistent inflation",35.0,8
Fall 2026,Sep-Oct 2026,23,"Geopolitical risks",30.0,7
Fall 2026,Sep-Oct 2026,23,"Private credit",22.0,5
Fall 2026,Sep-Oct 2026,23,"Inflation expectations de-anchoring",13.0,3
Fall 2026,Sep-Oct 2026,23,"Policy uncertainty",13.0,3
Spring 2026,Mar-Apr 2026,20,"Geopolitical risks",75.0,15
Spring 2026,Mar-Apr 2026,20,"Oil shock",70.0,14
Spring 2026,Mar-Apr 2026,20,"Artificial intelligence",50.0,10
Spring 2026,Mar-Apr 2026,20,"Private credit",50.0,10
Spring 2026,Mar-Apr 2026,20,"Persistent inflation; monetary tightening",45.0,9
Spring 2026,Mar-Apr 2026,20,"Risk asset/valuations correction",35.0,7
Spring 2026,Mar-Apr 2026,20,"Fiscal debt sustainability",30.0,6
Spring 2026,Mar-Apr 2026,20,"Policy uncertainty",20.0,4
Spring 2026,Mar-Apr 2026,20,"Cyberattacks",20.0,4
Spring 2026,Mar-Apr 2026,20,"Higher long-term rates",20.0,4
Spring 2026,Mar-Apr 2026,20,"Market liquidity strains and volatility",15.0,3
Spring 2026,Mar-Apr 2026,20,"Labor market weakness",10.0,2
Spring 2026,Mar-Apr 2026,20,"Basis trade",10.0,2
```

### fig-a-issuance.csv

```csv
period,"Securitization","High-yield corporate bonds","Investment-grade corporate bonds","Corporate loans","Corporate, non-USD","Corporate, other (not rated)","High-yield project finance","Investment-grade project finance",total
"2022 (Nov-Dec only)",2.5,0.0,18.9,0.5,1.1,0.0,0.0,0.0,23.0
"2023",18.5,3.1,62.0,20.0,29.1,0.6,0.0,0.0,133.4
"2024",35.7,1.9,100.8,34.4,25.0,3.5,0.0,0.0,201.4
"2025",57.0,8.7,179.6,56.1,55.9,15.9,10.6,27.3,411.1
"2026 (Jan-Oct)",60.6,19.2,283.4,108.5,106.8,18.5,41.8,45.6,684.4
```

### fig-c-obligations.csv

```csv
period,debt,leases_yet_to_start,guarantees_and_contract_commitments,off_balance_sheet_total
2020,346,47,80,126
2021,393,55,138,193
2022,447,58,173,231
2023,517,93,217,310
2024,502,231,306,537
2025,663,534,637,1171
2026:Q2,879,1019,2068,3087
```

### lease-commitments-10q.csv

```csv
company,filing,period_end,leases_not_yet_commenced_usd_bn,commencement_window,other_offbalance_item,other_item_usd_bn,filing_page
Meta Platforms,Form 10-Q,2026-09-30,355.73,"remainder of 2026 through 2036","non-cancelable contractual commitments (mostly third-party cloud capacity, servers and network, energy)",454.52,21
Meta Platforms,Form 10-Q,2026-09-30,,,"maximum residual value guarantees to Louisiana and Texas data center ventures",41.49,18
Microsoft,Form 10-Q,2026-09-30,364.6,"fiscal 2027 through fiscal 2034",,,22
Oracle,Form 10-Q,2026-08-31,288,"Q2 fiscal 2027 through fiscal 2029",,,13
Alphabet,Form 10-Q,2026-09-30,130.5,"2026 through 2031","credit derivatives backstopping third-party data center lease and energy payments (notional)",48.01,"25 (leases); 21 (derivatives)"
Amazon,Form 10-Q,2026-09-30,164.922,"payments scheduled Q4 2026 through after 2030 (commencement dates not stated)",,,15
Nvidia,Form 10-Q,2026-07-26,,,"maximum gross exposure under data center lease guarantees incl. SB Energy/OpenAI (capped $105bn)",108.5,19
```
