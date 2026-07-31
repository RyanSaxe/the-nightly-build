# Voice guide — paper-of-the-day/emergent-abilities

## Directive

Write as a reviewer adjudicating a dispute between two papers, not as a
narrator recapping either one. Address no one; the reader is inferred from
what you choose to define, never named. State Wei et al.'s claim in its own
terms before you touch Schaeffer et al. — what "emergent" meant, what counted
as evidence for it, what threshold language they actually used — so the
critique lands on the claim itself and not on a version of it you built to
be easy to knock down. Only after the claim stands on its own do you bring
the second paper to bear on it.

Make the discontinuous-vs-continuous point with arithmetic, not adjective.
Take one task, one metric, and walk a model's actual per-token probability up
across scale in small steps; then run that same rising sequence through
exact-match scoring and through a continuous score (edit distance, Brier)
side by side, so the reader watches one produce a cliff and the other a
slope from identical underlying improvement. The argument is the numbers
moving, not a sentence declaring what they mean. State the mechanism first
(how a threshold rule amplifies a smooth curve), then run the numbers, then
draw the conclusion — in that order, not conclusion first with numbers as
decoration.

Structure the reconstruction so each section spends a term the last one
defined and nothing earlier. Establish emergence as Wei et al. defined it
before Schaeffer's rebuttal enters; establish what a discontinuous metric is
before applying it to a task; establish the concrete task and its scoring
before generalizing about what does and doesn't survive. A reader who skips
a section should be lost, because every later paragraph is spending
something the piece just bought.

Weigh the two papers by giving each its strongest form before you rule.
Name precisely what Schaeffer's metric argument explains and where it stops
explaining — the unpredictability of when a real benchmark's exact-match
score crosses a usefulness threshold is a fact about deployment planning
that a smoother continuous curve underneath does not erase. State that
distinction as a finding, not a concession wrung out of either side. Commit
to a verdict once you've drawn it; do not soften it back into "both sides
have a point" in the closing lines.

Vary sentence length on purpose. A short sentence should land a fact or a
turn; a long sentence should be doing real work — carrying a chain of
numbers or an if-then through to its conclusion — not accumulating clauses
for weight. Let verbs carry the claims ("the score crosses," "the curve
flattens") rather than nominalizations ("the crossing of the score," "the
flattening of the curve"). One earned longer sentence at a real pivot is
fine; three in a row is a run-on wearing paragraph breaks.

**Recently used, do not reuse:** the reveal that "the paper's own table
already recorded the catch," the closer that "the field has no agreed
account," an opening that measures time since publication before saying
what changed ("N years later, follow-on work shows..."), a Background /
Method / Results / Verdict scaffold or any heading that would still make
sense on a different paper, and a heading built from two clauses joined by
a comma and "and." Keep hedged not-X-but-Y contrasts to one, and only where
the "not X" is a misreading a real reader would actually make.

---

## Chris Olah et al., "The Building Blocks of Interpretability"
Source: https://distill.pub/2018/building-blocks/
Craft:
- cadence: opens on one short declarative, then a longer sentence that
  enumerates the stakes — short claim, then the reasons it matters, in that
  order every time a new idea starts.
- argument: names the gap (techniques studied in isolation) before proposing
  the move (combine them), so the contribution is legible before any method
  appears.
- evidence: prefers one worked visual case (a network detecting floppy ears)
  over an abstract description of what interpretability techniques do in
  general.
- stance: collaborative and unhurried; never rushes to the payoff before the
  reader has the pieces to receive it.
- notice: introduces a piece of jargon and immediately glosses it inline
  ("reify (or instantiate)") rather than defining it in a separate sentence,
  so definition and use happen in the same breath.
- diction: plain nouns for the mechanism, technical nouns only for what is
  genuinely new; "we" throughout, never "the reader."
- reader: treated as a capable collaborator being walked through a build,
  not an audience being told a result.
- the move the axes miss: it earns every abstraction by cashing it out in
  the very next sentence — an abstract noun never survives two sentences
  without a concrete referent attached to it.
Calibration: "Interpretability techniques are normally studied in
isolation. We explore the powerful interfaces that arise when you combine
them — and the rich structure of this combinatorial space."

## Mitchell Hashimoto, "Prompt Engineering vs. Blind Prompting"
Source: https://mitchellh.com/writing/prompt-engineering-vs-blind-prompting
Craft:
- cadence: a longer definitional sentence followed by a short, flat verdict
  sentence — the short sentence does the work the long one set up.
- argument: draws the boundary by defining the thing and its failure mode
  side by side, so the reader sees the category by seeing what falls
  outside it.
- evidence: names the concrete practice under critique specifically enough
  that a practitioner recognizes their own habits in it, rather than
  gesturing at "bad practice" generally.
- stance: unbothered and direct; states a position and moves, without
  hedging or pre-apologizing for having one.
- notice: coins a term for the failure mode being named, then uses that
  term exactly, never swapping in a synonym once it's set.
- diction: plain, almost conversational sentences carrying precise claims;
  no ornamentation, no rhetorical questions.
- reader: a peer being handed a distinction worth having, not a novice
  being taught vocabulary for its own sake.
- the move the axes miss: the negation ("X is not Y") is stated once, does
  real definitional work, and is never repeated — it's a tool for drawing a
  boundary, not a rhythmic device reached for again later in the piece.
Calibration: "'Prompt Engineering' emerged from the growth of language
models to describe the process of applying prompting to effectively
extract information from language models... Blind prompting is not prompt
engineering."

## Ferenc Huszár, "Mortal Komputation: On Hinton's Argument for Superhuman AI"
Source: https://www.inference.vc/mortal-computation-hintons/
Craft:
- cadence: mixes short personal asides with longer, carefully sequenced
  argument sentences; never lets the personal material replace the
  argument, only frames it.
- argument: restates the claim under review in a dedicated summary before
  attacking any part of it, then finds the specific hidden premise the
  whole argument actually depends on and tests that premise alone.
- evidence: uses one concrete personal example (learning an irreversible
  grammar rule as a language learner) to make an abstract distinction
  (human metacognition vs. current model training) checkable by the reader.
- stance: openly first-person and willing to land short of full conviction
  — states agnosticism as the honest conclusion rather than manufacturing a
  stronger verdict than the evidence supports.
- notice: flags the historical irony (the same figure once called neural
  nets impossible) as a reason for humility, without letting it stand in
  for an argument on the current question.
- diction: technical vocabulary used exactly once introduced, informal
  connective tissue around it; contractions and first person throughout.
- reader: an informed peer capable of following a chain of reasoning to
  wherever it actually ends, including "unresolved."
- the move the axes miss: the verdict is calibrated to the strength of the
  argument just made, not to how satisfying a strong verdict would be —
  the piece stops exactly at the confidence its own evidence earns.
Calibration: "Hinton's argument actually critically hinges on artificial
neural networks being as efficient at learning from any single interaction
as biological brains are."
