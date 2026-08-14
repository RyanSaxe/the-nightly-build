# Evidence record: investing/enterprise-to-equity-value (01)

This record supports both halves of the commissioned bridge. The
enterprise-value-to-equity waterfall (why each subtraction and addition
belongs) is grounded in Aswath Damodaran's own materials, read directly: a
2013 blog essay on the three value measures, a 2005 Stern working paper on
option and restricted-stock valuation, and a slide deck and a 2018 blog post
specifically on share-count mechanics. The treasury-stock and if-converted
methods are grounded in that same Damodaran material plus a CFA-aligned
secondary source (AnalystPrep) and two finance-education explainer sites used
only for the uncontested mechanical formula. The worked example is Uber
Technologies, Inc., chosen because its most recent Form 10-Q (quarter ended
June 30, 2026, filed August 5, 2026) discloses, in one filing and in the
company's own words, both a treasury-stock-method share-count adjustment and
an if-converted convertible-note adjustment, next to material net debt and a
large non-operating investment portfolio (Didi, Grab, Aurora, Delivery Hero,
Careem). Every balance-sheet and note figure below was read from the filing
itself on sec.gov, not from a data aggregator.

The record is thin in two places, both flagged where they occur: (1) the
filing discloses unrecognized stock-compensation cost only as a single
blended figure across all unvested award types, so a treasury-stock proceeds
figure isolated to Uber's RSUs specifically cannot be sourced from this
filing; and (2) the "defensible EV" the brief asks for is, by necessity,
back-solved from Uber's market capitalization rather than an independent DCF
(no DCF for Uber exists in this lesson's inputs), which the record states
plainly so the writer can substitute the class's own DCF output instead.

## Sources

```text
URL:         https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000032/uber-20260630.htm
Kind:        Primary. Uber Technologies, Inc.'s own Form 10-Q, filed with the SEC on
             2026-08-05 for the quarter ended June 30, 2026 (accession
             0001543151-26-000032). This is the filing's own page on sec.gov, not a
             viewer or a data-vendor mirror.
Establishes: Every balance-sheet line, debt-instrument breakdown, non-controlling-
             interest structure, equity-method and marketable-securities investment
             detail, stock option/RSU activity, and the basic-to-diluted EPS
             reconciliation used in the worked example.
Paraphrase:  See Numbers section below for every figure drawn from this filing, each
             with its own note/page locator.
Locators:    Cover page (shares outstanding); p.4 (condensed consolidated balance
             sheet); Note 2 - Financial Instruments, "Investments" table, ~p.13-14;
             Note 3 - Equity Method Investments, ~p.16; Note 5 - Debt and Credit
             Arrangements, ~p.18-21; Note 7 - Stockholders' Equity (option/SAR and RSU
             activity), ~p.22-23; Note 9 - Net Income Per Share, ~p.23-24; Note 13 -
             Non-Controlling Interests, ~p.30-31; Note 15 - Subsequent Event, ~p.32.
Quote:       "For diluted net income per share, the dilutive effect of outstanding
             awards is reflected by application of the treasury stock method and
             convertible securities by application of the if-converted method, as
             applicable." (Note 9)
```

```text
URL:         https://aswathdamodaran.blogspot.com/2013/06/a-tangled-web-of-values-enterprise.html
Kind:        Primary. Aswath Damodaran (NYU Stern) writing under his own byline on his
             own valuation blog, "Musings on Markets" -- the authority the brief asks
             for, in his own words, not a restatement by a third party.
Establishes: Why enterprise value is defined as the value of operating assets alone,
             and therefore why every non-operating claim and asset must be stripped
             out or added back to reach equity value. Flags cross-holdings and
             "trapped" (not freely available) cash as places the mechanical bridge
             breaks down.
Paraphrase:  Enterprise value equals the market value of a company's operating assets.
             To get there from a market-value balance sheet, you back out (or, in the
             other direction, add back) the market value of cash and other
             non-operating assets, because those assets are not what enterprise value
             is meant to capture. Debt "is inclusive of all non-equity claims
             (including preferred equity)," and lease commitments should be
             "converted into debt." Minority interest is conventionally added to get
             to enterprise value, but Damodaran flags that this is a book-value
             figure standing in for what should be a market value, since "the
             conventional practice of netting out the minority interest does not
             accomplish" a true market-value adjustment when the subsidiary hasn't
             been separately valued. On cash: not all of it is free to net off --
             "to the extent that some or a large portion of the cash balance ... may
             be needed for its ongoing operations, you should be separating this
             portion," and overseas cash facing repatriation tax is "trapped," so
             netting out the entire balance "will therefore give you too low an
             estimate of enterprise value." Cross-holdings (non-controlling equity
             stakes in other companies) should be valued at market and netted out
             separately from operating value; the problem intensifies when the stake
             is in a private company with no market price.
Locators:    Full post; the load-bearing paragraphs are the ones defining enterprise
             value as operating-asset value, the debt/minority-interest paragraph, the
             trapped-cash paragraph, and the cross-holdings paragraph.
Quote:       "the conventional practice of netting out the minority interest does not
             accomplish this, because minority interest reflects book rather than
             market value." / "When a company has non-controlling stakes in other
             companies, the market value of these holdings should be netted out."
```

```text
URL:         https://pages.stern.nyu.edu/adamodar/pdfiles/papers/esops.pdf
Kind:        Primary. "Employee Stock Options (ESOPs) and Restricted Stock: Valuation
             Effects and Consequences," Aswath Damodaran, Stern School of Business,
             September 2005. Read in full as a PDF (117,709 characters extracted).
             Dated -- flagged below -- but still the fullest primary statement of his
             reasoning and still hosted on his own site as current course material.
Establishes: The reasoning for why in-the-money vested options, unvested options, and
             restricted stock are claims on equity that reduce value per share before
             a shareholder's share is counted; a side-by-side comparison of four ways
             analysts handle outstanding options (fully diluted, forecast-exercise,
             treasury stock, option-pricing), with his own critique of each; and the
             reasoning for discounting restricted stock for its vesting and
             illiquidity conditions.
Paraphrase:  Four approaches exist for folding already-granted options into value per
             share. (1) Fully diluted shares: divide equity value by shares assuming
             every option is exercised today. Damodaran's critique: this "will lead to
             too low of an estimate of value per share" because it counts
             out-of-the-money and unvested options, ignores exercise proceeds as a
             cash inflow, and ignores the option's time premium. (2) Forecast future
             exercise: "neither practical nor... particularly useful," since it
             requires forecasting the future stock price to value today's stock price
             -- circular. (3) Treasury stock approach: adjust share count for options
             outstanding, but add the assumed exercise proceeds (exercise price x
             options) back to the value of equity before dividing. Explicit critique:
             "like the fully diluted approach, it does not consider the time premium
             on the options and there is no effective way of dealing with vesting...
             this approach, by under estimating the value of options granted, will
             over estimate the value of equity per share." (4) Value options with an
             option-pricing model and net that value out of equity value before
             dividing by the share count including restricted shares -- "we believe
             that the last approach is the only one that completely incorporates the
             effect of existing options into value per share." On restricted stock:
             it should be valued at a discount to the observed market price to
             reflect the illiquidity of the trading restriction and the risk of
             forfeiture if the employee leaves before vesting, quoting FASB that
             "restricted securities are often purchased at a discount from the quoted
             price of otherwise identical unrestricted securities."
Locators:    "Ways of incorporating existing options into discounted cash flow
             valuations," roughly the paper's pp.21-24 by its own pagination
             (approaches I-IV); "Valuing Restricted Stock," roughly p.48-49.
Quote:       "this approach, by under estimating the value of options granted, will
             over estimate the value of equity per share." / "we believe that the
             last approach is the only one that completely incorporates the effect of
             existing options into value per share."
```

```text
URL:         https://pages.stern.nyu.edu/~adamodar/pdfiles/blog/TeslaDilution.pdf
Kind:        Primary. "Dilution and Options: The Mystery of Share Count," Aswath
             Damodaran slide deck (undated internally, tied to Tesla's 2017 10-K
             figures, so circa 2018 -- matches the companion blog post below). Read
             in full as a PDF (12,224 characters extracted, 20 numbered slides).
Establishes: The formal treasury-stock-method formula in Damodaran's own notation, a
             worked numeric comparison against a fully-diluted count and against his
             preferred option-pricing approach, and his explicit naming of the
             treasury-stock method as "a sloppy alternative."
Paraphrase:  "Treasury Stock Value per share = (DCF value of equity + Exercise Price x
             # Options outstanding) / (Share Count today + Options Outstanding)."
             Applied to Tesla's 2017 options (10.88 million options, weighted-average
             exercise price $105.56), this produced $184.19/share versus $177.83 for
             the naive fully-diluted count. The heading over this slide reads "A
             Sloppy Alternative: The Treasury Stock Approach." He also states the
             correct treatment of a firm's own expected future DCF-based dilution:
             "The aggregate value of equity that you compute today includes the
             present value of expected cash flows, including the negative cash flows
             in the up front years... You can divide the value of equity by the
             number of share[s] outstanding today, and you will have already
             incorporated dilution" -- and warns against separately forecasting share
             issuance on top of that, calling it double-counting.
Locators:    Slide 6 ("The Right Response" to expected dilution); slides 12 and 15-16
             (treasury stock vs. fully diluted vs. option-pricing for existing
             grants).
Quote:       "A Sloppy Alternative: The Treasury Stock Approach"
```

```text
URL:         https://aswathdamodaran.blogspot.com/2018/07/share-count-confusion-dilution-employee.html
Kind:        Primary. "Share Count Confusion: Dilution, Employee Options and Multiple
             Share Classes!" Aswath Damodaran, Musings on Markets, July 2018.
Establishes: How restricted stock (the RSU-era descendant of restricted stock
             grants) is already folded into the current share count once issued, and
             a caution against double-counting dilution; supplements the treasury-
             stock critique above.
Paraphrase:  Restricted shares are already included in the current share count
             because they are issued shares, even though vesting and trading
             restrictions make them marginally less valuable than an unrestricted
             share; the post calls this "a relatively small problem" not usually
             worth a separate adjustment. Reiterates the "don't double-count"
             warning: you can either build expected future dilution into the DCF's
             negative early cash flows and use today's share count, or forecast the
             future share count and use only the positive cash flows -- never both.
             This post's worked example does not extend to convertible bonds or
             preferred stock -- a gap, noted below.
Locators:    Sections "Share Based Compensation: A Sloppy Alternative" and "Share
             Based Compensation: Past option and share grants."
Quote:       n/a (paraphrase only; see prior source for the verbatim "sloppy
             alternative" quote, which recurs in this post).
```

```text
URL:         https://analystprep.com/cfa-level-1-exam/financial-reporting-and-analysis/basic-and-diluted-eps/
Kind:        Secondary. A CFA Level 1 exam-prep resource (AnalystPrep), restating the
             CFA Institute curriculum's treatment of basic and diluted EPS. Not the
             standard-setter itself (FASB/CFA Institute curriculum text was not
             directly reachable this pass -- see Discarded), but a close, uncontested
             restatement of settled accounting mechanics, used only for the parts of
             the bridge that are not contested.
Establishes: The formal definitions of basic and diluted EPS, the three categories of
             dilutive securities, and the if-converted method for convertible
             preferred and convertible debt as distinct from the treasury-stock
             method for options/warrants.
Paraphrase:  Basic EPS = (net income - preferred dividends) / weighted-average common
             shares outstanding. Diluted EPS gives effect to all dilutive financial
             instruments and "is always equal to or less than basic EPS." Three
             categories of dilutive instruments: convertible preferred stock,
             convertible debt, and options/warrants. For convertible preferred, the
             numerator drops the preferred-dividend deduction and the denominator
             adds the as-converted common shares. For convertible debt, the numerator
             is increased by after-tax interest expense (since it would disappear on
             conversion) and the denominator adds the as-converted shares. For
             options/warrants, the treasury-stock method assumes the company "utilize
             the cash gained to buy back shares at the period's weighted average
             market price," and the denominator rises only by the net increment
             (shares issued minus shares repurchased). Anti-dilutive securities --
             ones whose inclusion would raise diluted EPS above basic EPS -- are
             excluded from the diluted count entirely.
Locators:    Sections "Basic EPS," "Diluted EPS," and the worked treasury-stock and
             if-converted examples on the page.
Quote:       "diluted EPS is always equal to or less than basic EPS." / anti-dilutive
             securities "are excluded from the calculation of diluted EPS."
```

```text
URL:         https://www.wallstreetmojo.com/treasury-stock-method/
Kind:        Secondary/tertiary. A finance-education explainer site. Used only to
             confirm the uncontested three-step mechanic and its formula with a clean
             worked number; not used for any contested or judgment-dependent claim.
Establishes: The three-step treasury-stock mechanic and a worked numeric example.
Paraphrase:  "If the exercise price of the option or warrants is lower than the
             stock's market price, dilution occurs" -- otherwise the instrument is
             anti-dilutive and exercise is not assumed. Mechanic: (1) assume in-the-
             money options/warrants are exercised, (2) assume the proceeds buy back
             shares at the average market price for the period, (3) the net share
             increase enters the diluted-EPS denominator. Worked example: 10,000
             options at a $2 strike against a $2.50 average market price generate
             $20,000 of proceeds, which repurchase 8,000 shares, for a net dilutive
             effect of 2,000 shares. Does not address RSU treatment.
Locators:    "Core Formula" and "Worked Example" sections of the page.
Quote:       "If the exercise price of the option or warrants is lower than the
             stock's market price, dilution occurs."
```

```text
URL:         https://corporatefinanceinstitute.com/resources/valuation/treasury-stock-method/
Kind:        Secondary/tertiary. A second finance-education explainer, used only to
             cross-check the treasury-stock formula in algebraic form; not load-
             bearing for any contested claim.
Establishes: The algebraic form of the treasury-stock net-share-increase formula.
Paraphrase:  Additional shares outstanding = n(1 - K/P), where n = shares under
             option/warrant, K = average exercise price, P = average share price for
             the period. Worked example: 15,000 options at a $7 strike against a $10
             average price yields 4,500 net incremental shares. Does not address RSU
             or unrecognized-compensation-cost treatment.
Locators:    "Core Formula" and "Worked Example" sections.
Quote:       "Additional Shares Outstanding = n (1 - K/P)"
```

```text
URL:         https://www.wallstreetprep.com/knowledge/common-topics-of-confusion-for-investment-banking-analysts/
Kind:        Secondary. A widely used training-desk explainer (Wall Street Prep), used
             only for the plainest form of the EV/equity bridge identity and its one-
             line rationale for why enterprise value belongs to all capital
             providers; every contested or reasoned claim in the lesson instead rests
             on the Damodaran material above.
Establishes: The bare-bones identity Enterprise Value = Equity Value + Net Debt (+
             other claims), and the one-sentence rationale that EV "represents the
             value for all contributors of capital -- for both you (equity holder)
             and the lender (debt holder)."
Paraphrase:  Start from equity value, add total debt, subtract cash and cash
             equivalents, to reach enterprise value (the reverse of the lesson's own
             direction, i.e. this source builds EV from equity value rather than
             bridging EV down to equity value, so the lesson must invert it). The
             piece explicitly does not cover diluted share count, the treasury-stock
             method, RSUs, or a detailed minority-interest or preferred-stock
             treatment.
Locators:    "Primary Formula and Bridge Items" section.
Quote:       "the enterprise value represents the value for all contributors of
             capital -- for both you (equity holder) and the lender (debt holder)."
```

```text
URL:         https://stockanalysis.com/stocks/uber/
Kind:        Secondary. A market-data site, used only for Uber's closing share price
             and to cross-check that price x share count reproduces the site's own
             reported market capitalization -- not used for any balance-sheet,
             debt, or EV/enterprise-value figure, per the brief's instruction not to
             take a derived EV from an aggregator.
Establishes: UBER's closing price of $75.88 on 2026-08-13, and a market
             capitalization of $154.99 billion, which is consistent with (shares
             outstanding on the 10-Q's cover page) x (this price) -- see Numbers.
Paraphrase:  n/a beyond the two figures above.
Locators:    Landing quote page.
```

```text
URL:         https://www.google.com/finance/quote/UBER:NYSE
Kind:        Secondary. A second market-data source, used only to cross-check the
             stockanalysis.com closing price above.
Establishes: A closing price in the same range ($75.36-$75.88 depending on the
             exact timestamp read) for 2026-08-13, corroborating the price used in
             the EV back-solve below within a fraction of a percent.
Paraphrase:  n/a beyond the price cross-check.
Locators:    Landing quote page.
```

## Contradictions

- **The treasury-stock method itself is contested by the authority the brief
  names.** Uber's own diluted-EPS footnote (Note 9) and the CFA-aligned
  description both use the treasury-stock method as the settled GAAP/analyst
  convention for options and warrants. But Damodaran, across three of his own
  documents read for this record, calls it "a sloppy alternative" that
  ignores an option's time premium and has "no effective way of dealing with
  vesting," and states his own preference for pricing outstanding options
  with an option-pricing model and netting that value against equity value
  directly. Since the worked example's diluted share count comes from a
  public filing (which is legally required to use the treasury-stock/if-
  converted convention under US GAAP), the lesson should teach the
  treasury-stock method as what a filing reports and what the reader will
  meet in practice, while naming Damodaran's objection rather than presenting
  the method as beyond dispute.

- **Whether operating leases belong in net debt is a real, unresolved
  convention question, not just an editorial nuance.** Uber carries $178
  million of current and $1,830 million of non-current operating lease
  liabilities (balance sheet, p.4) under ASC 842, separate from and larger
  than its (undisclosed-separately, apparently immaterial: $82 million of
  principal payments over the first half of 2026, per the cash-flow
  statement) finance leases. Damodaran's own instruction is that "lease
  commitments" should be "converted into debt" for consistency with how
  enterprise value is measured -- i.e., operating leases belong in net debt.
  Many practitioners nonetheless net out only finance leases, on the
  reasoning that operating-lease capitalization under ASC 842 already puts a
  liability on the balance sheet that is offset by a right-of-use asset the
  bridge does not otherwise touch. The lesson should teach this as a live
  judgment call, not assert one side.

- **Whether "restricted" cash and investments should be added back as excess
  cash is a judgment call the filing itself surfaces.** Beyond the $4,870
  million of unrestricted cash and $521 million of short-term investments,
  Uber separately discloses $2,307 million of restricted cash (current plus
  non-current) and $9,486 million of restricted investments (balance sheet,
  p.4; debt-securities table, Note 2). These exist chiefly to collateralize
  Uber's self-insurance program (see MD&A liquidity discussion) and are not
  freely available to shareholders. Damodaran's own caution about "trapped"
  cash -- cash that "may be needed for its ongoing operations" and should
  not be netted off in full -- supports treating restricted cash and
  investments as unavailable for the bridge's cash add-back, but he was
  writing about tax-trapped foreign cash, not contractually restricted
  insurance collateral, so this is an extension of his reasoning rather than
  a claim he makes directly. The lesson should say plainly that "excess
  cash" excludes what is legally restricted, and that a reader must check a
  filing's own restricted-cash note before adding cash back wholesale.

- **A collateralized non-operating asset complicates a clean "subtract the
  debt, add back the stake" bridge.** As of June 30, 2026, 61% of Uber's
  Aurora Innovation stake (carried at $1,763 million; Note 2) is pledged as
  collateral for the $1,324 million (carrying value) 2028 Exchangeable
  Senior Notes, which are exchangeable into Aurora shares, not Uber shares
  (Note 5). A bridge that subtracts the exchangeable notes as debt and
  separately adds back the full Aurora stake at fair value is arithmetically
  correct but pedagogically misleading if presented as two independent line
  items: the note is very likely to be settled with the pledged Aurora
  shares themselves, not cash, so the debt and the asset are two views of
  the same collateral, not two separate claims. None of the sources read
  state a rule for this; it is this record's own observation from reading
  Note 5 and Note 2 together, flagged as a genuine complication rather than
  an authority's stated position.

- **Preferred stock can hide inside "non-controlling interest" rather than
  standing as its own bridge line.** The standard bridge (as taught by
  Damodaran and restated by AnalystPrep) treats preferred stock and minority
  interest as separate subtractions. Uber has no preferred stock of its own
  (balance sheet shows common stock only), but Note 13 discloses that the
  minority stockholders of its majority-owned subsidiary Freight Holding
  include "holders of Freight Holding's Series A and A-1 Preferred Stock" --
  a real preferred-equity claim that appears on Uber's consolidated balance
  sheet only inside the non-redeemable non-controlling-interest total ($903
  million), not as a separate preferred line. A reader following the
  textbook bridge line-by-line could miss this.

- **Book value versus fair value of debt is a live choice, and the two
  differ here.** Note 5 discloses Uber's total debt at $12,723 million book
  value but $12.9 billion fair value as of June 30, 2026 (Level 2 inputs).
  None of the authority sources read take an explicit position on which to
  use in an EV bridge; conventional practice defaults to book value for
  simplicity (which this record does, in the Numbers section below), but the
  gap is real and, for a company whose bonds trade meaningfully away from
  par, would move the answer.

- **Whether Uber's non-operating investment stakes are truly non-operating
  is arguable, not settled.** Delivery Hero (equity-method investment,
  $3,502 million, Note 3) is the subject of a signed agreement, dated July
  16, 2026, for Uber to acquire it outright; Careem Technologies (equity-
  method, $147 million) is a former Uber subsidiary and remains a related
  party; Aurora (marketable equity security, $1,763 million, Note 2) is an
  autonomous-driving technology partner integrated into Uber's own Mobility
  product. Damodaran's own framework (cross-holdings) assumes a passive
  stake with no operating tie to the parent; these three stakes have
  varying degrees of strategic and operating connection to Uber's core
  business, which is a reason a careful reader might treat some of them
  differently from a pure financial cross-holding like Grab (marketable
  equity security, $2,020 million, apparently passive). No source read
  resolves this; it is recorded as a live judgment call.

## Numbers

```text
Figure: Total debt, $12,723 million (short-term $1,997M + long-term $10,726M)
Owner:  Uber Technologies, Inc. Form 10-Q
Scope:  As of June 30, 2026; balance sheet p.4 and Note 5 debt table. Fair value of
        the same debt was $12.9 billion (Level 2), per the same note.
```

```text
Figure: Debt-instrument breakdown (book value, June 30, 2026): 2026 Term Loan $2,000M
        (4.46% stated, matures Dec 2026); 2028 Convertible Notes $1,725M (0.875%,
        conversion price ~$72.54/Uber common share); 2028 Exchangeable Senior Notes
        $1,324M (0.00%, exchangeable into Aurora Class A common stock at ~$8.50/Aurora
        share, not Uber-dilutive); 2029 Senior Notes $1,500M (4.50%); 2030 Senior
        Notes $1,250M (4.30%); 2031 Senior Notes $1,000M (4.15%); 2034 Senior Notes
        $1,500M (4.80%); 2035 Senior Notes $1,250M (4.80%); 2054 Senior Notes $1,250M
        (5.35%); less unamortized discount/issuance costs ($76M).
Owner:  Uber Technologies, Inc. Form 10-Q, Note 5
Scope:  As of June 30, 2026.
```

```text
Figure: Cash and cash equivalents $4,870 million; short-term investments $521 million
Owner:  Uber Technologies, Inc. Form 10-Q, balance sheet, p.4
Scope:  As of June 30, 2026. (Comparative Dec 31, 2025: $7,105M cash; $528M
        short-term investments.)
```

```text
Figure: Restricted cash and cash equivalents (current $661M + non-current $1,646M) =
        $2,307 million; restricted investments $9,486 million -- excluded from the
        "excess cash" add-back as not freely available (see Contradictions)
Owner:  Uber Technologies, Inc. Form 10-Q, balance sheet p.4 and Note 2
Scope:  As of June 30, 2026.
```

```text
Figure: Investments (marketable and non-marketable equity securities), $8,759 million
        total: Didi (non-marketable) $1,900M; Grab (marketable) $2,020M; Aurora
        (marketable) $1,763M; other non-marketable $2,263M; other marketable $813M
Owner:  Uber Technologies, Inc. Form 10-Q, Note 2 "Investments" table
Scope:  As of June 30, 2026. (Dec 31, 2025: $9,178M total, incl. Didi $3,011M, Grab
        $2,674M, Aurora $1,252M.)
```

```text
Figure: Equity method investments, $3,773 million total: Delivery Hero $3,502M
        (24.99% owned as of the transition to equity-method accounting during Q2
        2026); Careem Technologies $147M (~45% owned); other $124M
Owner:  Uber Technologies, Inc. Form 10-Q, Note 3
Scope:  As of June 30, 2026. (Dec 31, 2025: $287M total -- the large jump reflects
        Uber's $2.3 billion purchase of additional Delivery Hero shares during Q2 2026
        and the resulting reclassification from a fair-value security to an
        equity-method investment.)
```

```text
Figure: Redeemable non-controlling interests $180 million; non-redeemable
        non-controlling interests $903 million (combined $1,083 million)
Owner:  Uber Technologies, Inc. Form 10-Q, balance sheet p.4 and Note 13
Scope:  As of June 30, 2026. Redeemable NCI relates to Trendyol GO (put/call
        exercisable Q1 2031); non-redeemable NCI relates chiefly to Freight Holding
        (Uber owns 90% of capital stock / 84% fully diluted; minority holders include
        Series A/A-1 preferred stockholders of the subsidiary).
```

```text
Figure: No preferred stock at the Uber Technologies, Inc. parent level; common stock,
        $0.00001 par value, 2,039,994,000 shares issued and outstanding
Owner:  Uber Technologies, Inc. Form 10-Q, balance sheet p.4
Scope:  As of June 30, 2026.
```

```text
Figure: Shares of common stock outstanding, 2,042,560,121
Owner:  Uber Technologies, Inc. Form 10-Q, cover page
Scope:  As of July 31, 2026 (the filing's own record date for shares outstanding).
```

```text
Figure: Basic weighted-average shares 2,044,279 thousand; diluted weighted-average
        shares 2,060,763 thousand. Reconciling items: dilutive effect of equity
        awards +13,343K; Freight Holding contingently issuable shares +10K;
        convertible notes (if-converted) +810K; other contingently issuable shares
        +2,321K
Owner:  Uber Technologies, Inc. Form 10-Q, Note 9
Scope:  Six months ended June 30, 2026. (Three months ended June 30, 2026: basic
        2,036,458K; diluted 2,050,225K; equity awards +11,180K; Freight Holding +12K;
        convertible notes +254K; other contingent +2,321K.) Approximately 15 million
        equity-award shares were excluded as antidilutive for the six months (about 61
        million for the three months alone).
```

```text
Figure: Stock options and SARs outstanding, 6,099 thousand shares (options) + 10
        thousand (SARs), weighted-average exercise price $51.44/share, aggregate
        intrinsic value $132 million; 3,557 thousand options exercisable at
        weighted-average $41.17/share. RSUs unvested and outstanding: 71,804 thousand
        shares, weighted-average grant-date fair value $71.66/share
Owner:  Uber Technologies, Inc. Form 10-Q, Note 7
Scope:  As of June 30, 2026.
```

```text
Figure: Unrecognized stock-based compensation cost, $4.9 billion, to be recognized
        over a weighted-average period of approximately 2.93 years
Owner:  Uber Technologies, Inc. Form 10-Q, Note 7
Scope:  As of June 30, 2026. NOTE: this figure is a single blended total across all
        unvested award types (options, RSUs, ESPP); the filing does not break out
        unrecognized cost by award type, so a treasury-stock "assumed proceeds"
        figure isolated to RSUs specifically cannot be sourced from this filing. This
        is a genuine gap, not an oversight -- flag it for the writer.
```

```text
Figure: 2028 Convertible Notes -- if fully converted at the stated rate (13.7848
        shares per $1,000 principal on $1,725M principal), approximately 23.8 million
        Uber shares; but the notes require cash settlement of principal and deliver
        shares (or cash) only for value in excess of principal ("net share
        settlement"), so at $75.88/share against a $72.54 conversion price (a 4.6%
        spread), the economically dilutive share count is much smaller --
        approximately 1.0-1.1 million shares by that spread arithmetic, consistent
        with (and explaining) the small 810K/254K if-converted additions the filing
        itself reports for H1/Q2 2026 above
Owner:  Uber Technologies, Inc. Form 10-Q, Note 5 (conversion terms and net-share-
        settlement mechanic) and Note 9 (reported if-converted effect); the spread
        arithmetic above is this record's own calculation from those two disclosures,
        not a figure the filing states directly
Scope:  As of June 30, 2026 terms; spread calculated against the $75.88 close of
        2026-08-13 (see market-price figure below).
```

```text
Figure: Total Uber Technologies, Inc. stockholders' equity (book value), $27,316
        million; total equity including non-controlling interests $28,219 million
Owner:  Uber Technologies, Inc. Form 10-Q, balance sheet p.4
Scope:  As of June 30, 2026. Given only for reference -- the bridge in this lesson
        works with market values, not book equity.
```

```text
Figure: UBER closing share price $75.88 on 2026-08-13; implied market capitalization
        $154.99 billion (2,042,560,121 shares x $75.88 = ~$154,989 million,
        reconciling to the $154.99B figure reported independently by the data source)
Owner:  stockanalysis.com (market price only), cross-checked against Google Finance
        ($75.36-$75.88 range for the same close)
Scope:  Close of trading, 2026-08-13 -- one trading day before this record's
        reference date of 2026-08-14. This is a market price, not a filing figure,
        and will already be stale by the time the article publishes; the writer
        should refresh it or, better, substitute the class's own DCF-derived equity
        value in its place (see next entry).
```

```text
Figure: Illustrative enterprise value for the worked example, ~$150.9 billion, derived
        as: Market cap ($154,989M) + total debt ($12,723M) + non-controlling interests
        ($1,083M) - cash ($4,870M) - short-term investments ($521M) - investments and
        equity-method stakes, i.e. Didi/Grab/Aurora/Delivery Hero/Careem/other
        ($8,759M + $3,773M = $12,532M) = ~$150,872 million
Owner:  This record's own calculation, built entirely from the primary filing figures
        and the market price above -- not a data aggregator's derived EV.
Scope:  As of the 2026-08-13 close / June 30, 2026 balance sheet, mixed-date, stated
        plainly as an illustration. Reversing every step (add back debt, NCI;
        subtract... i.e. run the bridge forward from this EV) reproduces the $154,989
        million market cap exactly, by construction, which is the point: this EV is
        for demonstrating the mechanics of the bridge, not an independent valuation
        judgment. The writer may substitute an assumed or class-derived EV instead;
        the brief permits this as long as the basis is stated, and this record states
        it. A genuine DCF-based EV (independent of market cap) was not built for this
        record -- that would require redoing the DCF lesson's own work, which is out
        of scope here.
```

```text
Figure: Approximate per-share effect of each bridge step, computed from the figures
        above (this record's own arithmetic, not filing-stated): net debt subtracts
        roughly $3.59/share ($7,332M / 2,042,560K basic shares); non-controlling
        interests subtract roughly $0.53/share ($1,083M / 2,042,560K); the
        Didi/Grab/Aurora/Delivery Hero/Careem equity-stakes add-back adds roughly
        $6.13/share ($12,532M / 2,042,560K) -- so equity stakes, not net debt, are the
        single largest mover of Uber's per-share value in this bridge, moving it
        opposite the direction leverage does. Going from basic to diluted shares
        separately reduces per-share value by roughly 0.8% (dividing by 2,060,763K
        weighted-average diluted shares instead of 2,044,279K basic).
Owner:  This record's own calculation from the filing figures above.
Scope:  As of June 30, 2026 balance sheet figures; per-share amounts approximate,
        for illustrating relative magnitude only.
```

**Flag for the writer/orchestrator:** the commission asks for a company where
leverage and dilution both "clearly move the answer." Uber delivers a real,
filing-sourced example of every bridge component the brief asks for, and its
own diluted-EPS footnote names both the treasury-stock and if-converted
methods explicitly, which is hard to find in one filing. But the actual
dilution effect on Uber's per-share value is modest by GAAP's own count
(roughly 0.8%, not a dramatic swing), and the largest mover of Uber's bridge
turns out to be the non-operating equity stakes add-back, not net debt or
dilution. That is still a legitimate and teachable bridge -- it just does not
match the commission's implicit picture of leverage and dilution as the two
dominant forces. The larger, gross in-the-money option-and-RSU pool (about
77.9 million shares combined, Note 7) is available if the writer wants a
more dramatic illustrative number than the period's actual weighted-average
dilutive effect, with the difference between the two explained honestly
(gross grants outstanding vs. the net incremental shares GAAP's
weighted-average method actually adds for the period).

## Source assets

```text
Asset: Uber Form 10-Q, Note 5, "Components of debt" table (debt-instrument list with
       stated/effective interest rates and maturities)
Shows: The full composition of a real company's debt stack in one table -- a mix of
       fixed-rate senior notes, a floating-rate term loan, and two different
       convertible/exchangeable instruments with different dilution consequences.
Crop:  Must retain the instrument name, principal amount, and maturity columns
       together; the interest-rate columns can be dropped without losing the bridge
       argument, since only "how much debt, and does it convert to Uber shares"
       matters here.
```

```text
Asset: Uber Form 10-Q, Note 9, basic-to-diluted reconciliation table
Shows: The mechanical bridge from basic to diluted weighted-average shares, broken
       into its component adjustments (equity awards via treasury-stock method,
       contingently issuable shares, convertible notes via if-converted method) --
       this is the treasury-stock/if-converted mechanic made concrete with one real
       company's numbers.
Crop:  Must retain the basic-shares row, each named reconciling-item row, and the
       diluted-shares row together, so a reader can see which method produced which
       addition; the three-months and six-months columns can be trimmed to just one
       period without losing the point.
```

```text
Asset: Uber Form 10-Q, Note 2, "Investments" table (Didi, Grab, Aurora, other)
Shows: A real, dollar-denominated example of the "equity stakes" add-back the bridge
       calls for -- three named, recognizable companies at disclosed fair or
       estimated values.
Crop:  Must keep the company names attached to their dollar figures; the marketable
       vs. non-marketable distinction can be dropped without losing the teaching
       point, though it is worth a sentence in prose given the Aurora-collateral
       complication recorded above.
```

```text
Asset: None found in the Damodaran materials suitable for direct reproduction --
       the Cisco/Google comparison table in the ESOPs paper and the Tesla slide in
       the dilution deck are both illustrative of the same method this lesson
       teaches, but are dated (2005 and 2017-18 figures) and about different
       companies, so they would confuse rather than support a lesson built around
       Uber's own 2026 numbers. The formulas themselves are safe to restate; the
       tables are not worth cropping.
```

## Discarded

```text
URL: https://soleadea.org/cfa-level-1/earnings-per-share -- returned HTTP 403
     Forbidden on direct fetch; only a third-party search-engine summary of its
     content was seen, which is not a reliable basis for citing it as read. Not
     cited; AnalystPrep's page was used instead for the same CFA-curriculum content
     and was successfully opened and read directly.
```

```text
URL: https://ryanoconnellfinance.com/dilutive-securities-eps/ -- returned HTTP 403
     Forbidden on direct fetch. Not cited, for the same reason as above.
```

```text
URL: https://www.investopedia.com/terms/t/treasurystockmethod.asp -- fetch tool
     could not reach investopedia.com from this environment at all (blocked). Not
     cited; wallstreetmojo.com and corporatefinanceinstitute.com cover the same
     uncontested mechanic and were both reachable and read.
```

```text
URL: https://pages.stern.nyu.edu/~adamodar/pdfiles/eqnotes/valpacket2spr25.pdf --
     Damodaran's own spring-2025 equity-valuation course packet. Attempted first,
     before the more targeted documents above; the fetch tool rejected it for
     exceeding its content-size limit (a large multi-topic course PDF). Not cited;
     the more targeted Damodaran documents above (the 2013 blog post, the 2005 ESOPs
     paper, the Tesla dilution deck, and the 2018 blog post) were fetched instead and
     cover the same ground in more citable, smaller pieces.
```

```text
URL: https://ctacquisitions.com/enterprise-value-to-equity-value-bridge/ -- surfaced
     in an initial general search on the EV-to-equity bridge, but never opened
     directly (only seen as a search-result title); not read, so not cited. Not
     rejected for cause -- simply not needed once the Damodaran primary material was
     in hand.
```
