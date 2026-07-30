# Editorial review — knowledge-distillation (editor 01)

## Skeptic
Skeptic: thesis "distillation reliably transfers a smaller model that
generalizes, but usually not the teacher's predictive distribution, because
copying the teacher is an optimization problem ordinary training does not
solve"; tested 5 claims; broke: none.

Claims tested against the owning primaries in the evidence record:
1. The 2015 machinery (temperature softmax, two-objective loss, 1/T² scaling,
   logit-matching as the high-T limit). Checked against Hinton [1] §2–2.1 and
   Eqs. 1–4. The article's equation legend, the T² bookkeeping, and the
   "matching logits is a special case" caption all state the paper correctly.
   The MNIST numbers (67 / 146 / 74 errors; 98.6% of unseen threes), the speech
   table (58.9 → 61.1, distilled 60.8, WER 10.9/10.7/10.7; ">80% transferred"),
   and the 3%-data regularizer (44.5% vs 57.0%) match [1] exactly.
2. Fidelity vs generalization and the fidelity gap. Checked against Stanton [4]
   §1, §3.2, §4.1, §5.1, §6.2. LeNet/MNIST ">99%", MixUp(τ=4) 86%, baseline(τ=4)
   84.5%, train agreement 78.95% (300 ep) → 83.3% (5000 ep), and the "teacher's
   own weights achieve zero loss" point are all read correctly, including
   directions (more data lowers *train* agreement; longer training barely moves
   it).
3. Born-Again as confirmation, not refutation. The article follows Stanton's own
   reading [4] §4.2 that a same-size student can only exceed the teacher by
   failing to match it; Furlanello [5] supplies the identical-capacity result.
   Correctly not presented as a fidelity success.
4. The successes: DistilBERT 40%/60%/97% [6] and Beyer's 82.8% ResNet-50 with
   patient, consistent, function-matching training to ~9600 epochs [7]. Verified
   against the abstracts and Beyer Fig. 1. "distilling during pre-training" is
   accurate to [6].
5. Müller [8]: a label-smoothed teacher distills worse because the between-class
   logit structure is erased. Correctly used to close the loop back to 2015.

Source kinds: all eight `data-nb-kind="primary"`. Each authoring team owns its
cited claim; there is no secondary reporting, which is right for a
paper-reconstruction. No `primary` label hides a missing independent source.
Headline and dek treated as claims: "inherits accuracy, not predictions" is a
fair compression of generalization-transfers / fidelity-usually-does-not, and
the body never overstates it (it notes the student can fall below or exceed the
teacher in accuracy). "an optimization problem no one had been solving" is
earned by Stanton's finding that ordinary training does not solve the fidelity
optimization and the field optimized accuracy instead. The dek makes a claim
about the world, not about the article's method. No revision required.

## Cut
Cut: 2 sentences reworked; worst tell: a stock-revelation frame.

Direct edits made in the article:
- Removed the stock reveal "There is a wrinkle that looks like a refutation and
  is really a confirmation." — replaced with "One result looks like a
  counterexample.", which states the move without announcing it.
- Removed the "not X but Y" mold "The fix is not a trick but a bill." — replaced
  with "The fix exists, and it is expensive.", keeping the one earned corrective
  contrast for the Verdict ("a smaller model that works, not a faithful
  replica").

Checked and left standing: "By 2015 the case looked closed" (a sourced claim
about the field's belief that the next section overturns, not self-grading);
"a different tool than its name promises" (earned, not a mold). No signposting,
no self-reference, no reader address, no instruction leakage: comparing the body
against the writer brief, none of the brief's planning vocabulary ("reconstruct",
"weigh against", "required contribution", "flex section") survives into prose.
Prose tells within budget: zero em-dashes, zero "mechanism", zero "leverage".
No semicolon chains remain (one was cut during the writer's density pass).

Furniture: the annotated temperature-softmax equation and the captioned
gradient-limit equation each carry reasoning the argument spends; the speech
table is three short numeric rows better as a table than prose; the single
strong Verdict note lands the takeaway; one chart, no pull quote. The page reads
as a continuous article, not a stack of blocks. Chart inspected: bars 84.5 / 86 /
99 match Stanton's Figs. 2–3, the dashed 100 line is labelled "perfect fidelity,"
axis and categories are legible after the writer widened the left margin, and the
caption states the two-task contrast honestly. Provenance script carries the
data and its locators.

## Reader
Reader: this gives me a single quantity — does the student match the teacher's
distribution — that unifies the 2015 wins and the 2021 failures, and a clear
practitioner rule for when distillation ships a distribution versus merely a
smaller working model.

Read straight through as the house reader (graduate ML): the piece builds each
term (dark knowledge, temperature, fidelity) at first use, spends the softmax
fluency it assumes, and turns from reconstruction to review without drama. What
it gives beyond the sources is exactly the writer's original-work sentence: the
sources are read against one another, with Hinton's results recast as the
fidelity claim Stanton measured, Born-Again reframed as evidence for low
fidelity, Müller closing the loop, and Beyer pricing the fix. That is synthesis
the sources do not perform themselves. Voice sits with the Olah/Weng/Karpathy
exemplars (concrete, first-principles, skeptical where it counts), not a median
summary. Headline retested as the largest claim: it commits to what the piece
establishes and states the finding with its actors.

## Visual evidence
Chart-1 is the only figure and it is evidence, not decoration: it isolates the
article's spine from Stanton's multi-panel figures. Numbers match the evidence
record and the owning primary; the image reads honestly. No source-asset capture
is warranted; the equations belong in KaTeX, not screenshots. No recrop needed.

## Decision
DONE. Two surgical prose fixes applied directly; no redraft required. The writer
reran the proof after the cuts: BLOCK 0, WARN 0, PUBLISHABLE, all eight source
URLs resolving under `--check-links`. Every load-bearing number traces to the
primary that owns it, the source kinds are honest, and the article delivers the
commission's required contribution.
