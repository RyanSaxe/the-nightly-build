# Editorial review: investing/the-value-of-growth (editor/01)

## Skeptic

Thesis: growth changes a company's value only through the return earned on the
capital that funds it; when that return clears the cost of capital growth adds
value, when it falls short growth destroys value, and the growth rate alone
settles nothing. The piece stands on four claims.

1. **Growth is bought, never free: g = reinvestment rate × return on capital
   (s1).** Confirmed against Damodaran's Stern page directly. The page states
   "Expected Growth_EBIT = Reinvestment Rate * Return on Capital" and the
   excess-return language the article leans on. Source owns the claim; label
   `primary` is correct.

2. **The value driver formula and its sign change (s3).** V = NOPLAT_1 ×
   (1 − g/RONIC)/(WACC − g). I recomputed the whole worked example by hand.
   Firm A (RONIC 15%, g 5%, WACC 9%): 1 − 0.05/0.15 = 0.6667, ÷ 0.04 = 16.667,
   × 100 = 1,667. Firm B (RONIC 6%): 1 − 0.05/0.06 = 0.16667, ÷ 0.04 = 4.1667,
   × 100 = 417. Zero-growth baseline NOPLAT/WACC = 100/0.09 = 1,111. Growth adds
   556 for A and destroys 694 for B. Ratio 1,667/417 = 4.0, so the dek's "four
   times" holds. The pivot algebra is right: at RONIC = WACC the numerator is
   (WACC − g)/WACC, which divided by (WACC − g) leaves 1/WACC, so g cancels and
   V = NOPLAT/WACC. I also checked the direction independently: dV/dg holding
   RONIC fixed is proportional to (RONIC − WACC), so growth raises value above
   the cost of capital and lowers it below. Every figure in the prose and the
   table reproduces. The formula matches the evidence quote character for
   character.

3. **Sign-change scope (s2, and the note).** This was the round's main risk and
   it is handled. The claim is stated everywhere as the return on *new*
   (marginal) capital inside a constant-growth model: "the return on the next
   dollar reinvested, the marginal dollar, not the average return," and the note
   fixes it as "not a verdict on a firm's average historical return and not a
   promise that any return holds forever." Nothing overclaims average ROIC or a
   permanent above-cost return. I confirmed the create/neutral/destroy direction
   against Damodaran's Myth 5.3 page: value is "decreasing when the return on
   invested capital < cost of capital, unchanged when the ROIC = Cost of capital
   and increasing when the ROIC > Cost of capital." The note cites s2; s2 owns
   the create/neutral/destroy rule tied to excess returns, so the citation
   holds, though the strict marginal-vs-average precision derives from the value
   driver formula (s3) as well. Adequately sourced.

4. **Empirical fade (s5, s6, s4).** The one-third-acquired-or-bankrupt figure,
   the 5–8 vs 1–4 TRS-point spread, and the high-then-low ROIC prescription all
   match the evidence record's quotes exactly. The s5 PDF is a genuine 334KB
   McKinsey file that resolves and downloads; this environment cannot re-extract
   its text, so I rely on the researcher's in-full read plus the internally
   consistent figures. If CI can text-extract the PDF, a re-confirmation of the
   "5 to 8 / 1 to 4" line is cheap insurance, but nothing suggests a break.

`data-nb-kind` audit: three primaries (Damodaran s1/s2, the Valuation text s3),
three secondaries (McKinsey s4/s5/s6). The core sign-change claim carries two
independent primary formulations — Damodaran and the Koller/Goedhart/Wessels
text — so the labeling hides no missing independent source. Damodaran is genuinely
independent of the McKinsey-lineage sources. Every external href I opened landed
on the source itself.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

Two sentences failed the slop test and were cut or trimmed.

- "This is the counterintuitive part, worth stating in plain words." A signpost
  that announces the coming point and self-grades it ("counterintuitive")
  instead of doing the reasoning; the sentence after it carries the actual
  content. Deleted. The paragraph now runs straight from the sign statement into
  the concrete consequence.
- "...and honesty about the rule means naming them." A meta clause that promised
  to name the assumptions rather than naming them; the next sentence names them.
  Trimmed the opener to "lives inside a set of assumptions worth naming."

The earned negative-parallelisms stay: "the marginal dollar, not the average
return," the note's "not a verdict... not a promise," and the takeaway's "the
question is never how fast it grows. It is whether..." each correct a real,
named misconception (marginal vs average, snapshot vs forever, growth rate vs
return), which is exactly where the "not" clause is allowed. No formula carried
forward from the recent lessons: the headline commits to the mechanism rather
than reusing the prior numeric-claim construction, the number lives in the dek,
and the section arc runs formula-then-worked-case, inverting the
worked-case-then-formula shape of the present-value and valuation-multiples
lessons. Headings reconstruct the argument in the piece's own nouns with no
scaffolding slots and no comma-and-clause repetition. Furniture (two nb-math
blocks, the nb-table, the nb-note) each carries reasoning; none is decorative.
Bookends address the reader under the template's license and both say something
particular to this lesson. No prompt leakage.

## Reader

Read straight through, the piece gives what no single source does: identical 5
percent growth staged against each firm's own zero-growth baseline so the reader
watches the same growth rate add $556 at a 15 percent return and destroy $694 at
a 6 percent return, then generalized to the one question worth asking of any
growing company. That paired with-growth / no-growth computation is the visible
new work, and it matches the draft handoff's original-work claim. The prose sits
with the voice-guide exemplars — a concrete case carried through every step in
plain sentences, Olah's and Damodaran's register — not a median summary. The
lesson relies on the earlier lessons rather than re-deriving them: return on
capital, cost of capital, and the profit-over-cost-of-capital perpetuity are
named as held knowledge and linked in Background, never rebuilt. The headline
reads true as the largest claim.

## Edits

- Cut "This is the counterintuitive part, worth stating in plain words." from the
  sign-change paragraph (signpost / self-grade).
- Trimmed the returns-fade opener from "lives inside a set of assumptions, and
  honesty about the rule means naming them" to "lives inside a set of assumptions
  worth naming" (meta throat-clearing).

## Required work

- **orchestrator / CI:** Chrome is absent locally, so no visual render pass was
  possible. CI must run the render-check on the annotated value-driver equation
  (the `\htmlClass{nb-mc1..4}` colored terms and legend) and the two-company
  `nb-table`; both passed the structural proof but neither was seen rendered.
- **writer (optional, non-blocking):** if CI can text-extract the s5 McKinsey PDF,
  re-confirm the "TRS 5 to 8 percent / growth 1 to 4 percent" line. Not a
  suspected error; the environment simply could not re-read the binary here.

No researcher work. No redraft.

## Decision

approve — the arithmetic reproduces exactly, every equation matches its sourced
formula, and the sign change is stated within its true marginal, constant-growth
scope; the two slop cuts were mine to make and left nothing publication-blocking.
