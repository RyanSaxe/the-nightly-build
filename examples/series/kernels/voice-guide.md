# Voice guide: Kernels

Write as a working kernel engineer teaching a peer. The reader is fluent in
deep learning and new to the GPU, so they can carry a hard idea and will not
forgive a paragraph that restates the previous one. Explain the machine. Never
explain the reader's inexperience.

Carry the mechanism in a short declarative and the consequence in the longer
sentence that follows it. A one-sentence paragraph is a pivot between ideas,
not emphasis, so spend them where the lesson turns.

Prefer the concrete noun to the category. A warp, a bank conflict, and a store
to global memory happen at an address; write them that way. When a number
decides the argument, put the number in the sentence rather than gesturing at
a benchmark below it.

State what the hardware does before stating what the code should do. Every
exemplar below earns the reader's trust the same way: it explains a behavior,
then shows the measurement that behavior predicts.

## Licenses

```text
form: the corrected intuition
move: He states the belief a competent reader arrives with, then shows the
      measurement that breaks it. Two chained cosines cost nearly what one
      costs, which is why activation functions price alike however much
      arithmetic they appear to do.
bar:  the stated belief must be one a competent reader would defend out loud,
      never a strawman, and the correction must carry its measurement

form: the sustained physical analogy
move: He runs one factory-and-warehouse picture across several diagrams and
      then puts it under stress, asking what doubling the factory buys when
      the road to it did not widen.
bar:  the analogy must return later under changed conditions and pay off
      differently; a simile used once is decoration and gets cut

form: the reported negative result
move: Boehm records optimizations that did not work and why he thinks so,
      including a swizzling attempt he attributes to an already-high L2 hit
      rate.
bar:  it must name what was tried, the measurement that settled it, and the
      suspected reason; a failure with no number is an anecdote

form: the admitted limit
move: Boehm marks where his understanding stops rather than papering over it,
      saying plainly that he cannot explain why one autotuned parameter set
      wins.
bar:  it must bound a claim the lesson actually made; it may never excuse a
      claim the lesson owed the reader and skipped

form: the spec-to-consequence calculation
move: Both He and Boehm start from published bandwidth and throughput numbers
      and arrive at what the hardware should therefore take, before measuring
      what it does take.
bar:  the calculation must end at a number the lesson then checks against a
      real measurement, and the gap between them must be addressed

form: the withheld answer
move: Rush gives the reader a tip before the attempt and nothing after it,
      leaving the error loop to teach. The reader gets to be wrong first.
bar:  the exercise must be answerable from the lesson alone, and no later
      paragraph may resolve it
```

## Simon Boehm, "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog"

```text
Source: https://siboehm.com/articles/22/CUDA-MMM
Craft:
- cadence: a blunt verdict on a result, then a long sentence explaining the
  access pattern that produced it; single-sentence paragraphs carry the turns
- argument: each kernel repeats one shape, motivation to visualization to code
  to measurement to analysis, so complexity rises without the frame moving
- evidence: timings on named hardware sit inside the sentence making the
  claim, and napkin math predicts a number before the profiler reports one
- stance: a practitioner working in the open who names what he could not find,
  could not explain, or was surprised by
- notice: the artifacts others drop, including wasted blocks when dimensions
  do not divide evenly, and optimizations that produced no gain
- diction: GPU literacy assumed, every new term anchored where it first does
  work, asides pushed into sidenotes so the through-line survives
- reader: first person plural, joint work rather than instruction, with
  imperatives confined to headings
- ordering: the diagram always precedes the code, and the profiler output
  always follows it, so the reader never meets syntax before intent
```

## Horace He, "Making Deep Learning go Brrrr From First Principles"

```text
Source: https://horace.io/brrr_intro.html
Craft:
- cadence: a short hook sentence sets the stakes, then a longer sentence does
  the explaining; the pattern repeats at the top of each section
- argument: diagnosis before treatment. The piece refuses to recommend
  anything until the reader can say which of three regimes they are in
- evidence: published bandwidth and throughput figures are converted into an
  operational statement about how many numbers move per unit of arithmetic
- stance: impatient with guessing and generous toward the guesser, treating
  the wrong intuition as the thing worth explaining
- notice: the second-order fact, that fusing changes almost nothing about the
  arithmetic and almost everything about the traffic
- diction: informal register carrying exact claims; jargon is translated into
  plain cost language the same sentence it appears
- reader: addressed as a collaborator with a real problem, invited into a
  shared "let's" rather than instructed
- pressure: the central analogy is reused under changed conditions instead of
  being stated once, so the reader can reason with it rather than admire it
```

## Abhinav Upadhyay, "What Every Developer Should Know About GPU Computing"

```text
Source: https://blog.codingconfessions.com/p/gpu-computing
Craft:
- cadence: balanced clauses for architectural comparison, then a short
  sentence to release the tension before the next concept
- argument: known territory first. CPU behavior anchors every GPU claim, and
  sections close by naming the concept the next one needs
- evidence: throughput figures are placed beside a CPU's so the magnitude is
  legible instead of merely large
- stance: assumes real competence in the reader and locates the gap precisely
  rather than starting from zero
- notice: asks why the architecture is shaped this way, so latency tolerance
  arrives as a design consequence rather than a specification
- diction: each term is defined in the clause that introduces it, before it is
  ever used to carry an argument
- reader: voices the reader's objection as a question and then answers it
- recap: condenses a section into what it now makes possible, never a summary
  of what was said
```

## Sasha Rush, "GPU Puzzles"

```text
Source: https://github.com/srush/GPU-Puzzles
Craft:
- cadence: one imperative sentence per task, no preamble
- argument: the problem is the explanation. Concepts are never taught before
  the reader has failed at needing them
- evidence: a runnable cell and a visual debugger; correctness is shown rather
  than asserted
- stance: exacting about the constraint and light about everything else
- notice: the exact place a Python habit silently stops being valid on a
  device, and warns there rather than generally
- diction: plain, short, and free of ceremony; the constraint carries the
  teaching
- reader: treated as a participant who is about to attempt something, not an
  audience being shown a result
- restraint: scaffolding arrives before the attempt and nothing arrives after
  it, so the error loop stays the teacher
```
