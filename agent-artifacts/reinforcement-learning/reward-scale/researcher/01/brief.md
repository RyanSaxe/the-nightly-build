# researcher brief: reinforcement-learning/reward-scale (01)

Inputs:
- editorial-direction.md: the standards and the series prompt for this lesson
- commission.md: topic, the one idea, the case, boundaries
Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

A lesson on a classic method cites little, so find only what the page will use:
- The scaling and shift results for MDPs: a textbook or paper statement that
  positive scaling preserves optimal policies and that an added constant can
  change them in episodic tasks (Sutton and Barto 2nd ed., Section 3.2–3.4 and
  the exercises on adding a constant, e.g. Exercises 3.15–3.16; give the exact
  exercise numbers and pages you find).
- DQN's reward clipping: Mnih et al. 2015 Nature, the passage in Methods that
  clips rewards and what it says clipping costs (cannot tell rewards of
  different magnitude apart). Exact locator.
- One source on reward normalization by a running return statistic: either
  Engstrom et al. 2020 "Implementation Matters in Deep Policy Gradients" or
  Huang et al. 2022 "The 37 Implementation Details of PPO" (ICLR blog track),
  with the exact passage. Also confirm Gymnasium's or Stable-Baselines3's
  current reward normalization wrapper names and what statistic they divide by
  (gymnasium.wrappers.NormalizeReward; SB3 VecNormalize norm_reward), checked
  against current docs or source (November 2026), with version numbers.
- Optionally, van Hasselt et al. 2016 "Learning values across many orders of
  magnitude" (Pop-Art), the passage arguing that clipping changes the objective,
  if it is a clean pointer for Go deeper.
- Ng, Harada and Russell 1999, only the passage contrasting potential-based
  shaping with arbitrary reward changes, if one exists, for one sentence linking
  back to the shaping lesson.

Record every URL as the document's own page.
