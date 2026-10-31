# editor review-brief: feature/agent-eval-cost-frontier (editor/01)

Inputs:
- `../../editorial-direction.md`
- `../../commission.md` (read the "Angle revised after research" section)
- `../../writer/01/brief.md`
- `../../writer/01/draft-handoff.md` (two open questions for you, below)
- `../../writing-coach/01/voice-guide.md`
- `../../researcher/01/evidence.md` (the live leaderboard numbers and the Limits)
- The article: `/home/user/the-nightly-build/.nb-work/feature/agent-eval-cost-frontier/library/feature/agent-eval-cost-frontier.html`
- The chart script: `.../library/feature/agent-eval-cost-frontier/chart-1.py`
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/agent-eval-cost-frontier/library/feature/agent-eval-cost-frontier.html --series feature --repo /home/user/the-nightly-build`
Output: `editorial-review.md` in `editor/01/`

Decide whether this publishes and edit it until it can. The writer reports a
clean proof at 1097 words, 6 primary sources, and both visuals rendered.

Press hardest here, on the claim you most want to keep:
- **The headline says a generic ReAct loop with GPT-5.5 "beats" Asta v0.** The
  evidence record puts that score lead at about 2.0 points, and the 95% intervals
  it reports are about ±2.4 to ±3.0 points, so the lead sits inside the noise.
  Check this. If a 2.0-point lead is within the interval, "beats" and any claim
  that Asta v0 is strictly "dominated" overstate the data. The defensible finding
  is the cost: a generic ReAct loop with a current model matches or edges Ai2's
  purpose-built agent at under half the cost. Rewrite the headline, dek and body
  to what the numbers support without losing the real point, and confirm the
  rewrite against spec/headlines.md.
- **Recompute the orderings** against the evidence Numbers: Opus 4.7 first by
  accuracy and 21st of 23 by score-per-dollar; GPT-5 Mini 26.7 points behind at
  ~1% cost; +12 points for 8.4x. Confirm the chart (Fig. 2) and the table plot
  the live-board numbers, not the arXiv table, and that labelled points match.
- **The honesty caveats must stand and be correct:** cost is logged tokens times
  a frozen price table (a token estimate, not a billed amount); tool calls are
  not priced; all costed rows were Ai2-submitted; commercial agents report no
  cost; the top intervals overlap and the board shows no error bars.

The writer's two open questions for you:
1. Whether LLM-judge calls count toward cost is not stated by the paper; the
   piece claims nothing either way. Keep it that way unless you find the source.
2. The sentence "No source I read puts a price on a tool call" is first-person
   and rests on the researcher's reading. Recast it as a plain claim about
   AstaBench ("AstaBench prices model tokens, not tool calls", from the paper
   §4.2) or cut it; the piece never narrates its own research.

Also: audit every citation href as the article prints it and every
`data-nb-kind` (a different website is not an independent author), read the
rendered page top to bottom for slop at the section and paragraph edges, and
check the dek and the 3-5 headings against spec/headlines.md and against the
recent-record notes in the commission (avoid the "its most-quoted figure"
deflation dek, the semicolon reversal and the comma-triad; headings built
differently from one another). Strict series: the word band 600-1200 and the
banned-term limits BLOCK, so keep edits inside the band and re-run the proof.

Make the edits you can from the evidence and this checkout; after edits run
`nb stamp` and the proof command yourself to BLOCK: 0. Return to me (the
orchestrator) only if a claim needs a fact nobody gathered. Report the review
path, the decision (approve | redraft), the final proof result and word count,
and what you changed in the headline/dek.
