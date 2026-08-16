# writer brief: investing/margin-of-safety (01)

Inputs (paths relative to the workspace root `.nb-work/investing/margin-of-safety/`):
- `agent-artifacts/investing/margin-of-safety/editorial-direction.md`
- `agent-artifacts/investing/margin-of-safety/writing-coach/01/voice-guide.md`
- `agent-artifacts/investing/margin-of-safety/researcher/01/evidence.md` — the complete claim set, including the Adobe value range
- `agent-artifacts/investing/margin-of-safety/commission.md` — the lesson's place in the course, what it teaches, the habits to break
- `library/investing/margin-of-safety.html` — the initialized lesson to edit in place
- `.nb-context/` — effective template contract (lesson) and furniture catalogs

Output: `agent-artifacts/investing/margin-of-safety/writer/01/draft-handoff.md`

Proof (from repo root, workspace-prefixed; iterate with `--no-check-links`, links on until BLOCK: 0):
`./nb check .nb-work/investing/margin-of-safety/library/investing/margin-of-safety.html --series investing --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check.

Evidence cautions to honor (from the researcher):
- The anchor is Adobe (ADBE). Present the conservative (~$236) and optimistic (~$518) per-share values as OUTPUTS OF STATED ASSUMPTIONS, never as figures Adobe reported. The 10-K owns the inputs (revenue, operating income, tax, cash flows, cash, debt, shares); the growth, discount, and terminal choices are estimates the lesson makes explicit.
- The teaching payoff is that the same $264 price is a small negative margin against the conservative value but a ~30% discount to the midpoint, so which estimate you anchor to decides whether there is a margin. This is why Graham ties the margin to a conservative value. Build to that, do not just assert it.
- The conservative case uses after-tax operating income, not headline free cash flow, because reported FCF adds back ~$1.94B of stock-based compensation, a real dilutive cost. Keep that choice explicit where the number first appears.
- Stage-1 growth is the swing input; say so and let the sensitivity show it.
- If you cite a specific Graham book and page for the margin-of-safety statement, confirm the edition; the idea is uncontested but its exact location varies between sources. Cite only what the evidence record shows was read.

nb-meta: set `date` 2026-08-16, `harness` `claude-code-routine`, `model` `claude-opus`, `tags` []. Keep nb-meta `dek` identical to the rendered dekline. This is a lesson: fill the `why` and `takeaway` bookends last, after the body; those two bookend cards may address the reader, the body may not.

This round's focus (recent investing-desk shapes to break, per the commission):
- Recent lessons open their first body section on "What the [shortcut / terminal value] takes on faith / left out." Do not open on that mold.
- Recent lessons are built as a two-named-company head-to-head. This one is Adobe's value against its price; do not force a second company in for contrast.
- Recent deks are quantitative one-line punches ("worth four times", "roughly triples"). A figure in the dek is fine, but vary the construction so it is this lesson's own.
- Use nb-math and nb-table where the arithmetic of the range and the discount is the point, not as decoration.
