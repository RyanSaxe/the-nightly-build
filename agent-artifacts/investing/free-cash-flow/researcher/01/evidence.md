# Evidence: investing/free-cash-flow (01)

The evidence supports the full lesson the commission asks for. It establishes,
from authoritative primaries, (1) the three-category structure of the statement
of cash flows (operating / investing / financing) from a standard-setter, and
(2) the standard construction of free cash flow — operating cash flow minus
capital expenditure — together with the corporate-finance distinction between
free cash flow to the firm (FCFF) and to equity (FCFE). It establishes plainly,
from the SEC's own staff guidance, that free cash flow is a constructed non-GAAP
measure with **no uniform definition**. It provides one fully verified worked
example: Apple Inc.'s fiscal-2025 10-K (year ended September 27, 2025), every
figure read from the primary filing, from which the reader can reproduce
`FCF = operating cash flow − capex = $111,482M − $12,715M = $98,767M` line by
line. It documents honest traps: Apple's FCF *fell* year-over-year while net
income *rose* (profit up, cash down); depreciation nearly equals capex, so
"reinvestment" net of depreciation is small; stock-based compensation
($12,863M) is added back as a non-cash charge and is larger than depreciation,
so the FCF number quietly carries it; and two authorities (SEC "OCF − capex"
vs. Damodaran's FCFF from after-tax EBIT) genuinely diverge — see
Contradictions.

Where it is thin: US GAAP's own codification (FASB ASC 230) is behind a
login/registration wall (403 to any anonymous request), so the *standard-setter*
citation for the statement's structure is anchored to IFRS IAS 7, whose
definitions are on the IFRS Foundation's own page and mirror ASC 230's
three-category scheme. ASC 230 is named in prose as the US equivalent but is not
given as a reader-resolvable link. The lesson does not need a second worked
company; one is sufficient and is fully verified.

## Sources

```text
URL:         https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures
Kind:        primary. This is the SEC Division of Corporation Finance's own
             Compliance & Disclosure Interpretations (staff guidance). It owns
             the regulator's position on what "free cash flow" is and is not.
Establishes: Free cash flow is a non-GAAP measure; it is permitted in filings;
             it has NO uniform definition; the "standard" construction is
             operating cash flow (from the GAAP statement of cash flows) less
             capital expenditures; a clear description and reconciliation must
             accompany it; it may not be shown per share.
Locators:    Question 102.07 (dated Jan. 11, 2010, on the page's C&DI list).
Quote:       "Some companies present a measure of 'free cash flow,' which is
             typically calculated as cash flows from operating activities as
             presented in the statement of cash flows under GAAP, less capital
             expenditures. ... companies should be aware that this measure does
             not have a uniform definition and its title does not describe how
             it is calculated. Accordingly, a clear description of how this
             measure is calculated, as well as the necessary reconciliation,
             should accompany the measure where it is used."
```

```text
URL:         https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/
Kind:        primary. IFRS Foundation's own page for IAS 7, the standard that
             governs the statement of cash flows under IFRS. It owns the
             definitions of the three activity categories.
Establishes: The statement of cash flows classifies the period's cash flows
             into operating, investing, and financing activities; operating
             cash flows may be shown by the direct or indirect method (the
             indirect method starts from profit/loss and adjusts for non-cash
             items and working-capital changes). US GAAP's ASC 230 uses the
             same three-category structure.
Locators:    IAS 7 "objective" and the defined terms for the three activities,
             as summarized on the standard's IFRS.org page.
Quote:       "Operating activities are the principal revenue-producing
             activities of the entity and other activities that are not
             investing or financing activities." "Investing activities are the
             acquisition and disposal of long-term assets and other investments
             not included in cash equivalents." "Financing activities are
             activities that result in changes in the size and composition of
             the contributed equity and borrowings of the entity."
```

```text
URL:         https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook/cashflows.htm
Kind:        primary (corporate-finance authority). Aswath Damodaran (Professor
             of Finance, NYU Stern) on his own page; the definitional source for
             FCFF vs. FCFE used across the field.
Establishes: The firm-level vs. equity-level construction of free cash flow and
             the role of capex, depreciation, and working capital as
             reinvestment.
Locators:    "The Little Book of Valuation" — cash flows chapter, FCFF and FCFE
             formula sections.
Quote:       FCFF: "Free Cash flow to firm (FCFF) = After-tax Operating Income
             − Reinvestment", expanded as "After-tax Operating Income −
             (Capital Expenditures − Depreciation + Change in non-cash Working
             Capital)". FCFE: "FCFE = Net Income − Reinvestment Needs − Debt
             Cash flows". On the difference: for FCFF "we begin with after-tax
             operating income instead of net income; the former is before
             interest expenses whereas the latter is after interest expenses."
Note:        Damodaran's companion PDF primer, "Earnings and Cash Flows: A
             Primer on Free Cash Flows"
             (https://pages.stern.nyu.edu/~adamodar/pdfiles/blog/FreeCF.pdf),
             resolves (HTTP 200) and states the same formulas; it is a valid
             backup primary but the Little Book chapter above is cleaner to
             quote.
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/R8.htm
             (worked example: Apple Inc. Consolidated Statements of Cash Flows)
Kind:        primary. Apple's own most-recent Form 10-K, filed with the SEC.
             R8.htm is EDGAR's XBRL-rendered Consolidated Statements of Cash
             Flows. Human-readable filing index:
             https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/0000320193-25-000079-index.htm
             Full 10-K document: .../aapl-20250927.htm
Establishes: Every figure in the worked example. Fiscal year ended
             September 27, 2025; filed October 31, 2025; the columns shown are
             FY2025 (Sep 27, 2025), FY2024 (Sep 28, 2024), FY2023
             (Sep 30, 2023). All figures in USD millions.
Locators:    Consolidated Statements of Cash Flows. Within the statement:
             "Net income" (first line, operating activities);
             "Depreciation and amortization" and "Share-based compensation
             expense" (adjustments to reconcile net income); the
             "Changes in operating assets and liabilities" block; the operating
             subtotal "Cash generated by operating activities"; under
             "Investing activities", the line "Payments for acquisition of
             property, plant and equipment".
Verified:    All figures below re-read from the raw R8.htm source
             (not a summarizer). See Numbers.
```

## Contradictions

- **The two authorities do not compute the same number, and this is the
  lesson's honest core.** The SEC's C&DI describes free cash flow as
  `operating cash flow (from the GAAP statement) − capital expenditures` — it
  starts from the *reported* operating-cash-flow subtotal, which already
  includes the depreciation add-back, the stock-based-compensation add-back,
  every working-capital change, and taxes *actually paid* (after the
  interest-expense deduction). Damodaran's **FCFF** starts somewhere different:
  `after-tax operating income (EBIT × (1 − tax rate)) − (capex − depreciation +
  Δ non-cash working capital)`. It uses a *hypothetical* tax on EBIT that
  ignores the interest tax shield, adds back only depreciation (not SBC or other
  non-cash items), and never touches the reported OCF line. For Apple FY2025
  these two methods produce materially different numbers from the same filing.
  So "free cash flow" names at least two constructions, not one. Teach which one
  is being used and why.
- **FCFF vs. FCFE diverge by design.** FCFF is cash available to *all* capital
  providers (debt and equity) and is computed before debt cash flows; FCFE
  starts from net income (after interest) and further subtracts net debt
  repayment. Damodaran: a firm paying down debt "will report positive FCFF while
  registering negative FCFE." Same firm, same year, two different "free cash
  flow" numbers depending on whose cash you mean.
- **"Capex" is not cleanly defined either.** The cash-flow line Apple uses,
  "Payments for acquisition of property, plant and equipment" ($12,715M),
  captures purchases of fixed assets but not acquisitions of whole businesses,
  and the filing does *not* split it into maintenance capex (spend to keep the
  current business running) vs. growth capex (spend to expand). The
  maintenance/growth distinction is analyst judgment, not a disclosed figure —
  a real limitation to flag, not paper over.

## Numbers

All figures are USD millions, read from Apple's FY2025 10-K Consolidated
Statements of Cash Flows (R8.htm). Fiscal year ended September 27, 2025.

```text
Figure: Net income = 112,010  (FY2024: 93,736 ; FY2023: 96,995)
Owner:  Apple 10-K, Consolidated Statements of Cash Flows, first line.
Scope:  Fiscal year ended Sep 27, 2025 (52/53-week fiscal year).
```

```text
Figure: Depreciation and amortization = 11,698  (FY2024: 11,445 ; FY2023: 11,519)
Owner:  Apple 10-K, cash-flow statement, "Adjustments to reconcile net income".
Scope:  FY ended Sep 27, 2025. Non-cash add-back.
```

```text
Figure: Share-based compensation expense = 12,863  (FY2024: 11,688 ; FY2023: 10,833)
Owner:  Apple 10-K, cash-flow statement, "Adjustments to reconcile net income".
Scope:  FY ended Sep 27, 2025. Non-cash add-back; larger than D&A.
```

```text
Figure: Cash generated by operating activities (OCF) = 111,482
        (FY2024: 118,254 ; FY2023: 110,543)
Owner:  Apple 10-K, cash-flow statement, operating-activities subtotal.
Scope:  FY ended Sep 27, 2025. Note this FELL from FY2024 while net income ROSE.
```

```text
Figure: Payments for acquisition of property, plant and equipment (capex) = 12,715
        (FY2024: 9,447 ; FY2023: 10,959)
Owner:  Apple 10-K, cash-flow statement, "Investing activities".
Scope:  FY ended Sep 27, 2025. Shown as an outflow, (12,715).
```

```text
Figure: FREE CASH FLOW (SEC "standard": OCF − capex) = 98,767
Owner:  Constructed by this record from the two Apple primary lines above:
        111,482 − 12,715 = 98,767. Not a line in the filing (FCF is non-GAAP).
Scope:  FY ended Sep 27, 2025. Comparison: FY2024 FCF = 118,254 − 9,447 = 108,807.
        FCF fell ~9.2% ($98.8B vs $108.8B) even as net income rose ~19%
        ($112.0B vs $93.7B). This is the "profit up, cash down" trap.
```

```text
Figure: Net capex over depreciation (Damodaran reinvestment component)
        = capex − D&A = 12,715 − 11,698 = 1,017
Owner:  Constructed from Apple primary lines. Shows depreciation nearly equals
        capex, so the "capex − depreciation" reinvestment term is small (~$1.0B)
        even though gross capex is $12.7B.
Scope:  FY ended Sep 27, 2025.
```

```text
Working-capital changes (the "Changes in operating assets and liabilities"
block), FY2025 / FY2024 / FY2023, USD millions, as read from R8.htm:
  Accounts receivable, net:                 (6,682) / (3,788) / (1,688)
  Vendor non-trade receivables:               (347) / (1,356) /  1,271
  Inventories:                                1,400 / (1,046) / (1,618)
  Other current and non-current assets:      (9,197) /(11,731) / (5,684)
  Accounts payable:                             902 /  6,020 / (1,889)
  Other current and non-current liabilities:(11,076) / 15,552 /  3,031
Owner: Apple 10-K cash-flow statement. Scope: fiscal years as labeled.
Use:   Explains why OCF fell in FY2025: "Other current and non-current
       liabilities" alone swung ~$26.6B (from +15,552 to −11,076). Working
       capital is the reason a single year's operating cash (and thus FCF) is
       lumpy even when profit is steady.
```

## Source assets

```text
Asset: Apple's Consolidated Statements of Cash Flows, operating-activities
       section, in the FY2025 10-K (R8.htm / aapl-20250927.htm).
Shows: The indirect-method reconciliation the lesson teaches: start at net
       income, add back depreciation and SBC (non-cash), adjust for
       working-capital changes, arrive at "Cash generated by operating
       activities". The reader sees exactly where every input to FCF lives.
Crop:  A crop must retain the net-income line, the D&A and SBC add-back lines,
       the operating subtotal, and (from investing) the capex line, with the
       FY2025 column and its header. It may omit the marketable-securities and
       financing sections. Keep the column-year headers so the figures are
       unambiguous.
```

```text
Asset: A small worked-calculation table built ONLY from the verified numbers
       above (this record, Numbers section), e.g.
         Operating cash flow      111,482
         − Capital expenditures     12,715
         = Free cash flow           98,767
       and a second column repeating it for FY2024 (108,807) to show the fall.
Shows: The line-by-line FCF construction and the "profit up, cash down"
       contrast in one glance.
Crop:  n/a (table, not an image crop). Build per spec/charts.md if rendered.
```

## Discarded

```text
URL: https://www.fasb.org/page/showpdf?path=fas95.pdf (FASB SFAS No. 95, the US
     origin of ASC 230): returns HTTP 403 to every anonymous request, browser
     user-agent included. asc.fasb.org/230 (the codification itself) also 403s
     and requires free registration/login. Would strand any reader who clicks
     it, so not cited as a resolvable link. ASC 230 is named in prose as the US
     GAAP equivalent; IAS 7 (IFRS.org, resolves) carries the standard-setter
     citation for the three-category structure.
URL: BDO / EY / Deloitte / PwC / KPMG ASC 230 explainer pages: secondary
     (accounting-firm restatements of the standard), not the standard itself.
     Not needed once IAS 7 and the SEC C&DI are in hand.
URL: en.wikipedia.org/wiki/Free_cash_flow_to_equity: secondary/tertiary;
     Damodaran's own page owns the FCFF/FCFE definitions.
```
