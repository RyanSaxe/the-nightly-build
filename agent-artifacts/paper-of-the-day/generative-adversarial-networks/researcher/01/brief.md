# Researcher brief: paper-of-the-day/generative-adversarial-networks (01)

## Your job
Produce `evidence.md` here: the verified evidence record for a `paper` article on
Goodfellow et al., "Generative Adversarial Nets" (2014). The writer rebuilds the
claim only from what you verify; the editor will reopen the math.

## Begin with these inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.

## What to read and verify (open the actual papers)
1. **The GAN paper** (arXiv:1406.2661 / NIPS 2014). Record exactly:
   - the value function V(D,G) = E_{x~p_data}[log D(x)] + E_{z~p_z}[log(1-D(G(z)))];
   - Proposition/Theorem: the optimal discriminator D*_G(x) = p_data(x)/(p_data(x)+p_g(x)),
     and that the global optimum of the training criterion is p_g = p_data, at
     value -log 4, with the criterion reducing to a Jensen-Shannon divergence
     term. Capture the exact statements and where in the paper they sit
     (section/eq numbers).
   - the non-saturating trick: training G to maximize log D(G(z)) instead of
     minimizing log(1-D(G(z))) "early in learning," and the paper's stated reason.
   - what experiments/datasets the paper actually ran (MNIST, TFD, CIFAR-10) and
     how it evaluated (Parzen-window log-likelihood) — and the paper's own caveats.
   - exact author names and affiliations (Université de Montréal, etc.).
2. **WGAN** (Arjovsky, Chintala, Bottou, arXiv:1701.07875). Record its diagnosis
   of the original loss (JS divergence gives no usable gradient when supports are
   disjoint / discriminator is near-optimal → vanishing gradients), what it
   replaces the objective with (Earth-Mover / Wasserstein-1 distance), and any
   exact claims/figures you cite.
3. **"Are GANs Created Equal?"** (Lucic et al., arXiv:1711.10337). Record its
   finding on whether variants beat the original under a fair compute/tuning
   budget, the metrics used (FID/precision-recall), and exact wording of the
   conclusion.
4. **Mode collapse / instability**: one or two authoritative primary/secondary
   sources documenting these failure modes with specifics.
5. **What happened next**: a verifiable, dated marker that diffusion models
   displaced GANs for much image generation (e.g. Dhariwal & Nichol,
   "Diffusion Models Beat GANs on Image Synthesis," arXiv:2105.05233 — record its
   exact claim/FID comparison). Keep this proportionate; it is context, not the
   subject.

## Contradictions / Numbers
Record disagreements (e.g. defenders of the original non-saturating loss vs the
WGAN critique; whether Lucic et al. undercuts specific later claims). In Numbers,
capture the exact figures you cite (the -log 4 optimum value; any FID numbers;
dataset sizes) with owning primary, unit, and period.

## Source assets
Note whether an exact visual from a cited primary would carry the argument (e.g.
the GAN paper's Figure 1 schematic of the minimax game, or its sample grids), or
`None found`. Do not prescribe crops.

## Constraints
Minimum 8 sources; classify each primary/secondary with a reason (the paper owns
its own claims; an explainer is secondary). Every equation and number verified
against the owning primary. Every URL resolves; arXiv is reachable.

Return `DONE researcher <path>`; `BLOCKED researcher <reason>` if a primary is
unreachable; `REQUEST orchestrator <need>` for a commission gap.
