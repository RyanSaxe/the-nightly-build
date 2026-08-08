# Commission: paper-of-the-day/neural-machine-translation-attention

## Subject
**Bahdanau, Cho, and Bengio, "Neural Machine Translation by Jointly Learning to
Align and Translate" (2014/2015, arXiv:1409.0473).** The paper that introduced
the attention mechanism: an encoder-decoder that, instead of squeezing a whole
source sentence into one fixed vector, learns a soft *alignment* and reads a
different weighted combination of the source at each output step.

## Why this paper, why now
It has exactly the after-record the series wants. The mechanism it introduced
(content-based soft attention) outlived the architecture it was introduced in
(the RNN encoder-decoder that Transformers replaced), so reading it now with the
abstract set aside is instructive: attention was born as an *alignment* device
with a concrete linguistic reading, and the field later argued about whether
those weights explain anything at all (Jain & Wallace, "Attention is not
Explanation," 2019; Wiegreffe & Pinter, "Attention is not not Explanation,"
2019). That live dispute is the "what happened next" the piece weighs the
original claim against. Rebuilding the alignment idea from the paper's own math
clarifies an active problem: what attention weights are and are not evidence of.

## The reconstruction to build (writer/researcher own exact form)
- Set the math the paper turns on, not a paraphrase: the fixed-context
  bottleneck of the prior Cho/Sutskever encoder-decoder, then Bahdanau's
  context vector `c_i = sum_j alpha_ij h_j` with the alignment weights
  `alpha_ij = softmax(e_ij)` and the additive score
  `e_ij = v^T tanh(W s_{i-1} + U h_j)`. Explain each term for the declared
  ML reader.
- Bring in the paper's own figures as source assets and say what each settles:
  (a) the alignment-matrix visualization (their Fig. 3) showing near-diagonal
  alignment with the documented non-monotonic reorderings (the French
  adjective-noun swap), and (b) the BLEU-vs-sentence-length curve (their Fig. 2)
  showing the fixed-vector model degrading on long sentences while the attention
  model holds. These are the claim's strongest material; do not merely describe
  them.
- The verdict as a reviewer would write it: what the paper established (soft
  alignment lifts the long-sentence bottleneck, learned end to end), and how the
  later record reframes the alignment reading — attention weights are a useful
  computational device whose status as *explanation* is contested.

## Boundaries
- `paper` template; word band 1800-3400; min_sources 8 (template floor).
- Stay in the paper and its documented after-record. The mechanics of *position*
  encoding are out of scope — today's build-from-scratch piece (RoPE) owns that.
  This piece owns attention/alignment and the explanation debate.
- Source assets must be captured from the actual primary documents via `nb asset`
  with factual cited captions; no external image URLs, no invented figures.
- Report figures (BLEU, RNNsearch vs RNNenc) against the paper's own tables.

## Neighbors in this run
Seven articles today; the only ML-adjacent neighbor is build-from-scratch/RoPE.
Territory split as above (position vs attention). No other overlap.

## Habits not to inherit (recent paper-of-the-day)
Recent PoD deks nearly all open on author surnames + verb and close on an
"the after-record narrows/reframes it" clause ("Ho, Jain, and Abbeel reached…
and every later model inherited…"; "Belkin and Nakkiran rebuilt… and the
after-record narrows it…"). Do not reuse that dek skeleton. Headlines have been
sharp single claims; find this piece's own claim (something the alignment-vs-
explanation record actually supports), not a formula. Vary heading shapes from
the recent run.

## Production
Harness: claude-code, isolated role subagents. Models by resolved policy —
writing-coach (low), researcher (high), writer (medium) at capable tier; editor
(high) required, inherits. No deviation. Writer sets `nb-meta` harness/model to
match the current published library exactly.
