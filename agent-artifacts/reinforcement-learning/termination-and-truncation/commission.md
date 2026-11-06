# Commission: reinforcement-learning/termination-and-truncation

Authorized by `nb duty` for 2026-11-06 (open section, no commissions). Template `lesson`. Lesson 7 of the course.

## Where the course stands
Published, in order: environments-and-the-rl-problem (MDPs, Bellman equations, slippery 4x4 grid), finding-optimal-policies (policy and value iteration), learning-values-from-samples (MC and TD prediction), action-values-from-samples (MC control, exploring starts, GPI), epsilon-greedy-exploration, sarsa-and-q-learning (TD control, on/off-policy as a term). The course has never mentioned Gymnasium, an environment API, time limits, or truncation. Stage 1's remaining topics (Gymnasium contract; a first custom environment; training an off-the-shelf agent) are unstarted, and the course must reach "train an off-the-shelf agent on a custom environment" within its first few weeks. The prompt allows alternating stages 1 and 2 from the Gymnasium contract onward.

## Topic and the one idea
Topic: the Gymnasium contract, including termination and truncation (stage 1).
One idea: an episode can end for two different reasons, and only one of them means the state has no future. `terminated` says the MDP reached a terminal state, so the return from there is zero and a TD target stops bootstrapping. `truncated` says an outside limit (a time limit) cut the episode off; the state still has a value, and the target must keep bootstrapping. Gymnasium's `step` returns the two flags separately for exactly this reason.

## Case to start from
The course's own slippery 4x4 grid (goal and pit, reward and discount as in lesson 1), written as a `gymnasium.Env` and wrapped in a time limit, with the Q-learning of the previous lesson. Reuse the earlier lessons' environment rules and code where they serve; link the lesson that introduced the rules.

## Decisions
- Teach the contract as far as the next lessons need it: `reset` (seed, returns observation and info), `step` (returns observation, reward, terminated, truncated, info), spaces, and the TimeLimit wrapper. The environment checker, play by hand, and training an off-the-shelf agent belong to the next stage-1 lessons; at most a pointer.
- Experiments, causes and page structure are the writer's. At most two experimental results. Any causal claim keeps its removal test on the page.
- Verify against the current Gymnasium release (check the version on PyPI and the API docs for `Env.step`, `TimeLimit`, and the 0.26 change that split `done`). Listings must run with `uv run` and inline script metadata pinning gymnasium and numpy.
- Mention only, if useful: the older `done` flag and the `TimeLimit.truncated` info key it needed; Pardo et al. "Time Limits in Reinforcement Learning" (2018) is the paper to link for the idea.
- Pinned voice guide in writing-coach/01 governs voice.
- Neighbours in this edition: the daily brief and a feature on data-center electricity prices; no overlap.

## Required contribution
A reader can write the TD target for any transition from Gymnasium's two flags, explain why a truncated state keeps its bootstrap, and see on the course's grid what goes wrong in the learned values when a time limit is treated as a terminal state.

## Decisions recorded after research (orchestrator)
- Correction: the course has already used a time limit. action-values-from-samples set CAP = 200 and sarsa-and-q-learning's td_control.py bootstraps on the capped move. The lesson links that passage and presents the new part as naming the two endings and what each does to the target, not time limits as new. The terminal-at-the-limit variant is the deliberate wrong version.
- The page states the two qualifiers the record establishes: a limit is a truncation only when it is outside the task (a limit that is part of the task belongs in the observation and is a termination, Pardo et al. case (i)); and both flags can be True on one step, so the target tests terminated alone.
- Pin gymnasium 1.4.0 (PyPI, 2026-10-05) in inline script metadata; cite the /v1.4.0/ docs. Do not copy the two Gymnasium tutorial passages the record flags.
- A 200-step cap rarely binds at γ = 0.9 on this grid; the writer chooses a limit at which the difference shows and says why it was chosen.
- The claim about the course's grid rests on the lesson's own derivation and run; no source measures it.
- Role models: researcher, writer and editor inherit the orchestrator's model at xhigh effort, as the series requires; voice guide pinned.

## Recent-pattern notes supplied to the writer and editor

- Headlines are full-sentence claims about what a method learns on the grid ("Moving at random half the time, Q-learning still learns the optimal arrows"; "ε-greedy control settles for..."). Keep the claim form; do not reuse the "X still learns / settles for" construction.
- Deks of lessons 5 and 6 both explain a one-term difference or a price that "grows with ε". Avoid "differs ... in one term".
- The why bookend in lesson 6 ends "You will derive ... and see why ..."; lesson 5 has a similar promise. Do not open or close the bookend with "You will derive / you will see".
- Section headings often cite a cell number ("At ε = 0.5 the two methods part at cell 9", "...at cell 14"). One cell-number heading at most.
- Recurring phrases: "the course's slippery grid", "the best ε-soft policy", "the arrows", "the direct solve". Use the grid's names where needed but vary sentence frames.
- Every lesson so far ends with a Problems nb-note followed by the takeaway. That is template furniture and stays.
- Lessons 5 and 6 each ran around 20 seeds and printed tables; that is fine, but the at-most-two-results rule applies.
