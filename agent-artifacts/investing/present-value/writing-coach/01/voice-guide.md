# Voice guide: investing/present-value (01)

## Directive

Write in the calm, first-principles register the press already sets, and add
one thing the default does not: compute in front of the reader. This lesson
turns future cash into a value today, and the reader should be able to redo
every number on the page with a calculator. Treat the reader as a capable peer
who happens not to know discounting yet, never a novice to reassure and never a
crowd to entertain.

Five moves should change sentences here.

1. Reach the first present value by hand, with small numbers, before the
   annotated equation generalizes it. Words for the mechanism first, then the
   symbol.
2. Name each symbol as it does its job, once, at the moment it acts. Do not
   pre-define the whole equation and then use it.
3. Carry the prior lesson forward by reference, not re-teaching. The discount
   rate is the cost of capital already taught; state that it is the same number
   and link back, rather than re-deriving WACC.
4. Ground the one genuinely hard idea (why a dollar later is worth less) in a
   single concrete comparison, then drop the comparison once the real
   mechanism is on the page.
5. Mark the deferred material as deferred. Terminal value and the perpetuity
   shortcut get named and bounded, not resolved. Say plainly what this lesson
   does not do.

Do not specify what the lesson concludes, which company or instrument appears,
or how the sections divide. That is the writer's and template's call.

## Licenses

form: measured second person in the body ("you")
move: Olah and Azad address the reader while walking a mechanism ("Let's go
  back to our example"; "you'll earn 50% of your principal in the course of a
  year"), turning a derivation into something the reader performs rather than
  watches. Deploy it only inside a worked step, where "you" is the one doing
  the arithmetic.
bar:  the sentence must carry an operation the reader could redo (a division, a
  discount, a sum). A "you" that only warms the tone or narrates the reader's
  feelings is cut.

form: one sustained comparison for the discount rate / opportunity cost
move: Azad maps an unfamiliar rate onto a familiar one ("50 mph means you'll
  travel 50 miles in the course of an hour; r = 50% per year means you'll earn
  50% of your principal") so the reader imports intuition they already hold.
  Use one comparison, for the single hard idea of why later money is worth
  less, and retire it once the mechanism is stated in its own terms.
bar:  the comparison must hold at the exact point being taught, mapping onto the
  number just computed. A decorative or approximate comparison, or a second
  competing one in the same lesson, is cut.

form: an inline running calculation in prose (numbers worked mid-paragraph, not
  only inside the table)
move: Azad and Olah compute in front of the reader, small numbers first, each
  line advancing one step, before any general formula appears. Use it to reach
  the first discounted figure by hand before the equation furniture states the
  identity.
bar:  every figure must be reproducible from figures already on the page, and
  each sentence advances the computation by one operation. A number that
  arrives without its arithmetic is cut or sourced.

form: reading the annotated equation symbol by symbol
move: Olah walks a diagram part by part, naming each ("cell state is kind of
  like a conveyor belt") as it does its job before the whole is used. Apply the
  same walk to the PV identity: CF, r, t, and the exponent each named where it
  first acts.
bar:  each symbol is named once, in plain words, at the moment it does work in
  the derivation. A symbol defined before it is used, or restated for emphasis,
  is cut.

form: a genuine setup question answered on the spot
move: Azad ("But is it really 12?") and Damodaran ("How do you estimate the
  intrinsic value of gold?") pose the reader's own next question and answer it
  in the following sentences. Use at most one in the body, at the hinge where
  the reader would ask why the future dollar is divided rather than subtracted.
bar:  the sentences after it must answer with a derivation or a number. Pose the
  question directly to the material; never narrate that "a reader will wonder"
  (that trips the self-reference ban). A question left rhetorical, hanging, or
  used to announce stakes is cut.

## Recently used, do not reuse

- The company-figure opener reflex. Recent lessons hooked on a single firm's
  headline number ("Costco turns each invested dollar into 37 cents of
  profit"). Do not open "Why this matters" or the first body line on that
  shape. If a company appears at all, it enters to make the mechanism concrete,
  not as the hook.
- The company-plus-number dek mold. That construction is spent across recent
  deks; the dek here identifies the lesson by its own particulars.
- Costco as the running case. It is over-used across prior lessons. The
  commission prefers instrument-level material (a Treasury cash flow, a bond
  coupon) where a concrete case is needed at all; choose a different example if
  one is used.
- The prior lessons' section outline and heading cadence. Do not copy the
  earlier lessons' heading shapes; vary them.

## Chris Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: long expository sentences alternate with short grounding
  declaratives ("Humans don't start their thinking from scratch every
  second."). The short line lands a concept the long one set up.
- argument: strict build order. Each idea arrives only when needed: the problem
  (long-term dependencies) is made felt before the mechanism (gates, cell
  state) that solves it is introduced.
- evidence: figures function as proof, not decoration. A diagram appears before
  its equation, so the reader sees the structure before the notation.
- stance: patient mentor who has read the field. Assumes intelligence, not
  expertise; flags what is coming ("We'll walk through the LSTM diagram step by
  step later") so confusion feels temporary.
- notice: points out that the method fails in practice, not theory, and cites
  who showed it. The honesty about limits builds trust.
- diction: technical terms enter only after the concept is built, and land with
  a homely handle ("cell state is kind of like a conveyor belt").
- reader: sparing, purposeful direct address ("Let's go back to our example")
  that makes the derivation collaborative rather than delivered.
- the important move: the deliberate walk. A single mechanism is taken apart
  component by component and named as each part does its work, before the whole
  is ever used. This is the model for reading the PV equation here.

## Kalid Azad (BetterExplained), "A Visual Guide to Simple, Compound and Continuous Interest Rates"
Source: https://betterexplained.com/articles/a-visual-guide-to-simple-compound-and-continuous-interest-rates/
Craft:
- cadence: rhythm mirrors the content. Short doubt ("But is it really 12?")
  precedes an expanding sequence of clauses that accumulate the way interest
  compounds.
- argument: teaches simple interest thoroughly first, not to endorse it but to
  create the friction the next idea resolves. Each section answers the
  objection the last one raised.
- evidence: worked numbers built one step at a time ("We earn $50 from year
  0-1... But in year 1-2..."), then a formula, then a diagram. Three channels
  for one idea.
- stance: fellow skeptic, not authority. This is the register to admire but not
  copy: the house voice is serious, so take his numeric build and analogies and
  leave the conspiratorial, jokey persona out.
- notice: names the thing a novice overlooks and gives it a handle (the
  "interest gap," the dead time where money is not yet compounding).
- diction: technical terms always arrive translated ("The math gurus will call
  this a 'derivative'... No need to hit a mosquito with the calculus
  sledgehammer just yet"). Plain words carry the weight.
- reader: constant direct address inside the computation ("Let's try a few
  examples"), which makes the reader perform the arithmetic.
- the important move: the rate-as-familiar-rate analogy (interest rate mapped
  to speed) that imports intuition the reader already has. Transfer the
  analogy craft, at the strict bar above, not the voice.

## Aswath Damodaran, "Thoughts on intrinsic value"
Source: https://aswathdamodaran.blogspot.com/2011/06/thoughts-on-intrinsic-value.html
Craft:
- cadence: a short definitional anchor ("Only assets that are expected to
  generate cash flows can have intrinsic values.") followed by a longer
  enumerating sentence that tests the definition across cases.
- argument: deductive from one principle. Establishes what value is, then
  derives consequences and boundaries by pushing the definition against
  categories until it breaks.
- evidence: category-testing rather than a single big example. Bonds, stocks,
  businesses fit; a house, fine art, baseball cards do not. The framework is
  shown by where it stops applying.
- stance: plain-spoken conviction, positions stated without hedging ("I don't
  intend this to come across as snobbish, but..."). Opinion is earned by the
  reasoning shown, which matches the house bar.
- notice: the distinction hiding in plain sight (value versus price; most
  "valuation experts" are really pricing experts). This is the move for
  separating the discount rate from an arbitrary number.
- diction: terms of art introduced through their function, not a glossary
  definition. "Cash flows" replaces jargon; "intrinsic value" earns its place
  by use.
- reader: treats the reader as capable but tangled in industry language,
  someone who should and can see the distinction once it is drawn.
- the important move: fixing a boundary by honest exclusion ("estimating the
  intrinsic value of your house is an exercise in futility"). This is the model
  for naming what this lesson defers: state the limit plainly instead of
  gesturing past it.
