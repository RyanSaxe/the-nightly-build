# Evidence record: investing/discounted-cash-flow (01)

The record firmly supports every structural claim the lesson needs. The DCF
identity (firm value = present value of free cash flow to the firm, discounted
at the cost of capital), the two terminal-value forms (perpetuity/Gordon growth
and exit multiple), and the enterprise-to-equity bridge (subtract net debt) are
each owned by a primary that states them as formulas, and each is corroborated
by a second independent authority. The lesson's spine is well sourced from two
sides: that terminal value dominates a typical DCF is stated as "70 to 80
percent of corporate value" by Mauboussin & Callahan (Morgan Stanley) and shown
to be about two-thirds in Damodaran's own published Tube Investments valuation,
which I recomputed from his numbers; that the output is highly sensitive to the
discount rate r and the stable growth rate g is stated outright by Damodaran
("none can affect the value more than the stable growth rate") and demonstrated
mechanically by my own labeled illustrative firm and its sensitivity grid.

The record is thin in one honest place: there is no single universal constant
for the terminal-value share. It is a typical-case figure that moves with the
forecast horizon, r, and g (my grid shows it ranging roughly 58% to 82% under
ordinary inputs). The worked example that carries the arithmetic is a clean
illustrative firm I constructed and labeled as such; it is not a real company's
filings. Two real published DCFs (Damodaran's Tube Investments and
DaimlerChrysler) corroborate the mechanics and the share, but they come from
Damodaran's teaching notes, not from the companies' own filings, and are
recorded that way.

## Sources

```text
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/termvalue.pdf
Kind:        primary — Aswath Damodaran (NYU Stern), the author who owns this
             statement of the DCF identity and terminal-value formulas; a
             textbook chapter, "Closure in Valuation: Estimating Terminal Value."
Establishes: the firm-value identity with an explicit-forecast term plus a
             terminal-value term; the three routes to terminal value
             (liquidation, multiple, stable growth); the Gordon/perpetuity
             terminal-value formula for the firm; the caution against
             comparable-multiple terminal values; the growth-rate cap; and the
             single strongest statement that r and g dominate the answer.
Paraphrase:  Because cash flows cannot be estimated forever, a DCF imposes
             "closure" by forecasting explicitly for n years and capping the
             stream with a terminal value at year n. Firm value is the present
             value of the explicit cash flows plus the present value of that
             terminal value, both discounted at the cost of capital k_c. The
             terminal value can be found three ways: liquidation, a multiple of
             earnings/revenue/book value, or a stable-growth (perpetuity) model.
             The stable-growth terminal value of the firm is next year's
             cashflow-to-firm divided by (cost of capital minus stable growth
             rate). A comparable-multiple terminal value mixes relative and
             intrinsic valuation and is discouraged. The stable growth rate
             cannot exceed the growth rate of the economy, and a rule of thumb
             caps it at the risk-free rate. Of all inputs, none moves the value
             more than the stable growth rate, and the effect grows as g nears r.
Locators:    p.1 (identity and closure), pp.1-2 (three routes), p.3 (multiple
             caution, "Stable Growth Model" formula), p.4 ("Constraints on
             Stable Growth"; firm terminal-value formula), p.5 (risk-free-rate
             rule of thumb), p.6 footnote (excess returns).
Quote:       "you generally impose closure in discounted cash flow valuation by
             stopping your estimation of cash flows sometime in the future and
             then computing a terminal value" (p.1). Firm identity as written:
             "Value of a Firm = Σ CFt/(1+kc)^t + Terminal Value_n/(1+kc)^n"
             (p.1). Firm terminal value: "Terminal value_n = Cashflow to
             Firm_{n+1} / (Cost of Capital_{n+1} − g_n)" (p.4). Spine:
             "Of all the inputs into a discounted cash flow valuation model,
             none can affect the value more than the stable growth rate ...
             small changes in the stable growth rate can change the terminal
             value significantly and the effect gets larger as the growth rate
             approaches the discount rate used in the estimation." (p.4).
             Multiple caution: "using multiples to estimate terminal value, when
             those multiples are estimated from comparable firms, results in a
             dangerous mix of relative and discounted cash flow valuation" (p.3).
             Growth cap: "a simple rule of thumb on the stable growth rate is
             that it should not exceed the riskless rate used in the valuation"
             (p.5). Excess returns: "Growth without excess returns will make a
             firm larger but not more valuable." (p.6 footnote 1).
```

```text
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/country/TerminalValue.pdf
Kind:        primary — Aswath Damodaran presentation, "Terminal Value: The Tail
             That Wags the Dog?" The title itself is authored evidence for the
             lesson's spine that terminal value dominates.
Establishes: the mathematical instability of the perpetuity formula as g
             approaches r; the "not debatable" growth cap; the risk-free rate as
             the practical cap, with supporting long-run data; the exit-multiple
             warning ("Trojan Horse DCFs"); and the excess-return link that
             growth is not free.
Paraphrase:  The perpetuity model is the sum of an infinite series, so as g
             moves toward r the terminal value approaches infinity, and if g
             exceeds r it turns negative — a mathematical, not economic,
             constraint. Damodaran caps g at the risk-free rate, noting that over
             1954-2015 the 10-year Treasury (5.93%) tracked nominal GDP growth
             (6.67%). Using an exit multiple drawn from today's peer group
             smuggles a relative valuation into a DCF ("Trojan Horse DCFs").
             Growth equals reinvestment rate times return on invested capital, so
             assuming growth with no reinvestment (which he says roughly half of
             DCFs do) is internally inconsistent.
Locators:    slide 11 ("The Mathematical Trap"), slide 12 ("The Growth Cap"),
             slide 14 ("My Simple Proxy: The Risk free Rate"), slide 15 ("Reason
             1: The Data is supportive"), slide 8 ("How about a multiple?"),
             slides 20-26 ("The Free Growth Myth"; "Dangerous Practice 2").
Quote:       "As g moves towards r, the terminal value will approach infinity.
             If g>r, the terminal value will become negative." (slide 11).
             "the growth rate that you can use in it is constrained to be less
             than equal to the growth rate of the economy ... This is not a
             debatable assumption, since it is mathematical, not one that owes
             its presence to economic theory." (slide 12). On exit multiples:
             "If that exit multiple is based upon what other companies are
             trading at today in the peer group, you have made your most
             important cash flow in your valuation into a pricing. These are
             Trojan Horse DCFs." (slide 8).
```

```text
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/fcff.pdf
Kind:        primary — Aswath Damodaran, "The Free Cashflow to Firm Model"
             lecture notes. Owns the worked enterprise-to-equity bridge and two
             fully worked real-firm DCFs.
Establishes: that discounting FCFF at the cost of capital yields the value of
             the firm; the bridge from firm value to equity value by adding cash
             and subtracting debt; and a real two-stage DCF (Tube Investments)
             whose terminal-value share I recompute below.
Paraphrase:  For DaimlerChrysler, Damodaran discounts FCFF at the cost of
             capital to get the value of operating assets (112,847 mil DM), adds
             cash and marketable securities (18,068), reaching a firm value of
             130,915, then subtracts debt outstanding (64,488) to get equity
             value (66,427), or 72.7 DM per share. For Tube Investments he runs a
             five-year explicit forecast at a 16.90% cost of capital and caps it
             with a stable-growth terminal value of 2,775/(0.1478−0.05) = 28,378
             at year five; the operating-asset value is 19,578, plus cash 13,653
             minus debt 18,073 gives equity of 15,158.
Locators:    p.5 (DaimlerChrysler "Valuation of Firm" block and per-share value);
             the Tube Investments valuation tree (base case): FCFF stream
             1,868 / 1,971 / 2,080 / 2,195 / 2,316, "Terminal Value_5 =
             2775/(.1478-.05) = 28,378", "Discount at Cost of Capital (WACC) =
             ... 16.90%", "Firm Value: 19,578 / + Cash: 13,653 / − Debt: 18,073
             / = Equity 15,158".
Quote:       "In discounting FCFF, we use the cost of capital ... We then use the
             present value of the FCFF as our value for the firm and derive an
             estimated value for equity." (p.5). Bridge as written: "Value of
             Firm = 130,915 mil DM / − Debt Outstanding = 64,488 mil DM / Value
             of Equity = 66,427 mil DM" (p.5).
```

```text
URL:         https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/free-cash-flow-valuation
Kind:        primary — CFA Institute, curriculum refresher reading "Free Cash
             Flow Valuation." Independent of Damodaran; the standards body that
             owns the professional statement of this identity.
Establishes: the same firm-value identity, single-stage formula, and equity
             bridge, from a second authority — the corroboration the editorial
             standard asks for on load-bearing claims.
Paraphrase:  Firm value is the present value of future FCFF discounted at the
             weighted average cost of capital. With constant growth, firm value
             is next year's FCFF over (WACC minus g). Equity value is firm value
             minus the market value of debt, and dividing equity value by shares
             outstanding gives value per share.
Locators:    Summary section, FCFF valuation bullets.
Quote:       "Firm value = Σ FCFF_t/(1+WACC)^t"; "Firm value = FCFF_1/(WACC − g)
             = FCFF_0(1+g)/(WACC − g)"; "Equity value = Firm value – Market value
             of debt"; "Dividing the total value of equity by the number of
             outstanding shares gives the value per share."
```

```text
URL:         https://www.morganstanley.com/im/en-us/individual-investor/insights/consilient-observer/everything-is-a-dcf-model.html
Kind:        primary — Michael J. Mauboussin & Dan Callahan, Counterpoint Global
             (Morgan Stanley Investment Management), "Everything Is a DCF Model."
             Authors who own this quantified claim; independent of Damodaran and
             the CFA Institute. (The PDF read carried a 2025 copyright and an
             08/31/2027 expiry; the landing page above is the source's own page.)
Establishes: the independent quantification that terminal ("continuing") value
             is typically 70-80% of value — the external number behind the
             lesson's spine — and a plain statement of the r/g sensitivity.
Paraphrase:  Any time an investor values a stake in a cash-generating asset, the
             authors argue, they are running a DCF whether they admit it or not.
             Surveys show analysts mostly use multiples, and they commonly set
             the DCF's terminal value with an EV/EBITDA multiple; since the
             continuing value is often 70-80% of corporate value, the model is
             then largely a dressed-up multiple. The authors note that small
             changes in DCF assumptions produce large changes in value, which is
             why many investors retreat to multiples that merely bury those same
             assumptions. Common DCF errors include a faulty risk-free rate and
             unrealistic continuing-value growth.
Locators:    p.3 (survey, continuing-value share, sensitivity bullet); pp.1-2
             (the "everything is a DCF model" framing).
Quote:       "The continuing value often represents 70 to 80 percent of corporate
             value. That means that what drives the DCF model is for the most
             part a dressed up multiple." (p.3). "Small changes in assumptions
             for a DCF model can lead to large changes in value." (p.3).
             Errors include "the use of a faulty risk-free rate and assuming
             unrealistic growth rates in the calculation of continuing value."
             (p.3).
```

```text
URL:         https://www.iese.edu/media/research/pdfs/WP-1062-E.pdf
Kind:        primary — Pablo Fernández (IESE Business School), working paper
             WP-1062-E, "Valuing Companies by Cash Flow Discounting: Fundamental
             Relationships and Unnecessary Complications" (Feb 2013). A critic's
             own paper; the contradiction source.
Establishes: the steelmanned critique that DCF's unreliability lives in its
             inputs, not its logic — most valuation errors are discount-rate
             errors — which supports the lesson's framing that a DCF is an
             argument about assumptions.
Paraphrase:  Fernández argues DCF valuation is at root the same procedure used
             to value a government bond, and that most of the apparatus layered
             on top is unnecessary complication and the source of many errors.
             His companion catalogue of "110 Common Errors" is led by errors in
             the discount rate: wrong beta, wrong market risk premium, and a WACC
             computed inconsistently or on book values.
Locators:    Abstract and Section 16 ("Some Errors Due to Using Unnecessary
             Complications"), error category 1 ("Errors in the Discount Rate
             Calculation and Concerning the Riskiness of the Company").
Quote:       Abstract: company valuation by DCF "consists of applying the
             procedure used to value government bonds to the debt and shares of a
             company." Section 16 leads its most-common list with "Errors in the
             Discount Rate Calculation" — "Wrong beta used for the valuation ...
             Wrong market risk premium used ... Wrong calculation of WACC ...
             Calculating the WACC using book values of debt and equity."
```

## Contradictions

- **How to pick the stable growth rate g.** Damodaran caps g at the risk-free
  rate and calls the economy-growth ceiling "mathematical, not ... economic
  theory" (TerminalValue.pdf, slides 12-14). He also records a competing camp:
  "a few valuation purists ... argue that the only assumption that is consistent
  with a mature, stable growth company is that you assume zero excess returns"
  and therefore a zero growth rate; he rebuts that "excess returns seem to last
  far longer than high growth rates do" (TerminalValue.pdf, slide 24). This is a
  genuine, in-source disagreement over g, exactly the one the brief flagged.
- **Terminal value by exit multiple vs. perpetuity.** Damodaran treats a
  peer-derived exit multiple as illegitimate inside a DCF ("Trojan Horse DCFs,"
  a "dangerous mix," termvalue.pdf p.3 / TerminalValue.pdf slide 8), yet
  Mauboussin reports that analysts "commonly use an enterprise value-to-EBITDA
  multiple to estimate the continuing value" in practice (Morgan Stanley, p.3).
  The exit-multiple form the lesson must present is, per these sources, both
  standard practice and specifically warned against.
- **Whether the DCF's sensitivity is a flaw of the method or of its users.**
  Mauboussin: "many DCF models are done poorly," so the "shortcomings speak
  poorly not about the approach but rather to how it is applied" (p.3). Fernández
  goes further, casting much of the standard machinery as "unnecessary
  complications" that breed error. Damodaran concedes the same instability that
  critics attack: analysts "often use [the stable growth rate] to alter the
  valuation to reflect their biases" (termvalue.pdf p.4). The sources agree the
  sensitivity is real and disagree only on whether to blame the tool or the hand.
- **No source contradicts the core identity or the bridge.** Damodaran, the CFA
  Institute, and Fernández state the same firm-value-equals-PV-of-FCFF-at-WACC
  logic and the same net-debt bridge. That claim is uncontested across the set.

## Numbers

Two blocks. The first is the illustrative firm I constructed to teach the
arithmetic; every figure in it is my computation on invented, clearly labeled
inputs, held so the writer can teach sensitivity without a real company's story.
The second is the real, sourced corroboration.

### Illustrative firm (constructed for teaching; NOT a real company)

Inputs chosen for clean arithmetic and consistency with the earlier cost-of-
capital and present-value lessons: r = 9% (the 10-year U.S. Treasury of 4.75% on
2026-07-31 from the present-value lesson, plus roughly a 4.25-point risk premium
for a moderate-risk firm), stable g = 2.5% (below the risk-free cap Damodaran
recommends), a five-year explicit forecast, and free cash flow to the firm of
$100 million in year 1 growing 8% a year.

```text
Figure: Explicit FCFF stream ($M): 100.00, 108.00, 116.64, 125.97, 136.05
Owner:  my computation (illustrative inputs)
Scope:  years 1-5; FCFF to the firm; annual

Figure: Terminal value at year 5 = 136.05 × (1.025) / (0.09 − 0.025) = $2,145.4M
Owner:  my computation; Gordon form owned by termvalue.pdf / CFA Institute
Scope:  perpetuity-growth terminal value, stated at end of year 5

Figure: PV of explicit 5-year FCFF = $450.4M
Owner:  my computation
Scope:  discounted at r = 9%

Figure: PV of terminal value = 2,145.4 / (1.09)^5 = $1,394.4M
Owner:  my computation
Scope:  discounted at r = 9%

Figure: Enterprise value = 450.4 + 1,394.4 = $1,844.7M
Owner:  my computation
Scope:  value of the whole firm (operating assets)

Figure: Terminal-value share of enterprise value = 1,394.4 / 1,844.7 = 75.6%
Owner:  my computation
Scope:  base case (r = 9%, g = 2.5%, 5-year horizon). This lands inside
        Mauboussin's stated 70-80% band.

Figure: Equity bridge — EV 1,844.7 − net debt 300 = equity 1,544.7; ÷ 100M
        shares = $15.45 per share
Owner:  my computation; bridge owned by fcff.pdf / CFA Institute
Scope:  illustrative net debt and share count
```

Sensitivity grid — enterprise value ($M), explicit FCFF held fixed, only r and
g varied. Preserved in full for a sensitivity chart or table:

```text
            g = 1.5%    g = 2.5%    g = 3.5%
r = 8%        1,909       2,189       2,593
r = 9%        1,647       1,845       2,114
r = 10%       1,447       1,593       1,783
```

Same grid, terminal-value share of enterprise value (%):

```text
            g = 1.5%    g = 2.5%    g = 3.5%
r = 8%        75.7        78.8        82.1
r = 9%        72.7        75.6        78.7
r = 10%       69.7        72.5        75.4
```

One-variable swings from the base case (EV = $1,845M), to show the raw
sensitivity in a single line each:

```text
g held cases (r = 9%):   g=1.5% → 1,647 (−10.7%);  g=2.0% → 1,739 (−5.7%);
                         g=2.5% → 1,845 (base);    g=3.0% → 1,968 (+6.7%);
                         g=3.5% → 2,114 (+14.6%)
r held cases (g = 2.5%): r=8.0% → 2,189 (+18.6%);  r=8.5% → 2,002 (+8.5%);
                         r=9.0% → 1,845 (base);    r=9.5% → 1,710 (−7.3%);
                         r=10.0% → 1,593 (−13.7%)
```

Horizon check (same firm, 10-year explicit forecast at 6% growth, r = 9%,
g = 2.5%): EV = $1,937M, terminal-value share = 58.1%. Lengthening the explicit
window lowers the terminal-value share — useful if the lesson notes that the
share is not a fixed constant.

Exit-multiple alternative (same firm): if year-5 EBITDA were $200M and a peer
EV/EBITDA of 8.0× were applied, terminal value would be $1,600M, against the
Gordon terminal value of $2,145M — a 25% swing in the terminal value from the
choice of method alone, concretizing Damodaran's "Trojan Horse" warning.

### Real corroboration (sourced)

```text
Figure: Tube Investments terminal value at year 5 = 2,775 / (0.1478 − 0.05)
        = 28,378 (Rs. million)
Owner:  Damodaran, fcff.pdf (Tube Investments valuation)
Scope:  stable-growth terminal value; stable-phase cost of capital 14.78%,
        stable g = 5%

Figure: Tube Investments terminal-value share of firm value ≈ 66%
Owner:  my computation from Damodaran's numbers — PV of terminal value =
        28,378 / (1.169)^5 = 12,999; his operating-asset value = 19,578;
        12,999 / 19,578 = 66.4% (the residual 6,579 is the PV of the five
        explicit FCFFs, which reconciles his 19,578 to the rupee)
Scope:  a real, published two-stage DCF; independent check that terminal value
        is roughly two-thirds of value, consistent with Mauboussin's 70-80%

Figure: Continuing (terminal) value is "70 to 80 percent of corporate value"
Owner:  Mauboussin & Callahan, Morgan Stanley Counterpoint Global
Scope:  typical DCF of a going concern; the external anchor for the spine

Figure: DaimlerChrysler firm→equity bridge: operating assets 112,847 + cash
        18,068 = firm value 130,915; − debt 64,488 = equity 66,427; = 72.7 DM/sh
Owner:  Damodaran, fcff.pdf
Scope:  a worked real-firm enterprise-to-equity bridge (mil DM; FY1998 base)

Figure: Long-run consistency of the growth cap: 1954-2015, 10-year Treasury
        5.93% vs. nominal GDP growth 6.67%
Owner:  Damodaran, TerminalValue.pdf, slide 15
Scope:  U.S., 1954-2015 averages; supports capping g at the risk-free rate
```

## Source assets

```text
Asset: The firm-value identity and the boxed terminal-value formula in
       termvalue.pdf (p.1 identity; pp.3-4 the "Cashflow to Firm_{n+1} /
       (Cost of Capital − g)" box).
Shows: the exact algebra the lesson states — explicit-period sum plus a single
       capped terminal term, and the perpetuity formula that owns the r−g
       denominator.
Crop:  reproduce as clean typeset equations in the article's own equation
       furniture, not as a screenshot; retain the r−g denominator and the
       year-n subscript, omit the surrounding prose.
```

```text
Asset: The r/g sensitivity is best carried by an original chart the writer
       builds from the Numbers grids above (EV and terminal-value share across
       r and g), not lifted from a source. None of the sources contains a
       ready sensitivity figure clean enough to reuse.
Shows: how a one-point move in r or g swings enterprise value 10-20%, and how
       the terminal-value share stays high (58-82%) across the whole grid.
Crop:  if drawn, label both axes, mark the base case, and note that g must stay
       below r (the grid deliberately keeps g well under the lowest r).
```

```text
Asset: Damodaran's "Mathematical Trap" slide (TerminalValue.pdf, slide 11)
       stating g→r sends terminal value to infinity and g>r turns it negative.
Shows: the instability at the heart of the sensitivity, in the author's words.
Crop:  quote the sentence rather than image the slide; the slide's own art is
       decorative.
```

```text
Asset: Damodaran's Tube Investments valuation tree (fcff.pdf) and DaimlerChrysler
       "Valuation of Firm" block (p.5).
Shows: a real, end-to-end DCF including the terminal-value term and the
       firm→equity bridge, the model the lesson assembles.
Crop:  if referenced, keep the terminal-value line and the Firm/Cash/Debt/Equity
       stack; these are dated (2000-era) figures, so label the year and treat as
       Damodaran's teaching case, not current company data.
```

```text
Asset: None found for the CFA Institute reading and the Fernández paper beyond
       plain equation/text; nothing there is a compelling standalone visual.
```

## Discarded

```text
URL: https://valuationmasterclass.com/terminal-value-formula/ — secondary
     tutorial; states the Gordon vs. exit-multiple split correctly but owns
     nothing. Superseded by termvalue.pdf.
URL: https://www.wallstreetprep.com/knowledge/terminal-value/ — secondary
     educational; repeats the "60-80%" share without a primary owner. Replaced
     by Mauboussin's sourced "70 to 80 percent."
URL: https://corporatefinanceinstitute.com/resources/financial-modeling/dcf-terminal-value-formula/
     — secondary; formula reference only, no ownable claim.
URL: https://financewithroy.medium.com/dcf-demystified-why-your-terminal-value-is-doing-80-of-the-work-2173a74b606e
     — blog; asserts the 80% share but is not authoritative and cites no data.
URL: https://www.academia.edu/42955951/VALUATION_Koller and pdfcoffee/scribd
     copies of McKinsey's "Valuation" (Koller et al.) — the canonical
     TV-share-by-industry table lives here, but every reachable copy is an
     unauthorized upload, not the publisher's own page, so it fails the
     resolve-to-source test. Mauboussin supplies an equivalent sourced figure.
URL: https://arxiv.org/pdf/1003.4881 (Steiger, "The Validity of Company
     Valuation Using DCF") — a student thesis; useful framing on sensitivity but
     secondary and weaker than Fernández for the critique.
```
