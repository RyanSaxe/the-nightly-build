# Evidence record: investing/reverse-dcf (01)

The evidence supports the method firmly. Reverse DCF, also called price-implied
expectations, is the standard DCF run backward: hold the current price fixed and
solve for the growth (or return) the price must assume, then judge whether that
assumption is achievable. This framing is owned by two authoritative primaries.
Rappaport and Mauboussin present it on their own site as "the market's own
pricing model, the discounted cash flow model, with an important twist," and
Damodaran uses the same inversion to compute the market's implied equity risk
premium from the S&P 500. Both are firsthand statements from the people who own
the framework. The Mastercard worked example is fully verifiable: every input
below (operating cash flow, capital spending, capitalized software, net income,
share count, cash, debt) is read from Mastercard's FY2025 10-K and Q2 2026 10-Q,
and the current price and Treasury yield are recorded with dates. Where the
evidence is thin: the single most-quoted modern statement of the method,
Mauboussin and Callahan's "Everything Is a DCF Model," could not be read in full
because the Morgan Stanley host and its mirrors returned 403; its thesis is
corroborated by the authors' own website, which I did read, so no claim rests on
the unread paper. The other thin spot is unavoidable and is itself the lesson:
the "implied growth" number is not unique. It is conditional on the assumed
discount rate, terminal growth, and forecast horizon, and my own computation
shows it moving from about 5.5% to about 8.8% for the same stock depending only
on model structure. The writer must present the implied number as a function of
stated assumptions, never as a single fact the market "says."

## Sources

```text
URL:         https://www.expectationsinvesting.com/the-book
Kind:        primary. The authors' own site for their book Expectations
             Investing (Rappaport & Mauboussin). They own the framework.
Establishes: The definition and steps of the reverse-DCF / price-implied
             expectations (PIE) method, firsthand.
Paraphrase:  The method is a stock-selection process that uses the market's own
             pricing model, the discounted cash flow model, run in reverse to
             read what the price already implies. It has three steps: (1)
             estimate the expectations the current price implies; (2) identify
             expectations opportunities by comparing those implied expectations
             against historical performance and competitive-strategy analysis;
             (3) convert to a buy/sell/hold decision with a margin of safety.
             The value triggers are sales, costs, and investments; value factors
             include volume, price/mix, operating leverage, scale, and cost and
             investment efficiencies. The method depends on a continuing
             (terminal) value and an explicit forecast, or competitive-advantage,
             period.
Locators:    "The Book" overview page; author framing of the process.
Quote:       "a stock-selection process that uses the market's own pricing
             model, the discounted cash flow model, with an important twist"
```

```text
URL:         https://www.expectationsinvesting.com/
Kind:        primary. Authors' site (Rappaport & Mauboussin).
Establishes: That the authors publish free tutorials and a downloadable reverse
             DCF spreadsheet, and that the method's two skills are reading the
             expectations in today's price and anticipating revisions to them.
Paraphrase:  Stock prices are treated as the clearest signal of the market's
             expectations about future financial performance. Expectations
             investing has two skills: use a reverse DCF to read the
             expectations embedded in the current price, then judge how those
             expectations are likely to be revised. The site hosts step-by-step
             tutorials with downloadable spreadsheets (present value, value
             drivers, PIE analysis, and others).
Locators:    Home page; method overview and tutorials list.
Quote:       (none beyond the-book entry above)
```

```text
URL:         https://aswathdamodaran.blogspot.com/2026/03/the-price-of-risk-equity-risk-premium.html
Kind:        primary. Damodaran (NYU Stern) on his own blog, Musings on Markets.
Establishes: That the same inversion applied to the whole S&P 500 yields the
             market-implied expected return and equity risk premium, and the
             2026 values used to build a discount rate for the worked example.
Paraphrase:  Damodaran computes the implied equity risk premium by backing out,
             from the index level and expected cash flows, the internal rate of
             return the market is pricing into stocks. This is a reverse DCF at
             the index level. He reports the U.S. implied ERP at the start of
             2026 at 4.23% paired with the 10-year Treasury bond rate, rising to
             4.37% on March 1 and 4.51% on March 13, 2026. He calls the
             forward-looking, model-agnostic estimate far more precise than a
             historical premium.
Locators:    Body, start-of-2026 and early-March 2026 figures.
Quote:       "backing out from stock prices and expected cash flows, the
             expected return (internal rate of returns) that markets were
             pricing into stocks"
```

```text
URL:         https://aswathdamodaran.blogspot.com/2016/11/myth-55-terminal-value-ate-my-dcf.html
Kind:        primary. Damodaran, own blog.
Establishes: That terminal value is the bulk of a DCF's value and that this
             raises, not lowers, the burden on the growth assumptions the
             inversion solves for.
Paraphrase:  For a five-year high-growth window, the terminal value in his
             worked table runs from about 75% of current value at no excess
             growth to well over 100% at high excess growth. He argues that as
             terminal value takes a larger share of value, the analyst should
             pay more attention to the high-growth assumptions, not less.
Locators:    Terminal-value share table and the sentence that follows it.
Quote:       "as the terminal value accounts for a larger and larger percent of
             my current value, I should be paying more attention to the
             assumptions I make about my high growth period, not less!"
```

```text
URL:         https://aswathdamodaran.blogspot.com/2016/11/myth-54-negative-growth-rates-forever.html
Kind:        primary. Damodaran, own blog.
Establishes: The hard cap on the terminal growth rate that bounds any reverse
             DCF's continuing-value assumption.
Paraphrase:  The perpetuity (terminal) growth rate cannot exceed the growth rate
             of the economy. It can be lower, and it can be negative. Because a
             company cannot outgrow the economy forever, the terminal growth
             input is bounded, which in turn bounds the whole inversion.
Locators:    Section "Negative Growth Rates: The Mechanics."
Quote:       "the growth rate in perpetuity cannot exceed the growth rate of the
             economy but it can be lower and that lower number can be negative"
```

```text
URL:         https://aswathdamodaran.blogspot.com/2015/02/dcf-myth-1-if-you-have-ddiscount-rate.html
Kind:        primary. Damodaran, own blog.
Establishes: The garbage-in limit and the internal-consistency requirement that
             a reverse DCF inherits from a forward DCF.
Paraphrase:  A DCF is only as good as its inputs, and for it to be defensible the
             assumptions about cash flows, growth, and risk have to be
             consistent with each other. Inconsistent inputs produce an error
             that reflects that dissonance. He warns against "Trojan Horse" DCFs
             that smuggle a market pricing (a current multiple) in as if it were
             an intrinsic value, which keeps the distinction between price and
             value intact.
Locators:    Body, valuation-consistency discussion.
Quote:       "for it to be defensible, the assumptions that you make about these
             variables have to be consistent with each other"
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/0001141391-26-000013-index.htm
Kind:        primary. Mastercard Incorporated FY2025 Form 10-K (period ended
             2025-12-31, filed 2026-02-11). The company owns these figures.
Establishes: The free-cash-flow base, earnings, revenue, and reinvestment inputs
             for the worked example, plus three years of history to judge the
             implied growth against.
Paraphrase:  Consolidated Statements of Operations: net revenue $32,791M
             (FY2025), $28,167M (FY2024), $25,098M (FY2023); net income $14,968M,
             $12,874M, $11,195M; diluted EPS $16.52 (FY2025) on 906M diluted
             weighted-average shares. Consolidated Statements of Cash Flows: net
             cash from operating activities $17,648M, $14,780M, $11,980M;
             purchases of property and equipment $489M, $474M, $371M; capitalized
             software $726M, $720M, $717M; purchases of treasury stock $11,727M,
             $10,954M, $9,032M.
Locators:    Consolidated Statements of Operations (R3) and Cash Flows (R8).
Quote:       (line items, no prose quote)
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1141391/000114139126000083/0001141391-26-000083-index.htm
Kind:        primary. Mastercard Q2 2026 Form 10-Q (period ended 2026-06-30,
             filed 2026-07-30).
Establishes: The current share count for turning price into market
             capitalization, and the balance-sheet cash and debt for an
             enterprise-value version of the inversion.
Paraphrase:  Cover page: 869,464,115 Class A shares and 6,545,825 Class B shares
             outstanding as of July 27, 2026 (total 876,009,940). Consolidated
             balance sheet as of 2026-06-30: cash and cash equivalents $11,291M;
             current investments $318M; current portion of long-term debt /
             short-term debt $2,459M; long-term debt $22,184M; total equity
             $5,606M.
Locators:    Cover page (R1); Consolidated Balance Sheet (R4).
Quote:       (line items, no prose quote)
```

```text
URL:         https://fred.stlouisfed.org/series/DGS10
Kind:        primary for the yield (U.S. Treasury data, published via FRED). The
             specific reading below was retrieved through market reporting and
             should be reconfirmed against FRED on the writing date.
Establishes: The risk-free rate input for the discount rate.
Paraphrase:  The 10-year U.S. Treasury constant-maturity yield was about 4.70%
             on 2026-08-15 and about 4.69% on 2026-08-17.
Locators:    DGS10 daily series, mid-August 2026.
Quote:       (numeric series)
```

```text
URL:         https://stockanalysis.com/stocks/ma/statistics/
Kind:        secondary. Aggregator; not the owner of any filing figure. Used only
             for the market quote, beta, and return metrics, none of which a
             filing owns.
Establishes: Current price context and a market beta for the discount rate, plus
             Mastercard's return profile.
Paraphrase:  Last close $569.29 on Friday 2026-08-14; market capitalization about
             $498.7B; 52-week range $464.52 to $601.77; trailing P/E roughly 31.
             Reported beta 0.83. Reported return on invested capital about 95%
             and return on equity about 210%, the latter inflated by Mastercard's
             small book equity after years of buybacks.
Locators:    Statistics and overview pages.
Quote:       (numeric)
```

## Contradictions

The implied growth rate is not a single number, and this is the central caveat
the commission's framing must absorb. Reverse DCF does not remove assumptions.
It relocates them from the cash-flow forecast to the discount rate, the terminal
growth rate, and the forecast horizon. The same Mastercard price and cash-flow
base yield very different "implied growth" answers depending on model structure
(all computed below from the verified inputs):

- A single-stage Gordon model implies about 5.0% to 6.0% perpetual free-cash-flow
  growth (5.5% at a 9% cost of equity).
- A two-stage model (ten explicit years, then a 4% terminal rate, 9% cost of
  equity) implies about 8.8% annual growth for the decade.
- Holding that two-stage structure and moving only the terminal rate from 4% to
  3% raises the implied decade growth from 8.8% to about 10.5%. Moving the
  discount rate from 9% to 9.5% raises it from 8.8% to about 10.1%; dropping it
  to 8.5% lowers it to about 7.4%.

So a one-point change in a single assumption moves the answer by one to two
points of implied growth. Damodaran's terminal-value point (Myth 5.5) is the
reason: with about two-thirds of the value in the terminal block, the growth
assumptions carry most of the weight.

Second contradiction, on the cash-flow base itself. The earlier free-cash-flow
lesson established that no accounting rule fixes the definition. Mastercard's
operating cash flow includes a non-cash add-back for stock-based compensation, so
free cash flow computed as operating cash flow minus capital spending overstates
what an owner keeps by the amount of that compensation. Subtracting capitalized
software (a real reinvestment) versus ignoring it also changes the base by about
$726M. Different but defensible bases feed different implied growth rates, which
is a concrete instance of Damodaran's garbage-in warning (Myth 1).

Third, on whether the answer even judges the stock. Reverse DCF reads the
expectations in the price. It does not tell you the price is right. The verdict
still requires the reader to decide whether the implied growth is achievable,
which is competitive-strategy work the number cannot do. This is consistent with
Damodaran's price-versus-value distinction and with the authors' own second
skill (anticipating revisions), so it refines the commission's angle rather than
opposing it.

No source contradicts the mechanics of the inversion itself. The disagreement is
entirely about how much to trust any single output, and every authority read here
lands on the same side of that: state the assumptions, and treat the implied
number as conditional.

## Numbers

```text
Figure: $569.29 per share (last close, Fri 2026-08-14)
Owner:  market quote (stockanalysis.com); not a filing figure. Prices move; the
        writer should refresh to the drafting date and keep the date visible.
Scope:  Mastercard Inc. Class A (NYSE: MA), single day.
```

```text
Figure: 876,009,940 total shares outstanding (Class A 869,464,115 + Class B 6,545,825)
Owner:  Mastercard Q2 2026 10-Q cover, as of 2026-07-27.
Scope:  Shares outstanding for market-cap = price x shares.
```

```text
Figure: market capitalization approx $498.7B (876.0M x $569.29)
Owner:  derived from the two figures above.
Scope:  Equity value used as the target the inversion must reproduce.
```

```text
Figure: net cash from operating activities $17,648M (FY2025); $14,780M (FY2024); $11,980M (FY2023)
Owner:  Mastercard FY2025 10-K, Consolidated Statements of Cash Flows.
Scope:  Full fiscal years ending Dec 31.
```

```text
Figure: purchases of property and equipment $489M (FY2025); $474M (FY2024); $371M (FY2023)
Owner:  Mastercard FY2025 10-K, Cash Flows.
Scope:  Capital expenditure, full fiscal years.
```

```text
Figure: capitalized software $726M (FY2025); $720M (FY2024); $717M (FY2023)
Owner:  Mastercard FY2025 10-K, Cash Flows.
Scope:  Second reinvestment line, full fiscal years.
```

```text
Figure: free cash flow base $16,433M (FY2025) = OCF 17,648 - capex 489 - capitalized software 726
Owner:  derived from Mastercard FY2025 10-K. A capex-only definition gives $17,159M.
Scope:  The FCF base used in the worked inversion. See the SBC caveat in Contradictions.
        Prior years on the same (both-lines) basis: $13,586M (FY2024), $10,892M (FY2023).
```

```text
Figure: net revenue $32,791M (FY2025); $28,167M (FY2024); $25,098M (FY2023)
Owner:  Mastercard FY2025 10-K, Statements of Operations.
Scope:  Full fiscal years. Two-year CAGR 14.3%.
```

```text
Figure: net income $14,968M (FY2025); $12,874M (FY2024); $11,195M (FY2023); diluted EPS $16.52 (FY2025)
Owner:  Mastercard FY2025 10-K, Statements of Operations.
Scope:  Full fiscal years. Net-income two-year CAGR 15.6%; FCF two-year CAGR 22.8%.
```

```text
Figure: cash $11,291M; current investments $318M; short-term debt $2,459M; long-term debt $22,184M (as of 2026-06-30)
Owner:  Mastercard Q2 2026 10-Q, Consolidated Balance Sheet.
Scope:  For an enterprise-value inversion: total debt $24,643M, cash + current
        investments $11,609M, net debt $13,034M, enterprise value approx $511.7B.
```

```text
Figure: risk-free rate 4.69% (10-year Treasury, 2026-08-17)
Owner:  U.S. Treasury / FRED DGS10.
Scope:  Discount-rate input. Reconfirm on the drafting date.
```

```text
Figure: equity risk premium 4.2% to 4.5% (2026)
Owner:  Damodaran implied ERP (4.23% start of 2026; 4.37%-4.51% early March 2026).
Scope:  Discount-rate input. The reverse DCF at the index level that produces it.
```

```text
Figure: cost of equity approx 9% (base); range 8.3% to 9.5%
Owner:  derived (CAPM): 4.69% + beta x 4.4%. Beta 0.83 (stockanalysis) gives
        8.3%; beta 1.0 gives 9.1%. WACC is close to cost of equity because debt
        is about 5% of capital.
Scope:  Discount rate for the worked inversion. Presented as a range on purpose.
```

Derived sensitivity series, computed from the verified inputs above (FCF base
$16,433M, 876.0M shares, cost of equity 9%, ten explicit years, 4% terminal
growth). This is the "implied value across a range of growth assumptions" series
the brief asked to preserve. It is my computation, not a figure any source owns,
and it is fully reproducible from the inputs.

```text
10-yr FCF growth ->  implied equity value  ->  implied price/share  (terminal-value share)
   4%             ->  $342B                ->  $390                 (62%)
   6%             ->  $400B                ->  $457                 (65%)
   8%             ->  $468B                ->  $534                 (67%)
   8.8%           ->  $498B                ->  $569  = today price   (67%)
   9%             ->  $506B                ->  $578                 (68%)
  10%             ->  $547B                ->  $625                 (68%)
  12%             ->  $640B                ->  $730                 (70%)
```

The crossing point is the finding: at a 9% cost of equity and a 4% terminal rate,
Mastercard's $569 price implies roughly 8.8% free-cash-flow growth per year for a
decade. Set that against the record: Mastercard grew revenue 14.3%, net income
15.6%, and free cash flow 22.8% per year across FY2023 to FY2025. The market's bar
sits below Mastercard's recent pace, so the reader's real question is durability,
whether a company already earning $16B of free cash flow can hold high-single to
low-double-digit growth for ten years at its scale, not whether the current rate
is high enough today.

## Source assets

```text
Asset: Mastercard FY2025 10-K, Consolidated Statements of Cash Flows (the
       operating-activities total and the two reinvestment lines).
Shows: How the free-cash-flow base is built from primary lines, which grounds the
       one input the whole inversion turns on and ties back to the FCF lesson.
Crop:  Retain the operating-activities subtotal, purchases of property and
       equipment, and capitalized software, for three years. Omit financing
       detail unless buybacks are discussed.
```

```text
Asset: Mastercard Q2 2026 10-Q cover page (share counts by class).
Shows: The exact current share count that converts price to the market
       capitalization the inversion must reproduce.
Crop:  Retain both class counts and the as-of date. Nothing else needed.
```

```text
Asset: Damodaran Myth 5.5 terminal-value table (terminal value as a percent of
       current value across growth scenarios).
Shows: That terminal value is the majority of a DCF, which is why the growth
       assumption dominates the inversion. Pairs with the derived series above,
       whose terminal share sits around 67%.
Crop:  Retain the percent-of-value column and its growth-rate axis. This is a
       teaching table, so a faithful redraw as furniture is better than a screen
       grab.
```

```text
Asset: The derived sensitivity series in Numbers (implied value versus assumed
       growth, with the price line crossing it).
Shows: The single most important idea of the lesson in one picture: the market's
       implied growth is the x-value where the model's output line crosses
       today's price, and the whole curve shifts when the discount or terminal
       rate changes.
Crop:  A chart script owns this per spec/charts.md. Plot implied price/share
       against 10-year growth, draw the current price as a horizontal line, mark
       the crossing. A second faint curve at a 3% terminal rate would show the
       assumption's leverage. Label the fixed assumptions in the caption.
```

## Discarded

```text
URL: https://www.morganstanley.com/im/publication/insights/articles/article_everythingisadcfmodel.pdf
     Mauboussin & Callahan, "Everything Is a DCF Model," the cleanest modern
     statement of the method. The Morgan Stanley host returned 403, as did the
     Eaton Vance mirror and the Wayback copy, and the Meb Faber page holds only
     an abstract. Not read in full, so not cited as read. Its thesis (price is
     the market's expectations; a reverse DCF reads them; DCF does not apply to
     assets with no cash flows such as gold or cryptocurrency) is corroborated by
     the authors' own site, which was read. If the writer can open the PDF, it is
     the best single citation for the framing.
```

```text
URL: https://www.fool.com/investing/2022/01/19/expectations-investing-qanda-mauboussin-rappaport/
     Secondary Q&A that reports the authors' words, including the "how high is the
     bar for the high jumper" analogy for reading implied expectations. Usable as
     color if attributed to the authors via this interview, but the same two
     skills are stated firsthand on the authors' own site, so that primary is
     preferred and this was set aside.
```

```text
URL: https://rpc.cfainstitute.org/blogs/enterprising-investor/2022/book-review-expectations-investing
     CFA Institute book review. Secondary commentary on the book, no firsthand
     claim the primaries do not already own. Not used.
```

```text
URL: https://www.wallstreetprep.com/knowledge/reverse-dcf-model/ ; https://www.finpab.com/pages/resources/blog/reverse-dcf-india-2026 ; https://www.tikr.com/blog/how-to-reverse-engineer-a-stocks-implied-growth-rate
     Tutorial and vendor pages restating the mechanics. The brief rules out blog
     restatements as the basis for the method, and each is downstream of the
     primaries above. Read for cross-checking the single-stage formula only; not
     cited.
```

```text
URL: https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/dcfall2pg.pdf
     Damodaran's DCF lecture notes, a strong primary for the terminal-growth
     constraint and mechanics, but the PDF did not convert to readable text on
     fetch. The two constraints needed (terminal growth capped by the economy;
     assumption consistency) are covered by his blog posts above, which were
     read cleanly, so nothing is lost.
```
