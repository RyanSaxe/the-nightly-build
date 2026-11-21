# Draft handoff: reinforcement-learning/reward-scale (writer 01)

## Main idea (30 words)

Multiplying every reward by a positive constant keeps the optimal policy;
clipping changes reward ratios and an added constant changes episodic returns
by episode length, so both can change it.

## Original work

The page derives the scaling result and the shift result that Sutton and Barto
only pose as exercises and Ng, Harada and Russell only state in a footnote, then
builds a new courier grid on which value iteration and Q-learning show clipping
and added constants moving the optimal route while a factor of 100 cannot.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`
with links: BLOCK 0, WARN 0. No warning left. Stamped: 4,304 words (code and
output included), 7 sources. Rendered prose is about 2,100 words by my count
(about 2,250 if every number counts as a word), so near the 2,200 line; I cut a
third problem (scale plus shift) and trimmed the normalizer and shaping
paragraphs to get there.

Figures checked in Playwright at 1200 px and 390 px, light and dark; no
horizontal scroll. Figures are drawn by `work/figures.py` from value
iteration's output (not on the page).

## Runs and checks (all from `.nb-work/reinforcement-learning/reward-scale/work/`)

- Listings: both were extracted from the article HTML into an empty folder and
  run with `uv run courier.py` and `uv run learn.py`; output is identical to the
  printed output. learn.py takes about 40 s here.
- On the page, learn.py: seeds 0-4, 20,000 episodes, every row 5 of 5 on
  delivery and on optimal moves, largest |Q - q*| 0.000.
- New seeds (`sh checks/seeds.sh`, first variant): seeds 5-19, 20,000
  episodes, every row 15 of 15 on both grades, error 0.000.
- Short budget (second variant): 2,000 episodes, seeds 0-19: delivery 20 of 20
  on every row; optimal moves 20 of 20 except fuel-free 18 of 20 (a
  non-optimal move that still delivers far); errors 2.0 dollars, 177 cents,
  0.48 clipped, 4.9 fuel-free, 6.2 hourly.
- Worst case for the explanation (`checks/gaps.py`): the closest near-versus-far
  calls are the three near cells under dollars (cells 14, 21, 22, gap about
  0.05, e.g. cell 14: near 1.00, far 0.95). Every run gets them right at 2,000
  and at 20,000 episodes.
- Cut treated as terminal (third variant), the case where bootstrapping at the
  time limit matters most: the hourly agent still never delivers in 5 of 5
  runs, with error 2.6 since its target now stops at the cut.
- Removal tests are on the page as rows: clipped against dollars (far fee 1
  against 10), hourly against fuel-free (+1 against 0 per move).
- Cents against dollars in Q-learning (`checks/diverge.py`): with the same seed
  the two runs make identical moves for 43,000 to 62,000 moves, then part at an
  exact tie between two equally optimal moves (cells 10, 11, 18; up against
  right), through floating-point rounding. The page therefore states the
  invariance of Q-learning from 0 as a derivation and prints no proportionality
  check.
- Problem answers (`PYTHONPATH=. uv run --with gymnasium==1.4.0 --with numpy
  python checks/problems.py`): Problem 1 near 0.18, far 0.6086, sign gives the
  clipped map and near from the depot; Problem 2, fee + 40 gives q* = dollar q*
  + 40 to 1.4e-14 with the same deliveries.
- Gymnasium's `check_env` passes on `Courier` (only the no-spec render warning).

`work/article.src.html` plus `work/assemble.py` built the article from the
scripts, their output and the SVGs. If you edit the article directly, do not
rerun assemble.py, which would overwrite it.

## Open questions

- Commission's practical point said Q-learning's starting estimates of 0 are
  optimistic or pessimistic only relative to the reward's size. Under a
  positive scale 0 stays 0, and tabular Q-learning from 0 is exactly unchanged
  by scale. The page makes the point with a nonzero start instead (Sutton and
  Barto's +5, p. 34) and keeps it to one paragraph, not a result.
- The Baselines issue #538 reason is paraphrased, not quoted, because the
  record asks for the page to be reopened before quoting.
- SB3 is one source entry whose href is the v2.9.2 vec_envs guide; the
  ClipRewardEnv locator names `common/atari_wrappers.py`, since the record gives
  no separate URL for it.
- Ng et al. use the record's ai.stanford.edu PDF with PDF page numbers. The
  shaping lesson cited a Berkeley copy with proceedings pages it assumed.
- DQN is described as clipping to [−1, 1] (Mnih); the page says SB3's
  ClipRewardEnv takes the sign and where the two differ, and Problem 1 uses the
  difference.
