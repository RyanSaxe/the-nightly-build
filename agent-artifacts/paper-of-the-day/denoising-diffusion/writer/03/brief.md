# writer brief: paper-of-the-day/denoising-diffusion (03) — revision

Apply the two required items in the editor's review, nothing else. Preserve settled work.

Inputs:
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/editor/01/editorial-review.md — the review to apply (Decision: revise)
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/researcher/01/evidence.md — for the watermark/memorization fact
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion.html — the article to fix
- /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion/asset-2.png — the LSUN Church grid (view to confirm the watermark)

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/agent-artifacts/paper-of-the-day/denoising-diffusion/writer/03/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/paper-of-the-day/denoising-diffusion/library/paper-of-the-day/denoising-diffusion.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Do NOT launch a headless browser (it stalls on CDN/proxy). Edit the HTML and view asset-2.png with the Read tool.

Required items (from editor/01):
1. **(blocking) asset-2 caption honesty:** the LSUN Church sample grid (caption labels it "Generated LSUN Church samples", FID 7.89, Fig. 3) shows a legible Shutterstock watermark in the top-left cell — the known DDPM training-data-memorization artifact. Add a brief FACTUAL note to the caption acknowledging the visible watermark (interpretation/the memorization point belongs in PROSE, not the caption). Do NOT recrop or edit the asset — the watermark is in the paper's own Figure 3. If you make the memorization point, do it in one prose sentence grounded in what the figure shows.
2. **(minor) heading cadence:** vary one of the two comma-and headings ("Strong samples, a likelihood that lost, and a cost left unnamed" / "A training recipe, not a new model, and the recipe was right") so the two do not read as the same stamped shape; optionally thin a recurring "not X" contrast where not load-bearing. Do not introduce a new formula.

Change ONLY these; preserve the verified equations, numbers, assets, and settled prose (including the editor's own cut). The 5 density WARN are justified equation-LaTeX false-positives — leave them. Run `nb stamp` then the exact proof to BLOCK: 0 (WARN may remain 5 for the equations). Add one line per required item resolved to draft-handoff.md.
