# Editorial review: build-from-scratch/flash-attention (editor/01)

## Skeptic

Thesis: exact attention never needs the full N-by-N score matrix in memory,
because a running max and a running denominator, updated one block of keys at a
time and rescaled whenever a block raises the max, produce the identical output;
a from-scratch NumPy version proves it against the naive baseline and shows what
the running max buys where the unshifted softmax overflows.

The claims it stands on, and how each held:

1. **The online-softmax recurrence equals the two-pass safe softmax.** The
   annotated equation reproduces Milakov and Gimelshein Algorithm 3 lines 4-5
   character-for-character (running max, running denominator, rescale term), and
   the evidence record confirms it against their Theorem 1. The legend labels
   each term correctly. Held.

2. **The block-tiled update returns exactly softmax(QKᵀ)V.** Cited to
   FlashAttention Algorithm 1 lines 9-13 and Theorem 1. The code in Fig. 2
   implements the merge (`m_new`, rescale of `l` and `o` by `exp(m - m_new)`,
   re-accumulate) faithfully. Held.

3. **The two implementations agree only to floating-point tolerance, not
   bit-identity.** This is the researcher's flagged trap #1, and the article
   handles it correctly: Fig. 3's float64 diffs (4.4e-16 up to 6.2e-15) are all
   small multiples of the float64 rounding unit, none zero, and the prose states
   plainly that the equivalence theorems are real-number theorems while
   floating-point addition is not associative. No overclaim of "identical." Held.

4. **Memory: the naive score matrix is O(N²), the streaming peak is O(N), and
   the papers' asymptotic figures are not the byte counts measured here.** I
   recomputed the whole table and chart against the committed `chart-1.py`
   closed form (naive = 4N²; streaming = 520N at d=64, block=64). Every table
   cell and ratio checks out: N=64 → 16 384 / 33 280 (0.5×); N=256 → 262 144 /
   133 120 (2.0×); N=1024 → 4 194 304 / 532 480 (7.9×); N=4096 → 31.5×; N=8192 →
   268 435 456 / 4 259 840 (63.0×). The crossover 4N² = 520N gives N = 130, so
   "N≈130" is exact. 268 435 456 B = 256 MiB, so the dek's "256 mebibytes by
   sequence length 8192" is right. The article also correctly separates
   Theorem 1's O(N) "additional" memory and Rabe/Staats' O(1)/O(log n) from the
   measured footprint (researcher trap #2). Held.

5. **The running max is what keeps the softmax finite.** Fig. 5's batch has
   S.max()=113.0, three of sixty-four scores ≥ 89, three NaN rows from the
   unshifted version, and safe/streaming agreeing to 2.384e-07 (float32 rounding
   unit). The 89 overflow threshold is Rabe and Staats Section 3, cited
   correctly. Held.

I re-derived the three-block trace by hand from the six stated scores
(−1.5058, −0.6387, −0.8939, 1.5231, 0.0306, 1.1040): block 0 gives m=−0.6387,
l=1.4202; block 1 raises m to 1.5231 with rescale exp(−2.1618)≈0.1151 and l to
≈1.2526 (article prints 1.2527, a fourth-decimal rounding difference, not an
error); block 2 keeps m and grows l to 2.1351. All consistent with the code.

**Display text.** Headline "A running max and a running sum replace attention's
score matrix" is subject-verb, concrete, no colon subtitle, and states the claim
the piece defends. Dek makes a claim about the world (reproduces exact attention
to float32 precision, names the 256 MiB the naive version costs), not a grade of
method. All seven section headings are declarative claims in the piece's own
nouns; none is a scaffolding slot, none copies the rotary piece's "what X does
not buy." The float32/float64 split is worth noting but not a defect: the dek's
"float32 precision" is supported by Fig. 5 and pairs with the float32 memory
figures, even though the five-size equivalence sweep (Fig. 3) is float64.

**data-nb-kind audit.** All four sources are `primary` and correctly so: each is
the arXiv abstract page owned by the paper's own authors (Dao et al.; Milakov
and Gimelshein / NVIDIA; Rabe and Staats / Google; Dao). No secondary source is
mislabeled as primary, and none hides a missing independent source — the concern
here is the opposite, the source *count* (see the floor ruling below).

**Citation hrefs.** I opened all four source-list URLs as printed. Every one
resolves to the correct arXiv abstract page with the exact title and author list
the article prints: 2205.14135 (FlashAttention, Dao/Fu/Ermon/Rudra/Ré),
1805.02867 (Milakov, Gimelshein), 2112.05682 (Rabe, Staats), 2307.08691
(FlashAttention-2, Dao). Inline anchors #s1–#s4 all target existing list items.
No broken or mistargeted citation.

**Chart provenance.** The committed `chart-1.py` computes the same accounting
the code performs at runtime, and its numbers match the table exactly. The
rendered PNG is honest: both axes labeled and log-scaled, legend present,
crossover near N≈130, naive slope 2 to ~256M at N=8192, streaming shallower to
~4M. One defect, in the figure caption rather than the chart: it stated the
streaming buffer as "(N × block_size + 3N + Nd) × 4 bytes," but the code holds
`m` (N) + `l` (N) + `o` (Nd) = 2N + Nd, and `chart-1.py` itself uses 2N + Nd. I
corrected the caption to "2N" directly, since the right value is the article's
own code and script. No change to the chart image or script is needed.

## Cut

Slop pass against `spec/slop.md`, every sentence including display text, code
captions, table caption, and the math legend. The draft is unusually clean:
almost every sentence is carried by its subject-specific nouns (the actual
scores, byte counts, dtype thresholds), so it survives the placeholder test.
Three sentences failed and were cut, all at edges, all signposts or filler:

- Orientation closer: "...and by the end of this piece it shows up in real
  numbers rather than being taken on faith" — a method-signpost promising a
  future demonstration, with mild self-reference ("this piece"). The surviving
  "That single correction is the entire trick" also leaned toward the "X is the
  whole Y" tell, so I rewrote the whole sentence to carry the causal claim
  plainly: "That single correction is what makes the streaming output exact."
- Recurrence section: "Nothing about d changes which row it belongs to, and
  nothing about m changes what d is normalizing." Cut. It references "row" in
  the scalar-stream passage where no rows exist yet (a dangling model the reader
  has not been given), and it carries no checkable fact the next sentence does
  not already carry.
- Memory section: "...and the table shows exactly where it starts to pay for
  itself and how fast it grows once it does." Cut the tail; it is a signpost
  describing what the adjacent table already shows. "The saving is asymptotic"
  survives as a reasoning summary.

Three sentences failed; no recurring pattern beyond edge-signposts. Edges I
checked and kept: the full-matrix section's "not a restatement of the paper's
own HBM-traffic claim" is earned negative parallelism — it corrects the real
HBM-traffic-versus-RAM-footprint distinction the researcher flagged, not an
invented strawman. The closing "The 15 percent, the 3×, and the 2.4× belong to
the kernel. A NumPy loop cannot produce them" is a concrete conclusion the
experiment earned, in the piece's own vocabulary — the habits-to-break target
(a "what X does not buy" heading, a closing `nb-note-strong` verdict box) is
absent throughout; there is no `nb-note` in the piece at all.

Prompt-leakage check against the commission, briefs, and voice guide: no lifted
framing, planning label, or "the assignment was fulfilled" claim. The honest-limit
paragraph states the boundary as reported fact, not as an instruction echo.
Borrowed-phrasing check against the voice-guide quotations (Hashimoto, Olah,
Weng): no distinctive clause carried over; the register matches (plain claims
stated then earned against the listing) without copying any exemplar's wording.
Punctuation: zero em-dashes; commas, colons, and periods used within standard.
Grammar and syntax clean in body, display, and furniture.

Furniture: the `nb-math`, two `nb-code` blocks, the `nb-table`, and the
`nb-figure` chart each carry distinct evidence, not decoration or a quota. The
writer's judgment call to set the single annotated equation as the scalar
Milakov-Gimelshein recurrence rather than the block-tiled form is the right one:
it is the one equation the piece is really about, the reader meets the notation
before the block section reuses it, and the block update is fully shown in code
(Fig. 2). I would not swap it.

## Reader

Reading straight through as an ML engineer who has read only this article, the
one thing I have that the four papers alone would not give me: a runnable,
measured demonstration that the online-softmax recurrence reproduces exact
attention to floating-point tolerance and holds a flat buffer where the naive
matrix reaches 256 MiB — the numbers (the equivalence diffs, the 63× memory gap,
the three float32 overflows the running max survives) are the article's own
runtime output, produced by writing and executing the recurrence, none of it
restated from the papers. The draft-handoff's original-work sentence claims
exactly this, and the article delivers it. The prose sits closer to the
voice-guide exemplars than to a median summary: it states each claim plainly and
then earns it against real numbers from the code, in the Hashimoto register the
guide names. This is not a restatement of its sources; it is a reconstruction
that measures what the sources assert.

## Edits

- Orientation: rewrote "That single correction is the entire trick, and by the
  end of this piece it shows up in real numbers rather than being taken on
  faith." to "That single correction is what makes the streaming output exact."
  (cut method-signpost and self-reference; neutralized the "X is the whole Y"
  tell).
- Recurrence section: deleted "Nothing about d changes which row it belongs to,
  and nothing about m changes what d is normalizing." (dangling "row" referent
  in a scalar passage; no checkable fact).
- Memory section: cut the tail of "The saving is asymptotic, and the table shows
  exactly where it starts to pay for itself and how fast it grows once it does."
  to "The saving is asymptotic." (table-signpost).
- Fig. 4 caption: corrected the streaming-buffer formula from
  "(N × block_size + 3N + Nd) × 4 bytes" to "(N × block_size + 2N + Nd) × 4
  bytes" to match the code (m + l + o = 2N + Nd) and `chart-1.py`.

## Required work

- **Researcher (round-02 evidence addition) — sources floor.** See the explicit
  ruling below. Add genuine, readable primary sources that own claims the
  article already makes, to meet the owner's floor of eight without padding.
  Read and confirm each; add only those that own a claim and resolve. Named
  candidates:
  - Vaswani et al., "Attention Is All You Need," arXiv:1706.03762 — owns the
    scaled dot-product attention (S = QKᵀ, softmax, ·V) the piece rebuilds and
    opens on, currently uncited.
  - A GPU memory-hierarchy primary (e.g., the NVIDIA A100/Ampere architecture
    whitepaper, or a peer-reviewed GPU-microbenchmark paper) — owns the
    "HBM is slow memory / SRAM is fast on-chip memory" hardware facts the
    orientation and closing paragraphs assert, currently leaning implicitly on
    the FlashAttention paper.
  - The shipped implementation for the honest real-kernel comparison (e.g.,
    the Dao-AILab/flash-attention repository, or PyTorch's
    `scaled_dot_product_attention` documentation that integrates it) — owns the
    "the real kernel / the shipped system" claims.
  - Optional, only if a genuine claim-owner: a safe-softmax numerical-stability
    reference predating Milakov-Gimelshein for the max-subtraction fix. Add only
    if it truly owns the claim; do not pad.
- **Writer (after evidence lands).** Cite the new primaries at the existing
  claim sites — the attention definition in the orientation, the HBM/SRAM facts,
  and the real-kernel comparison — without adding new sections or drifting into
  a survey of attention variants. Re-run the proof; `nb-meta` `sources` updates
  from 4. No chart or asset work is required; the caption defect was fixed in
  edit above.

## Decision

revise — the article's argument is sound, its numbers all reconcile against the
committed code, and its citations resolve, but real readable primaries exist for
claims the piece already makes (the attention origin, the GPU memory hierarchy,
the shipped kernel), so the owner's eight-source floor should be met by a
round-02 evidence addition rather than approved under W-SOURCES-MIN.

### Sources-floor ruling (explicit)

I do **not** approve under the floor. The four papers genuinely carry the core
mathematical argument — the recurrence, its two independent re-derivations, and
the honest real-kernel comparison — and I would reject any attempt to pad the
list with sources the researcher has not read. But the review brief asked
whether legitimate additional sources exist that a researcher could actually
read and cite, and they do, tied to claims the article already asserts and
currently leaves uncited: the scaled dot-product attention it rebuilds
(Vaswani et al.), the HBM-slow/SRAM-fast hardware facts it states (a GPU
memory-hierarchy primary), and the shipped kernel it compares against (the
implementation's own repository or docs). Adding these is not a survey and does
not violate cite-only-what-you-read, because each owns a claim already in the
piece and each is readable. Four plus these reaches the owner's floor of eight
with real sources. The writer's round-01 decision to stand on four rests on
"padding would violate the house standard," which only holds if no legitimate
additional sources exist; they do, so the stand does not survive. Route to the
researcher first, then the writer.
