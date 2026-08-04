# Voice guide: paper-of-the-day/generative-adversarial-networks (01)

## Directive

Register: calm, precise, first-principles — the house baseline, sharpened for
a piece that lives inside a derivation rather than around one. Reader: an
ML-engineer peer who wants to watch the minimax game get solved, not be told
the result. Three moves change sentences here:

1. **The cash-out is not a paraphrase of the symbols, it is what the equation
   changes about the objective.** Do not follow V(D,G) or D* with a sentence
   that re-says the formula in words ("this means D is the ratio of..."). Say
   what the result now lets the generator or discriminator do that it
   couldn't before, or what quantity the game has been reduced to optimizing.
   The cash-out lands in the same beat as the equation — the next sentence,
   not the next paragraph.
2. **Build the theorem's promise before you build its ceiling.** State
   exactly what the global-optimum proof assumes (function-space
   optimization, an inner loop trained to optimality) with the same
   precision used to state the theorem itself. The gap to training reality
   is not a twist sprung on the reader; it is the next fact, earned by the
   assumptions just named.
3. **The verdict grades, it doesn't split the difference.** Say plainly what
   the paper's theorem is right about and what it never promised, in that
   order, and let the WGAN diagnosis supply the mechanism (near-zero gradient
   under disjoint support) rather than asserting "training is unstable" and
   moving on. A sentence that could apply to any two-network setup has not
   located the failure.

What this should sound like that the house default does not already
guarantee: the default bans fluff and demands earned analysis, but it does
not by itself stop an equation from sitting inert between two paragraphs of
narration, and it does not by itself stop a theory/practice piece from
resolving into "it's complicated." This guide is the difference between a
paper that sets four equations as furniture and one where each equation does
a turn of the argument's work, and between a graded verdict and a shrug.

## Licenses

```text
form: worked micro-example
move: Nielsen (Neural Networks and Deep Learning, ch. 5) does not leave "the
      gradient shrinks in early layers" as a qualitative trend — he quantifies
      it on an explicit small network, so the reader watches the number
      collapse rather than being told a mechanism exists. Olah does the same
      at sentence scale, computing ∂e/∂b = 1·2 + 1·3 = 5 instead of saying
      "b affects e through two paths."
bar:  Any invocation must use an actual computable quantity from the paper's
      own math or a concrete, checkable instance of it — never a restated
      trend ("this makes training harder") standing in for a number. One use
      is enough; do not build a running toy example that competes with the
      paper's own artifacts for space.

form: analogy that precedes or follows formalization
move: Weng grounds Earth Mover's distance in a dirt-transport image before
      the reader meets the infimum over joint distributions; Olah grounds
      "touch each edge exactly once" in a physical verb before the reader
      meets the sum-over-paths formula. The analogy carries the shape of the
      idea for one beat, then the math takes over.
bar:  The analogy must map to a specific structural feature of the math (disjoint
      support, not "the model is confused") and must be retired once the
      equation is set — it cannot recur later as a shorthand for the concept.
      At most one per major concept (JS divergence's behavior under disjoint
      support; the Earth-Mover distance, if the reconstruction reaches WGAN's
      proposed fix).

form: rhetorical question as derivation pivot
move: Weng opens the discriminator-optimization step with "What is the
      optimal value for D?" immediately before solving for it — the question
      names exactly what the next paragraph computes.
bar:  Permitted at most once, and only in the sentence directly before a step
      the reader watches get solved in the paragraph that follows. Never as a
      section-opening hook or a stand-in for stating the claim.
```

## Recently used, do not reuse

The commission names these directly — carry them as constraints, not as
material studied for voice:

- The "famous claim overturned" cadence: a clean result stated only to be
  knocked down. This paper's theorem is not wrong; hold the gap without
  staging it as a reversal.
- The eponym/announcement mold ("In 2014, Goodfellow et al. introduced...").
  Open on the game and the objective, not the byline.
- A colon-subtitle headline and the comma-triad dek (three clauses joined by
  commas and closed with "and").
- More than one earned hedged-contrast sentence ("X is not Y; it is Z") in
  the piece — the theory/practice pivot may spend one; it does not get a
  second at the WGAN turn.

## Lilian Weng, "From GAN to WGAN"

Source: https://lilianweng.github.io/posts/2017-08-20-gan/

Craft:
- cadence: short definitional sentences open a section, then lengthen into
  the derivation; a rhetorical question ("What is the optimal value for D?")
  marks the pivot from setup to solving.
- argument: builds the failure case from the paper's own math rather than
  asserting instability — disjoint supports are a stated consequence of low-
  dimensional manifolds, not an empirical complaint bolted on afterward.
- evidence: cites specific papers for specific claims (Arjovsky & Bottou for
  the vanishing-gradient diagnosis, Salimans et al. for the Nash-equilibrium
  difficulty) rather than a general "researchers have shown."
- stance: names a real weakness plainly ("weight clipping is a clearly
  terrible way to enforce a Lipschitz constraint") without treating it as
  disqualifying — the fix under discussion gets the same clear-eyed treatment
  as the problem.
- notice: treats the JS-divergence's symmetry, not just its existence, as the
  load-bearing design choice — a property most treatments would pass over as
  incidental.
- diction: alternates plain verbs ("trick the discriminator") with exact
  technical terms (Lipschitz continuity, infimum) and never blurs the two
  registers into a hedge.
- reader: assumes the reader will sit through a derivation if roadmapped
  first ("before we start examining GANs closely, let's review...") — the
  roadmap is one sentence, not a preamble.
- the cash-out discipline: every derived quantity gets one sentence stating
  its behavior at the limit (D* → 1/2 when p_g = p_r) before the prose moves
  on — the equation is never the last word on itself.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"

Source: https://colah.github.io/posts/2015-08-Backprop/

Craft:
- cadence: short declaratives establish authority early ("Backpropagation is
  the key algorithm"), then the piece slows for each derivation step, and
  speeds back up in a closing reflection.
- argument: reframes an apparently simple result (it's just the chain rule)
  as historically non-obvious, then earns that reframe by showing the
  combinatorial cost the naive approach would pay — the surprise is
  demonstrated, not asserted.
- evidence: cites sparingly and by name (Griewank on backpropagation's
  independent reinventions) and points elsewhere for adjacent ground
  (Nielsen's chapter) rather than re-deriving what a citation already covers.
- stance: openly narrates his own prior misjudgment of the result's
  difficulty and corrects it in the same breath — confident about the
  content, provisional about his own first read of it.
- notice: insists on the general graph-theoretic frame instead of the
  neural-network special case most treatments jump to, and separates
  forward- from reverse-mode differentiation as a structural duality rather
  than an implementation detail.
- diction: physical verbs for abstract operations ("touch each edge exactly
  once") and calibrated alarm words ("combinatorial explosion") stand in for
  jargon without softening the math.
- reader: uses inclusive "we" to walk the derivation together, and closes on
  a line that generalizes past the specific technique — a move earned by
  having done the specific technique first, not a substitute for it.
- the cash-out discipline: every equation is preceded by a sentence stating
  why it's needed and followed by a sentence unpacking what it says in
  words — motivation, formula, translation, in that fixed order.

## Michael Nielsen, *Neural Networks and Deep Learning*, ch. 5 ("Why are deep
neural networks hard to train?")

Source: http://neuralnetworksanddeeplearning.com/chap5.html

Craft:
- cadence: states the clean expectation first, in the same declarative
  register as the rest of the book, then shifts into an investigative mode
  ("let's see what happens") exactly at the point reality departs from it.
- argument: builds the gap as a located mechanism, not a general complaint —
  the vanishing gradient is traced to a specific multiplicative chain through
  a specific activation function, so the reader can see which factor is
  responsible.
- evidence: a small worked network stands in for the general claim, with an
  actual computed ratio between the first- and last-layer gradients, so
  "learns more slowly" becomes a number instead of a description.
- stance: does not treat the failure as an indictment of deep networks — it
  is one identified mechanism among others, stated with the same weight as
  the theorem it complicates, not more.
- notice: separates "the gradient is smaller" from "training is bad," and
  insists on tracing the first claim to a cause before letting the reader
  infer the second — the two are kept distinct sentence by sentence.
- diction: plain and unhurried, willing to name the emotional beat of a
  result ("this is deeply unsatisfying") without letting that stand in for
  the technical explanation that follows it.
- reader: treated as a fellow investigator mid-experiment — the prose
  narrates what is being tried and what was found, in that order, rather
  than presenting the finding first and the method as justification after.
- the theory/practice structure this article needs most: expectation, then
  the exact point of departure, then the mechanism, then a verdict that
  keeps the theorem's original claim intact rather than retracting it.
