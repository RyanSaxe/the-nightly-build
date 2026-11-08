# Commission: reinforcement-learning/training-an-off-the-shelf-agent

Authorized by `nb duty` for 2026-11-08: open series `reinforcement-learning`, no commissions queued. Template `lesson`, not strict, 2,500 to 6,000 words counting code and output, two to five flex sections, at least one source. This is lesson 9 of the course.

## Where the course stands

Published, in order: environments-and-the-rl-problem (MDPs, Bellman equations, the slippery 4×4 grid), finding-optimal-policies (policy and value iteration), learning-values-from-samples (Monte Carlo and TD prediction), action-values-from-samples (MC control, GPI), epsilon-greedy-exploration, sarsa-and-q-learning, termination-and-truncation (Gymnasium's reset and step, TimeLimit, `grid_env.py` with `SlipperyGrid`), checking-a-custom-environment (check_env, random and hand-drawn baselines, play by hand, observation and reward ranges). Stage 1's remaining item is training an off-the-shelf agent on the custom environment, and the series prompt's one timing target is that the reader does this within the first few weeks. Lesson 8 ends by noting that Stable-Baselines3 one-hot encodes SlipperyGrid's integer cell, and its opening says a later lesson hands SlipperyGrid to an off-the-shelf agent.

## Topic, idea and case

Topic: stage 1's last item, "Training an off-the-shelf agent on it, with a separate evaluation environment, several seeds, and random and scripted baselines."

The one idea, for the writer to sharpen into the 30-word sentence: a trained agent is judged by what its frozen policy earns in a separate evaluation environment, across several training seeds, measured against baselines whose values are known; the training curve alone does not show that.

The case to start from: SlipperyGrid from `grid_env.py`, which lesson 8 checked. It suits the idea because the course can solve its optimal value exactly and already has two baselines with solved values (uniform random moves and the hand-drawn policy), so every evaluation number has a fixed reference above and below it. Reuse the earlier lessons' files by import and link the lessons that printed them.

The agent: one algorithm from Stable-Baselines3, used as a library. Name the algorithm and the hyperparameters the listing sets, and do not explain how the algorithm works. Its stage (4 or 5) teaches it later; say that in a sentence. The writer chooses which algorithm and justifies the choice in the handoff.

## What the lesson leaves to the writer

The experiments, the causes to test, and the page's structure. At most two experimental results, per the series prompt. Candidates the idea supports, not a list to fill: the gap between the reward a training curve logs (exploring, with its own episode starts) and what the frozen greedy policy earns in a fresh evaluation environment; the spread across training seeds against the gap to the baselines; comparison of the learned policy's arrows and values with the optimal arrows from the exact solve. Each result passes the series prompt's checks: new seeds, other cells, removal tests for any causal claim, and the case the explanation fits worst.

## Boundaries

- Interval estimates, bootstrap confidence intervals and the statistics of reporting belong to stage 4. Show individual runs and say how many seeds; do not teach interval estimation here.
- Do not explain the algorithm's update, network or loss.
- Every experiment finishes within a few minutes on a laptop CPU. Pin package versions in inline script metadata, consistent with the earlier lessons' pins (gymnasium==1.4.0) and the current Stable-Baselines3 release the researcher confirms.
- Vectorized environments and autoreset are stage 5 material. If the library wraps the environment in a vector environment, say only what the reader needs to read the code.

## Recent patterns to break

- Every lesson so far runs on SlipperyGrid. This lesson keeps it because the item says "on it" and the exact solve gives the reference, and the next lessons should move off it. Do not describe the grid again.
- Recent Why this matters cards state the third part with "You will derive ...", "You can then prove ...". Phrase it differently.
- Recent headlines are a claim whose subject is a method or a tool doing something on "the course's grid" or with a specific number. Keep the claim form but do not reuse "the course's grid", "the hand-drawn policy" as headline nouns, or a dek built on "so only ... can".
- Recent section headings are full declarative sentences with a figure or cell number. Vary the build.

## Neighbours in this edition

Daily Brief 2026-11-08 and a Feature on the pelacarsen Lp(a)HORIZON trial. No overlap.

## Production

Required production policy for this series: researcher, writer and editor each run on the inherited model (the orchestrator's) at extra-high effort. The voice guide is pinned by the series (`writing-coach/01/voice-guide.md`), so no writing coach runs. The lesson template requires a reader check after the editor's first review; the orchestrator runs it. Harness: Claude Code, cloud session.

## Decisions after researcher/01

- The writer reads the earlier lessons that printed `mc_control.py`, `estimators.py`, `control.py` and `td_control.py` with `nb history --show` and confirms every imported name before relying on it. The lesson's folder list names every file the listings need.
- State the online view fairly. Machado et al. (2018, §4.1 and §4.2) measure an agent by the average of its last training episodes and argue that a separate frozen-policy evaluation hides sample efficiency. The lesson's idea is the policy-optimization view in Henderson et al.'s terms. Say in a sentence or two which question each view answers, and that this lesson asks what policy the agent ends with.
- Because one episode's return has a standard deviation near 8.5 against a 0.25 band between the hand-drawn and optimal values, the lesson may evaluate the frozen greedy policy exactly with the course's own policy-evaluation solve, beside a sampled `evaluate_policy` run. Whether to make that the second result is the writer's call.
- Discounting: SB3's Monitor, training curve and `evaluate_policy` report undiscounted returns, and the course's solved values are discounted at GAMMA = 0.9. Every comparison on the page uses one convention, stated where it first appears. Set the agent's gamma to the course's 0.9 or say why not.
- Cells 9 and 12 have tied optimal moves. Treat either tied move as optimal when counting a learned policy's optimal arrows.
- Algorithm: the writer's choice. The researcher's informal trial found DQN with defaults stopping at the hand-drawn value and PPO reaching the optimum; any such claim on the page comes from the lesson's own printed runs. Pin torch to the CPU-only wheel index in the inline script metadata so `uv run` stays small.

## Decision after writer/01

Accepted: PyTorch's CPU-only index applies on Linux only, so the inline metadata resolves on macOS arm64 and Windows as well. Problem 1's answer rests on an interpolated ε value no run printed; the editor either runs the value or rewrites the answer so it needs no unprinted number.

## Decisions after editor/02

- The editor's corrected main-idea sentence stands: "Judge an agent by its frozen greedy policy's return in a separate evaluation environment, over several seeds, beside baselines scored the same way; its training curve scores the sampling policy."
- The episode-count rule n ≥ (3σ/d)² stays. It reuses the three-standard-error flag the course already taught and teaches no interval estimation, so it is inside the stage-4 boundary.
- Because the main idea's wording changed and four passages are new, the orchestrator runs the second and last reader check.
