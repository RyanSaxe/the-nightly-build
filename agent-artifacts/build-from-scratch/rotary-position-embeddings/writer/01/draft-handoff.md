# Draft handoff: build-from-scratch/rotary-position-embeddings (01)

## Original work

Building one `rope()` and reading its real output, the piece pulls apart two
properties the literature usually bundles as "RoPE encodes relative position
with long-term decay": the attention logit is *exactly* relative for every
query-key pair (a shared shift of both positions moves it by at most
1.1e-15, floating-point noise), but it decays with distance *only for aligned
pairs*. Fig. 2 shows the aligned envelope falling to about a fifth of its
starting magnitude across 512 positions while the mean over 2000 random q,k
pairs stays flat. That reframes RoPE's decay as a distance-bound a model may
exploit, not one RoPE imposes, and it grounds the honest limit (exact relative
position is not useful extrapolation) that motivates the base-scaling work.

## Proof

`./nb check … --series build-from-scratch --library <scratch>/library` with
links included: **BLOCK: 0, WARN: 0 — PUBLISHABLE.** No warning left standing.
Also built clean through `nb preview` (article + `chart-1.png` render).
`nb stamp`: words=1922, reading_minutes=8, sources=10.

All demonstration numbers are from a real run (numpy), not invented:
q·k baseline −0.85; gap-3 logit −1.314201 at positions (2,5),(7,10),(100,103);
gap-4 −0.234807; gap-2 −2.146777; shift deviation 1.1e-15; θ₁=1, θ₂=0.01 at
d=4; wavelength stretch ~54k → ~2.56M positions from base 10000 → 500000.
`chart-1.py` is committed beside the article as the decay figure's provenance
and reproduces from array math alone.

## Evidence / attribution notes for the editor

- **Base-scaling "why" is presented as contested but sourced only to YaRN.**
  Per the brief's caution (2), I did not cite the unread competing-cause
  sources (openreview PR1PPxvG9Q; Su Jianlin's blog). The piece states only
  that YaRN motivates the base change through NTK theory while the result is
  measured rather than derived ("argued more than settled"), grounded in YaRN
  itself (s9). If the editor wants a stronger claim that the community
  disagrees on the cause, that needs a researcher pass opening one of those
  sources firsthand — I stopped short rather than cite unread work.

- **NTK-aware origin (s10, bloc97 Reddit) is cited only for its verified title
  claim** (the trick's name and the no-fine-tuning result). The formula
  `b' = b·s^(|D|/(|D|-2))` is attributed to YaRN Eq. 16 (s9), not to the Reddit
  post, which the researcher could not open firsthand. Link-check does not block
  on the Reddit URL (it resolves; restricted, not 404).

- **Config sources use the resolvable NousResearch mirrors** for Llama-2 and
  Llama-3 (the Meta-gated originals 401); Mistral is the official HF page. All
  three link-check clean.

- **Interleaved-vs-half-split reconciliation** (weight permutation at
  conversion) is stated as a known conversion step, not a measured claim, per
  the evidence record — the HF conversion script was not opened.

## Furniture

One annotated equation (the relative-offset identity, the piece's core), two
bare/captioned equations (the 2-D rotation; the YaRN base change), one code
listing (`rope.py`, the toy in full), one table (the shift-invariance run), one
figure (the decay chart), one note ("The limit"). Six flex sections between
orientation and sources.
