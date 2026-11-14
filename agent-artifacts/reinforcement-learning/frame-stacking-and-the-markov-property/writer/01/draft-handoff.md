# Draft handoff: frame-stacking-and-the-markov-property (writer 01)

## Main idea (lesson template, 30 words)

An entry keyed on an observation that hides part of the state mixes hidden states by the policy's visits; stacking frames that fix the hidden part restores the Markov property.

## Original work

The lesson builds Pitch, where the ball's cell hides its speed, and computes from visit counts the exact fixed point that Q-learning's aliased entries should reach (Singh, Jaakkola and Jordan's equation 4). Runs at five exploration rates then match it. The one-frame entry at cell 2 is the visit share of each speed, so it moves with ε and flips the learned move past ε = 0.55, and cell 3 reads 0.76 although every ball there is hit. A two-frame Gymnasium stack gives the optimal values at every rate.

## Proof

`nb stamp`, then the exact brief command with links: **BLOCK: 0**, verdict PUBLISHABLE. Two warnings are left on purpose:

- W-CITE-DENSITY on `one-frame` and on `exploration`. Both sections are code and runs printed on the page. The series prompt says such sections need no citation and that this warning needs no action there.

Stamped words: 4,774, inside the 2,500 to 6,000 band. Prose by my own count of the rendered text is 2,207. That count includes the title, the dek, the headings and the equation-legend text, and is about 2,160 without them. It sits at the template's 2,200 line, so the editor should recount. To get there I cut a third problem, the Flickering Pong limit and Sutton and Barto's "more Markovian" judgement of DQN.

## Checks (throwaway, rerunnable)

The scripts are in `/tmp/claude-0/nb-fs-writer/checks/` and run with `uv run` beside copies of the lesson files.

- **The page's listings rerun as printed.** I extracted every listing from the built article into `/tmp/claude-0/nb-fs-writer/rerun/` and ran all six printed commands. Every output is byte-identical to the output printed on the page.
- **Fresh seeds and every cell** (`check_seeds_cells.py`). I reran seeds 100–119 at ε = 0.1, 0.5 and 0.7 for both observations, and the conclusions held. At ε = 0.1 one frame hits 0.75 and two frames hit 1.00. At ε = 0.7 one frame hits 0.50. At ε = 0.5, near the crossing, the runs split, with 6 of 20 swinging, against 1 of 20 for seeds 0–19. The page therefore says only "some runs already swing". Across all table entries, including the cells where aliasing cannot act (cell 1, cells 4–9, padded first stacks), run means land within 0.007 of equation (4) for one frame and 0.000 for two frames.
- **Problem 1 checked by run.** Adding a start at cell 2 gives the two-frame agent 13 of 14 hits (0.93). Its padded entry (2, 2) learns (0.48, 0.48) against equation (4)'s (0.5, 0.5). Problem 2 (acceleration, three frames) is worked by hand and was not run.
- **The exact curve** (`curve.py`). At ε = 0, cell 2 is 2/3 and 1/3 and cell 3 is 7/9. The two cell-2 estimates cross at ε = 0.551. Fig. 3's lines come from this curve and its dots from the printed sweep output.
- **SB3 and Gymnasium behaviour** (`sb3_check.py`, run in the researcher's venv). FrameStackObservation turns Pitch's space into MultiDiscrete([10 10]). VecFrameStack raises AssertionError on Pitch's Discrete space (SB3 2.9.2, Gymnasium 1.4.0).
- **Removal tests on the page.** `--frames 2` restores the speed, and every pitch is hit. `--starts 5 7 9` keeps fast balls out of cell 2, and cell 3's entry rises to 1.00.
- **Figures.** I checked every figure and both equations with Playwright at 390 and 1280 px, light and dark. I fixed label collisions in Figs. 2 and 3 and an equation that overflowed at phone width. The page does not scroll sideways at either width.

## Decisions taken without asking

- **Derivation.** The page derives equation (4) as the point where Q-learning's average target stops moving, in the sarsa lesson's style. It attributes convergence only to Singh et al.'s Theorem 2, under a fixed behaviour policy. The Monte Carlo average (their equation 2) gets one sentence, and cell 3 shows that the two differ. The page makes no convergence claim for a changing ε-greedy policy.
- **Exact fixed point.** runs.py's `exact` assumes the agent waits at every cell from 3 up. That holds for both agents, because a swing there always misses. The function says so in its docstring.
- **First-step padding.** Pitch starts every ball out of a fast ball's one-step reach, so the aliased padded stack costs nothing. The page states this, and Problem 1 shows the cost of a nearer start.
- **Actions in the stack.** The page says Sutton and Barto's kth-order history keeps actions. It also says that dropping them is harmless in Pitch, because every action before a swing is a wait.
- **DQN.** The stated reason is attributed to Mnih et al. (perceptual aliasing, with the sequence as the state). The velocity reading is attributed to Hausknecht and Stone. The VecFrameStack bounds finding is not mentioned.
- **No off-the-shelf PPO run.** There was no word budget for one. VecFrameStack gets one sentence, and RL Zoo's velocity-masked tasks are a Go deeper row.
- **Sources left out.** Whitehead and Ballard is cited for the term from its abstract only. I did not cite the first edition of Sutton and Barto, POPGym or Ni et al.
- **Sutton and Barto link.** The source href is https, which the proof requires (B-SOURCES-FORM). The note gives the http copy, as semi-gradient-td does.
- **Model field.** nb-meta `model` is "Claude Opus 5.5", as the brief gives it. Most recent lessons use "claude-opus-5-5".
- **Inline math.** It is written in Unicode, because `nb-math-in` is not in the furniture catalog.

## Open questions

None block the draft. If the editor wants the prose clearly under 2,200 words, the next whole idea to cut is the cell-3 contrast: the paragraph in the derivation section and the `--starts` output under it.
