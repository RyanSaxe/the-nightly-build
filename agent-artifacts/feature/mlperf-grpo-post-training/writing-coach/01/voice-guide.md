# Voice guide: feature/mlperf-grpo-post-training (01)

## How this piece should sound

The register is one engineer explaining a measurement to others who build the same kind of system. It is plain and exact, with no marketing temperature in either direction. The reader already knows what a rollout, a reward model and an accelerator are. What they do not have is a clear picture of what this benchmark's clock covers, and the piece exists to give them that picture. Like Austin et al. opening the roofline chapter, the piece can start from the concrete question a practitioner would ask about a number ("why this many minutes and not ten times more or less?"), then answer it by breaking the time into parts.

Each section sits under a figure, so the prose mostly tells the reader how to read the figure. Horace He and Dan Luu both do this. They say what the axis or column means, say what pattern would appear if a hypothesis were true, and then say whether it appears. Where the material allows it, read the GRPO loop drawing and the results comparison that way. Say which stage of the loop falls inside the timed region. Then say what a submission's minutes would look like if rollout generation, reward computation or the policy update dominated, and whether the table bears that out.

When a headline comparison is checked against what it holds constant, follow Luu's 1 ms display and Austin et al.'s "does not normalize to cost" note. Name the quantity the comparison leaves free, such as accelerator count, chip type or number of runs, in a single flat clause. Do not editorialize about it. Where the arithmetic is simple enough to show, like accelerators times minutes or a ratio between two submissions, show the actual computation inline as Luu does with his buffered frames, so the reader can redo it.

Use the rules document's own terms (timed region, quality target, pass@4, reference convergence points) and keep each one fixed once it is defined, the way He keeps "overhead" and "memory-bandwidth bound" fixed. He shows that a little informality ("big chonky matmuls") is fine in an explainer. The person on the page comes through in what the writer chose to measure and check, not in jokes, and five minutes leaves room for one light touch at most. Do not reteach GRPO. The audience knows it, and the brief allows one sentence.

## Horace He, "Making Deep Learning Go Brrrr From First Principles"

Source: https://horace.io/brrr_intro.html

> "For example, if you're spending all of your time doing memory transfers (i.e. you are in an memory-bandwidth bound regime), then increasing the FLOPS of your GPU won't help. On the other hand, if you're spending all of your time performing big chonky matmuls (i.e. a compute-bound regime), then rewriting your model logic into C++ to reduce overhead won't help."

Checked: https://horace.io/brrr_intro.html (raw HTML via curl, tags stripped), retrieved 2026-11-28
He defines each regime by an action that would be wasted inside it. That makes the categories useful the moment they appear. "Big chonky matmuls" sits next to exact terms, and that is the voice of a PyTorch engineer who is relaxed about the material.

> "So, how do you tell if you're in this regime? Well, since overhead generally doesn't scale with problem size (while compute and memory do), the easiest way to tell is to simply increase the size of your data. If that doesn't increase the runtime proportionally, you're overhead bound. For example, if you double your batch size but your runtime only increases by 10%, you're likely overhead bound."

Checked: https://horace.io/brrr_intro.html, retrieved 2026-11-28
He gives the reader a test they can run, along with the reason it works and a worked number. The question here is not rhetorical: the next sentence answers it with a procedure.

> "First, notice that the runtime doesn't increase noticeably at all until we're performing 64 multiplications. That means that up until that point, we're mostly memory-bandwidth bound - our compute is mostly sitting idle."

Checked: https://horace.io/brrr_intro.html, retrieved 2026-11-28
This is prose reading a log-log plot. He names one feature of the curve, gives its threshold, and states what it means about the hardware, in two sentences.

## Jacob Austin et al., "All About Rooflines" (How To Scale Your Model, Part 1)

Source: https://jax-ml.github.io/scaling-book/roofline/

> "Let’s start with an extremely simple question: why does an algorithm take 50ms instead of 50s or 5ms? What is actually happening within the model that takes substantial time and how long should we expect it to take?"

Checked: https://jax-ml.github.io/scaling-book/roofline/ (raw HTML via curl, tags stripped), retrieved 2026-11-28
The chapter opens on a measured time and asks where it comes from, with order-of-magnitude alternatives that make the question concrete. Authors who spend their time estimating step times show up in the choice of 50ms against 50s or 5ms.

> "That means doing 1e12 FLOPs on an H100 will take (roughly) 1e12 / 9.89e14 = 1.01ms and 1e12 / 9.1e14 = 1.1ms on a TPU v6e. Note that these chips are priced differently, and this comparison does not normalize to cost."

Checked: https://jax-ml.github.io/scaling-book/roofline/, retrieved 2026-11-28 (the second sentence is a sidenote attached inline to the first)
The authors write the division out and then state in one flat clause what the cross-vendor comparison leaves out. The caveat is specific and checkable, and the authors do not make a show of being careful.

> "Typically (but not always), computation within a single chip can be overlapped with communication within a chip and between chips. This means we can lower-bound training and inference time by using the maximum of computation and communication time. We can also upper-bound with their sum."

Checked: https://jax-ml.github.io/scaling-book/roofline/, retrieved 2026-11-28
They turn a wall-clock time into components and bounds, and they put the qualification ("but not always") in parentheses at the point where it applies. Three short sentences carry the whole idea.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "These are tests of the latency between a keypress and the display of a character in a terminal (see appendix for more details). The results are sorted from quickest to slowest."

Checked: https://danluu.com/input-lag/ (raw HTML via curl, tags stripped), retrieved 2026-11-28
Directly under the table, Luu states exactly what interval each number measures and how the rows are ordered. A reader knows what the benchmark's clock contains before reading any conclusion.

> "I have a display that advertises 1 ms switching on the box, but if we look at how long it takes for the display to actually show a character from when you can first see the trace of it on the screen until the character is solid, it can easily be 10 ms."

Checked: https://danluu.com/input-lag/, retrieved 2026-11-28
Luu sets an advertised figure beside the one he measured and defines the start and end points of his own measurement in the same sentence. The first person is there because he measured his own display.

> "At 24 Hz each frame takes 41.67 ms and at 165 Hz each frame takes 6.061 ms. ... But the difference is actually 90 ms, implying we have latency equivalent to (90 - 18) / (41.67 - 6.061) = 2 buffered frames."

Checked: https://danluu.com/input-lag/, retrieved 2026-11-28 (ellipsis omits the intervening expected-latency sentence)
He uses a gap between the expected and the observed result to infer a hidden component, and he shows the arithmetic so a reader can check it. The inference stops at what the numbers give.
