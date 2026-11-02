# Commission: reinforcement-learning/learning-values-from-samples (lesson 3)

## What this lesson is

Lesson 3 of the RL course. The first two lessons both end on the same open
question: lessons 1 and 2 solved for and improved a policy only because the slip
probabilities and the rewards were known and written down. This lesson teaches
how to **estimate the value function of a fixed policy from sampled experience
alone, with the transition model and the reward function hidden** from the
learner. It covers Monte Carlo prediction and temporal-difference (TD(0))
prediction, and the bias-variance contrast between them. Prediction only: it does
**not** find a better policy. That is the next lesson (model-free control: SARSA
and Q-learning), and this lesson should point there at the end.

Curriculum stage: Stage 2, "Learning from samples," first lesson of that stage.

## The through-line and the running example

Reuse lesson 1's `gridworld.py` unchanged, exactly as lesson 2 did. The same
slippery 4x4 grid: 16 cells numbered 0-15 row by row; arriving at cell 3 (goal)
pays +10 and arriving at cell 6 (pit) pays -20, both terminal; every other move
pays -1; slip 0.2 (intended move with prob 0.8, each perpendicular side 0.1); the
discount is gamma = 0.9. Evaluate the **same hand-drawn fixed policy `PI`** whose
exact value function lesson 1 computed by the direct linear solve
`v = (I - gamma Q)^{-1} b`. That exact v_pi is the ground truth this lesson
measures the sampled estimates against, with v_pi(13) = -2.01 the anchor already
established across both prior lessons.

The learner sees only what `gridworld.episode(P, policy, start, rng)` returns: a
list of `(cell, intended action, reward, next cell)` transitions. The estimators
use only the observed rewards and next states from those episodes. They must not
read `P`, `R`, `transitions`, or `fixed_policy`. The exact solve is imported only
to report the error of the estimates, never inside an estimator. State this
boundary explicitly in the prose and keep it true in the code.

Important: lesson 1 already ran 20,000 Monte Carlo episodes from cell 13 (mean
-1.94 +/- 0.05) as a one-cell sanity check against its solve, with the model
known. Do not reintroduce Monte Carlo as if it were new. Open by naming that lesson
1 already averaged sampled returns for one cell, and make this lesson's new work
the model-free setting and the whole value function: first-visit vs every-visit
MC, the incremental update, and then TD(0), which lesson 1's one-cell average could
not have shown.

## The ideas to teach, in order

1. **The model is gone.** Frame the shift: lessons 1-2 needed P and R. Outside a
   solved grid you have episodes, not equations. Define the prediction problem:
   estimate v_pi for a fixed policy from sampled episodes.
2. **Monte Carlo prediction.** v_pi(s) is the expected return from s, so average
   the observed returns. First-visit MC (average the return following the first
   visit to s in each episode) vs every-visit MC (average over all visits).
   The incremental running-mean update V(s) <- V(s) + (1/N(s)) (G - V(s)), and the
   constant-step form V(s) <- V(s) + alpha (G - V(s)). MC needs a complete episode
   before it can update, is unbiased, and is high variance.
3. **TD(0) prediction.** V(s) <- V(s) + alpha [ R + gamma V(s') - V(s) ]. Define
   the TD error delta = R + gamma V(s') - V(s). TD bootstraps: its target uses the
   current estimate of the next state after a single observed step, so it updates
   online without waiting for the episode to end. It is biased while the estimates
   are wrong and has lower variance than MC.
4. **The contrast.** MC's target is the actual return G_t (a sample of the whole
   tail); TD's target is R + gamma V(S_{t+1}) (one real reward plus a bootstrap).
   Both converge to the same v_pi here (tabular, decaying or small alpha). Show the
   bias-variance difference with real runs, not assertion.
5. **Why this is not yet control.** Prediction evaluates a fixed policy. To improve
   a policy without the model you need action values q (lesson 2's greedy step used
   P to turn v into q, which is now unavailable) and you need to explore. That is
   the next lesson's subject. State this as the forward pointer.

## Visuals (draw the mechanism; this press aims past bar/line charts)

- An inline-SVG backup-diagram contrast: the MC update target (back up the full
  sampled trajectory from a state to the terminal cell) beside the TD(0) target
  (one observed step: reward plus the bootstrapped value of the next cell). Lesson
  1 drew a one-step backup tree for cell 5; build this differently so it is not
  that figure again.
- A computed learning-curve figure via `nb chart` (Plotly): RMS error over the 14
  non-terminal cells against number of episodes (or against transitions seen), one
  trace for first-visit MC and one for TD(0), both falling toward 0, with the
  spread across seeds shown. This is where the bias-variance story is earned.
- At least one "what it learned" view: the estimated value function as a grid
  heatmap at a few checkpoints converging to lesson 1's exact grid, the way lesson
  1 showed its sweeps. Draw what the agent learned, not only that error fell.
- Annotated equations (nb-math legend) for the MC incremental update and for the
  TD(0) update / TD error, every symbol defined.

## Code

One new Python file beside the article (inline script metadata, `uv run` with no
other setup), importing `gridworld.py` from lesson 1. It implements first-visit
and every-visit MC prediction and TD(0) prediction using only sampled episodes,
and reports the error of each against the exact solve (import or recompute the
solve only to score, not inside the estimators). Every number on the page is from
an actual run, scaled to finish in a few minutes on a laptop CPU. Suggested name:
`samples.py`. If a listing imports the exact-solve helper for scoring, keep that
import visibly separate from the estimators.

## Required bands and template

Template `lesson`. Word band 2000-3600 counting code; flex sections 2-5 between
the fixed `why` opener and `takeaway` closer; min 4 sources; cite per section
(why/takeaway are cite-exempt). Open on "Why this matters" with the particular
problem and one real case; close on "The takeaway." End the body with an
`nb-note` of 2-3 problems answerable from the lesson alone, each answer in a
`details` element.

## Sources to anchor (researcher will verify and extend)

- Sutton & Barto, *Reinforcement Learning: An Introduction*, 2nd ed.: chapter 5
  (Monte Carlo methods) and chapter 6 (temporal-difference learning), for the
  definitions, the first-visit/every-visit distinction, TD(0), and the MC-vs-TD
  comparison in the field's standard notation. This is the primary pedagogical
  source and is already a recurring source in this course.
- The real case for "Why this matters": Tesauro's TD-Gammon (1995,
  *Communications of the ACM*, "Temporal difference learning and TD-Gammon") is the
  canonical real success of TD prediction/learning and is the natural anchor for a
  TD lesson. The dopamine / TD-error result (Schultz, Dayan, Montague 1997,
  *Science*) is an alternative anchor. Pick one; do not use AlphaGo or AlphaZero,
  which lessons 1 and 2 already used.
- Lesson 1 (environments-and-the-rl-problem) and lesson 2 (finding-optimal-policies)
  for the grid, the exact v_pi, and the model-known setting these build on. Link
  lesson 1 for gridworld.py.

## Model / effort (recorded)

Writer: model inherit (orchestrator model), effort high (series + production
policy). Researcher: capable, high. Writing-coach: capable, low. Editor: inherit,
high, required. These match `nb production-policy --series reinforcement-learning`.

## Recent-pattern notes (do not repeat these; the editor holds this list)

The course has only two prior lessons, so the habits below come from both:

- **"Why this matters" both reach for DeepMind/AlphaGo as the real case** (L1: the
  AlphaGo value network; L2: AlphaGo Zero as approximate policy iteration). Do not
  open on AlphaGo/AlphaZero again. Use TD-Gammon or the dopamine result.
- **The dek mold is fixed across both:** "On [the/lesson 1's] slippery grid,
  [numbers/method] [verb] cell 13 from X to Y, while [a contrasting clause]."
  (L1: "...20,000 episodes and one linear solve put cell 13 at about -2, and the
  discount turns out to be needed only by a policy that never ends." L2: "...two
  rounds of evaluate-and-improve lift cell 13 from -2.01 to -0.71, while the top
  half, already optimal, does not move.") Build this lesson's dek on a different
  frame. It may still name a concrete number, but not as "X does Y to cell 13,
  while Z."
- **Both end the body by announcing the next lesson in the words "the next
  lesson" / "the subject of the next lesson."** Point forward, but not in that
  phrasing.
- **Both takeaways close on a reflective "remember the pair of them" style line.**
  Close on this lesson's own finding instead.
- Cell 13 is the recurring protagonist and gamma 0.9 / slip 0.2 are fixed
  furniture of the running example, not habits to avoid. Keep them.
- Section headings in both are argument steps in the grid's own nouns; several use
  a comma-plus-clause join. Vary the construction and do not echo L2's heading
  shapes ("A max in place of the average", "Evaluate, improve, repeat until the
  arrows stop").

## The one line of original work (writer completes in draft-handoff)

Something like: this lesson puts first-visit MC and TD(0) on lesson 1's grid with
the model hidden and shows, from runs against the known v_pi, where each estimate's
error comes from. The writer must be able to state in one sentence what the lesson
does to the sources that the sources did not do.

## Query decisions (orchestrator, after research 01)

The researcher correctly flags that the MC-vs-TD contrast is not an established
theorem. Decisions, which the writer and editor follow:

1. **Bias/variance is earned from the runs, not asserted as theory.** Present the
   contrast as what this grid's runs show, supported where a general source exists
   (S&B Section 9.3 p.202 and Ch.13 pp.331/337 as general remarks), and say plainly
   that *which converges faster is an open question* (S&B p.124; Sutton 1988 p.29).
   Do not claim a proved general bias/variance ordering.
2. **"MC is unbiased" means first-visit MC.** State that. Every-visit MC is biased
   at finite sample size (Singh & Sutton 1996): lower error early, higher later. If
   the lesson shows every-visit, label it as biased and say why.
3. **Make the curves actually converge or state the floor.** Use the 1/N(s)
   running mean for MC and a decaying step size for TD(0) so the RMS error falls
   toward 0; if a constant alpha is used anywhere, state that both then fluctuate
   around a floor above 0 (S&B p.125) and show it honestly.
4. **TD-Gammon opener framed honestly.** TD-Gammon learned a value function from
   self-play by temporal-difference learning — the right spirit for "learning
   values from experience" — but it is TD(lambda) with a neural network doing a
   combined prediction/control task, not tabular TD(0) prediction of a fixed
   policy. The opener may use it as the real case for why learning values from
   experience matters, and must not describe it as this lesson's exact method. Use
   Tesauro's own game counts (200,000 for the best raw-input net; the zero-knowledge
   net matched Neurogammon, with near-grandmaster play coming from handcrafted
   features and a 2-ply search). Do not use the S&B 300,000 figure as Tesauro's.
5. **Inherited numbers.** v_pi(13) = -2.01 (and lesson 1's -1.94 +/- 0.05 MC check)
   are inherited from lesson 1, cited to lesson 1, not re-derived here.
