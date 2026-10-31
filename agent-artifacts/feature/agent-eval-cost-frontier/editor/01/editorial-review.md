# Editorial review: feature/agent-eval-cost-frontier (editor/01)

## Correct

Thesis from the draft alone: AstaBench's published cost frontier is mostly a
model-choice curve on one generic ReAct loop, so a plain loop with a current
model reaches the purpose-built agent's score at a fraction of the cost, and
pricing the answers reorders the board.

Claims under it:
1. Ten of the eleven frontier agents are one ReAct loop with the model swapped.
2. A generic ReAct loop with GPT-5.5 reaches Asta v0's score at under half the
   cost.
3. Score ranking and score-per-dollar ranking are different orderings (Opus 4.7
   first by accuracy, 21st of 23 per dollar).
4. The honesty caveats: cost is a token estimate not a bill, tool calls are
   unpriced, every costed row is Ai2's, commercial agents report no cost, the top
   intervals overlap.

Claim 2 broke on the one it most wanted to keep. The draft headline and body
said the loop "beats" Asta v0 and the figure caption called the off-frontier
agents "dominated." The score difference is 52.9 against 50.9, 2.0 points. The
researcher's Appendix D intervals are 52.9 ±3.0 for gpt-5.5 and 50.9 ±2.5 for
Asta v0 (evidence record, Numbers, 95% intervals). The 2.0-point gap is smaller
than either interval, so the two tie on score and the board's strict-domination
flag rests on point estimates the intervals wash out. The real, intact finding
is cost: $1.61 against $3.40, which is 47% (1.6104 / 3.3950 = 0.474, under half).
Fix: the headline verb is now "matches"; the body states the gap is smaller than
the interval and that the separation is cost; the honesty paragraph now carries
Asta v0's own interval (50.9 ±2.5) and says the gpt-5.5/Asta v0 intervals
overlap, so the comparison is backed where it is made. This is narrowing a claim
to what the record supports, not hiding thin reporting: the cost finding stands
at full strength and the honesty section already flagged the overlap.

Claims 1, 3 and 4 held. I recomputed the table and the frontier figures against
the evidence rows: points per dollar (opus-4-7 0.5804/3.5422 = 16.4; gpt-5.5
32.8; Asta v0 15.0; gpt-5.4 66.3; GPT-5 140; o3 231; GPT-5 Mini 857), the ranks
(1/21, 4/17, 5/22, 7/11, 8/7, 9/5, 13/1), the step sums (Mini to GPT-5 +12.0 for
8.4x; GPT-5.5 to Opus 4.7 +5.2 for 2.2x and $1.93), the 26.7-point / 1%-cost gap,
and the frontier span ($0.0359 to $3.5422, factor ~99). All match. The chart
(chart-1.py) plots the live-board rows, not the arXiv table, and the labelled
points match the rows; I did not rebuild it because the data is correct and only
a caption word changed.

Every citation href was audited as printed. All six are Ai2-owned, human-facing
pages (leaderboard, arXiv abstract, agent-eval repo, leaderboard About, blog,
results dataset); the full proof with link checking resolved them (no
--no-check-links). Every `data-nb-kind` is `primary` and correct: the paper is
the Asta team's, the leaderboard and its About page are the same Ai2 app (the
allenai.org address 302-redirects to the hf.space host per the evidence), the
toolkit and dataset are Ai2's repositories. No independent author is claimed.

## Reads well

One sentence went for coming from outside the reporting: "No source I read puts
a price on a tool call" narrated the researcher's own reading in the first
person. Recast as a plain claim about the benchmark: "The tool calls themselves
carry no price." The writer raised this as an open question; this resolves it.

No sentence failed the placeholder test at the section or paragraph edges. The
closing sentence ("It does not show that no agent design could beat that loop,
because the board holds three designs with a cost, all submitted by Ai2") states
a real, checkable limit and survives. The register already sits at the voice
guide's level: figure, then the one thing it licenses. My rewrite of the Asta v0
sentence keeps that habit (the gap, then what the interval licenses, then the
cost).

Checked against the recent-record notes: no "most-quoted figure" deflation dek,
no semicolon-reversal dek, no comma-triad. The dek states this piece's own two
findings with unmistakable numbers (ten of eleven; 21st of 23) and does not
restate the headline, so I kept it. The headings are declarative and built
differently from one another ("AstaBench prices a run's tokens, not its tools" /
"Ten of eleven frontier agents are one loop with the model swapped" / "Opus 4.7
scores first and ranks 21st of 23 per dollar" / "Ai2 submitted every costed row,
and the top intervals overlap"). The new headline is subject-verb-surprise with
the one number that is the surprise, and it survives spec/headlines.md.

## The experience

The rendered page reads top to bottom with both visuals intact: the diagram
shows priced model tokens inside the unpriced tool environment, the scatter
shows the model-swap frontier with Asta v0 off it. The caption second clause now
attributes the off-frontier marking to the board ("the ones it leaves off")
rather than asserting domination in the article's own voice, which matches the
corrected prose.

What the piece gives beyond its sources: it re-ranks Ai2's flat board by
score-per-dollar, shows the frontier is a model-swap curve on one scaffold with
the purpose-built agent matched by a generic loop at half the cost, and states
the overlapping intervals the board's chart hides. That is the draft-handoff's
original-work sentence, and it survives the narrowing.

## Edits

- Headline verb "beats" to "matches" in the `<title>`, the nb-meta title and the
  `<h1>`.
- "No source I read puts a price on a tool call" to "The tool calls themselves
  carry no price."
- Asta v0 comparison: removed "which is 2.0 points higher at 47% of the cost";
  added "The 2.0-point score gap is smaller than the 95% interval on either
  score, so the two tie on score while the generic loop costs 47% as much."
- Intervals paragraph: added "50.9 ±2.5 for Asta v0"; replaced the opus-only
  overlap sentence with "The gpt-5.5 and Asta v0 intervals overlap, so the
  2.0-point gap between them sits inside the noise; the opus-4-7 interval
  overlaps opus-4-6's and sonnet-4-6's."
- Fig. 2 caption: "hollow markers are dominated" to "hollow markers are the ones
  it leaves off."
- Ran `nb stamp` (words 1134).

## Decision

approve. The argument holds once the score claim is narrowed from "beats" to a
tie-within-interval; the cost finding, the model-swap frontier and the re-rank
all stand on the record, and the proof is BLOCK 0 at 1134 words.
