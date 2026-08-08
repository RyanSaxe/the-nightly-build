# Editorial review: paper-of-the-day/neural-machine-translation-attention (editor/01)

## Skeptic

Thesis: Bahdanau's 2015 model removed the fixed-vector bottleneck by rebuilding a
soft read of the source at every output word, and the alignments it learned look
linguistic without settling the later, stronger question of whether attention
weights explain the output. The piece stands on four load-bearing claims: (1) the
reconstruction math (context vector, softmax alignment weights, additive score) is
the paper's actual mechanism; (2) the Table 1 / Figure 1 evidence shows the
fixed-vector baseline decaying on long sentences while the attention model holds;
(3) the captured alignment matrix (Figure 2) shows a genuine linguistic
reordering; (4) the "attention is / is not explanation" debate bears on those
alignments only as the article's own inference, never as a claim either 2019 paper
makes about Bahdanau's model.

Math. Verified every displayed line against the evidence record and the primary
(Appendix A.1.2 fetched directly). `c_i = sum_j alpha_ij h_j`, the softmax
`alpha_ij = exp(e_ij)/sum_k exp(e_ik)`, and the additive score
`e_ij = v_a^T tanh(W_a s_{i-1} + U_a h_j)` are all correct and correctly located.
The score's dependence on `s_{i-1}` (previous decoder state) versus the emission's
use of `s_i` is handled correctly in the legend and prose. The two consequences
the prose reads off the score line — `U_a h_j` is independent of `i` so it is
precomputed (near-linear cost), and the path is differentiable end to end so one
backward pass trains the alignment — are both real and are exactly the objects the
voice guide wants the math spent on. The math is set as objects reasoned from, not
narrated; each equation is motivated before and consumed after. Holds.

Table 1. All six rows match the paper's own table exactly, confirmed against the
primary: RNNencdec-30 13.93/24.19, RNNsearch-30 21.50/31.44, RNNencdec-50
17.82/26.71, RNNsearch-50 26.75/34.16, RNNsearch-50* 28.45/36.15, Moses
33.30/35.63. The article labels the baseline "RNNenc" everywhere (table, prose,
alt text). The primary's Table 1 writes "RNNencdec," but its Figure 2 legend —
baked into the captured asset-1.png the article displays — writes "RNNenc." The
article normalized to the figure's abbreviation so the displayed plot and the
table name the same model; this is internally consistent and matches the paper's
own figure, not a fabricated label. Directional claims check out: RNNsearch-30
(21.50) beats RNNencdec-50 (17.82); RNNsearch-50* (36.15 No UNK) edges Moses
(35.63 No UNK), and the article correctly confines that "edge" to the No-UNK set
and never claims a win on the full set, where Moses leads. The "418-million-word
monolingual corpus" for Moses is not in the evidence record's Numbers block, so I
verified it against the primary: the paper states "Moses uses a separate
monolingual corpus (418M words)." Sourced and correct.

Figures as evidence. Inspected both captured assets directly. Asset-1 (the paper's
Fig. 2) shows RNNencdec curves peaking near 22 and falling steeply while
RNNsearch-50 holds flat around 26-27 across all lengths — the prose's core reading
is honest. One imprecision: the prose says "RNNsearch stays flat," but the figure
shows RNNsearch-30 (dotted) declining past its 30-word training length. The
sentence immediately singles out RNNsearch-50 for "no decay even past fifty
words," and the article's caption attributes the flat-holding to the attention
model generally, so the contrast the figure is spent on survives; I judged this a
tolerable generalization, not a misread. Asset-2 (the paper's Fig. 3) shows panel
(a) exactly as described: generating "zone" the alignment crosses to "Area" over
"European"/"Economic," then steps back for the two adjectives in French order. The
captions are factual, cited, and carry the paper's verbatim caption in the
`data-nb-note`; interpretation stays in the prose. Both figures meet the figure
license. The article numbers them locally as Fig. 1 / Fig. 2 while the
`data-nb-locator` correctly points to the primary's Fig. 2 / Fig. 3 — honest
local numbering, not a citation slip.

The explanation bridge. This is the piece's spine and it holds. The Scope note and
the verdict both state, in the article's own voice, that neither 2019 paper tested
Bahdanau's translation model (they study later BiLSTM classification/QA), so
carrying the dispute onto Figure 2's alignments is the article's inference, "not a
claim either paper makes about this paper," and that Bahdanau's own reading was the
modest "agree well with our intuition." Both sides are steelmanned: Jain &
Wallace's two grounds (low correlation with gradient/leave-one-out importance;
constructible alternative attention distributions) and Wiegreffe & Pinter's
sharper objection (a per-instance adversary is weaker than a single
dataset-consistent one; the reliable adversaries do poorly on the frozen-attention
diagnostic). Quotes and paraphrases match the evidence record. The predecessor
line is handled honestly: the long-sentence degradation is attributed
specifically to the RNN Encoder-Decoder line (Cho 1406.1078 / 1409.1259), and
Sutskever's contrary "did not have difficulty on long sentences" is acknowledged
with an explicit refusal to compare BLEU across the different vocabulary/decoding
setups. No cross-setup BLEU is compared head-to-head.

Display text. Headline, dek, and every subhead check out as claims about the
world, not self-grading. Author names, dates, venues, arXiv IDs, and quantities in
display text all verify. The dek breaks the flagged recent mold: it opens on "The
2015 model," not author-surnames-plus-verb, and closes on "without settling what
the weights explain," not an "after-record narrows it" clause.

data-nb-kind audit. Every non-focal source (s2-s8) is labeled `secondary` and only
the focal paper `primary`. Under the strict "a primary owns the claim" test, some
of these (Luong, Jain & Wallace, Wiegreffe & Pinter) are cited for claims their
own authors own and could read as primary-for-that-claim. But this article follows
the paper-template convention where the focal paper is the sole primary and all
predecessor/after-record literature is contextual/secondary; the labeling is
internally consistent and, critically, hides no missing independent source (none
of these is presented as independent corroboration of a focal claim; s3 is
explicitly flagged as the "same group"). I audited this and accept it as a
defensible convention rather than a sourcing failure.

Links. Every source-list `href` carries a correct, resolving arXiv ID for the
paper it names (1409.0473 confirmed live; the rest are the correct canonical IDs),
and every inline `data-nb-url` lands on the source itself (abstract or the paper's
own PDF), not a text-extraction endpoint.

No claim retired. No break found that a fix or route is needed for.

## Cut

Ran the earns-its-place test sentence by sentence. The prose is already lean and
in-register, and I made no cuts: the sentences I flagged as candidates each clear a
license or carry cargo.

- "Read it as data." and "Read the strength of that claim exactly:" — imperative
  openers that would normally read as lecture-openers, but each enacts the voice
  guide's figure/verdict license (read the figure as measurement; bound the claim)
  and is immediately followed by the actual data reading or the bound. Kept.
- "The gap is not marginal." / "The read is soft, then." / "One bound on the
  reading." — short verdict/consequence snaps the cadence calls for; each reads a
  consequence off the evidence just laid down. Kept.
- Pull quote ("Attention entered translation as a way to read the source, and only
  later was asked to justify the output.") sits at the true hinge between the
  mechanism's success and the explanation debate, and marks a deliberate emphasis
  the template licenses. It echoes the headline's thesis but the argument has
  earned both halves by that point. Kept.
- "answered no" / "answered not so fast" — the second is faintly colloquial for the
  reviewer register, but it parallels the first cleanly and stays compact. Optional
  polish only; not touched, to avoid regressing the voice.

Worst tell found: none rising to a cut. The nearest thing is the triple statement
of the plausibility-vs-explanation caveat (Scope note, "what to be careful about"
ledger bullet, verdict), but these sit at three deliberate altitudes — the visible
original-work disclosure, the scannable ledger, and the bounded synthesis — and the
ledger restating prose points is the furniture's job, not redundancy. Furniture
overall (paper card, three math displays, two figures, table, pull quote, hold-up
block, scope and verdict notes) each carries distinct evidence or reasoning; the
verdict section's hold-up block plus verdict note are template-appropriate for the
"state a verdict before the sources" mandate and do not read as a stack.

No prompt leakage: comparing the authored text against the writer/01 brief, nothing
copies instruction language, planning labels, selection rules, or an
assignment-fulfilled claim. The one heading using the comma-and shape ("What
attention became, and what it left open") is a single instance, not a repeated
cadence, so it is not a formula. Grammar and syntax are clean throughout,
including display text and furniture.

## Reader

Read straight through as the declared ML engineer. What the piece gives beyond its
sources, in one sentence: a rebuilt, reasoned-from account of the additive-attention
mechanism joined to a carefully bounded bridge from the 2015 alignment evidence to
the 2019 explanation debate, with the scope mismatch (the debate never ran on this
model) made explicit as the article's own inference. That is exactly the
original-work sentence in draft-handoff.md, and it survives on the page — the Scope
note and verdict carry it visibly rather than gesturing at it. Both answers survive:
the piece is not a restatement of its sources; no single source connects Bahdanau's
Figure 3 to Jain & Wallace / Wiegreffe & Pinter with this scope caveat. The prose
sits closer to the voice-guide exemplars (Weng's incremental notation, Voita's
figure-as-testimony, Recht's bounded verdict) than to a median AI summary: math is
reasoned from, figures are cross-examined, and the verdict commits and marks its own
edge. Reread as the largest claim, the headline ("Attention learned to align long
before it was asked to explain") is defended by the body — alignment came first as a
reading mechanism, the explanation question came years later — and does not overreach
past the plausibility the alignments actually show.

## Edits

None. No direct cuts or prose fixes were required; the declared counts are
unchanged, so no `nb stamp` was run.

## Required work

None.

## Decision

approve — the reconstruction math, all Table 1 figures, and both captured figures
verify against the primary; the explanation-debate bridge is stated honestly as the
article's own bounded inference; the prose is lean, in-register, and free of
leakage, with no publication-blocking issue found.
