# Voice guide: Kernels

## How this piece should sound

Write as a working kernel engineer teaching a peer. The reader is fluent in
deep learning and new to the GPU, so they can carry a hard idea and will not
forgive a paragraph that restates the previous one. Explain the machine. Never
explain the reader's inexperience.

The four writers below have one thing in common worth taking. Each of them
sounds like a person who has actually run the thing, and it shows in small
places: Boehm calling his own result "pretty bad", He interrupting his own
diagram to say the arrangement is stupid, Upadhyay saying "if you like numbers,
let's talk about numbers" before producing them, Rush warning that an error is
probably because you did something fancy. None of that is decoration around the
technical content. It is what makes the technical content believable.

Prefer the concrete noun to the category. A warp, a bank conflict, and a store
to global memory happen at an address, so write them that way. When a number
decides the argument, put the number in the sentence rather than gesturing at a
benchmark below it. State what the hardware does before stating what the code
should do.

The subject's own vocabulary belongs in the prose, not translated out of it.
Swizzling, occupancy, and warpspace are how the work is discussed by the people
who do it, and a lesson that avoids them to stay accessible ends up sounding
like it was written from a distance.

## Simon Boehm, "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog"

```text
Source: https://siboehm.com/articles/22/CUDA-MMM

"Pretty bad, considering that the A6000 is advertised as being able to achieve
almost 30 TFLOPs. Just for comparison, 300 GFLOPs is also roughly the
performance achieved by the optimized BLAS library on the 2015 Haswell CPU that
I used in my earlier post on CPU matmul."
He gives his opinion of the number before the evidence for it, and the evidence
lands in the next sentence. "Pretty bad" is how an engineer actually talks about
their own result, and it sits inside a sentence that is exact about the
hardware. Casual about the verdict and precise about the machine in the same
breath is what makes this read as a person at a desk.

"I like to think of the three dimensions x,y,z of threadId as being
"column-major", due to the first dimension x being the one that's continuous in
"warpspace". I don't know if others use that term, but it makes the concept
more clear to me."
He offers a private mental model and admits it may be his alone. The reader gets
the idea and its standing at once, and nothing is dressed up as established
usage. A writer who says where a framing came from is easier to trust on the
things they then state flatly.

"It didn't increase performance, presumably because L2 hit rate is already
fairly high at 80%, so I ended up removing the swizzling code. The commit is
here if anyone is interested."
An optimization that failed, the cause he suspects, and a shrug. "If anyone is
interested" is the kind of aside that survives only because nobody edited it
out. Keeping the failed attempt tells the reader what the search actually
looked like.
```

## Horace He, "Making Deep Learning go Brrrr From First Principles"

```text
Source: https://horace.io/brrr_intro.html

"Hey! This is a very stupid arrangement. Why are we sending the same data to
global memory and then back to the compute units, over and over? We should just
keep the data at the factory, perform all of our compute, and then send it
back!"
He interrupts his own explanation to react to it. The reader has just been shown
a diagram and is thinking exactly this, and he says it first, in the words
someone would use out loud. The exclamation marks are doing real work here: the
insight arrives as a reaction rather than as a result.

"On the other hand, if you're spending all of your time performing big chonky
matmuls (i.e. a compute-bound regime), then rewriting your model logic into C++
to reduce overhead won't help."
"Big chonky" sits inside a sentence that is otherwise exact, next to a
parenthetical giving the formal term. He never picks between sounding like a
person and being correct, and the precision around the joke is what lets the
joke pass.

"So, if you want to keep your GPUs going brrrr, let's discuss the three
components your system might be spending time on - compute, memory bandwidth,
and overhead."
The piece is named after a noise, and here the noise does the transition work
that a section heading would usually do. It tells the reader the writer is
enjoying this, which buys patience for the three components that follow.
```

## Abhinav Upadhyay, "What Every Developer Should Know About GPU Computing"

```text
Source: https://blog.codingconfessions.com/p/gpu-computing

"If you like numbers, let's talk about numbers. The performance of hardware for
numerical computations is measured in terms of how many floating point
operations it can do per second (FLOPS)."
He announces the turn toward hard figures instead of sliding into it, and he
does it in a friendly voice. The reader gets a moment to decide how closely to
read, which is a small courtesy most technical writing skips.

"CPUs dedicate a significant amount of chip area towards features which will
reduce instruction latency, such as large caches, less ALUs and more control
units. In contrast, GPUs use a large number of ALUs to maximize their
computation power and throughput. They use a very small amount of the chip area
for caches and control units, the things which reduce the latency for CPUs."
Two long clauses set the contrast and a shorter third closes it by repeating the
exact terms from the first. Nothing is renamed on its second appearance, so the
reader tracks one comparison rather than two.

"So, why can't we always reach 100% occupancy? The SM has a fixed set of
execution resources, including registers, shared memory, thread block slots, and
thread slots."
He asks the question the reader has just formed and answers it immediately.
Putting it in the reader's voice, with "we", makes the constraint feel
discovered rather than announced.
```

## Sasha Rush, "GPU Puzzles"

```text
Source: https://github.com/srush/GPU-Puzzles

"It is hard to gain intuition working through abstractions. This notebook is an
attempt to teach beginner GPU programming in a completely interactive fashion.
Instead of providing text with concepts, it throws you right into coding and
building GPU kernels."
He states the pedagogical bet plainly and takes responsibility for it. "An
attempt" is an unusual word to use about your own teaching material, and it sets
up a reader who is willing to be thrown in because the writer has been honest
about what he is doing.

"This code looks like Python but it is really CUDA! You cannot use standard
python tools like list comprehension"
A warning written the moment before the reader would have hit the wall, in the
place they will actually be looking. He knows exactly which habit is about to
fail and stops it on the spot, instead of filing it in a general note about how
the two languages differ.

"If you get an error it is probably because you did something fancy :)."
The smiley is doing a lot of work. He tells the reader their error is expected
and slightly their own fault, and he is warm about it, so the puzzles read as an
invitation instead of a test.
```
