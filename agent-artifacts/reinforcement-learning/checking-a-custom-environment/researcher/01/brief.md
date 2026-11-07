# researcher brief: reinforcement-learning/checking-a-custom-environment (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/editorial-direction.md (standing directions)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/commission.md (assignment, decisions, neighbours)
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Note: the pinned voice guide is for the writer, not for you.
Published lessons you may open for the course's code and rules:
/home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/termination-and-truncation.html
and the earlier lessons in the same folder (read with
`nb history --show reinforcement-learning/<slug>`).

The page will use: what check_env and the passive checker test in gymnasium
1.4.0 (from the docs and the source of gymnasium/utils/env_checker.py and
passive_env_checker.py, with function names and line ranges), whether
check_env catches a wrong transition or reward (it should not; confirm from
source), what an off-the-shelf library does with a Discrete observation
(Stable-Baselines3's current release and its preprocessing of Discrete
observations, with locator), and the paper or text to link for baselines and
sanity checks if one clearly exists. Ask only for what a lesson on a classic
method cites; keep it short.
