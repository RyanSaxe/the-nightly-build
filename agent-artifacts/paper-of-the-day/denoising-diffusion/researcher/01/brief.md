# researcher brief: paper-of-the-day/denoising-diffusion (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/editorial-direction.md — citation standard, series territory, declared reader
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/commission.md — the paper, required reconstruction, math/figure obligations, sourcing

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/researcher/01/evidence.md

Run environment: harness = claude-code, model = capable, high effort. Web search
and fetch available.

Focus:
- Read the focal paper in full: Ho, Jain, Abbeel, "Denoising Diffusion
  Probabilistic Models" (arXiv:2006.11239). Read past the abstract into the
  derivations and appendix. Capture the exact statements the reconstruction needs
  verbatim where wording matters: the abstract (verbatim, for the card); the
  forward process definition and the closed-form q(x_t|x_0) with alpha-bar; the
  reverse parameterization; the reduction of the variational bound to the
  epsilon-prediction objective and the simplified loss L_simple (with the dropped
  weighting term); Algorithm 1 (training) and Algorithm 2 (sampling); and the
  reported metrics (CIFAR-10 FID and Inception score, LSUN, CelebA-HQ),
  each with its exact table location.
- Record which FIGURES/ALGORITHM BOXES are candidate source assets, where they
  live in the paper (figure/page), and what each one settles. Do not prescribe
  crop coordinates.
- Establish the lineage and public record with primaries: Sohl-Dickstein et al.
  2015 (deep unsupervised learning / nonequilibrium thermodynamics); Song &
  Ermon 2019 (NCSN / score matching); and the after-record — DDIM (Song et al.
  2020), classifier / classifier-free guidance, latent diffusion (Rombach et al.
  2022), score-SDE unification (Song et al. 2021), and at least one serious later
  assessment or survey. For each, establish firsthand what it changes in the
  interpretation of DDPM's claim.
- Verify every number against the paper's own tables (do not carry a secondary's
  restatement). Confirm each URL is the source's own page (arXiv abs, proceedings).
- Contradictions: note where DDPM's own claims are qualified by later work (e.g.,
  sampling cost, log-likelihood competitiveness) — this feeds the verdict.
