# Voice guide: investing/free-cash-flow

Register: plain, first-principles, unhurried — the paper's default (Hashimoto's
calm precision, Olah/Weng's patience for building a concept before the sentence
that needs it). Nothing here replaces that default. Reader relationship: a
teacher standing beside the reader at the spreadsheet, working the same numbers
they are, not a lecturer standing ahead of them with the answer already found.

Two moves should change sentences in this article:

1. **Build the definition and its worked figure in one motion.** Don't write a
   paragraph that defines a term (capex, working-capital change, the non-cash
   add-back) and then a separate paragraph or section that demonstrates it.
   State what the term means, and in the same breath or the next sentence, give
   it its real number from the worked example. Each step of the build — start
   from operating cash flow, add this back, subtract that — earns its dollar
   figure the sentence after it is named, not three paragraphs later. The
   definition and the arithmetic are a single motion, not two.
2. **Let the two bookends run the same argument at two different altitudes.**
   Why this matters should name, concretely, the way this number gets misused
   or misread — not "FCF matters because it's important," but the specific
   failure mode a reader will otherwise fall for. The takeaway should hand back
   the specific test that catches that failure, stated as a judgment the reader
   can now make on any company's numbers. The takeaway is not a recap of the
   calculation; it is the opener's warning, now answered with a tool.

## Licenses

```text
form: bounded second-person address during a calculation pivot
move: the exemplars below switch to direct "you" address exactly at the
      moment the reader must personally take the next step of a
      calculation or judgment — deciding which cash flow variant to use,
      deciding what to do with a genuinely ambiguous line item — then drop
      back to plain declarative explanation once that step is placed.
bar:  only at a real fork in the calculation (operating cash flow to free
      cash flow; which variant to build; how to treat one ambiguous line).
      Never as an opener, never filling a sentence that adds no new step.
      A small handful of uses across the whole body, not a running habit.
```

No other form is licensed. The lesson register is plain by design; leave
metaphor, wit, and extended analogy at the house default.

## Recently used, do not reuse

Checked against `profit-versus-cash` and `return-on-capital` (the two prior
lessons this one continues from) via `nb history --structure`, per the
commission's continuity instruction. These are negative constraints only, not
voice exemplars — do not read the prior lessons for how to sound.

- **The paradox opener.** Both prior lessons open with "[A company / two
  things] can do X and still / not do Y, because —" before naming the
  concept. Do not open this lesson the same way.
- **The colon-definition that follows it.** Immediately after the paradox,
  both name the concept as "the number built to catch that difference," or
  restate it as two paired abstractions joined by a colon ("what a business
  has earned... and what has actually moved..."). Avoid this exact move.
- **The generalizing takeaway closer.** Both takeaways end by declaring the
  specific worked case transferable in general terms — "applies to any
  company's own income statement and balance sheet, not just these two," "that
  comparison... is what tells an investor whether a business is worth
  owning." Resolve this lesson's opener with its own specific tool, not this
  formula.
- **The aphoristic mid-body closer.** `profit-versus-cash` drops a single
  short declarative sentence as its own paragraph-closer ("Cash is what
  already happened."). Don't reach for this shape here.
- **Paired-heading callbacks.** `profit-versus-cash` runs "When a sale and its
  cash land in different years" against "The same gap, running the other
  way." `return-on-capital` runs "The money behind the profit" / "The number
  growth has to clear." Vary the heading shape; don't build this lesson's
  headings as an echoing pair or a "the [noun] behind/that [verb]s the
  [noun]" formula.

## Aswath Damodaran, "Earnings and Cash Flows: A Primer on Free Cash Flow"
Source: https://aswathdamodaran.blogspot.com/2022/10/earnings-and-cash-flows-primer-on-free.html
Craft:
- cadence: a sentence defining a term is followed immediately by a sentence
  giving that term's real number; a paragraph runs long only while one
  calculation is still unresolved, then breaks the instant it lands.
- argument: opens by naming the field's actual malpractice (free cash flow
  stretched to mean adjusted EBITDA, "community-adjusted EBITDA") before
  defining the term correctly, so the correct definition arrives as a fix to
  a named problem, not a formality.
- evidence: every claim is built off one real, dated filing (Microsoft's FY
  2021 cash-flow statement), never a hypothetical company; commits to the
  exact dollar figure at each intermediate step ($41,901 million pre-debt,
  $36,397 million after debt), not just the final answer.
- stance: takes a side on a contested line item and says so in the first
  person — "I do not add back stock-based compensation, and will provide a
  rationale" — instead of listing both views and declining to choose.
- notice: spends the most words on the one place the calculation is most
  often gamed (stock-based compensation, capitalized R&D), and moves fast
  through the routine steps.
- diction: plain verbs carry the action (nets out, adds back, wrestles with);
  each abbreviation (FCFE, FCFF) is spelled out in full once, then reused by
  its initials exactly, never re-expanded for variety.
- reader: talks the reader through each fork as if standing beside them at
  the spreadsheet — "you have to define...", "you will wrestle with..." —
  not from ahead of them with the answer already known.
- the move the axes miss: the piece's opening promise (definitions get abused,
  here is the real one) and its closing verdict (even a cash-flow advocate
  should mostly stick to earnings multiples for pricing) are the same
  argument run twice — first as a warning, then as an earned conclusion that
  cuts against the writer's own priors. The close teaches nothing new; it
  cashes out the stance the opener took.

## Marc Rubinstein, "Banks in Disguise"
Source: https://www.netinterest.co/p/banks-in-disguise
Craft:
- cadence: a short narrative beat (Starbucks relaunching its gift card in
  2008) runs before any number appears; once numbers start, one new figure
  per sentence, each sized against a figure already placed.
- argument: states the reframing before any evidence ("a bank dressed up as a
  coffee shop"), then spends the section making the reader see the reframing
  is literal, not decorative.
- evidence: no number appears without a comparison the reader already owns —
  "$1.9 billion of stored value... 85% of US banks have less than $1 billion
  in assets" — and the comparison lands one sentence before the mechanism
  that explains why it matters, so the surprise is felt before it is named.
- stance: discloses a personal stake plainly where relevant ("Full
  disclosure: I'm an angel [investor]") instead of writing around it.
- notice: catches and quantifies the exact mechanism a casual reader would
  miss — Starbucks profits from money customers forget to spend — and gives
  the rate (13% of stored balances) and its direction of travel (up from
  11%), not just the fact that it happens.
- diction: one technical term per mechanism (breakage), never swapped for a
  synonym.
- reader: conversational and confiding, but the confiding never substitutes
  for the arithmetic — every aside still resolves into a figure.
- the move the axes miss: he reuses the same defined term in a second
  company's section before moving to the next idea ("Like at Starbucks,
  though, there is also breakage...") — planting that the term generalizes
  while the reader is still inside a related case, instead of defining it
  once and trusting the reader to remember it three sections later.

## Patrick McKenzie, "Accounting for SaaS and swords"
Source: https://www.bitsaboutmoney.com/archive/accounting-for-saas-and-swords/
Craft:
- cadence: states the puzzle as a puzzle before resolving it (what does a
  purchased-but-unused virtual sword deserve, accounting-wise?), then works
  backward through the layers of substance underneath the fiction, one layer
  per paragraph.
- argument: draws a hard two-way distinction early (a consumed potion vs. a
  banked sword) and holds it rigidly through every later example, never
  blurring which bucket a new case belongs to.
- evidence: applies a real accounting test to a case chosen to be unfamiliar
  (game currency), so the reader has to reason from the rule instead of
  pattern-matching a case they already know.
- stance: admits a past misjudgment directly — "you were in excellent company
  in being totally wrong" — rather than writing as if the right answer were
  always obvious in hindsight.
- notice: catches that the same accounting question recurs in a completely
  different, more consequential domain (SaaS deferred revenue), and makes the
  reader do the term-for-term mapping explicitly rather than asserting the
  parallel.
- diction: coins one working label for the general pattern early, then reuses
  that exact label at each new instance instead of re-describing the pattern
  from scratch.
- reader: trusts the reader to follow a genuinely counterintuitive case
  rather than offering a simplified stand-in for it.
- the move the axes miss: the essay's real payoff is not the accounting
  answer to the game-currency question, it's proving that one three-part test
  resolves both a curiosity and a serious business question, stated
  explicitly at the end. That is the shape this lesson's own takeaway needs —
  the worked example resolved, then named as the general test it actually is.
