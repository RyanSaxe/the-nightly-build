# editor brief: reinforcement-learning/checking-a-custom-environment (02)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/editorial-direction.md (standing directions)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/commission.md (assignment, decisions, recent-pattern notes)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/writer/01/brief.md (the exact writer brief)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/writing-coach/01/voice-guide.md (pinned voice guide)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/researcher/01/evidence.md (claim set)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/writer/01/draft-handoff.md (writer's handoff)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/editor/01/editorial-review.md (your first review)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/code/ (the lesson's code as run)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/.nb-context/ (template contract and furniture catalogs; the reader-check rules are in the lesson identity)
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/library/reinforcement-learning/checking-a-custom-environment.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/agent-artifacts/reinforcement-learning/checking-a-custom-environment/editor/02/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/checking-a-custom-environment/library/reinforcement-learning/checking-a-custom-environment.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

This round answers reader check 1, copied below. A fresh agent read the
rendered page (collapsed sections closed), the four linked earlier lessons and
the reader background, and nothing else. Compare its restatement with the
handoff's main-idea sentence. For each place it lists, first ask whether the
passage can be cut; add explanation only where the main idea needs it. Record
the action on each place in your review. Say explicitly whether your changes
alter the lesson's central explanation or rewrite a whole section, because that
decides whether a second reader check runs. Then nb stamp, the proof to
BLOCK: 0, and a look at changed visuals at phone and desktop width in both
themes.

## Reader check 1 (verbatim)

Reader: CS/maths degree, production ML experience. My RL knowledge is the four earlier lessons and nothing more.

### 1. The main idea in my own words

Gymnasium's `check_env` only checks that `reset` and `step` return values of the right shape and that seeding repeats. It compares the environment with itself, never with the grid's rules, so a wrong slip rule or a missing termination still passes. To test the rules, run a fixed policy whose value can be solved exactly from those rules, and see whether its average discounted return lands within a few standard errors of that value. Which policy you pick matters. A uniformly random policy cannot tell apart two slip rules that give every aim the same turn probabilities, so a policy that prefers some moves, like the hand-drawn one, is needed to catch a bug like SlipBack. In turn, the hand-drawn policy cannot see errors in moves it never makes.

### 2. Places I got lost, worst first

1. Fig. 4 and the Stable-Baselines3 one-hot paragraph. I can't say why they are there.
> "SlipperyGrid's observation is one integer from 0 to 15. Stable-Baselines3 2.9.2, the current release of one off-the-shelf library, does not feed that integer to its network. It first turns a Discrete observation into a one-hot vector of 16 floats (Fig. 4)."
The section is about the ranges the rules allow. The next paragraph moves on to reward scale and return bounds and never mentions the one-hot vector again. The point might be "an out-of-range integer would break the one-hot encoding" or "so observation scale is not a concern", but the lesson says neither. Stable-Baselines3 appears here for the first time, so I don't know whether it is the "off-the-shelf agent" that "Why this matters" promised.

2. The render-mode and PassiveEnvChecker paragraph: undefined terms and an unexplained conclusion.
> "The warning every passing copy gets is about render modes, which the checker can try only on an environment made through gymnasium.make. An environment made that way is also wrapped in PassiveEnvChecker, which checks only the first reset and the first two steps of its life. Neither checker sees a fault that first appears on an episode's third move."
The earlier lessons never explain `gymnasium.make`, a "spec" or render modes. Why the third move? check_env's steps all start in cell 0 or 8, which reads as if each comes right after a reset; if so check_env never sees even a second move. PassiveEnvChecker checks the first two steps "of its life", not of each episode. None of the bugs in bugs.py first appears on a third move; SlipBack can show on the first move.

3. The cells check_env started from.
> "On SlipperyGrid the variety is 12 resets and 5 steps, and every step starts in cell 0 or cell 8, as the output below counts."
The sentence before says both runs share a seed, so a backward slip would happen in both and could never be seen, whatever the start cell. Pointing out the start cells suggests wider coverage would have helped, which contradicts that.

4. "The second line is the one to read."
> "For any cell s and next cell s′ it takes two steps, and the second line is the one to read."
The display has three lines. I first read "the second line" as the conclusion, but the conclusion is the third line. The caption explains this better than the sentence.

5. The heading makes the bug sound local to cell 10.
> "One character sends cell 10's slip backward"
Only in the Fig. 2 section ("SlipBack moves one 0.1 in every row") did I learn that it changes the slip in every cell.

6. "Fig. 2 also shows what the hand-drawn policy cannot see."
> "It aims only up or right and slips a quarter turn, so it never moves down from cells such as 5, 9 and 13, or left from cell 10."
Fig. 2 is a table of aims against directions with no cells. To check "5, 9 and 13" I had to go back to the earlier lesson's arrows.

7. "Both sides of the comparison share move and R … and cancel."
> "Both sides of the comparison share move and R from gridworld.py, so an error in those would appear on both sides and cancel."
A large blind spot stated in passing. Nothing says which check, if any, would catch such an error. The takeaway lists every check's blind spot except this one.

8. "a short sum" and "relabels the aims."
> "Each check misses some errors, and a short sum lets you name the ones random moves will miss before any episode runs."
> "The sum also hides any error that relabels the aims, since it adds the four aims in any order."
The first is a forward reference I couldn't decode in "Why this matters". For the second, no example of relabelling is given.

Minor undefined terms: "Box space" in ArrayCell's docstring, pygame and frame rendering for `play`, and John Schulman (cited with no introduction).

### 3. Sections I could skip and still explain the main idea
- "Play by hand catches SlipBack at its first backward slip": a third, separate check.
- "The rules bound every number an agent will receive", especially Fig. 4 and the Stable-Baselines3 paragraph. The behaviour table already flags NeverEnds.
- The last paragraph of "check_env compares an environment only with itself" (render modes, gymnasium.make, PassiveEnvChecker).
- Within "Uniform aims average the slip rule away", the displayed derivation is close to redundant given the sentence before it.

### 4. Results reported without saying what they mean
1. NeverEnds' large positive returns ("never-ends hand-drawn 1.36 57.06 21.23 166.0 *"; "undiscounted returns from −761 to 129"): never says why. Presumably the goal and pit no longer end the episode, so +10 or the pit penalty is collected repeatedly. One sentence would confirm.
2. SlipBack raises the hand-drawn value from 1.36 to 2.40: nothing says why the wrong rule makes the policy do better.
3. up_or_right falls from −4.18 to −5.23 on SlipBack: direction and why it is opposite to the hand-drawn change are unexplained. The exact −4.18 is not computed in any visible code (EXACT in baselines.py has only "random" and "hand-drawn"; behaviour.py is collapsed).
4. "check_env made 12 resets and 5 steps, from cells [0, 8]": unclear what the counts show, given the shared-seed argument.
5. "Nine more seeds gave the same flags, and more episodes would not flag the random row": the second half is justified only in the next section.
