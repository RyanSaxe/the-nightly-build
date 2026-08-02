# Commission: investing/cost-of-capital

## Assignment
The next lesson in the cumulative Investing Course. Teach **the cost of capital
(the hurdle rate)**: the return investors require to fund a business, why it is
the yardstick against which return on capital is judged, and the rule that a
business creates value only when its return on invested capital exceeds its cost
of capital (and destroys value below it).

## Where this sits in the course
Published so far, in order:
1. `how-a-business-earns-a-profit` (income statement, margins)
2. `profit-versus-cash` (cash flow, accrual vs cash, working capital)
3. `what-a-company-owns-and-owes` (balance sheet, book value, goodwill)
4. `return-on-capital` (ROIC: profit per dollar of invested capital; ended on
   "the test that decides whether a company's growth creates value or destroys
   it")
The ROIC lesson set up exactly this one: ROIC only means something against a
required return. This lesson supplies that yardstick and the value-creation rule.
It leaves ground for a later lesson to discount future cash flows into a value.

## What to teach (keep it to 2-3 ideas taught completely)
1. **Cost of capital = opportunity cost = required return.** A dollar invested in
   this business must beat what investors could earn elsewhere at the same risk.
   Riskier businesses carry a higher required return. Ground it with a worked
   number: the risk-free rate (a current US Treasury yield) plus a premium for
   risk.
2. **Where the number comes from, at a high level: WACC.** A firm is funded by
   debt and equity; the cost of capital is the blended (weighted-average) return
   both require. Explain cost of debt (roughly the interest rate it pays, after
   tax) and cost of equity (the higher return shareholders require because they
   are paid last) in plain terms. Teach the intuition and the weighting; do NOT
   turn the lesson into a CAPM derivation — introduce beta only as far as "equity
   in a riskier business demands more," and say plainly what is being
   simplified.
3. **The value-creation rule: ROIC vs the hurdle.** Value is created only when
   ROIC > cost of capital; growth multiplies value above the line and destroys it
   below. Make it real with the two cases the ROIC lesson already introduced:
   Costco (high ROIC, well above any reasonable hurdle) and a regulated utility
   near its allowed return (American Electric Power, whose regulators set an
   allowed return that *is* essentially a cost-of-equity determination). Use
   their real, cited figures to show a company earning above vs at/near its
   hurdle, and what that means for whether growth helps.

## Reader / mode / template
The lesson reader: smart, widely read, new to this subject. Explain everything
finance takes for granted. mode open; template `lesson` (1200-2200 words). Fixed
order: "Why this matters" bookend, body, "The takeaway" bookend — write both
bookends AFTER the body. Background band may link earlier lessons (e.g.
`return-on-capital`) instead of re-teaching; Go deeper links beyond this paper.
The lesson must work for a reader who opens none of the links.

## Source obligations
- Template floor: **minimum 6 sources**; per-section citation (bookends exempt).
- Concepts: cite an authoritative corporate-finance source (e.g. a standard text
  such as Berk & DeMarzo or Brealey/Myers, or Aswath Damodaran's published
  material) for the definitions of cost of capital, WACC, cost of debt/equity,
  and the value-creation rule. Prefer primary/authoritative over blog restatement.
- Real figures: cite **primary** filings for company numbers (Costco and AEP
  10-K/annual reports for the ROIC inputs already used in the prior lesson; reuse
  consistent figures), a **primary** current US Treasury yield (Treasury/FRED)
  for the risk-free rate, and AEP's regulators' **allowed return on equity** from
  a primary regulatory/utility source. Verify every number against its owner.
- Every URL resolves; keep estimates, reported facts, and synthesis distinct.

## Structures not to inherit
Prior lessons lean heavily on Costco and open on a company fact as the hook. Use
the companies to make the idea real, but do not default to a company walkthrough
or a quarterly-earnings frame; let the concept drive the form. Vary the opener
and headings from the prior lessons' shapes.

## Neighboring articles tonight
word-of-the-day, current-events, tech-news, paper (ML), parenting. Investing is
the only markets/finance teaching piece; no overlap.

## Output paths
- Article: `.nb-work/investing/cost-of-capital/library/investing/cost-of-capital.html`
- Artifacts under `agent-artifacts/investing/cost-of-capital/`.

## Harness / model (balanced profile)
harness `claude-code`; writing-coach `claude-sonnet-5`/low; researcher
`claude-sonnet-5`/high; writer `claude-sonnet-5`/medium (record in nb-meta);
editor `claude-opus-4-8` (inherit)/high, required.
