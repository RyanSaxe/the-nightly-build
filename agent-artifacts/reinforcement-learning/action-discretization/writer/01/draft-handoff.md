# Draft handoff: reinforcement-learning/action-discretization (writer 01)

## Main idea (30 words or fewer)

More torque levels raise the best return a policy over them can reach, but a
fixed budget then spreads its updates over more action values, so small
budgets favour few levels.

## Original work

The lesson derives that a level δ from the best torque costs about C·δ² a step
(bound 200·C(Δ/2)² per episode), checks it against an exact backward solve per
k on a dearer Pendulum-v1, and measures where tabular Q-learning's best k sits
at three budgets, with removal tests separating updates per action value from
exploration.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`
with links checked: BLOCK: 0, WARN: 2, verdict PUBLISHABLE. After that run I
changed only the TeX layout of two equations (an ≈ in place of "+ O(δ³)", and
the backward solve split over two lines) and one equation caption, rebuilt
and re-stamped (4,763 words, 21 min, 4 sources). The shell's permission check
then stopped answering, so the proof was not rerun on that final file; please
rerun it once.

Visuals looked at after `nb preview` with Playwright at 390 px and 1280 px, light
and dark: no horizontal page scroll, no overlapping labels; two equations that
overflowed a phone were reset to fit.

Warnings left on purpose:

- W-CITE-DENSITY on `ceiling` and `learning`: both sections are made of the
  lesson's own solve, runs and printed output. The series prompt says no action
  is needed there.

Display text checked against the runs and the record: headline, dek and
headings carry only 3 / 5 / 9 levels at 60,000 / 200,000 / 600,000 steps
(learn.py output) and "a thousand times" (1.0 against Pendulum-v1's 0.001,
pendulum.py line 136 in the record). The nb-meta dek and the rendered dekline
are the same string.

## Where things are

- Lesson code: `code/` in the workspace (pendulum.py, ceiling.py, learn.py),
  run from that folder with `uv run <file>`. Printed outputs: `runs/`.
- The article is assembled by `figures/build.py` from `figures/article.src.html`
  (it escapes the code and outputs and inlines the SVGs). Edit the HTML
  directly from here on, or edit the source and rerun `python3 build.py` then
  `nb stamp`; build.py overwrites the HTML. The figure scripts (catch.py,
  qmaps.py, dpmap.py write data; fig_*.py draw) only draw and stay off the page.
- Throwaway checks and their outputs: `checks/`.

## Decisions taken without a ruling (questions for the orchestrator)

1. **Near-upright starts, a second change to Pendulum-v1.** Episodes start
   within 0.3 rad of upright and 0.5 rad/s, through Pendulum-v1's own reset
   options (`x_init`, `y_init`, record: pendulum.py lines 149-167), on top of the
   torque cost. Reason: on the full swing-up a table a laptop can fill does not
   get near the ceiling. With C = 1.0, a 31 × 31 table, γ 0.95 and up to 600,000
   steps, learned returns were −550 to −1200 against ceilings of −185 to −230,
   and an aggregated-model value iteration on a 61 × 61 table (the model known)
   reached only −246 to −407. With near-upright starts the per-k shortfalls are
   the same as on the full task (the loss is in the catch), and Q-learning
   approaches its plateau within 200,000 steps. The page says the starts keep
   episodes in the region the table covers; it does not mention the swing-up
   attempt. If you want the full task, the lesson needs a much larger budget or
   a different learner.
2. **C = 1.0, not 0.1.** At 0.1 the ceiling gains beyond 3 levels are a few
   return units (5.1, 1.3, 0.7), far below the learning noise, so no budget
   showed fine levels winning. At 1.0 the gains are 45, 12, 3, 1.7 and the best
   learned k moves with the budget.
3. **Result count.** Result 2 is one set of runs read at three budgets
   (checkpoints of the same runs). I count it as one result; the removal tests
   (`--explore-ends`, `--per-level`) belong to it. The stock-cost solve is one
   sentence plus Seyde et al. on the page; its output is in `runs/ceiling-stock.txt`.
4. **Length.** Prose is about 2,450 words by my count (cards, captions, problems
   and headings included; code, output, equations, figure text and reading
   bands excluded), over the identity's 2,200. I cut the stock-cost output, a
   third problem and an explanation of optimistic zero estimates. The next whole
   pieces to cut would be Fig. 3 with its two sentences (it is the only figure of
   what the agent learned, which the series asks for) or problem 2.

## Checks run off the page (rerun from `checks/` or `code/`)

- **New seeds.** `uv run learn.py --seeds 5 6 7 8 9` (`runs/learn-seeds-5-9.txt`):
  same best sets (3, 5, 9). At 600,000 steps 9 levels beat 5 in both seed sets
  but by less than one sd; the page says so.
- **Per-level test on ten seeds.** `uv run checks/perlevel_seeds.py`
  (`checks/perlevel_seeds.txt`): on seeds 5-9 one 9-level run (−635) and one
  17-level run (−1368) collapsed, so those means are −177 and −344; the medians
  (9 levels −63, 5 levels −77) keep the conclusion that equal steps per level
  bring 9 level with 5. Seeds 0-4 per seed for 17 levels: −47, −138, −38, −44,
  −328, which is the run the page says still drops the rod.
- **Grid of the solve.** ceiling.py at 181 × 161, 361 × 321 (page) and
  541 × 481 (`checks/ceiling_541.txt`): shortfalls for k = 2, 3, 5, 9, 17 of
  791.1/45.8/11.9/7.0/2.2, 791.5/45.0/11.6/2.9/1.65 and 791.5/44.7/11.2/3.5/1.1.
  k = 3 and 5 are stable; k = 9 and 17 move by about 0.6 between the two finer
  grids, which is the "grid error" the page cites for 17 levels. A box grid
  clamped at |θ| ≤ 1 found worse 3- and 5-level policies (`checks/box*.txt`);
  not used.
- **Bound across costs** (full swing-up starts, 181 × 161 grid, throwaway): the
  shortfall stays under 800C/(k−1)² for C = 0.03, 0.1, 0.3 and 1.0 at every k,
  and fails only at Pendulum-v1's 0.001 (k = 2: 1.5 against 0.8), where κ
  dominates. The page states the failure at 0.001 in terms of κ only in the
  bound's "to leading order" wording.
- **Worst-fit case for the explanation.** Where the ceiling side cannot act,
  Pendulum-v1's own cost, `uv run checks/stock_learn.py`
  (`checks/stock_learn.txt`): 2 levels best at 60,000 and 200,000 steps, 3
  levels best at 600,000 (−0.9 against −2.4), as the per-level rule predicts
  (3 levels add 1.1 to the ceiling and win once they finish learning). Two
  levels, which have the most updates per value but the worst ceiling under
  C = 1, sit at their ceiling of −802 from 200,000 steps, which the ceiling
  side explains.
- **Physics copy.** `uv run pendulum.py`: largest difference from env.step over
  1000 random steps 1.9e-10 (float32 rounding of 0.001 inside Pendulum-v1).

## Evidence or voice questions

- The researcher's record has no source for tabular Q-learning on Pendulum-v1
  across bin counts; the page's learning numbers are its own runs only.
- DecQN's "likely to delay convergence" is attributed by its authors to
  exploration over more options, not to updates per value, so I left it out of
  the body and kept the paper in Go deeper.
