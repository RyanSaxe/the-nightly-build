# writer brief: tech-news/2026-08-16 (01)

Inputs (paths relative to the workspace root `.nb-work/tech-news/2026-08-16/`):
- `agent-artifacts/tech-news/2026-08-16/editorial-direction.md`
- `agent-artifacts/tech-news/2026-08-16/writing-coach/01/voice-guide.md`
- `agent-artifacts/tech-news/2026-08-16/researcher/01/evidence.md` — the candidate items with primary + independent sources
- `agent-artifacts/tech-news/2026-08-16/commission.md` — the selection bar, source geometry, do-not-repeat list, habits to break
- `library/tech-news/2026-08-16.html` — the initialized brief to edit in place
- `.nb-context/` — effective template contract (brief) and furniture catalogs

Output: `agent-artifacts/tech-news/2026-08-16/writer/01/draft-handoff.md`

Proof (from repo root, workspace-prefixed; iterate with `--no-check-links`, links on until BLOCK: 0):
`./nb check .nb-work/tech-news/2026-08-16/library/tech-news/2026-08-16.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check.

Selection and evidence cautions (from the researcher):
- Select 4 to 6 items. Each item needs exactly one primary record and at least one independent account, per the brief template. The researcher surfaced 7 candidates; choose on significance, not popularity.
- Every model capability or benchmark number here is a lab self-report; no independent evaluator had posted verified scores for the 14 Aug releases. Say so plainly for any item you carry (Qwen, GLM-5.3): report the number as self-reported and the gap between it and independent verification.
- 15-16 August proper was quiet; the strongest developments cluster 12-14 August. Treat the brief as the Sunday desk carrying the freshest consequential work; do not manufacture items to fill a quota (four strong items beat six padded ones).
- Do not repeat the DeepSeek V4-Pro item (covered 15 Aug) or anything else on the commission's do-not-repeat list.
- If you use the lower-tier Nvidia 13F item, verify the figure against the raw SEC Form 13F on EDGAR first; the researcher did not open it directly. The "$21B vs $50B" discrepancy is SpaceX-alone vs SpaceX-plus-Intel.
- The Anthropic watermarking/C2PA item: state the company's own caveat that the mark proves involvement, not authorship.

nb-meta: set `date` 2026-08-16, `harness` `claude-code-routine`, `model` `claude-opus`, `tags` []. Keep nb-meta `dek` identical to the rendered dekline. Each item carries its own tags in the item markup per the brief template; use concrete topical tags drawn from the items you select.

This round's focus (recent brief-desk shapes to break, per the commission):
- Name the single most consequential item in the headline and lead with the concrete result; avoid a triad-of-topics headline that only sounds comprehensive.
- Each item's "why it matters" states what changed in the technical picture, not that a company shipped something. Assume the reader has seen the day's headlines.
