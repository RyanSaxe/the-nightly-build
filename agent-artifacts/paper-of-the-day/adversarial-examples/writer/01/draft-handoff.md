# Draft handoff: paper-of-the-day/adversarial-examples (01)

## Original-work sentence
This article re-sequences the paper's linear argument so the max-norm bound and
its growth with dimension come before the algebra, then sets the paper's own
printed self-qualification (adversarial error cut to 17.9% but still 81.4%
confident when wrong) beside the pockets-versus-contiguous-regions geometry and
the Ilyas, Tsipras, and Madry record to reach a verdict on which half of
"linearity explains adversarial examples" the following decade kept.

## Proof result
`./nb check` with links on: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. Stamped
words=2421, reading_minutes=11, sources=9. No warnings left standing.

Banned-term counts: em-dash 1 (the verbatim abstract's only; budget 4),
mechanism 0, leverage 0, load-bearing 0. nb-meta `dek` is byte-identical to the
rendered dekline.

## Reconstruction cautions, how each was handled
- The equations are set with the equation furniture, not paraphrased. The
  linear-growth step is the one annotated equation, with epsilon (the bound), m,
  and n each named; the perturbation is written eta = epsilon*sign(w) with growth
  epsilon*m*n, so the paper's bare "sign(w)" is not copied with the epsilon
  dropped. FGSM is eta = epsilon*sign(grad_x J); the adversarial-training
  objective carries alpha = 0.5.
- Figure 1 is a captured source asset (asset-1.png, page 3 clip retaining all
  three panels, the "+ .007 x" and "=" operators, and the per-panel labels and
  confidences), not an external URL. The printed page caption was cropped out;
  the article's caption states what it settles.
- Szegedy 2013 is represented in his own words (the "pockets" quotation in a
  note), and the piece states plainly that the paper's "nonlinearity" framing is
  partly its own construction, without repeating a straw man.
- The reframing is grounded in the paper's own numbers (0.94% -> 0.84% clean,
  89.4% -> 17.9% adversarial, 81.4% confidence when wrong) before the outside
  record weighs in; the linear view's real wins (cheap, gradient-aligned,
  transferable) are conceded before the limits.
- The robustness frontier is presented as a dated checkpoint (Wang et al. 2023,
  70.69% at eps=8/255, then top of RobustBench), not a live leaderboard read.

## One deliberate choice worth a reviewer's eye
The closing stat strip places three CIFAR-10 robust-accuracy figures at the same
eps=8/255 threat model (undefended ~0%, Madry PGD 45.8%, Wang 2023 70.69%) as a
scale of a decade's movement. The attacks behind them differ (PGD vs AutoAttack),
so the strip is a scale anchor rather than a like-for-like table; the prose says
so. If the editor wants strict like-for-like, the undefended and Madry rows can
be restated under AutoAttack, but the order-of-magnitude story is unchanged.

## Open evidence or voice questions
None blocking. All nine sources resolved under the link check.
