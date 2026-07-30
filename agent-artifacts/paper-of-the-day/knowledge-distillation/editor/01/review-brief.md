# Editor review-brief — paper-of-the-day/knowledge-distillation (01)

## Your task
Give the drafted article three ordered reads (skeptic, cut, reader). Make cuts
and small prose fixes directly. Return anything past a word or clause to the
writer, evidence gaps to the researcher. Record the review in
`editorial-review.md`. Approve only with a `DONE` that requires no change.

## Exact inputs
- `editorial-direction.md` (governing stack).
- The exact writer brief: `writer/01/brief.md` (handed to you so prompt leakage
  is detectable).
- `writing-coach/01/voice-guide.md` (read first).
- `researcher/01/evidence.md` (open on the first read; keep the draft-handoff's
  original-work sentence closed until the third read).
- `writer/01/draft-handoff.md`.
- The article: `library/paper-of-the-day/knowledge-distillation.html`.
- The chart provenance: `library/paper-of-the-day/knowledge-distillation/chart-1.py`
  and `chart-1.png`.
- Template context under `.nb-context/`.

## What to test hardest
- The thesis in the headline and dek: "inherits accuracy, not predictions," and
  "an optimization problem no one had been solving." Are they claims the piece
  earns, or overreach? A dek that grades the article's method rather than the
  world needs revision.
- Every number against the owning primary in the evidence record: the MNIST
  67/146/74 and 98.6%; the speech table and ">80%"; the 3%-data regularizer;
  Stanton's fidelity readings (LeNet >99%; MixUp τ=4 86%; baseline τ=4 84.5%;
  train 78.95%→83.3%); DistilBERT 40/60/97; Beyer 82.8% and ~9600 epochs;
  Müller's label-smoothing finding. Recompute directions.
- Source kinds: all eight are labelled `primary`. Confirm each authoring team
  owns its cited claim and that no `primary` hides a missing independent source.
- The chart: does it plot only verified numbers, and does the caption make the
  two-task contrast honest rather than a single sweep?
- Furniture: the two equations, the table, and the strong Verdict note — does
  each carry reasoning, and does the page still read as a continuous article?

## Known writer decisions to weigh (not automatically wrong)
- The chart mixes LeNet/MNIST (99%) with ResNet/CIFAR-100 (mid-80s), two tasks
  by design; the caption says so.
- "around 85%" in the Verdict rounds Stanton's 84.5–86% band; the body carries
  the exact figures with locators.

## Proof
The writer owns the proof. If prose changes alter counts, keep nb-meta honest
and have the writer rerun:
export PATH="/root/.local/bin:$PATH"
./nb check .nb-work/paper-of-the-day/knowledge-distillation/library/paper-of-the-day/knowledge-distillation.html --series paper-of-the-day --repo . --library ../library

## Return
`DONE editor <editorial-review-path>` when no redraft is required, or a
`REQUEST researcher/writer/orchestrator <one-sentence need>`.
