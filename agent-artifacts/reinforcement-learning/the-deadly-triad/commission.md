# Commission: reinforcement-learning/the-deadly-triad

Series: reinforcement-learning (open course, not strict). Template: lesson.
Slug: the-deadly-triad. Bands: 2,500 to 6,000 words including code and printed
output; 2 to 5 flex sections; at least 1 source. Voice guide: pinned by the
series, already written to writing-coach/01.

## Where the course stands

Thirteen lessons are published. Stage 1 is complete through training an
off-the-shelf agent. Stage 2 has covered Monte Carlo and TD prediction, action
values and GPI, epsilon-greedy, SARSA and Q-learning, off-policy learning with
importance sampling, n-step returns, and semi-gradient TD with function
approximation (`semi-gradient-td`, 2026-11-11). The one stage-2 topic left is
"The deadly triad, with its statement and one example of divergence". This
lesson closes stage 2.

## Topic and the one idea

Topic: the deadly triad.

The one idea: semi-gradient TD can diverge, and the danger needs all three of
function approximation, bootstrapping, and off-policy training. Take any one
away on the same problem and the weights stay bounded.

## The case to start from

Baird's counterexample (Sutton and Barto, Example 11.1, Section 11.2): seven
states, eight weights in linear features, a behavior policy that picks the
"dashed" action 6/7 of the time and a target policy that always picks "solid",
zero reward, discount 0.99. Off-policy semi-gradient TD(0) and semi-gradient
expected DP both send the weights to infinity. This is a classic case built to
show where a method fails, which the series prompt allows as a new
environment.

The lesson may first give the two-state "w to 2w" example in Section 11.2 as
the smallest instance, where the derivation fits on a line, if the writer finds
it teaches the mechanism before Baird's star. That choice is the writer's.

The statement of the triad is Sutton and Barto Section 11.3. Cite it there.
State the claim as the book does: any two of the three are safe, all three can
diverge. Do not overstate it as "all three always diverge".

## Prior lessons this one depends on

- semi-gradient-td: the semi-gradient update, linear features, the TD fixed
  point, and the on-policy distribution μ. The writer links it where the update
  first returns.
- off-policy-importance-sampling: importance ratios. Link it where the per-step
  ratio enters the off-policy semi-gradient update.
- n-step-returns or learning-values-from-samples for bootstrapping as a term,
  if needed.

## Boundaries

- Mention only, per the series prompt: Expected SARSA, eligibility traces,
  Gradient-TD and Emphatic-TD. Gradient-TD and Emphatic-TD can get a sentence
  and a pointer as the methods built to remove the instability; do not derive
  them.
- Do not teach DQN, target networks or replay. A one-line pointer that stage 4's
  deep value methods face this triad is allowed.
- Experiments: at most two reported results. The natural pair is the divergence
  itself and the three removal runs that keep the weights bounded (on-policy
  state weighting, a Monte Carlo target in place of the bootstrap target, and
  tabular features). Removal tests belong to the result they explain and do not
  count as extra results. The writer decides the exact experiments.
- Show what happens to the weights, not only an error curve: the weight
  trajectories, or the expected update as a matrix whose eigenvalues decide
  stability, drawn as inline SVG.
- Every listing runs with `uv run file.py` on a laptop CPU in a few minutes.

## Recent patterns to break

Notes from the last three lessons (semi-gradient-td, n-step-returns,
off-policy-importance-sampling):

- Headlines are a method-on-environment claim with a number ("Four-step TD
  learns a 19-state random walk faster than...", "TD(0) no longer converges to
  the best fit once states share weights"). This one should not be built as
  "<method> <verb> <environment> <comparison>".
- Deks open with a method name as subject and join two clauses with a comma and
  "and" around a figure. Build this dek differently.
- "Why this matters" bookends have opened by describing what a table does and
  then pivoted to the new method; they close with "You derive ... then ... and
  check ..." or "After working ... by hand, you will code ...". Do not reuse
  either opening move or the second-person roadmap sentence shape.
- The Background and Go-deeper bands have said "in the field's standard
  notation" in two consecutive lessons. Do not use that phrase.
- "the course's slippery grid" recurs; the grid is not this lesson's
  environment, so it should not appear except as a link reference.
- Takeaways have restated the dek's figure as the last sentence. End on the
  conclusion the lesson built, not a recap of its number.

## Production

Required directives from series.yaml: researcher, writer and editor run at the
orchestrator's model with effort xhigh; writing-coach is pinned. This run uses
subagents on the orchestrator's model; the Agent tool does not expose an effort
setting per subagent, so effort follows the session's configuration. Recorded
as a deviation: effort xhigh requested, session default used.

## Decisions during production (after researcher/01)

- Correction: Baird's counterexample is in Section 11.2, Figures 11.1 and 11.2
  (pp. 261-262), not Example 11.1. Example 11.1 is Tsitsiklis and Van Roy's.
- The idea is restated for linear function approximation: the book says that
  with any two of the three present, "instability can be avoided" (p. 264).
  Tsitsiklis and Van Roy show nonlinear on-policy TD can diverge; the lesson
  says the safety claim is for linear features.
- "Stays bounded" under each removal is the lesson's own finding from its runs
  and the expected-update eigenvalues, not a cited claim. Two removals
  (on-policy weighting, Monte Carlo target) sit at a zero eigenvalue: say
  "bounded", not "converges to zero", unless the writer's runs show otherwise.
- Baird's MDP is drawn with no terminal state; the lesson treats it as a
  continuing task and says so.
- After editor/01: the Sources entry for Sutton and Barto keeps the https
  address the proof requires, with a note giving the working http address; an
  MIT Press page that could not be confirmed to land is not substituted. The
  editor's change of the on-policy removal to evaluating b is accepted: it
  removes off-policy training without the degenerate state-7-only case.
