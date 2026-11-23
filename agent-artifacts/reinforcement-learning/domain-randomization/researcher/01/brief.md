# researcher brief: reinforcement-learning/domain-randomization (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editorial-direction.md — the layered direction for this lesson
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/commission.md — topic, one idea, case and boundaries
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

A lesson on a classic idea cites little; gather only what the page will use:
1. The paper that introduced domain randomization for transfer (Tobin et al.
   2017, and Sadeghi & Levine 2017 CAD2RL if it predates or parallels it):
   exact claim, setting, and which section/figure a reader should open.
2. One or two well-known follow-ups suitable for a "Go deeper" line each, with
   the section to read: e.g. Peng et al. 2018 dynamics randomization, OpenAI
   2019 Rubik's cube (automatic domain randomization), and a source that states
   the cost of randomization (conservatism / performance at the nominal
   parameter) or frames randomized parameters as a hidden context (contextual
   MDP), if one exists.
3. The current Gymnasium release (Nov 2026) and whether the reset(options=...)
   pattern, the TimeLimit and RepeatAction-style wrappers, and env checker still
   behave as documented. Record exact doc pages.
Use `/home/user/the-nightly-build/nb history --show reinforcement-learning/action-frequency`
and `.../held-out-levels` only to learn what the course has already taught and
cited, so you do not re-gather it.
