# Voice guide — knowledge-distillation

## Directive

Write for a reader who already holds softmax, logits, gradients, and
cross-entropy, and resents having them re-explained. Spend that fluency: skip
the primer and open on the specific puzzle the paper answers. The register is a
calm technical paper. Structure carries the persuasion; adjectives do not.

Build every concept before the sentence that spends it, and only the concepts
this argument spends. When a term of art first appears (soft target, fidelity,
dark knowledge), give it one plain sentence of meaning at that spot, then reuse
the exact name without variation. Do not gather definitions into a glossary
paragraph; introduce each where the reader first needs it, the way you would
lay a stepping stone just before the foot lands.

Teach the mechanism concretely. A temperature-scaled softmax is a formula the
reader can hold, so hold it: show what raising the temperature does to one
distribution before you claim what it does in general. Ground the abstract move
in the paper's own worked case (the digit that is 10^-6 a three and 10^-9 a
seven) rather than restating the abstraction louder. An equation is a sentence.
Punctuate it, read it aloud in prose, and make the surrounding text carry its
meaning so a reader who skips the display still follows.

Then change stance. The second half of this piece is a review, not a summary. A
review states what was measured, on what, and what would count as the claim
failing, then commits to a verdict the evidence earns. Name a weak or narrow
result plainly. Do not stage the reversal as drama ("but here is the twist"),
and do not hedge it into mush. Two numbers that disagree are the whole finding;
report both, say which measurement governs, and stand behind the reading.

Sentences are short and single-purpose. A long sentence is allowed when it is in
control and earns its length. Reach for the period before the semicolon, the
colon, or the dash. Cut any sentence that grades the article, announces its own
importance, or narrates where the piece has been or is going. Let the teaching
and the citations equip the reader; skip the moral.

Recently used, do not reuse: the "the paper's own table/proof already recorded
the limit" opener; the bare "weigh the claim against the follow-on" move written
as a visible scaffold or announced as the plan; colon-subtitle headlines
("Distillation: How Soft Targets Changed Deep Learning"); the banned dek molds
(semicolon reversal "X did A; Y refuses B", the suspended question "and the real
question is whether", the comma triad closed with "and"); section headings that
keep joining two clauses with a comma and "and".

## Chris Olah, "Understanding LSTM Networks"
Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/
Craft:
- cadence: short declaratives that each add one mechanism, paced so a diagram or
  a worked step lands between claims; almost no subordinate clauses.
- argument: problem-first scaffolding — establish why the simple thing fails
  (long-term dependencies) before naming the fix (gates), so the solution
  arrives as relief, not assertion.
- evidence: the walk-through is the evidence; he traces one example through the
  cell step by step rather than asserting behavior from the equations.
- stance: a trusted guide who has done the reading and hides none of the ladder.
- notice: points at the one part that matters ("the key to LSTMs is the cell
  state") instead of describing everything at once.
- diction: plain, concrete, occasional homely analogy ("kind of like a conveyor
  belt") used to carry structure, not to decorate.
- reader: anticipates the confusion and disarms it ("Don't worry about the
  details") before going deeper.
- the important move the axes missed: he defines each gate at the moment the
  data flow reaches it, so the reader never carries an unexplained symbol.
Calibration: "Humans don't start their thinking from scratch every second. As
you read this essay, you understand each word based on your understanding of
previous words."

## Lilian Weng, "Attention? Attention!"
Source: https://lilianweng.github.io/posts/2018-06-24-attention/
Craft:
- cadence: progressive concreteness — an intuitive one-sentence gloss first,
  then the formal object, then the equation, each step tightening.
- argument: assembles a mechanism from parts the reader already holds, naming
  the whole only once the parts are in place.
- evidence: equations are load-bearing and read as sentences; she names each
  symbol as she writes it rather than after.
- stance: rigorous but warm; precise without performing difficulty.
- notice: parenthetical restatements pin a term at first use ("context vector
  (also known as ... 'thought' vector)") so no reader is stranded.
- diction: clarity over jargon; she brackets a technical phrase with an
  accessible one instead of choosing between them.
- reader: assumes real background and speaks to it ("as you may have read in
  many papers"), never talking down.
- the important move the axes missed: she defines a term at its point of use,
  inside the sentence that needs it, not in a preamble.
Calibration: "attention in deep learning can be broadly interpreted as a vector
of importance weights: in order to predict or infer one element ... we estimate
using the attention vector how strongly it is correlated with ... other
elements."

## Andrej Karpathy, "A Recipe for Training Neural Networks"
Source: https://karpathy.github.io/2019/04/25/recipe/
Craft:
- cadence: understated, clause-light sentences that move from a general
  principle to a concrete failure it predicts.
- argument: separates what is claimed or looks correct from what actually
  happens in practice, and treats the gap as the real subject.
- evidence: hard-won practitioner observation stated flatly, so the reader
  trusts it because it is specific, not because it is loud.
- stance: skeptical realism earned by having been burned; he suffers the
  failure alongside the reader rather than lecturing from above.
- notice: flags the silent failure mode — the thing that "works" without
  working — which is exactly the fidelity-vs-accuracy gap this article needs.
- diction: plain, slightly dry, severity kept understated ("it's really hard to
  tell") so the judgment feels earned.
- reader: a peer who has shipped models, addressed as an equal.
- the important move the axes missed: he holds a comfortable belief against
  what measurement shows and lets the discomfort stand, without softening it
  into a hedge.
Calibration: "Everything could be correct syntactically, but the whole thing
isn't arranged properly, and it's really hard to tell."
