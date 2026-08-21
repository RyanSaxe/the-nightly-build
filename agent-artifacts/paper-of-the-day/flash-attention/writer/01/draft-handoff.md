# Draft handoff: paper-of-the-day/flash-attention

## What the draft does
Reconstructs FlashAttention as a memory-systems argument, then weighs it. Six
sections: the memory-IO bottleneck (orientation), tiling that avoids
materializing the N x N matrix (tiling), the online softmax that makes the
block-wise result exact (online-softmax), the IO-cost theorem and the
more-FLOPs-yet-faster table plus backward recomputation (io-cost), and the
after-record of FlashAttention-2/-3, adoption, and the exact-vs-approximate
placement (after). The verdict lands in one Verdict note.

## Furniture and why each is there
- Abstract card: verbatim abstract, paper link. Chrome.
- Fig. 1 (asset-1.png, the paper's Figure 1): memory-hierarchy triangle, the
  tiling loop, and the GPT-2 runtime breakdown. Settles that attention is
  memory-bound and that tiling avoids storing the N x N matrix. In the tiling
  section.
- Fig. 2 (asset-2.png, the paper's Figure 2 table): GFLOPs, HBM R/W, Runtime for
  Standard vs FlashAttention. Settles the thesis in three numbers — more
  arithmetic, ~9x less HBM traffic, ~5.7x faster. In the io-cost section.
- Display equation: standard attention S = QK^T, P = softmax(S), O = PV.
- Display equation: the running max/normalizer update.
- Annotated equation (the one): the online-softmax output-accumulator rescaling,
  three colored terms (renormalize; rescaled old accumulator; new block).
- Display equation: the IO-cost comparison Theta(Nd+N^2) -> Theta(N^2 d^2 / M).
- One strong Verdict note.

## Pattern-breaks honored
- Opens on the memory-IO bottleneck (GPU waits on memory), not a baseline to
  overturn.
- No "got X right/Y wrong" dek; no "the record after it."
- Single Verdict note; no holds-up grid.
- Argument-step headings in the paper's nouns; no semicolon-contrast, no
  wh-clause heading.
- States plainly what FlashAttention-2 partitioned better and what stays
  hardware-bound; no "no later work overturns" line.

## Proof state
PUBLISHABLE, 0 blocks. Two residual W-SENTENCE-DENSITY warnings both fall on the
verbatim abstract (its parenthetical capabilities sentence and its speedup
sentence), which the template requires reproduced verbatim and which cannot be
split without misquoting. Both figure assets validate; all eight source URLs
resolve; citations are numbered in order of first appearance.

## Numbers to keep honest
GFLOPs 66.6 -> 75.2 (more work); HBM 40.3 -> 4.4 GB (~9x); runtime 41.7 -> 7.3 ms
(~5.7x); SRAM 19 TB/s vs HBM 1.5 TB/s (~13x). All from Figure 1 and Figure 2 of
the paper. FA-2 ~2x and 50-73% of A100 peak; FA-3 ~75% H100 util, ~1.2 PFLOPs/s
FP8. The algorithm is exact: compute stays quadratic, memory is linear.
</content>
