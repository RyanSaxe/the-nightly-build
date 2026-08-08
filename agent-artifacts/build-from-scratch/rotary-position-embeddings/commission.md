# Commission: build-from-scratch/rotary-position-embeddings

## Subject
Rebuild **Rotary Position Embeddings (RoPE)** from scratch: the scheme
(Su et al., RoFormer, 2021) that most current open-weight LLMs use to tell a
transformer where each token sits. Start from the smallest thing that
demonstrates the idea and show, in runnable `nb-code`, that rotating query and
key vectors by a position-dependent angle makes the attention score depend only
on the *relative* offset between two tokens, not their absolute indices.

## Why this, why now
Position encoding is the part of a transformer a summary hides: the reader is
told "RoPE encodes relative position" and never sees why a rotation does that or
why it extrapolates to longer contexts than it was trained on. It is squarely
current — RoPE and its context-extension variants (NTK-aware / YaRN scaling) are
the live mechanism behind the long-context race in shipping models. Rebuilding
it exposes an insight hard to get from a description: the dot product of two
rotated vectors is a function of the angle *difference*, so absolute phase
cancels. That single fact is the whole reason the trick works, and it is
checkable in a few lines of code.

## The argument to build (writer/researcher own the exact form)
1. The problem RoPE solves: self-attention is permutation-equivariant, so
   position must be injected. Contrast with the two prior families the reader
   should know by name only (learned absolute embeddings; the original
   sinusoidal additive encoding) — one sentence each, not a history.
2. The construction: split each head's vector into 2-D pairs, rotate pair `i` by
   angle `m * theta_i` where `m` is the token index and `theta_i` is a fixed
   geometric frequency. Set the math the reconstruction leans on (the 2-D
   rotation, the relative-offset identity `<R_m q, R_n k> = <q, R_{n-m} k>`)
   rather than paraphrasing it.
3. The demonstration in `nb-code`: implement `rope(x, positions)` as pure array
   math; show numerically that attention logits between two tokens are invariant
   to a shared shift of both positions (relative-only), and that they decay with
   distance. A small figure/table from the code the reader could reproduce.
4. Compare the prototype to the real system: how production RoPE differs
   (applied per head to q/k only, interleaved-vs-half-split conventions, the
   base `theta` = 10000, and the one-line change that yields NTK/YaRN context
   extension). Say honestly what the toy leaves out.

## Boundaries
- `article` template; word band 1500-4500; min_sources 8 (template floor).
- This is an engineering rebuild, not a survey of position encodings and not a
  paper review. Keep it to RoPE. Do **not** wander into attention-mechanism
  history or interpretability — the paper-of-the-day piece in today's edition
  (Bahdanau 2014 attention) owns attention's origins; this piece owns position.
- Code carries the argument: it must run and its output must be shown honestly
  (real numbers from a real run, per the code furniture and spec/charts.md if a
  chart is used). No invented benchmark numbers.
- Sources should include the primary artifacts: the RoFormer paper, the YaRN
  paper (Peng et al.) or the NTK-aware scaling primary write-up, and at least one
  reference implementation or model config showing `theta`/scaling in the wild.

## Neighbors in this run (coherence / non-redundancy)
Seven articles today. The only adjacent one is paper-of-the-day
(neural-machine-translation-attention). Division of territory: **this piece =
positional encoding by rotation; that piece = the origin and after-record of the
attention mechanism.** Neither recaps the other's subject.

## Habits not to inherit (recent build-from-scratch)
Recent BFS: speculative-decoding, byte-pair-encoding. Both opened on a
mechanism-as-subject headline and a dek that reports an empirical result from a
"trained/run from scratch on N units" reproduction ("Two hand-built models run
two hundred thousand times…"; "…trained from scratch on 617 bytes…"). Break that
dek mold: find a fresh way to state RoPE's surprise, not "a tiny reimplementation
confirms X." Vary section-heading shape from those pieces.

## Production
Harness: claude-code, isolated role subagents. Models by resolved policy —
writing-coach (low effort), researcher (high effort), writer (medium effort) at
the capable tier; editor (high effort) required, inherits. No policy deviation.
The writer sets `nb-meta` harness/model to match the current published library
exactly.
