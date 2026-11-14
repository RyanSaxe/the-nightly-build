# researcher brief: reinforcement-learning/frame-stacking-and-the-markov-property (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/frame-stacking-and-the-markov-property/agent-artifacts/reinforcement-learning/frame-stacking-and-the-markov-property/editorial-direction.md: the paper's standards, lesson template and series prompt
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/frame-stacking-and-the-markov-property/agent-artifacts/reinforcement-learning/frame-stacking-and-the-markov-property/commission.md: topic, one idea, case, and the sources to check
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/frame-stacking-and-the-markov-property/agent-artifacts/reinforcement-learning/frame-stacking-and-the-markov-property/writing-coach/01/voice-guide.md: the series' pinned voice guide (for register only)
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/frame-stacking-and-the-markov-property/agent-artifacts/reinforcement-learning/frame-stacking-and-the-markov-property/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

A lesson on a classic idea cites little. Ask only what the page will use:
the definitions of the Markov property and of state as an observation summary
in Sutton and Barto (exact sections and pages, 2nd edition), the DQN paper's
frame-stacking passage and its stated reason, and the current Gymnasium
FrameStackObservation and Stable-Baselines3 VecFrameStack APIs (names,
signatures, versions current in November 2026, with links to the docs and
source). Verify the APIs by installing the packages with uv in a scratch
directory under /tmp/claude-0 and calling them, and record the versions.
Record any well-known velocity-masked benchmark (for example the POMDP
CartPole variants used in recurrent-RL papers) with its source, in case the
writer wants it. Also list the course's published lessons this one may link
(read from /home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/, file names and titles only).
