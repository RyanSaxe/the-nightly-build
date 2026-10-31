# Draft handoff: feature/agent-eval-cost-frontier (writer 01)

## Original work
The piece re-ranks Ai2's published board by score per dollar and shows that its cost frontier is a model-swap curve on one generic loop (10 of 11 points are ReAct, with a seven-model check that swapping the scaffold moves scores 0.4 to 9.3 points against 7.7 to 58.0 for swapping the model), which the leaderboard reports as a flat list and never says.

## Proof
`nb check ... --series feature --repo /home/user/the-nightly-build` (links included): BLOCK 0, WARN 0, PUBLISHABLE. `nb stamp`: 1097 words, 5 min, 6 sources. Both visuals were rendered and looked at (diagram at desktop width, scatter PNG at full size). No warning left on purpose.

## Decisions to know
- `nb-meta.mode` is `open`, not the generated `collection`: the proof blocked `collection` (B-META-MATCH, series mode is open).
- Chart uses the live board's 23 four-category costed agents; the 24th costed row (Smolagents Coder, Llama 4 Scout, 3/4 categories) is omitted and the caption says so. Provenance: `agent-eval-cost-frontier/chart-1.py` (data inline, scores x100).
- The Asta v0 vs ReAct gpt-5.5 comparison is stated with its generation caveat (Aug 2025 vs Apr 2026 runs), plus the same-vintage comparison (Asta v0 +7.6 points at 11x the cost vs ReAct GPT-5) and the paper's note that engineering cost is excluded. The angle is not "top accuracy is off the frontier"; Opus 4.7 is named as on it.
- Derived figures (points per dollar and ranks, the 0.4 to 9.3 scaffold spread over seven models, 7.6 points / 11x, $1.93, 8.4x, 2.2x) are computed from the evidence-record rows; the table caption says "computed from the leaderboard rows".
- Intervals (opus-4-7 58.0 +/-2.7, opus-4-6 55.3 +/-2.4, gpt-5.5 52.9 +/-3.0) are the researcher's computation from the raw result files by the paper's Appendix D method; cited to the results dataset and the paper.
- Source 5 (Ai2 blog) is cited only for "reasoning effort fixed at medium"; the AstaBrief posts were left out as off-topic (no cost figure).

## Open questions for the editor
- The paper says nothing on whether LLM-judge calls count toward cost, and it is not claimed in the piece.
- The "No source I read puts a price on a tool call" sentence is first-person and rests on the researcher's reading of the paper, About page, blog and README; the editor may want it reworded as a plain absence claim.
