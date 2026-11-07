# Draft handoff: reinforcement-learning/checking-a-custom-environment (writer 01)

## Main idea (27 words)

check_env tests only form; a wrong rule shows when a baseline's average return misses the value solved from the rules, and each baseline is blind to some errors.

## Original work

The lesson turns the checker's source and the course's exact solutions into a test bench. It builds copies of SlipperyGrid with one mistake each, and check_env passes the ones with rule errors. A two-line sum shows why uniformly random moves can never see a slip-direction or relabelling error while a policy that favours some moves can. The runs confirm the sum and its removal test, `up_or_right`.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`, links included: **BLOCK: 0, WARN: 3, PUBLISHABLE.** Stamped words 4399 (band 2500–6000), 10 sources.

Warnings left on purpose:
- W-SENTENCE-DENSITY (65 words). The "sentence" is the TeX source of the display equation in `uniform-aims`, not prose. I confirmed this with the engine's own `sentence_density` on the article text.
- W-CITE-DENSITY on `baselines` and `uniform-aims`. Both sections are the lesson's derivation and its own printed runs. The series direction says W-CITE-DENSITY needs no action there.

Prose is about 2,150 words by my count. That count leaves out code, outputs, display and inline math, SVG text, the reading bands and the sources list. To get there I cut two whole side ideas:
- The episodes-needed arithmetic, (3 sd/Δ)² ≈ 700 for the hand-drawn policy.
- The discounted-return bound [−20, 10]. It bounds every value, so the next lesson can use it on the agent's value estimates.

## Code, seeds and checks

Lesson code is in `/home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/code/`. The course files there were extracted verbatim from the published lessons. This lesson's files are `bugs.py`, `baselines.py` (importable names `random_policy`, `hand_drawn`, `exact_value`, `EXACT`, `returns`), `checker.py`, `behaviour.py` and `play.py`. Every listing was rerun exactly as printed, from a fresh folder holding only gridworld.py, estimators.py, mc_control.py, grid_env.py and those five files. All outputs are byte-identical to the page, and `uv run bugs.py` and `uv run baselines.py` exit cleanly. behaviour.py takes about 7 s.

The throwaway checks are in `/tmp/claude-0/-home-user-the-nightly-build/fb40cc08-66d0-53e1-a6c3-bfcb111cfc68/scratchpad/cce/explore/` (exact.py, blind.py, seeds.py). The figures come from `../figs.py`, which reads the saved behaviour.py output. `../build.py` assembles the article from `article.src.html`, the code folder and the saved outputs.

1. **Seeds for behaviour.py.** Seed 0 is on the page. Seeds 1–9 were rerun with `uv run behaviour.py N`, and the flag pattern was identical in all ten:
   - On the correct copy nothing was flagged. The largest |z| was 2.1 (hand-drawn, seed 4).
   - On SlipBack the random row was never flagged (|z| ≤ 2.4, seed 3). The hand-drawn row was always flagged, z 6.2 to 9.2, and so was up_or_right, z −5.6 to −9.2.
   - On NeverEnds every row was flagged, |z| ≥ 19.8.
2. **checker.py.** Five runs gave byte-identical output. The unseeded action at env_checker L478 changes neither the verdicts nor the cells, which are always [0, 8].
3. **The derivation, checked by exact solve (blind.py).**
   - The random policy's transition matrix is unchanged (max |ΔP| = 0) and its mean value stays at −10.904 under each of these: the rule, SlipBack, both slips back, a slip to one side only, SLIP = 0.02, no slip, and up and down swapped.
   - The hand-drawn values under the same changes, in that order: 1.360 for the rule, then 2.284, 3.698, 1.145, 5.479, 5.900 and −7.431.
4. **Worst-fitting case.** A slip error that depends on the aim, where only aiming left slips back, breaks the sum's assumption. Random then moves to −10.744 (max |ΔP| 0.025): visible, as the derivation predicts, but weak. The hand-drawn policy stays at 1.360, because it never aims left.
5. **The hand-drawn policy's blind spot** (body paragraph and problem material). With "down from cell 5 lands in the pit", the hand-drawn value is exactly 1.360 and random's is −11.610. With "down from cell 9 stays", the values are 1.360 and −11.005.
6. **Removal test on the page.** up_or_right has an exact value of −4.178 under the rule and −5.352 under SlipBack, and the run flags it.
7. **Time limit.** At seeds 0–4, the longest random episode on the correct copy was 158 to 199 moves. Seed 0 cut none of them (the output prints 0). γ^200 < 1e-9, so the infinite-horizon exact values apply.
8. **Hand-play seed.** I searched seeds 0–299 for a start in the bottom row, a backward slip within the first three moves of the hand-drawn path, and an end at the goal. 33 qualified, and so did 50, 143, 215 and 226. With seed 33, the correct copy falls into the pit from cell 10 and SlipBack goes to cell 9 on the same draw. The page says the seed was chosen to show the slip early.
9. **Problem 2's answer.** Value iteration on the NeverEnds grid gives a goal cell that aims up and stays, and every cell heads to the goal. This matches the answer.

## Questions for the orchestrator

1. **Schulman URL.** The commission says to cite it at http, but the proof blocks non-https sources (B-SOURCES-FORM). Provisional choice: https://joschu.net/docs/nuts-and-bolts.pdf, with a data-nb-note giving the http address that served the file. https resets from this session, and the link check does not block on that.
2. **Bug choice differs from the evidence's examples.** SlipBack is a one-character change to mc_control.step, `(a + 3) % 4` → `(a + 2) % 4`. It is not the record's "reverse with probability 0.2", so none of the record's 3.698-type values appear on the page. All page numbers come from the lesson's code. In place of a reward bug, the second rule error is NeverEnds (`==` for `in`), which random actions do catch.
3. **Passive checker.** I described PassiveEnvChecker in two sentences from its source and did not register SlipperyGrid.
4. **Material not used.** Gymnasium's tutorial coordinate mix-up (it stays in Go deeper), DQN's random anchor (it suits the next lesson), SB3's own check_env, CleanRL and PufferLib.
