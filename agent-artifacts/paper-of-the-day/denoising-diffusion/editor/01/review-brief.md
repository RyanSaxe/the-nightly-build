# review-brief: paper-of-the-day/denoising-diffusion (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/editorial-direction.md — governing standard, `paper` identity, series prompt, declared reader (math/CS/ML background)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writer/01/brief.md — the exact writer brief (instruction-leakage checks)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writing-coach/01/voice-guide.md — voice guide (read FIRST): each equation transition should read as a decision forced by a named constraint
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/researcher/01/evidence.md — the evidence (verbatim equations, figure assets, after-record, verdict-feeding limitation)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writer/02/draft-handoff.md — the handoff (original-work sentence; the 5 justified warnings)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion/asset-1.png, asset-2.png — the source assets (VIEW with Read tool)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (REQUIRED stage).
Do NOT launch a headless browser to render — VIEW the asset PNGs and READ the HTML; CI's render-probe verifies typesetting.

This round's focus:
- **The reconstruction is the point.** Verify the math is SET (not paraphrased) and correct against the evidence: forward process; closed-form q(x_t|x_0) with the ᾱ reparameterization (Eq. 4); the variational bound (Eq. 5); tractable posterior (Eq. 6-7); the reduction to the ε-prediction objective and **L_simple with the weighting term dropped** (Eq. 14). Confirm each transition reads as a decision forced by a named constraint (tractability/variance/an empirical result), per the voice guide — not algebra resolving itself. A wrong or hand-waved load-bearing equation is a required fix (writer).
- **Numbers vs the paper's own tables:** CIFAR-10 FID 3.17 / IS 9.46; the ablation figures; NLL ≤3.75 (L_simple) vs ≤3.70 (fixed-Σ variant); LSUN Church 7.89 / Bedroom 4.90 (in figure captions); Score-SDE 2.20. Any secondary restatement standing in for a paper number is a fix.
- **Source assets are evidence:** VIEW asset-1 (Algorithm 1/2 boxes) and asset-2 (LSUN Church grid, caption "FID 7.89", Fig. 3). Confirm each caption is factual and cited, the crop retains the evidence the prose spends and omits clutter. RULE on the asset-2 watermark: a faint Shutterstock watermark fragment is visible because DDPM's LSUN samples famously reproduce training-set watermarks — decide whether the caption should note this (honesty) or whether it is acceptable unremarked as the paper's own figure. Interpretation belongs in prose, the caption stays a factual label.
- **Verdict:** confirm a verdict on the claims precedes Sources and weighs sample quality vs. non-competitive log-likelihood and the unaddressed 1000-step sampling cost, using the after-record (DDIM, Improved DDPM, Score-SDE, etc.) only where it changes interpretation. Place the paper against its lineage (Sohl-Dickstein 2015; NCSN 2019).
- **The 5 remaining WARN (density):** the handoff argues they are the density heuristic scoring verbatim equation LaTeX inside `nb-math-eq` divs, not prose. Confirm this by reading them — each flagged "sentence" should be display-equation TeX (Eq. 4, 5, 6-7, 12, 14), not an actual prose run-on. Accept them as justified furniture; but if a genuine prose run-on hides among them, cut/split it (writer if it needs new prose). Do NOT ask to split an equation.
- Open every citation href as printed — arXiv abs pages (not PDF-fetch endpoints), proceedings. Audit data-nb-kind (the focal paper is primary; after-record sources secondary unless they own a distinct claim). Check display text (headline/dek/subheads) against the evidence; nb-meta dek == dekline; no colon-subtitle/banned mold.
- Third read: what does the reconstruction give beyond the paper (the original-work sentence), and is the prose closer to the voice-guide exemplars (Weng/Olah-style build-up) than a median summary?
- After any direct cuts run `nb stamp`. Decision: approve or revise, naming each required item's owner.
