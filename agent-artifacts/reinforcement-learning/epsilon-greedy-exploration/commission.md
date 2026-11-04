# Commission: reinforcement-learning/epsilon-greedy-exploration

Series: Reinforcement Learning (open course). Template: lesson. Date: 2026-11-04.
Curriculum position: stage 2, "Why greedy learning stalls, and epsilon-greedy exploration".
Published so far: environments-and-the-rl-problem (MDPs, Bellman equations, the slippery 4x4
grid), finding-optimal-policies (policy and value iteration), learning-values-from-samples
(Monte Carlo and TD prediction), action-values-from-samples (action values, Monte Carlo
control with exploring starts, generalized policy iteration).

## The one idea

Without exploring starts, a greedy policy stops sampling the moves it rates low, so their
estimates never correct; making the policy epsilon-soft keeps every move sampled, and on-policy
Monte Carlo control then converges to the best epsilon-soft policy, which is not the optimal one.
The writer owns the final 30-word sentence.

## Case to start from

The previous lesson printed "no exploring starts, optimal runs at 10,000: 0" for Monte Carlo
control on the slippery grid with ordinary starts. Start from why that happens: show, in one run,
a (cell, move) pair whose average is wrong and never revisited by the greedy policy.

## Scope

In: why greedy learning stalls with ordinary starts; epsilon-greedy and epsilon-soft policies;
on-policy first-visit Monte Carlo control with an epsilon-soft policy (Sutton and Barto 5.4);
the policy improvement argument for epsilon-soft policies; what epsilon costs, i.e. the gap between
the best epsilon-soft policy and the optimal policy on this grid, and how that gap depends on
epsilon. A decaying epsilon may appear as a sentence and a pointer (GLIE) if the writer needs it,
without its own section.

Out (later lessons): SARSA, Q-learning, TD control, off-policy learning and importance sampling,
bandits/UCB/regret (stage 6), optimistic initialization as a full topic (a sentence at most).

## Boundaries

- Reuse the course's slippery 4x4 grid and the code of earlier lessons unchanged; link the lesson
  that introduced each piece reused. Do not change the environment.
- At most two experimental results. The orchestrator suggests, and leaves to the writer, that one
  result is whether epsilon-soft control escapes the stall, and the other is the price of epsilon
  against the optimal policy.
- Every number on the page comes from a printed run. Seed checks and removal tests go in
  draft-handoff.md per the series prompt.

## Recent patterns to break (from the last four lessons)

- Headlines: "Action values let an agent improve its policy...", "An agent can learn what each
  state is worth...", "Two improvements find the best policy", "The value of a state is an average
  you can solve for". Two of four put "an agent" in the headline; avoid a third.
- Deks: three of four lean on a named cell and a figure ("lift cell 13 from -2.01 to -0.71",
  "put cell 13 at about -2", "on the course's slippery grid"). Find a different dek construction.
- "On the course's slippery grid" / "on lesson 1's slippery grid" recurs; do not repeat it.
- Section headings in lesson 4 are all full declarative sentences of similar length; vary them.

## Roles and models

Production policy for this series is required: researcher, writer and editor at the
orchestrator's model and xhigh effort. Voice guide pinned (writing-coach/01, written by
nb start-article); no writing coach runs.

## Decisions after researcher/01

1. "Converges" is withdrawn. No primary source proves that first-visit on-policy Monte Carlo
   control with a fixed epsilon converges. The page states what Sutton and Barto prove (eq. 5.2 and
   pp. 101-102): an epsilon-greedy step never makes an epsilon-soft policy worse, and improvement
   stops only at the best epsilon-soft policy, under exact action values. It says plainly that
   convergence of the sample-based algorithm is not proven, and shows only what its own runs do.
   The revised one idea: a greedy policy gathers no returns for the moves it does not take, so it
   cannot correct them; an epsilon-soft policy samples every move, and the only policy greedy
   improvement can rest at is the best epsilon-soft one, which is worse than optimal.
2. The starting case changes. In the previous lesson's code with ordinary starts, the moves a
   policy does not take have no returns at all, not wrong ones. Start from that: show, in one run,
   a cell whose other moves have zero returns after many episodes, and why the greedy step never
   gives them one. The bandit-style mechanism (a disappointing early sample never retried) belongs
   to estimates that exist; mention it only if a run here shows it.
3. Code: the previous lesson's play() follows one move per cell, so epsilon-soft play needs a new
   function. Put it in this lesson's own file and import the environment and helpers unchanged from
   the earlier lessons' files, linking those lessons.
4. GLIE gets at most a sentence and a pointer to Singh et al. (2000), Section 2.2.
5. Origin of the term: not established; do not claim one.
