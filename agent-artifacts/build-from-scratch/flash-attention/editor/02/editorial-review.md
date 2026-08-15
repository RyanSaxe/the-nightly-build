# Editorial review: build-from-scratch/flash-attention (editor/02)

This is a confirmation re-review after the sources-floor repair. In editor/01 I
completed the three reads and approved the argument, the math, the code's
numbers, and the chart; the only open item was the source floor. This round
verifies the five added sources, the renumber, and that nothing regressed. It
does not re-litigate what editor/01 already settled.

## Skeptic

The thesis and its five supporting claims are unchanged from editor/01, and both
writer handoffs confirm no claim site, number, locator, or `data-nb-kind` on the
original four sources was altered — writer/02 added citations only at existing
claim sites, writer/03 changed numbering only. I confirmed this against the
article: the three-block trace (−1.5058 … 1.1040; m/l values; 0.1151 rescale;
final 2.1351), the memory table (256 MiB at N=8192, 63.0× gap, N≈130 crossover),
the float64 equivalence sweep, and the float32 overflow demo (S.max()=113, three
NaN rows, 2.384e-07 agreement) all read exactly as editor/01 verified them. No
regression.

**The five new citations, each opened as printed.** All five land on the source
that owns the claim they are attached to, and every `data-nb-kind` is honest:

- **s1 — Vaswani et al., "Attention Is All You Need" (arXiv:1706.03762).**
  Opened; title and full author list (Vaswani, Shazeer, Parmar, Uszkoreit,
  Jones, Gomez, Kaiser, Polosukhin) confirmed on the abstract page. Cited once,
  at the orientation opening, for the general attention shape — a score matrix
  with one entry per query/key pair, softmax then weighted sum — which Vaswani
  et al. own. `primary`, correctly: the authors introduced the mechanism.

- **s2 — PyTorch `scaled_dot_product_attention` reference docs.** The printed
  `docs.pytorch.org/.../stable/...` URL resolves via PyTorch's own same-host
  meta-refresh to the version-pinned page (2.13), which I opened directly. It is
  PyTorch's official reference doc; its reference block sets
  `scale_factor = 1/math.sqrt(query.size(-1))` before softmax, and a Note lists
  FlashAttention-2 as one of three backends. `primary`, correctly: PyTorch's own
  documentation of its own function. The "stable" alias is PyTorch's canonical,
  persistent pointer and lands a clicking reader on the live source.

- **s4 — Jia, Maggioni, Staiger, Scarpazza, "Dissecting the NVIDIA Volta GPU
  Architecture via Microbenchmarking" (arXiv:1804.06826).** Opened; title and
  authors confirmed. Cited for the measured HBM-slow / SRAM-fast hardware facts
  the orientation and closing sections assert. `primary`, correctly: the authors
  ran the microbenchmarks themselves and own the measured figures.

- **s5 — Goodfellow, Bengio, Courville, "Numerical Computation" (Deep Learning,
  Ch. 4).** The fetch tool truncated the 1.5 MB PDF-derived HTML, so I confirmed
  the page directly: HTTP 200, and Section 4.1's own text is present — the
  softmax worked example, "adding or subtracting a scalar … input vector.
  Subtracting max," and the log-softmax caveat. It owns the general safe-softmax
  max-subtraction argument, cited at the baseline's `exp(s - max(s))` sentence.
  `primary`, correctly: the authors' own official free HTML edition of their
  textbook.

- **s8 — Dao-AILab/flash-attention repository.** Opened; the README states it
  "provides the official implementation of FlashAttention and FlashAttention-2,"
  a maintained CUDA kernel. Cited at the closing "fused CUDA kernel" claim.
  `primary`, correctly: the shipped artifact of the papers' own author, not a
  third party's report.

**The scaled/unscaled trap is honored.** Both scaled-form sources — Vaswani (s1)
and the PyTorch docs (s2), each of which defines attention with the 1/√d_k
division — are cited only once, together, at the orientation opening, attached
to the general attention shape (query/key score matrix → softmax). Neither is
attached to the article's own unscaled `S = QKᵀ` formula in the
full-matrix-baseline section: that sentence carries no s1/s2 citation, and the
section's formula is cited to FlashAttention's unscaled Algorithm 0 (s3). So no
scaled-form source is presented as though it implements the article's unscaled
code. The trap the researcher flagged twice is respected exactly.

**Citation hrefs and anchors.** Every inline `href="#sN"` targets an existing
`<li id="sN">`; all nine anchors s1–s9 are present; no dangling or mistargeted
reference. The four carried-over URLs (FlashAttention, Milakov/Gimelshein,
Rabe/Staats, FlashAttention-2) were confirmed in editor/01 and their targets did
not change — only their numbers did.

## Cut

No new prose entered the article: writer/02 added citation superscripts at
existing sentences, writer/03 changed only numbers inside `href`/`id`/`sup`.
There is no new sentence to slop-test, and I re-read the edges the new
superscripts sit on to confirm none introduced a stray clause — they did not.
The prose is identical to the version editor/01 already passed on the cut read.
No cuts required this round.

**My four editor/01 edits all still stand, verified in place:**
- Orientation closer reads "That single correction is what makes the streaming
  output exact." (the rewritten sentence).
- The deleted recurrence sentence ("Nothing about d changes which row…") remains
  absent.
- The memory section reads "The saving is asymptotic." with no restored tail.
- Fig. 4's caption reads "(N × block_size + 2N + Nd) × 4 bytes" (the corrected
  formula).

## Renumber spot-check

The renumber is internally consistent and in first-citation order. Reading the
`href` sequence straight through, first appearances fall in exact ascending
order: s1, s2 (orientation opening), s3, s4 (orientation SRAM sentence), s5, s6
(baseline), s7 (memory), s8, s9 (closing) — s1 through s9 with none out of
place. The Sources `<ol>` lists s1–s9 top to bottom with identities matching the
writer/03 mapping (s1 Vaswani, s2 PyTorch, s3 FlashAttention, s4 Jia et al., s5
Goodfellow, s6 Milakov/Gimelshein, s7 Rabe/Staats, s8 repo, s9 FlashAttention-2).
Every `data-nb-locator` still names its own source's territory after the
shuffle: s1 "Section 3.2" (Vaswani's Attention section), s3 the FlashAttention
loci (Algorithm 0/1, Theorems), s4 "Table 3.1, Section 3.6/3.7" (Jia's memory
chapter), s5 "Section 4.1, Equation 4.1" (Goodfellow), s6 the Milakov/Gimelshein
algorithm lines, s7 Rabe/Staats sections, s8 "README.md", s9 "Abstract." No
locator was left pointing at the wrong paper. 24 citation occurrences, 9
anchors, all resolved.

## Reader

Unchanged from editor/01: the piece still gives a runnable, measured
reconstruction that the online-softmax recurrence reproduces exact attention to
floating-point tolerance while holding a flat buffer where the naive matrix
reaches 256 MiB. The five added sources strengthen the sourcing floor without
adding or diluting a single claim, and the prose still sits closer to the
voice-guide exemplars than a median summary.

## Edits

- None. No prose, structure, or furniture change was needed this round; the four
  editor/01 edits were confirmed still in place.

## Required work

- None. The sole open item from editor/01 — the source floor — is resolved.
  Source count is 9 (above the owner's floor of 8), each addition owns a claim
  the article already makes, and `nb check` returns BLOCK 0 / WARN 0 /
  PUBLISHABLE (W-SOURCES-MIN and W-CITE-ORDER both cleared).

## Decision

approve — the five added sources each land as printed and own the claim they are
attached to with an honest `data-nb-kind`, the scaled/unscaled trap is honored
(Vaswani and PyTorch cite only the general attention shape, never the unscaled
`S = QKᵀ` formula), the renumber is internally consistent and in first-citation
order, my editor/01 edits still stand, nothing else regressed, and the gate is
met.
