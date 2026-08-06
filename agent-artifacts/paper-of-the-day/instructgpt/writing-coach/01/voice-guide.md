# Voice guide: paper-of-the-day/instructgpt

Write as a reviewer rebuilding a derivation for a peer who could have derived it
too. The register is the house baseline — calm, first-principles, structure
doing the persuading — with one shift the default does not supply: the math is
load-bearing evidence, not illustration, and the verdict on durability is
pressed through what the objective provably optimizes, never through adjectives.

The reader has the mathematical maturity to read set notation cold. Spend that.
Do not narrate that a derivation is coming or that a step is hard. Do the step.
Every displayed equation is a beat the prose has already earned a sentence
earlier and spends a sentence later; an equation the surrounding text neither
sets up nor uses has no reason to be set. Define each symbol in the sentence
that first writes it, then reuse it exactly — a reward model called `r_phi` in
one line is not "the scorer" in the next.

Two things this article decides that the house register leaves open. First, when
math goes inline and when it is displayed. Second, how hard to stand behind a
judgment about whether InstructGPT's claim held up. The licenses below calibrate
both. Everything else stays house default.

## Licenses

form: a displayed set-math equation (nb-math-eq)
move: Gundersen sets an equation as a rest point in the argument — the clause
  before it names the question it answers ("what the RL stage maximizes is"),
  the display states it, and the next sentence reads a term back out and spends
  it. He introduces notation just-in-time, never front-loaded.
bar:  the sentence before the display commits to what the equation will show,
  and the sentence after uses at least one of its terms to advance the argument.
  A display that is announced with "the objective is" and left uninterpreted is
  cut or folded inline.

form: inline math inside a sentence
move: reserve the display for the object the argument turns on (the ranking
  loss, the KL-regularized objective, the DPO reparameterization); keep the
  supporting algebra inline where breaking it out would stall the read.
bar:  an equation is displayed only if a later sentence points back at it. If it
  is stated and never referenced again, it belongs inline in the sentence that
  needed it.

form: a verdict on the claim's durability
move: Huszár states a judgment plainly ("maximum likelihood is not a desirable
  training objective") and then lets the mechanism carry it — which divergence
  is minimized, which failure mode follows — rather than repeating the verdict
  louder. The math is the proof, so the verdict names the exact term or optimum
  that makes it true.
bar:  a durability verdict names the specific mechanism behind it — the proxy
  reward that over-optimizes, the KL term that binds the policy, the reward
  model DPO's closed form removes — and could be contested on that mechanism. A
  verdict resting on scale, fame, or consensus is cut.

form: weighing the paper against a later result
move: Lambert brings a follow-on result forward and first says what it actually
  controlled for before crediting it ("these results are with datasets no one
  has extracted powerful performance from"), which deflates the hype read
  without dismissing the finding.
bar:  each after-record claim (Gao et al. on over-optimization; Rafailov et al.
  on DPO) states what was measured and on what, and therefore what it does or
  does not settle about InstructGPT's claim. A follow-on cited only as a verdict
  on the original, without its own measured content, is cut.

form: a mechanistic contrast between two objectives
move: Huszár pairs opposite behaviors by their real mechanism — KL[P‖Q] versus
  KL[Q‖P], the "liberal" versus "conservative" divergence — so the contrast
  teaches a difference the reader can check, not a rhetorical reversal.
bar:  a contrast (SFT vs the RL stage, reward-model score vs true preference,
  PPO's loop vs DPO's closed form) names the concrete thing that differs and is
  checkable against the math. The editorial ceiling on "not X but Y" contrasts
  still holds; this license covers the technical pairing, not the rhetorical
  one.

## Gregory Gundersen, "The Exponential Family"
Source: https://gregorygundersen.com/blog/2019/03/19/exponential-family/
Craft:
- cadence: short sentence announces a move ("To show this, let's maximize the
  log likelihood"), longer sentence develops it; interpretive pauses recenter
  the reader on why a step matters before resuming.
- argument: builds each object in flowing prose, then formalizes it; the
  derivation is the spine and prose is the connective tissue between displays.
- evidence: the algebra itself; a claim is settled by carrying it to a form the
  reader recognizes, not by asserting the result.
- stance: patient and collaborative, confident the reader will follow the steps.
- notice: introduces notation exactly where it becomes necessary (bold vectors
  only at the multivariate case), so no symbol arrives unmoored.
- diction: plain and procedural — "putting everything together," "with a little
  algebraic manipulation"; names the natural parameter only after the equation
  that needs the name.
- reader: a participant choosing the next step, not a recipient of a conclusion.
- the important move: a display is choreographed in three beats — announce the
  question, show the equation, read a term back out — so the equation is a
  turn in the argument rather than a pause from it.

## Ferenc Huszár, "How to Train your Generative Models?"
Source: https://www.inference.vc/how-to-train-your-generative-models-why-generative-adversarial-networks-work-so-well-2/
Craft:
- cadence: problem definition, then formalization, then the consequence;
  sentences narrow from scope to the exact term that decides the argument.
- argument: expose what an objective actually optimizes (which divergence),
  then judge whether that is the objective anyone wanted.
- evidence: the math proves the point — showing KL[P‖Q] and KL[Q‖P] as mirror
  divergences with opposite failure modes turns a preference into a structural
  fact.
- stance: states the verdict once, plainly, then lets the mechanism press it;
  tone of inevitability rather than polemic.
- notice: reframes an empirical success as a theoretical necessity by naming the
  middle ground (Jensen-Shannon) the method actually lands on.
- diction: casual precision — "liberal" and "conservative" divergences,
  "optimist" and "pessimist"; admits limits directly ("super hard to optimise").
- reader: assumes sophistication, signals translation ("in yet other words")
  rather than simplification.
- the important move: the verdict is inseparable from the term that proves it,
  so it cannot be restated as an adjective without losing its content.

## Nathan Lambert, "Do we need RL for RLHF?"
Source: https://www.interconnects.ai/p/the-dpo-debate
Craft:
- cadence: a broad question funnels into specific, testable sub-questions;
  momentum without premature closure.
- argument: reads a method (DPO) against what happened after it shipped, and
  weighs later comparisons instead of the abstract's promise.
- evidence: empirical follow-on results, each contextualized before it is
  credited — data quality treated as more probative than the algorithm choice.
- stance: honest about uncertainty ("not conclusive"); credits a finding only
  after saying what it controlled for, which deflates hype without dismissal.
- notice: the real variable is often not the one under debate — limitations in
  data and tooling over optimizer choice.
- diction: precise but unguarded; names the debate plainly and resists a winner
  the evidence has not earned.
- reader: a translator addressing peers inside a live argument, not a verdict
  handed down.
- the important move: a durability judgment is built from what later work
  measured, so the after-record does argumentative work rather than decorating a
  conclusion.
