# Voice guide: Kernels

## How this piece should sound

Write as a working kernel engineer teaching a peer. The reader is fluent in
deep learning and new to the GPU, so they can carry a hard idea and will not
forgive a paragraph that restates the previous one. Explain the machine. Never
explain the reader's inexperience.

Every writer below sounds like someone who has actually run the thing. That is
the quality to take from them, and it shows up in small places rather than
large ones: Boehm saying plainly that he cannot explain why one autotuned
parameter set wins, He calling a matmul "big chonky" in a sentence that is
otherwise exact, Rush handing over a puzzle and then refusing to rescue the
reader from it. None of that is decoration. Each is a moment where the writer
tells the truth about their own position, and a lesson without any such moment
reads like it was assembled rather than written.

Prefer the concrete noun to the category. A warp, a bank conflict, and a store
to global memory happen at an address, so write them that way. When a number
decides the argument, put the number in the sentence rather than gesturing at a
benchmark below it. State what the hardware does before stating what the code
should do.

Be willing to be surprised on the page. Boehm records optimizations that did
not work and what he suspects went wrong; He treats the wrong intuition as the
thing most worth explaining rather than as an error to correct. A lesson that
only reports what succeeded has hidden the part the reader learns from.

## Simon Boehm, "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog"

```text
Source: https://siboehm.com/articles/22/CUDA-MMM
- sound: "Pretty bad, considering that the A6000 is advertised as being able
  to achieve almost 30 TFLOPs. Just for comparison, 300 GFLOPs is also roughly
  the performance achieved by the optimized BLAS library on the 2015 Haswell
  CPU that I used in my earlier post on CPU matmul." The verdict lands in a
  fragment and the next sentence pays for it with a comparison the reader can
  check, so the judgment arrives before the evidence and never floats
- words: "Pretty bad" where a paper would write "suboptimal"; GPU literacy
  assumed, every new term anchored where it first does work, asides pushed into
  sidenotes so the through-line survives
- stance: a practitioner working in the open who names what he could not find,
  could not explain, or was surprised by
- attention: the artifacts others drop, including wasted blocks when dimensions
  do not divide evenly, and optimizations that produced no gain
- reader: first person plural, joint work rather than instruction, with
  imperatives confined to headings
- the human part: he publishes his failures. He records a swizzling attempt
  that bought nothing and attributes it to an already-high L2 hit rate, and he
  marks the place where his understanding stops instead of writing around it.
  A machine would have reported the wins and left a clean, useless account.
```

## Horace He, "Making Deep Learning go Brrrr From First Principles"

```text
Source: https://horace.io/brrr_intro.html
- sound: "For example, if you're spending all of your time doing memory
  transfers (i.e. you are in an memory-bandwidth bound regime), then increasing
  the FLOPS of your GPU won't help. On the other hand, if you're spending all
  of your time performing big chonky matmuls (i.e. a compute-bound regime),
  then rewriting your model logic into C++ to reduce overhead won't help." Two
  sentences of identical build, each ending on the same flat refusal, so the
  reader hears the symmetry of the two regimes before it is named
- words: "big chonky matmuls" sitting inside a precise technical claim; jargon
  translated into plain cost language the same sentence it appears
- stance: impatient with guessing and generous toward the guesser, treating
  the wrong intuition as the thing worth explaining
- attention: the second-order fact, that fusing changes almost nothing about
  the arithmetic and almost everything about the traffic
- reader: addressed as a collaborator with a real problem, invited into a
  shared "let's" rather than instructed
- the human part: the willingness to sound unserious in a sentence that is not.
  "Big chonky" is the word a person uses talking to a colleague, and its
  presence is what makes the surrounding precision read as confidence rather
  than caution.
```

## Abhinav Upadhyay, "What Every Developer Should Know About GPU Computing"

```text
Source: https://blog.codingconfessions.com/p/gpu-computing
- sound: "CPUs dedicate a significant amount of chip area towards features
  which will reduce instruction latency, such as large caches, less ALUs and
  more control units. In contrast, GPUs use a large number of ALUs to maximize
  their computation power and throughput. They use a very small amount of the
  chip area for caches and control units, the things which reduce the latency
  for CPUs." Two long balanced clauses set the contrast and a shorter third
  sentence closes it by reusing the exact terms, never a synonym
- words: each term defined in the clause that introduces it, before it is ever
  used to carry an argument
- stance: assumes real competence in the reader and locates the gap precisely
  rather than starting from zero
- attention: asks why the architecture is shaped this way, so latency tolerance
  arrives as a design consequence rather than a specification
- reader: voices the reader's objection as a question and then answers it
- the human part: he keeps saying the plain thing twice rather than reaching
  for a synonym, which reads as someone who would rather be understood than
  admired.
```

## Sasha Rush, "GPU Puzzles"

```text
Source: https://github.com/srush/GPU-Puzzles
- sound: "Implement a kernel that adds 10 to each position of vector `a` and
  stores it in vector `out`. You have 1 thread per position." The task, then
  the single constraint that makes it solvable, and nothing else
- words: plain, short, and free of ceremony; the constraint carries the
  teaching
- stance: exacting about the constraint and light about everything else
- attention: the exact place a Python habit silently stops being valid on a
  device, with the warning placed there rather than generally
- reader: treated as a participant who is about to attempt something, not an
  audience being shown a result
- the human part: he refuses to help after the attempt. Scaffolding arrives
  before the puzzle and nothing arrives after it, which is a teacher choosing
  to let the reader be wrong. It costs him the chance to explain, and that is
  the point.
```
