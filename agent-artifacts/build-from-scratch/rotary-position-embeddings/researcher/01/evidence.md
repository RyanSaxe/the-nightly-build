# Evidence record: build-from-scratch/rotary-position-embeddings (01)

The evidence fully supports the article's core mechanical argument. The
RoFormer paper (Su et al., 2021) states the RoPE construction the piece rebuilds
in exact, locatable equations: the 2-D rotation (Eq. 13), the block-diagonal
d-dimensional matrix with the frequency schedule `theta_i = 10000^(-2(i-1)/d)`
(Eq. 15), and the relative-offset property the whole trick rests on
(the constraint in Eq. 11, that the query-key inner product equals a function
`g(x_m, x_n, m-n)` of the offset alone). The long-term decay claim is proven, not
asserted (Section 3.4.3, bound at Eq. 37, via Abel summation). Two independent
production reference implementations pin down the two conventions the commission
names: Meta's original Llama code interleaves adjacent dimensions into complex
pairs, while HuggingFace's `rotate_half` uses the half-split convention — these
are genuinely different orderings, reconciled by a weight permutation at
conversion, and this is a real trap the article should flag. The base constant
`10000` is confirmed in the paper and in a shipping config (Mistral-7B-v0.1),
and its variance in the wild is confirmed (Llama-3-8B ships `rope_theta` =
500000). Context extension is well-sourced from the YaRN paper (Peng et al.,
2023) for the formal one-line base change (`b' = b·s^(|D|/(|D|-2))`, Eq. 16) and
its honest cost (Llama 2 to 128k on ~0.1% of pretraining tokens).

Where the evidence is thin: (1) the original NTK-aware write-up is a June 2023
Reddit post by bloc97 that could not be fetched through the automated tools
(Reddit is blocked; the archiving GitHub issue does not reproduce the code). The
formula and claim are recorded from YaRN's formalization and a search snippet,
not from the origin post read in full — flagged below. (2) The commission's
"decays with distance" demonstration is proven in RoFormer for the paper's
construction, but the article's own toy numbers (a specific decay curve, the
shift-invariance of logits) must come from the article's `nb-code` run, not from
any figure captured here. (3) On *why* RoPE extrapolates, the record carries a
genuine contradiction (below): the RoFormer abstract's "flexibility of sequence
length" is contradicted by the ALiBi paper's measurement that rotary does *not*
extrapolate efficiently, and the community explanations for what base-scaling
fixes do not agree.

## Sources

```text
URL:         https://arxiv.org/abs/2104.09864
Kind:        primary — this is the paper that introduces and owns RoPE
             (Su, Lu, Pan, Murtadha, Wen, Liu; "RoFormer: Enhanced Transformer
             with Rotary Position Embedding"; v1 Apr 2021, v5 last revised
             Nov 2023).
Establishes: the full RoPE construction, the relative-position property, the
             frequency schedule, and the long-term decay property, firsthand.
Paraphrase:  RoPE encodes absolute position by multiplying the query/key
             projection of a token at index m by a rotation matrix whose angle
             grows linearly in m; the paper proves this makes the query-key
             inner product depend only on the relative offset. Each 2-D
             coordinate pair is rotated by a fixed per-pair frequency, and the
             frequencies form a geometric schedule set by the constant 10000.
Locators:    Eq. 11 (the design constraint <f_q(x_m,m), f_k(x_n,n)> =
             g(x_m, x_n, m-n)); Eq. 13 (the 2-D solution: the
             [[cos m theta, -sin m theta],[sin m theta, cos m theta]] matrix
             times W_q x_m); Eq. 15 (the block-diagonal R^d_{Theta,m} built from
             d/2 such 2x2 blocks); the set Theta = {theta_i = 10000^(-2(i-1)/d),
             i in [1,...,d/2]} defined immediately after Eq. 15; Section 3.4.3
             and Eq. 37 (long-term decay upper bound, derived by Abel
             summation); Section 1 introduction (self-attention is
             "position-agnostic", citing Yun et al. 2020).
Quote:       "encodes the absolute position with a rotation matrix and meanwhile
             incorporates the explicit relative position dependency in
             self-attention formulation." (abstract) — the decay claim: the
             inner product "will decay when the relative position increase."
             (Section 3.3 heading/text)
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — "Attention Is All You Need" (Vaswani et al., 2017) owns
             the sinusoidal additive encoding and the learned-embedding baseline.
Establishes: the two prior families the commission names for one-sentence
             contrast: the original sinusoidal *additive* encoding, and learned
             absolute embeddings.
Paraphrase:  Positions are encoded by adding fixed sinusoids of geometrically
             spaced wavelengths to the input embeddings; the authors also tried
             learned positional embeddings and found the two nearly identical in
             quality. They chose sinusoids partly on the hypothesis that a fixed
             offset k makes PE(pos+k) a linear function of PE(pos), which might
             help the model attend by relative position.
Locators:    Section 3.5. PE(pos,2i) = sin(pos/10000^(2i/d_model));
             PE(pos,2i+1) = cos(pos/10000^(2i/d_model)); Table 3 row (E) for the
             learned-vs-sinusoidal comparison.
Quote:       "The wavelengths form a geometric progression from 2π to 10000·2π."
             "We also experimented with using learned positional embeddings ...
             and found that the two versions produced nearly identical results."
             "we hypothesized it would allow the model to easily learn to attend
             by relative positions, since for any fixed offset k, PE(pos+k) can
             be represented as a linear function of PE(pos)."
```

```text
URL:         https://arxiv.org/abs/2309.00071
Kind:        primary — YaRN (Peng, Quesnelle, Fan, Shippole, 2023) owns the YaRN
             method and formalizes NTK-aware / NTK-by-parts base scaling.
Establishes: the one-change context-extension family and its honest cost;
             the formal statement of the NTK-aware base change originally from
             bloc97; the interpolation/extrapolation framing.
Paraphrase:  Position Interpolation linearly rescales positions by s = L'/L
             (extended length over original), which loses high-frequency detail.
             NTK-aware instead changes only the RoPE base: b' = b·s^(|D|/(|D|-2)),
             stretching low frequencies more and high frequencies less. YaRN
             combines an "NTK-by-parts" schedule (rotate high-frequency pairs
             unchanged, interpolate low-frequency pairs, ramp between with
             alpha=1, beta=32 for Llama) with an attention-temperature factor
             sqrt(1/t) = 0.1·ln(s) + 1. It extends Llama 2 to long context with a
             fraction of the training prior methods needed.
Locators:    Section 2.2 / Eq. 10 (Position Interpolation baseline, s = L'/L);
             Section 3.1 / Eq. 16 (NTK-aware base b' = b·s^(|D|/(|D|-2)));
             Section 3.2 / Eqs. 17-20 (NTK-by-parts: wavelength lambda_d =
             2π·b^(2d/|D|), ratio r(d) = L/lambda_d, ramp gamma, mixed
             frequencies); Section 3.4 / Eqs. 21-22 (temperature scaling);
             Section 4 (experiments); Table 2 (Proof-pile perplexity).
Quote:       requires "10x less tokens and 2.5x less training steps than previous
             methods" (abstract).
```

```text
URL:         https://github.com/meta-llama/llama/blob/main/llama/model.py
Kind:        primary — Meta's official reference Llama implementation; it owns
             the "interleaved" application convention it ships.
Establishes: (a) the base constant 10000.0 in production; (b) the interleaved
             pairing convention (adjacent dims 2i, 2i+1 form each rotated pair).
Paraphrase:  `precompute_freqs_cis(dim, ..., theta=10000.0)` builds
             `freqs = 1.0 / (theta ** (arange(0, dim, 2)/dim))`. `apply_rotary_emb`
             reshapes q/k with `reshape(*shape, -1, 2)` and calls
             `torch.view_as_complex`, so consecutive coordinate pairs (2i, 2i+1)
             are the rotated 2-D pairs. RoPE is applied to q and k only, per head.
Locators:    functions `precompute_freqs_cis` and `apply_rotary_emb`.
Quote:       `freqs = 1.0 / (theta ** (torch.arange(0, dim, 2)[: (dim // 2)].float() / dim))`
             `xq_ = torch.view_as_complex(xq.float().reshape(*xq.shape[:-1], -1, 2))`
```

```text
URL:         https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/modeling_llama.py
Kind:        primary — the HuggingFace Transformers Llama implementation; it owns
             the "half-split" application convention used across the HF ecosystem.
Establishes: the half-split convention: pair coordinate i with coordinate i+d/2,
             not with i+1. Numerically different ordering from Meta's, reconciled
             by permuting the q/k projection weights at checkpoint conversion.
Paraphrase:  `rotate_half(x)` sets x1 = first half, x2 = second half, returns
             cat(-x2, x1); `apply_rotary_pos_emb` computes q*cos +
             rotate_half(q)*sin. `inv_freq = 1.0 / (base ** (arange(0, dim, 2)/dim))`.
Locators:    functions `rotate_half`, `apply_rotary_pos_emb`,
             `LlamaRotaryEmbedding`.
Quote:       `def rotate_half(x): x1 = x[..., : x.shape[-1] // 2]; x2 = x[..., x.shape[-1] // 2 :]; return torch.cat((-x2, x1), dim=-1)`
             `q_embed = (q * cos) + (rotate_half(q) * sin)`
```

```text
URL:         https://huggingface.co/mistralai/Mistral-7B-v0.1/blob/main/config.json
Kind:        primary — a shipped open-weight model's own config file.
Establishes: the base 10000 in a real released model, and its head geometry, for
             a concrete worked example.
Paraphrase:  Mistral-7B-v0.1 ships rope_theta = 10000.0 with hidden_size 4096,
             32 attention heads (head_dim = 128, so 64 rotated pairs per head),
             and max_position_embeddings 32768.
Locators:    top-level keys rope_theta, hidden_size, num_attention_heads,
             max_position_embeddings.
Quote:       rope_theta: 10000.0
```

```text
URL:         https://huggingface.co/NousResearch/Meta-Llama-3-8B/blob/main/config.json
Kind:        primary — an open (non-gated mirror) copy of Meta-Llama-3-8B's own
             config file, used only to read the shipped hyperparameters.
Establishes: that the base is tuned per model in production — it is not always
             10000. Llama 3 ships a far larger base.
Paraphrase:  Llama-3-8B ships rope_theta = 500000.0, hidden_size 4096, 32
             attention heads, max_position_embeddings 8192.
Locators:    top-level keys rope_theta, max_position_embeddings.
Quote:       rope_theta: 500000.0
```

```text
URL:         https://huggingface.co/NousResearch/Llama-2-7b-hf/blob/main/config.json
Kind:        primary — an open mirror of Llama-2-7B's own config file.
Establishes: the head geometry of the model YaRN extends, and that Llama 2's
             config leaves rope_theta at the 10000 default (the key is absent).
Paraphrase:  Llama-2-7B: hidden_size 4096, 32 heads (head_dim 128), 32 layers,
             max_position_embeddings 4096; rope_theta not set (defaults to
             10000). This is the 4096-token model YaRN extends to 64k/128k.
Locators:    top-level keys hidden_size, num_attention_heads, num_hidden_layers,
             max_position_embeddings.
Quote:       max_position_embeddings: 4096
```

```text
URL:         https://arxiv.org/abs/2108.12409
Kind:        primary — the ALiBi paper (Press, Smith, Lewis, 2021) owns this
             extrapolation measurement.
Establishes: the honest, contrary fact that RoPE does NOT extrapolate
             efficiently beyond its training length without modification.
Paraphrase:  Measuring perplexity as inference length exceeds training length,
             rotary embeddings extend usefully only a short way past the training
             window — trained at L=512, a rotary model improves perplexity for
             only ~200 additional tokens before degrading — better than
             sinusoidal (~20-50) but far short of efficient extrapolation. This
             is the empirical backdrop that motivates the NTK/YaRN base changes.
Locators:    Section 2.2 "Measuring Extrapolation" and its perplexity figures.
Quote:       "current methods do not allow for efficient extrapolation."
```

```text
URL:         https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/
Kind:        primary (origin) — bloc97's June 2023 post is the origin of the
             NTK-aware base-scaling trick. NOT read firsthand: Reddit is
             unreachable through the automated fetch tools, and the archiving
             GitHub issue (huggingface/text-generation-inference #512) does not
             reproduce the code. Its content here is carried by YaRN's Eq. 16
             (a peer primary that formalizes it) and a search-result summary.
Establishes: the claim that changing only the RoPE base extends Llama context
             with NO fine-tuning; the origin of the "NTK-aware" name.
Paraphrase:  Changing ~3 lines — scaling the RoPE base by an alpha factor
             (reported alpha=8 to reach 8k+ from the 2048 training window) —
             extends context "without any fine-tuning and minimal perplexity
             degradation." The formal base change is b' = b·s^(|D|/(|D|-2))
             (YaRN Eq. 16).
Locators:    the r/LocalLLaMA post body and its linked Colab (not accessed).
Quote:       (title, verified) "NTK-Aware Scaled RoPE allows LLaMA models to have
             extended (8k+) context size without any fine-tuning and minimal
             perplexity degradation."
```

## Contradictions

- RoFormer's abstract sells "flexibility of sequence length," and the paper
  proves clean relative-position behavior and decay. That is not the same as
  usable long-context extrapolation, and the ALiBi paper (arXiv:2108.12409,
  Section 2.2) measures directly that rotary embeddings do NOT extrapolate
  efficiently past training length. Both are true and the article must not let
  the first imply the second: RoPE gives *relative* position exactly, but a model
  trained at length L still degrades well before large multiples of L without a
  base change. This is precisely why the NTK/YaRN line of work exists.

- The community does not agree on *why* base-scaling fixes extrapolation. YaRN
  (Section 3.1) frames it as recovering "high frequency information" lost when
  Position Interpolation compresses all dimensions equally (an NTK-theory
  argument). A separate line (e.g. the "Frequency Bands in RoPE" work,
  openreview.net/forum?id=PR1PPxvG9Q; and RoFormer author Su Jianlin's own
  blog derivations) frames it as a trade-off in which raising theta improves
  interpolation *within* the training length but can hurt extrapolation *beyond*
  it — the opposite of the naive "bigger base is always better" intuition. The
  article should present base-scaling as the mechanism and flag that the precise
  explanation for its success is contested, not settled. (These competing-cause
  sources are noted for honesty, not read in full; if the piece leans on the
  contested-explanation point it should cite one of them read directly.)

- Interleaved vs half-split is not a cosmetic detail: Meta's model.py rotates
  adjacent pairs (2i, 2i+1) while HF's rotate_half pairs (i, i+d/2). Applied to
  the same weights they give different results; the HF checkpoint conversion
  permutes the q/k projection rows so the two produce equivalent attention. A toy
  built one way is not drop-in compatible with weights exported for the other.
  Both implementations are cited above; the reconciling permutation lives in the
  HF Llama weight-conversion script (not separately fetched — state it as a known
  conversion step, not a measured claim, unless the writer opens that script).

## Numbers

```text
Figure: theta_i = 10000^(-2(i-1)/d),  i in [1, ..., d/2]
Owner:  RoFormer (arXiv:2104.09864), the set defined after Eq. 15.
Scope:  d = per-head dimension; d/2 independent 2-D rotation frequencies.
```

```text
Figure: base constant = 10000
Owner:  RoFormer (Eq. 15) and "Attention Is All You Need" (Section 3.5);
        confirmed in production as rope_theta = 10000.0 in Mistral-7B-v0.1
        and theta = 10000.0 in Meta's llama/model.py.
Scope:  the base of the geometric frequency schedule; sinusoidal wavelengths
        span a geometric progression from 2π to 10000·2π.
```

```text
Figure: rope_theta = 500000.0
Owner:  Meta-Llama-3-8B config.json (NousResearch mirror).
Scope:  a shipped model's RoPE base — evidence the base is tuned per model,
        not fixed at 10000. max_position_embeddings = 8192.
```

```text
Figure: rope_theta = 10000.0; max_position_embeddings = 32768
Owner:  Mistral-7B-v0.1 config.json.
Scope:  hidden_size 4096, 32 heads => head_dim 128 => 64 rotated pairs per head.
```

```text
Figure: Llama-2-7B: hidden 4096, 32 heads, head_dim 128, ctx 4096
Owner:  Llama-2-7b-hf config.json (NousResearch mirror).
Scope:  the base model YaRN extends; a concrete d and pair count for the toy.
```

```text
Figure: NTK-aware modified base b' = b · s^(|D|/(|D|-2)),  s = L'/L
Owner:  YaRN Eq. 16 (formalizing bloc97's NTK-aware post).
Scope:  |D| = head dimension; single scalar change to the base recomputes all
        inv_freq. Origin post reports alpha=8 to reach 8k+ from 2048 with no
        fine-tuning (bloc97, not read firsthand).
```

```text
Figure: Llama 2 extended 4096 -> 64k (s=16) and -> 128k (s=32)
Owner:  YaRN Section 4.
Scope:  fine-tune ~400 steps (s=16) + ~200 more (s=32), ~400M tokens,
        ~0.1% of pretraining; "10x less tokens, 2.5x less steps" vs prior
        methods. Proof-pile perplexity (Table 2) stays low out to 128k
        (e.g. Llama 2 7B + YaRN s=32 around 2.37 at 128k tokens).
```

```text
Figure: YaRN attention temperature sqrt(1/t) = 0.1 · ln(s) + 1
Owner:  YaRN Eq. 22.
Scope:  scalar on the pre-softmax logits; NTK-by-parts ramp alpha=1, beta=32.
```

```text
Figure: rotary extrapolation reach ~200 tokens beyond L=512 training
Owner:  ALiBi (arXiv:2108.12409, Section 2.2).
Scope:  perplexity stops improving ~200 tokens past training length for rotary
        (vs ~20-50 for sinusoidal); the honest ceiling on naive extrapolation.
```

## Source assets

The commission and brief state the demonstration is the article's own `nb-code`
output, not a captured paper figure. The named assets below are candidates only;
prefer generating equivalents from the article's run.

```text
Asset: RoFormer Figure 1 (the schematic of applying rotary position embedding /
       rotating 2-D coordinate pairs by position-dependent angle).
Shows: the geometric picture of "rotate each pair by m·theta_i" the article
       teaches. Useful as intuition, but a reader-reproducible SVG/plot from the
       article's own code is preferable and the template favors that.
Crop:  must retain the position-scaled rotation of at least two different-
       frequency pairs; omit surrounding paper layout.
```

```text
Asset: RoFormer Figure 2 (long-term decay of the inner product vs relative
       distance).
Shows: the decay-with-distance property the commission's demo point 3 must
       exhibit. The article should instead produce its own decay curve from
       rope() output to keep numbers honest and reproducible.
Crop:  keep both axes labeled (relative distance vs inner-product magnitude).
```

```text
Asset: YaRN Table 2 / the perplexity-vs-context-length figure.
Shows: that base-scaled context extension holds perplexity out to 128k. Useful
       to cite as a number in the "compare to the real system" section, not to
       reproduce (it is a training result the toy cannot rerun).
Crop:  n/a — cite the figure/number; do not reproduce a training result.
```

Otherwise: None found. The relative-only-invariance demonstration and the
decay demonstration are expected to be the article's own array-math output.

## Discarded

```text
URL: https://huggingface.co/meta-llama/Llama-2-7b-hf/raw/main/config.json — gated
     (HTTP 401); used the open NousResearch mirror of the same config instead.
URL: https://huggingface.co/meta-llama/Meta-Llama-3-8B/raw/main/config.json — gated
     (HTTP 401); used the open NousResearch mirror of the same config instead.
URL: https://github.com/huggingface/text-generation-inference/issues/512 — archives
     the NTK-aware claim but does not reproduce the code/formula; kept only as a
     pointer, not cited for the mechanism.
URL: https://github.com/jquesnelle/yarn (scaled_rope source file) — target file
     path 404'd; the NTK/YaRN formulas are taken from the YaRN paper itself
     (primary) rather than the repo.
```
