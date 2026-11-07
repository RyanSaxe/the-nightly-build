# Commission: reinforcement-learning/checking-a-custom-environment

Authorized by `nb duty` for 2026-11-07, open section, no commissions. Template `lesson`. Lesson 8 of the course.

## Where the course stands
Published, in order: environments-and-the-rl-problem (MDPs, Bellman equations, the slippery 4x4 grid, gridworld.py), finding-optimal-policies (policy and value iteration, control.py), learning-values-from-samples (MC and TD prediction, estimators.py), action-values-from-samples (MC control, exploring starts, mc_control.py), epsilon-greedy-exploration, sarsa-and-q-learning (td_control.py), termination-and-truncation (Gymnasium's Env, reset, step, spaces, TimeLimit; grid_env.py with SlipperyGrid, q_gym.py). The course has not used the environment checker, played an environment by hand, examined observation and reward scale, or trained an off-the-shelf agent. The course must reach training an off-the-shelf agent on a custom environment within its first few weeks; that is the next stage-1 lesson after this one.

## Topic and the one idea
Topic: a first custom environment, checked with the environment checker, random actions, a hand-written policy, play by hand, and a look at the scale of observations and rewards (stage 1).
One idea (provisional; the writer may sharpen it): Gymnasium's environment checker tests the contract, not the task. It confirms spaces, types, seeding and the reset and step signatures, so an environment whose rules are wrong can pass it. The checks that catch a wrong rule compare the environment's behaviour with numbers known independently: what random actions earn, what a hand-written policy earns, and what the course's exact solutions say those should be. Playing by hand and printing the ranges of observations and rewards catch what neither numeric check would.

## Case to start from
SlipperyGrid in grid_env.py from termination-and-truncation, the course's one custom environment. Copy it and its dependencies exactly from the published lessons. A natural start: run the checker on it, then on a copy with one plausible bug in the rules (the writer chooses: for example a slip that goes the wrong way, a reward on the wrong cell, or a goal that does not terminate) that the checker passes, and show which behavioural check catches it. The writer decides experiments and structure.

## Decisions
- Verify the checker against the current release: gymnasium 1.4.0 (pinned last lesson), `gymnasium.utils.env_checker.check_env` and what it tests, and the `PassiveEnvChecker` wrapper that `gymnasium.make` applies. Report what the checker checks from its documentation and source, with locators.
- Random actions and a hand-written policy are baselines the next lesson reuses for the off-the-shelf agent. Name them so they can be imported later.
- Play by hand: a short keyboard loop is enough. On the page its run may be shown with scripted input (for example piped keystrokes), and the page says so.
- Scale: what the observation is (a cell index in Discrete(16)) and what a neural agent would receive from it, and the reward range per step and per episode under the time limit. Teach only what the next lesson needs; one-hot encoding by an off-the-shelf library can be a pointer, checked against the library's current documentation, without teaching any algorithm.
- At most two experimental results. Any causal claim keeps its removal test on the page.
- Listings run with `uv run` with inline script metadata pinning gymnasium 1.4.0 and numpy; print in full every file a listing needs, or link the lesson that printed it.
- Mention only, if useful: CleanRL as reading material, PufferLib as a source of practical advice. No JAX environments.
- Pinned voice guide in writing-coach/01 governs voice.

## Required contribution
A reader can run the checker on an environment and say what a pass does and does not establish, and can write the behavioural checks (random and scripted baselines compared with exact values, play by hand, ranges of observations and rewards) that catch a wrong rule before any training.

## Neighbours in this edition
- daily-brief/2026-11-07; feature/anthropic-rd-acceleration-review (METR's review of Anthropic's automated-R&D risk report). No overlap.

## Recent-pattern notes supplied to the writer and editor
- Headlines are full-sentence claims about what a method learns on the grid ("Q-learning that treats its time limit as terminal learns the values of a different grid"; "Moving at random half the time, Q-learning still learns the optimal arrows"; "ε-greedy control settles for..."). Keep a claim headline; this lesson's subject is the environment and its checks, not a learner, so do not build it as "X learns Y".
- The last three lessons share one shape: derivation, listing, a run printed as a table over a swept parameter, a triptych of 4x4 heatmaps (exact vs method A vs method B), and an error-vs-parameter line chart. Do not repeat that shape; choose figures that show this lesson's idea.
- Deks lately carry two clauses joined by "and" with a figure ("...and the price of those moves grows with ε..."). Vary.
- Recurring phrases: "the course's grid", "the course's slippery grid", "mean of five runs", "the arrows", "resting point". Use sparingly.
- The why bookend in recent lessons ends on what the reader will be able to do ("Given the five values a step returns, you can write its target"). Vary its last sentence.
- Section headings often cite a cell number. One at most.
- Problems nb-note before the takeaway is template furniture and stays.

## Role models
Voice guide pinned (no coach run). Researcher, writer and editor inherit the orchestrator's model at xhigh effort, as the series requires.

## Decisions recorded after research (orchestrator)
- The record shows a uniformly random policy is blind to any slip-rule bug on this grid (relabelled moves leave its transition probabilities unchanged), while a hand-written policy exposes it. This sharpens the one idea: each behavioural check is blind to some bugs, so the checks are complementary, and the reason a given check is blind can be derived. The writer may build the lesson on a slip bug (caught by the hand-written policy, provably missed by random actions and by check_env) and may add a reward bug that random actions do catch. Experiments and structure stay the writer's; at most two results.
- Wording on the checker: a pass means no assertion fired; several type and bounds faults in step only warn. The page says that precisely.
- Registering SlipperyGrid to show the passive checker is the writer's choice; a sentence is enough.
- Cite Schulman's "The Nuts and Bolts of Deep RL Research" at its http address as the record gives it.
- SB3 2.9.2 one-hot encoding of Discrete observations is a pointer only. Do not install torch in this lesson's listings.
- The detection-cost figures are the record's own calculations; the writer recomputes and prints them from the lesson's code, or leaves them out.
- After the draft (orchestrator): the bug may be the writer's one-character SlipBack typo and the second copy a termination bug (NeverEnds); accepted. Passive checker described from source; accepted.
- Schulman link: the proof blocks non-https sources, so the http decision above is superseded. The printed link must open for a reader. If https://joschu.net does not serve the PDF, the editor substitutes a working https location for the same document (for example an archived copy) or cuts the citation; a link that resets is not acceptable.
- After reader check 1 and editor round 2: the cut of the 12-resets/5-steps count stands. The play-by-hand claim about a shared move/R error is a statement of what the check compares, which is reasoned and needs no run. The editor reports that the central explanation is unchanged and that no section was rewritten whole, so a second reader check is not owed. The lesson settles on editor/02, which follows the last check and has no required change.
