# writer brief: investing/margin-of-safety (02)

Prior artifacts to apply, not re-derive:
- Editorial review that routed this: `agent-artifacts/investing/margin-of-safety/editor/01/editorial-review.md` (the editor made four direct edits already; apply only the one routed writer item below)
- Article (already carries the editor's direct edits): `library/investing/margin-of-safety.html`

Single required fix (the editor verified the correct figure against Adobe's 10-K): change the two display instances of Adobe's subscription/recurring revenue from "97 percent" / "97%" to 96 — one in the orientation prose (around line 85), one in the stat strip (around line 103). Adobe's 10-K MD&A prints 96% ($22,904M of $23,769M = 96.4%, rounded to 96). Change only these two figures and any immediately adjacent wording the change requires. Preserve every other word, including the editor's four direct edits.

Do not add or remove any claim or source. This is a single-number correction the editor pre-approved for publication once applied.

Output: a new `agent-artifacts/investing/margin-of-safety/writer/02/draft-handoff.md` with one line recording the resolved item.

Proof (rerun complete, links on, until BLOCK: 0):
`./nb check .nb-work/investing/margin-of-safety/library/investing/margin-of-safety.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check. Keep nb-meta `dek` identical to the rendered dekline.
