# Draft handoff: build-from-scratch/flash-attention (writer 02)

## Original work

Unchanged from round 01, and still true after this round's citation-only
revision: this piece writes, runs, and measures both attention
implementations itself. Neither the naive N²-matrix baseline nor the
block-tiled online-softmax version exists anywhere in the evidence record as
code, so every number the article asserts (the five float64 equivalence
diffs, the eight-point peak-memory series behind the chart and its N≈130
crossover, the three-block rescale trace, and the three-of-sixty-four
float32 overflow the safe versions survive) is this piece's own runtime
output, produced by writing the recurrence into code and executing it, not a
restatement of anything the papers themselves report.

## Editorial requests resolved

- Sources-floor item from `editor/01/editorial-review.md`: added the five
  sources the researcher confirmed in `researcher/02/evidence.md` and
  `researcher/03/evidence.md` — Vaswani et al. (`s5`), PyTorch's
  `scaled_dot_product_attention` reference docs (`s6`), Jia, Maggioni,
  Staiger, Scarpazza (`s7`), Goodfellow, Bengio, and Courville (`s8`), and
  the Dao-AILab/flash-attention repository (`s9`) — bringing the count from 4
  to 9, above the owner's floor of 8. Each is cited only at an existing claim
  site the article already makes, with no new claims or sections added:
  - `s5`/`s6` (Vaswani; PyTorch docs) at the orientation's opening sentence,
    the general query-paired-with-key score-matrix shape — not on the
    article's own unscaled `S = QKᵀ` formula sentence in the
    full-matrix-baseline section, per the scaled/unscaled trap both
    evidence rounds flagged: Vaswani's Equation 1 and PyTorch's reference
    formula are both the *scaled* softmax(QKᵀ/√d_k)V, and the article's
    `naive_attention`/`streaming_attention` code is unscaled, matching
    FlashAttention's own Algorithm 0. No sentence was reworded to imply
    otherwise.
  - `s7` (Jia et al.) at the orientation's HBM/SRAM sentence and again at the
    closing section's "fused CUDA kernel... SRAM... HBM" sentence, the two
    places the editorial review named as asserting the HBM-slow/SRAM-fast
    hardware facts.
  - `s8` (Goodfellow, Bengio, Courville) at the full-matrix-baseline
    section's safe-softmax max-subtraction sentence, the general fact the
    overflow experiment later demonstrates numerically.
  - `s9` (Dao-AILab repo) at the closing section's "fused CUDA kernel"
    sentence, the shipped-kernel claim.
  Every existing citation, its number, and every existing number in the
  article are unchanged. `nb-meta` `sources` now reads 9 (written by
  `nb stamp`, not hand-set).

## Proof result

`./nb check --series build-from-scratch
.nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html
--library /home/user/library-checkout` (links included, after `nb stamp`):

```
BLOCK: 0
WARN:  1
  W-CITE-ORDER       citation '#s5' (source 5) is first cited before source 1; number sources in order of first appearance
verdict: PUBLISHABLE
```

This warning is left standing rather than fixed, and it replaces the round-01
W-SOURCES-MIN warning, which is now clear. The check requires every source's
first in-document citation to land in exact list order (s1, then s2, then
s3, then s4, then s5...). In the original, unedited article s2 first appears
only in the full-matrix-baseline section and s4 only in the closing section,
so no citation of any round-02/03 source can appear anywhere in the
orientation or full-matrix-baseline sections — where the editor's required
work explicitly places them (the attention definition and the HBM/SRAM facts
in the orientation, the safe-softmax fact in full-matrix-baseline) — without
tripping this check. The only way to clear it fully would be either to
renumber `s1`-`s4`, which the brief requires stay intact, or to move the new
citations off the claim sites the editor named onto some other sentence that
does not actually make the claim, which would misattribute the source. Both
are worse than the warning. `nb check` treats this as non-blocking by
design (`rep.warn`, not a block), and every citation resolves and supports
the sentence it is attached to.

## Open questions

None blocking. One open item carried from round 01, unresolved because this
round's tools have the same restriction: `nb preview` cannot fetch KaTeX or
Prism from jsdelivr/cdnjs under this sandbox's egress policy, so the
recurrence equation and code highlighting could not be visually re-confirmed
after this round's edits (none of which touched the `nb-math` block or code
listings). `nb render-check` reports no page errors or overflow at 390px.
