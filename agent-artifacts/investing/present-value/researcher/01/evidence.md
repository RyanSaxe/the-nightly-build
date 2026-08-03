# Evidence: investing/present-value (researcher 01)

This record sources everything the lesson's teaching spine needs: the definition
of the time value of money and present value, the single-cash-flow discounting
identity PV = CF/(1+r)^t, the perpetuity form PV = CF/r, and the growing-perpetuity
shortcut PV = CF/(r-g), all from a recognized authority (Aswath Damodaran, NYU
Stern) and independently corroborated for the perpetuity forms (Bigel,
*Introduction to Financial Analysis*). It supplies one real, current discount-rate
anchor verified against primary data: the U.S. Treasury 10-year par yield of
**4.75% as of 07/31/2026**. The evidence is strong and uncontested on the formulas
themselves (these are standard mathematical results, not contested claims). It is
thin in exactly one place the writer must handle with care: the only real rate I
can anchor is a **risk-free Treasury yield**, whereas the commission frames the
discount rate as "the cost of capital from the prior lesson" (WACC). Those are not
the same number. The Treasury yield is the risk-free floor beneath a real cost of
capital, not a company's cost of capital. See Contradictions. The worked-table
cash flows the commission calls for are teaching inventions, not real figures; only
the discount rate is a sourced real number, and the flat-rate/no-tax choices are
teaching simplifications, flagged below.

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
URL:         https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026
Kind:        Primary. The U.S. Department of the Treasury owns and publishes the
             Daily Treasury Par Yield Curve Rates.
Establishes: The one real, current discount-rate anchor: the 10-year U.S. Treasury
             par yield, with the full curve for the latest trading day.
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
URL:         https://biz.libretexts.org/Bookshelves/Finance/Introduction_to_Financial_Analysis_(Bigel)/03%3A_Part_III-_The_Time_Value_of_Money/11%3A_The_Time_Value_of_Money-_Annuities_Perpetuities_and_Mortgages/11.20%3A_Growth_Perpetuities
Kind:        Primary/authoritative for the definitional statement (open academic
             textbook: Kenneth S. Bigel, "Introduction to Financial Analysis,"
             hosted on LibreTexts). Independent of Damodaran.
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
  capital.** The commission says "The discount rate is the cost of capital from the
  prior lesson" (WACC) and asks to connect them. The only real, current rate this
  record can source is the 10-year Treasury par yield (4.75%, 07/31/2026), which is
  a **risk-free rate**, not a firm's cost of capital. Damodaran (slide 3) treats the
  discount rate as incorporating uncertainty/risk on top of the pure time and
  inflation preference; the Treasury yield carries essentially no default risk, so it
  is the **floor beneath** a real cost of capital, not the cost of capital itself. If
  the writer discounts risky business cash flows at 4.75% flat and calls it "the cost
  of capital," that is an error the prior WACC lesson would contradict. The honest
  move: present the 10-year Treasury as the risk-free anchor the discount rate is
  built up from, and either (a) build a plausible cost of capital above it, or
  (b) state plainly that a full cost of capital adds a risk premium taught in the WACC
  lesson. This is the record's most important limitation.

- **r > g is a hard constraint, not a footnote.** Both Damodaran (slide 29, the
  growing-annuity edge case where g = r) and Bigel (explicitly, section 11.20) flag
  that the growing-perpetuity/growing-annuity math breaks when g >= r. Any worked
  perpetuity number in the lesson must keep g strictly below r, or the shortcut
  produces a zero/negative denominator and a nonsensical value.

- **Automated table-reads disagreed; the primary resolved it.** Two automated fetches
  of the Treasury HTML table returned conflicting 10-year values for 07/31/2026 (one
  reported 4.08%, another 4.75%) because the summarizer misaligned columns (4.08% is
  in fact the 1-year yield). The Treasury CSV settles it: 10 Yr = 4.75%. Recorded so
  the editor does not reintroduce the misread.

## Numbers

```text
Figure: 4.75% (10-year U.S. Treasury par yield)
Owner:  U.S. Department of the Treasury, Daily Treasury Par Yield Curve Rates
Scope:  Constant-maturity par yield, 10-year point, as of 07/31/2026 (latest
        trading day before the 2026-08-03 run). Annualized percent. This is a
        risk-free benchmark rate, not a company cost of capital.
```

```text
Figure: Full curve on 07/31/2026 (for context / optional chart)
Owner:  U.S. Department of the Treasury
Scope:  1 Yr 4.08%, 2 Yr 4.28%, 3 Yr 4.34%, 5 Yr 4.45%, 7 Yr 4.59%,
        10 Yr 4.75%, 20 Yr 5.28%, 30 Yr 5.27%. Same date and basis as above.
        Note the near-inversion at the very long end (20 Yr above 30 Yr).
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
        years, mirroring Damodaran's slide-5 timeline) is a legitimate teaching
        choice. Only the discount rate carries a real-world citation (the Treasury
        anchor). State in-text that the cash flows are illustrative.
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
Asset: U.S. Treasury Daily Par Yield Curve Rates table, 07/31/2026 row / the 2026
       daily series.
Shows: A real, current term structure of risk-free rates. If the lesson wants a
       chart, the full 2026 daily 10-year series (or the 07/31 curve across
       maturities) is the honest, citable data behind any figure.
Crop:  A chart must be rendered from committed chart-N.py per spec/charts.md, label
       axes, and cite "U.S. Department of the Treasury, Daily Treasury Par Yield
       Curve Rates" in the caption. Do not hand-draw or screenshot.
```

## Discarded

```text
URL: https://www.scribd.com/document/55001902/Time-Value-of-Money-Damodaran — a
     re-host of Damodaran's material behind a login wall; the primary NYU Stern PDF
     is the source of record, so the mirror adds nothing and should not be cited.
URL: https://www.wallstreetprep.com/knowledge/growing-perpetuity/ and
     financeformulas.net — commercial explainers that merely restate the standard
     growing-perpetuity formula; superseded by Damodaran (authority) and Bigel
     (independent academic corroboration). Not needed and weaker than what is kept.
URL: https://www.studocu.com/.../a-primer-on-the-time-value-of-money — student
     re-upload of Damodaran's primer; use the original.
```
