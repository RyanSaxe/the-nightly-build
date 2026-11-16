# Draft handoff: feature/toolturns-multi-turn-agents (writer 02)

## Original work

Unchanged from 01. The paper cubes one model's pooled rate (Opus 4.8). This article multiplies each model's three per-position rates, shows all nine completing 5.8 to 8.4 points above that independence product, and then shows that cubing the opening rate lands within 3.3 points for eight of nine models only because the follow-up decline (factor 0.59 to 0.94) and the clustering (factor 1.19 to 1.51) offset. It also reports the rubric-versus-success rank disagreement at its actual strength (GPT-5.4-mini; p = 0.55 at n = 9).

## Proof result

After `nb stamp` (1,196 words, 5 min, 5 sources), the exact proof command with links included: BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `W-SOURCES-MIN` is cleared with five real sources, each carrying a claim. Rendered with `nb preview` and Playwright at 390 px (light) and 1280 px (dark): Fig. 1 and the new BFCL paragraph render cleanly, and there is no sideways page scroll.

## Revision lines

- BFCL v3 multi-turn (new s5, closing section): carries the all-turns scoring rule (same rule as all-three-pass), single-turn accuracy as a poor guide (all 75 entries at or above 80% single-turn score lower on multi-turn, 0.4% to 77.4%, marked as my computation from the leaderboard data of 16 November and as different task sets), and protocol sensitivity (Claude Opus 4.5: 68.4% native function calling against 16.1% prompt mode at 88.6% and 89.7% single-turn). The paragraph states that BFCL publishes no per-turn rates and cannot test clustering. I used the researcher's cleaner "all 75" statement and not the rank correlation. BFCL's stop-at-first-failed-turn design is stated in a clause so it is not read as a cascade finding.
- tau2-bench (new s2, orientation): carries only the measured user-simulator error rates (40% retail, 47% airline, 12% and 13% critical, from Table 2), with the caveat that it is another simulator on other tasks and not a rate for ToolTurns. It is not used for clustering. Sources renumbered into first-citation order (ToolTurns, tau2-bench, Laban et al., tau-bench, BFCL).
- Cuts to stay under 1,200 (Fig. 1 judge line, Fig. 2 caption clause, Fig. 3 and Fig. 4 caption fragments, the range sentence in the follow-ups section, the Laban restatement, the problem-140 sentences and the paper's rubric quote, the efficiency clause, the clustering restatement, a few connective words). The Fig. 1 viewBox height was reduced to fit. The rubric section now cites no problem 140, which is a loss of one concrete case.
- No new evidence was added. MultiChallenge was not used.

## Open items for the editor

- The sentence "That is another simulator on other tasks, not a rate for ToolTurns" rests on the researcher's note that tau2-bench's audit used gpt-4.1 on its own retail and airline versions. The article does not claim that ToolTurns has no audit, only that the checker-fixer was not tested against agent scores (unchanged from 01).
- "Same rule as all-three-pass" compares BFCL's every-turn rule (state and response checks per turn) with ToolTurns's three-subtask rule. The rule shape matches. The tasks do not.
