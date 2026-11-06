# researcher brief: reinforcement-learning/termination-and-truncation (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/termination-and-truncation/agent-artifacts/reinforcement-learning/termination-and-truncation/editorial-direction.md: the standing editorial direction
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/termination-and-truncation/agent-artifacts/reinforcement-learning/termination-and-truncation/commission.md: topic, one idea, case and decisions
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/termination-and-truncation/agent-artifacts/reinforcement-learning/termination-and-truncation/writing-coach/01/voice-guide.md: the pinned series voice (for register only)
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/termination-and-truncation/agent-artifacts/reinforcement-learning/termination-and-truncation/researcher/01/evidence.md

Work from these inputs. Do not tour the repository or Git history. You may read the published lessons the commission names with `/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>` to record the grid's exact rules (layout, slip, rewards, discount) and the Q-learning code the writer will reuse. Where something you need is missing, record the question in Limits, decide it, and say so in your report.

The lesson cites little. Establish only what the page will use:
- The current Gymnasium release on PyPI, its date, and the documented signatures and semantics of Env.reset, Env.step (terminated, truncated), spaces used for a grid (Discrete), the TimeLimit wrapper and how gymnasium.make applies max_episode_steps, with exact doc URLs and anchors.
- The Gymnasium documentation's own statement on handling time limits / bootstrapping at truncation, and the 0.26 release note that replaced done.
- Pardo, Tavakoli, Levdik and Kormushev, "Time Limits in Reinforcement Learning" (ICML 2018): the exact sections stating partial-episode bootstrapping and time-awareness, with page numbers.
- Sutton and Barto 2nd ed. passage defining episodic tasks, the terminal state, and v(terminal) = 0, with page.
Install and import gymnasium with uv in a scratch directory to confirm the API you record actually behaves as documented in the current version.

Run environment: WebSearch and WebFetch (summarizing; use curl for raw text). Today is 6 November 2026.
