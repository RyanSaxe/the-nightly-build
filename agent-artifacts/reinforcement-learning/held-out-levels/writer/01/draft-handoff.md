# Draft handoff: reinforcement-learning/held-out-levels (writer 01)

## Main idea (30 words)

Training-level return cannot reveal memorization; held-out levels from the same
generator can, and held-out return reaches training return only when the
observation shows what varies and enough levels are trained.

## Original work

The lesson derives, by swapping a maximum and an average over levels, why no
number of training levels lifts a policy of the current observation above the
best single policy for the generator, and checks it on a seed-keyed grid where
the position agent's gap closes only because its training return falls while
the view agent's closes because its held-out return rises, with a removal test
that hands the views a table never met to a fixed rule.

## Proof

`nb stamp`, then the brief's `nb check` with links: BLOCK 0, WARN 2,
PUBLISHABLE (stamped 4,109 words by the engine's count, 18 min, 7 sources).

Warnings left on purpose:

- W-SENTENCE-DENSITY, "43 words with punctuation score 38": the sentence is the
  TeX source of the bound's `nb-math-eq` (`\begin{aligned} ...`), which the
  heuristic reads as prose. No prose sentence triggers it.
- W-CITE-DENSITY on `view-levels`: the section is the lesson's own runs and
  their removal test; the series prompt exempts such sections.

Word count (my count of rendered prose, including captions, cards, legend and
problems, excluding code, output, drawings, bands and sources): about 2,255
with the title and dek, about 2,205 without. Above the 2,000 aim and at the
2,200 cut line; already cut to two problems and one level-count sentence.

## Runs (all from `/home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/work/`)

Page listings: `levels.py` and `heldout.py`, run exactly as printed with
`uv run` (gymnasium 1.4.0, numpy). Both listings were extracted from the built
article into `work/asprinted/` and rerun there; both outputs match the printed
ones byte for byte.

- `uv run levels.py` (seconds): check_env on both observations, first
  observations on levels 1000 and 100008, toward_goal 500/500 shortest routes
  on held-out seeds 100000-100499.
- `uv run heldout.py` (2 min 18 s on one core): runs 0-9; run k uses seed k
  and training level seeds 1000k .. 1000k+n-1, n in 1, 4, 16, 64, 256;
  held-out seeds 100000-100499; 3,000 episodes, eps 0.1, step 0.1, gamma 0.9,
  limit 40. The last column is the removal test (views missing from Q handed
  to toward_goal).

Checks (throwaway, off the page; scripts in `work/figs/` unless noted):

1. New seeds: `uv run heldout.py --runs 10 11 12 13 14 15 16 17 18 19`
   (`work/check_runs10-19.txt`). Same conclusions: position training 1.00 ->
   0.05, held-out 0.04 throughout; view held-out 0.11 -> 0.99, within 0.01 of
   training from 64 levels; one-level fill 0.77 [0.36, 1.00].
2. Second held-out set: `uv run heldout.py --held-out 200000`
   (`work/check_heldout200000.txt`). Every mean within 0.03 of the main run.
3. Twenty runs of the view agent at n = 1, 16, 64 (`view20.py`): one-level
   fill ranges 0.26-1.00 (about half the runs at 0.95 or more); at 16 levels
   runs 5, 13, 18 fail some of their own training levels (0.50-0.75), and
   their held-out return falls with it. The page states the lowest run and
   gives the conclusion; the spread did not change the conclusion.
4. Worst case for the missing-views explanation: run 5 (one level, filled
   0.26). Its learned entries move away from the goal, e.g. view
   (0,0,0,0,2,2) -> left (`fillcheck.py`). The page says only that its learned
   entries lead it astray, which follows from the fill test itself.
5. Route rule for the position agent: "solves a held-out level iff the goal is
   on its empty-grid greedy route before any wall" agrees with play on 500/500
   held-out levels for run 1 and for run 0 (`paths.py`, `RUN=1` / default).
6. The view at (0, 3) on level 100005, (1,0,1,0,2,2), is absent from run 1's
   one-level table of 21 views (`missing.py`).
7. Episode budget: 6,000 episodes steadied 16 levels over 20 runs but one
   64-level run collapsed (0.47 training, 0.34 held-out) (`view20e.py`).
   Count-based step sizes N^-0.7, N^-0.5 and a step of 1 were no better
   (`stepsize.py`). Kept 3,000 episodes and a constant 0.1.
8. Position ceiling, not on the page: a 40-move route found by hill climbing
   solves 0.14 of the held-out levels (`routes.py`), so Q-learning's 0.04 sits
   below what one fixed route can do; the bound only says no position policy
   reaches the per-level optimum, and the page claims no more.
9. Generator: of 7,000 seeds, 2 leave room for only five walls (hence "up to
   six walls"; count script in the session scratchpad, logic as `make_level`).

Figures: Figs. 1 and 3 are drawn by `work/figs/figures.py` from run 1's
agents (seed 1; levels 1000, 100066, 100005, 100008); Fig. 2 by
`work/figs/chart.py` from `work/out_main.txt`, checked against the printed
output (means and run ranges). Looked at phone and desktop width, light and
dark; no horizontal page scroll.

## Open questions

- The strictness step of the bound uses the discounted optimum (a shortest
  route) while the printed score is the 0-or-1 return within 40 moves. The page
  says "Under the agents' discount"; the bound itself holds for either return.
- Recurrent policies are named as a later stage without a lesson link, since
  none is published yet.
