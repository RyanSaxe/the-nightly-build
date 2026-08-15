# Evidence record: build-from-scratch/flash-attention (researcher 01)

The evidence supports every mathematical claim the commission needs: the
online-softmax recurrence (running max, running denominator, rescaling
correction) is confirmed character-for-character against Milakov and
Gimelshein's own algorithm box and its inductive proof, and the block-tiled
attention form of that same recurrence is confirmed character-for-character
against FlashAttention's Algorithm 1 and Theorem 1 and independently re-derived
in FlashAttention-2's own worked two-block example. FlashAttention-2 states
outright that it is citing Milakov and Gimelshein for the online-softmax
technique itself and Rabe and Staats for applying it to attention, which is
direct primary confirmation of the lineage the commission asserts. The backward
pass recomputation-from-statistics claim and the O(N) additional-memory /
Θ(N²d²M⁻¹) HBM-access claims are confirmed against FlashAttention's own
Theorem 1, Theorem 2, and Appendix B.5. All four source URLs resolve to the
papers' own arXiv abstract pages. Evidence is thin in one place only: none of
the four papers discuss the difference between exact equivalence in real-number
arithmetic (what every equivalence theorem below actually proves) and bit-exact
equivalence under floating-point summation order, which matters because the
commission's own experiment plan checks output equality "to floating-point
tolerance," not bit-exactly. That gap is mine to flag, not sourced, and is
recorded under Contradictions so the writer does not overstate what "exact"
means at the float64/float32 level. No primary source states a wall-clock
number for a pure-Python or NumPy prototype; the honest-limit framing in the
commission (memory and output match, wall-clock speedup does not translate) is
not contradicted by anything found, but it is also not itself a citable
figure — it follows from what tiling and recomputation are *for* (reducing HBM
traffic on a GPU), which a Python loop over NumPy arrays does not do.

## Sources

```text
URL:         https://arxiv.org/abs/1805.02867
Kind:        primary — Milakov and Gimelshein are the authors and sole owners
             of the online-normalizer-calculation algorithm and its proof;
             both list NVIDIA as their affiliation on the paper itself.
Establishes: The single-pass online softmax recurrence (running max, running
             denominator, rescaling correction) and its inductive equivalence
             proof against the two-pass "safe softmax." Also establishes the
             general two-accumulator block-merge operator that the FlashAttention
             block update is a vector-valued generalization of.
Paraphrase:  Standard ("unsafe") softmax computes d = sum(exp(x_i)) directly,
             which the paper says overflows or underflows in the exponent on
             real hardware. The fix subtracts the running max before
             exponentiating. Algorithm 2 (Safe Softmax) does this in three
             passes: one to find the max, one to accumulate the shifted-exp
             sum, one to divide. Algorithm 3 (Online Softmax) fuses the first
             two passes into one, carrying a running max m and running
             denominator d that are jointly updated per element, then still
             needs one final pass to produce outputs y_i. Section 3.1 extends
             this to an associative, commutative binary merge operator on
             (m, d) pairs so that partial results from different chunks of the
             input can be combined in any order or in parallel — this is
             exactly the operation a block-tiled attention implementation uses
             to fold in one new K/V block's partial statistics.
Locators:    Abstract; Section 2 "Original softmax" (the overflow motivation);
             Section 3 "Online normalizer calculation," Algorithm 2 and
             Algorithm 3 (the exact update lines, reproduced under Numbers /
             equations below); Section 3.1 "Parallel online normalizer
             calculation," Equations 3-4 (the merge operator); Theorem 1 and
             its inductive proof, immediately after Algorithm 3.
Quote:       Algorithm 3, lines 4-5: "m_j ← max(m_{j-1}, x_j)" and
             "d_j ← d_{j-1} × e^{m_{j-1}-m_j} + e^{x_j-m_j}". Theorem 1: "The
             lines 1-6 of the algorithm 3 compute m_V = max_{k=1}^{V} x_k and
             d_V = sum_{j=1}^{V} e^{x_j - m_V}." Equation 4 (merge operator):
             "[m_i; d_i] ⊕ [m_j; d_j] = [max(m_i,m_j); d_i·e^{m_i-max(m_i,m_j)}
             + d_j·e^{m_j-max(m_i,m_j)}]." Text following: "The operation ⊕ is
             associative, which enables parallel evaluation... It is also
             commutative... We omit the proofs for these two statements for
             brevity." Section 2: "on real hardware, where the range of
             numbers represented is limited, [unsafe accumulation] can
             overflow or underflow due to the exponent."
```

```text
URL:         https://arxiv.org/abs/2205.14135
Kind:        primary — Dao, Fu, Ermon, Rudra, and Ré are the authors and
             owners of the FlashAttention algorithm, its exactness theorem,
             and its IO-complexity theorem. Affiliations on the paper: Dao and
             Fu at Stanford CS, Ermon at Stanford CS, Rudra at University at
             Buffalo, Ré at Stanford CS.
Establishes: The block-tiled forward algorithm (Algorithm 1) that generalizes
             the Milakov/Gimelshein recurrence to matrix-valued blocks with an
             attached output accumulator; the theorem that this algorithm's
             output is bit-for-bit the same real-valued function as naive
             attention (Theorem 1); the IO-complexity argument for why tiling
             matters on real hardware (Theorem 2); and the backward-pass
             recomputation-from-saved-statistics design.
Paraphrase:  Algorithm 0 states the naive baseline directly: compute S = QK^T
             and write it to HBM, read S back to compute P = softmax(S) and
             write P to HBM, then read P and V to compute O = PV. This is the
             O(N^2)-memory-traffic baseline the commission's naive
             implementation stands in for (in HBM-access terms; the commission's
             naive prototype is memory-footprint-quadratic in NumPy, which is
             the in-process analogue of this HBM-traffic argument, not the
             identical claim — the paper's O(N^2) is about HBM reads/writes of
             a GPU kernel, not RAM footprint of a Python array, though a
             literal S = Q @ K.T array in NumPy is also O(N^2) in RAM).
             Algorithm 1 tiles Q into row blocks and K, V into column blocks,
             then for each (row block i, column block j) computes a local
             score block S_ij, its local row-max and row-sum, and folds those
             into running per-row statistics m_i (max) and ℓ_i (denominator)
             using exactly the Milakov/Gimelshein merge structure, extended to
             also rescale and re-accumulate the output block O_i. Theorem 1
             proves the algorithm returns the exact softmax(QK^T)V. The paper
             frames its actual product as reduced HBM traffic, not reduced
             FLOPs: Theorem 2 states FlashAttention needs asymptotically fewer
             HBM accesses than standard attention for typical head dimensions,
             which is what converts into wall-clock speedup on a GPU — a
             property a pure-Python/NumPy prototype cannot exhibit, because it
             has no HBM/SRAM hierarchy to be IO-aware about. For the backward
             pass, the paper explicitly chooses to recompute S and P on-chip
             from the saved output and the saved (m, ℓ) statistics rather than
             store the full attention matrix, framed as a form of selective
             gradient checkpointing.
Locators:    Abstract (naive-vs-Flash framing, speedup numbers); Section 2.2
             "Standard Attention Implementation," Algorithm 0; Section 3.1 "An
             Efficient Attention Algorithm With Tiling and Recomputation,"
             Algorithm 1 (lines 1-16), Theorem 1 immediately after; Section 3.2
             "Analysis: IO Complexity of FlashAttention," Theorem 2; Section
             3.1 body text (the recomputation sentence, quoted below);
             Appendix B.5 "Comparison with Rabe and Staats 2021" (the
             difference in what each paper recomputes in the backward pass).
Quote:       Algorithm 1, line 11: "m_i^new = max(m_i, m̃_ij) ∈ R^{B_r},
             ℓ_i^new = e^{m_i - m_i^new}ℓ_i + e^{m̃_ij - m_i^new}ℓ̃_ij ∈
             R^{B_r}." Line 12: "O_i ← diag(ℓ_i^new)^{-1}(diag(ℓ_i)
             e^{m_i-m_i^new} O_i + e^{m̃_ij-m_i^new} P̃_ij V_j) [written] to
             HBM." Theorem 1: "Algorithm 1 returns O = softmax(QK^T)V with
             O(N^2 d) FLOPs and requires O(N) additional memory beyond inputs
             and output." Theorem 2: "Standard attention (Algorithm 0)
             requires Θ(Nd+N^2) HBM accesses, while FlashAttention (Algorithm
             1) requires Θ(N^2 d^2 M^{-1}) HBM accesses." Section 3.1: "by
             storing the output O and the softmax normalization statistics
             (m, ℓ), we can recompute the attention matrix S and P easily in
             the backward pass from blocks of Q, K, V in SRAM." Appendix B.5:
             "FlashAttention instead simplifies the backward pass
             analytically... It only recomputes the attention matrix and does
             not recompute the temporary output of each block." Citation
             check: the sentence "we decompose the large softmax with scaling
             [60, 51, 66]" resolves in the bibliography to reference 60 =
             Milakov and Gimelshein (2018), 51 = Kitaev et al., Reformer
             (2020), 66 = Rabe and Staats (2021) — FlashAttention's own
             citation of the online-softmax source.
```

```text
URL:         https://arxiv.org/abs/2112.05682
Kind:        primary — Rabe and Staats are the authors and owners of the O(1)
             / O(log n) memory attention algorithm; both list Google Research
             as affiliation on the paper.
Establishes: An independent, query-side derivation of the same running-max /
             rescale recurrence, applied to attention specifically (rather
             than softmax in the abstract), plus the O(1)/O(log n)/O(√n)
             memory-complexity claims the commission wants as anchoring
             figures, and the explicit statement that the result is exact, not
             an approximation.
Paraphrase:  For one query and a stream of key/value pairs, the algorithm
             keeps a running unnormalized output accumulator v*, a running
             denominator s*, and a running max m*, updating all three per
             key/value pair with the identical rescale-then-add structure as
             Milakov/Gimelshein's d update, but applied to a vector (v*)
             instead of a scalar. This is finished with a single division
             v*/s* — an O(1)-memory algorithm with respect to sequence length
             for one query (the paper does not count the O(n) cost of writing
             one output per query toward this complexity — it states this
             explicitly). Extending to all queries at once, done sequentially,
             costs one extra index into the query list, which the paper says
             gives the O(log n) figure for full self-attention. Their actual
             runnable JAX/TPU implementation (Section 4) uses fixed chunk
             sizes for tractability and lands at O(√n) memory, not O(1) or
             O(log n) — the headline complexity figures describe the abstract
             algorithm, not the shipped implementation. The paper states this
             is not an approximation: it computes the same function as
             standard attention.
Locators:    Abstract; Section 1 Introduction (the "very simple algorithm...
             not an approximation" sentence); Section 2 "Algorithm" (the O(1)
             / O(log n) derivation, and the sentence about not counting output
             cost); Section 3 "Numerical Stability" (the running-max recurrence
             itself and the overflow threshold); Section 4 "An Implementation
             For TPUs" (the O(√n) practical implementation, with a JAX code
             listing).
Quote:       Abstract: "We present a very simple algorithm for attention that
             requires O(1) memory with respect to sequence length and an
             extension to self-attention that requires O(log n) memory... For
             sequence length 16384, the memory overhead of self-attention is
             reduced by 59X for inference and by 32X for differentiation."
             Section 1: "the memory-efficient algorithm for attention that we
             suggest is not an approximation, but computes the same function."
             Section 2: "This requires just one additional index into the
             list of queries, giving rise to the O(log n) memory complexity.
             Note that the operation produces outputs that are linear in the
             size of the number of queries... which is not counted towards the
             space complexity." Section 3: "For scores ≥ 89 the exponentiation
             results in inf (for bfloat16 and float32)... To resolve this
             problem, we introduce an additional scalar, which keeps track of
             the maximum score... m_i = max(m*, s_i); v* ← v* e^{m*-m_i} +
             v_i e^{s_i-m_i}; s* ← s* e^{m*-m_i} + e^{s_i-m_i}; m* ← m_i."
```

```text
URL:         https://arxiv.org/abs/2307.08691
Kind:        primary for the "honest comparison to the shipped system" claims
             only, per the commission's instruction — Dao is the sole author
             and owner of the FlashAttention-2 work-partitioning changes and
             its measured speedups; affiliation Princeton CS / Stanford CS.
Establishes: That FlashAttention-2 changes parallelism and work partitioning,
             not the underlying exact-attention math; a second, independent,
             fully worked re-derivation of the two-block online-softmax merge
             (with algebra shown to confirm it equals the non-blocked result);
             an explicit statement of which reference is being credited for
             the online-softmax technique itself versus its use in attention;
             and the concrete speedup/utilization numbers useful for the
             honest-limits paragraph.
Paraphrase:  Section 2.3.1 restates online softmax from scratch for a
             two-block row, explicitly deriving m^(2), ℓ^(2), and O^(2) for
             combining a second block into a first, and shows algebraically
             that the combined O^(2) equals the same-shape result computed
             from the whole row at once — a second, independent confirmation
             of the exact-equivalence property Theorem 1 states in the
             FlashAttention paper. The text attributes the online-softmax
             technique itself to citation [11] and its use in attention to
             citation [13]; these resolve to Milakov and Gimelshein (2018) and
             Rabe and Staats (2021) respectively — FlashAttention-2 naming its
             own math lineage in the same shape the commission asserts.
             FlashAttention-2's own stated motivation is that FlashAttention
             (v1) is not yet close to matmul-efficient (25-40% of theoretical
             max FLOPs/s), and it closes that gap through work-partitioning
             changes across GPU thread blocks and warps — a hardware-scheduling
             change, not a change to the math that Theorem 1 in the
             FlashAttention paper proves.
Locators:    Abstract; Section 2.3.1 "Forward pass" (the two-block worked
             derivation and citations [11], [13]); Section 4.1 "Benchmarking
             Attention"; Section 4.2 "End-to-end Performance."
Quote:       Abstract: "FlashAttention... exploits the asymmetric GPU memory
             hierarchy to bring significant memory saving (linear instead of
             quadratic) and runtime speedup (2-4× compared to optimized
             baselines), with no approximation. However, FlashAttention is
             still not nearly as fast as optimized matrix-multiply (GEMM)
             operations, reaching only 25-40% of the theoretical maximum
             FLOPs/s... These yield around 2× speedup compared to
             FlashAttention, reaching 50-73% of the theoretical maximum
             FLOPs/s on A100... FlashAttention-2 reaches training speed of up
             to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization)."
             Section 2.3.1: "As the softmax couples entire rows or blocks of
             row, online softmax [11, 13] can split the attention computation
             into blocks, and rescale the output of each block to finally get
             the right result (with no approximation). ... We describe the
             online softmax technique [11] and how it is used in attention
             [13]." Two-block derivation, final line: "O^(2) =
             diag(ℓ^(1)/ℓ^(2))^{-1} O^(1) + P̃^(2) V^(2) = ... = O." Section
             4.1: "FlashAttention-2 is around 2× faster than FlashAttention
             and FlashAttention in xformers... FlashAttention-2 is around
             1.3-1.5× faster than FlashAttention in Triton in the forward pass
             and around 2× faster in the backward pass... up to 10× faster"
             than PyTorch standard attention. Section 4.2: "FlashAttention-2
             yields up to 1.3× speedup compared to FlashAttention and 2.8×
             speedup compared to a baseline without FlashAttention."
```

## Contradictions

No source disagrees with another on the mathematics: the M&G recurrence, the
FA1 block update, and the FA2 two-block re-derivation are algebraically the
same operation at increasing levels of generality (scalar → matrix block with
attached output accumulator), and I checked this by working the algebra
through by hand from the quoted equations above, not just by reading the
papers' own claims of consistency. Two genuine traps for the writer, neither a
disagreement between sources but both easy to misstate:

1. **The "exact" theorems are real-number theorems, not floating-point
   theorems.** FlashAttention's Theorem 1 and Milakov/Gimelshein's Theorem 1
   both prove equivalence to the naive computation as functions on real
   numbers. Neither paper — nor Rabe/Staats, nor FlashAttention-2 — discusses
   whether re-ordering the summation (which tiling necessarily does) can
   change the result at the bit level under IEEE floating point, where
   addition is not associative. It generally can, by rounding-level amounts.
   The commission's own experiment plan checks equality "to floating-point
   tolerance," which is the right test and implicitly acknowledges this, but
   the article should not claim the two implementations return bit-identical
   arrays — only that they agree to numerical precision, which is what
   "exact" means in this literature. This observation is mine, not sourced;
   flagging it here so the writer doesn't oversell "identical" beyond what any
   of the four papers claims.

2. **The memory-complexity figures across the two "memory" papers are not
   measuring the same thing, and citing them side by side without saying so
   would misstate one or both.** Rabe and Staats' O(1) and O(log n) figures
   are for their idealized algorithm and explicitly exclude the cost of
   writing per-query output ("not counted towards the space complexity");
   their own working TPU implementation lands at O(√n), not O(1) or O(log n),
   because it uses fixed chunk sizes for tractability. FlashAttention's O(N)
   figure is "additional memory beyond inputs and output" — also excluding
   the O(Nd) the inputs and outputs already cost — and it is a claim about
   memory footprint, whereas FlashAttention's actual headline result (Theorem
   2, and the whole IO-awareness argument) is about the asymptotically smaller
   number of HBM accesses, a different quantity from footprint. A reader who
   assumes "O(1)" or "O(N)" describes total memory used, without the
   footnoted exclusions, would come away with an inflated sense of savings.

## Numbers

```text
Figure: m_j = max(m_{j-1}, x_j); d_j = d_{j-1}·e^{m_{j-1}-m_j} + e^{x_j-m_j}
        (the online-softmax recurrence, one scalar element at a time)
Owner:  Milakov and Gimelshein, arXiv:1805.02867, Algorithm 3 lines 4-5
Scope:  Any input vector of length V; final normalizer d_V and max m_V equal
        the two-pass safe-softmax values exactly (Theorem 1)
```

```text
Figure: [m_i; d_i] ⊕ [m_j; d_j] = [max(m_i,m_j);
        d_i·e^{m_i-max(m_i,m_j)} + d_j·e^{m_j-max(m_i,m_j)}]
        (associative, commutative merge of two partial (max, denominator)
        pairs — the operation block-tiling relies on to combine blocks in any
        order)
Owner:  Milakov and Gimelshein, arXiv:1805.02867, Equation 4 and surrounding text
Scope:  Any two partial accumulations over disjoint subsets of the input;
        generalizes by induction to any number of blocks in any order
```

```text
Figure: m_i^new = max(m_i, m̃_ij); ℓ_i^new = e^{m_i-m_i^new}ℓ_i +
        e^{m̃_ij-m_i^new}ℓ̃_ij; O_i ← diag(ℓ_i^new)^{-1}(diag(ℓ_i)
        e^{m_i-m_i^new}O_i + e^{m̃_ij-m_i^new}P̃_ijV_j)
        (block-tiled attention update: same merge as above, extended with a
        rescaled, re-accumulated output block)
Owner:  Dao, Fu, Ermon, Rudra, Ré, arXiv:2205.14135, Algorithm 1 lines 9-13
Scope:  One row-block i of queries against one new column-block j of
        keys/values; iterated over all column blocks (and all row blocks)
        returns the exact O = softmax(QK^T)V (Theorem 1)
```

```text
Figure: O(N^2 d) FLOPs, O(N) additional memory beyond inputs and output
Owner:  Dao et al., arXiv:2205.14135, Theorem 1
Scope:  FlashAttention forward pass, sequence length N, head dimension d;
        "additional" excludes the O(Nd) already spent on Q, K, V, O
```

```text
Figure: Θ(N^2 d^2 M^{-1}) HBM accesses for FlashAttention vs.
        Θ(Nd + N^2) HBM accesses for standard attention (Algorithm 0)
Owner:  Dao et al., arXiv:2205.14135, Theorem 2
Scope:  d ≤ M ≤ Nd, where M is SRAM size; stated to be a provable lower bound
        for exact attention over all SRAM sizes, not an empirical measurement
```

```text
Figure: 15% end-to-end wall-clock speedup on BERT-large (seq. length 512) vs.
        MLPerf 1.1 training speed record; 3× speedup on GPT-2 (seq. length 1K);
        2.4× speedup on long-range arena (seq. length 1K-4K)
Owner:  Dao et al., arXiv:2205.14135, Abstract
Scope:  Measured wall-clock training speedups from the CUDA kernel on GPU,
        against stated baselines — not applicable to a Python/NumPy prototype
```

```text
Figure: O(1) memory w.r.t. sequence length for one query streamed over all
        keys/values; O(log n) for extending to all queries in self-attention;
        O(√n) for the actual JAX/TPU implementation
Owner:  Rabe and Staats, arXiv:2112.05682, Abstract and Sections 2 and 4
Scope:  The O(1)/O(log n) figures exclude the cost of writing per-query
        output and describe the idealized algorithm; O(√n) is what the paper's
        own runnable implementation achieves with fixed chunk sizes
```

```text
Figure: 59× memory-overhead reduction for inference, 32× for differentiation
Owner:  Rabe and Staats, arXiv:2112.05682, Abstract
Scope:  Sequence length 16384, specific to their measured self-attention setup
```

```text
Figure: Exponentiated scores ≥ 89 overflow to inf in bfloat16 and float32
Owner:  Rabe and Staats, arXiv:2112.05682, Section 3
Scope:  Stated for bfloat16 and float32; consistent with float32's max
        representable value (~3.4×10^38 ≈ e^88.7) — a concrete, checkable
        anchor for an overflow demonstration, but the paper does not state
        the corresponding float64 threshold (≈ e^709)
```

```text
Figure: FlashAttention (v1) reaches only 25-40% of theoretical max FLOPs/s;
        FlashAttention-2 reaches 50-73% (up to 230 TFLOPs/s, 73% of max on
        A100); training throughput up to 225 TFLOPs/s per A100 (72% model
        FLOPs utilization); FlashAttention-2 is ~2× faster than FlashAttention
        (~1.3-1.5× forward, ~2× backward in the Triton comparison), up to 10×
        faster than standard PyTorch attention; end-to-end training 1.3×
        faster than FlashAttention and 2.8× faster than no-FlashAttention baseline
Owner:  Dao, arXiv:2307.08691, Abstract and Sections 4.1-4.2
Scope:  Measured on A100 GPUs; FlashAttention-2's own characterization of
        FlashAttention v1's efficiency and its own measured improvement —
        included only for the honest real-system comparison, not as a claim
        about the prototype's math
```

```text
Figure: Softmax alone accelerates up to 1.3×; fused Softmax+TopK up to 5×
Owner:  Milakov and Gimelshein, arXiv:1805.02867, Abstract
Scope:  Their own kernel benchmarks of the online-normalizer technique in
        isolation, predating any attention application — useful only as
        background on where the trick was first measured, not for the
        article's own experiment
```

## Source assets

```text
Asset: FlashAttention paper, Figure 2 (left/middle panels): measured runtime
       and HBM-access count vs. sequence length / block size, GPT-2 setting
Shows: The IO-complexity argument (Theorem 2) validated empirically — fewer
       HBM accesses tracking directly to lower measured runtime despite higher
       FLOP count from recomputation
Crop:  Would need the left panel's runtime-vs-HBM-access comparison alone;
       omit the block-size sweep (middle panel) unless the article discusses
       tuning, which is out of scope here
```

```text
Asset: FlashAttention paper, Algorithm 1 (the boxed pseudocode, Section 3.1)
Shows: The complete, exact block-update procedure line by line — this is a
       stronger anchor than any prose paraphrase for a reader checking the
       article's own nb-code against the paper
Crop:  None found needed; if used at all, the full box should be quoted
       (lines 1-16), not partially cropped, since every line does distinct
       work the equivalence proof depends on
```

```text
Asset: Milakov and Gimelshein paper, Algorithm 2 vs. Algorithm 3 side by side
       (Section 2 and Section 3, adjacent boxed pseudocode)
Shows: The exact three-pass-to-two-pass reduction that motivates "online" —
       useful if the article wants to show the safe-softmax baseline the
       online version improves on, at the softmax level before attention
       enters
Crop:  None found; the two boxes are short and are the whole point of showing
       them together
```

```text
Asset: None found in Rabe and Staats or FlashAttention-2 beyond what is
       already covered by the equations quoted above.
Shows: —
Crop:  —
```

## Discarded

```text
URL: https://arxiv.org/pdf/2205.14135 and https://arxiv.org/pdf/2307.08691 (raw
     PDF fetch): the automated PDF-to-text conversion returned corrupted /
     undecoded FlateDecode stream content on first attempt via the fetch tool.
     Superseded by reading https://arxiv.org/html/2205.14135 and
     https://arxiv.org/html/2307.08691 (the arXiv-hosted HTML rendering),
     downloaded directly and parsed by hand to pull exact equation text; used
     as the basis for every quote above credited to those two papers. The abs
     pages remain the recorded canonical URLs.
```
