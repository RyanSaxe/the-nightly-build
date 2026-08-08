# Voice guide: Kernels

## How this piece should sound

Write as a working kernel engineer teaching a peer. The reader is fluent in
deep learning and new to the GPU, so they can carry a hard idea and will not
forgive a paragraph that restates the previous one. Explain the machine. Never
explain the reader's inexperience.

Every writer below sounds like someone who has actually run the thing, and it
shows in small places rather than large ones. Boehm stops to report an
optimization that bought him nothing. He calls a matmul "big chonky" in a
sentence that is otherwise exact. Rush hands over a puzzle and then refuses to
rescue the reader from it. A lesson with no moment like that reads as though it
was assembled from sources rather than written by someone.

Prefer the concrete noun to the category. A warp, a bank conflict, and a store
to global memory happen at an address, so write them that way. When a number
decides the argument, put the number in the sentence rather than gesturing at a
benchmark below it. State what the hardware does before stating what the code
should do.

Say what you think of a result before you justify it, then justify it
immediately. And report what did not work: the optimization that bought
nothing teaches more than the one that worked, and leaving it out is how a
lesson turns into an advertisement.

## Simon Boehm, "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog"

```text
Source: https://siboehm.com/articles/22/CUDA-MMM

sentences
"Pretty bad, considering that the A6000 is advertised as being able to achieve
almost 30 TFLOPs. Just for comparison, 300 GFLOPs is also roughly the
performance achieved by the optimized BLAS library on the 2015 Haswell CPU that
I used in my earlier post on CPU matmul."
He says what he thinks of the number before he justifies it, and the
justification arrives in the very next sentence. The reader is never asked to
take the verdict on trust and never made to wait for it either. Put the
judgment first when the evidence for it is one sentence away.

words
"Pretty bad, considering that the A6000 is advertised as being able to achieve
almost 30 TFLOPs."
He writes "pretty bad" where a paper would write "suboptimal", and he does it
about his own result. The technical terms stay exact and the judgments stay in
ordinary English.

judgment
"It didn't increase performance, presumably because L2 hit rate is already
fairly high at 80%, so I ended up removing the swizzling code."
He gives the cause he believes and marks it as a belief with one word,
"presumably", then acts on it anyway by deleting the code. Commit to the
explanation you actually hold and label the part you have not proved, rather
than hedging the whole sentence.

unmistakable
"I also want to report a negative results: For this kernel, I additionally
implemented an optimization called thread swizzling."
He announces in advance that he is about to describe something that failed.
Most write-ups report only what worked, and volunteering the dead end is what
makes the piece read as a log of real work rather than a result.
```

## Horace He, "Making Deep Learning go Brrrr From First Principles"

```text
Source: https://horace.io/brrr_intro.html

sentences
"For example, if you're spending all of your time doing memory transfers (i.e.
you are in an memory-bandwidth bound regime), then increasing the FLOPS of your
GPU won't help. On the other hand, if you're spending all of your time
performing big chonky matmuls (i.e. a compute-bound regime), then rewriting
your model logic into C++ to reduce overhead won't help."
Two sentences built identically, each ending on the same flat refusal. The
reader hears that the two regimes are symmetric before being told so. Build
parallel sentences when the ideas in them are genuinely parallel.

words
"big chonky matmuls (i.e. a compute-bound regime)"
The casual word and the exact term sit in the same breath. He never chooses
between being correct and sounding like a person talking, and the precision
around it is what lets the joke pass.

judgment
"increasing the FLOPS of your GPU won't help"
He tells the reader flatly that an expensive obvious fix will do nothing,
without hedging it into a maybe. Say the useless thing is useless when the
diagnosis supports it.

unmistakable
"big chonky matmuls"
Nobody writing a performance guide needs that phrase, and its presence changes
how the whole piece reads: a person who is relaxed about vocabulary and strict
about claims. The looseness buys the exactness elsewhere.
```

## Abhinav Upadhyay, "What Every Developer Should Know About GPU Computing"

```text
Source: https://blog.codingconfessions.com/p/gpu-computing

sentences
"CPUs dedicate a significant amount of chip area towards features which will
reduce instruction latency, such as large caches, less ALUs and more control
units. In contrast, GPUs use a large number of ALUs to maximize their
computation power and throughput. They use a very small amount of the chip area
for caches and control units, the things which reduce the latency for CPUs."
Two long clauses set the contrast and a shorter third closes it by repeating
the exact terms from the first. Nothing is renamed on its second appearance, so
the reader tracks one comparison instead of two.

words
"the things which reduce the latency for CPUs"
He restates a term he has already used rather than reaching for a synonym, and
uses the plainest available phrase for it. Repeat the word. Variety costs the
reader more than it gives.

judgment
"GPUs use a large number of ALUs to maximize their computation power and
throughput."
He states the design intent as fact rather than attributing it to unnamed
engineers. Where the architecture makes the reason obvious, say the reason.

unmistakable
He anchors every GPU claim to a CPU the reader already understands, all the way
through, rather than only in the opening.
The comparison is not an introduction he abandons once the real material
starts. Carrying one frame the whole way is what lets a reader new to the
subject hold the piece together.
```

## Sasha Rush, "GPU Puzzles"

```text
Source: https://github.com/srush/GPU-Puzzles

sentences
"Implement a \"kernel\" (GPU function) that adds 10 to each position of vector
`a` and stores it in vector `out`. You have 1 thread per position."
The task, then the single constraint that makes it solvable, and nothing else.
No preamble and no encouragement. Cut every sentence between the reader and
the thing they are about to attempt.

words
"You have 1 thread per position."
Plain, short, and free of ceremony. The constraint carries the teaching, so no
adjective is asked to help.

judgment
"You have 1 thread per position."
He decides exactly what the reader gets and does not soften it into a
suggestion. When a constraint is the lesson, state it as a fact about the
world.

unmistakable
He gives the reader a tip before the attempt and nothing at all after it.
The error loop is left to do the teaching, which means giving up the chance to
explain. That refusal is why the puzzles work and why they read as written by
a teacher rather than a documentation page.
```
