# Voice guide: paper-of-the-day/denoising-diffusion

## Directive

Register: the house baseline already applies in full — calm, precise, argued
from first principles, plain sentences, structure doing the persuading. This
article does not need a different register. It needs the derivation staged so
that every equation reads as a forced move, not a substitution. Reader
relationship: a peer engineer looking over the derivation with you, not a
student being walked through calculus. Name the conceptual leap; skip the
algebra a reader in this field can do unprompted.

Moves that change sentences in this piece:

- Stage each equation change in the derivation — the forward process's
  closed-form marginal, the reverse mean parameterization, the collapse of
  the full variational bound to `L_simple` — as a decision forced by a named
  constraint (tractability, variance, or a stated empirical result), so the
  reader sees why this move was taken over the alternative left on the table.
  A step presented as mere algebraic tidying has lost the argument.
- Give every equation a sentence that is its own: what it buys, stated before
  or immediately after it appears. No equation sits between two paragraphs
  unaddressed.
- Cite a figure only when the adjoining sentence names the specific claim it
  settles. A figure introduced to depict what the prose has already fully
  stated is decoration.

## Licenses

```text
form: payoff-first equation lead-in
move: Weng and Song both open a load-bearing equation with one clause naming
      the capability or problem it resolves, before or as the equation lands
      ("a nice property of the above process is that we can sample x_t at
      any t in closed form"; "by modeling the score function instead of the
      density, we can sidestep the intractable normalizing constant").
bar:  the clause must name a concrete capability the equation immediately
      supplies or a concrete problem it removes — never generic scene-setting
      ("we can now see that..."). If the equation that follows delivers less
      than the clause promised, cut the clause.
```

```text
form: worked instance before the general form
move: Olah solves a small concrete graph by hand before stating the general
      backprop algorithm, so the general statement reads as the pattern
      already executed, not a new claim.
bar:  reserve for the single equation the article's argument turns on — the
      collapse of the variational bound to L_simple, or the closed-form
      marginal. Resolve it for one concrete step (a single t, or the t=1
      case) before the general statement. Used more than once in the piece,
      it stops being a derivation and becomes a tic.
```

```text
form: figure captioned as a claim, not a description
move: Song cites a figure to show a specific failure (score estimates
      drifting into low-density voids) before the fix is introduced — the
      figure is the reason the naive approach is abandoned, not an
      afterthought illustrating a conclusion already stated in prose.
bar:  the caption or its adjoining sentence must name the specific claim the
      figure supports or the specific alternative it rules out (a sample
      grid that settles a quality comparison, an algorithm box that settles
      what the sampler actually iterates). A caption that only describes
      contents defaults out of license.
```

```text
form: paired construction stating a real opposition
move: Olah states forward-mode and reverse-mode differentiation in two
      grammatically parallel sentences ("Forward-mode tracks how one input
      affects every node. Reverse-mode tracks how every node affects one
      output.") so the opposition is legible at a glance.
bar:  both halves must already be true and established by the argument at
      that point — mean-prediction versus noise-prediction, forward process
      versus reverse process — not invented for the symmetry. Each half must
      state something the other doesn't. Use once per real opposition in the
      piece; a third use reads as a mannerism.
```

## Recently used, do not reuse

The commission flags this directly: break the outline, opener, and closer
shape of the other paper-of-the-day slugs rather than inheriting one. Two
consequences for this voice guide's own licenses — do not let the
payoff-first lead-in above harden into a repeated formula ("a nice property
of..." used at every equation is the tell); do not let the worked-instance
license fire more than the single time it's reserved for. Both would produce
exactly the stamped, recurring shape the house standard already bans in
headings and deks and that the commission separately bans at the structural
level.

## Lilian Weng, "What are Diffusion Models?"
Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
Craft:
- cadence: a short definitional sentence lands immediately before the
  equation it defines; sentence length expands right after an equation to
  unpack what it now licenses, then contracts again ahead of the next one.
- argument: each section states a constraint, then produces the
  reparameterization that removes it — intractable posterior, then the
  conditioning on x0 that makes it a closed Gaussian.
- evidence: a simplified objective is defended by citing what the original
  authors found trained better, not only by the algebra that makes it
  cleaner — the empirical result outranks the derivation's elegance.
- stance: reports what the field found; opinion surfaces only as naming
  which variant "works better," never as unsupported preference.
- notice: catches the exact moment a term turns tractable — conditioning the
  reverse step on x0 converts an intractable object into a known Gaussian —
  and flags that pivot with a plain "we cannot... but if we condition on
  x0..." rather than letting it pass inside a paragraph.
- diction: technical nouns stay literal — score, marginal, closed form — with
  no adjectives dressing up a term once it's defined.
- reader: assumes the reader can hold an equation across two sentences;
  transitions name what changed rather than re-explaining it.
- the move the other axes miss: a simplification of the training objective
  is narrated as a reported empirical decision, not a mathematical
  convenience — the piece stays honest about which steps are proof and which
  are a choice the authors made and defended with a result.

## Yang Song, "Generative Modeling by Estimating Gradients of the Data Distribution"
Source: https://yang-song.net/blog/2021/score/
Craft:
- cadence: accelerates into short declaratives to state a problem,
  decelerates into longer sentences around the dense equation that follows,
  then a short sentence names the consequence.
- argument: discovery through failure — the naive method is stated, shown
  failing, and only then is the fix earned. The fix never arrives as the
  obvious first move.
- evidence: a figure is entered as proof that the naive approach fails
  (score estimates accurate only where data is dense, sample trajectories
  drifting into the gaps), and that figure is the stated reason the method
  is abandoned, not an illustration added after the argument already closed.
- stance: matter-of-fact even at the turn — the moment a normalizing
  constant drops out of the objective gets one exclamation point and an
  immediate sentence of consequence, not a celebration.
- notice: catches exactly where an assumption breaks — too few data points
  in low-density regions make the score-matching objective's implicit
  weighting fail — and states it as a named mechanism, not a vague caveat.
- diction: a physical analogy (Langevin dynamics) is stated once to seat the
  intuition, then dropped rather than carried as a running metaphor.
- reader: assumes the reader can follow a discrete-to-continuous
  generalization (noise scales becoming an SDE) without each step re-derived.
- the move the other axes miss: a figure only ever appears to demonstrate a
  specific failure or a specific gain the prose has not yet stated in full —
  it does argumentative work, rather than restating a conclusion prose
  already reached.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"
Source: https://colah.github.io/posts/2015-08-Backprop/
Craft:
- cadence: a short question opens a beat ("If a changes a little bit, how
  does c change?"), and the definition that answers it lands in one plain
  sentence directly after.
- argument: generalizes from a single worked instance — a small concrete
  graph solved by hand — before stating the general algorithm, so the
  general statement reads as the pattern the reader already executed.
- evidence: the diagram carries the actual proof step. The annotated graph
  showing that a naive method must sum nine paths is where the combinatorial
  problem becomes visible; the prose narrates what the diagram has already
  shown, rather than the diagram decorating a conclusion prose stated first.
- stance: plainly instructional throughout, first-person plural, no
  hedging on what the reader should now see.
- notice: catches the exact point where complexity becomes a problem —
  naming the paths a naive method must sum — before naming the fix, so the
  fix reads as necessary rather than clever.
- diction: parallel grammatical construction states a real opposition
  ("Forward-mode differentiation tracks how one input affects every node.
  Reverse-mode differentiation tracks how every node affects one output.").
- reader: builds every term from the toy example and assumes no prior
  familiarity with the specific algorithm, though calculus itself is a given.
- the move the other axes miss: the worked toy instance is not a warm-up —
  it is the derivation. The general algorithm is presented as the pattern
  already executed by hand, so the piece never asserts something new without
  having first shown it.
