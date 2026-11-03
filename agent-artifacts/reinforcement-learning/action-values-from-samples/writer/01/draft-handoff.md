# Draft handoff: reinforcement-learning/action-values-from-samples (writer 01)

## Main idea (30 words)

Greedy choice over action values needs no model, so an agent averaging the return after each
(cell, move) pair can improve its policy after every episode, without finishing evaluation first.

## Original work

The lesson turns Sutton and Barto's Monte Carlo ES into a 70-line agent that reuses the course's
own first-visit estimator on (cell, move) pairs, then measures on the course's grid that improving
after every episode does as well as a slower schedule while clearing the averages at each
improvement does not. It also maps the published convergence proofs onto this grid and shows that
none of them covers it.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` (links on):
BLOCK 0, WARN 0, PUBLISHABLE. Stamped: 4,055 words, 18 min, 4 sources.

No warning was left. `W-CITE-DENSITY` on `carried-averages` went away once the section cited
Sutton and Barto p. 97 for policy iteration evaluating each policy, which the section claims.

Prose length is about 2,170 words by my count. That leaves out headings, band and summary labels,
code headers, equations, code, output, text inside drawings and reading bands. Counting headings and
labels it is about 2,260. That is a little over the 2,000 target and below the 2,200 cut line on the
first measure. To get there I cut a third problem (the truncation bound), an "arrows settle before
averages" observation and the SARSA/Q-learning pointer.

## Code and runs

- `mc_control.py` and `experiment.py` ran exactly as printed (`uv run experiment.py`, 2 min 14 s),
  with lesson 1's `gridworld.py`, lesson 2's `control.py` and lesson 3's `estimators.py`, all
  copied verbatim from the published HTML. The printed output on the page is from that final run.
- Figures are inline SVG drawn by `figures.py`, an off-page script in this folder. Fig. 2 re-runs
  seed 0 and asserts its arrows match the printed `run 0 at` lines. Fig. 3 parses the printed
  schedule table. Fig. 1's numbers are in the first two printed lines.
- Rendered checks: `nb preview` plus Playwright at 390 px and 1280 px, in light and dark. There is
  no page-level horizontal scroll. I moved Fig. 3's legend above the plot because on a phone it
  touched the amber line. I turned the proof-status table into a list because its two prose columns
  scrolled sideways on a phone and hid the second column.

## Checks off the page (rerun: `uv run check_seeds.py` from this folder beside the five .py files)

- Unused seeds 100-119 (page uses 0-19). After every episode: 3, 4, 5, 10, 15, 19, 20 optimal at
  1k/2k/5k/10k/20k/50k/100k (page: 2, 3, 6, 10, 12, 16, 18). "Half at 10,000" repeats exactly, and
  "18 of 20 at 100,000" came out as 20. Kept 5,600: 0, 0, 0, 3, 15, 15, 16 (page ends at 18).
  Cleared 5,600: 0, 0, 0, 3, 2, 1, 1. No exploring starts: 0. The page's conclusions hold on these
  seeds. Waiting brings no gain by 100,000 (equal on the page seeds, behind on the new ones). The
  page does not claim the two kept schedules are equal at every checkpoint, because at 20,000 kept
  5,600 led 15 to 12 on seeds 0-19.
- Removal tests on the page: `explore=False` (exploring starts) and `forget=True` (clearing). The
  "kept" schedule is the removal test for "clearing is what costs".
- Worst-fit case for the explanation that cleared averages hold too few returns: clearing with
  50,000-episode evaluations instead of 5,600 gave 9 optimal at 50k and 15 at 100k on seeds
  100-119, much better than 5,600 cleared. That fits the explanation. The cleared-5,600 runs are
  wrong all over the grid at 100k (cells 1, 2, 4, 5, 8, 9, 10, 12, 13, 14, 15), and
  improving-every-episode runs are wrong only at 5 and 10 late on, which matches the 0.35 gaps.
- An independent fast reimplementation (same algorithm, list-based) over 100 seeds gave 0.96
  optimal at 100k and 0.53 at 10k, which is consistent.
- Capped episodes: 84 of 2,000,000 in the main schedule, 36 on the new seeds.

## Open evidence or voice questions

- Delattre and Fournier row: the page says they prove convergence "for first-visit updates in a
  general form that allows random start pairs and greedy steps". That describes their Algorithm 1
  family as the evidence record paraphrases it. That the S&B box itself falls under Theorem 3 is
  the researcher's reading, which the authors do not state. The page does not claim more than the
  family description. I assumed this is acceptable. If the editor wants it tighter, cut "random
  start pairs and greedy steps allowed" back to "first-visit Monte Carlo control".
- Wang et al. row: their Theorem 2 algorithm discards episodes past a cutoff, and `mc_control.py`
  truncates them. The page covers this with "each with its own conditions on step sizes and long
  episodes", and it does not affect the conclusion because the grid is not covered anyway.
- `nb-meta` `order` is set to 4, following lessons 1-3 (orders 1-3). Harness `claude-code`, model
  `claude-opus-5-5`.
