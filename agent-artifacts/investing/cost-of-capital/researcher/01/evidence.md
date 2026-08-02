# Evidence: investing/cost-of-capital (01)

The evidence supports every number the brief asks for: a current 10-year Treasury
yield, a dated Damodaran implied equity risk premium, Costco's operating income
and invested capital (fresh from its FY2025 10-K, since no prior `return-on-capital`
article exists in this environment to reuse — `nb history --series investing` and
`nb history return-on-capital` both return "No matching published coverage," so I
sourced Costco directly from primary filings rather than reconstructing a prior
lesson), and AEP's operating income, invested capital, and regulator-authorized
ROE by jurisdiction, the last confirmed against AEP's own investor-relations rate
tables (two dated snapshots) rather than a single summary. The concept definitions
(cost of capital, WACC, cost of debt/equity, the ROIC-vs-hurdle rule, and the
growth-amplification effect) are all grounded in two Aswath Damodaran papers with
exact quoted passages and locators.

It is thin in one place: a full-text, sentence-level quote from a state
commission's actual order setting AEP's authorized ROE (as opposed to AEP's own
disclosure of that authorized ROE) was not obtained inside the research budget for
this pass — see Contradictions and Discarded. The brief explicitly allows AEP's
own disclosed authorized ROEs as sufficient ("or AEP's disclosed authorized
ROEs"), and I obtained two independently dated company snapshots (as of
12/31/2024 and 3/31/2025) that agree with each other and with the SEC 10-Q's
docket references, so the number is verified, just not from the commission order
text itself. A specific secondary claim (a February 2026 West Virginia PSC order
reaffirming 9.75% ROE with a $15 million rate increase) could not be verified
against primary text and is recorded as discarded, not as fact.

It is also thin on one nuance the writer must handle carefully: AEP's
return-on-invested-capital (computed the same way as Costco's, on total debt +
equity) is not on the same basis as AEP's authorized return on equity (which
applies only to the equity slice of a state-specific rate base). Both are
reported below, with the basis mismatch flagged, plus AEP's own
like-for-like "operating earned ROE vs. approved ROE" by jurisdiction, which is
the cleaner apples-to-apples comparison.

## Sources

### S1. Aswath Damodaran, "The Cost of Capital: The Swiss Army Knife of Finance" (April 2016)
- **URL:** https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/costofcapital.pdf (verified resolving, HTTP 200)
- **Classification:** Authoritative secondary. Damodaran (NYU Stern finance professor)
  did not originate the cost-of-capital concept, but this paper codifies the
  accepted mechanics, terminology, and cautions used across corporate finance and
  valuation practice; it is the kind of standard, citable synthesis the brief asks
  for in place of a textbook chapter.
- **Establishes:** The definition of cost of capital as opportunity cost, discount
  rate, and hurdle rate simultaneously; the WACC formula and its weighting; cost
  of debt and cost of equity components; the market-vs-book-value weighting
  debate; the "no risk subsidies" critique of using one company-wide WACC for
  businesses of different risk; empirical evidence that growth more often
  destroys value than creates it.
- **Verbatim passages:**
  - "The cost of capital, in its most basic form, is a weighted average of the
    costs of raising funding for an investment or a business, with that funding
    taking the form of either debt or equity. The cost of equity will reflect the
    risk that equity investors see in the investment and the cost of debt will
    reflect the default risk that lenders perceive from that same investment. The
    weights on each component will reflect how much of each source will be used
    in financing the investment." (p.2, "The Mechanics")
  - Figure 1 (p.2): Cost of Capital = (Cost of Equity × Weight of equity) + (Cost
    of Debt × Weight of Debt); Cost of Equity = Risk free Rate + Risk Premium;
    Cost of Debt = [Risk free Rate + Default Spread] × (1 − tax rate).
  - "If you make it through the mechanics of computing cost of capital, you will
    see it described as an opportunity cost, a discount rate and a hurdle rate
    for investments and it is all of the above depending upon where it is being
    used and by whom." (p.2)
  - "In the corporate finance world, it is the cost of capital that is the
    benchmark that has to be beaten for an investment to be categorized as a good
    investment... Accounting Test: Return on invested capital (ROIC) > Cost of
    Capital." (p.3–4, Figure 3)
  - "The first is when a company insists on using its cost of capital on all
    investments, even if these investments are in different businesses and have
    different risk profiles. That will lead to safe businesses subsidizing risky
    businesses within the company." (p.4, "No risk subsidies")
  - "At the start of 2016... I assessed the returns on capital and costs of
    capital of more than 40,000 publicly traded companies globally and came to
    the conclusion that more than half of them generated returns on their
    investments that, at least in the aggregate, were lower than the costs of
    capital of these companies... Put simply, growth, across the globe, is more
    likely to destroy value than to add it, in a company." (p.5–6, Figure 5,
    "Dividend Policy")
  - Table 1 (p.11), Historical Equity Risk Premium – US 1928–2015: Arithmetic
    average, Stocks minus T.Bonds = 6.18% (1928–2015), 3.89% (1966–2015), 3.88%
    (2006–2015); Geometric average, Stocks minus T.Bonds = 4.54%, 2.90%, 2.53%
    respectively — illustrates how much the "historical" ERP moves with window
    and averaging choice.
  - "On this one, there can be no straddling the fence. Book value weights are
    not only irrelevant when it comes to cost of capital but come with problems
    that can be insurmountable. For instance, about 10% of all US companies at
    the end of 2015 had negative book values of equity... unless you are willing
    to weight debt more than 100% and give equity a negative weight, the cost of
    capital becomes impossible to estimate." (p.25, "Market versus Book Value")
  - Figure 16 (p.27): distribution of cost of capital across ~8,000 US companies,
    January 2016 — 10th percentile 5.23%, 25th 6.60%, median 8.00%, 75th 9.20%,
    90th 10.00%.
- **Locators:** Page numbers are the paper's own internal pagination (PDF is
  unpaginated by section headers; cited pages above are approximate reading
  order, all within the paper's ~28-page body — "The Mechanics," "Role in
  Corporate Finance," "Debt: Its cost and weight," "Lessons").

### S2. Aswath Damodaran, "Return on Capital (ROC), Return on Invested Capital (ROIC) and Return on Equity (ROE): Measurement and Implications" (July 2007)
- **URL:** https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf (verified resolving, HTTP 200)
- **Classification:** Authoritative secondary, same reasoning as S1 — a standard,
  widely cited Damodaran paper that codifies how ROIC is measured and why it is
  compared to the cost of capital.
- **Establishes:** The exact ROIC formula and its four defining choices (operating
  income vs. net income, tax adjustment, book value, timing); the value-creation
  rule stated as an "excess returns" framework; the explicit statement that
  growth amplifies value creation when returns exceed the cost of capital and
  amplifies value destruction when they do not; the terminal-value proof that
  growth is neutral to value exactly when ROIC equals the cost of capital.
- **Verbatim passages:**
  - "In effect, this is what we are trying to do when we compute the return on
    invested capital and compare it to the cost of capital." (p.4)
  - "A firm that generates higher returns on an investment than it costs it to
    raise capital for that investment is earning excess returns and will trade
    at a premium over a firm that does not earn excess returns... A firm that
    expects to continue generating positive excess returns on new investments in
    the future will see its value increase as growth increases, whereas a firm
    that earns returns that do match up to its cost of funding will destroy
    value as it grows." (p.5)
  - "Return on Capital (ROIC) = Operating Income_t (1 − tax rate) / Book Value of
    Invested Capital_{t−1}." (p.7) — with the four components explained: after-tax
    operating income in the numerator, book (not market) value of invested
    capital in the denominator, and a one-period lag between the capital base and
    the income it is compared to.
  - "It relates the earnings left over for equity investors after debt service
    costs have been factored in to the equity invested in the asset." (p.11,
    defining Return on Equity relative to Return on Capital) — the textual basis
    for "equity is paid after debt."
  - "If the return on capital is equal to the cost of capital, increasing the
    stable growth rate will have no effect on value... Assuming that a firm will
    earn returns that are higher than costs in perpetuity will make the terminal
    value an increasing function of growth, whereas assuming negative excess
    returns will make the terminal value a decreasing function of growth."
    (p.61, "Forever," with the algebraic proof and Figure 10 showing three growth
    curves: ROC > WACC increasing value with growth, ROC = WACC flat, ROC < WACC
    decreasing value with growth.)
  - Table 11 (pp.66–69): sector-level ROC, non-cash ROE, and ROE for the US
    market in 2007 — market-wide average ROC 17.05%, useful only as historical
    texture, not as a current number.
- **Locators:** PDF page numbers as printed on each page (1–69, including tables).

### S3. Aswath Damodaran, "The Price of Risk: An Equity Risk Premium Monologue!" (Musings on Markets, March 2026)
- **URL:** https://aswathdamodaran.blogspot.com/2026/03/the-price-of-risk-equity-risk-premium.html (verified resolving, HTTP 200)
- **Classification:** Primary for the specific ERP figure — Damodaran is the
  author and originator of this implied-ERP estimate; he computes it himself from
  market prices and expected cash flows and publishes it under his own name. It
  is not a report about someone else's number.
- **Establishes:** The current, dated, forward-looking US equity risk premium.
- **Verbatim passage:** "Using this approach, the equity risk premium at the
  start of 2026 was 4.23% (over the US treasury bond rate)." Confirmed by direct
  text search of the raw page content (not a model paraphrase).
- **Locator:** Mid-post, in the section describing the implied-premium
  methodology and its January-2026 reading.

### S4. US Department of the Treasury, Daily Treasury Par Yield Curve Rates (2026)
- **URLs:**
  - CSV: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv (verified resolving; downloaded directly and inspected raw rows)
  - Human-readable: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202607 (verified resolving, HTTP 200)
- **Classification:** Primary. The Treasury is the issuer of these securities and
  the direct source of the par yield curve; this is not a restatement.
- **Establishes:** The risk-free rate.
- **Exact reading:** Row dated 07/31/2026 (the most recent trading day in the
  file; today is 2026-08-02, a Sunday): 10 Yr = 4.75%, 2 Yr = 4.28%, 30 Yr =
  5.27%. Confirmed by downloading the raw CSV and reading the header and final
  data row directly (not summarized).
- **Locator:** CSV header row: `Date,"1 Mo","1.5 Month","2 Mo","3 Mo","4
  Mo","6 Mo","1 Yr","2 Yr","3 Yr","5 Yr","7 Yr","10 Yr","20 Yr","30 Yr"`; first
  data row: `07/31/2026,3.78,3.80,3.85,3.83,3.92,3.98,4.08,4.28,4.34,4.45,4.59,4.75,5.28,5.27`.

### S5. Costco Wholesale Corp, Form 10-K for fiscal year ended August 31, 2025
- **URL:** https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm (verified resolving, HTTP 200; filed 2025-10-08, accession 0000909832-25-000101)
- **Classification:** Primary. Costco's own audited annual report, filed with the SEC.
- **Establishes:** Operating income, effective tax rate, total assets, current
  liabilities, cash, short-term investments, long-term debt, and stockholders'
  equity for FY2025 (ended 8/31/2025) and FY2024 (ended 9/1/2024) — the inputs
  needed to compute ROIC.
- **Verbatim passages (from the document's own text, downloaded and parsed
  directly, not summarized):**
  - Consolidated Statements of Income (p.37 per the filing's internal page
    numbering): "OPERATING EXPENSES ... Operating income 10,383 9,285 8,114 ...
    INCOME BEFORE INCOME TAXES 10,818 9,740 8,487 Provision for income taxes
    2,719 2,373 2,195 NET INCOME $ 8,099 $ 7,367 $ 6,292" — columns are FY2025,
    FY2024, FY2023 respectively, dollars in millions.
  - MD&A: "The effective tax rate in 2025 was 25.1%, compared to 24.4% in 2024."
  - Provision for Income Taxes note: "Provision for income taxes $ 2,719 $ 2,373
    $ 2,195 Effective tax rate 25.1% 24.4% 25.9%" (FY2025, FY2024, FY2023).
  - Consolidated Balance Sheets (p.39): "Cash and cash equivalents $ 14,161 $
    9,906 ... Short-term investments 1,123 1,238 ... Total current liabilities
    37,108 35,464 ... Long-term debt, excluding current portion 5,713 5,794 ...
    TOTAL EQUITY 29,164 23,622 ... TOTAL ASSETS $ 77,099 $ 69,831" — first
    column FY2025 (8/31/2025), second FY2024 (9/1/2024), dollars in millions.
- **Locators:** Item 8, Consolidated Statements of Income (internal page 37) and
  Consolidated Balance Sheets (internal page 39); Provision for Income Taxes note
  in the same section.

### S6. SEC EDGAR XBRL Company Facts API — Costco Wholesale Corp (CIK 0000909832)
- **URLs (all verified resolving, HTTP 200):**
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0000909832/us-gaap/OperatingIncomeLoss.json
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0000909832/us-gaap/Assets.json
  - (and the equivalent companyconcept endpoints for LiabilitiesCurrent, CashAndCashEquivalentsAtCarryingValue, ShortTermInvestments, LongTermDebtNoncurrent, LongTermDebtCurrent, StockholdersEquity, NetIncomeLoss, Liabilities, IncomeTaxExpenseBenefit)
- **Classification:** Primary. This is SEC-hosted, machine-readable structured
  data extracted directly from Costco's own XBRL-tagged 10-K filing (same
  accession number, 0000909832-25-000101) — not a third party's summary.
- **Establishes:** Cross-verification of every figure pulled from S5's prose,
  plus the one figure not visible on the balance sheet face: current portion of
  long-term debt, tagged `LongTermDebtCurrent` = $75M (FY2025) and $103M
  (FY2024), folded into "Other current liabilities" on the face statement.
- **Exact readings used (all in USD, all matched exactly against S5):**
  FY2025 operating income $10,383,000,000; FY2024 $9,285,000,000. FY2025 total
  assets $77,099,000,000; FY2024 $69,831,000,000. FY2025 current liabilities
  $37,108,000,000; FY2024 $35,464,000,000. FY2025 cash $14,161,000,000; FY2024
  $9,906,000,000. FY2025 short-term investments $1,123,000,000; FY2024
  $1,238,000,000. FY2025 long-term debt (noncurrent) $5,713,000,000; FY2024
  $5,794,000,000. FY2025 long-term debt (current portion) $75,000,000; FY2024
  $103,000,000. FY2025 stockholders' equity $29,164,000,000; FY2024
  $23,622,000,000.
- **Locator:** JSON `units.USD` array, entries with `form: "10-K"` and `end`
  dates `2025-08-31` / `2024-09-01`.

### S7. American Electric Power Co Inc, Form 10-K for fiscal year ended December 31, 2025
- **URL:** https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/aep-20251231.htm (verified resolving, HTTP 200; filed 2026-02-12, accession 0000004904-26-000013)
- **Classification:** Primary. AEP's own audited annual report, filed with the SEC.
- **Establishes:** Operating income, income-tax reconciliation (including why the
  effective tax rate is far below the statutory rate), and balance-sheet inputs
  for AEP's ROIC, plus actual 2025 long-term-debt issuance rates usable as a real
  cost-of-debt anchor.
- **Verbatim passages (downloaded and parsed directly from the filed document):**
  - Consolidated Statements of Income: "TOTAL EXPENSES 16,557 15,417 15,426
    OPERATING INCOME 5,319 4,304 3,556 ... INCOME BEFORE INCOME TAX EXPENSE
    (BENEFIT) AND EQUITY EARNINGS 3,724 2,843 2,209 Income Tax Expense (Benefit)
    129 (39) 55 Equity Earnings of Unconsolidated Subsidiaries 101 94 59 NET
    INCOME 3,696 2,976 2,213 ... EARNINGS ATTRIBUTABLE TO AEP COMMON
    SHAREHOLDERS $ 3,580 $ 2,967 $ 2,208" — columns FY2025, FY2024, FY2023,
    dollars in millions.
  - Income tax reconciliation note: "Net Income $ 3,696 $ 2,976 $ 2,213 Income
    Tax Expense (Benefit) 129 (39) 55 Pretax Income $ 3,825 $ 2,937 $ 2,268 ...
    U.S. Federal Statutory Tax Rate $ 803 21.0% $ 617 21.0% $ 476 21.0% ... Tax
    Credits: Production Tax Credits (244) (6.4)% (214) (7.3)% (175) (7.7)% ..."
    (FY2025, FY2024, FY2023) — the effective rate lands far under 21% because of
    production tax credits from AEP's wind and solar assets, not because of debt
    tax shields.
  - MD&A, "Debt" bullet: "During 2025, AEP issued approximately $8.3 billion of
    long-term debt, including $3 billion of junior subordinated notes at
    interest rates ranging from 5.80% to 6.05%... $2.1 billion of senior
    unsecured notes at interest rates ranging from 5.38% to 5.85%, $478 million
    of securitization bonds at an interest rate of 5.30%, $320 million of
    pollution control bonds at interest rates ranging from 3.30% to 3.70%..."
  - MD&A, short-term debt table footnote: "Securitized Debt for Receivables, for
    the year ended 2025, had a weighted-average interest rate of 4.46% ... The
    commercial paper program, for the year ended 2025, had a weighted-average
    yield of 4.47%..."
- **Locators:** Consolidated Statements of Income (early in Item 8); "Income
  Taxes" note (Note on income taxes, later in Item 8, reconciliation table);
  MD&A "Liquidity and Capital Resources" section, "Debt" bullet list.

### S8. SEC EDGAR XBRL Company Facts API — American Electric Power Co Inc (CIK 0000004904)
- **URLs (all verified resolving, HTTP 200):**
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0000004904/us-gaap/OperatingIncomeLoss.json
  - https://data.sec.gov/api/xbrl/companyconcept/CIK0000004904/us-gaap/Assets.json
  - (and the equivalent endpoints for LiabilitiesCurrent, CashAndCashEquivalentsAtCarryingValue, LongTermDebtNoncurrent, LongTermDebtCurrent, StockholdersEquity, IncomeTaxExpenseBenefit, ProfitLoss, Liabilities)
- **Classification:** Primary, same reasoning as S6 — SEC-hosted structured data
  from AEP's own XBRL-tagged 10-K (accession 0000004904-26-000013).
- **Exact readings used (USD):** FY2025 operating income $5,319,000,000; FY2024
  $4,303,600,000 (rounds to $4,304M on the face statement). FY2025 total assets
  $114,460,000,000; FY2024 $103,078,000,000. FY2025 current liabilities
  $13,314,000,000; FY2024 $13,009,300,000. FY2025 cash $197,000,000; FY2024
  $202,900,000. FY2025 long-term debt (noncurrent) $44,128,000,000; FY2024
  $39,307,800,000. FY2025 long-term debt (current) $3,194,000,000; FY2024
  $3,335,000,000. FY2025 stockholders' equity $31,138,000,000; FY2024
  $26,943,800,000.
- **Locator:** JSON `units.USD` array, entries with `form: "10-K"` and `end`
  dates `2025-12-31` / `2024-12-31`.

### S9. American Electric Power, "Rate Base and ROE's" investor document, as of 12/31/2024
- **URL:** https://docs.aep.com/docs/investors/RateBaseandROE.pdf (verified resolving, HTTP 200)
- **Classification:** Primary. AEP's own investor-relations disclosure of the
  return on equity each of its regulated jurisdictions is authorized to earn and
  what it actually earned, sourced from AEP's own regulatory and accounting
  records. The brief's source policy explicitly accepts "AEP's disclosed
  authorized ROEs" as sufficient; the individual state-commission or FERC orders
  behind each line are the ultimate primary source for that specific docket, but
  AEP owns and stakes its own disclosure to investors on this table's accuracy.
- **Establishes:** Approved (authorized) ROE by state jurisdiction and by FERC
  formula rate, each with the effective date of the last approved rate case, and
  AEP's own "operating earned ROE" for the same business unit as of the same
  date — the regulator-set hurdle and how close AEP came to it, in one table.
- **Exact readings (Approved ROE / effective date of last approved rate case,
  vertically integrated retail utilities), as of 12/31/2024:**
  APCo–Virginia 9.75% (1/1/2025); APCo–West Virginia/WPCo 9.75% (3/6/2019);
  APCo–FERC 11.4% (1/1/2017); APCo/WPCo combined operating earned ROE 7.9%.
  KGPCo–Tennessee 9.50% (8/8/2022); earned 8.4%. KPCo–Distribution/Generation
  9.75% (1/16/2024); KPCo–FERC 11.7% (1/1/2017); earned (total) 4.4%.
  I&M–Indiana 9.85% (5/28/2024); I&M–Michigan 9.86% (7/15/2024); I&M–FERC 11.2%
  (1/1/2017); earned (total) 10.9%. PSO–Distribution/Generation 9.50%
  (10/23/2024); earned 7.6%. SWEPCO–Louisiana 9.50% (1/31/2023);
  SWEPCO–Arkansas 9.50% (7/1/2022); SWEPCO–Texas 9.25% (3/18/2021);
  SWEPCO–FERC 10.5% (1/1/2017); earned (total) 8.3%.
  T&D utilities: AEP Ohio–Distribution 9.70% (12/1/2021); AEP
  Ohio–Transmission 9.85% base (1/1/2018); AEP Ohio total earned 9.9%. AEP
  Texas–Transmission/Distribution 9.76% (10/1/2024); earned 8.9%.
  Transcos (FERC formula rate): AEP Appalachian Transco 10.35% (approved),
  earned 10.3%; AEP Ohio Transco 9.85%, earned 10.0%; AEP Kentucky Transco
  10.35%, earned 10.2%; AEP Indiana Michigan Transco 10.35%, earned 10.3%; AEP
  West Virginia Transco 10.35%, earned 10.7%; AEP Oklahoma Transco 10.50%,
  earned 10.5%.
- **Locator:** Page 1 (vertically integrated utilities table) and page 2 (T&D
  utilities and Transcos tables) of the two-page PDF; footnotes 1–2 on page 1
  define "rate base proxy" and "operating earned ROE" (12-month rolling, GAAP
  results adjusted for material nonrecurring items, not weather normalized).

### S10. American Electric Power, "Rate Base and ROE's" investor document, as of 3/31/2025
- **URL:** https://docs.aep.com/docs/investors/RateBase_and_ROE03-31-25.pdf (verified resolving, HTTP 200)
- **Classification:** Primary, same reasoning as S9 — a later, updated snapshot
  of the same AEP-authored table, used to confirm the approved ROE figures did
  not change quarter to quarter and to get a more current "operating earned ROE"
  reading.
- **Establishes:** The same approved-ROE figures as S9 (unchanged), plus updated
  operating earned ROE as of 3/31/2025: APCo/WPCo 8.2%; KGPCo–Tennessee 7.3%;
  KPCo 4.4%; I&M 10.3%; PSO–Oklahoma 8.0%; SWEPCO 8.1%; AEP Ohio total 10.2%; AEP
  Texas 9.2%; Transcos 10.0%–11.0%.
- **Locator:** Page 1 and page 2, same layout as S9, headed "as of 3/31/2025."

### S11. American Electric Power Co Inc, Form 10-Q for the quarter ended March 31, 2026
- **URL:** https://www.sec.gov/Archives/edgar/data/0000004904/000000490426000034/aep-20260331.htm (found via search; not re-verified with a fresh HTTP request in this pass, but the WebFetch tool successfully retrieved and parsed its XBRL structure)
- **Classification:** Primary. AEP's own SEC filing.
- **Establishes:** That a "2024 West Virginia Base Rate Case" (XBRL member tag
  `aep:A2024WestVirginiaBaseRateCaseMember`) had commission activity with date
  ranges extending into February 2026 — i.e., regulatory action on this docket
  did occur around that time. It does **not**, in what I was able to extract,
  confirm the specific 9.75% figure or the "$15 million" number reported in
  secondary summaries; those details would be in the note's narrative text, which
  this fetch did not surface (see Discarded).
- **Locator:** XBRL member/context metadata referencing `A2024WestVirginiaBaseRateCaseMember` with date ranges 2025-09-01–2025-09-30 and 2026-02-01–2026-02-28.

## Contradictions

1. **Historical vs. implied equity risk premium disagree by a wide margin, and
   the brief's chosen figure (implied, 4.23%) is the smaller and more volatile of
   the two common approaches.** S1's Table 1 shows historical ERP (arithmetic,
   stocks minus T.Bonds) ranging from 3.88% to 6.18% depending on the look-back
   window, versus S3's forward-looking implied ERP of 4.23% at the start of 2026
   (down from an implied 6.12% Damodaran reported in a January 2016 example
   inside S1). The two methods do not agree, and even the implied number moves
   month to month with market pricing — a genuine, active debate in the field,
   not a settled constant. The lesson should not present 4.23% as *the* ERP, only
   as a dated estimate.

2. **Book value vs. market value weights for WACC is explicitly contested and
   Damodaran takes a hard position.** S1 states flatly that book-value weighting
   is "irrelevant" and can be mathematically impossible (negative book equity at
   ~10% of US firms in 2015). This is worth stating as a real methodological
   fork, not a footnote, if the lesson touches WACC weighting mechanics.

3. **A single company-wide WACC as "the" hurdle rate is itself criticized inside
   the same authoritative source used to define it.** S1's "no risk subsidies"
   passage says using one WACC across businesses of different risk profiles
   causes safe businesses to subsidize risky ones. This complicates a clean
   "ROIC beats WACC, therefore value" story for a multi-segment company —
   AEP is a good example, since its Transcos, T&D utilities, and vertically
   integrated generation businesses carry different approved ROEs (9.25%–11.4%)
   under one consolidated entity.

4. **AEP's own reported "operating earned ROE" is below its approved ROE in some
   jurisdictions and at or above it in others — it is not uniformly "near/below."**
   Per S9/S10 (both AEP's own numbers): APCo/WPCo, KGPCo, KPCo, PSO, and SWEPCO
   all earned below their approved ROE as of both snapshot dates (worst case:
   KPCo earning 4.4% against a 9.75% approved ROE). I&M, AEP Ohio, and the
   Transcos earned at or slightly above their approved ROE in the same periods.
   The commission's framing ("near/below its allowed return") holds cleanly for
   the vertically integrated retail-utility segment, not for AEP as a whole — the
   writer should pick a specific jurisdiction (APCo/WPCo or KPCo are the starkest
   examples) rather than an unqualified "AEP."

5. **AEP's consolidated ROIC (on total capital) is not the same basis as its
   authorized ROE (on equity capital only), and a naive side-by-side comparison
   of the two numbers I computed (ROIC ≈ 6–7%) against AEP's authorized ROEs
   (≈ 9.25%–11.4%) risks reading as a like-for-like comparison when it is not.**
   ROIC blends AEP's ~35–40% debt / ~60–65% equity total capital structure and
   its (unusually low, see #6) effective tax rate; authorized ROE applies only to
   the equity slice of a state-specific regulatory rate base. AEP's own
   "operating earned ROE" figures in S9/S10 are the correct like-for-like
   comparison to "approved ROE" — both computed on the same equity basis by the
   same company. I recommend the lesson use the S9/S10 earned-vs-approved pairs
   as the AEP illustration and treat my ROIC computation as supplementary, framed
   explicitly as "return on AEP's total capital" rather than compared directly to
   the authorized ROE number.

6. **AEP's effective tax rate (3.4% in FY2025) is far below the 21% federal
   statutory rate, and this is disclosed and explained (production tax
   credits from wind and solar assets), not a data error.** Using the actual
   effective rate versus the 21% statutory rate changes computed after-tax
   operating income by roughly $940 million and moves computed ROIC from about
   6.1% to about 7.4% — a meaningful swing for a worked example. This is worth
   naming explicitly if AEP's ROIC appears as a specific percentage in the
   lesson, per S7's own tax reconciliation note.

7. **A specific secondary claim about a February 2026 West Virginia PSC order
   could not be verified against primary text and should not be treated as
   confirmed.** An AI-generated web-search summary (not a source I opened
   directly) asserted that the WV PSC "issued an order approving a revised ROE
   of 9.75% in the 2024 West Virginia Base Rate Case, resulting in a $15 million
   prospective annual increase." S11 confirms structurally that this docket had
   commission activity in the stated window, but I could not extract the
   narrative text confirming the 9.75%/$15 million detail from AEP's own 10-Q
   within this pass's fetch budget. The underlying 9.75% APCo–West
   Virginia/WPCo approved ROE figure is independently and separately confirmed
   by S9 and S10 (AEP's own investor disclosure, both snapshots agree), so the
   number itself is solid — only the "February 2026" order/amount detail is
   unverified and should not be cited.

## Numbers

| Figure | Value | Owning primary | Period / as-of date | Note |
|---|---|---|---|---|
| Risk-free rate (10-Yr UST par yield) | 4.75% | Treasury.gov (S4) | 2026-07-31 | Most recent trading day before article date |
| 2-Yr UST par yield | 4.28% | Treasury.gov (S4) | 2026-07-31 | Context/comparison only |
| 30-Yr UST par yield | 5.27% | Treasury.gov (S4) | 2026-07-31 | Context/comparison only |
| Equity risk premium (implied, S&P 500, over 10-Yr UST) | 4.23% | Damodaran (S3) | Start of 2026 (Jan 1, 2026) | Damodaran's own dated estimate; moves monthly |
| Worked cost of equity (β = 1 illustration) | ≈ 8.98% (4.75% + 4.23%) | Derived from S3 + S4 | 2026 | Estimate, not a single-source figure; state assumption plainly (β = 1) |
| AEP 2025 senior unsecured note issuance rate (pretax) | 5.38%–5.85% | AEP 10-K (S7) | Issued during FY2025 | Real, dated cost-of-debt anchor for a worked example |
| AEP junior subordinated notes issuance rate (pretax) | 5.80%–6.05% | AEP 10-K (S7) | Issued during FY2025 | — |
| Costco FY2025 operating income | $10,383 million | Costco 10-K (S5/S6) | FY ended 8/31/2025 | — |
| Costco FY2025 effective tax rate | 25.1% | Costco 10-K (S5) | FY2025 | Company-disclosed, exact |
| Costco FY2025 after-tax operating income | ≈ $7,777 million | Derived: 10,383 × (1−0.251) | FY2025 | — |
| Costco invested capital, start of FY2025 (= FY2024 year-end) | $18,375 million | Derived from S5/S6: LT debt $5,794M + current LT debt $103M + equity $23,622M − cash $9,906M − ST investments $1,238M | 9/1/2024 | Damodaran timing convention (t−1 capital) |
| **Costco ROIC (FY2025 operating income / FY2024-end invested capital)** | **≈ 42.3%** | Derived: 7,777 / 18,375 | FY2025 | Well above any plausible cost of capital |
| Costco ROIC, alternative (FY2025 operating income / FY2025-end invested capital of $19,668M) | ≈ 39.5% | Derived | FY2025 | Same conclusion either way |
| AEP FY2025 operating income | $5,319 million | AEP 10-K (S7/S8) | FY ended 12/31/2025 | — |
| AEP FY2025 pretax income (incl. equity earnings) | $3,825 million | AEP 10-K (S7) | FY2025 | Net income $3,696M + tax $129M |
| AEP FY2025 effective tax rate | 3.37% (129/3,825) | AEP 10-K (S7) | FY2025 | Depressed by production tax credits, not debt shield — see Contradiction #6 |
| AEP FY2025 after-tax operating income (actual effective rate) | ≈ $5,140 million | Derived: 5,319 × (1−0.0337) | FY2025 | — |
| AEP FY2025 after-tax operating income (illustrative 21% statutory rate) | ≈ $4,202 million | Derived: 5,319 × 0.79 | FY2025 | Alternative, avoids PTC distortion |
| AEP invested capital, start of FY2025 (= FY2024 year-end) | $69,384 million | Derived from S7/S8: LT debt $39,307.8M + current LT debt $3,335M + equity $26,943.8M − cash $202.9M | 12/31/2024 | Damodaran timing convention |
| **AEP ROIC (actual effective-tax basis)** | **≈ 7.4%** | Derived: 5,140 / 69,384 | FY2025 | See Contradiction #5 on basis mismatch with authorized ROE |
| AEP ROIC (21%-statutory-tax basis) | ≈ 6.1% | Derived: 4,202 / 69,384 | FY2025 | — |
| AEP approved ROE, APCo–Virginia | 9.75% | AEP investor disclosure (S9/S10) | Effective 1/1/2025 | — |
| AEP approved ROE, APCo–West Virginia/WPCo | 9.75% | AEP investor disclosure (S9/S10) | Effective 3/6/2019 | See Contradiction #7 on a more recent, unverified order |
| AEP approved ROE, KPCo–Distribution/Generation (Kentucky) | 9.75% | AEP investor disclosure (S9/S10) | Effective 1/16/2024 | Earned only 4.4% (S9/S10) — the starkest below-hurdle case |
| AEP approved ROE, PSO–Oklahoma | 9.50% | AEP investor disclosure (S9/S10) | Effective 10/23/2024 | Earned 7.6%–8.0% |
| AEP approved ROE, SWEPCO (LA/AR/TX blend) | 9.25%–9.50% | AEP investor disclosure (S9/S10) | Various 2021–2023 | Earned 8.1%–8.3% |
| AEP approved ROE, I&M (Indiana/Michigan) | 9.85% / 9.86% | AEP investor disclosure (S9/S10) | Effective 5/28/2024 and 7/15/2024 | Earned 10.3%–10.9% — at/above approved |
| AEP APCo/WPCo operating earned ROE | 7.9% (12/31/24) / 8.2% (3/31/25) | AEP investor disclosure (S9/S10) | As of stated dates | Directly comparable to the 9.75% approved figure above |

## Source assets

- **AEP's "Rate Base and ROE's" table (S9/S10).** This is already a formatted,
  publication-quality comparison table pairing "Approved ROE" against "Operating
  Earned ROE" by jurisdiction, with effective dates. A cropped version showing
  jurisdiction name, approved ROE, and operating earned ROE (dropping the
  dollar rate-base column if space is tight) would carry the "near/below the
  hurdle" argument better than a paragraph of prose — a reader can see, at a
  glance, that APCo/WPCo earns roughly 1.5–2 points below what regulators
  authorize. Keep the "as of" date visible; omit the FERC-only rows if
  simplifying, since they are a different (and higher) regulatory basis than the
  state retail rows.
- **Damodaran's Figure 16, "Cost of Capital for US Companies" (S1, p.27).** A
  histogram of computed cost of capital across ~8,000 US firms, January 2016,
  with percentile markers (10th 5.23%, median 8.00%, 90th 10.00%). Useful only
  with an explicit caveat that the data is from January 2016 — a decade stale
  relative to this lesson's 2026 risk-free rate and ERP — so it should not be
  used to assert "typical WACC today," only to make the point that computed
  WACCs cluster in a fairly narrow band across most companies.
- **Costco's Consolidated Statements of Income and Balance Sheets (S5, pp.37,
  39).** Standard financial-statement tables; no crop of these carries the
  argument better than the two or three line items already quoted above. None
  needed beyond what is already extracted into the Numbers table.
- **AEP's Consolidated Statements of Income and income-tax reconciliation note
  (S7).** Same as above — the tax reconciliation table (showing the 21%
  statutory rate walked down to 3.37% actual, with the production-tax-credit
  line item visible) could be cropped if the lesson wants to visually show why
  AEP's effective tax rate is unusually low, but this is a secondary point, not
  central to the lesson's argument. None found that outperforms the quoted
  numbers in prose.
- **Treasury's daily par yield curve.** A tabular data source, not a chart; no
  visual asset beyond a simple stated number is warranted for one point-in-time
  rate.

## Discarded

- **Web-search AI summary claiming a specific February 2026 West Virginia PSC
  order (9.75% ROE, $15 million increase).** Not opened directly; could not
  independently confirm the order text or the dollar figure within this pass's
  fetch budget. See Contradiction #7. Do not cite as fact; the underlying 9.75%
  approved-ROE figure is independently confirmed elsewhere (S9/S10).
- **CorporateFinanceInstitute-style blog restatements of ROIC vs. WACC** (surfaced
  in early search results: dividend.school "ROIC vs. WACC," einvestingforbeginners
  "WACC vs. ROIC," a Medium "Decoding ROIC" post, an "Interactive SPA" site).
  Not opened in full text; these are tertiary restatements of the same rule
  already sourced authoritatively from Damodaran (S1, S2). Discarded once the
  primary/authoritative papers were secured.
- **Berk & DeMarzo and Brealey/Myers textbooks**, named as acceptable sources in
  the commission. Could not access the actual text (not freely available
  online and not present in this environment); did not cite. Relied on
  Damodaran's papers instead, which the commission explicitly lists as an
  acceptable alternative ("a standard text such as Berk & DeMarzo or
  Brealey/Myers, or Aswath Damodaran's published material").
  A reader who wants the textbook framing directly will need it added by an
  editor with access to a physical or licensed copy.
- **Macrotrends "American Electric Power ROE - Return on Equity 2012-2026,"
  tikr.com blog posts, ad-hoc-news.de articles.** Surfaced in search results
  about AEP's returns and rate cases; not opened or relied on, since AEP's own
  SEC filings and investor-relations documents (S7–S10) were directly available
  and are stronger primaries for the same facts.
- **last10k.com mirrors of Costco's and AEP's 10-Ks.** Third-party re-hosting of
  the same SEC filings; not used, since the original filings on sec.gov were
  directly fetchable and preferred.
- **An initial WebFetch attempt to parse `costofcapital.pdf` and
  `returnmeasures.pdf` as web pages** failed (the tool could not decode the raw
  PDF binary stream). Superseded by re-reading the same downloaded PDF files
  through the Read tool's native multimodal PDF extraction, which succeeded and
  is the basis for S1 and S2 above.
- **A first WebFetch pass at Treasury.gov's `TextView` endpoint** returned a
  paraphrase claiming "No Results Found" for the current month. Superseded by
  directly downloading and reading the raw CSV export (S4), which resolved the
  ambiguity and gave an exact, quotable data row.
