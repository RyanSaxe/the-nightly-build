# Voice guide: paper reconstruction that sets math and cross-examines figures

## Directive

Write as a reviewer rebuilding a result on the page, not a teacher walking a
newcomer through it. The declared reader holds the math and the ML; they want
the machinery in front of them and the evidence weighed, and they will resent
being re-taught what a softmax is or being handed an equation wrapped in its own
restatement. Sharpen the house register in one direction: toward the evidentiary
posture of a careful reviewer. Equations are objects the prose reasons about.
Figures are testimony the prose cross-examines. A claim is something the prose
establishes, bounds, and then holds to a stated limit.

Three moves decide most sentences here, and each has a license below. First, an
equation earns its display by carrying an operation the prose then reasons from;
the sentences around it motivate the term and read off its consequence, and they
never say in words what the line already says in symbols. Second, a figure is
brought in to settle something; the prose names what it settles and where that
evidence stops, rather than describing what the picture looks like. Third, the
verdict on the contested question commits to a position and names its own edge in
the same breath.

Let cadence follow the reasoning. Derivation and setup run long and even;
verdicts snap short. A section that has been building for four clauses should land
its consequence in a sentence a reader could quote back. Define each symbol in the
clause where the argument first spends it, once, and reuse it exactly after. Keep
the first person out and keep the curiosity in: the reviewer's stance is
confident and bounded, not playful.

## Licenses

form: a displayed (set) equation with its surrounding prose
move: the studied writers place the line only after the prose has said what it
  computes and why the argument now needs it (Voita states the translation
  objective in words, then writes it; Weng names the context vector as a weighted
  sum of encoder states before the sum appears). The prose before it motivates,
  the prose after it spends the result on a consequence, and neither re-verbalizes
  the operation the line already shows.
bar: every displayed equation is preceded by the reason the argument needs it and
  followed by a sentence that draws a consequence from it rather than restating
  it; each symbol new to the declared reader is defined in the clause where it
  first appears. A sentence that narrates the operation the equation performs
  ("we sum the hidden states weighted by the alignment scores" beside the line
  that is that sum) fails.

form: a source figure carried as evidence, with caption and discussion
move: the writers introduce a figure to settle a specific question and say what it
  settles (Voita: "from the examples, we see that attention learned soft alignment
  between source and target words — the decoder looks at those source tokens which
  it is translating"). They read the figure as data — what was measured, on what —
  not as a picture to admire, and they name the limit of what one figure can show.
bar: each figure's caption or discussion states in one sentence what the figure
  establishes about the claim, and where the evidence turns on a measurement, names
  what was measured and against what baseline. A caption that only labels axes or
  names the figure, or a discussion that describes the image without saying what it
  settles, fails.

form: a bounded verdict on the contested question
move: the reviewer states what the evidence establishes and, in the same passage,
  bounds it — holding the demonstrated result apart from the interpretation laid
  over it (Recht separates what a practice observably does from what it is taken to
  mean, and commits to the first while questioning the second). The verdict takes a
  position and marks the edge where that position stops.
bar: the verdict names, as distinct claims each carried by its own cited source,
  what the original established and what the after-record contests, then commits to
  a position and states the boundary where it stops holding. A verdict that hedges
  without naming that boundary, or that asserts past the cited evidence, fails.

## Lilian Weng, "Attention? Attention!"
Source: https://lilianweng.github.io/posts/2018-06-24-attention/
Craft:
- cadence: short declarative openers that state the problem, then longer chains
  that qualify it; the rhythm quickens into notation and slows for interpretation.
- argument: problem to mechanism to instantiation — the fixed-vector failure is
  built first so the remedy reads as a response rather than an announcement.
- evidence: tables serve as taxonomy of scoring functions, not proof; figures
  authenticate a specific claim ("the model is paying attention to" a named
  region), captions carry the interpretation.
- stance: assured authority with disclosed uncertainty; commits on the mechanics,
  hedges on motivation.
- notice: the bottleneck is felt before it is formalized — the encoder "has
  forgotten the first part once it completes processing the whole input."
- diction: concrete anchors (named image regions) bridged to abstract terms
  (representation, alignment) by metaphor introduced and then dropped.
- reader: assumes RNNs, LSTMs, basic architectures; refreshes by link, defines
  only what is new, moves into formal math without apology.
- the important move: notation is introduced incrementally and each symbol is a
  servant to the argument — encoder states, then weights, then the scoring
  function named in words before its algebraic form. The math never arrives cold.

## Christopher Olah and Shan Carter, "Attention and Augmented Recurrent Neural Networks"
Source: https://distill.pub/2016/augmented-rnns/
Craft:
- cadence: dramatic variation, from "They can be combined." to forty-word
  multi-clause builds; intuition arrives by embodied analogy before any mechanism.
- argument: four techniques revealed to share one underlying device, so the
  meta-claim (disparate innovations, common structure) outweighs any single part.
- evidence: figures illustrate exactly the narrowed focus the prose has just named
  ("let's focus on reading"); the visual shows the instantiation the prose defines.
- stance: bold on established technique, openly speculative on the frontier ("our
  guess is"), with the two kept visibly apart.
- notice: process is described as degree, not switch — "every step, they read and
  write everywhere, just to different extents."
- diction: embodied and concrete; operations stated as human action before they
  generalize.
- reader: assumes little; defines the RNN, invites collaborative working-through.
- the important move: this piece uses zero notation, and reads as evidence for the
  opposite discipline — do not inherit its notation-avoidance. Take its figure
  craft (the picture shows precisely what the prose just narrowed to) and leave its
  refusal to set math, which this commission explicitly reverses.

## Elena Voita, "Sequence to Sequence (seq2seq) and Attention"
Source: https://lena-voita.github.io/nlp_course/seq2seq_and_attention.html
Craft:
- cadence: two-beat pedagogical rhythm, mechanism then constraint, extending into
  conditionals exactly where a naive approach fails, building pressure the
  mechanism then releases.
- argument: computational constraint drives the narrative — compression demand,
  then decoder failure mode, then attention as the differentiable resolution, so
  the development feels necessary rather than arbitrary.
- evidence: alignment figures read as legible testimony to what the mechanism
  discovered; "from the examples, we see that attention learned soft alignment"
  states what the picture settles and then what the model is doing at each step.
- stance: teaching honesty — hedges on approximations and trade-offs, absolute on
  the core ("since everything here is differentiable, a model with attention can be
  trained end-to-end").
- notice: names the bottleneck as a burden on both ends, not just the encoder —
  the single vector is "also hard for the decoder."
- diction: oscillates and immediately materializes terms; alignment glossed as
  "what is translated to what."
- reader: assumes basic neural networks and language modeling, references prior
  material by link, invites the reader to watch the weights change step to step.
- the important move: the equation always follows the intuition — the objective is
  stated in words, then written — so notation confirms an argument the reader
  already holds rather than opening one.

## Benjamin Recht, "Machine Learning Evaluation"
Source: https://www.argmin.net/p/machine-learning-evaluation
Craft:
- cadence: long multi-clause exposition that snaps to short declaration when a
  verdict lands; sentences stretch for theory and shorten for judgment.
- argument: distinguishes what a practice observably is from what it is taken to
  mean, committing to the first while pressing on the second.
- evidence: anchors claims to specific references; separates observed practice
  ("most of the time... 'articulate' means 'quantify'") from open inquiry.
- stance: confident but bounded — professorial authority alongside disclosed
  limits, asserting influence without claiming completeness.
- notice: reads a stated result against the interpretation layered on it and finds
  the gap between them.
- diction: specialized vocabulary sits beside plain phrasing so a technical claim
  stays legible.
- reader: addressed as a peer who will accept both rigor and an admitted boundary.
- the important move: the verdict is delivered and bounded in one motion — the
  position is taken and its edge marked together. Take that structure; leave the
  first-person and the playful self-reference, which this register does not carry.
