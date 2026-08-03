# Editorial review: investing/present-value (editor/01)

## Skeptic

Thesis: a future dollar is worth less than one today by exactly the return you
forgo while waiting; you convert future cash to a value now by dividing it by
(1+r)^t, sum a stream term by term, build the rate as a risk-free floor plus a
risk premium (which is the cost of capital from the prior lesson), and extend
the same machinery to never-ending cash with the perpetuity forms. That is the
spine of every DCF the course will later build.

Load-bearing claims and how they held:

- **A future dollar is worth less, for three reasons (time preference,
  inflation, default).** Attributed to Damodaran, slide 2. Correct and owned.
- **The discount rate is an opportunity cost.** Damodaran slide 3. Correct.
- **The real anchor is a risk-free rate of 4.75% (Treasury, 07/31/2026).**
  Opened the Treasury page as printed; the 07/31/2026 row reads 10 Yr = 4.75%.
  Opened the FRED DGS10 page; title and source match, latest observation 4.68%
  on 07/30/2026. The two figures are attributed to distinct owners, dates, and
  constructions (par yield vs constant-maturity investment basis) and are
  explicitly not presented as a disagreement. Not blurred. This satisfies the
  round focus.
- **PV = CF/(1+r)^t.** Recomputed: $100/1.0475 = $95.47; check $95.47 x 0.0475
  = $4.53, back to $100.00; $100 x 1.0475 = $104.75. All correct. The annotated
  equation and its CF/r/t legend are right, and each symbol is named where it
  acts, per the voice guide.
- **A stream is the sum of discounted terms.** Recomputed the table at 4.75%:
  year 1 $95.47, year 2 $91.14, year 3 $87.00, year 4 $83.06. The displayed
  rows sum to $356.67, and $400 - $356.67 = $43.33, matching the prose. (The
  unrounded PV is $356.66; the one-cent gap is the ordinary rounding of
  per-row-rounded values, internally consistent for a reader who re-adds the
  column, so no fix.) The 10% contrast checks out: the same four years discount
  to $316.99, i.e. "about $317 rather than $357."
- **CRITICAL: risk-free floor vs cost of capital.** The piece never calls the
  Treasury yield the cost of capital. The orientation calls 4.75% "close to the
  pure price of waiting"; the table caption calls it "the risk-free 4.75 percent
  rate"; the risk section states a risky payment is discounted at "the risk-free
  figure as a floor, plus a premium for the risk on top of it," cited to OpenStax
  15.3 (verified: Re = Rf + risk premium, Treasury securities as the risk-free
  proxy). Only the higher floor-plus-premium rate is identified as "the cost of
  capital the previous lesson built," and the takeaway repeats the correct
  framing. The worked table discounts illustrative cash flows at the risk-free
  rate and labels them illustrative; the very next section moves risky cash to a
  higher rate. The framing is correct throughout. No fix required.
- **Perpetuity PV = CF/r and growing PV = CF1/(r-g), r > g, CF1 = next year.**
  Verified against OpenStax 8.1 and Bigel 11.20 (both opened): forms correct,
  the r > g hard constraint is stated and owned, CF1 is correctly the next-year
  flow, and the g = 0 collapse to CF/r is sound (also implied by s7).

Display text: headline "A dollar next year is worth 95 cents today" is a claim
the piece defends ($95.47 rounds to 95 cents at 4.75%). The dek makes a claim
about the mechanism, not a grade of the article's method, and avoids the spent
company-plus-number mold. All five section headings are argument steps in the
piece's own nouns, varied in shape, none scaffolding slots, none repeating the
comma-and cadence. No false label found.

data-nb-kind audit: s1 Damodaran, s2 Treasury, s3 FRED, s5/s6/s7 OpenStax,
s8 Bigel all primary; s4 CFI secondary. Each matches the evidence record and
the nature of the owner. Correct.

Citations: opened all eight source hrefs plus the two Go-deeper links as
printed. Every one resolves and lands on the source itself (the Damodaran href
is the primary PDF artifact; Treasury and FRED return the exact quoted figures;
OpenStax 9.1/15.3/8.1, Bigel 11.20, CFI, and BetterExplained all return the
cited content). Locators match the evidence record. The round-02 additions
(FRED, OpenStax 9.1/8.1/15.3) each attach to an existing load-bearing statement
as a genuine second owner, not decoration to clear the floor.

No break found that retires a claim. Nothing routed to the researcher.

## Cut

The piece is disciplined; the tells were few and local.

- Worst tell: the "Why this matters" opener carried a table-of-contents
  signpost, "It covers why a later dollar is worth less than one now, how to
  move a single future payment back to today, and how to add up a run of them"
  — a comma triad previewing the article's own method, made redundant by the
  concrete "By the end you should be able to..." sentence that follows. Cut.
- "Hold that number; the rest of the lesson runs cash flows through it" paired
  a reflex semicolon with a where-the-piece-goes signpost, and the imperative
  carried no operation the reader redoes. Cut the whole sentence; the section
  now ends on "close to the pure price of waiting."
- "The gain here is that the same number now has a second job" announced the
  payoff before making it. Trimmed the frame so the fact stands on its own.
- One reflex semicolon repaired to a period ("...not a real security. Only the
  rate is a real figure.").

No repeated structural formula across the piece. One semicolon survives (the
healthy-company contrast), a legitimately tight pairing within the rare
allowance. The single sustained comparison (rate as speedometer) is licensed,
holds at the point taught, and is retired once the mechanism stands in its own
terms. No prompt leakage: the "cash flows are illustrative" disclosure is
honest sourcing, not copied instruction. Furniture (annotated PV equation,
worked table, growing-perpetuity equation) each carries evidence the prose
would hide, and each earns its place.

Minor, non-blocking: the byline reads "8 min read" while the stamped meta now
reads reading_minutes 9. Reading time is approximate and this predates the
round; a furniture nit for the writer, not a publication blocker.

## Reader

Read straight through, the lesson gives what no single source does: one by-hand
pipeline that carries a reader from discounting a single $100 payment, to a
summed four-year stream at a real Treasury rate, to the risk-premium step that
connects the discount rate back to the prior WACC lesson, to the perpetuity
shortcut that sets up terminal value and DCF, with every figure reproducible on
a calculator. The original-work sentence in the handoff (discount a concrete
$100 stream to $356.67 at the risk-free rate, then re-run at a higher rate into
the rule "raise the rate, every value today falls") survives intact and is the
piece's spine. Both answers hold; this is synthesis, not restatement. The prose
sits close to the voice-guide exemplars (Olah's part-by-part walk of the
equation, Azad's compute-in-front build with small numbers) rather than a
median summary. The takeaway names DCF as the deferred next step without
overreaching.

## Edits

- Cut the method-preview triad "It covers why a later dollar is worth less than
  one now, how to move a single future payment back to today, and how to add up
  a run of them." from the "Why this matters" bookend.
- Cut the sentence "Hold that number; the rest of the lesson runs cash flows
  through it." from the orientation section (signpost + reflex semicolon).
- Trimmed "The gain here is that the same number now has a second job" to "The
  same number now has a second job" (self-grading frame removed).
- Repaired a reflex semicolon: "...not a real security; only the rate is a real
  figure." to "...not a real security. Only the rate is a real figure."
- Ran `./nb stamp` after the cuts: words 1980, reading_minutes 9, sources 8.

## Required work

None blocking. Optional, writer: reconcile the byline "8 min read" with the
stamped reading_minutes (9) if desired; non-blocking, as reading time is an
estimate.

## Decision

approve — the critical risk-free-floor-vs-cost-of-capital framing is correct
throughout, all arithmetic and equations recompute, every citation resolves to
its source with the right kind, the two rate figures are cleanly attributed to
distinct owners, and the remaining tells were removed by surgical cut.
