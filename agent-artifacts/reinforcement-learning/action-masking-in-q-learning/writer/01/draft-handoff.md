# Draft handoff: reinforcement-learning/action-masking-in-q-learning (writer 01)

## Main idea (lesson identity, 27 words)

When legal actions depend on the state, Q-learning must mask the max in its target as well as its choices, or never-updated illegal estimates set the values.

## Original work

The lesson derives, and checks with its own runs on a new Gymnasium environment, that Q-learning which masks only its choice solves the Bellman optimality equation of a puzzle where every illegal move ends the episode for its initial estimate. That identifies "mask the choice only" with the episode-ending convention and predicts exactly which values break: every state nine or more moves from the four-disk goal sits at −1. No source in the record states or measures this.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` (links on): BLOCK 0, WARN 1.

- W-CITE-DENSITY on `resting-point`, left on purpose. That section is a derivation plus the page's own printed run, which the series direction says needs no citation.

Prose is about 2,220 words by my count of the rendered page (cards, captions, legends and problems included; code, output, equations, figure text, bands and sources left out). That sits right at the identity's limit. To get there I cut five whole ideas, all checked and listed below: −∞ initialization, check_env's shared-memory failure, a function-approximation sentence, the note that Gymnasium's tutorial never isolates the target, and a three-disk problem. Any of them can come back if the editor trims elsewhere.

## Runs and checks (rerunnable; scratch root `/tmp/claude-0/-home-user-the-nightly-build/84eccc3f-e59d-500c-be1e-12104b5380af/scratchpad/rl-lesson/`)

- Listings exactly as printed: `verify/` holds hanoi.py, masked_q.py and leak.py extracted from the article HTML. `uv run hanoi.py` and `uv run leak.py` reproduce the printed output byte for byte. leak.py takes about 40 s here.
- New seeds (`page/`: `cp ../check_seeds.py . && uv run check_seeds.py 5000 5 15`). Seeds 5–14 give the same conclusions. Legal target: the start is solved in 15 moves in 10 of 10 runs, and the fewest moves are taken from 79.9 starts on average (one run misses one start). Target over all six: the start is solved in 0 of 10 runs, 29.0 starts, 147.5 moves with ties broken at random. Init −10: tables identical. The page reports seeds 0–4 only.
- One cell or one seed (`explore3.py`, seeds 5–14). Under the target over all six, every legal estimate in states nine or more moves out is exactly −1.0 in every run. The greedy path from the start is 0→1→7→6→7… in every run. The 29th start is state 12, nine moves out, whose first legal move happens to be optimal. The page states this without the numbers.
- Removal test (on the page): every estimate starts at −10 = −1/(1−γ), and the two targets' tables are identical (largest difference 0.0).
- Worst-fit cases. Inside the four-disk run, all 28 starts within eight moves are solved in the fewest moves, which matches the derivation. With three disks (`three/ident.py`), every value is ≥ 0.63, the resting point equals q* exactly, and the two targets' rows match to two decimals. With optimistic init +10 (`verify/check_optimistic.py`), the target over all six rests 0.017 from the predicted point, where every value beyond one move is 8. Its greedy agent takes the fewest moves from only 4 of 80 starts. The masked target reaches q* (0.02) and all 80 starts. This covers the commission's "vary initialization and reward sign" check.
- −∞ for illegal estimates (`throw_inf.py`). With the choice masked, it is identical to masking the target. With unmasked exploration, the first NaN appears at step 5, and 261 table entries are NaN after 50 episodes. Cut from the page for length.
- Conventions, for the Problems answers (`page/check_conventions.py`). Under the no-op convention, an agent that ignores the mask learns q* on the legal pairs (error 0.10–0.14 at 5000 episodes), solves from the start in 15 moves and never picks a no-op. Under "an illegal move ends the episode with 0" (40,000 episodes), the legal estimates end 0.067 from the choice-only resting point, and the greedy agent ends the episode at once from exactly 54 states.
- API statements, all run with gymnasium 1.4.0. `Taxi-v3` raises DeprecatedEnv and `Taxi-v4` works. Taxi's `info["action_mask"]` is an int8 array. `Discrete.sample(mask=bool_array)` raises an AssertionError with "The expected dtype of the sample mask is np.int8, actual dtype: bool". An all-zero mask returns 0. check_env passes Hanoi with only the render-modes warning. check_env fails an environment whose info returns rows of one precomputed mask table ("share an object"; `throw_shared.py`). No run contradicted evidence.md.
- Locators: I fetched the raw sources and confirmed the line numbers I cite. These are taxi.py 113–141 and 417, env_checker.py 204/218, 273–303 and 478, discrete.py 154–156, sb3-contrib utils.py 5–19, OpenSpiel pytorch/dqn.py 444–459 and 541–552, and HLE dqn_agent.py 18–19 and 230–238.
- Fig. 2 is drawn by `figs.py` (off the page) from run 0 of leak.py's first two rows, with the same code and seed. Its colours match the printed resting points: −1.00 beyond eight moves for the target over all six.

## Open questions

- None on evidence. The record had nothing on the page's central measurement, so that comes entirely from the printed run and the derivation, as the commission expected.
- MaskablePPO appears only in the Why card and in one sentence on `action_masks()`. The environment exposes both conventions, so the later lesson can import `hanoi.py` unchanged.
