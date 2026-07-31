# Evidence — investing/return-on-capital (01)

## What this evidence supports, and where it is thin

This record supports a full, reproducible ROIC calculation for Costco's fiscal
2025 (Aug. 31, 2025 year-end) 10-K, a full contrast calculation for American
Electric Power's fiscal 2025 (Dec. 31, 2025 year-end) 10-K under the *same*
convention, and an authoritative definition of ROIC/NOPAT/invested capital
with the specific convention forks the article must be honest about (cash
treatment, effective-vs-marginal tax rate, goodwill, operating leases). Both
companies' most recent 10-Ks are used, both already filed as of today
(2026-07-31). It also supports the value-creation-test statement from
Damodaran's own paper, and a sourced (not invented) cost-of-capital ballpark
from Damodaran's live sector dataset plus AEP's own disclosed rate-case ROEs.

Where it is thin: the "cost of capital" side of the contrast is not a single
clean number. Damodaran's broad "Utility (General)" sector WACC (4.36%, a
CAPM/market-based blended figure) and AEP's own regulator-authorized ROE band
(9.25%–10.9%, an accounting/ratemaking figure for the equity slice only) are
built on different methods and disagree about how far AEP's ROIC actually
falls short. Both are sourced below; the writer must pick a framing honestly
rather than average them into a false precision. Separately, AEP's book
effective tax rate (3.4%) is so distorted by production tax credits and a
regulatory deferred-tax remeasurement that using it "as reported" for NOPAT is
defensible but arguably misleading — I computed AEP's ROIC three ways (its own
effective rate, the 21% federal statutory rate, and a ~25% rate comparable to
Costco's) and it lands in a tight 4.9%–6.4% band regardless, which is the
finding I'd lean on. The invested-capital "average vs. ending balance" and
"cash vs. cash+short-term-investments" convention forks likewise move Costco's
number by several points (22%–40% depending on convention); the ending-balance,
cash-only convention (37.4%) is what I'd recommend the lesson stand on, stated
as a choice, not the only true number.

## Sources

### 1. Costco Wholesale Corp., Form 10-K for fiscal year ended August 31, 2025 (SEC EDGAR)
- URL (primary filing document): https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/cost-20250831.htm
- URL (filing index): https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/0000909832-25-000101-index.htm
- URLs (XBRL statement/note viewer pages, read individually and cross-checked
  against the numbers above): 
  - Income statement: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/R3.htm
  - Balance sheet: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/R5.htm
  - Debt carrying-value detail: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/R50.htm
  - Effective tax rate reconciliation: https://www.sec.gov/Archives/edgar/data/909832/000090983225000101/R63.htm
- **Classification: Primary.** This is the filer's own audited annual report,
  filed with the SEC; it owns every number cited from it.
- **Establishes:** all Costco fiscal-2025 income-statement and balance-sheet
  figures used in the worked ROIC calculation below (see Numbers).
- **Locators:** Filed with SEC EDGAR 2025-10-08, accession 0000909832-25-000101,
  for fiscal year ended August 31, 2025 (Costco's 52-week fiscal year). Item
  8, "Financial Statements and Supplementary Data," begins page 33.
  Consolidated Statements of Income: page 33. Consolidated Balance Sheets:
  page 34. Note on Debt: page 50. Note on Income Taxes: page 53.
- **Useful verbatim/derived figures:** see Numbers section.

### 2. American Electric Power Co., Inc., Form 10-K for fiscal year ended December 31, 2025 (SEC EDGAR)
- URL (primary filing document): https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/aep-20251231.htm
- URL (filing index): https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/
- URLs (XBRL statement/note viewer pages, read individually):
  - Income statement: https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/R3.htm
  - Balance sheet: https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/R8.htm
  - Income tax rate reconciliation: https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/R92.htm
  - Rate Matters note detail: https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/R58.htm
- **Classification: Primary.** AEP's own audited annual report; owns every
  number cited from it, including the rate-case ROE percentages AEP itself
  requested/was awarded by state regulators.
- **Establishes:** all AEP fiscal-2025 (calendar year) income-statement and
  balance-sheet figures used in the contrast ROIC calculation, plus AEP's own
  disclosure of the regulatory ROE figures active in its jurisdictions during
  2025.
- **Locators:** Filed with SEC EDGAR 2026-02-12, accession
  0000004904-26-000013, for fiscal year ended December 31, 2025. Consolidated
  Statements of Income: page 96. Consolidated Balance Sheets: pages 99–100
  (assets p.99, liabilities & equity p.100). Notes to Financial Statements of
  Registrants begin page 182. Note 4, Rate Matters: page 200. Note 5, Effects
  of Regulation: page 213. Note 12, Income Taxes: page 282. Note 15,
  Financing Activities (debt detail): page 297.
- **Useful verbatim passage (Rate Matters note, p.200):** "OPCo filed a
  request with the PUCO for a net $97 million annual increase in distribution
  base rates based upon a 10.9% ROE." "PSO filed a request with the OCC for a
  $218 million annual base rate increase based upon a 10.8% ROE." "the WVPSC
  issued an order on the Companies' base case filing... based on a 9.25% ROE."
  "KPCo filed a request with the KPSC for a $96 million net annual increase in
  base rates based upon a proposed 10% ROE." Note: most of these are
  *requested* ROEs pending regulatory decision during fiscal 2025; the West
  Virginia figure (9.25%) is the one explicit *authorized/ordered* ROE found
  in this note. State this precisely — do not call all four "authorized."

### 3. Aswath Damodaran, "Return on Capital (ROC), Return on Invested Capital (ROIC) and Return on Equity (ROE): Measurement and Implications," Stern School of Business, July 2007
- URL: https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf
- **Classification: Primary.** This is the authoring finance academic's own
  paper laying out the definitions and reasoning; it owns the claims about
  what ROIC/NOPAT/invested capital mean and why they're computed the way they
  are. (Read in full via local text extraction of the PDF; 69 pages, read
  pages 1–15 closely, which cover all definitional material needed.)
- **Establishes:** the formal ROIC/NOPAT/invested-capital definitions, the
  cash-netting rationale, the financing-vs-operating invested-capital
  equivalence and its two named exceptions, the effective-vs-marginal tax
  rate choice, and the value-creation/excess-returns principle.
- **Useful verbatim passages (with page numbers as printed in the PDF):**
  - p.4: "In effect, this is what we are trying to do when we compute the
    return on invested capital and compare it to the cost of capital."
  - p.5: "A firm that generates higher returns on an investment than it costs
    it to raise capital for that investment is earning excess returns and
    will trade at a premium over a firm that does not earn excess returns."
    [This is the clean, quotable value-creation-test sentence.] The same
    paragraph continues: "...whereas a firm that earns returns that [do]
    match up to its cost of funding will destroy value as it grows" — the
    extracted text is missing a word here (reads as "do match up," which
    contradicts the point being made); the intended sense, given the
    paragraph's logic, is a firm whose returns do *not* clear its cost of
    funding destroys value by growing. Use the p.5 sentence above instead;
    it is unambiguous and says the same thing cleanly.
  - p.6: "we can safely conclude that the key number in a valuation is not
    the cost of capital that we assign a firm but the return earned on
    capital that we attribute to it."
  - p.7: "Return on Capital (ROIC) = Operating Income_t (1 - tax rate) / Book
    Value of Invested Capital_(t-1)." Four components named: (1) operating
    income not net income in the numerator, (2) "a hypothetical tax based on
    an effective or marginal tax rate," (3) book values not market values for
    invested capital, (4) capital is measured at the *end of the prior
    year*, operating income is the *current* year's — a timing convention
    this lesson's simpler single-balance-sheet approach will depart from; flag
    it as a simplification, don't hide it.
  - p.7–8: warns against using *actual taxes paid* in place of a hypothetical
    unlevered tax rate — using actual cash taxes double-counts the interest
    tax shield (once in ROIC, again in the cost of capital). Directly
    relevant to the AEP tax-rate convention question below.
  - p.9: "The reason we net out cash is to be consistent with the use of
    operating income as our measure of earnings. The interest income from
    cash is not part of operating income." — the clean statement for why
    invested capital nets out cash.
  - p.9–10: gives the financing approach (book debt + equity, cash netted
    out) and the equivalent operating/asset approach: "Invested Capital =
    Fixed Assets + Current Assets – Current Liabilities – Cash = Fixed Assets
    + Non-cash Working Capital." States the two approaches diverge when (a)
    the firm holds minority stakes in other companies (excluded from the
    asset approach, implicitly included in the capital approach) or (b) the
    firm carries non-debt long-term liabilities like unfunded pension
    obligations (included in the asset approach, excluded from the capital
    approach when only interest-bearing debt is counted).

### 4. Aswath Damodaran, "Cost of Capital by Sector (US)," NYU Stern data page
- URL: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html
- **Classification: Primary.** Damodaran's own live, self-compiled dataset,
  updated by him annually; owns the sector WACC figures it reports.
- **Establishes:** current (dataset explicitly dated "as of January 2026")
  sector-level cost-of-capital estimates for context, not for a false-precise
  claim about either specific company's actual cost of capital.
- **Locators/figures (Jan. 2026 vintage):** "Total Market (including
  financials)": 5,994 firms, cost of equity 8.02%, cost of debt 5.29%, WACC
  6.96%. "Retail (General)": 23 firms, cost of equity 7.54%, cost of debt
  5.07%, WACC 7.27%. "Utility (General)": 14 firms, cost of equity 5.02%,
  cost of debt 4.73%, WACC 4.36%.
- **Caveat:** this is a broad sector average built from a small firm count
  (14 firms for "Utility (General)," 23 for "Retail (General)") using
  Damodaran's own CAPM/market-based methodology — it is a ballpark, not a
  company-specific WACC for Costco or AEP. State it as such.

### 5. Wall Street Prep, "Return on Invested Capital (ROIC)"
- URL: https://www.wallstreetprep.com/knowledge/roic-return-on-invested-capital/
- **Classification: Secondary.** A widely used practitioner-training
  reference explaining and popularizing the ROIC concept; it reports on
  established finance theory rather than originating it.
- **Establishes:** a second, independent statement of the same formula and
  the ROIC-vs-WACC decision rule, useful for corroboration and for a
  plain-English restatement.
- **Useful verbatim passages:** "Return on Invested Capital (ROIC) = NOPAT ÷
  Average Invested Capital." "NOPAT = EBIT × (1 – Tax Rate %)." "Invested
  Capital = Fixed Assets + Net Working Capital (NWC) + Acquired Intangibles +
  Goodwill" (the operating-approach version, explicitly keeping goodwill and
  acquired intangibles inside invested capital — the opposite convention from
  excluding them). Alternative financing approach given as net debt (gross
  debt − cash) plus equity. Decision rule: "If the ROIC is higher than the
  WACC, that means the company creates positive value, whereas if the ROIC is
  lower than the WACC, that means the company's value is declining."

### 6. Corporate Finance Institute, "Invested Capital"
- URL: https://corporatefinanceinstitute.com/resources/accounting/invested-capital/
- **Classification: Secondary.** A finance-training reference site (the kind
  of CFA/Investopedia-grade explainer the commission calls for); reports on
  standard practice rather than originating it.
- **Establishes:** an explicit statement that operating leases belong in the
  financing-approach invested-capital total as debt-equivalent: "add the
  short-term debt, long-term debt, and PV of lease obligations." Confirms the
  operating approach as working capital + PP&E + goodwill & intangibles, and
  the financing approach as total debt & leases + total equity and equity
  equivalents − non-operating cash & investments.
- **Use:** corroborates that "should operating leases count as debt in
  invested capital" is a live, named convention choice (post-ASC-842), not
  something this lesson is inventing. Neither Costco's nor AEP's figures used
  in the worked calculation below capitalize operating leases as debt (both
  use the plainer debt+equity−cash convention); this source is why that
  omission must be stated as a choice, not silently made.

### 7. Bob Shively (Enerdynamics President and Lead Facilitator), "How Regulators Determine a Utility's Return on Equity (ROE)," Enerdynamics Energy Currents blog
- URL: https://www.enerdynamics.com/Energy-Currents_Blog/How-Regulators-Determine-a-Utilitys-Return-on-Equity-ROE.aspx
- **Classification: Secondary.** An energy-industry training firm's
  explanatory post; reports on regulatory practice and cites the governing
  case law rather than being a regulatory order itself.
- **Establishes:** the general principle that state utility regulators set a
  utility's allowed ROE deliberately to approximate what investors could earn
  elsewhere at comparable risk — the plain-language version of the
  cost-of-capital idea, applied specifically to a regulated utility, which is
  exactly the intuition the lesson needs for the "cost of capital = what
  investors could earn elsewhere at similar risk" framing.
- **Useful verbatim passage:** ROE is set to be "sufficient to attract the
  capital needed for the utility to construct and maintain a safe and
  reliable system while not charging utility customers more than is
  necessary," tracing this to the standard that a utility's return "should be
  commensurate with other enterprises having corresponding risks" and
  "sufficient to assure confidence in the financial integrity" of the
  enterprise (the 1944 *FPC v. Hope Natural Gas Co.* standard, as
  characterized by the author). No specific percentage figures given in this
  piece — use AEP's own 10-K (source 2) for the actual FY2025 numbers.

## Contradictions

1. **Utility "cost of capital" does not resolve to one number.** Damodaran's
   sector-wide "Utility (General)" WACC (4.36%, Jan. 2026, source 4) sits
   *below* every version of AEP's computed ROIC (4.9%–6.4%, see Numbers) —
   which on its face would say AEP clears its cost of capital. But AEP's own
   FY2025 regulatory filings (source 2) show state commissions setting or
   AEP requesting equity returns of 9.25%–10.9% — well *above* AEP's computed
   ROIC. These are not the same measurement (blended-firm CAPM WACC vs.
   allowed-return-on-the-equity-slice-of-rate-base) and they point in
   different directions about whether AEP is a value-creator. This is a real
   tension in the literature, not a research error, and the article should
   not paper over it by picking whichever number fits the story. The
   more defensible framing: AEP's book ROIC, computed the same way as
   Costco's, sits well below the return regulators themselves treat as fair
   for the equity portion of its capital — that comparison is internally
   consistent (both concern the return utility investors expect); the
   sector-wide blended WACC number is offered only as a rough second
   reference point, with its very different basis flagged.

2. **Effective tax rate for NOPAT is not a neutral choice for AEP.** AEP's
   GAAP effective tax rate for FY2025 is 3.46% (tax expense $129M / pretax
   income $3,724M), driven overwhelmingly by production tax credits
   (−6.4 points), remeasurement of excess accumulated deferred income taxes
   from the 2017 tax reform being flowed back to ratepayers (−10.0 points),
   and AFUDC equity (a non-cash, non-taxable construction allowance, −1.1
   points) — all disclosed in the rate reconciliation (source 2, p.282).
   Applying this rate to operating income makes NOPAT (and therefore ROIC)
   noticeably higher than applying a marginal/statutory rate would. Costco's
   effective and statutory rates are much closer (25.1% effective vs. 21%
   federal statutory), so this distortion is specific to AEP and to
   capital-intensive, tax-credit-heavy utilities generally — which somewhat
   undercuts a literal "apples-to-apples" claim unless the tax-rate choice is
   stated. I computed AEP's ROIC three ways (see Numbers) precisely so the
   writer isn't forced to pick blind.

3. **Cash treatment swings Costco's ROIC by 15+ points.** Whether cash and
   cash equivalents alone are netted from invested capital, or cash plus
   short-term investments, or nothing at all, moves Costco's computed ROIC
   from about 37% to about 40% to about 22% (see Numbers). Costco is
   unusually cash-rich, so this is not a rounding issue — it is the single
   biggest lever in the whole calculation. Damodaran's rationale (source 3,
   p.9) supports netting *some* form of non-operating financial assets; it
   does not by itself settle where to draw the line between "cash" and
   "short-term investments," both of which are non-operating for a retailer.
   State the convention chosen, and that the number would look meaningfully
   different under a different (also defensible) convention.

4. **Reconciliation-table rounding vs. computed effective tax rate (Costco).**
   Costco's tax-rate reconciliation note lists a total effective rate of
   25.10% (source 1, R63), built from rounded component percentages; dividing
   the reported dollar figures directly (provision $2,719M / pretax income
   $10,818M) gives 25.13%. The difference is trivial (three basis points) but
   worth noting so the writer doesn't treat either figure as more precise
   than it is.

## Numbers

### Costco Wholesale Corp. — fiscal year ended August 31, 2025

| Item | Value | Source | Statement / line | Period |
|---|---|---|---|---|
| Operating income | $10,383 million | 10-K, R3 (Consolidated Statements of Income), p.33 | "Operating Income" | FY2025 (year ended 8/31/2025) |
| Income before income taxes | $10,818 million | 10-K, R3, p.33 | "Income Before Income Taxes" | FY2025 |
| Provision for income taxes | $2,719 million | 10-K, R3, p.33 | "Provision for Income Taxes" | FY2025 |
| Effective tax rate (computed) | 25.13% ($2,719M / $10,818M) | Derived from above | — | FY2025 |
| Effective tax rate (per reconciliation note) | 25.10% | 10-K, R63 (rate reconciliation), p.53 | "Total provision" line, % column | FY2025 |
| Long-term debt, excluding current portion | $5,713 million | 10-K, R5 (Balance Sheet), p.34 | "Long-term debt, excluding current portion" | as of 8/31/2025 |
| Current portion of long-term debt | $75 million | 10-K, R50 (Debt carrying value detail), p.50 | "Current portion of long-term debt" (not broken out on balance sheet face; folded into "Other current liabilities") | as of 8/31/2025 |
| Total debt (current + long-term) | $5,788 million | Derived: $75M + $5,713M | — | as of 8/31/2025 |
| Total stockholders' equity | $29,164 million | 10-K, R5, p.34 | "TOTAL EQUITY" | as of 8/31/2025 |
| Cash and cash equivalents | $14,161 million | 10-K, R5, p.34 | "Cash and cash equivalents" | as of 8/31/2025 |
| Short-term investments | $1,123 million | 10-K, R5, p.34 | "Short-term investments" | as of 8/31/2025 |
| Prior-year total debt (for reference) | $5,897 million ($103M + $5,794M) | 10-K, R5 & R50 | — | as of 9/1/2024 |
| Prior-year total equity | $23,622 million | 10-K, R5 | — | as of 9/1/2024 |
| Prior-year cash | $9,906 million | 10-K, R5 | — | as of 9/1/2024 |

**Worked NOPAT (Costco, FY2025):**
NOPAT = Operating income × (1 − effective tax rate) = $10,383M × (1 − 0.2513)
= $10,383M × 0.7487 ≈ **$7,773 million**

**Worked invested capital (Costco, FY2025, financing approach, cash-only convention):**
Invested capital = Total debt + Total equity − Cash & equivalents
= $5,788M + $29,164M − $14,161M = **$20,791 million**

**Worked ROIC (Costco, FY2025, primary convention):**
ROIC = NOPAT / Invested capital = $7,773M / $20,791M ≈ **37.4%**

**Alternate conventions, same inputs (for the honesty section, not the headline number):**
- Also netting short-term investments: invested capital = $20,791M − $1,123M =
  $19,668M → ROIC ≈ **39.5%**
- Not netting any cash (gross financing capital = debt + equity only):
  invested capital = $5,788M + $29,164M = $34,952M → ROIC ≈ **22.2%**
- Using average of FY2025 and FY2024 ending invested capital instead of the
  FY2025 ending balance alone (the timing convention Damodaran actually
  recommends, source 3 p.7): prior-year invested capital (cash-only
  convention) = $5,897M + $23,622M − $9,906M = $19,613M; average of $20,791M
  and $19,613M = $20,202M → ROIC ≈ **38.5%**

### American Electric Power Co., Inc. — fiscal year ended December 31, 2025

| Item | Value | Source | Statement / line | Period |
|---|---|---|---|---|
| Total revenues | $21,876 million | 10-K, R3, p.96 | "Total Revenues" | FY2025 (calendar year) |
| Operating income | $5,319 million | 10-K, R3, p.96 | "Operating Income" | FY2025 |
| Income before income tax expense (and equity earnings) | $3,724 million | 10-K, R3, p.96 | "Income Before Income Tax Expense" | FY2025 |
| Income tax expense | $129 million | 10-K, R3, p.96 | "Income Tax Expense" | FY2025 |
| Effective tax rate (computed) | 3.46% ($129M / $3,724M) | Derived from above | — | FY2025 |
| Effective tax rate (per reconciliation note) | 3.4% | 10-K, R92 (tax rate reconciliation), p.282 | "Income Tax Expense (Benefit)" %, total line | FY2025 |
| Short-term debt | $1,508 million | 10-K, R8 (Balance Sheet), p.100 | "Total Short-term Debt" | as of 12/31/2025 |
| Long-term debt due within one year | $3,194 million | 10-K, R8, p.100 | "Long-term Debt Due Within One Year" | as of 12/31/2025 |
| Long-term debt (noncurrent) | $44,128 million | 10-K, R8, p.100 | "Long-term Debt" (noncurrent liabilities) | as of 12/31/2025 |
| Total debt | $48,830 million | Derived: $1,508M + $3,194M + $44,128M | — | as of 12/31/2025 |
| Total common shareholders' equity | $31,138 million | 10-K, R8, p.100 | "Total Common Shareholder's Equity" | as of 12/31/2025 |
| Noncontrolling interests | $1,080 million | 10-K, R8, p.100 | "Noncontrolling Interests" | as of 12/31/2025 |
| Total equity (incl. noncontrolling interests) | $32,218 million | 10-K, R8, p.100 | "TOTAL EQUITY" | as of 12/31/2025 |
| Cash and cash equivalents | $197 million | 10-K, R8, p.99 | "Cash and Cash Equivalents" | as of 12/31/2025 |

**Worked NOPAT (AEP, FY2025, three tax-rate conventions):**
- Using AEP's own effective tax rate: NOPAT = $5,319M × (1 − 0.0346) =
  $5,319M × 0.9654 ≈ **$5,135 million**
- Using the 21% federal statutory rate: NOPAT = $5,319M × 0.79 ≈
  **$4,202 million**
- Using a ~25% rate comparable to Costco's effective rate (for a stricter
  apples-to-apples cross-company read): NOPAT = $5,319M × 0.75 ≈
  **$3,989 million**

**Worked invested capital (AEP, FY2025, same convention as Costco: financing
approach, cash-only netted, total equity including noncontrolling interests):**
Invested capital = Total debt + Total equity − Cash & equivalents
= $48,830M + $32,218M − $197M = **$80,851 million**

**Worked ROIC (AEP, FY2025), three ways:**
- AEP's own effective tax rate: $5,135M / $80,851M ≈ **6.4%**
- 21% federal statutory rate: $4,202M / $80,851M ≈ **5.2%**
- ~25% comparable rate: $3,989M / $80,851M ≈ **4.9%**

All three land in a **~5%–6.4%** band — robust to the tax-rate choice. Using
common equity only ($31,138M instead of $32,218M; invested capital $79,771M)
shifts these to 6.4%, 5.3%, and 5.0% respectively — a negligible difference.

**Cost-of-capital reference points for the contrast (both sourced, not invented):**
- Damodaran sector WACC, Jan. 2026 vintage (source 4): "Retail (General)"
  7.27%; "Utility (General)" 4.36%; "Total Market" 6.96%.
- AEP's own FY2025 regulatory filings (source 2, Rate Matters note, p.200):
  requested ROEs of 10.9% (Ohio/OPCo), 10.8% (Oklahoma/PSO), 10% (Kentucky/
  KPCo); one explicit authorized/ordered ROE of 9.25% (West Virginia).

**Headline contrast:** Costco's ROIC (~37%, primary convention) sits roughly
30 percentage points above the retail-sector WACC ballpark (~7.3%). AEP's
ROIC (~5%–6.4%, any tax convention) sits below every regulatory ROE figure
AEP itself cites for FY2025 (9.25%–10.9%), and roughly in line with (slightly
above) Damodaran's broad utility-sector WACC estimate (4.36%) — a much
narrower, more ambiguous spread than Costco's, which is itself the honest
point: AEP is close to its cost of capital, not dramatically below it, and
which side of the line it falls on depends on which "cost of capital" the
reader means.

## Source assets

- **Costco Consolidated Statements of Income, FY2025 (source 1, R3.htm,
  p.33).** A clean, five-line income statement (net sales, membership fees,
  merchandise costs, SG&A, operating income) that a table or annotated
  callout could reproduce directly to let the reader see NOPAT's starting
  point without a full statement walkthrough (which the lesson should avoid
  repeating from the prior lesson). Crop/copy should keep the operating
  income line and the tax lines together; omit the per-share data below net
  income, which this lesson doesn't use.
- **AEP Income Tax Rate Reconciliation table, FY2025 (source 2, R92.htm,
  p.282).** This table is the single best visual for the "why is the tax
  rate so low" convention point: it shows the 21% federal statutory rate
  being pulled down to 3.4% almost entirely by production tax credits and a
  deferred-tax remeasurement, both regulatory/tax-policy artifacts rather
  than ordinary profitability. A reader can see in one table why "the
  reported effective tax rate" is not a neutral, always-comparable number.
  Keep the federal statutory line and the total; the individual small
  adjustment lines (changes in unrecognized tax benefits, etc.) can be
  simplified or omitted without losing the point.
- **AEP Rate Matters excerpt, FY2025 (source 2, R58.htm/note 4, p.200).** Not
  a chart, but a strong quotable block: several state commissions' explicit
  ROE percentages in one place, in the company's own words, makes the
  "regulators set an allowed return meant to match investors' required
  return" idea concrete rather than abstract.
- **Comparison bar chart (to be built, not sourced from an image): Costco
  ROIC vs. AEP ROIC vs. their respective cost-of-capital ballparks.** Data
  for this exists entirely in the Numbers section above (four bars: Costco
  ROIC ~37%, retail WACC ballpark ~7.3%; AEP ROIC ~5%–6.4% range, utility WACC
  ballpark ~4.4% and AEP's own regulatory ROE band ~9.25%–10.9%). This is the
  chart most likely to carry the lesson's central comparison better than
  prose; per house style it would be a committed `chart-N.py`, not a screenshot.
- Damodaran's ROIC paper and the CFI/Wall Street Prep pages: no chart-worthy
  visual content — they are prose/formula references. None found beyond text
  quotation.

## Discarded

- Morgan Stanley / Counterpoint Global Insights, "Return on Invested
  Capital" PDF (https://www.morganstanley.com/im/publication/insights/articles/article_returnoninvestedcapital.pdf)
  — returned an "Access Denied" error page on fetch; never actually read, so
  never cited or relied on for any claim.
- https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html.htm
  (note the doubled `.htm`) — resolved to a stale, differently-formatted copy
  showing "Data used is as of January 2013" with implausible utility WACC
  figures (3.1%–3.6%) inconsistent with the live page. Discarded in favor of
  the correct current URL (`wacc.html`, no doubled extension), which returned
  the live January 2026 dataset used above.
- SEC EDGAR company-filing browse CGI URL
  (https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany...) — used only
  to enumerate Costco's recent 10-K filing dates/accession numbers, which
  checked out; not cited as a source of financial figures since it's a filing
  index, not the filing itself.
- Search-result snippets citing stock-analysis-on.net and macrotrends.net for
  Costco's current-debt breakdown and AEP's authorized-ROE history — seen only
  as search summaries, never opened and read directly, so not used as
  sources; every figure they suggested was independently verified against the
  primary SEC EDGAR filings before being recorded above.
- marginofmaybe.com blog post on operating leases and ROIC — surfaced in a
  search result as thematically relevant but not opened; not read, not cited.
- SEC EDGAR "cgi-bin/viewer" URL (attempted for Costco) — returned "Missing
  accession number parameter," a dead end; abandoned in favor of the
  FilingSummary.xml route, which worked.

## Candidate Background / Go-deeper links

**Background (internal, prior lessons in this course — already established
by the commission):**
- `how-a-business-earns-a-profit` — the income statement, margins, and where
  operating income comes from.
- `profit-versus-cash` — why accrual profit and cash timing diverge.
- `what-a-company-owns-and-owes` — the balance sheet, including the earlier
  finding that Costco's $994 million of goodwill is folded into a single
  "other long-term assets" line rather than broken out — directly relevant
  context for the invested-capital/goodwill convention point in this lesson.

**Go deeper (external, beyond this paper):**
- Aswath Damodaran's ROIC/ROE paper itself
  (https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/returnmeasures.pdf) —
  for a reader who wants the full rigor (timing conventions, cash-flow-based
  ROIC variants, the assessment of when accounting returns are trustworthy)
  beyond what the lesson has room to teach.
- Damodaran's live Cost of Capital by Sector dataset
  (https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.html) —
  for a reader who wants to look up a real WACC ballpark for any industry,
  since this lesson explicitly defers precise WACC measurement to a later
  lesson.
