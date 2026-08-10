# Commission: investing/the-value-of-growth (2026-08-10)

## The concept and why it is next

The course has taught what a company owns and owes, how it earns a profit, profit
versus cash, free cash flow, return on capital, the cost of capital, present
value, discounted cash flow, and valuation multiples. The reader can now value a
stream of cash and knows that return on capital and the cost of capital are
different numbers. The keystone that ties those two together has not been taught:
growth creates value only when the return on the capital that funds it exceeds
the cost of that capital, and growth funded at a return below the cost of capital
destroys value. This lesson makes "is growth good?" a question with a
quantitative answer, and it is the judgment every DCF and every multiple already
assumes without saying so.

Teach it so the reader leaves able to look at a growing company and ask the only
question that decides whether the growth is worth paying for: what return is the
reinvested capital earning against what it costs. Rely on the earlier lessons
(return on capital, cost of capital, present value) rather than re-deriving them;
name them as prerequisites the reader holds.

## The worked example

Make the idea real with two companies that grow at the same rate but earn
different returns on the capital they reinvest — one above its cost of capital,
one below — and show their value diverging even though their growth rates match.
A reader should see the same growth rate add value in one case and subtract it in
the other. Keep the arithmetic transferable to the next investment, not tied to
one firm. A real company may anchor the example only if it makes the mechanism
clearer; the lesson does not default to a company walkthrough.

## Required contribution

The lesson does what a definition does not: it shows growth changing sign as a
value driver as the return on reinvested capital crosses the cost of capital, on
worked numbers the reader can reproduce. If the reader could get the same
understanding from the term's definition, the lesson has not done its work.

## Template and furniture

Template: `lesson`. The template's bookend cards may address the reader directly;
that is the one allowed exception to the self-reference rule, and those cards
still have to say something. Use `nb-math` / `nb-math-eq` to set the relationship
between growth, return on capital, and the cost of capital, and `nb-table` for
the two-company comparison. Set the math the reasoning leans on rather than
paraphrasing it.

## Recent investing habits not to inherit

Recent lessons headline with a concrete numeric claim ("A dollar next year is
worth 95 cents today", "Every valuation multiple hides a discounted cash flow"),
which fits the beat — write one for this lesson that commits to the growth/return
mechanism rather than reusing a prior lesson's construction. The present-value
and valuation-multiples lessons both moved from one worked case to a general
formula; keep that pedagogy but do not let the section shapes copy forward.

## Sources

Minimum 6 sources. Prefer authoritative primary treatments of value creation and
reinvestment economics: recognized valuation texts and the writers finance rates
on return on invested capital and growth. Cite the source that owns each claim;
a formula's provenance matters here as much as a figure's.

## Runtime

Harness `claude-code-routine`; model Opus 4.8 for every role. Production policy
asks researcher/high, writer/medium, writing-coach/low, editor/high (required).
Per-invocation reasoning effort is not separately settable through this runtime's
child launches, so each role runs at the session's effort; the editor gate is
preserved in full. Writer records `harness: claude-code-routine` and
`model: Opus 4.8` in nb-meta.
