# researcher brief: reinforcement-learning/action-masking-in-maskable-ppo (01)

Inputs:
- editorial-direction.md
- commission.md
- writing-coach/01/voice-guide.md
Output: researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background.
Where something you need is missing, ask me.

The lesson cites little. Establish only what the page will use:
1. The current sb3-contrib release (November 2026) and its pinning against stable-baselines3 2.9.2,
   gymnasium 1.4.0 and torch: does `uv run` resolve and install them together? Try it.
2. MaskablePPO's mask API in that release, from source with file and line locators: how the mask is
   obtained (the env's `action_masks` method, ActionMasker, `get_action_masks`), how it is applied to the
   distribution (logits set to a large negative value or equivalent), whether the mask is stored in the
   rollout buffer and reapplied in the update, what `predict` does when `action_masks` is omitted, and
   how MaskableEvalCallback and `evaluate_policy` handle masks.
3. The paper that introduced or analysed invalid-action masking in policy gradients (Huang and Ontañón,
   "A Closer Look at Invalid Action Masking in Policy Gradient Algorithms", 2020/2022): the experiment
   comparing masking with an invalid-action penalty, with section and figure locators, for a single
   Go-deeper line and at most one cited comparison.
4. From /home/user/the-nightly-build, `./nb history --show reinforcement-learning/action-masking-in-q-learning`
   and `--show reinforcement-learning/training-an-off-the-shelf-agent`: record the exact hanoi.py and
   agent.py listings and the API they expose (names, constants, dependency lines) so the writer can
   import them correctly. These pages are the course's own record, not sources to cite.
