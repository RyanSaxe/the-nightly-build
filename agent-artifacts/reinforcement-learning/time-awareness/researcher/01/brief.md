# researcher brief: reinforcement-learning/time-awareness (01)

Inputs:
- agent-artifacts/reinforcement-learning/time-awareness/editorial-direction.md (standing directions)
- agent-artifacts/reinforcement-learning/time-awareness/commission.md (topic, idea, boundaries)
Output: agent-artifacts/reinforcement-learning/time-awareness/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This is a lesson on a classic idea, so cite little and only what the page will use. Establish, with exact locators:
1. Pardo, Tavakoli, Levdik and Kormushev, "Time Limits in Reinforcement Learning" (ICML 2018, arXiv 1712.00378): the section on time-limited tasks and time-awareness — what they say must be added to the state, the claim that the state without time violates the Markov property, how they treat reaching the limit (termination), and any experiment that illustrates it (e.g. their Two-Goals / Queue-of-cars / InvertedPendulum examples). Section, equation and figure numbers.
2. Gymnasium's current release number and date, and its TimeAwareObservation wrapper as of that release: constructor arguments, what it appends (normalized or raw time, flattening), and the docs page that documents it. Confirm against the source or the versioned docs page, not a blog.
3. Gymnasium's TimeLimit wrapper and its truncated flag, only as far as the lesson needs to contrast it.
4. Sutton & Barto (2nd ed.) only if it states the Markov property in a form the lesson would quote; give the section.
5. Any primary that disagrees: e.g. arguments that time features hurt generalisation or that normalised time vs raw step count matters. Record in Contradictions.

You may run `nb history --show reinforcement-learning/termination-and-truncation` to see what that lesson already cited, so you do not duplicate its sources needlessly.
