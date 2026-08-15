# Draft handoff: build-from-scratch/flash-attention (writer 01)

## Original work

This piece writes, runs, and measures both attention implementations itself:
the naive N²-matrix baseline and the block-tiled online-softmax version exist
nowhere in the evidence record as code, so every number the article asserts
(the five float64 equivalence diffs, the eight-point peak-memory series behind
the chart and its N≈130 crossover, the three-block rescale trace, and the
three-of-sixty-four float32 overflow that the safe versions survive) is this
piece's own runtime output, produced by writing the recurrence into code and
executing it, not a restatement of anything the four papers themselves report.

## Proof result

`./nb check --series build-from-scratch
.nb-work/build-from-scratch/flash-attention/library/build-from-scratch/flash-attention.html
--library /home/user/library-checkout` (links included, after `nb stamp`):

```
BLOCK: 0
WARN:  1
  W-SOURCES-MIN      4 sources; series floor is 8
verdict: PUBLISHABLE
```

The one warning left stands rather than gets fixed. The evidence record
verified exactly four primary papers, and the commission scopes the piece
tightly to the online-softmax core those four papers establish end to end
(the recurrence's origin, its two independent re-derivations, and the honest
real-kernel comparison). Padding the source list to clear the floor would mean
citing something the researcher did not open, which the house standard and
the writer brief both rule out. Sentence-density warnings (12 on the first
pass) were fixed by splitting, not left.

## Open questions

None blocking. Two judgment calls worth the editor's attention:

- The annotated `nb-math` equation is the scalar Milakov-Gimelshein
  recurrence (Algorithm 3), not the block-tiled FlashAttention form, on the
  theory that it is "the one equation the piece is really about" per the
  commission and lets the block section build on notation the reader already
  has. The block update itself is fully shown in code (Fig. 2) and prose
  instead of a second equation, since the article is allowed only one
  annotated equation.
- KaTeX and Prism load from jsdelivr/cdnjs at runtime (`nb.js`), which this
  sandbox's egress policy blocks, so `nb preview` here shows raw TeX text and
  unhighlighted code rather than typeset output. `nb render-check` reports no
  page errors and no overflow at 390px, and I hand-verified the equation's
  brace-balance against the furniture catalog's own annotated-equation
  example; I could not visually confirm the typeset render before handoff.
