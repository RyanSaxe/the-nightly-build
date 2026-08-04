# writer brief: paper-of-the-day/generative-adversarial-networks (01)

Inputs:
- .nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/editorial-direction.md — governing standard, `paper` template identity, series prompt, declared reader
- .nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/commission.md — subject, angle, required contribution, boundaries
- .nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/writing-coach/01/voice-guide.md — craft standard and licenses (every set equation cashes out in the next sentence)
- .nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/researcher/01/evidence.md — the complete verified claim set; cite only what it opened; use Numbers and Source assets exactly
- .nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html — the initialized article to edit (do not recreate its skeleton)
- .nb-work/paper-of-the-day/generative-adversarial-networks/.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: .nb-work/paper-of-the-day/generative-adversarial-networks/agent-artifacts/paper-of-the-day/generative-adversarial-networks/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/2d5b8802-c025-5b79-bf1d-234ffd5a3463/scratchpad/library-checkout

Focus:
- Rebuild the minimax game from the paper's own artifacts and SET the math (don't paraphrase): the value function min_G max_D V(D,G); Prop. 1 optimal discriminator D*(x)=p_data/(p_data+p_g); Thm. 1 global optimum at p_g=p_data with V reducing to a Jensen-Shannon divergence. Each equation cashes out in the very next sentence (voice guide) — what it now lets the objective do.
- The examine-able gap, stated precisely per the evidence: the global-optimum theorem and Prop. 2 convergence assume optimization in FUNCTION space with the discriminator trained to its inner-loop optimum, but Algorithm 1 runs alternating parameter-space SGD with k=1, and the paper itself abandons the analyzed minimax loss for the non-saturating heuristic (Sec. 3). "The theorem and the training loop are about different objects, and the paper says so." Make that the spine.
- Two sharpenings the researcher flagged, respect exactly:
  1. "JS gives vanishing gradient" (Arjovsky & Bottou, arXiv:1701.04862, Thm 2.4) is exact for the ORIGINAL minimax loss. For the non-saturating loss the paper actually uses, the diagnosis differs and is arguably worse: an unstable, infinite-variance gradient optimizing KL − 2·JSD (their Thms 2.5-2.6). Do not overclaim the JS-gradient story onto the loss GANs actually trained.
  2. WGAN (arXiv:1701.07875) offers the Earth-Mover fix but is NOT the last word: Fedus et al. 2018 (arXiv:1710.08446, Goodfellow a co-author) calls the divergence-minimization frame "overly restrictive" with counterexamples; Mescheder 2018 and WGAN-GP show WGAN's fix was provisional. The shape is "elegant theory, messy practice, principled-but-contested diagnosis" — weigh it and land a graded verdict; do not manufacture symmetry and do not debunk (GANs worked — cite DCGAN as the "it worked" premise).
- The paper's weakest ACTUAL claim is its evaluation (Parzen-window log-likelihood, which the authors themselves flag), not the theory. Say so plainly when you weigh the evidence as a reviewer.
- Source assets from the evidence, captured with `nb asset` from the arXiv source: Fig. 1 (the schematic pushing D toward 1/2), Algorithm 1 (the alternating-SGD loop), and Fig. 2 samples if it earns space. Captions say what each settles.
- Do NOT inherit the "famous claim overturned" mold; avoid a colon-subtitle headline and the comma-triad dek; check recent paper-of-the-day deks (in commission). nb-meta: date 2026-08-04, harness Claude Code / The Nightly Build, model = the model you run on (Opus); run `nb stamp`.
- Name the piece's one act of original work in draft-handoff.md and make it visible.
