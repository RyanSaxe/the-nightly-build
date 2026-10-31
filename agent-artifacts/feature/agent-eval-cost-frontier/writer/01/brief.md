# writer brief: feature/agent-eval-cost-frontier (01)

Inputs:
- `../../editorial-direction.md` (house + press + article-template + feature direction)
- `../../commission.md` (read the "Angle revised after research" section; it
  supersedes the earlier angle)
- `../../writing-coach/01/voice-guide.md`
- `../../researcher/01/evidence.md` (the live leaderboard series, the orderings,
  and the Limits that the piece must carry)
Output: `/home/user/the-nightly-build/.nb-work/feature/agent-eval-cost-frontier/library/feature/agent-eval-cost-frontier.html`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/agent-eval-cost-frontier/library/feature/agent-eval-cost-frontier.html --series feature --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. The markup contract and furniture catalogs are under
`.nb-work/feature/agent-eval-cost-frontier/.nb-context/`; read them and
`spec/charts.md` for chart provenance. Where something you need is missing, ask
me (the orchestrator), do not invent.

This round's focus and caveats (not in the inputs, or easy to get wrong):

- **The angle is the revised one in the commission.** The finding: AstaBench's
  published frontier is mostly a model-choice curve on one generic ReAct
  scaffold; a plain ReAct loop with a stronger model beats Ai2's own specialized
  science agent (Asta v0 is dominated); and pricing the answers reorders the
  board (top-accuracy Opus 4.7 is near-worst by score-per-dollar). Do NOT write
  that the most accurate agent is off the frontier; it is on it.
- **Honesty is part of the piece, not a footnote.** State plainly: cost is logged
  model-token usage priced by a frozen litellm snapshot (a token estimate, not a
  billed amount); tool calls are not priced; all costed rows were submitted by
  Ai2; commercial agents report no cost; the top agents' intervals (~±2.4 to ±3.0
  points) overlap and the board shows no error bars. These are what keeps the
  claim fair.
- **Visuals carry the piece** (writer runs at high effort for this reason). Build
  two or three:
  1. A drawn inline-SVG diagram (theme variables) of how a cost is produced:
     priced model calls inside a fixed, UNPRICED tool/search environment, dollars
     = logged tokens x a frozen price table. Draw where the number comes from.
  2. A real accuracy-vs-cost scatter via `nb chart` (plotly) from the LIVE
     leaderboard numbers in the evidence record, with the Pareto frontier marked
     and a few points labeled (e.g. ReAct opus-4-7, ReAct sonnet-4.6, ReAct
     gpt-5.4, GPT-5 Mini, Asta v0). Use a log x-axis for cost and note the scale;
     label axes; cite the leaderboard and retrieval date in the caption. Do not
     use the arXiv table numbers, which differ from the live board.
  3. Optional if the word budget allows: a small `nb-table` re-ranking a handful
     of agents by accuracy and by score-per-dollar to show the two orderings.
  Run `nb preview` and look at every visual for overlapping labels and arrows
  that stop short.
- **Geometry.** Template `article`: orientation + 2-4 flex sections + Sources.
  Words 600-1200, STRICT (a hard limit both ways), so cut to the visuals and the
  conclusion. Every non-source section cited; number sources in first-citation
  order; carry each source's kind from the evidence record into `data-nb-kind`;
  prefer a locator that lands on the passage. min_sources 5. Do not close on a
  reading list or a pointer away.
- **Headline/dek.** State the finding with a verb; the researcher's sharpest
  single fact (a generic agent with a better model beating the specialized one,
  or the accuracy/cost re-ranking) is the headline candidate. Avoid the recent
  deks the commission flags (the "its most-quoted figure" deflation mold, the
  semicolon-reversal, the comma-triad). Build the 3-5 section headings
  differently from one another.
- **nb-meta.** date `2026-10-31`; keep mode as generated; `order` stays `null`;
  set `tags` to `["ai-agents","evaluation","benchmarks"]`; `harness` to
  `claude-code-routine`; `model` to the model you actually ran as (if you ran as
  Claude Sonnet, use its model id). Make the `nb-meta` dek and the rendered
  dekline identical. `nb stamp` writes the counts.
- **Banned terms** (merged, STRICT series — these BLOCK): em-dash max 4,
  "leverage" max 1, "load-bearing" 0, "mechanism"/"mechanisms" max 1. Rewrite
  whole sentences rather than swapping synonyms.

Do the original work: say in one sentence (in `draft-handoff.md`) what the piece
does with the leaderboard that the leaderboard does not do itself (re-rank by
score-per-dollar and expose the model-swap frontier). Iterate the proof with
`--no-check-links`, fix warnings in batches, then `nb stamp` and the exact proof
command above with links until `BLOCK: 0`. Write `draft-handoff.md` in
`writer/01/` with the original-work sentence, the proof result and any warning
left on purpose, and any open question. Report the handoff path and any warning.
