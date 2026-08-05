# draft-handoff: paper-of-the-day/denoising-diffusion (03) — revision

## Original work

Unchanged from writer/02: the reconstruction stages DDPM's derivation around a
single fork the paper treats as routine — predict the mean versus predict the
noise — and shows the headline result is the consequence of taking the noise
branch and then *discarding* the weight the same derivation produced, defended
by the paper's own ablation (FID 13.51 vs 3.17) rather than by algebra.

## Editorial requests resolved (editor/01)

- **(blocking) asset-2 caption honesty** — Added a factual note to the Fig. 2
  (LSUN Church) caption recording that the top-left sample carries a legible
  "www.shutterstock.com 193883335" watermark present in the paper's own
  Figure 3; the caption stays a factual label. The memorization interpretation
  now lives in one what-it-measured prose sentence ("One of those Church samples
  reproduces a stock-photo watermark from the training set intact, a visible
  instance of the training-data memorization these models can exhibit at this
  resolution"). The asset was not recropped or edited.
- **(minor) heading cadence** — Reshaped the verdict heading from the comma-and
  triad "A training recipe, not a new model, and the recipe was right" to the
  shorter, differently-shaped "A training recipe the whole field kept," so it no
  longer mirrors "Strong samples, a likelihood that lost, and a cost left
  unnamed." This also thins one non-load-bearing "not X" contrast; the
  recipe-not-model point is still carried by the body ("That is a training
  recipe, not a model family"). No new formula introduced.

Nothing else changed: verified equations, numbers, assets, and the editor's own
verdict cut are preserved.

## Proof result

`./nb check ... --series paper-of-the-day --library <checkout>` (links included):
**BLOCK: 0, WARN: 5, verdict PUBLISHABLE.** `nb stamp` updated words 2711 → 2750.

## Warnings intentionally left (all 5)

Unchanged from writer/02: all five remaining W-SENTENCE-DENSITY warnings fall on
verbatim display-equation LaTeX inside `<div class="nb-math-eq">` (Eq. 4, Eq. 5,
Eq. 6-7, Eq. 12, Eq. 14), which the density heuristic scores as one long
"sentence" because that div is not a skip tag. Splitting them would corrupt the
math. The two prose sentences added this pass introduced no new warning; the
count held at 5.
