# Evidence: investing/present-value (researcher 02)

This record carries forward all still-valid round-01 work and raises the lesson to
**eight citable source entries** (two new independent authorities beyond the four
opened in round 01). It sources everything the lesson's teaching spine needs: the
definition of the time value of money and present value, the single-cash-flow
discounting identity PV = CF/(1+r)^t, multi-period PV as a sum, the perpetuity form
PV = CF/r, and the growing-perpetuity shortcut PV = CF/(r-g). Each load-bearing
claim now has at least two independent owners. The formulas come from Aswath
Damodaran (NYU Stern) and are independently corroborated by OpenStax *Principles of
Finance* (Rice University peer-reviewed OER) and, for the perpetuity forms, by Bigel,
*Introduction to Financial Analysis*. The real discount-rate anchor is now owned by
two independent institutions: the U.S. Department of the Treasury (10-year par yield
**4.75% as of 07/31/2026**) and the Board of Governors of the Federal Reserve via
FRED (10-year constant-maturity yield **4.68% as of 07/30/2026**). Round 01 flagged
one gap as its most important limitation: no source owned the "discount rate = cost
of capital = risk-free rate + risk premium" claim that the commission's WACC linkage
rests on. **That gap is now filled** by OpenStax 15.3 (CAPM), which owns the
required-return buildup Re = Rf + risk premium and names US Treasury securities as
the risk-free proxy. The evidence is strong and uncontested on the formulas
themselves (standard mathematical results, not contested claims). The remaining care
point is unchanged: the Treasury/FRED yield is a **risk-free** rate, the floor
beneath a company's cost of capital, not the cost of capital itself. The worked-table
cash flows the commission calls for remain teaching inventions; only the discount
rate carries a real citation. See Contradictions.

## Sources

```text
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/acf4E/presentations/timevalue.pdf
Kind:        Primary (authoritative). Authored by Aswath Damodaran (Professor of
             Finance, NYU Stern School of Business); it is his own exposition and
             owns these definitions and worked examples. The formulas themselves
             are standard results; this source is the authority stating them.
Establishes: The intuition and definition of present value, the discount rate and
             its role, and every formula the lesson needs.
Paraphrase:  A dollar tomorrow is worth less than a dollar today for three reasons:
             people prefer present to future consumption, inflation erodes currency,
             and future cash flows carry uncertainty (risk). The discount rate is
             the mechanism that factors these in, and it is also an opportunity cost
             capturing the return available on the next best alternative. Cash flows
             at different points in time cannot be compared or added until brought
             to the same point in time. The present value of a single future cash
             flow is that cash flow divided by (1+r) raised to the number of periods.
             A perpetuity is a constant cash flow forever, valued at A/r; a growing
             perpetuity grows at a constant rate forever, valued at CF1/(r-g).
Locators:    Slide 2 "Intuition Behind Present Value" (three reasons); slide 3
             "Discounting and Compounding" (discount rate incorporates the three
             factors; is also an opportunity cost); slide 4 "Present Value Principle
             1" (cash flows must be brought to a common point in time); slide 7
             "I. Simple Cash Flows" (PV = CFt / (1+r)^t; FV = CF0 (1+r)^t); slide 32
             "IV. Perpetuity" (PV of Perpetuity = A/r); slide 34 "V. Growing
             Perpetuities" (PV = CF1/(r-g), CF1 = expected cash flow next year, g =
             constant growth rate, r = discount rate); slide 35 "Valuing a Stock
             with Growing Dividends" (worked Con Ed example). Simplification signals
             on slide 20 ("invest, after taxes, at 8%") and slide 24 ("We've ignored
             taxes in this analysis. How would it impact your decision?").
Quote:       Slide 7: "PV of Simple Cash Flow = CFt / (1+r)t". Slide 34: "PV of
             Growing Perpetuity = CF1 / (r - g)". Slide 3: "The discount rate is
             also an opportunity cost, since it captures the returns that an
             individual would have made on the next best opportunity."
```

```text
URL:         https://openstax.org/books/principles-finance/pages/9-1-timing-of-cash-flows
Kind:        Primary/authoritative. OpenStax *Principles of Finance* (Rice
             University), a peer-reviewed open textbook. It owns this statement of
             the discounting identity and the multi-cash-flow method as a textbook
             authority, independent of Damodaran, Bigel, and CFI. The formula is a
             standard result; this source is a second recognized authority stating
             it.
Establishes: Independent second owner of the core PV identity PV = FV / (1+i)^n and
             of the requirement that unequal cash flows at different dates each be
             discounted and then summed to a single present value today. This is the
             exact operation the commission's "small worked table discounting a few
             years of cash flows" performs.
Paraphrase:  The present value of a single future amount is that amount multiplied
             by 1/(1+i)^n, where i is the periodic interest rate and n the number of
             periods; bringing future values back in time this way is called
             discounting, the inverse of compounding. When cash flows of different
             sizes occur in different years, each is discounted individually with the
             single-amount formula and the results are added to give the total
             present value required today (demonstrated with an unequal-withdrawal
             lottery example across years 1-5).
Locators:    Section 9.1 "Timing of Cash Flows." Equation 9.12: PV = FV x 1/(1+i)^n.
             Worked unequal-cash-flow (lottery) example following the equation.
Quote:       "PV = FV x 1/(1 + i)^n" (Equation 9.12). "In this case, we're bringing
             future values back in time to find their present values. You will recall
             that this process is called discounting rather than compounding."
```

```text
URL:         https://openstax.org/books/principles-finance/pages/8-1-perpetuities
Kind:        Primary/authoritative. OpenStax *Principles of Finance* (Rice
             University), peer-reviewed OER. A second corporate-finance textbook
             authority for the perpetuity and growing-perpetuity forms, independent
             of Damodaran and Bigel.
Establishes: Independent corroboration of the constant-perpetuity value PV = C/Rs and
             the growing-perpetuity value PV = C/(Rs - G), and of the definitions of
             a constant vs. a growing perpetuity. Sets up terminal/continuing value.
Paraphrase:  A perpetuity is a stream of periodic payments expected to continue
             indefinitely. A constant perpetuity pays the same amount forever and is
             valued as the periodic cash flow divided by the required rate of return.
             A growing perpetuity's payment increases by a fixed percentage each
             period and is valued as the cash flow divided by the required return
             minus the growth rate. An indefinite payment stream cannot be compounded
             to a future value but can be discounted to a present value, which is what
             an investor should be willing to pay for it.
Locators:    Section 8.1 "Perpetuities." Equation 8.1 (constant perpetuity):
             PV = C / Rs. Equation 8.3 (growing perpetuity): PV = C / (Rs - G).
Quote:       Equation 8.1: PV = C / Rs. Equation 8.3: PV = C / (Rs - G).
Note:        OpenStax notation differs from Damodaran/Bigel: C is the (constant or
             next-period) cash flow / dividend, Rs is the required rate of return
             (r elsewhere in this record), and G is the growth rate (g elsewhere).
             The automated page render dropped the fraction bars ("PV=CRs",
             "PV=CRs-G"); the correct forms are PV = C/Rs and PV = C/(Rs-G), matching
             Damodaran (A/r; CF1/(r-g)) and Bigel. The lesson should use one
             notation consistently and not mix OpenStax's Rs/G with Damodaran's r/g.
```

```text
URL:         https://openstax.org/books/principles-finance/pages/15-3-the-capital-asset-pricing-model-capm
Kind:        Primary/authoritative. OpenStax *Principles of Finance* (Rice
             University), peer-reviewed OER. Owns, as a textbook authority, the
             required-return buildup on which the commission's WACC linkage depends.
Establishes: The claim round 01 could not source: a discount rate (required return)
             is the risk-free rate PLUS a risk premium, and US Treasury securities
             are the standard proxy for the risk-free rate. This is what lets the
             lesson connect the Treasury/FRED anchor to the cost of capital taught in
             the prior WACC lesson without conflating the two.
Paraphrase:  Investors will hold a risky asset only if compensated above what they
             could earn risk-free, so the required (expected) return equals the
             risk-free rate plus a risk premium. Under the capital asset pricing
             model the premium is the asset's beta times the market risk premium, so
             Re = Rf + beta x (Rm - Rf). The return available on US Treasury
             securities is the proxy used for the risk-free rate Rf.
Locators:    Section 15.3 "The Capital Asset Pricing Model (CAPM)." Equation 15.12:
             Re = Rf + beta x (Rm - Rf) (equivalently Re = Rf + beta x Market Risk
             Premium). Worked example (Equation 15.13) applies it to DAL stock.
Quote:       "The rate that you can earn by purchasing US Treasury securities is a
             proxy for the risk-free rate." Equation 15.12: "Re = Rf + Beta x
             (Rm - Rf)."
```

```text
URL:         https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026
Kind:        Primary. The U.S. Department of the Treasury owns and publishes the
             Daily Treasury Par Yield Curve Rates.
Establishes: A real, current discount-rate anchor: the 10-year U.S. Treasury par
             yield, with the full curve for the latest trading day.
Paraphrase:  On the most recent trading day in the 2026 table, 07/31/2026, the
             Treasury par yield curve reads 4.08% at 1 year, 4.28% at 2 years, 4.45%
             at 5 years, 4.75% at 10 years, and 5.27% at 30 years. These are
             constant-maturity par yields interpolated from the Treasury's daily
             yield curve based on secondary-market closing bid quotations.
Locators:    "Daily Treasury Par Yield Curve Rates" table, final (most recent) row,
             07/31/2026. Today is 2026-08-03 (Monday); 07/31 (Friday) is the last
             trading day, so it is the current reading as of the run date.
Quote:       (data row, exact) "07/31/2026, ... 1 Yr 4.08, 2 Yr 4.28, 3 Yr 4.34,
             5 Yr 4.45, 7 Yr 4.59, 10 Yr 4.75, 20 Yr 5.28, 30 Yr 5.27"
Note:        Exact figures were verified from the Treasury's own CSV data endpoint
             (.../daily-treasury-rates.csv/2026/all?...&_format=csv), because the
             rendered HTML table was misread by an automated summarizer on two
             attempts (see Contradictions). The human-readable page above is the
             address to cite; the CSV was the verification transport, not the source.
```

```text
URL:         https://fred.stlouisfed.org/series/DGS10
Kind:        Primary. FRED (Federal Reserve Economic Data), Federal Reserve Bank of
             St. Louis, publishing the series whose underlying source is the Board of
             Governors of the Federal Reserve System (H.15). This is an institution
             INDEPENDENT of the U.S. Treasury, so it is a second, independent owner
             of "the 10-year Treasury rate" anchor the lesson uses.
Establishes: A second, independent real anchor for the 10-year U.S. Treasury yield:
             the constant-maturity market yield on an investment basis, 4.68% on
             07/30/2026, the latest observation available in the run window.
Paraphrase:  The DGS10 series is the market yield on U.S. Treasury securities at
             10-year constant maturity, quoted on an investment basis, sourced from
             the Board of Governors of the Federal Reserve System and published daily
             in percent (not seasonally adjusted). Constant-maturity yields are
             derived from the Treasury yield curve per the Treasury Yield Curve
             Methodology. The most recent observation is 4.68% on 07/30/2026.
Locators:    Series page DGS10, "Market Yield on U.S. Treasury Securities at 10-Year
             Constant Maturity, Quoted on an Investment Basis," latest observation
             row (07/30/2026 = 4.68).
Quote:       Series title: "Market Yield on U.S. Treasury Securities at 10-Year
             Constant Maturity, Quoted on an Investment Basis." Source: "Board of
             Governors of the Federal Reserve System (US)."
Note:        Values verified from FRED's own data download
             (fredgraph.csv?id=DGS10, window 2026-07-20..2026-08-01): 07/24 4.69,
             07/27 4.65, 07/28 4.61, 07/29 4.67, 07/30 4.68 (07/31 not yet posted in
             that pull). The series page above is the address to cite; the CSV was the
             verification transport. DGS10 (constant-maturity, investment basis) and
             the Treasury par yield are two slightly different constructions of the
             10-year rate on adjacent days, which is why 4.68% and 4.75% differ; see
             Contradictions.
```

```text
URL:         https://biz.libretexts.org/Bookshelves/Finance/Introduction_to_Financial_Analysis_(Bigel)/03%3A_Part_III-_The_Time_Value_of_Money/11%3A_The_Time_Value_of_Money-_Annuities_Perpetuities_and_Mortgages/11.20%3A_Growth_Perpetuities
Kind:        Primary/authoritative for the definitional statement (open academic
             textbook: Kenneth S. Bigel, "Introduction to Financial Analysis,"
             hosted on LibreTexts). Independent of Damodaran and OpenStax.
Establishes: Independent confirmation of the growing-perpetuity formula and its
             required constraint, plus the ordinary-perpetuity form as the g=0 case.
Paraphrase:  The present value of a growing perpetuity is the next-period cash flow
             divided by (r - g). For the formula to work, g cannot equal or exceed
             r, or the denominator turns zero or negative and the value becomes
             meaningless. The ordinary (no-growth) perpetuity is the special case
             g = 0, collapsing to PV = CF/r.
Locators:    Section 11.20 "Growth Perpetuities."
Quote:       "PV = CF1 / (r - g)"; "for this formula to work, 'g' cannot equal or
             exceed 'r.'"
```

```text
URL:         https://corporatefinanceinstitute.com/resources/valuation/time-value-of-money/
Kind:        Secondary (educational explainer, Corporate Finance Institute).
             Acceptable for context and a plain-language definition; not the owner
             of the concept.
Establishes: A plain restatement of the time-value definition and the discounting
             direction, useful only as a second, accessible gloss.
Paraphrase:  Money in the present is worth more than the same sum received in the
             future, because money in hand can be invested to earn a return. Present
             value is found by dividing a future amount by the interest-rate factor
             raised to the number of periods, the inverse of compounding.
Locators:    "Time Value of Money" resource page, definition and worked
             single-period example.
Quote:       "Money in the present is worth more than the same sum of money to be
             received in the future."
```

## Contradictions

- **The real anchor is a risk-free rate; the commission's framing is a cost of
  capital. (Now partly resolvable.)** The commission says "The discount rate is the
  cost of capital from the prior lesson" (WACC) and asks to connect them. The only
  real, current rates this record can source are the 10-year Treasury par yield
  (4.75%, 07/31/2026) and the 10-year FRED constant-maturity yield (4.68%,
  07/30/2026), both **risk-free** rates, not a firm's cost of capital. Round 01
  could not source the bridge between them. Round 02 can: OpenStax 15.3 owns the
  buildup Re = Rf + risk premium and names US Treasury securities as the risk-free
  proxy, and Damodaran (slide 3) treats the discount rate as incorporating
  uncertainty/risk on top of pure time and inflation preference. So the honest move
  is now fully citable: present the 10-year Treasury/FRED yield as the risk-free
  anchor (Rf), and state that a company's cost of capital adds a risk premium on top
  (the WACC/CAPM lesson), citing OpenStax 15.3. Do NOT discount risky business cash
  flows at 4.68-4.75% flat and call it "the cost of capital"; that would contradict
  the prior WACC lesson. This remains the record's most important care point, but it
  is no longer an unsourced gap.

- **Two owners of "the 10-year Treasury rate" report slightly different numbers.**
  Treasury's Daily Par Yield Curve gives 4.75% at the 10-year point on 07/31/2026;
  FRED's DGS10 (Board of Governors constant-maturity, investment basis) gives 4.68%
  on 07/30/2026. This is not an error: they are two different constructions (par
  yield vs. constant-maturity investment-basis yield) on adjacent trading days. The
  lesson needs only one real anchor; cite one owner for the figure it uses and, if
  both are mentioned, attribute each number to its owner and date rather than
  presenting a single "the" 10-year rate.

- **r > g is a hard constraint, not a footnote.** Damodaran (slide 29, the
  growing-annuity edge case where g = r), Bigel (explicitly, section 11.20), and
  OpenStax (growing-perpetuity denominator Rs - G, section 8.1) all require the
  growth rate to stay strictly below the discount rate. Any worked perpetuity number
  in the lesson must keep g < r, or the shortcut produces a zero/negative denominator
  and a nonsensical value.

- **Automated table-reads disagreed; the primary resolved it.** Two automated fetches
  of the Treasury HTML table returned conflicting 10-year values for 07/31/2026 (one
  reported 4.08%, another 4.75%) because the summarizer misaligned columns (4.08% is
  in fact the 1-year yield). The Treasury CSV settles it: 10 Yr = 4.75%. Similarly,
  the OpenStax 8.1 render dropped fraction bars (rendering PV = C/Rs as "PV=CRs");
  the correct division is confirmed by the equation numbering and by Damodaran/Bigel.
  Recorded so the editor does not reintroduce either misread.

## Numbers

```text
Figure: 4.75% (10-year U.S. Treasury par yield)
Owner:  U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates
Scope:  Constant-maturity par yield, 10-year point, as of 07/31/2026 (latest
        trading day before the 2026-08-03 run). Annualized percent. This is a
        risk-free benchmark rate, not a company cost of capital.
```

```text
Figure: 4.68% (10-year U.S. Treasury constant-maturity yield, investment basis)
Owner:  Board of Governors of the Federal Reserve System, via FRED series DGS10
Scope:  10-year constant-maturity market yield, investment basis, 07/30/2026 (latest
        observation in the run-window pull). Annualized percent, not seasonally
        adjusted. An independent second owner of the same 10-year Treasury anchor;
        differs from the Treasury par yield (4.75%) by construction and by one day.
        Also a risk-free benchmark, not a company cost of capital.
```

```text
Figure: Full Treasury curve on 07/31/2026 (for context / optional chart)
Owner:  U.S. Department of the Treasury
Scope:  1 Yr 4.08%, 2 Yr 4.28%, 3 Yr 4.34%, 5 Yr 4.45%, 7 Yr 4.59%,
        10 Yr 4.75%, 20 Yr 5.28%, 30 Yr 5.27%. Same date and basis as above.
        Note the near-inversion at the very long end (20 Yr above 30 Yr).
```

```text
Figure: DGS10 daily series, late July 2026 (for context / optional chart)
Owner:  Board of Governors of the Federal Reserve System, via FRED series DGS10
Scope:  07/24 4.69%, 07/27 4.65%, 07/28 4.61%, 07/29 4.67%, 07/30 4.68%. Daily,
        percent. Verified from FRED's own CSV. Useful if the lesson wants a short
        time series behind the discount-rate anchor rather than a single reading.
```

```text
Figure: Con Ed growing-perpetuity worked example (from Damodaran, if reused)
Owner:  Aswath Damodaran, "The Time Value of Money," slide 35
Scope:  Trailing dividend per share $2.52; long-run growth g = 2%; required return
        r = 7.50%. Value = 2.52 x (1.02) / (0.075 - 0.02) = $46.73 per share.
        This is Damodaran's illustration, dated to Jan 2014, not a current quote;
        use it only as a formula demonstration, not a live valuation. The
        commission also asks to avoid a single-company default, so prefer a generic
        cash-flow table and keep this as at most a formula check.
```

```text
Figure: Worked discounting-table cash flows (to be chosen by the writer)
Owner:  None — these are teaching inventions, not sourced real figures.
Scope:  The commission asks for "a small worked table discounting a few years of
        cash flows at a stated rate." Any level (e.g., a level $100/yr for a few
        years, mirroring Damodaran's slide-5 timeline, or unequal flows like the
        OpenStax 9.1 example) is a legitimate teaching choice. Only the discount
        rate carries a real-world citation (the Treasury or FRED anchor). State
        in-text that the cash flows are illustrative.
```

## Source assets

```text
Asset: Damodaran slide 7 "I. Simple Cash Flows" — the boxed identity
       PV of Simple Cash Flow = CFt / (1+r)t.
Shows: The core discounting identity in the authority's own hand; supports the
       commission's request for an annotated equation of the PV identity.
Crop:  The lesson should render its own annotated equation (per template furniture),
       not screenshot the slide. Use the slide only to confirm notation (CFt, r, t).
```

```text
Asset: Damodaran slide 34 "V. Growing Perpetuities" — PV of Growing Perpetuity
       = CF1 / (r - g), with CF1, g, r defined beneath.
Shows: The perpetuity shortcut and its exact variable definitions; sets up the
       terminal-value idea the commission wants introduced but not fully built.
Crop:  Reproduce as the lesson's own equation; the slide confirms that CF1 is the
       NEXT-year cash flow (a common student error is using this year's).
```

```text
Asset: OpenStax 9.1 "Timing of Cash Flows" — the unequal-cash-flow worked example
       (lottery withdrawals across years 1-5, each discounted then summed).
Shows: The multi-period "discount each flow, then add" operation the commission's
       worked table performs, from an independent textbook authority.
Crop:  Do not reproduce OpenStax's table; the lesson builds its own worked table.
       Use only to confirm the method and Equation 9.12 notation (i, n).
```

```text
Asset: U.S. Treasury Daily Par Yield Curve Rates table (07/31/2026 row) and/or the
       FRED DGS10 daily series chart.
Shows: A real, current term structure / time series of risk-free rates. If the
       lesson wants a chart, either the 07/31 Treasury curve across maturities or the
       FRED DGS10 daily series is the honest, citable data behind the figure.
Crop:  A chart must be rendered from committed chart-N.py per spec/charts.md, label
       axes, and cite its owner in the caption ("U.S. Department of the Treasury,
       Daily Treasury Par Yield Curve Rates" or "Board of Governors of the Federal
       Reserve System, FRED series DGS10"). Do not hand-draw or screenshot. Do not
       mix the two owners' numbers into one unattributed line.
```

## Discarded

```text
URL: https://openstax.org/books/principles-finance/pages/7-2-time-value-of-money-tvm-basics
     — OpenStax's TVM-basics page states the FUTURE value form (FV = PV(1+r)^n,
     Equation 7.9) but not the present-value/discounting form; superseded for this
     lesson by OpenStax 9.1, which owns PV = FV/(1+i)^n directly. Read but not cited.
URL: https://www.scribd.com/document/55001902/Time-Value-of-Money-Damodaran — a
     re-host of Damodaran's material behind a login wall; the primary NYU Stern PDF
     is the source of record, so the mirror adds nothing and should not be cited.
URL: https://www.wallstreetprep.com/knowledge/growing-perpetuity/ and
     financeformulas.net — commercial explainers that merely restate the standard
     growing-perpetuity formula; superseded by Damodaran, OpenStax, and Bigel. Not
     needed and weaker than what is kept.
URL: https://www.studocu.com/.../a-primer-on-the-time-value-of-money — student
     re-upload of Damodaran's primer; use the original.
```
