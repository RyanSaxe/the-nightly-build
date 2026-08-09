# Commission: investing/valuation-multiples

## What this lesson teaches and why now

The course has just finished building intrinsic value from the ground up:
present value, free cash flow, cost of capital, and the discounted-cash-flow
model that ties them together. The natural next concept is the one every
practitioner actually reaches for first and the course has not yet taught: the
valuation multiple. A reader who can run a DCF but cannot say what a price-to-
earnings ratio means is missing the tool markets quote in, and the tool that
lets them sanity-check a DCF in one number.

Teach two or three ideas, completely, in this order:

1. What a multiple is and how a comparables valuation works: a ratio of price
   (or enterprise value) to a fundamental (earnings, EBIT, EBITDA, sales, book),
   used to price one business off what the market pays for similar ones.
2. Why a multiple is a DCF compressed into a single number. Derive a justified
   multiple from the same inputs the DCF lesson used, so the reader sees that
   growth, the reinvestment or payout it demands, and the cost of capital are
   what a multiple silently encodes. This is the lesson's spine and the place
   for the template's math furniture.
3. The consequence that makes multiples dangerous in untrained hands: a low
   multiple is not automatically cheap and a high one is not automatically dear,
   because two businesses with different growth, returns on capital, and risk
   deserve different multiples. Comparing multiples is comparing implied DCFs.

Keep the destination in view without teaching it yet: a later lesson can turn
the justified-multiple relationship into a screen or a model. This one
establishes the judgment that screen would encode.

## Template, sources, tags

- Template: `lesson`. Fixed order: Why this matters bookend, body, The takeaway
  bookend, written after the body. 1200 to 2200 words. Two or three ideas taught
  completely beats six in passing.
- Link the discounted-cash-flow, cost-of-capital, and free-cash-flow lessons in
  Background rather than re-teaching them.
- Source floor: 6. Ground the definitions and the justified-multiple derivation
  in a recognized valuation authority (a standard text or curriculum, not a
  blog), and ground the worked contrast in real, current figures for named
  companies verified against the filings or a data source that owns them.
- Tags: valuation, multiples, relative-valuation (metadata only; writer sets
  them in `nb-meta`).

## Production policy (resolved)

Run's model is Opus 4.8 across roles. Effort per `nb production-policy`:
writing-coach low, researcher high, writer medium, editor high (required).
Harness `claude-code-routine`; published `model` field reads `Opus 4.8`.

## Distinct value and habits not to inherit

The course keeps reaching for the same two companies: Costco anchors several
recent lessons and Apple anchors free-cash-flow. Do not build the worked example
on Costco or Apple. Pick companies whose contrast makes the "cheap is not cheap"
point land, for instance a high-growth business and a slow, stable one whose
different justified multiples the reader can feel. The DCF lesson opened on a
striking share-of-value number and closed on a "is the tool broken or the hand"
turn; do not reuse either shape. The Why/takeaway bookends and the Sources
heading are required furniture, not formula.

## Boundaries

One lesson, this slug. Teach relative valuation and the fundamentals behind a
multiple. Do not drift into a full company walkthrough or into automation. Stay
within the word band.
