# Draft handoff: investing/present-value (writer 02)

## Original work

Unchanged from round 01. This lesson performs one reproducible computation the
sources never do themselves: it discounts a concrete four-year $100 stream at
the real 4.75 percent risk-free rate to a single $356.67 present value, then
re-runs the same mechanism at a higher risk-adjusted rate to turn the evidence's
risk-free-floor vs. cost-of-capital distinction into an operational rule (raise
the rate, every value today falls). Visible in the worked table in "From one
payment to a stream" and the $100-at-10-percent contrast in "Risk lifts the rate
and lowers the value."

## Round-02 changes (evidence expansion only; no new claims)

- Attached FRED DGS10 (Board of Governors, constant-maturity 4.68% on
  07/30/2026) to the existing 10-year Treasury anchor as a second independent
  owner. Each rate is attributed to its owner and date; the 4.75% par vs 4.68%
  constant-maturity gap is stated as a construction/date difference, not an
  error. 4.75% remains the working number the lesson runs cash flows through.
- Attached OpenStax §9.1 (Timing of Cash Flows, Eq 9.12) as a second owner of
  the single-cash-flow PV identity (equation figure) and of the discount-each-
  flow-then-sum method (the stream sum).
- Attached OpenStax §8.1 (Perpetuities, Eq 8.1 and 8.3) as a second owner of the
  plain-perpetuity form PV = CF/r and the growing-perpetuity form PV = CF1/(r-g).
- Attached OpenStax §15.3 (CAPM, Eq 15.12) to the existing "risk-free floor plus
  a risk premium" sentence. This closes the round-01 gap: a named authority now
  owns the required-return buildup Re = Rf + risk premium and the use of Treasury
  securities as the risk-free proxy. Framing preserved: the Treasury/FRED rate is
  the floor, not a company's cost of capital.
- Renumbered all sources in first-citation order: 1 Damodaran, 2 Treasury,
  3 FRED, 4 CFI, 5 OpenStax 9.1, 6 OpenStax 15.3, 7 OpenStax 8.1, 8 Bigel. All
  settled prose preserved; the only new sentence is the FRED attribution
  required to keep the two rate owners distinct.

## Proof result

`nb check` (links on, against the library checkout): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. Source count: **8** (7 primary, 1 secondary). The round-01
W-SOURCES-MIN warning is cleared (8 vs floor 6).

## Warnings intentionally left

None.

## Open questions

None.
