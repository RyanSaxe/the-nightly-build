# writer brief: tech-news/2026-08-16 (02)

Prior artifacts to apply, not re-derive:
- Editorial review: `agent-artifacts/tech-news/2026-08-16/editor/01/editorial-review.md` (the editor made direct edits already; apply only the one routed writer item below)
- Your prior handoff: `agent-artifacts/tech-news/2026-08-16/writer/01/draft-handoff.md`
- Evidence record: `agent-artifacts/tech-news/2026-08-16/researcher/01/evidence.md`
- Article (already carries the editor's direct edits): `library/tech-news/2026-08-16.html`

Single required fix (blocking, from the editor's skeptic read): the footprint sentence "still fit the 24 to 28 GB of a single workstation GPU at 8-bit precision" is cited to the Qwen model card (s1), which states no VRAM figure at any precision. Take the editor's path (b): replace the specific 24-28 GB range with the ~27 GB that follows arithmetically from the 27B parameter count at 8-bit (about one byte per parameter), cite that anchor to the card's parameter count, and cite the qualitative "runs on a single workstation / consumer GPU" claim to s2 (local-ai-zone, which says it runs on consumer hardware). Frame the number as an at-reduced-precision estimate, not a measured figure. Do not introduce a new source; do not restate the runbook estimate the card cannot back.

Preserve all of the editor's direct edits and everything else in the article. Change only what this fix requires.

Output: a new `agent-artifacts/tech-news/2026-08-16/writer/02/draft-handoff.md` with one line recording the resolved item.

Proof (rerun complete, links on, until BLOCK: 0):
`./nb check .nb-work/tech-news/2026-08-16/library/tech-news/2026-08-16.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check. Keep nb-meta `dek` identical to the rendered dekline.
