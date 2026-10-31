# researcher brief: feature/agent-eval-cost-frontier (01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md`
Output: `evidence.md` in this folder (`researcher/01/`)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

The article reads Ai2's AstaBench as a budget decision: when agents are scored
with their inference cost measured, there is a frontier, not a single winner.
Your job is to make that claim checkable or to break it.

Questions to answer from primary documents:
1. What is AstaBench? Open the arXiv paper (2510.21652, "AstaBench: Rigorous
   Benchmarking of AI Agents with a Scientific Research Suite") and read how it
   measures cost and tool access, not just accuracy. Record the exact mechanism:
   the fixed search/tool environment, what is metered, how cost per problem is
   defined. Record the scale (problems, agents, agent classes) exactly.
2. The data for the chart. Find the public AstaBench leaderboard (Ai2 / Asta /
   HuggingFace space, whatever Ai2 actually publishes) and record a table of
   (agent name, overall accuracy/score, cost per problem in USD) for as many
   agents as it lists. This is the series the writer plots. Preserve the full
   list, the units, the exact date you retrieved it, and the page that owns it.
   If per-agent cost is NOT published, say so clearly in Limits: that decides
   whether the chart is real or conceptual.
3. Does the accuracy ranking differ from the accuracy-per-dollar ranking? From
   the numbers you recorded, note at least one concrete case where a cheaper
   agent is within a few points of the most accurate one, and at least one where
   paying more buys real accuracy. Record the exact figures, not an impression.
4. The AstaBrief 8B release (early Oct 2026) if it helps show the cost point:
   Ai2's reported per-report latency (the ~51s vs ~178s figures) and any cost
   claim, from Ai2's own model card / blog, with locators. Secondary only if
   Ai2's own page is unreachable.
5. What breaks the angle. Look for it: does AstaBench's cost accounting have a
   known limitation (cached calls, free tools, provider price drift, non-comparable
   cost across closed vs open models)? Does the paper itself caution against
   reading the frontier as a deployment guide? Record every such caution with its
   locator. Record contradictions in full.

Source rules: AstaBench's paper and Ai2's leaderboard/posts are primary for
their own numbers. Independent coverage is secondary and never the owner of a
number. Confirm every URL resolves to the document's own page. min_sources 5.

In Source assets, note any figure in the paper (for example a cost-vs-accuracy
plot, or a results table) that shows the frontier better than prose, with where
it lives and what a crop must keep. Do not prescribe pixel crops.

Report the path, the single most important limit, and whether the per-agent cost
data needed for the chart is actually published.
