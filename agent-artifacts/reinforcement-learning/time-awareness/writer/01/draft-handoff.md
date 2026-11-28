# Draft handoff: reinforcement-learning/time-awareness (writer 01)

Writer: Claude Opus 5.5 (claude-opus-5-5), harness Claude Code (nb-meta `claude-code`).

## Main idea (29 words)

When a time limit belongs to the task, the moves left are part of the state, so the agent must observe them, and the last move is a termination.

## Original work

The lesson computes the four-move task's exact time-indexed values by backward induction (value iteration's first four sweeps), finds that cell 5's best move flips from left to up once three moves remain, and shows that a cell-only Q-learner with the correct terminated flag learns, entry for entry, the table termination-and-truncation's mistaken loop learned, so the same numbers are wrong here for a different reason and need a different fix: the observation, not the target.

## Proof

`nb check .../time-awareness.html --series reinforcement-learning --repo /home/user/the-nightly-build` (links included): BLOCK 0, WARN 0, PUBLISHABLE. No warning left. `nb stamp`: words 3929, 17 min, 8 sources. My own count of prose as the identity defines it (no code, output, equations, SVG text, bands or sources) is about 2,100 words.

## Run environment (deviation)

`uv run` is blocked here. Both listings ran with the prepared interpreter (Python 3.11.18, gymnasium 1.4.0, numpy 2.4.6). Their inline metadata pins `gymnasium==1.4.0`, `numpy==2.4.6` and `requires-python >=3.11`, because numpy 2.4.6 needs Python 3.11. I extracted both listings from the rendered HTML and ran them in a clean folder with the printed files of the earlier lessons. The output matched the printed output byte for byte. `moves_left.py` takes about 34 s here.

The workspace `code/` folder holds the listings, their captured output, `figures.py` (off-page, draws Fig. 1 and Fig. 2 from `moves_left.py`), and `checks/`. The article HTML is now the source of truth. I built it from a scratch template, and edits go into the HTML directly.

## Checks kept off the page (rerun from `code/checks/` with the same interpreter)

- `seeds.py 5 10 0.5` reruns `moves_left.main` on unused seeds 5-9. Time-aware: 0.66 and the right switches at cells 5 and 10 in every run. Cell-only: 0.20-0.38, wrong at cell 5, cell 10 or both in every run. `seeds.py 0 3 0.2` and `seeds.py 0 3 1.0` give the same conclusion at eps 0.2 and 1.0. The cell-only agent was never right at both 5 and 10 in any of the 16 runs (seeds 0-9 at eps 0.5, and three seeds at each of the other two rates).
- `checks1.py` confirms that the cell-only table is bit-identical to `q_learning(TimeLimit(SlipperyGrid(), 4), ..., cut_is_terminal=True)`. It also confirms the researcher's unexecuted reading of `TimeAwareObservation(TimeLimit(SlipperyGrid(), 4))`: a `Box(0, [1]*16+[4], (17,), int64)` observation, elapsed count last, `truncated=True` on move 4, and a ValueError without the inner TimeLimit. The table identity is also printed on the page.
- `checks3.py` covers mechanism and worst case. Forcing the cell-only policy to up at cell 5 and right at cell 10 cuts its loss from 0.29-0.46 to 0.131 in all 10 seeds. Most of the loss is those two cells. The starts at cells 2 and 7, whose best move never changes with the moves left, lose 0.00 in every run, and that is printed on the page.
- `stationary.py` is not on the page. The best one-move-per-cell policy I found by coordinate ascent (200 restarts, all agreeing) earns 0.587 against the optimum 0.664. So no cell-only table can reach the optimum, and the cell-only learner (0.20-0.35) falls well below even that. I cut it for length, and it can come back as one sentence if the editor wants the split between what the representation costs and what the learning costs.
- `p2.py` backs Problem 2. With a time-aware observation and the limit reported as truncated, bootstrapping matches terminated exactly from a zero start. From a start of 5 the error goes from 0.12 to 3.43 and the return to -0.03, while the terminated version stays at 0.66. The page states only the derivation, so no run numbers appear there.
- `check_env` passes on `FourMoveGrid(see_time=True/False)` with only the render-mode warning that `SlipperyGrid` also gets.

## Decisions and open questions

- The decisions after researcher/01 are followed. The page shows only the Section 2.2 time-unaware failure, and Section 3.1 PEB appears only as the earlier lesson's fix and in Problem 2. The page says "moves made" (elapsed) for TimeAwareObservation, and the environment reports terminated itself.
- No grid extension was needed. Backward induction gives cell 5 (and its mirror, cell 10) a strict switch: left with one or two moves left, up with three or four.
- Sutton and Barto (s2) links the MIT Press page with a note on the free copy, as termination-and-truncation did. The proof requires https, and the evidence's http PDF URL fails. https://incompleteideas.net did not answer through this proxy.
- I cut one sentence for length: TimeAwareObservation's parameter docs say "remaining", but its code counts elapsed steps (evidence Contradiction 1). The page says "moves made" and shows the output, so a reader isn't misled. The editor may restore the sentence.
- I looked at both figures in light and dark at 390 px and 900 px through `nb preview` and headless Chrome, since Playwright isn't installed and uv is blocked. The target equation was split over two lines to fit a phone. Fig. 1's small text is about 9 px on a phone, which is legible.
- No open evidence or voice questions.
