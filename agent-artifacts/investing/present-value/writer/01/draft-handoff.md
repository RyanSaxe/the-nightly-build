# Draft handoff: investing/present-value (writer 01)

## Original work

This lesson performs one reproducible computation the sources never do
themselves: it discounts a concrete four-year $100 stream at the real 4.75
percent risk-free rate to a single $356.67 present value, then re-runs the same
mechanism at a higher risk-adjusted rate to turn the evidence's risk-free-floor
vs. cost-of-capital distinction into an operational rule (raise the rate, every
value today falls). The sources supply the abstract identity, the perpetuity
forms, and the one real rate separately; the article is where they are joined
into an arithmetic the reader can redo with a calculator.

Visible in: the worked table in "From one payment to a stream" and the
illustrative $100-at-10-percent contrast (~$317 vs ~$357) in "Risk lifts the
rate and lowers the value."

## Framing correction handled

The brief's CRITICAL note is applied. The only real sourced rate (10-year U.S.
Treasury par yield, 4.75% as of 07/31/2026) is presented as the risk-free floor,
never as a company's cost of capital. The worked table discounts explicitly
risk-free-shaped cash flows at 4.75%. A separate section builds the cost of
capital above that floor (risk-free + risk premium), links back to the
cost-of-capital/WACC lesson without re-deriving it, and shows the risky rate
lowers present value. The invented cash flows and the flat-rate/no-tax choices
are flagged in-text as teaching simplifications (the tax point cited to
Damodaran's own note).

## Proof result

`nb check` (links on, against the library checkout): **BLOCK: 0**, verdict
PUBLISHABLE.

## Warning intentionally left

- **W-SOURCES-MIN: 4 sources; series floor is 6.** The evidence record opened
  only four citable sources (Damodaran "The Time Value of Money"; U.S. Treasury
  par yield curve; Bigel/LibreTexts growing perpetuities; Corporate Finance
  Institute). All four are cited and used. The two discarded record entries were
  rehosts/weaker duplicates the record explicitly rules out, and this is a
  formula-teaching piece where the standard warns against padding citations.
  Adding two sources to clear the floor would mean either citing evidence the
  researcher did not open or decorating with duplicate explainers, both barred
  by the citation standard. Left as a WARN (not a BLOCK).

## Open question for the orchestrator / next round

If the lesson floor of 6 must be met, it is a research gap, not a writing one:
the researcher would need to open two more independent, citable primaries (for
example, a second authority stating the single-cash-flow discount identity, and
a primary source for the perpetuity/terminal-value intuition) through a new
evidence artifact. The writer did not expand the claim set to reach the count.
