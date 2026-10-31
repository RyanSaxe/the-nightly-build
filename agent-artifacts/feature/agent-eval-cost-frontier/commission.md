# Commission: feature/agent-eval-cost-frontier

## The article
A five-minute feature for readers who build ML systems in production. The
subject is how AI research agents are scored, using Ai2's AstaBench as the case.
Most agent leaderboards report an accuracy number and stop. AstaBench measures
the dollar cost of each run in a fixed search-and-tool environment and reports
accuracy against that cost. The finding the article carries: there is no single
best science agent, there is a frontier, and which agent you would pick depends
on the budget you are willing to spend per problem.

## The angle, in one line
When you price an AI agent's answers, the leaderboard stops being an ordered
list and becomes a trade-off curve, and the agent at the top of the accuracy
column is often not the one you would deploy.

## Original work the piece must do
The sources report accuracy and cost side by side. The article does one thing
with them the sources do not: it reads the leaderboard as a budget decision.
Take the published (agent, accuracy, cost-per-problem) points, show the Pareto
frontier they trace, and show that the accuracy ranking and the
accuracy-per-dollar ranking are different orderings of the same agents. State
plainly where a cheaper agent is within a few points of the most accurate one at
a fraction of the cost, and where paying more buys real accuracy.

## Boundaries
- Anchor on AstaBench. Do not drift into a survey of every benchmark. One case,
  shown well, beats a tour.
- This is about evaluation and cost, not about which lab's model is best and not
  about reinforcement learning. The RL course lesson in tonight's edition owns
  RL; the brief owns model-release news. Keep off both.
- Report only what the paper and the public leaderboard establish. Cost figures
  are the agents' measured inference cost under AstaBench's environment, not
  retail API prices, and the article says so.
- No claim that AstaBench is the right or only way to benchmark. It is the case
  that makes the cost point visible. If the sources show a weakness in its cost
  accounting, report it.

## Required visuals (the visuals carry this piece)
1. A drawn diagram (inline SVG in `figure.nb-figure`, theme variables) of how a
   cost-controlled evaluation works: an agent runs inside a fixed
   search-and-tool environment, every model call and tool call is metered, and
   the run produces both an answer scored for accuracy and a dollar cost per
   problem. Draw where the quantity comes from, not a generic box flow.
2. A real accuracy-vs-cost scatter with the Pareto frontier marked, built with
   `nb chart` from the leaderboard's own (agent, accuracy, cost) numbers that
   the researcher records. Log x-axis for cost if the range spans decades; note
   the scale. Cite the data source in the caption.
A third visual (a small table re-ranking agents by accuracy vs. by
accuracy-per-dollar) is welcome if the word budget allows.

## Geometry and policy
- Template `article`: orientation + 2-4 flex sections + Sources. Words 600-1200,
  strict. Every non-source section cited. min_sources 5.
- Sources: AstaBench is primary for its own numbers (the arXiv paper and the
  public AstaBench leaderboard page). Ai2's Asta/AstaBrief posts are primary for
  Ai2's claims. Any independent coverage is secondary and never a source for a
  number. Classify each honestly.

## Recent-record notes (break these habits; the editor compares against them)
Recent features and their tells to avoid:
- Deks that name a dataset then deflate its "most-quoted figure" (ai-economy-ATLAS:
  "Its most-quoted figure ... is a share ... reproduces only as 20.06%"). Write a
  dek that states this piece's own finding and one unmistakable number, not that
  mold.
- The semicolon-reversal dek ("Optical images show glacier motion; radar finds
  no progressive signal", nepal-geohazard) and the comma-triad dek are banned.
- Closing-heading molds "What the X will bear" / "What a court would still have
  to decide". Name the last section for this argument's own close.
- Headings in recent features are all declarative "subject verb object"
  argument steps (good house style). Keep them declarative but build them
  differently from one another so the set does not read stamped.
- A deflationary section-ender is a house strength; phrase any such line in this
  piece's own nouns (cost, frontier, budget), never a reusable aphorism.

## Angle revised after research (orchestrator decision — supersedes the above)
The researcher confirmed per-agent (score, cost-per-problem) data is published on
Ai2's live AstaBench leaderboard, with an 11-agent Pareto frontier it
independently recomputed. But the evidence breaks two of my original framings, so
the angle changes to what the data actually shows:

- Drop "the top-accuracy agent is often not the one you would deploy." The
  top-accuracy agent (ReAct with claude-opus-4-7, 0.5804 at $3.5422/problem) is
  itself ON the frontier. That framing is unsupported; do not use it.
- The real, sharper finding: the leaderboard's frontier is mostly a *model-choice*
  curve, not an agent-design curve. Ten of the eleven frontier points are Ai2's
  one generic ReAct scaffold with the language model swapped. The lever on both
  score and cost is which model you drop into the same loop. The piece's spine:
  1. A generic ReAct loop with a strong model beats Ai2's own purpose-built
     science agent: Asta v0 is dominated — ReAct with gpt-5.5 scores ~2.0 points
     higher at ~47% of the cost.
  2. Accuracy ranking and score-per-dollar ranking are different orderings of the
     same agents: Opus 4.7 is 1st by accuracy and 21st of 23 by score-per-dollar;
     GPT-5 Mini is 26.7 points behind at ~1% of the cost; paying 8.4x (Mini -> GPT-5)
     buys +12 points. These are the budget trade-offs, stated as the data shows
     them and not as a claim about any one reader's choice.
- Honesty the piece must carry (from the evidence Limits): "cost" is measured
  model-token usage priced by a frozen litellm snapshot, so it is a token estimate
  and not a billed amount; tool calls are not priced; all 24 costed rows were
  submitted by Ai2; commercial agents (Elicit, SciSpace, OpenAI Deep Research)
  report no cost and cannot sit on the frontier; and the top agents' ~±2.4 to ±3.0
  point intervals overlap, which the board's chart does not show. State these;
  they are the fair-to-the-opposing-view part.

Corrected visual 1 (the diagram): show priced model calls inside a fixed,
UNPRICED tool/search environment, and that the dollar figure is logged tokens
times a frozen price table. Do not draw tool calls as metered in dollars.
Chart data: use the LIVE leaderboard numbers (the arXiv Tables 4/11 differ from
the live board for the same agents; the researcher recorded the full live series).

Original work (revised): re-rank the published board by score-per-dollar against
accuracy, and show that the frontier is a model-swap curve on one scaffold, with
Ai2's specialized agent dominated. That is the thing the sources report but do
not themselves say.

## Production
- writing-coach: model sonnet, effort low (capable/low).
- researcher: model sonnet, effort high (capable/high).
- writer: model sonnet, effort high (capable/high per series).
- editor: model opus (inherit), effort high, required.
Recorded deviations: "capable" is served by Claude Sonnet, "inherit" by the
orchestrator's Claude Opus. No required model/effort was traded down.
