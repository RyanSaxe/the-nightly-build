# Voice guide: paper-of-the-day/double-descent (01)

## Directive

Write for a machine-learning engineer who knows bias, variance, and
over-parameterization cold and wants the double-descent claim rebuilt from its
own figures and math, then judged. Assume that reader; skip the primer and
spend the space on the reconstruction and the verdict.

The piece runs in two registers and the writing has to switch between them
cleanly, because the house baseline (calm first-principles exposition, Olah and
Weng patience) supplies only the first one.

- **Builder.** When you set up a figure or an equation, walk it one visible
  step at a time and make the artifact carry the point. A figure earns its place
  only when a sentence names the exact feature that settles a claim: which axis,
  which peak, where the curve turns. The same holds for the one set equation.
  Point the reader at the thing on the page, do not gesture past it. If the prose
  would read identically with the figure deleted, the figure is decoration and
  the sentence has not done its job.
- **Reviewer.** When you weigh the claim, first restate what the paper actually
  established, in its own terms and at full strength, before you press on it.
  Then test it against the after-record with a specific hand: what was measured,
  on what, at what label-noise level, and what would count as the effect failing
  to appear. Mark the boundary between what the evidence settles and what is
  still open in the sentence itself, not in a hedge. Commit to a verdict; state
  it proportionately to the evidence, and let it be able to come out either way.

The register turn is a real seam in the argument. Signal it by what the sentence
does (building versus testing), the way Weng marks a shift into comparison with
"Compared to..." or "However, according to...". Do not narrate the turn.

## Licenses

form: collaborative walk-through ("we" / "let us" tracing a construction)
move: Olah and Weng put the reader inside a derivation or transformation with
      "let us define..." and "we can see...", advancing one operation the reader
      can then verify against the figure or the math. Deploy while building a
      concept before the sentence that spends it.
bar:  the "we" must name the next concrete operation the reader can check against
      the artifact on the page. Cut it wherever plain third person says the same
      thing.

form: rhetorical gate question answered in the same passage
move: Huszar opens a test with a blunt question ("Does the argument hold water?")
      and the next sentences settle it with evidence. Deploy at the pivot from
      building a claim to weighing it.
bar:  the passage answers it with cited evidence before the next heading, and the
      honest answer must be able to be "no". At most one per register-turn; a
      question left hanging is cut.

form: measured understatement at the verdict
move: Huszar rates a claim dryly and in proportion ("it passes my bar for an
      interesting narrative. However, ... I don't consider it much stronger
      than..."), neither inflating the result nor sneering at it.
bar:  the wording attaches to a specific reservation the evidence earned. If it
      reads as wit for its own sake, or announces its own stakes, it goes.

## Recently used, do not reuse

- The "follow-up work disagrees" catalog framing, and any structure that lines
  up subsequent papers as a roll-call of objections. It was used for grokking
  and emergent-abilities. Rebuild and weigh one argument; fold each critique in
  where it changes the interpretation, never as a catalog beat.
- The dek molds that framing traveled with: a subsequent-work reversal, a
  suspended "the real question is whether", a comma triad of clauses. Cut on
  sight.
- Heading cadence that keeps joining two clauses with a comma and "and". Vary
  the shape across the piece; a reader skimming only the headings should
  reconstruct the argument, not hear a stamp.

## Chris Olah, "Neural Networks, Manifolds, and Topology"
Source: https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/
Craft:
- cadence: short declarative problem statement, then a longer exploratory
  sentence, then a claim the visualization can confirm; the alternation gives
  dense material room to breathe.
- argument: strictly incremental. Each step is small enough to see, and every
  new step reuses what the previous one established rather than restarting.
- evidence: the figure is the proof, not an illustration of a proof stated
  elsewhere. Prose points at a specific visible feature and the reader verifies
  the claim by looking.
- stance: guide through a genuine difficulty. Anticipates the confusion and
  meets it before it derails the reader.
- notice: the spatial behavior of the transformation (stretching, squishing,
  untangling) and where it stalls, over the formal object.
- diction: concrete active verbs for abstract operations; a formal term arrives
  attached to what it does before its definition.
- reader: collaborative and verifying. Invites checking rather than belief, and
  admits the limits of his own knowledge without losing authority.
- the move the axes miss: he introduces a concept visually first and only then
  names it and formalizes it, so the term lands on something the reader already
  saw happen.

## Lilian Weng, "What are Diffusion Models?"
Source: https://lilianweng.github.io/posts/2021-07-11-diffusion-models/
Craft:
- cadence: equation, then a plain-sentence interpretation, then the next
  equation the interpretation set up; short declaratives break long derivations
  so density never compounds.
- argument: each concept is built in the order motivation, mechanism, evidence,
  and only then spent on the next dependent idea.
- evidence: mathematics is earned by prose setup, never dropped cold; every
  quantity is named and labeled before it is used, so a later line can lean on
  the label instead of re-deriving.
- stance: assumes competence, adds no hand-holding beyond what the step needs,
  and never condescends.
- notice: the exact property a method unlocks (a deterministic map enabling
  interpolation) and what it costs, over restating what the method is.
- diction: precise, restrained, technical without ornament; terms of art used
  exactly and repeated exactly.
- reader: a practitioner who could implement this; comparisons are framed as
  what one method buys over another.
- the move the axes miss: transitions are labeled by function ("Compared
  to...", "Empirically, ... found...", "However, according to..."), so the
  reader always knows whether the next sentence builds, compares, or complicates.

## Ferenc Huszar, "Mortal Komputation: On Hinton's argument for superhuman AI"
Source: https://www.inference.vc/mortal-computation-hintons/
Craft:
- cadence: short decisive opening or gate ("Does the argument hold water?")
  anchoring a longer analytical chain; a punchy one-line summary can precede the
  full treatment.
- argument: reconstruct the other side at full strength first, crediting what is
  persuasive, then object; the fair rebuild is what makes the skepticism land.
- evidence: tests a claim with a concrete lived case rather than an abstract
  objection, turning a theoretical assertion into observable behavior that
  either holds or does not.
- stance: skeptical but not dismissive; grants the argument its interest, then
  bounds it.
- notice: the gap between what a claim asserts and what would actually be
  observed if it were true.
- diction: plain and blunt, dry wit held in reserve for the verdict, never
  reaching for the generic academic hedge.
- reader: a peer who can follow a technical case and wants the reviewer's honest
  standing, not a summary.
- the move the axes miss: the verdict is explicit, placed at the pivot, hedged
  only where the evidence is genuinely thin, and framed so it could have gone the
  other way.

## Self-test

The house default already gives this writer calm, precise, first-principles
exposition and Olah/Weng patience. What it does not give, and what this guide
adds, is the disciplined switch between a builder who makes each figure and the
one equation settle a named claim, and a reviewer who rebuilds the double-descent
argument fairly and then commits to a verdict against the label-noise and
replication record. A draft that stays in one register the whole way, or that
lets a figure sit without a sentence naming what it settles, has ignored the
calibration.
