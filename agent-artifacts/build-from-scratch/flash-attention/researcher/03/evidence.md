# Evidence record: build-from-scratch/flash-attention (researcher 03)

This is a complete record for the round-03 evidence request. Round 02's seven
sources and findings are reproduced below unchanged; nothing in them was
contradicted or superseded. Two new sources are added, both opened and
confirmed, both tied to a claim the article already makes and currently
leaves uncited: Goodfellow, Bengio, and Courville's "Deep Learning" (2016),
Section 4.1, for the general safe-softmax max-subtraction argument the
article's overflow experiment rests on, independent of and predating Milakov
and Gimelshein (2018) by two years; and PyTorch's own
`scaled_dot_product_attention` reference documentation for the "shipped as a
framework's fused attention backend" claim in the closing comparison, distinct
from the Dao-AILab repository already cited (s6) as the kernel's own upstream
home. Both candidates named in the round-03 brief genuinely resolve and own a
claim the article makes, so both are added, bringing the total from seven to
nine — above the owner's floor of eight.

The one new item the writer needs: PyTorch's own reference implementation of
`scaled_dot_product_attention`, quoted in the new s9 entry below, uses the
*scaled* form (`scale_factor = 1 / sqrt(d_k)`), matching Vaswani et al.'s
Equation 1 and not the article's own unscaled `naive_attention`. This is the
same trap flagged in round 02's Contradictions #3 for Vaswani, now confirmed a
second time from an independent source; see the round-03 addendum to
Contradictions #3 below.

## Sources

Entries 1-7 are preserved from researcher/02/evidence.md without change.
Entries 8-9 are new to this round.

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
             Algorithm 3 (the exact update lines, reproduced under Numbers
             below); Section 3.1 "Parallel online normalizer calculation,"
             Equations 3-4 (the merge operator); Theorem 1 and its inductive
             proof, immediately after Algorithm 3.
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
             Round-02 addendum, checked directly against the arXiv HTML source
             for this evidence request: Algorithm 0's own line 1 reads
             "compute S = QKᵀ, write S to HBM," with no scaling factor applied
             to S anywhere in the algorithm box or the surrounding prose. The
             standard-attention formula this paper states is unscaled,
             matching the article's own naive_attention exactly.
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
             not recompute the temporary output of each block." Section 2.2,
             Algorithm 0, line 1 (round-02 recheck): "𝐒 = 𝐐𝐊ᵀ ∈ ℝ^{N×N},
             𝐏 = softmax(𝐒) ∈ ℝ^{N×N}, 𝐎 = 𝐏𝐕 ∈ ℝ^{N×d}, where softmax is
             applied row-wise." No scaling term appears in this statement or
             in the boxed Algorithm 0 that follows it. Citation check: the
             sentence "we decompose the large softmax with scaling [60, 51,
             66]" resolves in the bibliography to reference 60 = Milakov and
             Gimelshein (2018), 51 = Kitaev et al., Reformer (2020), 66 =
             Rabe and Staats (2021) — FlashAttention's own citation of the
             online-softmax source.
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

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez,
             Kaiser, and Polosukhin are the authors and owners of scaled
             dot-product attention, the mechanism the article rebuilds.
             Affiliations stated on the paper: Google Brain (Vaswani,
             Shazeer, Kaiser), Google Research (Parmar, Uszkoreit, Jones),
             University of Toronto (Gomez, work done at Google Brain).
Establishes: The Q/K/V dot-product-then-softmax-then-weighted-sum structure
             the article's naive_attention and streaming_attention both
             implement, and — distinct from what the article's code does —
             the 1/√d_k scaling term the paper states is necessary to keep
             large dot products out of the softmax's small-gradient region.
Paraphrase:  Section 3.2.1 names the mechanism "Scaled Dot-Product Attention."
             Given queries and keys of dimension d_k and values of dimension
             d_v, packed into matrices Q, K, V, the paper computes the dot
             product of each query with every key, divides each by √d_k, and
             applies softmax to get the weights on the values: Equation 1,
             Attention(Q,K,V) = softmax(QKᵀ/√d_k)V. The paper explains the
             scaling directly: without it, for large d_k the dot products
             grow large in magnitude (variance d_k, if each of the d_k
             components of q and k is an independent mean-0, variance-1
             variable) and push softmax into a region with extremely small
             gradients, which is why "dot-product (multiplicative) attention"
             without scaling underperforms additive attention at large d_k
             while the scaled version does not. This scaling term is not
             optional decoration in the paper's own account; it is the stated
             fix for a stated failure mode.
             The article's own textbook computation ("Scores: S = QKᵀ...
             Weights: softmax each row of S. Output: multiply the weight
             matrix by V") and its naive_attention code (`S = Q @ K.T`, no
             division) match FlashAttention's Algorithm 0 line for line (see
             the FlashAttention entry above, round-02 addendum) but do not
             include Vaswani's 1/√d_k division. Citing this paper for "the
             textbook computation" the article rebuilds is accurate for the
             query/key/value, dot-product, softmax, weighted-sum-of-values
             shape; it would misstate the source to cite it for the article's
             specific unscaled formula as if Equation 1 were unscaled. See
             Contradictions.
Locators:    Section 3.2 "Attention" (introductory sentence on queries, keys,
             values, and compatibility functions); Section 3.2.1 "Scaled
             Dot-Product Attention" (the full definition, Equation 1, and the
             scaling rationale, including the footnote on why d_k drives dot
             product magnitude); Figure 2 (left panel, the Scaled Dot-Product
             Attention diagram).
Quote:       Section 3.2.1: "We call our particular attention 'Scaled
             Dot-Product Attention' (Figure 2). The input consists of queries
             and keys of dimension d_k, and values of dimension d_v. We
             compute the dot products of the query with all keys, divide each
             by √d_k, and apply a softmax function to obtain the weights on
             the values. ... Attention(Q,K,V) = softmax(QKᵀ/√d_k)V (1) ...
             Dot-product attention is identical to our algorithm, except for
             the scaling factor of 1/√d_k. ... We suspect that for large
             values of d_k, the dot products grow large in magnitude, pushing
             the softmax function into regions where it has extremely small
             gradients [footnote: assume the components of q and k are
             independent random variables with mean 0 and variance 1; their
             dot product has mean 0 and variance d_k]. To counteract this
             effect, we scale the dot products by 1/√d_k."
```

```text
URL:         https://arxiv.org/abs/1804.06826
Kind:        primary for the measured GPU memory-hierarchy figures — Jia,
             Maggioni, Staiger, and Scarpazza performed the microbenchmarks
             themselves and are the sole owners of the reported latency and
             bandwidth numbers. Affiliation stated on the paper: High
             Performance Computing R&D Team, Citadel, Chicago. A technical
             report, not a peer-reviewed conference or journal paper, but a
             primary source for these figures by the authorship-and-stake
             test: the authors are the ones who ran the p-chase latency probes
             and bandwidth benchmarks the numbers come from, on their own
             hardware, and report the methodology alongside the results.
Establishes: Measured latency and bandwidth for global memory (HBM2, the
             "slow" memory the article's orientation and closing sections
             refer to) versus shared memory (the on-chip, SRAM-backed "fast"
             memory the same sections refer to) on an NVIDIA V100 GPU — the
             specific hardware fact underneath the article's qualitative
             HBM-is-slow / SRAM-is-fast language, currently asserted without
             a citation of its own.
Paraphrase:  Table 3.1 reports, for the Volta V100 (GV100): global memory
             (HBM2) theoretical bandwidth 900 GiB/s, measured 750 GiB/s;
             shared memory theoretical bandwidth 13,800 GiB/s, measured
             12,080 GiB/s — a measured bandwidth ratio of about 16:1 in
             shared memory's favor. Figure 3.2, using the fine-grained
             p-chase method, measures global memory access latency at 28
             cycles on an L1 cache hit, 193 cycles on an L1 miss / L2 hit, 375
             cycles on an L2 miss with a TLB hit, and 1029 cycles on a first
             access that misses both L2 and the TLB. Section 3.6 measures
             shared memory's no-conflict latency at 19 cycles on the V100 —
             the lowest of the five GPU generations the report compares — and
             states plainly that shared memory has "low latency and high
             memory bandwidth" by design, contrasted with global memory's
             role as "the primary means of transferring data to and from the
             host," the slowest tier in the measured hierarchy (Figure 3.1).
             The report attributes the bandwidth gap partly to memory
             technology: Volta and Pascal's HBM2 buses reach meaningfully
             higher bandwidth than the GDDR5 buses on the older GPUs compared
             in the same table.
Locators:    Section 3, "Memory Hierarchy" (chapter opening, Figure 3.1
             hierarchy diagram); Table 3.1 (p. 19, "Geometry, properties and
             latency of the memory hierarchy on the Volta, Pascal, Maxwell and
             Kepler architectures"); Figure 3.2 and its caption (p. 20, global
             memory access latency by cache level); Section 3.6 "Shared
             memory," Latency and Bandwidth subsections (p. 31), Figure 3.9
             (contention latency); Section 3.7 "Global memory" (p. 32),
             Figure 3.11 (measured vs. theoretical bandwidth by GPU).
Quote:       Section 3.6: "The V100 GPU has up to 96 KiB of shared memory
             (configurable) with low latency and high memory bandwidth. ...
             Volta's shared memory has the lowest latency among the GPUs we
             examined." Section 3.7: "Thanks to their adoption of HBM2 memory,
             Volta and Pascal boards feature a significantly higher bandwidth
             than GPUs based on GDDR5 memory. ... Volta not only enjoys higher
             theoretical and actual bandwidth values than Pascal, it also
             enjoys a higher actual-to-theoretical bandwidth ratio (83.3% vs.
             69.6%)." Figure 3.2 caption: "The 1029-cycle latency of the first
             access is the result of both L2 cache miss and TLB miss. The
             accesses to the following data, which are stored in the same L1
             cache line, enjoy the very low, 28-cycle, L1 cache hit latency."
             Table 3.1 (selected cells, V100 column): "Shared memory ...
             No-conflict latency 19 ... Theoretical bandwidth 13,800 GiB/s ...
             Measured bandwidth 12,080 GiB/s"; "Global memory ... Memory bus
             HBM2 ... Theoretical bandwidth 900 GiB/s ... Measured bandwidth
             750 GiB/s."
```

```text
URL:         https://github.com/Dao-AILab/flash-attention
Kind:        primary for "the shipped kernel" claim — Tri Dao and the
             Dao-AILab organization are the maintainers of this repository,
             the same author who wrote the FlashAttention and FlashAttention-2
             papers already cited (s1 above cites Dao, Fu, Ermon, Rudra, Ré;
             s4 cites Dao alone). This is the artifact those papers' own
             authors ship, not a third party's report about it.
Establishes: That a real, maintained CUDA implementation of FlashAttention and
             FlashAttention-2 exists and is what the article's closing section
             means by "a fused CUDA kernel" and "the kernel" when it
             distinguishes what the NumPy prototype in this piece can and
             cannot demonstrate.
Paraphrase:  The README states plainly that the repository "provides the
             official implementation of FlashAttention and FlashAttention-2"
             from the two papers already cited in this article (s1 and s4),
             linking directly to both papers' own URLs. It documents install
             instructions, a Python API, and — separately — a beta
             FlashAttention-3 release for Hopper-generation GPUs, which the
             article does not discuss and this evidence record does not cite
             for anything. The README also links a partial list of production
             systems using the repository, supporting the article's framing
             that the wall-clock and utilization numbers quoted from the
             papers (already in this record's Numbers section) come from code
             that ships and runs, not only from a theorem.
Locators:    Repository root README.md, opening paragraph and "Usage" section
             (the "official implementation" statement and the links to both
             papers); the FlashAttention-3 section further down (read and
             confirmed out of scope for this article, not cited).
Quote:       README, opening lines: "This repository provides the official
             implementation of FlashAttention and FlashAttention-2 from the
             following papers." Followed immediately by the FlashAttention
             paper title, author list, and arXiv link, then the
             FlashAttention-2 title and author line, matching s1 and s4 above
             exactly. "Usage" section: "We've been very happy to see
             FlashAttention being widely adopted in such a short time after
             its release."
```

```text
URL:         https://www.deeplearningbook.org/contents/numerical.html
Kind:        primary — Goodfellow, Bengio, and Courville are the authors of
             this MIT Press textbook (2016) and its Chapter 4; the page is the
             book's own official free HTML edition, hosted by the authors at
             the book's own domain, not a third-party summary or excerpt.
             Genuinely independent of and predating Milakov and Gimelshein
             (2018) by two years, so it owns the general safe-softmax argument
             on its own terms rather than repeating the 2018 paper's framing.
Establishes: The general, hardware-agnostic algebraic argument for why
             subtracting the max before exponentiating fixes softmax overflow
             and underflow: the shift leaves the softmax's analytic value
             unchanged, forces the largest exponent argument to 0 (ruling out
             overflow), and guarantees at least one denominator term equal to
             1 (ruling out a zero denominator from underflow). This is the
             textbook-standard version of the safe-softmax fix the article's
             overflow experiment (Fig. 5, S.max()=113, three float32
             overflows survived by the running max) demonstrates, distinct
             from and prior to Milakov and Gimelshein's online single-pass
             algorithm (already cited, s1), which assumes this same fix and
             builds a fused recurrence on top of it rather than establishing
             it from scratch.
Paraphrase:  Section 4.1, "Overflow and Underflow," opens the book's chapter
             on numerical computation with underflow (numbers near zero
             rounding to exactly zero) and overflow (large-magnitude numbers
             rounding to ±∞) as the two general failure modes, then names
             softmax as a worked example that must be stabilized against
             both. It gives the standard definition (Equation 4.1),
             softmax(x)_i = exp(x_i) / Σ_j exp(x_j), and reasons through what
             happens when every x_i equals a large-magnitude constant c: if c
             is very negative, exp(c) underflows to 0, and the denominator
             becomes 0, leaving the result undefined; if c is very positive,
             exp(c) overflows to ∞, again leaving the result undefined. The
             fix is to evaluate softmax(z) with z = x − max_i(x_i) instead of
             softmax(x) directly. The book states plainly that this shift does
             not change the softmax's analytic value (adding or subtracting a
             scalar from every input to softmax is a no-op on the output), and
             that it fixes both failure modes at once: the largest entry of z
             is exactly 0, so the largest argument passed to exp is 0, which
             cannot overflow; and because that same entry contributes
             exp(0) = 1 to the denominator, the denominator can never
             underflow to exactly 0. The book adds one further caveat the
             article's own experiment does not need: numerator underflow can
             still silently drive an individual output to 0, which is why a
             numerically stable log-softmax needs its own, separately
             stabilized implementation rather than composing log with a
             softmax that has already underflowed — a distinct, narrower
             failure mode than the one the article's overflow experiment
             targets, and not itself a claim the article makes, so it is
             recorded here for completeness rather than cited.
Locators:    Chapter 4, "Numerical Computation," Section 4.1, "Overflow and
             Underflow," pp. 78-79 of the book's own pagination as rendered on
             this page; Equation 4.1 and the two paragraphs immediately
             following it (the c-constant thought experiment and the
             max-subtraction fix); the closing paragraph of the section (the
             log-softmax caveat).
Quote:       "Overflow occurs when numbers with large magnitude are
             approximated as ∞ or −∞... One example of a function that must be
             stabilized against underflow and overflow is the softmax
             function. The softmax function is defined to be
             softmax(x)_i = exp(x_i) / Σ_{j=1}^{n} exp(x_j). (4.1) Consider
             what happens when all the x_i are equal to some constant c.
             Analytically, we can see that all the outputs should be equal to
             1/n. Numerically, this may not occur when c has large magnitude.
             If c is very negative, then exp(c) will underflow. This means the
             denominator of the softmax will become 0, so the final result is
             undefined. When c is very large and positive, exp(c) will
             overflow, again resulting in the expression as a whole being
             undefined. Both of these difficulties can be resolved by instead
             evaluating softmax(z) where z = x − max_i x_i. Simple algebra
             shows that the value of the softmax function is not changed
             analytically by adding or subtracting a scalar from the input
             vector. Subtracting max_i x_i results in the largest argument to
             exp being 0, which rules out the possibility of overflow.
             Likewise, at least one term in the denominator has a value of 1,
             which rules out the possibility of underflow in the denominator
             leading to a division by zero." (Quoted with standard ligature
             spacing artifacts from the page's PDF-derived HTML rendering
             — e.g. "ﬂow" rendered with extraneous internal spacing —
             silently corrected to normal spelling; no wording was altered.)
```

```text
URL:         https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
Kind:        primary for "the shipped-framework fused backend" claim — this is
             PyTorch's own official reference documentation for the function,
             published and maintained by the PyTorch project itself, not a
             third party's account of it. Distinct claim-owner from the
             Dao-AILab/flash-attention repository already cited (s6): s6 is
             FlashAttention's own upstream home; this page is a separate
             organization's (PyTorch's) own statement that it ships
             FlashAttention-2 as a selectable backend inside a standard
             framework function, which is the specific "shipped as a
             framework's fused attention backend" claim in the article's
             closing comparison.
Establishes: That `torch.nn.functional.scaled_dot_product_attention` — a
             function in PyTorch itself, not a third-party extension — offers
             FlashAttention-2 as one of three interchangeable backend
             implementations (alongside Memory-Efficient Attention/xFormers
             and a native C++ fallback matching the reference formula),
             auto-selected by default on the CUDA backend without the caller
             writing any kernel-selection code.
Paraphrase:  The function's reference documentation gives the formula it
             computes as a plain, non-fused reference implementation (the
             docstring's "Efficient implementation equivalent to the
             following" code block): scale_factor = 1/√(query.size(-1)) by
             default, attn_weight = (query @ key.transpose(-2,-1)) *
             scale_factor, softmax applied row-wise, then attn_weight @
             value — the scaled form, matching Vaswani et al.'s Equation 1
             (already cited, s5), not the article's own unscaled
             naive_attention (see the round-03 addendum to Contradictions #3).
             A "Note" admonition on the same page states there are three
             supported implementations: FlashAttention-2 (linking directly to
             arXiv:2307.08691, the same paper already cited here as s4),
             Memory-Efficient Attention (linking to the xFormers repository),
             and a PyTorch C++ implementation matching the reference formula
             above. The page states the function "may call optimized kernels
             for improved performance when using the CUDA backend" and that
             "all implementations are enabled by default," with automatic
             selection based on the inputs, plus explicit context-manager and
             global-flag mechanisms (`torch.nn.attention.sdpa_kernel`,
             `torch.backends.cuda.enable_flash_sdp`) for a caller who wants to
             force one backend. This is the framework-level statement, from
             the framework's own maintainers, that the honest-limits
             comparison in the article's closing section needs: a mainstream
             deep-learning framework ships the FlashAttention-2 kernel as a
             switchable, auto-selected backend behind a standard library call,
             which a NumPy prototype has no equivalent of.
Locators:    "torch.nn.functional.scaled_dot_product_attention" reference
             page (PyTorch 2.13 stable documentation, the version the "stable"
             URL above resolved to at the time of this check): the function's
             main description and its "Efficient implementation equivalent to
             the following" code block (the reference formula); the "Note"
             admonition beginning "There are currently three supported
             implementations of scaled dot product attention"; the paragraph
             beginning "The function may call optimized kernels for improved
             performance."
Quote:       "There are currently three supported implementations of scaled
             dot product attention: FlashAttention-2: Faster Attention with
             Better Parallelism and Work Partitioning [linked to
             arxiv.org/abs/2307.08691] ... Memory-Efficient Attention [linked
             to github.com/facebookresearch/xformers] ... A PyTorch
             implementation defined in C++ matching the above formulation."
             "The function may call optimized kernels for improved
             performance when using the CUDA backend. For all other backends,
             the PyTorch implementation will be used." "All implementations
             are enabled by default. Scaled dot product attention attempts to
             automatically select the most optimal implementation based on
             the inputs." Reference-formula code block: "scale_factor = 1 /
             math.sqrt(query.size(-1)) if scale is None else scale ...
             attn_weight = query @ key.transpose(-2, -1) * scale_factor ...
             attn_weight = torch.softmax(attn_weight, dim=-1) ... return
             attn_weight @ value."
```

## Contradictions

No source disagrees with another on the mathematics: the M&G recurrence, the
FA1 block update, and the FA2 two-block re-derivation are algebraically the
same operation at increasing levels of generality (scalar → matrix block with
attached output accumulator), and I checked this by working the algebra
through by hand from the quoted equations above, not just by reading the
papers' own claims of consistency. Two genuine traps for the writer, neither a
disagreement between sources but both easy to misstate, are preserved from
round 01:

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

3. **Vaswani et al.'s attention formula is scaled; the article's own formula,
   matching FlashAttention's Algorithm 0, is not.**
   Vaswani et al., Equation 1: Attention(Q,K,V) = softmax(QKᵀ/√d_k)V. The
   paper states the 1/√d_k division is not cosmetic — it is the fix for a
   named failure mode, large dot products pushing softmax into a
   small-gradient region as d_k grows (Section 3.2.1, with the variance
   argument in the paper's own footnote). FlashAttention's Algorithm 0
   (already cited as s1) states the standard baseline as S = QKᵀ with no
   scaling term anywhere in the box or the surrounding text — I rechecked
   this directly against the arXiv HTML source for this round. The article's
   naive_attention computes `S = Q @ K.T`, also unscaled, so its own
   "textbook computation" matches FlashAttention's Algorithm 0 verbatim and
   does not match Vaswani's Equation 1 verbatim. This is not an error in the
   article — FlashAttention's own paper makes the identical simplification,
   and the recurrence the piece is actually about (the online-softmax merge)
   does not depend on whether a fixed scalar was applied to S beforehand. But
   it means Vaswani et al. should be cited for the query/key/value,
   dot-product-then-softmax-then-weighted-sum structure the piece rebuilds —
   the shape of the computation — not framed as though its exact formula is
   what the code implements. A citation reading "the scaled dot-product
   attention Vaswani et al. define, S = QKᵀ, softmax, then ·V" would misstate
   the source; "the query/key/value attention mechanism Vaswani et al.
   introduce, here without the 1/√d_k scaling FlashAttention's own baseline
   also omits" would not.
   **Round-03 addendum:** PyTorch's own `scaled_dot_product_attention`
   reference formula (new s9 above) independently confirms the same trap
   rather than complicating it: its documented reference implementation also
   applies `scale_factor = 1/√d_k` before the softmax, the scaled form. This
   is a second, independent source using the scaled convention as the
   framework default, reinforcing — not contradicting — the same caution: if
   the writer quotes PyTorch's reference formula alongside Vaswani's for the
   "textbook computation," neither should be captioned as what the article's
   own unscaled naive_attention implements.

## Numbers

Figures 1-11 are preserved from round 02. Figure 12 is new.

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

```text
Figure: Attention(Q,K,V) = softmax(QKᵀ/√d_k)V
Owner:  Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin,
        arXiv:1706.03762, Section 3.2.1, Equation 1
Scope:  One attention head, queries and keys of dimension d_k, values of
        dimension d_v; the 1/√d_k scaling is stated as necessary for large
        d_k and is not implemented by the article's own naive_attention or
        streaming_attention (see Contradictions #3)
```

```text
Figure: Global memory (HBM2) measured bandwidth 750 GiB/s, theoretical
        900 GiB/s; shared memory measured bandwidth 12,080 GiB/s, theoretical
        13,800 GiB/s (V100/GV100) — roughly a 16:1 measured gap. Global
        memory access latency 28 cycles (L1 hit) up to 1029 cycles (L2 miss +
        TLB miss); shared memory no-conflict latency 19 cycles.
Owner:  Jia, Maggioni, Staiger, Scarpazza, arXiv:1804.06826, Table 3.1
        (bandwidth), Figure 3.2 (global memory latency), Section 3.6
        (shared memory latency)
Scope:  NVIDIA Volta V100 (GV100), measured directly by the paper's authors
        with a p-chase probe and a custom nvprof-instrumented bandwidth
        benchmark; not the numbers for the A100 the FlashAttention paper
        itself benchmarks on, but the same HBM-vs-SRAM relationship the
        article's orientation and closing paragraphs assert qualitatively
```

```text
Figure: softmax(x)_i = exp(x_i) / Σ_j exp(x_j) (Eq. 4.1); softmax(z) with
        z = x − max_i(x_i) is analytically identical and additionally
        guarantees the largest exp argument is exactly 0 (no overflow) and at
        least one denominator term is exactly 1 (no underflow-to-zero
        denominator)
Owner:  Goodfellow, Bengio, Courville, "Deep Learning" (MIT Press, 2016),
        Chapter 4, Section 4.1, Equation 4.1 and surrounding text
Scope:  General real-valued softmax over any input vector x; a
        hardware-agnostic algebraic argument, not a measurement on any
        specific dtype or accelerator — the general-purpose textbook version
        of the fix the article's float32/float64 overflow experiment (Fig. 5)
        demonstrates numerically
```

## Source assets

Preserved from round 01 and round 02, plus two new entries for the sources
added this round.

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

```text
Asset: Jia et al., Figure 3.1, the Volta V100 memory-hierarchy diagram (DRAM,
       L2 cache, L1 data cache / shared memory, registers, annotated with
       what is private to the whole GPU vs. one SM vs. one processing block)
Shows: The physical location of "slow" HBM versus "fast" on-chip SRAM the
       article's orientation paragraph describes in prose — a single diagram
       that would let a reader see the hierarchy instead of only reading
       about it
Crop:  None found needed; the figure is already a compact single box, and
       trimming it would drop the private-to-GPU / private-to-SM labeling
       that is the point of showing it
```

```text
Asset: None found in Vaswani et al. or the Dao-AILab README beyond what is
       already covered by the equations and README text quoted above. (The
       Vaswani paper's Figure 2, Scaled Dot-Product Attention diagram, is a
       standard architecture box with no numeric content the article would
       need beyond Equation 1 itself.)
Shows: —
Crop:  —
```

```text
Asset: None found in Goodfellow, Bengio, and Courville beyond the equation and
       prose already quoted above. Section 4.1 is prose and one numbered
       equation, no figure or table.
Shows: —
Crop:  —
```

```text
Asset: None found in the PyTorch scaled_dot_product_attention documentation
       beyond the reference-formula code block and the three-implementations
       Note already quoted above. The page is reference documentation with no
       chart, benchmark plot, or diagram.
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
     pages remain the recorded canonical URLs. (Carried over from round 01.)
```

```text
URL: https://arxiv.org/pdf/1804.06826 (raw PDF fetch, round 02): the same
     automated PDF-to-text conversion failure occurred (garbled FlateDecode
     stream content). This report has no arXiv HTML rendering, so I downloaded
     the PDF directly and extracted its text with pypdf (page-by-page), which
     produced clean, readable text for the memory-hierarchy chapter (Section
     3, pages 18-33) including Table 3.1 and the figure captions quoted above.
     The abs page, https://arxiv.org/abs/1804.06826, remains the recorded
     canonical URL.
```

```text
URL: Candidate not added (round 02) — a safe-softmax numerical-stability
     reference predating Milakov and Gimelshein (2018), as round 02's optional
     fourth item. Searched specifically for a pre-2018 primary establishing
     the max-subtraction shift as a numerical-stability fix. Found nothing
     that cleared the bar at the time: the max-subtraction identity was
     treated as a folk numerical-computing technique with no single canonical
     originating paper in the search performed then, and Blanchard, Higham,
     and Higham (2021) postdates Milakov and Gimelshein. Superseded this round
     by the round-03 brief's specific candidate, Goodfellow, Bengio, and
     Courville's "Deep Learning" (2016) — a genuine pre-2018 primary that this
     round's search located and added as s8 above. Recorded here so the
     round-02 "not added" note is not read as still current.
```

```text
URL: https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
     (round 03, procedural note, not a rejected source): PyTorch's top-level
     pytorch.org domain issues an HTTP 301 to
     https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html,
     confirmed directly with curl (-L, HTTP 200 after the redirect). That
     "stable" docs.pytorch.org URL is itself PyTorch's own permanent alias for
     "whichever version is current," and it resolves via a client-side
     meta-refresh (not a further HTTP redirect) to a version-pinned page —
     at the time of this check, PyTorch 2.13's
     .../docs/2.13/generated/torch.nn.functional.scaled_dot_product_attention.html
     — confirmed directly with curl, HTTP 200, full reference documentation
     content, matching what is quoted in s9 above. The stable URL is recorded
     as canonical because it is PyTorch's own persistent, versionless pointer
     to this page — the link the project's own navigation and cross-references
     use — and because PyTorch keeps prior-version docs archived rather than
     deleting them, so the version-pinned page a reader ultimately lands on
     stays live even after "stable" moves on to a newer release. Not
     discarded; recorded here only to make the two-hop resolution path
     explicit for whoever next confirms this URL.
```

## Report to orchestrator

Two sources added and confirmed open this round, each tied to a claim already
in the article and currently uncited, both named as candidates in the
round-03 brief:

- Goodfellow, Bengio, and Courville, "Deep Learning" (MIT Press, 2016),
  Chapter 4, Section 4.1 ("Overflow and Underflow"),
  https://www.deeplearningbook.org/contents/numerical.html — owns the
  general, hardware-agnostic safe-softmax max-subtraction argument the
  article's overflow experiment (Fig. 5) demonstrates numerically, genuinely
  independent of and two years prior to Milakov and Gimelshein (2018,
  already cited as s1), which assumes this fix rather than establishing it.
- PyTorch's `scaled_dot_product_attention` reference documentation,
  https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
  — owns the "shipped as a framework's fused attention backend" claim in the
  closing comparison: PyTorch's own documentation states that
  FlashAttention-2 is one of three selectable, auto-chosen backends behind
  this standard library function, distinct from the Dao-AILab repository
  already cited (s6) as the kernel's own upstream home.

This brings the source count from seven to nine, above the owner's eight-source
floor, with no padding: both additions own a claim the article already makes
and neither restates a source already in the record.

One item the writer needs before citing the new PyTorch source: its own
reference-formula code block is the *scaled* form (`scale_factor =
1/√d_k`, matching Vaswani's Equation 1, already flagged in round 02's
Contradictions #3), not the article's own unscaled `naive_attention`. This is
the same trap already flagged for Vaswani, now independently confirmed by a
second source; see the round-03 addendum appended to Contradictions #3 above.
The Goodfellow source carries no such trap — its softmax formula and fix are
scale-invariant with respect to the 1/√d_k question, since Section 4.1 is
about softmax alone, not attention.
