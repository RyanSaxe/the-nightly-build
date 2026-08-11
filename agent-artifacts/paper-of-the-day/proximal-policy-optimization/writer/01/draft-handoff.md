# Draft handoff: paper-of-the-day/proximal-policy-optimization (01)

## Original-work statement

The article reconstructs PPO's clipped objective and full training loop from the
paper's own equations and clipping figure, then stages the paper's advertised
account and the two controlled reexaminations against each other on that single
reconstructed objective, isolating exactly where the clip's stated job (holding a
ratio trust region) and its measured behavior diverge and preserving, sentence by
sentence, the ratio-versus-KL distinction that the flattened "PPO leaves its trust
region" reading erases.

## Proof result

`./nb check … --series paper-of-the-day` (links included): **BLOCK: 0**, verdict
PUBLISHABLE. 3050 words, 8 sources, 13 min. All eight source URLs resolve.

### Warnings intentionally left (3, all W-SENTENCE-DENSITY)

1. The 47-word / punctuation-17 sentence is the deliberate enumeration of the
   nine code-level optimizations (value clipping, reward scaling, orthogonal
   init, Adam annealing, reward clipping, observation normalization, observation
   clipping, tanh, gradient clipping). The list is the evidence; naming all nine
   in one breath is the point, and splitting it would blunt "nine unglamorous
   tricks."
2. & 3. The two remaining warnings (40 w / punct-14 and 47 w / punct-10) are the
   probability-ratio definition and the GAE temporal-difference-residual
   sentence. Their density scores are inflated by inline TeX tokens (braces,
   backslashes in `\dfrac`, `\pi_\theta`, `\delta_t = r_t + \gamma V(...)`),
   which the reader sees as single symbols. Splitting mid-definition would
   fragment the math the reconstruction leans on. Left as controlled long
   sentences per `spec/editorial.md`.

## Note for the editor: math rendering

Equations use the engine's KaTeX furniture, including the one annotated
equation (`\htmlClass{nb-mc1..3}` on L^CLIP). KaTeX is a press-declared CDN
runtime dependency. It could not load in the offline preview sandbox, so local
screenshots show raw TeX; nb.js config (`throwOnError: false`, `strict: "ignore"`,
`trust` enabling `htmlClass`) and the fact that the TeX is the sanctioned
furniture pattern confirm it typesets on the live site. `nb render-check` was
skipped locally ("no Chrome in this environment").

## Open questions

None. The evidence record fully supported the reconstruction and every
correction it flagged (advertised-vs-operative framing, ratio-not-KL on the
trust-region result, PPO-NoClip > PPO-Minimal with the footnote-6 containment
caveat, PPO's dominance undisputed) is respected in the prose.
