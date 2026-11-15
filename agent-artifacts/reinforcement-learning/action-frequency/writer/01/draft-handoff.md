# Draft handoff: reinforcement-learning/action-frequency (writer 01)

## Main idea (30 words)

Holding an action for dt changes a smooth system's return by O(dt), so two actions' values differ
by O(dt) while Q-learning's estimation error doesn't shrink; action repeat restores the gap.

## Original work

The lesson checks Tallec et al.'s O(dt) theorem exactly in a new continuous-time environment,
shows tabular Q-learning failing at a fine step and recovering under RepeatAction, and uses
removal tests to credit the recovery to the wider gap rather than to exploration or the horizon,
which no source does for tabular Q-learning.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` (links on):
BLOCK 0, WARN 1, PUBLISHABLE.

- W-CITE-DENSITY on `orientation`, left on purpose. The section is the lesson's own environment and
  run (gap.py output), and the series prompt says such a section needs no citation.

Prose by my count (cards, body, captions, legends, problems; no code, output, equations or
bands) is about 2,270 words. That is a little over the ~2,200 trigger. I already cut whole ideas:
MaxAndSkipObservation, DQN as body text (now problem 2), Metelli/Braylan numbers (Metelli is in
Go deeper only), the options pointer, a third problem, and an unverified "more time doesn't help"
paragraph.

## Code and runs

The lesson files are in `writer/01/code/` (dock.py, gap.py, qcells.py, runs.py), and their saved
outputs are in `writer/01/out/`. The article inlines them verbatim. I extracted every listing
from the built page into `checks/frompage/` and ran it there. gap.py and all four runs.py calls
reproduce the printed output exactly. Figures are inline SVG from `figs/build.py`. Fig. 3 uses
`figs/mapdata.py` (seeds 0–9), and its means match runs.py (0.71, 0.94).
`assemble.py` rebuilt the article from `article.src.html`. Editing the article directly is fine.

Runtime here: gap.py about 1 s. runs.py takes 28 s by default, 8 s with `--repeat 10`, 20 s with
`--explore-repeat 10`, and 26 s with `--tau 0.1`.

## Checks off the page (throwaway code in `writer/01/checks/`, run with `uv run <file>`)

- **New seeds** (`alpha.py 10 20 ...`, seeds 10–19, same settings as the page). At dt 0.01 the
  share is 0.74 and 4/10 runs dock from every start, with spread 0.046. Repeat 10 gives 0.93, 8/10,
  spread 0.016. Explore-repeat 10 gives 0.75, 1/10. Tau 0.1 gives 0.68, 2/10. Dock(0.1) directly
  gives 0.93, 9/10. The conclusions hold. The exploration effect is smaller on these seeds (+0.01
  against +0.08 on seeds 0–9), so the page says "most" of repeat's gain comes from the gap.
- **Other states for the derivation** (`centregap.py`). The exact gap is positive at all 516
  states tested (86 safe cell centres plus 5 random states per cell), so right is optimal there.
  The median |gap/derived − 1| is 4.2% at dt 0.1, 0.4% at dt 0.01 and below 0.1% at dt 0.001. The
  median gap is 0.057, 0.0057 and 0.00057. The (0.5, 0) state is typical.
- **Worst case for the derivation**: the brink state is on the page (Fig. 2, gap.py).
- **Worst case for the Q-learning explanation** (`brink.py`). Brink cells hold some states that
  roll off whatever the agent does. At dt 0.01 they do no better than safe cells (share 0.63
  against 0.71), and at dt 0.1 they do worse (0.75 against 0.92). The finite pointwise gap covers
  only a sliver of a cell about 2|v|·dt wide, so the cell's averaged gap is still O(dt). The
  explanation covers this case, so the page states nothing beyond the 2|v|·dt band.
- **Finer dt** (`brink.py`, 4 seeds at dt 0.001). The safe-cell share is 0.51, a coin toss. It is
  not on the page.
- **Step size and budget** (`alpha.py`, seeds 0–7). At α 0.1 and dt 0.01 the share is 0.73 after
  2,000 s and 0.89 after 10,000 s. At α 0.1 with repeat it is 0.81 after 2,000 s. At α 0.03 both
  are slow (0.57 and 0.59 after 2,000 s). At α 0.3, 10,000 s at dt 0.01 gives only 0.77 (seeds
  10–19). So at α 0.3 the fine step stalls, and at α 0.1 it learns slowly. The page names α = 0.3
  and claims no independence from α (see the open question below).
- **Faint lower-right cells in Fig. 3** (`edge.py`). The neighbouring cells with v in [−1.2, −1.0)
  near the dock get 0–24 visits per run. Their estimates stay near the initial 0, above every true
  value, so left looks good from the bottom start row. The caption says these are cells the cart
  seldom returns to.
- **Pessimistic initial estimates (−1)** tried once. The dt 0.01 share is 0.70 against 0.89 with
  repeat, so the conclusion survives. I reverted to zeros because −1 is tied to τ = 1 and breaks
  the tau test.

## Design decisions the editor should know

- **Crash cost −2, not −1.** With −1 and τ = 1 s, the discretized time cost of never docking
  (dt/(1−e^{−dt}) ≈ 1.05 at dt 0.1) exceeds the crash cost. Doomed states then prefer to crash
  sooner, and left becomes optimal there at coarse dt. With −2, pushing right is optimal in every
  state, so "right is correct everywhere" is exact.
- **The jump is at the back-end brink, not next to the goal.** The commission placed the jump
  "next to the goal boundary". A speed-limited dock would put it there, but the optimal policy then
  brakes along the jump. That makes V_dt carry an O(dt) sawtooth from the discrete switching time,
  as large as the gap itself, which would have spoiled the exact check. Dock's jump is at the
  brink, and problem 1 works through the speed-limited dock, where the jump does sit next to the
  goal.
- **Fixed-policy theorem.** Pushing right is optimal, so Q^π = q*, which closes contradiction 3.

## Open questions

1. **Step size.** Should the page say that a smaller step size learns at dt = 0.01, only more
   slowly? I cut that sentence because no printed output supports it. Adding it needs a
   `--alpha`/`--seconds` flag and one more output block, roughly 40 words plus about 2 minutes of
   runtime.
2. **Prose length** is slightly over 2,200. The next whole idea to cut would be the `--tau 0.1`
   removal test. I kept it because the commission named it.
3. My arithmetic, not a source: the 2|v|·dt band (the stopping point moves by 2|v|·dt + u·dt²), and
   "a flatter V has a smaller gap" (from the derived 2u·dt·∂V/∂v). Both are on the page as
   reasoning, not as citations.
