# Commission: investing/capital-allocation

## Assignment
Teach **capital allocation**: what management does with each dollar of free cash
flow the business throws off, and why that choice creates or destroys value. The
five uses to teach are reinvestment in the business, acquisitions, share
buybacks, dividends, and paying down debt. The test that decides among them is
the one the course has already built: a use creates value only when the return
it earns clears the cost of capital, and a buyback creates value only when the
shares are bought below intrinsic value.

## Why this is the next lesson
The archive has built the full single-security valuation machine: return on
capital, cost of capital, present value, free cash flow, DCF, multiples, the
value of growth, competitive advantage, the enterprise-to-equity bridge, margin
of safety, and reverse DCF. The reader can now value a business but has not been
taught to judge what management *does* with the cash that value throws off.
Capital allocation is the judgment that sits on top of the valuation lessons and
turns them toward an actual investment decision. It relies on earlier lessons
rather than restarting them.

## Angle and required contribution
Rely on the taught concepts (return on capital vs. cost of capital, the value of
growth, free cash flow) instead of reteaching them; cite or point to them where
a reader needs the bridge. Use one concrete company to make each choice real,
but keep the lesson transferable: the reader should leave able to judge any
company's allocation, not to recite one company's history. Do not default to a
quarterly-earnings walkthrough. The reader finishes able to look at where a
company sends its cash and say whether that choice adds or destroys value, and
why. Make the buyback case precise: a buyback below intrinsic value transfers
value to remaining holders; above it, the reverse.

## Boundaries
- Template `lesson`: 1200-2200 words, 0-4 flex sections between the fixed
  bookends, minimum 6 sources, per-section citation. The `why` and `takeaway`
  bookend cards are citation-exempt and may address the reader directly (the one
  allowed self-reference); the body may not.
- Sources: company filings for the concrete figures, and authoritative texts on
  capital allocation and return-on-capital for the framework.

## Production record
- Correspondent (coach + research + draft + self-proof): model
  `claude-sonnet` tier, high effort for research.
- Editor (fresh eyes, required): model `claude-opus-4-8`, high effort.
- nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date
  `2026-08-21`.
- Proof: `nb check .nb-work/investing/capital-allocation/library/investing/capital-allocation.html --series investing --library /home/user/library-checkout`

## Recent patterns to break
- Dek: avoid the numeric-contrast-"at once" mold ("a 12% premium and a 30%
  discount at once", "worth roughly triple"). Write a dek that names this
  lesson's own claim.
- "Why this matters": do not open on a sweeping generalization ("Every price in
  the market is a bet on the future…", "Every valuation you can build returns a
  single number…").
- Do not include a "Verdict" section on top of "The takeaway"; recent lessons
  stacked both. The takeaway is the close.
- Avoid the imperative aphorism as the final sentence ("Quote the implied number
  with the assumptions that produced it, never on its own").
- Let the concept choose the body sections; do not inherit the rigid
  "Background list → math/table → Verdict" shape.
