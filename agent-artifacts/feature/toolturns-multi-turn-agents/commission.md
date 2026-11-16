# Commission: feature/toolturns-multi-turn-agents

Series: feature (Daily). Template: article. Strict: yes (600 to 1200 words, hard). Flex sections 2 to 4. Min sources 5.
Production (balanced, advisory except the editor): writing-coach capable/low, researcher capable/high, writer capable/high (series override), editor inherit/high (required).
Edition neighbours this run: the Daily Brief for 16 November (news and technology items; it will not cover ToolTurns) and an RL course lesson on discretizing continuous actions. No overlap.

## The story

ToolTurns (Gholami, King and Flanigan, arXiv 2611.14925, submitted 11 November 2026) is a multi-turn tool-use benchmark: 2,620 problems over 1,827 tools and 11,004 endpoints, each dialogue an underspecified opening request plus two context-dependent follow-ups, driven by a released user simulator. The best of nine models resolves 69.6% of individual requests and completes 39.8% of whole dialogues; every model scores lower on follow-ups than on the opening request; rubric-based dialogue quality ranks models differently from task success.

## Angle

The gap between per-request and per-dialogue success is the story, and it can be shown. Work out what the paper's own per-turn numbers imply about how failures in one turn relate to failures in the next (for example, set the observed dialogue completion against what independent per-turn success would predict, per model, from the paper's tables), and say what that means for anyone who evaluates an agent on single requests. The second strand is the ranking disagreement between rubric quality and task success. Report the user-simulator and checker-fixer only as far as a reader needs to trust or doubt the numbers.

The angle stands only if the paper's tables support it. If per-turn rates are not reported in a form that permits the comparison, narrow to what is reported and say so; do not reconstruct numbers the paper does not give.

## Required contribution

A computation or visual the paper does not itself present (for example, per-model turn-by-turn success with the independence prediction beside the observed dialogue rate, or a rank-versus-rank comparison of rubric quality against task success), built from the paper's reported figures, plus outside context from at least one other multi-turn or tool-use benchmark (for example tau-bench, BFCL multi-turn, MultiChallenge, or Laban et al.'s "LLMs Get Lost in Multi-Turn Conversation") that either agrees with or cuts against the finding.

## Boundaries

- A single preprint: say so, and do not present its figures as settled beyond what the paper establishes. Note the simulator-driven design as a limit where it matters.
- Five-minute read. Open with the finding in two or three sentences; build each section around a visual.

## Recent-pattern notes (features 8 to 15 November, and the AstaBench feature of 31 October)

- Recent headlines lean on a figure-against-figure comparison ("cuts ... 87%, as lanadelumab does ...", "trades X for Y", "twice as far ... as ..."). Use a different construction.
- Recent deks close with a trailing "which leaves ..." or "while X ..." clause. Do not.
- The AstaBench feature (an agent benchmark) was organized as a decomposition of one score by component. Do not reuse that structure.
- Headings: avoid "What X averages" / "Between X, Y" constructions used on 31 October.

## Decisions log

- Topic chosen by the orchestrator from a scout's four candidates. The data-centers/electricity candidate was rejected because the paper ran it on 6 November; the Microsoft 365 outage has no public primary record and ran in the brief; AlienBench was lighter on substance.
- Researcher Q1 (attach the paper's GitHub repo for per-dialogue outcomes): decided no. Work from the paper's tables only.
- Researcher Q2: the paper itself computes the independence product for Opus 4.8 (§4.1.3). Credit the paper for that; the per-model extension is this article's work.
- Angle narrowed on the evidence. The supported finding: most of the fall from per-request to per-dialogue success is compounding over three required passes; follow-up success is what single-request evaluation overstates; observed dialogue completion beats the independence product for every model, so failures cluster, with no evidence on whether shared difficulty or carried-forward error causes it. Do not claim failures cascade. The rubric-versus-success rank disagreement rests largely on one model (GPT-5.4-mini) and is not statistically distinguishable from no relation at n = 9; report it at that strength or drop it. State the paper's own caveat that the follow-up decline may partly be a judge artifact.
- Source floor: writer/01 proved at 3 of 5 sources. Researcher/02 added BFCL v3 multi-turn (blog and leaderboard, one source) and tau2-bench's simulator audit. Decided: use both, each for a claim it owns (BFCL: all-turns scoring, single-turn accuracy as a poor guide to all-turns accuracy, protocol sensitivity; tau2-bench: measured user-simulator error rates). Neither may be used to claim clustering or cascading. MultiChallenge optional. Cut elsewhere to stay under 1,200.
- Editor/01 question (tau-bench pass^8): keep the editor's reading. The tau-bench introduction (arXiv 2406.12045 HTML, §1) says pass^8 drops 'to as low as ∼25%' on retail from ∼61% pass^1, which supports the 25%-versus-1.9% comparison. Approved by editor/01.
