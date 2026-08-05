# writer brief: paper-of-the-day/denoising-diffusion (02) — takeover to finish

The writer/01 invocation built the article to BLOCK:0 (assets captured, equations placed) but
STALLED on a headless-browser render inspection (KaTeX/Prism CDN needs proxy) and never finished:
no draft-handoff, 6 density warnings unaddressed, final link-proof not run. Finish the job.
PRESERVE the substantial completed article; do NOT rebuild it.

Inputs:
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writer/01/brief.md — the full original brief (equations/assets/verdict requirements)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/researcher/01/evidence.md — verify numbers/equations against this
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writing-coach/01/voice-guide.md — voice guide
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion.html — the ALREADY-BUILT article (edit in place)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion/asset-1.png and asset-2.png — the captured source assets

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writer/02/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

CRITICAL — avoid the stall: **Do NOT launch a headless browser / custom render server / `nb preview` browser inspection that routes CDN assets through the proxy — that is exactly what stalled the prior run and it is NOT the publication gate.** The deterministic `nb check` proof is the gate; the CI render-probe will verify actual rendering downstream. To sanity-check the equations and assets, READ the HTML source and VIEW the two asset PNGs with the Read tool (it renders images) — do not open Chrome.

Finish these, nothing more:
1. Read the current article and confirm it holds: the abstract card is filled; the load-bearing equations are SET as equation furniture (forward process, closed-form q(x_t|x_0) with alpha-bar, the reduction to the epsilon objective and L_simple with the weighting dropped); the two source assets (Algorithm boxes / a sample-quality figure) have factual cited captions and the argument spends them; a verdict precedes Sources. Verify every number against the evidence (CIFAR-10 FID 3.17 / IS 9.46; the NLL 3.75 vs 3.70 bits/dim; LSUN FIDs in captions). Fix any factual slip you find; otherwise do not rewrite settled prose.
2. Address the 6 W-SENTENCE-DENSITY warnings: split each long sentence into plain sentences, OR record in the handoff why a given one must stand (a dense derivation step can justify one, but 6 is too many — split most). Re-proof until warnings are cleared or justified.
3. Display-text pass: headline, dek (nb-meta dek == rendered dekline), subheads, and every number/name against the evidence; headline/dek not a colon-subtitle or banned mold.
4. Run `nb stamp`, then the exact `nb check` proof WITH links to BLOCK: 0 (and WARN:0 or warnings justified).
5. Write draft-handoff.md with the one-sentence original-work statement, the proof result, and any warning intentionally left with its reason.

Report: draft-handoff path, final BLOCK/WARN, which warnings you split vs justified, and confirmation the assets/equations read correctly from the HTML+PNGs.
