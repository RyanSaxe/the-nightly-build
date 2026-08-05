# draft-handoff: paper-of-the-day/denoising-diffusion (02)

## Original work

The reconstruction stages DDPM's derivation around a single fork the paper
itself treats as routine — predict the mean versus predict the noise — and shows
that the paper's headline result is the consequence of taking the noise branch
and then *discarding* the weight the same derivation produced, defended by the
paper's own ablation (FID 13.51 vs 3.17) rather than by algebra.

## Proof result

`./nb check ... --series paper-of-the-day --library <checkout>` (links included):
**BLOCK: 0, WARN: 5, verdict PUBLISHABLE.**

## Warnings intentionally left (all 5)

All five remaining W-SENTENCE-DENSITY warnings fall on **equation furniture, not
prose**. The density heuristic splits text on sentence punctuation and counts
words plus internal punctuation; the documented equation markup places verbatim
LaTeX inside `<figure class="nb-math"><div class="nb-math-eq">…</div>`, and that
`div` is not among the parser's `SENTENCE_SKIP_TAGS` (`math`, `code`, `pre`, …),
so each display equation's TeX source is scored as one long "sentence." The five
flagged strings are the verbatim equations, transcribed from the evidence:

1. 42w — closed-form marginal `q(x_t|x_0)` with the `x_t = √ᾱ_t x_0 + √(1-ᾱ_t)ε`
   reparameterization (Eq. 4).
2. 72w — the variational-bound decomposition with the `L_T / L_{t-1} / L_0`
   underbraces (Eq. 5).
3. 46w — the tractable forward posterior `q(x_{t-1}|x_t,x_0)` with `β̃_t` (Eq. 6-7).
4. 46w — the weighted noise-prediction term with the exact step coefficient (Eq. 12).
5. 47w — `L_simple`, the annotated objective with `\htmlClass{nb-mc*}` term spans (Eq. 14).

These stand because they are load-bearing equations reproduced verbatim from the
paper; "splitting" them would corrupt the math, and the markup is the one the
engine's own furniture catalog prescribes. The CI render-probe verifies these
typeset correctly downstream.

The **one** genuine prose sentence the heuristic flagged in the prior build (a
55-word sentence in the noise-objective section) was **split** into three plain
sentences, clearing that warning.

## Notes for the editor

- All equations verified verbatim against the evidence record (Eq. 1, 2, 4, 5,
  6-7, 8, 11, 12, 14; Algorithms 1-2 as the source asset). Every number checked
  against the evidence: CIFAR-10 FID 3.17 / IS 9.46; ablation 13.51 / 7.67;
  NLL ≤ 3.75 (L_simple) vs ≤ 3.70 (fixed-Σ bound variant); Table 1 baselines
  (NCSN 25.32/8.87, SNGAN 21.7/8.22, SNGAN-DDLS 15.42/9.09, StyleGAN2+ADA
  3.26/9.74); LSUN Church 7.89 and Bedroom 4.90 in captions; Score-SDE 2.20.
- The two source assets read correctly: asset-1 is the Algorithm 1 (Training) /
  Algorithm 2 (Sampling) box pair; asset-2 is the LSUN Church 256×256 sample grid
  captioned FID 7.89. The visible watermark fragment in one asset-2 cell is the
  known DDPM artifact of LSUN samples reproducing training-set watermarks, not a
  captioning error; the caption attributes the grid and its FID to Fig. 3.
- Display-text pass: nb-meta `dek` is identical to the rendered dekline; headline
  and dek carry no colon-subtitle; the body byline was corrected from "14 min
  read" to "12 min read" to match the stamped `reading_minutes`.

## Open questions

None. No new evidence was needed; the claim set is unchanged from writer/01.
