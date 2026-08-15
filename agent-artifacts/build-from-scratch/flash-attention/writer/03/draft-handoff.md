# Draft handoff: build-from-scratch/flash-attention (writer 03)

## Original work

Unchanged from round 02: this piece writes, runs, and measures both attention
implementations itself. Neither the naive N²-matrix baseline nor the
block-tiled online-softmax version exists anywhere in the evidence record as
code, so every number the article asserts is this piece's own runtime
output, not a restatement of anything the papers themselves report. This
round touched no content, only citation numbering.

## Editorial requests resolved

- Brief's single fix: renumbered all nine sources into strict
  first-citation order, overriding the round-02 instruction to keep numbers
  intact (that instruction is what produced the W-CITE-ORDER warning this
  round clears).

  First-citation order in the unedited body was s5, s6, s1, s7, s8, s2, s3,
  s9, s4. Applying that order as the new numbering:

  | old | new | source |
  |---|---|---|
  | s5 | s1 | Vaswani et al., "Attention Is All You Need" |
  | s6 | s2 | PyTorch `scaled_dot_product_attention` docs |
  | s1 | s3 | Dao, Fu, Ermon, Rudra, Ré, "FlashAttention" |
  | s7 | s4 | Jia, Maggioni, Staiger, Scarpazza, Volta microbenchmarking |
  | s8 | s5 | Goodfellow, Bengio, Courville, "Numerical Computation" |
  | s2 | s6 | Milakov, Gimelshein, "Online normalizer calculation" |
  | s3 | s7 | Rabe, Staats, "Self-attention Does Not Need O(n²) Memory" |
  | s9 | s8 | Dao-AILab/flash-attention repository |
  | s4 | s9 | Dao, "FlashAttention-2" |

  Every `<sup class="nb-cite">` superscript, its `href="#sN"`, and the
  corresponding `<li id="sN">` anchor in the Sources list were updated
  together (24 citation occurrences, 9 list anchors). The Sources `<ol>` was
  reordered so the list order now matches the new numbering (s1..s9 top to
  bottom). No `data-nb-locator`, no `data-nb-kind`, no claim site, no prose,
  and no number the article asserts changed. `nb-meta` `sources` remains 9.

## Proof result

`./nb check --series build-from-scratch
.nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html
--library /home/user/library-checkout` (links included, after `nb stamp`):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

W-CITE-ORDER is gone; no warnings remain.

## Open questions

None blocking. The `nb preview` KaTeX/Prism egress limitation noted in round
02 still applies to this sandbox, but this round did not touch the
`nb-math` block or code listings, and no citation markup lives inside
either.
