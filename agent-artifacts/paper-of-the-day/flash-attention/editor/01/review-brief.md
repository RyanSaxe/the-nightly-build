# Editor review brief: paper-of-the-day/flash-attention (01)

Inputs:
- `../../editorial-direction.md` — the governing standard, including the paper
  template identity (abstract card + paper link up front; the idea rebuilt in
  the piece's own words and weighed as a reviewer would).
- `../../commission.md` — what to rebuild (the memory-IO bottleneck, the online-
  softmax recurrence, the IO-cost argument, backward recomputation), the
  after-record to weigh (FlashAttention-2/-3, the exact-vs-approximate nuance,
  the hardware/IO-bound caveat), boundaries, and the recent patterns to break.
- `../../writer/01/brief.md` and `../../writer/01/draft-handoff.md`.
- `../../researcher/01/evidence.md` — the sourced record and the figure captures.
- The article: `.nb-work/paper-of-the-day/flash-attention/library/paper-of-the-day/flash-attention.html`.

Proof: `./nb check .nb-work/paper-of-the-day/flash-attention/library/paper-of-the-day/flash-attention.html --series paper-of-the-day --library /home/user/library-checkout`

## Known state
The correspondent's proof is `BLOCK: 0 / WARN: 2 / PUBLISHABLE`. Both warnings are
W-SENTENCE-DENSITY on the paper's abstract, which the template requires reproduced
verbatim; they cannot be split without misquoting. Confirm that is the only
source of the two warnings and do not "fix" them by altering the quoted abstract.

## Round focus (a reconstruction, so correctness is load-bearing)
Fresh-eyes read at high effort. Verify the technical reconstruction against the
evidence and the sources:
- The online-softmax recurrence (running max, running normalizer, output-
  accumulator rescaling) is stated correctly and the annotated equation's terms
  are defined where first used.
- The IO-cost claim (standard Θ(Nd+N²) vs FlashAttention Θ(N²d²/M)) and the ~9x
  memory-traffic / HBM reduction match Figure 2's numbers (HBM 40.3→4.4 GB,
  runtime 41.7→7.3 ms, GFLOPs rising) and the captions say what each figure
  settles.
- The framing that FlashAttention is EXACT (not on the approximate-attention
  frontier) and its benefit is hardware/IO-bound, and that FlashAttention-2
  improved GPU utilization v1 left on the table — check these are stated
  accurately, not overclaimed.

## Recent patterns to catch
Compare against recent paper-of-the-day pieces (`NB_LIBRARY=/home/user/library-checkout ./nb history --series paper-of-the-day`):
- Reject the "What holds up / Verdict" box mold, the "got X right/Y wrong"
  concession dek, semicolon-contrast or wh-clause headings, and the "no later
  work overturns" tic. Confirm the piece opens on the memory-IO bottleneck, not
  a baseline-before-twist lede.

Fix prose, structure, equations, and figure captions in place; route to the
writer only for a reconstruction error or missing evidence you cannot settle.
