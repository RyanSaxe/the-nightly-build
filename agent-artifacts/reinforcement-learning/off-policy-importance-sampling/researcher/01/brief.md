# researcher brief: reinforcement-learning/off-policy-importance-sampling (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/off-policy-importance-sampling/agent-artifacts/reinforcement-learning/off-policy-importance-sampling/editorial-direction.md — the standing directions, including the course prompt
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/off-policy-importance-sampling/agent-artifacts/reinforcement-learning/off-policy-importance-sampling/commission.md — topic, the one idea, the case to start from
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/off-policy-importance-sampling/agent-artifacts/reinforcement-learning/off-policy-importance-sampling/writing-coach/01/voice-guide.md — the pinned series voice
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/off-policy-importance-sampling/agent-artifacts/reinforcement-learning/off-policy-importance-sampling/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background, apart from what this brief names. Where something you need is missing, ask me.

The lesson cites little. Ask only what the page will use:
1. Sutton and Barto (2nd ed., 2018), Section 5.5 and Example 5.5: exact page numbers, the definitions of the importance-sampling ratio, ordinary and weighted IS, the bias/variance statements, coverage, and Example 5.5's setup and its infinite-variance argument. Also Section 5.6 (incremental weighted IS) if the writer may use it.
2. The paper that introduced importance sampling for off-policy RL evaluation (Precup, Sutton and Singh 2000, "Eligibility traces for off-policy policy evaluation", or the right earlier reference): locator for the estimators.
3. The prior lessons' code the writer can reuse: run `/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>` for checking-a-custom-environment, training-an-off-the-shelf-agent, learning-values-from-samples and sarsa-and-q-learning, and record which printed files (names, functions, signatures, GAMMA, grid layout, exact_value) a new lesson can import, with the lesson link for each. Record what the SARSA lesson already said about target and behavior policies, so the lesson does not re-teach it.
