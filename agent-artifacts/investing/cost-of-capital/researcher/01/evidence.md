# Evidence: investing/cost-of-capital (researcher/01)

The record supports every element the commission asked for: cost of capital as
opportunity cost, the after-tax cost of debt and its statutory basis, the cost
of equity as a required (not observed) return with CAPM as the standard
estimation tool, WACC and how its weights are formed, and the ROIC-vs-WACC
value-creation test from an authoritative source. The strongest material is on
what cost-of-equity estimation cannot pin down: Fama and French's own verdict
on CAPM's empirical failure, a live regulatory record (FERC) showing four
competing models producing four different numbers for the same utilities, and
a Supreme Court doctrine (Hope Natural Gas) that defines the required return
in opportunity-cost terms without ever specifying how to compute it. This last
point closes the loop the commission named: "what a company's own regulators
call fair" traces to a 1944 Supreme Court standard, not a formula.

The record is thin in one place: a single, clean, non-anomalous company
numeric example combining a real cost of debt, real weights, and a real WACC
computed step by step. Intel's FY2025 SEC filings give real debt and equity
figures but an unusable, anomalous effective tax rate (98.3%, driven by a
one-time item, not a normal marginal rate) for the after-tax cost of debt
step. Damodaran's live industry-average WACC table is clean and directly
usable for a low-risk/high-risk contrast, but it is a continuously updated
web dataset with no visible "as of" date in the fetched page — a number that
will not match if the page is reopened later, which the writer must flag if
used. The Numbers section records exactly what was captured and when.

## Sources

```
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/costofcapital.pdf
Kind:        Primary — Aswath Damodaran (Kerschner Family Chair in Finance
             Education, NYU Stern) authored this paper; it is his own
             articulation of the cost-of-capital framework, not a report on
             someone else's.
Establishes: "The Cost of Capital: The Swiss Army Knife of Finance" (April
             2016). Establishes firsthand: cost of capital as a weighted
             average of the cost of equity and after-tax cost of debt; the
             cost of capital's three roles (opportunity cost for investors,
             cost of financing for the company, hurdle rate for projects);
             the risk-free rate as the common input to both cost of equity
             and cost of debt; the equity risk premium (ERP) and its two
             estimation approaches (historical vs. implied) with the
             weaknesses of each; the default spread as the debt-side "price
             of risk"; the tax benefit of debt and the rule to use the
             marginal, not effective or book, tax rate; and market-value (not
             book-value) weighting of debt and equity, including why book
             value is "not only irrelevant... but comes with problems that
             can be insurmountable" (about 10% of US companies had negative
             book equity at end of 2015).
Paraphrase:  Cost of capital is one number playing three roles at once: to an
             outside investor it is the return forgone by not putting money
             in an equivalent-risk alternative (opportunity cost); to the
             company raising money it is the cost of financing; to a
             division inside a multi-business company it is the hurdle a
             specific project must clear. Damodaran states plainly that a
             good investment is one that beats the cost of capital,
             "though there is still some disagreement about how best to
             measure the return on an investment" — comparing to ROIC is one
             of the three approaches he names (the others: net present value
             and internal rate of return, both discounting at the cost of
             capital).
Locators:    "The Mechanics" and "Role in Corporate Finance" sections (early
             pages, unnumbered in extraction); "Cost of Equity: Key Inputs" /
             "Risk free Rate" / "The Price of Risk: ERP and Default Spreads"
             sections (mid-paper); "Debt: Its cost and weight" / "The Cost of
             Debt – Current and Consistent" / "The Tax Benefit of Debt" /
             "Debt Weights" / "Market versus Book Value" sections (later
             pages).
Quote:       "For investors in companies, the cost of capital is an
             opportunity cost in the sense that it is the rate of return that
             they would expect to make in other investments of equivalent
             risk." / "There are three simple guides to arriving at the tax
             benefit of debt. The first is to remember that interest expenses
             save you taxes as the margin... leading to the decision to use
             the marginal tax rate (which comes from the tax codes and not
             the company financials)." / "Book value weights are not only
             irrelevant when it comes to cost of capital but come with
             problems that can be insurmountable."

URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/ovhds/ch8.pdf
Kind:        Primary — same author (Damodaran), teaching slides ("Finding the
             Right Financing Mix: The Capital Structure Decision") from his
             NYU Stern corporate finance course.
Establishes: The explicit formulas: WACC = ke(E/(D+E)) + kd(D/(D+E)); cost of
             debt kd = long-term borrowing rate x (1 - tax rate); and the
             sharpest available statement of what cost of equity is and is
             not.
Paraphrase:  Cost of debt is today's market borrowing rate, not the rate
             the company happened to borrow at historically, adjusted down
             for the tax shield on interest. Cost of equity is the required
             rate of return given the risk, inclusive of both dividend yield
             and price appreciation — explicitly not the dividend yield alone
             and not the earnings/price ratio. Weights should be target or
             average weights (not project-specific) and market-value, not
             book-value.
Locators:    Slides 3-9 (in original slide numbering, present in the
             extracted text as "Aswath Damodaran / 3" through "/9").
Quote:       "The cost of equity is / 1. the required rate of return given
             the risk / 2. inclusive of both dividend yield and price
             appreciation // The cost of equity is not / 1. the dividend
             yield / 2. the earnings/price ratio." / "Cost of debt = kd =
             Long Term Borrowing Rate(1 - Tax rate)."

URL:         https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.htm
Kind:        Primary — Damodaran's own continuously updated dataset, computed
             from market data he compiles and publishes himself (not a
             report on someone else's figures).
Establishes: A live table of cost of equity, after-tax cost of debt, D/E
             weights, and WACC for roughly 150 industry groups and a "Total
             Market" aggregate, covering 5,994 firms.
Paraphrase:  As fetched, Utility (General) shows a materially lower cost of
             equity, lower weight of equity, and lower overall WACC than
             Semiconductor or Software (Internet) — a real, sourced
             illustration of a low-risk/high-risk contrast between industries
             without needing a single company's messy one-off numbers. Used
             correctly this replaces a company walkthrough with an industry
             comparison.
Locators:    Table rows "Utility (General)," "Semiconductor," "Semiconductor
             Equip," "Software (Internet)," "Pharmaceutical," "Total Market
             (including financials)."
Quote:       (data table, see Numbers section for exact figures)

URL:         https://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S6B-FamaFrench-CAPM-JEP04.pdf
Kind:        Primary — Eugene Fama and Kenneth French are the researchers
             making these claims about CAPM's empirical performance; this is
             their own paper, not a report on it. (Hosted as a course-site
             mirror; the canonical journal page,
             https://www.aeaweb.org/articles?id=10.1257/0895330042162430,
             confirms the same title, authors, and pagination — Journal of
             Economic Perspectives, Vol. 18, No. 3, Summer 2004, pp. 25-46 —
             and offers the same PDF as a complimentary download.)
Establishes: Firsthand, the authors' own verdict that the Sharpe-Lintner CAPM
             "has never been an empirical success," that the beta-return
             relation is empirically flatter than the model predicts (so
             CAPM cost-of-equity estimates run too high for high-beta stocks
             and too low for low-beta and value stocks), and that even if the
             model held, "the large standard errors of estimates of the
             market premium and of betas for individual stocks probably
             suffice to make CAPM estimates of the cost of equity rather
             meaningless."
Paraphrase:  The paper is explicit that this is a teaching tool, not a
             reliable estimation tool: "We continue to teach the CAPM as an
             introduction to the fundamental concepts of portfolio theory...
             But we also warn students that despite its seductive
             simplicity, the CAPM's empirical problems probably invalidate
             its use in applications." A concrete illustration: using the
             CRSP value-weight portfolio of US stocks and 1927-2003 data, the
             average equity premium is 8.3%/year with a standard error of
             2.4%, so the two-standard-error range runs from 3.5% to 13.1% —
             "sufficient to make most projects appear either profitable or
             unprofitable."
Locators:    Journal of Economic Perspectives 18(3), p. 44 (footnote 7) for
             the standard-error figure; p. 44 for the "seductive simplicity"
             conclusion; p. 33 (Figure 2) for the empirical beta-return plot;
             "The Market Proxy Problem" section for Roll's (1977) critique
             that the CAPM "has never been tested and probably never will
             be," because the true market portfolio is unobservable and
             tests substitute proxies.
Quote:       "The problems are serious enough to invalidate most applications
             of the CAPM." / "The problems are compounded by the large
             standard errors of estimates of the market premium and of betas
             for individual stocks, which probably suffice to make CAPM
             estimates of the cost of equity rather meaningless, even if the
             CAPM holds." / "We also warn students that despite its
             seductive simplicity, the CAPM's empirical problems probably
             invalidate its use in applications."

URL:         https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/comparing-performance-when-invested-capital-is-low
Kind:        Primary for McKinsey's own economic-profit/ROIC-vs-WACC
             framework — this is McKinsey & Company presenting its own
             analytical model (drawn from its "Valuation: Measuring and
             Managing the Value of Companies," which McKinsey's Corporate
             Finance practice authors), not a secondary report on someone
             else's framework.
Establishes: The value-creation test itself, stated directly: value is
             created when ROIC clears the cost of capital.
Paraphrase:  "When managers generate returns on invested capital (ROIC) above
             their cost of capital, they create value." Economic profit
             equals post-tax operating profit minus a capital charge, where
             the capital charge is WACC multiplied by operating invested
             capital — equivalent to (ROIC - WACC) x invested capital. The
             article's specific argument is that this test breaks down for
             businesses with very little invested capital (economic profit
             per dollar of revenue is a better metric there), which is a
             useful boundary condition but not a contradiction of the core
             test.
Locators:    Opening framing paragraphs of the article (no page numbers; web
             article).
Quote:       "when managers generate returns on invested capital (ROIC) above
             their cost of capital, they create value."

URL:         https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/working-hard-for-the-money-the-crunch-on-global-economic-profit
Kind:        Primary, same basis as above — McKinsey presenting its own study
             of its own economic-profit dataset across roughly 4,000 of the
             world's largest public companies by revenue.
Establishes: Concrete magnitudes for the ROIC-WACC spread across company size
             and how concentrated economic profit has become.
Paraphrase:  From 2005 to 2009, the ten largest companies by revenue in the
             sample averaged an 8-point ROIC-WACC spread; the next 90 largest
             averaged 4 points; the smallest 3,500 companies in the same
             4,000-company universe averaged barely more than 1 point. By the
             following decade the smallest group's spread had "approached
             zero," and its share of global economic profit fell from 19% to
             3%. This is a quantified version of the same test McKinsey
             states qualitatively in the companion article above, from a
             named byline (Marc de Jong, Tido Röder, Peter Stumpner, Ilya
             Zaznov), published April 21, 2023.
Locators:    Section "The wider the spread" (opening section of the article).
Quote:       "the average ROIC–WACC spread was 8 percent for the ten largest
             companies, 4 percent for the next 90 largest companies... The
             smallest 3,500 companies by revenue size, on the other hand, had
             a spread that barely exceeded 1 percent."

URL:         https://www.ferc.gov/sites/default/files/2020-05/E-6_71.pdf
Kind:        Primary — this is the Federal Energy Regulatory Commission's own
             order, the agency's own record of its reasoning and method
             choice, in Docket Nos. EL14-12-003 and EL15-45-000 (165 FERC
             P 61,118, issued November 15, 2018, "Order Directing Briefs").
Establishes: Firsthand, that a real regulator setting a real required return
             on equity for real utilities cannot use a single formula and
             get an agreed answer. It shows FERC moving from one model (DCF)
             toward averaging four competing models (DCF, CAPM, an "expected
             earnings" model, and a risk-premium model) because market
             conditions (in this case, historically low bond yields) made the
             Commission "less confiden[t]" that any one model's output was
             reliable.
Paraphrase:  In the underlying rate proceeding, the existing return on equity
             for New England transmission owners was 11.14%; using the DCF
             model's zone of reasonableness, FERC set it to 10.57% instead
             (effective October 16, 2014). The order under discussion here
             proposes to stop relying primarily on DCF and instead average
             the DCF, CAPM, Expected Earnings, and Risk Premium models with
             equal weight, precisely because "relying on the DCF methodology
             alone will not produce a just and reasonable ROE" given current
             conditions. This is a live, high-stakes instance of "cost of
             equity is estimated, not observed": four standard models, four
             different numbers, and a regulator averaging them rather than
             picking the "true" one.
Locators:    Pages 4-5 (background on Opinion No. 531/531-A and the 10.57%
             ROE); pages ~35-36 in the extracted text ("Determining a Just
             and Reasonable ROE," "Use of Multiple Financial Models"
             sections) for the four-model proposal and the Hope quotation.
Quote:       "we believe that, in light of current investor behavior and
             capital market conditions, relying on the DCF methodology alone
             will not produce a just and reasonable ROE. Instead, we propose
             to rely upon the results of all four financial models in the
             records for these proceedings: the DCF, CAPM, Expected
             Earnings, and Risk Premium models." / "In Hope, the Supreme
             Court held that 'the return to the equity owner should be
             commensurate with returns on investments in other enterprises
             having corresponding risks.'"

URL:         https://caselaw.findlaw.com/court/us-supreme-court/320/591.html
Kind:        Primary — the U.S. Supreme Court's own opinion in Federal Power
             Commission v. Hope Natural Gas Co., 320 U.S. 591 (1944).
Establishes: The doctrinal source of "what a company's own regulators call
             fair," cited by the commission as the prior ROIC lesson's
             closing hurdle. States the opportunity-cost standard for a
             utility's allowed return in the Court's own words, not a
             restatement.
Paraphrase:  A utility's allowed return on equity must be comparable to what
             an investor could earn on other investments of similar risk, and
             must be enough to preserve the company's financial health and
             ability to raise capital. The Court sets the standard in
             opportunity-cost terms without specifying any estimation method
             — the "how" (DCF, CAPM, or otherwise) was left to regulators and
             has been contested ever since, as the FERC order above shows.
Locators:    320 U.S. 591, 603.
Quote:       "By that standard the return to the equity owner should be
             commensurate with returns on investments in other enterprises
             having corresponding risks. That return, moreover, should be
             sufficient to assure confidence in the financial integrity of
             the enterprise, so as to maintain its credit and to attract
             capital."

URL:         https://uscode.house.gov/view.xhtml?req=%28title%3A26+section%3A163+edition%3Aprelim%29
Kind:        Primary — the actual codified text of 26 U.S.C. Section 163, the
             statutory basis for interest deductibility.
Establishes: The general rule that interest is deductible, firsthand from
             the statute, plus the heading of the limitation that qualifies
             it.
Paraphrase:  Section 163(a) states the general rule in one sentence. Section
             163(j), "Limitation on business interest," caps how much
             business interest expense is deductible in a year, generally at
             business interest income plus 30% of adjusted taxable income
             plus floor-plan financing interest, with disallowed amounts
             carried forward indefinitely.
Locators:    26 U.S.C. Section 163(a); Section 163(j) heading and cap
             structure.
Quote:       "There shall be allowed as a deduction all interest paid or
             accrued within the taxable year on indebtedness."

URL:         https://www.irs.gov/newsroom/questions-and-answers-about-the-limitation-on-the-deduction-for-business-interest-expense
Kind:        Primary — the IRS is the administering agency describing its own
             rule application, not a third party interpreting it.
Establishes: Plain-language confirmation of the general deductibility rule
             and the mechanics of the 163(j) cap (30% of adjusted taxable
             income, plus carryforward of any disallowed amount).
Paraphrase:  For teaching purposes: most large, profitable companies' actual
             interest expense sits comfortably under the 30%-of-ATI cap, so
             "after-tax cost of debt = pretax rate x (1 - tax rate)" is a
             fair simplification unless a firm is highly levered relative to
             its income — a caveat worth stating rather than assuming away.
Locators:    "Q1" (general rule) and the paragraph describing the 30% ATI
             computation.
Quote:       "Generally, taxpayers can deduct interest expense paid or
             accrued in the taxable year."

URL:         https://www.sec.gov/Archives/edgar/data/50863/000005086326000009/q425earningsrelease.htm
Kind:        Primary — Intel Corporation's own Q4/FY2025 earnings release,
             filed as Exhibit 99.1 to a Form 8-K with the SEC (filed on or
             about January 22, 2026, covering the fiscal year ended December
             27, 2025). This is the company's own disclosure of its own
             results.
Establishes: Real, filed figures for a capital-intensive company: debt
             outstanding, tax provision and pretax income, stockholders'
             equity, and capital expenditures, plus the headline result that
             Intel posted a full-year net loss in FY2025.
Paraphrase:  Intel's FY2025 numbers make a vivid, real illustration of "the
             hurdle obviously bites": a full-year net loss (EPS attributable
             to Intel of $(0.06)) alongside $14.6 billion in gross capital
             spending, on a company carrying $46.6 billion in total debt.
             Whatever Intel's actual ROIC works out to for the year, a
             company posting a net loss cannot be clearing any positive cost
             of capital — value was destroyed, not created, in the period.
             The one figure that is NOT safely usable is the effective tax
             rate: provision for taxes of $1,531 million against income
             before taxes of only $1,557 million implies a 98.3% effective
             rate, an obvious anomaly (consistent with a large one-time
             charge, e.g. a valuation allowance against deferred tax assets)
             rather than Intel's ordinary marginal or effective tax rate. Do
             not use FY2025's effective rate for an after-tax-cost-of-debt
             calculation; either use the US federal statutory corporate rate
             (21%, per IRC Section 11) or flag the anomaly explicitly if
             citing Intel's actual FY2025 figure.
Locators:    Condensed consolidated balance sheet (short-term debt, long-term
             debt, total stockholders' equity lines); condensed consolidated
             statement of income (provision for taxes, income before taxes,
             EPS lines); condensed consolidated statement of cash flows
             (additions to property, plant and equipment; government
             incentives; partner contributions lines).
Quote:       (tabular figures; see Numbers section)
```

## Contradictions

- Fama and French's own conclusion directly contradicts the textbook
  prescription they describe: finance textbooks "often recommend using the
  Sharpe-Lintner CAPM risk-return relation to estimate the cost of equity
  capital," yet the same authors conclude the model's "empirical problems
  probably invalidate its use in applications." CAPM remains the standard
  taught tool (confirmed by Damodaran's practitioner treatment and by FERC's
  own regulatory practice) precisely because no superior single alternative
  has displaced it, not because its problems were resolved. This is a real
  tension the lesson should state plainly rather than smooth over: the
  standard tool is standard by convention and by the absence of a better
  alternative, not because it is known to be accurate.
- Standard corporate-finance teaching (Damodaran) treats cost of equity as
  something a company or analyst estimates once from public market data.
  FERC's actual regulatory practice shows the opposite: for the same set of
  utilities in the same proceeding, four standard models (DCF, CAPM, Expected
  Earnings, Risk Premium) are run in parallel and produce different point
  estimates, which the Commission then averages rather than choosing among.
  This is not a disagreement between sources about a fact; it is documented
  proof that the estimation step itself does not converge on one number even
  among expert practitioners using the standard toolkit on the same company
  at the same time.
- No contradiction found on the core mechanics: every source consulted
  (Damodaran's two documents, the McKinsey pieces, the FERC order) agrees
  that market values, not book values, should weight debt and equity, and
  that interest's tax deductibility is what makes the after-tax cost of debt
  lower than the pretax borrowing rate. Searched specifically for a
  dissenting view on market-vs-book weighting and did not find one among the
  sources read.

## Numbers

```
Figure: WACC = ke x (E/(D+E)) + kd x (D/(D+E))
Owner:  Aswath Damodaran, "Finding the Right Financing Mix" (NYU Stern
        course slides)
Scope:  General formula, not company- or period-specific.

Figure: Cost of debt (kd) = long-term borrowing rate x (1 - tax rate)
Owner:  Aswath Damodaran, "Finding the Right Financing Mix"
Scope:  General formula; Damodaran's companion paper specifies the marginal
        (statutory) tax rate, not the effective or book rate, should be used.

Figure: Historical US equity risk premium standard error: average 8.3%/year,
        standard error 2.4%, two-standard-error range 3.5% to 13.1%
Owner:  Fama and French (2004), Journal of Economic Perspectives 18(3), p.
        44, footnote 7
Scope:  US equity premium over the T-bill rate, CRSP value-weight portfolio
        of publicly traded US common stocks, 1927-2003.

Figure: Damodaran's January 2016 implied equity risk premium for the S&P 500:
        6.12%
Owner:  Aswath Damodaran, "The Cost of Capital: The Swiss Army Knife of
        Finance" (2016)
Scope:  S&P 500, forward-looking implied premium as of January 2016 — an
        illustration of the implied-ERP method, not a current figure. Do not
        present as today's premium.

Figure: FERC-set base ROE for New England transmission owners: 10.57%,
        replacing an existing 11.14% ROE
Owner:  FERC, Opinion No. 531 / 531-A (referenced in 165 FERC P 61,118 at
        pp. 4-5)
Scope:  New England transmission-owning utilities, effective October 16,
        2014. A single regulatory determination, not a market-wide figure.

Figure: Damodaran live industry cost-of-capital table (fetched August 2,
        2026):
          Utility (General):   cost of equity 5.02%, after-tax cost of debt
                                3.55%, E/(D+E) 55.10%, D/(D+E) 44.90%,
                                WACC 4.36%
          Semiconductor:       cost of equity 10.72%, after-tax cost of debt
                                3.97%, E/(D+E) 97.47%, D/(D+E) 2.53%,
                                WACC 10.55%
          Software (Internet): cost of equity 11.48%, after-tax cost of debt
                                3.97%, E/(D+E) 89.05%, D/(D+E) 10.95%,
                                WACC 10.66%
          Total Market (incl. financials): cost of equity 8.02%, after-tax
                                cost of debt 3.97%, E/(D+E) 73.98%,
                                D/(D+E) 26.02%, WACC 6.96%
Owner:  Aswath Damodaran, live datafile at pages.stern.nyu.edu/~adamodar/
        New_Home_Page/datafile/wacc.htm
Scope:  Industry aggregates across thousands of firms (Damodaran states
        5,994 firms across the full dataset). IMPORTANT: the fetched page
        showed no visible "as of" date. This is a continuously updated
        dataset — if used, the writer must state the access date and expect
        the numbers to drift (possibly materially) if the page is reopened
        later, e.g. at editing time.

Figure: ROIC-WACC spread by company size, 2005-2009: 8 points (ten largest
        companies), 4 points (next 90 largest), just over 1 point (smallest
        3,500 companies); the smallest group's spread "approached zero" the
        following decade and its share of global economic profit fell from
        19% to 3%
Owner:  McKinsey & Company, "Working hard for the money: The crunch on
        global economic profit" (de Jong, Röder, Stumpner, Zaznov; April 21,
        2023)
Scope:  A sample of the world's roughly 4,000 largest public companies by
        revenue; McKinsey's own economic-profit dataset, not an independent
        academic study.

Figure: Intel Corporation FY2025 (year ended December 27, 2025): short-term
        debt $2,499 million, long-term debt $44,086 million (total ~$46,585
        million); provision for taxes $1,531 million on income before taxes
        of $1,557 million (implied effective rate ~98.3%, anomalous — see
        Sources); total stockholders' equity $126,360 million; gross capital
        expenditures $14,646 million, net of $1,577 million in government
        incentives and $4,891 million in partner contributions (~$8,178
        million net); full-year EPS attributable to Intel $(0.06) (net loss)
Owner:  Intel Corporation, Q4/FY2025 earnings release, Exhibit 99.1 to Form
        8-K filed with the SEC (~January 22, 2026)
Scope:  Intel Corporation, consolidated, fiscal year ended December 27,
        2025 (52-week year beginning December 30, 2024).

Figure: US federal statutory corporate income tax rate: 21%
Owner:  26 U.S.C. Section 11 (referenced for context; not separately read in
        full — flagged here because it is the safer rate to use in place of
        Intel's anomalous FY2025 effective rate if a marginal-tax-rate figure
        is needed for a worked after-tax-cost-of-debt example)
Scope:  US federal corporate rate, current law as of this research; state
        and local taxes are additional and vary by jurisdiction.
```

Note on the last line: Section 11's rate was not independently opened and
read for this record (it was not one of the URLs fetched); it is included
only as a well-known figure for the writer's/editor's awareness and should
not be cited to this evidence record without a researcher or writer opening
the statute directly. Every other figure above was read at its stated URL.

## Source assets

```
Asset: Fama and French (2004), Figure 2, "Average Annualized Monthly Return
       versus Beta for Value Weight Portfolios Formed on Prior Beta,
       1928-2003" (p. 33 of the JEP article)
Shows: Ten beta-sorted stock portfolios plotted by realized average return
       against beta, against the straight line the Sharpe-Lintner CAPM
       predicts. The actual relation is visibly flatter than the predicted
       line — high-beta portfolios earn less than CAPM says they should,
       low-beta portfolios earn more.
Crop:  Must retain both the predicted CAPM line and the actual plotted
       points/fitted line together — the mismatch between the two is the
       entire point. Must retain axis labels (average return, beta) and the
       time period in the caption. Omitting the predicted line would turn a
       falsification chart into a decorative scatterplot.

Asset: Damodaran's live industry cost-of-capital table (wacc.htm), rows for
       Utility (General) and Semiconductor (or another contrasting pair)
Shows: Side by side, a low-risk and high-risk industry's full WACC build:
       cost of equity, after-tax cost of debt, capital-structure weights,
       and the resulting WACC — a real, sourced version of exactly the
       "clean contrast between a low-risk and high-risk firm" the commission
       invites, without needing a single company's filings.
Crop:  If rebuilt as the lesson's own table, must carry the access date
       (this is live data, not a fixed historical figure) and should not
       silently mix rows fetched on different dates.

Asset: None found in the McKinsey articles, the FERC order, the Hope opinion,
       the IRS/IRC pages, or Intel's earnings release beyond their own
       standard financial-statement tables (which are numeric evidence
       already captured in Numbers, not standalone visual arguments).
```

## Discarded

```
URL: https://www.ferc.gov/news-events/news/ferc-revises-public-utility-roe-methodology-sets-policy-natural-gas-oil-pipelines
     Returned HTTP 403 Forbidden (gated, not dead). Not retried with a
     different request style because the substantive content — the same
     ROE-methodology reasoning — was available and read directly in the
     underlying order, 165 FERC P 61,118, which resolved normally.

URL: https://supreme.justia.com/cases/federal/us/320/591/
     Returned HTTP 403 Forbidden (gated, not dead). Substituted with
     https://caselaw.findlaw.com/court/us-supreme-court/320/591.html, which
     resolved and carries the same opinion text.

URL: https://www.sec.gov/Archives/edgar/data/50863/000005086326000011/intc-20251227.htm
     Opened (Intel's full FY2025 Form 10-K). Resolved, but the specific
     financial-statement figures needed were not visible in the fetched
     excerpt of this large document. Superseded by Intel's Q4/FY2025
     earnings release (Exhibit 99.1 to Form 8-K), a shorter primary SEC
     filing that contains the same audited-basis figures in a directly
     readable form.
```
