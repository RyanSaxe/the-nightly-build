# researcher brief: reinforcement-learning/potential-based-shaping (01)

Inputs:
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/editorial-direction.md — standing directions
- .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/commission.md — topic, idea, case, boundaries
- The prior lesson, for what the course already taught: `./nb history --show reinforcement-learning/specification-gaming`
Output: .nb-work/reinforcement-learning/potential-based-shaping/agent-artifacts/reinforcement-learning/potential-based-shaping/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This is a lesson on a classic method, so it cites little. Gather only what the page will use:
1. Ng, Harada and Russell (1999), "Policy invariance under reward transformations": the theorem (sufficiency and necessity), the proof's key step, how they handle terminal/absorbing states, and the bicycle example, with page and section locators. Find a stable URL to the paper itself.
2. Wiewiora (2003), "Potential-based shaping and Q-value initialization are equivalent" (JAIR): the exact statement and its conditions (which learners, what initialization), with locators.
3. Anything authoritative on the terminal-potential and time-limit cases (for example Grzes 2017 "Reward shaping in episodic reinforcement learning", AAMAS), only if it states the limit directly. Record what it says, with locators.
4. Sutton and Barto (2nd ed.) passages on shaping, if any, with page numbers.
5. Confirm current versions of gymnasium and stable-baselines3 on PyPI as of today, in case the writer pins them.
