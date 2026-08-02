# Voice guide: GAN paper-of-the-day

Register: calm, first-principles, declarative. Short sentences carrying one
claim each. No performance of surprise, no aside to the reader, no narrating
the article itself. The writer's authority comes from showing the algebra and
the evidence, not from announcing that something is surprising or important.

Reader relationship: a peer with the math already. Do not build probability
or calculus from the ground up. Do build the paper's own notation from the
ground up, once, in the order the argument needs it, and never define a term
twice.

Moves that change sentences in this article:

- **Derivation pacing.** Before naming a quantity, spend one sentence on why
  the argument needs it: what question is unanswered without it. Only then
  give the symbol, then the formula, then one sentence stating what the
  formula means in the units the reader already has (a probability, a ratio,
  a loss). Never let two unexplained symbols land in the same sentence. When
  a term in the algebra vanishes, drops to a bound, or cancels, say which
  term and why in the same breath that reports the result — not a general
  "this simplifies," the specific mechanism. This applies to both the D*
  derivation and the JS-divergence reduction: each gets its own
  question-symbol-formula-consequence chain, not a shared one.
- **Intuition and formula in the same breath.** State what a quantity means
  before or immediately beside the line that defines it formally, so a reader
  who skips the algebra still has the idea, and a reader checking the algebra
  has something to check it against. Don't let plain-English meaning and
  notation drift more than a sentence apart.
- **Hard boundary between proof, empirical record, and synthesis.** Finish
  what the paper proves — fully, in its own frame, under its own conditions —
  before a single sentence about what training actually did. The sentence
  that crosses that boundary should name the specific assumption the proof
  needed and say plainly that practice did not supply it: not a reveal, a
  report. Keep the same discipline crossing into the writer's own synthesis:
  mark it as the piece's argument, not another finding.
- **One name per concept, held for the whole piece.** Generator,
  discriminator, value function, optimal discriminator, JS divergence — pick
  the name at first use and never swap in a synonym for variety. A varied
  word reads as a new concept.
- **The verdict commits and bounds itself in the same sentence.** State
  plainly what was established, then what condition it depended on, in one
  breath — not a hedge, a scope. "Proved under X; X is what practice doesn't
  have" is the shape, not "seems to suggest" or "may indicate."
- **No colloquial swerve at the theory/practice hinge.** The transition into
  what went wrong is a plain declarative sentence naming the mechanism, not a
  performed reaction ("turns out," "and yet," an exclamation). Let the
  mechanism carry the surprise; the sentence doesn't need to announce it.

Recently used, do not reuse: the one-line-paradox headline paired with a
"N follow-ups disagree" dek; opening on the formula "proved X for a setting
practice never occupied"; closing the piece on a reading list.

## Gabriel Goh, "Why Momentum Really Works"
Source: https://distill.pub/2017/momentum/
Craft:
- cadence: motivate the quantity in a plain sentence, name it, give the
  closed form, then state its consequence in one short sentence — four beats,
  every time a new quantity enters.
- argument: works forward from one tractable case (a quadratic) to the
  general claim, and isolates the single ratio responsible for slow
  convergence rather than gesturing at "curvature" broadly.
- evidence: closed-form solutions and exact rates on toy problems, not
  qualitative description of what momentum does.
- stance: confident inside the proven case, explicit about where the proof
  stops covering the practice that motivated the piece.
- notice: catches where the standard textbook story oversimplifies, and says
  what it leaves out rather than just contradicting it.
- diction: a technical noun (condition number, spectral radius) is introduced
  once with its definition and never re-described in looser language after.
- reader: assumes linear algebra and calculus fluency; skips no algebraic
  step but gives each step exactly one sentence.
- the move the axes miss: a geometric picture (a ball in a valley, a
  suspended weight) arrives immediately before the formal derivation of the
  same quantity, so the reader has an image to check the symbols against
  before the symbols multiply.
Calibration: "The larger the ratio, the slower gradient descent will be. The
condition number is therefore a direct measure of pathological curvature."

## Chris Olah, "Visual Information Theory"
Source: https://colah.github.io/posts/2015-09-Visual-Information/
Craft:
- cadence: short declarative sentences; each new definition opens by
  restating the question the previous paragraph left open.
- argument: builds one definition at a time as the answer to a concrete
  question (how long does this message need to be?), so the formula arrives
  as the necessary conclusion rather than an assertion.
- evidence: a single running worked example, reused and extended rather than
  swapped for a new one each time a concept advances.
- stance: patient and exact; treats a possible misreading of a formula as
  worth a sentence rather than leaving it for the reader to catch.
- notice: flags the specific place a quantity could be misunderstood (that a
  divergence is not symmetric, that a code length is an expectation) instead
  of only stating the correct version.
- diction: pairs a plain-language gloss with the exact term at first use, then
  drops the gloss and keeps only the term for every use after.
- reader: assumes no prior probability background — the pacing itself is too
  slow for this article's reader, but the sequencing (meaning stated beside
  the formula, one definition building the next) transfers regardless of
  starting level.
- the move the axes miss: the informal meaning of a quantity sits in the same
  sentence or the next one as its formula, so meaning and notation are never
  separated by more than a beat.
Calibration: "The KL divergence of p with respect to q, D_q(p), is defined:
D_q(p) = H_q(p) - H(p). The really neat thing about KL divergence is that
it's like a distance between two distributions."

## Lilian Weng, "From GAN to WGAN"
Source: https://lilianweng.github.io/posts/2017-08-20-gan/
Craft:
- cadence: one equation-bearing sentence followed by one plain consequence
  sentence, in short paragraphs of a single claim each.
- argument: the theory stays entirely inside the paper's own frame —
  objective, optimum, value at the optimum — before a single practice claim
  enters; the practice section then traces each failure back to a named
  assumption from the theory section.
- evidence: an unbroken derivation chain (state the objective, differentiate,
  solve, substitute) with no step left for the reader to supply.
- stance: matter-of-fact; a discriminator's failure is reported as a
  mechanical consequence of a formula, not staged as a twist.
- notice: names the exact term in the loss that goes to zero and why, not
  just that "gradients vanish."
- diction: generator, discriminator, and value function keep their one name
  across the entire derivation and the entire practice discussion that
  follows it.
- reader: comfortable with expectation notation and calculus; no step is
  re-explained once shown.
- the move the axes miss: the sentence that crosses from theory to practice
  names the boundary directly — what was proved, under what condition — so
  the reader is told exactly which assumption practice failed to meet,
  instead of the crossing being staged as a reveal. (The piece itself
  sometimes breaks its own register with a chatty aside at that hinge; that
  aside is the one thing not to carry over — keep the boundary-naming move,
  drop the tone.)
Calibration: "When the discriminator is perfect, we are guaranteed with
D(x) = 1 for all x in p_r and D(x) = 0 for all x in p_g. Therefore the loss
function L falls to zero and we end up with no gradient to update the loss
during learning iterations."
