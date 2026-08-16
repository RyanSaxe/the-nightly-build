# Commission: investing/margin-of-safety

## Where this sits in the course
The published lessons have built a complete valuation machine: return on
capital, cost of capital, present value, the discounted cash flow, free cash
flow, multiples, the value of growth, how long a moat lasts, and the bridge from
enterprise value to a price per share. Three of those lessons taught the same
uncomfortable fact from different directions: the answer moves a lot when the
inputs move a little. Terminal value was three-quarters of a DCF and its
shakiest part, a single point of growth swung the whole valuation fifteen
percent, extending a moat from four to fifteen years roughly tripled the value,
and at one growth rate a higher return on capital was worth four times a lower
one.

This lesson teaches the decision that fact forces: because an intrinsic value is
a range and not a number, an investor's protection is the gap between that value
and the price paid. That gap is the margin of safety. It is the concept that
turns the machinery already taught into a rule for acting, and it is the natural
next prerequisite before any lesson on building a model or a portfolio.

## What the lesson must teach
- An intrinsic value is an estimate with a spread, not a point. Make this
  concrete by building a conservative and an optimistic value for one real
  company from its own filing, using only tools earlier lessons established
  (return on capital, reinvestment and growth, cost of capital, terminal value).
  The spread is the lesson's central exhibit, not an aside.
- The margin of safety is the discount of price to a conservative estimate of
  value. It absorbs estimation error and ordinary bad luck. Show what price
  would offer a real margin against the range built above, and what price would
  leave none.
- The required margin scales with the uncertainty of the business, not with the
  investor's mood. A stable, predictable earner justifies a smaller discount; a
  business whose value hinges on inputs that could plausibly land anywhere needs
  a larger one, or is simply uninvestable at any honest price.
- Margin of safety is about price, and it is distinct from business quality. A
  genuinely good company bought too dear has no margin. This is where the course
  separates a good business from a good investment.

The lesson's own contribution is to connect the estimation uncertainty the last
several lessons demonstrated to a single sizing rule, made concrete on one
company's numbers, rather than restating Graham's slogan.

## Boundaries
- This is investment judgment, not personal-finance advice and not a
  buy/sell call on the anchor company. The anchor exists to make the range real.
- Rely on earlier lessons instead of re-deriving them. Reintroduce a term only
  in one clause where the reader needs it, then move on.
- The concept traces to Graham and Dodd; teach the reasoning from first
  principles in the paper's register and cite Graham for the idea's statement,
  not as the argument.

## Sources
Template floor is 6 sources. Expect: Graham's statement of the concept (The
Intelligent Investor, and Security Analysis where useful); a serious treatment
of estimation uncertainty in valuation (Damodaran on the range/uncertainty of
intrinsic value is the natural fit); and the anchor company's own most recent
filing for every number in the worked range. The researcher selects the anchor
company (constraints below) and builds both ends of the range from primary
filings.

## Anchor company (researcher selects, then reports the pick)
Choose one company whose intrinsic value genuinely turns on uncertain inputs, so
the margin concept bites, and whose latest 10-K or 10-Q supplies the figures to
build both a conservative and an optimistic per-share value. Avoid re-centering
companies the course has already built lessons around (Uber, Costco, Apple,
Coca-Cola, Verizon, American Electric Power, Copart, Crocs). Report the chosen
company and the conservative/optimistic per-share figures in the handoff.

## Habits to break (recent investing desk)
Recent lessons open on "what the [shortcut/terminal value] leaves out or takes
on faith" and are built as a two-named-company head-to-head. This lesson is one
company's value against its price, so do not force a second company in for
contrast, and find an opener that is not "what X takes on faith." Deks have been
quantitative one-line punches ("worth four times", "roughly triples"); a figure
in the dek is fine, but vary the construction. Use nb-math and nb-table where
the arithmetic of the range and the discount is the point, not as decoration.

## Neighbors this run
Five other articles are in production in unrelated series. No cross-reference is
needed.

## Production record
- Harness: `claude-code-routine`. Writer model recorded in nb-meta: `claude-opus`.
- Effort by role: writing-coach low, researcher high, writer medium, editor high
  (required). Roles run as in-process children on the routine's session model;
  where a stage's configured effort cannot be set explicitly, the closest
  available setting on that model is used. No `required` directive was traded
  down.
- Source policy: `{"templates": {"lesson": {"min_sources": 6}}}`.
