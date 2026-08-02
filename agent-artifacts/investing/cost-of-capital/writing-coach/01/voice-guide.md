# Voice guide: investing/cost-of-capital (01)

## Directive

Write like a patient teacher walking one reader through a decision they will
actually have to make, not like a reference entry defining a rate. The house
register (calm, first-principles, Olah/Weng patience) is the floor. What this
lesson needs on top of it: put the reader inside the calculation instead of
beside it, converge on the term's definition from more than one angle before
you commit to it, and back every general claim about value creation with more
than one company's worth of evidence. Cost of capital is easy to teach as a
formula and hard to teach as a constraint that bites; write for the second
one. Open Why This Matters on the cost of getting the hurdle wrong — a real
project cleared or killed by the number — not on the definition itself; the
definition can wait a paragraph, the stakes cannot.

## Licenses

```text
form: second-person walkthrough of the worked numeric case
move: Damodaran and Hobart both drop into "you" when they reach the point
      where the reader has to actually do the arithmetic — "if you are
      considering investing in a new asset, you have to earn more than you
      could make elsewhere" — then return to third person once the concept
      is established. It is not a standing address to the reader; it is a
      tool for the one paragraph where the reader is meant to be the decision
      -maker running the numbers.
bar:  Used only inside the worked example(s) where the reader computes or
      compares a return, never in the framing prose around them. Must
      disappear the moment the example ends. One sustained use per worked
      case, not a "you" dropped into scattered sentences.
```

```text
form: multi-lens convergence on a single definition
move: Damodaran introduces cost of capital as three different questions
      (what does financing cost, what am I giving up by not investing
      elsewhere, what rate do I discount at) before collapsing them into one
      number, so the reader sees why one rate answers three questions instead
      of memorizing a formula. Use this once, at the term's first full
      definition, not as a recurring structural tic.
bar:  Every lens named must be a question this lesson's reader would
      independently ask (the ROIC lesson already raised "what counts as
      fair"), and the paragraph must end by naming the one number that
      answers all of them. A lens that does not correspond to something the
      lesson already needs is padding, not convergence.
```

```text
form: population-level evidence for a general claim
move: Mauboussin backs "ROIC above cost of capital creates value" with
      quintile-level return data across many firms, not one company's
      history, precisely because the claim is meant to generalize. Damodaran
      does the same with a distribution of estimated costs of capital across
      the market, so a single number can be placed at a percentile instead of
      asserted as typical.
bar:  Reserve for the lesson's transferable claims, i.e. anything the reader
      should be able to apply to an investment this lesson never mentions. A
      worked company case stays a worked case; do not retrofit population
      evidence onto it. The source must be a real dataset or study, cited,
      not an implied "studies show."
```

## Recently used, do not reuse

- Costco as the worked example or running company. It has carried profit,
  balance sheet, and ROIC. If a company example helps here, it must not be
  Costco, and it should not be a low-risk, low-leverage business where the
  hurdle is easy to clear without tension — the commission wants a case where
  the cost of capital obviously bites, or a contrast between a low- and
  high-risk firm. American Electric Power already anchored the ROIC dek; a
  capital-intensive utility or similar business can still teach the concept,
  but do not reuse AEP itself in the headline or dek.
- Dek molds already spent: the semicolon reversal ("X does A; Y refuses B"),
  the suspended question ("...and the real question is whether"), and the
  three-clause comma triad closed with "and."
- Heading cadence already spent: two clauses joined by a comma and "and"
  ("The scale, and what it is compounding against").

## Aswath Damodaran, "Putting the D in the DCF: The Cost of Capital"
Source: https://aswathdamodaran.blogspot.com/2015/01/putting-d-in-dcf-cost-of-capital.html
Craft:
- cadence: Short declaratives stake out a claim, then one longer sentence
  works out its consequence. He does not chain qualifiers; each qualifying
  point gets its own sentence.
- argument: Builds by resolving apparent multiplicity into one number. He
  names every context the term shows up in before he defines it, so the
  definition arrives already justified rather than asserted.
- evidence: Distributional, not anecdotal. He shows where a chosen rate sits
  in the range of rates real companies use, so the reader can judge a number
  against a population instead of trusting it on authority.
- stance: A practitioner telling you where the effort is worth spending and
  where it is not ("don't sweat the small stuff") — he ranks the reader's
  attention, not just the material.
- notice: He treats precision-seeking on the discount rate as a tell of
  wasted effort, and redirects the reader's scrutiny to the cash flows
  instead. The lesson can borrow this move: name where false precision
  tempts the reader and say plainly that it is not where the rigor belongs.
- diction: Plain, almost spoken register ("if there were a contest for the
  most measured number in finance") that never drops the technical content
  to get there.
- reader: Assumes the reader already does this kind of calculation and needs
  calibration, not a first introduction to the idea of a rate of return.
- the move the axes miss: he tells the reader what NOT to do with the number
  as clearly as what to do with it. A definition paired with a warning
  against its most common misuse teaches faster than the definition alone.

## Michael Mauboussin, "ROIC and the Investment Process"
Source: https://www.morganstanley.com/im/publication/insights/articles/article_roicandtheinvestmentprocess.pdf
Craft:
- cadence: States the test, then spends the rest of the section proving it
  rather than restating it in new words. One idea per paragraph, and the
  paragraph ends when the idea is proven, not when it is pretty.
- argument: A single operational test carries the whole piece: does a dollar
  invested become worth more than a dollar in the market. Every later
  distinction (margin vs. turnover, accounting vs. economic capital) is
  introduced only once it changes what that test would conclude.
- evidence: Large-sample and longitudinal — quintile movement over time,
  mean-reversion patterns — used to earn a general claim rather than
  illustrate it. The evidence is doing argumentative work, not decoration.
- stance: Professorial without condescension; he defines terms once, cleanly,
  and trusts the reader to carry them forward without a reminder.
- notice: He is honest about where the accounting understates the true
  picture (intangibles missing from invested capital) before the reader can
  object, which is candor about the method's limits rather than a hedge.
- diction: Technical vocabulary is introduced exactly once, always paired
  with the plain-language equivalent in the same sentence, then used bare
  from that point on.
- reader: Assumes financial literacy but not familiarity with this specific
  framework; he is introducing a tool, not reviewing one.
- the move the axes miss: the test he opens with is restated by name, not by
  paraphrase, every time it recurs, so forty pages later the reader still
  knows exactly what "the test" checks. Precision comes from repeating the
  same words for the same idea, not from finding new ones.

## Byrne Hobart, "Hurdle Rates"
Source: https://capitalgains.thediff.co/p/hurdle-rates
Craft:
- cadence: Alternates a short, plain claim with a longer sentence that works
  an example through to a number. The short sentence sets up; the long one
  pays it off.
- argument: Opens on a concrete, current puzzle (hurdle rates have stayed
  high even as the environment around them changed) and works toward an
  explanation, rather than opening on the definition and illustrating it
  afterward.
- evidence: Real, checkable, current figures — an actual treasury yield, an
  actual company's stated target return — so an abstract rate is pinned to
  something the reader could look up today, not a round illustrative number.
- stance: A knowledgeable peer thinking out loud with the reader, including
  the moments he is not sure of the answer, rather than a lecturer who has
  already resolved everything before the first sentence.
- notice: He walks the blended-rate arithmetic once, with real percentages,
  and does not repeat the mechanical walkthrough when the idea recurs later
  in the piece — he refers back to the number instead of rederiving it.
- diction: Concrete nouns for abstract financial machinery (a business
  "borrows at 6%," not "incurs debt financing costs").
- reader: Assumes the reader can follow a blended-rate calculation on one
  pass and does not need the arithmetic slowed down or repeated.
- the move the axes miss: he defines a term precisely once, in an aside, the
  moment a reader might reasonably misread it (flagging that "funded by
  equity" is loosely used and offering the more accurate phrase), then moves
  on without dwelling on the correction.

## Self-test

A writer following only the house default would open on a definition, work
the WACC formula, and support the "ROIC must beat the hurdle" claim with the
same single worked case doing double duty as proof. This guide asks for
three things the default does not supply on its own: open on what a wrong
hurdle costs before defining the rate that fixes it; converge on the
definition from the questions the reader already has, rather than stating it
cold; and back the general, transferable claim with more than one company's
evidence, saving the single worked case for making the arithmetic real rather
than for proving the claim generalizes.
