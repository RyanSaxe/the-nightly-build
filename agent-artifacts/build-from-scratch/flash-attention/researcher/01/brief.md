# researcher brief: build-from-scratch/flash-attention (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader
- commission.md — the subject, the reconstruction the writer will run, and the
  four primary sources to begin from

Output: researcher/01/evidence.md

The article's argument rests on the online-softmax recurrence and the writer's
own runnable experiment, so the evidence that matters most is the exact math and
the primary claims about the shipped kernel. Read the four primary sources named
in the commission and verify the recurrence arithmetic (running max, running
denominator, rescaling correction) against Milakov and Gimelshein, and the
tiling and backward-recomputation claims against the FlashAttention paper. Set
the recurrence precisely enough that the writer can implement it and the editor
can recompute it. Record the honest limit: a pure-Python prototype reproduces
the exact output and the memory scaling but not the wall-clock speedup, which is
the kernel's IO behavior. Note in Numbers any concrete figures the piece could
anchor to (for example the memory-complexity claims the papers state).
