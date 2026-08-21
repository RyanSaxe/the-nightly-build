# Voice guide: paper-of-the-day/flash-attention

## Sound
Technical writing in the register of a careful systems reviewer. Plain sentences,
the structure doing the persuading. The math is set with the equation furniture
and read straight through, not narrated around.

## Sentence discipline
- Name the quantity once and keep it. N is sequence length, d head dimension, M
  the SRAM size, HBM and SRAM the two memories, all the way through.
- Keep three numbers distinct and never let one stand in for another: arithmetic
  (FLOPs), memory traffic (HBM reads and writes), and wall-clock time. The whole
  argument is that they come apart.
- A figure arrives with its comparison. "4.4 GB" means nothing until it sits next
  to standard attention's 40.3 GB at the same problem size.

## Opening and closings
- Open on the memory-IO bottleneck itself: the GPU finishes the multiplies and
  then waits on memory. Do not open on a baseline to overturn ("attention was
  slow; FlashAttention made it fast").
- No section closes on a line built to sound like a finding. When a paragraph has
  said its thing, it stops.
- The last section lands an earned verdict: what FlashAttention settled (exact
  attention, far less HBM traffic, real speedups) and what it did not (asymptotic
  compute, and a win that depends on the SRAM/HBM gap and the sequence length).
  One Verdict note carries it.

## Forbidden moves for this piece
- No "got X right and Y wrong" dek; not the phrase "the record after it."
- No holds-up-grid-plus-verdict close; a single Verdict note only.
- No semicolon-contrast heading and no "what the experiments actually settle"
  wh-heading. Headings are argument steps in the paper's own nouns.
- No "no later work overturns" reassurance. State plainly what FlashAttention-2
  partitioned better and what stays bound by the hardware.

## Terms to define on first use
HBM, SRAM, IO-aware, tiling, materializing the attention matrix, the online
(streaming) softmax, the running max and running normalizer, recomputation.
</content>
