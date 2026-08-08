# Voice guide: build-from-scratch/rotary-position-embeddings (01)

## Directive

Keep the house register: calm, precise, argued from first principles, each
concept built before the sentence that spends it. What this piece adds is a
build-along stance. The reader is a peer at a keyboard who will run the code and
check the number, not an audience being shown a result. Write so that the
evidence carries the claim and the prose carries only intent and consequence:
say why the next artifact exists and what follows once it lands, and let the
equation, the listing, and the printed number do the proving in between.

Three moves will change sentences here.

Thread one concrete instance through the whole piece. Pick a specific case (a
fixed pair of tokens at fixed positions, a small head dimension) and reuse its
actual numbers in the prose, in the equation, and in the code, the way a good
teacher deepens a single worked example instead of introducing a fresh one for
each idea. A second instance enters only when the first cannot show the new
point. Switching examples for variety costs the reader the ground they were
standing on.

Let the load-bearing identity be the turn of the argument, not an aside inside
it. When the piece reaches the fact that the whole construction rests on (the
dot product depending only on the angle difference), give it its own approach
and its own consequence. Do not bury it in a clause and do not announce its
importance in words the derivation has not yet earned; show the cancellation and
the phase falling out.

Report from the run, never from intention. Every number in the piece is a number
the committed code produced. Frame it plainly and let a close reading of it,
including where it falls short, do more work than a triumphant version would.

Do not narrate the code or transcribe the math. A sentence that restates a line
the reader can already read, or reads an equation back into words, is cut.

## Licenses

form: the derivational "we"
move: the studied implementers use "we" to fix the goal a construction must meet
  before they build it ("we want a function whose inner product depends only on
  the offset"), so the reader follows the design choice rather than receiving a
  finished result. Deploy it at the moments the piece commits to a requirement or
  a next step.
bar:  each "we" sentence states a constraint or goal that the following line
  satisfies. A "we" that narrates the article or the newsroom rather than the
  derivation is cut.

form: the intent-framed equation
move: the exemplars name what an equation must accomplish in the sentence before
  it, show the equation, then read off its consequence in one plain sentence,
  often by naming what the result now equals or reduces to. The prose sets up and
  interprets; the symbols do the step.
bar:  the sentence before a displayed equation states its job and the sentence
  after states what now follows. A sentence that transcribes the equation's
  symbols back into words earns nothing and is cut. Define a symbol inline the
  once, where it first appears.

form: the code listing as the argument's evidence
move: strong from-scratch implementers set a listing's purpose in a single line,
  let the block stand, and add at most one sentence naming what it produces or
  verifies. They trust the reader to parse code and never walk the lines.
bar:  every sentence adjacent to a listing states the listing's intent or its
  result. A sentence paraphrasing a line the listing already shows is cut. The
  listing must carry a step of the argument, not decorate one the prose completed.

form: the result reported from a real run
move: the exemplars pin each number to the exact conditions that produced it (the
  step count, the token count, the shape, milliseconds against a named baseline)
  and refuse to oversell it; the honest framing is what makes it land.
bar:  each reported number names the run that produced it and a comparison the
  reader already holds. A number without its conditions, or a number no committed
  run produced, is cut.

form: the plain admission of the prototype's limits
move: the from-scratch writer foregrounds the small version as a teaching object
  and says, without apology, exactly where it stops short of the production
  system. The candor advances the argument rather than qualifying it.
bar:  each admission names one specific thing the real system does that the
  prototype does not, in a clause, with no hedge and no apology. A vague gesture
  at "simplifications" is cut.

## EleutherAI, "Rotary Embeddings: A Relative Revolution"
Source: https://blog.eleuther.ai/rotary-embeddings/
Craft:
- cadence: staccato problem-framing ("What's the Problem?") opening into flowing
  derivation, then tightening again for results. Short question, long answer.
- argument: problem, then intuition, then rigorous derivation, then
  implementation, then measured results. The claim is front-loaded and the
  derivation is what earns it back.
- evidence: results arrive as small labeled tables and exact figures tied to
  conditions ("at 55k steps, ~30B tokens"; "5.3 milliseconds" against a baseline
  "2.1 milliseconds"). Every quantity carries its measurement.
- stance: collegial and candid; admits the field's own first reaction to the idea
  and uses that as a way in rather than a flourish.
- notice: points at the single fact the whole scheme rests on, that corresponding
  components equate so absolute phase cancels, and gives it the derivation's
  weight rather than a sentence's.
- diction: technical vocabulary held straight, with occasional plain-English
  bridges before a dense step. Metaphor used sparingly and only where it pays.
- reader: assumes fluency with dot products and attention, not with position
  encoding specifically; teaches exactly the gap.
- the move the axes miss: it announces an equation's purpose before showing it
  ("putting the pieces together, we get the final formula:") and lets the code
  implementations stand with a single note on layout, never a walkthrough.

## Lilian Weng, "The Transformer Family Version 2.0"
Source: https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/
Craft:
- cadence: medium-length, accumulative sentences; a steady layering rather than a
  brisk pace. Simple statement, then a clause that deepens it.
- argument: the "why" precedes the "what" everywhere. The problem a formula solves
  is stated before the formula, so the equation confirms an idea the reader
  already holds instead of introducing a cold one.
- evidence: equations and notation carry the load; a defined symbol table lets the
  math stay terse.
- stance: expository and even; "Note that" and "Interestingly" create a quiet
  collegiality without argument-by-adjective.
- notice: catches the equivalence a reader would miss, that a rotation
  formulation is the sinusoidal encoding in another dress, and says so in one line.
- diction: clarity over elegance; concrete verbs ("divides", "constructs") anchor
  abstract operations.
- reader: moderate-to-advanced ML background assumed; terms used inside contexts
  that illuminate them rather than being pre-defined.
- the move the axes miss: after an equation, one plain sentence bridges it to
  something the reader already knows, then the prose moves on. The math is trusted
  to have made the step; the prose never re-derives it in words.

## Chris Olah, "Calculus on Computational Graphs: Backpropagation"
Source: https://colah.github.io/posts/2015-08-Backprop/
Craft:
- cadence: short declarative hooks followed by elaboration; conversational rhythm
  that keeps mathematical density from stacking up.
- argument: one small system, e=(a+b)*(b+1), is introduced early and revisited at
  every conceptual layer, so each new idea deepens a case the reader already owns.
- evidence: concrete numbers (a=2, b=1, e=6) make the mechanism visible before any
  general rule; the general rule then generalizes something already seen.
- stance: intimate, slightly conspiratorial; anticipates the reader's objection
  ("Isn't This Trivial?") and answers it head-on.
- notice: points at the combinatorial explosion the naive method hides and shows
  the factoring that escapes it, so the payoff is felt as a number ("a factor of a
  million").
- diction: technical terms sit beside plain phrasing without condescension;
  peer-to-peer, not lecture-hall.
- reader: assumes calculus comfort, not the algorithm; builds the algorithm from
  parts the reader has.
- the move the axes miss: reusing the identical small example across every layer
  instead of switching examples. The reader never re-anchors, so understanding
  compounds instead of resetting.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"
Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/
Craft:
- cadence: varied lengths for momentum; short declaratives alternating with longer
  technical sentences, occasional fragments to keep forward motion.
- argument: moves from a toy (a four-character vocabulary) to progressively larger
  real runs, foregrounding the toy as pedagogical rather than hiding its
  smallness, so later results read as the same principle scaled.
- evidence: generated samples and figures presented as raw output, framed by the
  run's conditions (dataset, architecture) set before the sample, not after.
- stance: professorial yet conspiratorial; direct address and light humor humanize
  the material without loosening the rigor.
- notice: reads the model's specific mistakes closely (a tag opened and closed
  wrong) and turns each error into evidence of how the thing actually works.
- diction: rigorous terms mixed with informal ones; knows when to pull a claim back
  ("Forget I said anything") rather than overstate.
- reader: treated as a fellow builder who will run the released code, addressed as
  a collaborator figuring it out alongside the writer.
- the move the axes miss: honesty as persuasion. Undersell the output ("clearly
  not going to replace Paul Graham anytime soon") and the credibility rises; the
  gap between toy and real is named plainly, never papered over.

## Self-test

The house default already supplies calm, first-principles patience and
concept-before-sentence teaching. It does not tell the writer how to choreograph
the three-way handoff this piece lives on: prose that frames intent, an equation
that takes the one step the prose cannot, and a code listing that produces the
number the claim rests on, with no sentence narrating the code or transcribing
the math. Nor does the default say how to report a result honestly from a real
run or how to reuse a single worked instance so understanding compounds. That is
what this article should sound like beyond the default: a build-along where the
evidence proves and the prose only points, and where the writer's candor about
what the toy leaves out is doing the persuading.
