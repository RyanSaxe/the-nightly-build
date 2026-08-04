# Voice guide: Kernels

Write as a working kernel engineer teaching a colleague who is fluent in deep
learning and new to the GPU. The reader is competent and impatient: they will
follow a hard idea, and they will close the tab on a paragraph that restates
the previous one. Explain the machine, never the reader's inexperience.

Prefer the concrete noun to the category. A warp, a bank conflict, and a store
to global memory are things that happen at an address; write them that way.
When a number decides the argument, put the number in the sentence rather than
gesturing at the benchmark below it.

Keep the sentence that carries the mechanism short. Long sentences are for
consequences, once the mechanism is already standing.

## Licenses

```text
form: the second-person walkthrough
move: the exemplars switch to "you" only at the moment the reader would run
      something, then drop it again once the result is on the page
bar:  the sentence must describe an action the reader can actually take with
      the code as printed

form: the measured aside
move: a one-clause interruption naming what the hardware is doing while the
      code runs, placed immediately after the line responsible
bar:  it must name a specific hardware behavior, not a vague cost

form: the corrected expectation
move: state the intuition a competent reader arrives with, then show the
      measurement that breaks it
bar:  the stated intuition must be one a reader could defend, never a
      strawman, and the correction must cite its number

form: the running example callback
move: return to the course's standing example to show what the new lesson
      changes about it
bar:  it must state what is different now, not merely that the example recurs
```

## Kevin Hou, "What Every Programmer Should Know About GPU Memory"

```text
Source: https://example.com/gpu-memory
Craft:
- cadence: short mechanism sentence, then a longer consequence sentence
- argument: builds from one measured anomaly outward to the general rule
- evidence: every claim about speed carries a timing on named hardware
- stance: confident about the machine, agnostic about the reader's setup
- notice: notices where the abstraction stops predicting the measurement
- diction: hardware nouns, almost no adjectives
- reader: assumes competence, never assumes prior CUDA
- close: ends sections on the open question the next section answers, so the
  piece pulls rather than pushes
```

## Sasha Rush, "GPU Puzzles"

```text
Source: https://example.com/gpu-puzzles
Craft:
- cadence: nearly all short declaratives; the code carries the length
- argument: each step is a solvable problem, and the prose only frames it
- evidence: the runnable cell is the evidence
- stance: playful about the puzzle, exacting about correctness
- notice: notices the exact index where a naive answer goes wrong
- diction: plain, no jargon left undefined on first use
- reader: treats the reader as a participant, not an audience
- restraint: refuses to explain the answer before the reader has had a chance
  to be wrong
```

## Lilian Weng, "The Transformer Family"

```text
Source: https://example.com/transformer-family
Craft:
- cadence: even, patient, paragraph-length units
- argument: comparative; each variant is defined by what it changes
- evidence: cites the originating paper for every claim of novelty
- stance: neutral surveyor, explicit about what is unsettled
- notice: notices when two papers name the same idea differently
- diction: precise technical terms, defined once and reused exactly
- reader: assumes the reader will return to the piece as a reference
- notation: keeps one notation across sources that disagree, so the
  comparison is real rather than apparent
```
