# researcher brief: reinforcement-learning/training-an-off-the-shelf-agent (01)

Inputs:
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/editorial-direction.md: the standing directions, including the lesson template and the series prompt
- agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/commission.md: the topic, the idea and the case

Output: agent-artifacts/reinforcement-learning/training-an-off-the-shelf-agent/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

A lesson on this topic cites little, so gather only what the page will use:
- The current Stable-Baselines3 release on PyPI, its supported Gymnasium versions, and whether it installs and runs with gymnasium==1.4.0 under `uv run` on Python 3.10+ (install it in a scratch directory and run a two-line training call to confirm). Record the exact locators in its source or documentation for: how a Discrete observation is preprocessed, `evaluate_policy` and its `deterministic` argument, `EvalCallback` and its separate evaluation environment, the Monitor wrapper and what episode reward it logs, and the default hyperparameters of whichever of PPO and DQN the docs recommend for a small discrete task.
- The SB3 documentation's own advice on evaluating with a separate environment and several seeds (RL Tips and Tricks), with the locator.
- The primary sources for evaluation practice the lesson may cite in one line or in Go deeper: Henderson et al. 2018, "Deep Reinforcement Learning that Matters" (seeds, the section and figure), and Machado et al. 2018 on evaluation protocols. Record what each establishes and which section a reader should open.
- The text of the earlier lessons this lesson imports from, obtained only through `/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>` for termination-and-truncation, checking-a-custom-environment and environments-and-the-rl-problem: record the exact file names, function and constant names (`SlipperyGrid`, `grid_env.py`, `gridworld.py`, the solved values of the random and hand-drawn baselines, `GAMMA`), and their reset distribution and TimeLimit, so the writer can import them without guessing.
Paths are relative to /home/user/the-nightly-build/.nb-work/reinforcement-learning/training-an-off-the-shelf-agent/.
