# Writer handoff: reinforcement-learning/training-an-off-the-shelf-agent (01)

## Main idea (30 words)

Judge an agent by its frozen greedy policy's return in a separate evaluation environment, over several seeds, between baselines of known value; its training curve scores a different, sampling policy.

## Original work

The lesson solves exactly both policies a Stable-Baselines3 PPO run carries, the one its training episodes sample from and the frozen greedy one, so that the training curve, 10- and 10,000-episode evaluations and five seeds are each checked against values fixed by the grid's rules, which no source does for an off-the-shelf agent.

The sentence still holds after the last revision: Table 1, Fig. 2 and Fig. 3 are those comparisons.

## Proof

`nb stamp`, then the brief's exact `nb check` command with links: BLOCK 0, WARN 0, PUBLISHABLE. Prose, counted as the lesson identity counts it (headline, dek, cards, body, captions, table cells, problems; no code, output, SVG text, reading bands or sources): 2,198 words. No warning left standing.

Preview: `nb preview` plus `capture.cjs` at phone and desktop, light and dark, with 0 px horizontal overflow at every size. Each figure was also screenshotted on its own in all four views and checked against the printed output.

## Algorithm: PPO, and why

- SB3's tips recommend "DQN with extensions" for one process with discrete actions, and SB3's own DQN has none of them.
- In throwaway probes, 2 seeds of default DQN with gamma 0.9 and 50,000 steps stopped at the hand-drawn level (exact 1.3600 and 1.3556). PPO reached the optimum or came within one arrow of it in 10 of 10 seeds.
- PPO's training moves are samples from its own stochastic policy, so the gap between the training curve and the frozen greedy policy can be solved exactly with `exact_value(move_probs(model))`. That gap is the lesson's first result.
- PPO is stage 5 material, and the page says the course builds it later. DQN appears only in problem 1, as a case not worked through.

## Decisions taken without asking (conservative)

1. **One convention, discounted at GAMMA = 0.9.** PPO's `gamma` is set to 0.9. The listing adds a `Returns` wrapper so that the last 100 training episodes are reported at GAMMA, the same window as SB3's undiscounted `rollout/ep_rew_mean`. The page states this. `evaluate_policy` is named, but not used, because it sums undiscounted. Evaluation uses `baselines.returns` on the greedy table.
2. **The frozen greedy policy is a table.** `greedy_moves` takes the argmax of `move_probs` and asserts, cell by cell, that it equals `model.predict(s, deterministic=True)`.
3. **`torch.set_num_threads(1)` in agent.py.** This is a line beyond the bare call. `det.py` showed that seed 0 trained with one thread and with four ends on different networks: exact value of the sampled policy 1.364902 against 1.406224, and last-100 undiscounted ep_rew_mean 1.82 against 1.38. With one thread the printed output repeats exactly: three full runs of `seeds.py` gave identical output.
4. **torch pins.** `torch==2.14.1` comes from the PyTorch CPU index on Linux only, through `marker = "sys_platform == 'linux'"` in `[tool.uv.sources]`. The CPU index has no macOS wheels for 2.14.1. Without the marker, `uv pip compile` fails for `aarch64-apple-darwin`, so the listing would not run on a Mac. With the marker, `uv lock --script` resolves 21 packages: Linux takes 2.14.1+cpu, and macOS arm64 and Windows take PyPI's 2.14.1. Only Linux x86_64 was actually run. Intel Macs have no torch 2.14.1 wheel at all, and the page does not mention them.
5. **Evaluation seed is 1000 + training seed**, never used in training. Each seed gets 10,000 evaluation episodes. The first 10 stand in for SB3's default count.
6. **Seeds on the page are 0 to 4.** Seeds 5 to 9 are an off-page check (below). PPO's `total_timesteps` of 50,000 runs 25 rollouts (51,200 steps). The page says "a budget of 50,000 steps", not "50,000 steps".
7. **Machado's view** is stated in their words (§4.1, §4.2), and the page says which question each view answers, as the commission asked. The Henderson Fig. 5 source asset was not captured. The lesson's own seeds show the seed effect, and Henderson is cited in prose.

## Runs and checks (rerunnable)

The folder `/tmp/claude-0/rl-lesson/run/` holds the course files: gridworld.py, estimators.py, mc_control.py, control.py, grid_env.py and baselines.py, all extracted from the published listings and identical to them. It also holds the two listings.

Use `UV_CACHE_DIR=/tmp/claude-0/rl-research/uv-cache` to reuse the installed packages. Each command takes about 4 minutes on one core.

- `uv run seeds.py` is the page's run: seeds 0 to 4. Its output is `seeds.out`, printed verbatim on the page.
- **New seeds:** `uv run seeds.py 5` runs seeds 5 to 9 (output `seeds5.out`). The conclusions held:
  - the sampled policy was below the greedy policy in every seed;
  - 4 of 5 seeds ended on optimal arrows, and seed 6 aims up in cell 13 (the hand-drawn move) with a greedy value of 1.52;
  - the removal test lifts seed 6 to 1.61;
  - the 10-episode means run from −4.11 to 5.48 and rank the suboptimal seed 6 first;
  - the 10,000-episode means also misorder: seed 5 is optimal at 1.51, against 1.52 for seed 6.
- **Cells:** `seeds.py` prints, for seed 0 and for every seed with a non-optimal arrow, the greedy move and P(sampled move is optimal) for each cell. Ties at cells 9 and 12 are counted as optimal through `np.isclose` on q\*.
- **Removal test, result 1 (on page):** the same frozen network scored with sampled moves (`exact_value(probs)`) and with greedy moves. Greedy was higher in all 10 seeds.
- **Removal test, result 2 (on page):** fixing the one wrong arrow restores 1.61 for seeds 2 (cell 8), 3 (cell 9) and 6 (cell 13).
- **Training curve tracks the sampled policy (`/tmp/claude-0/rl-lesson/scratch/checks.py`, seeds 0-4):**
  - The means of the last 1,000 training episodes were 1.147, 1.420, 1.343, 1.403 and 1.922, against sampled exact values of 1.365, 1.413, 1.393, 1.397 and 1.434. Each pair is within 2 SE (SE about 0.25 to 0.27); seed 4 is the farthest, at about 1.9 SE.
  - Sampled moves played for 20,000 episodes in an evaluation environment gave 1.335 to 1.510, each within about 1.3 SE (0.06) of `exact_value(probs)`. This confirms that the exact solve of a stochastic table matches the environment.
- **Where sampling costs value (checks.py):**
  - Sampling only in cells 9 and 12, greedy elsewhere: 1.583, 1.594, 1.492, 1.563 and 1.576.
  - Sampling everywhere except cells 9 and 12: 1.400, 1.432, 1.401, 1.387 and 1.474.
  - So most of the loss comes from the other cells. In seed 0, cell 9 still costs a little, because only 0.57 of its sampled moves are optimal there.
- **Worst-fit cases:**
  - Before training (checks.py, `train(seed, steps=0)`, seeds 0-9), the greedy table was worth less than random in seeds 0, 4, 6, 7 and 8, at −13.61, −12.90, −13.17, −13.78 and −12.56. The sampled policies were worth −10.90 to −10.91. The page cut this paragraph for length.
  - In trained runs, sampling only in the wrong cell raised the greedy policy (`checks2.py`): seed 2 went from 1.5051 to 1.5336 with sampling only in cell 8, and seed 3 from 1.5531 to 1.5742 with sampling only in cell 9. The page states this conclusion without its numbers.

## Open questions

None block publication.

- **Voice:** the template allows "you" and "we". The page uses "you" only in the Why card and for the reader's own printed numbers.
- **Problem 1's answer interpolates** the printed ε table from epsilon-greedy-exploration (0.10 at ε 0.01, 1.08 at ε 0.10) to about 0.5 at ε 0.05. No run printed the value at ε 0.05, so the answer says "near".
- **Not checked:** whether the PyTorch CPU index stays the right choice for Linux aarch64. It does have 2.14.1+cpu wheels there, according to the lock.
