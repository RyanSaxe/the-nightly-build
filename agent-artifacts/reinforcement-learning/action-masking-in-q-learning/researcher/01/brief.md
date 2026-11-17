# researcher brief: reinforcement-learning/action-masking-in-q-learning (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/commission.md
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/writing-coach/01/voice-guide.md (the series' pinned voice guide, for register only)
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-q-learning/agent-artifacts/reinforcement-learning/action-masking-in-q-learning/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
You may read published lessons with `./nb history --show reinforcement-learning/<slug>` from /home/user/the-nightly-build to confirm what the course has taught and which code a lesson may reuse.

A lesson on a classic idea cites little. The page will use: (1) what current Gymnasium (version as of November 2026) documents about action masks: Taxi's and other envs' `action_mask` in `info`, `Discrete.sample(mask=...)`, exact names and semantics; (2) sb3-contrib MaskablePPO's mask interface (`action_masks()` / ActionMasker wrapper), for one sentence; (3) the paper(s) that introduced or analysed invalid-action masking (Huang & Ontañón 2020, "A Closer Look at Invalid Action Masking in Policy Gradient Algorithms", and anything earlier for value methods, e.g. Vinyals et al. StarCraft II or the Q-learning literature) with what each actually shows and the section; (4) any source documenting the specific bug of masking selection but not the bootstrap target (issue reports, papers, RLlib/Dopamine docs), so the lesson can say whether it is a known pitfall; (5) the Sutton & Barto definitions the lesson leans on (A(s) as a state-dependent action set, Q-learning update) with section numbers. Verify each tool name still exists and works as stated.
