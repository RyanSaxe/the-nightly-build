# Commission: reinforcement-learning/frame-stacking-and-the-markov-property

Series: reinforcement-learning, open, template `lesson`, not strict. 2,500 to
6,000 words including code and output, two to five flex sections, at least one
source. Voice guide pinned by the series. Production policy is required: all
roles at the orchestrator's model, extra-high effort.

## Where the course stands

Stages 1 and 2 are complete through the deadly triad (12 Nov). Stage 3 began on
13 November with observation-scale (units and normalization, Dock, PPO with
VecNormalize). This lesson is the next stage 3 topic: the Markov property,
with history and frame stacking. Time awareness, also listed under that topic,
is a separate idea and is left for the next lesson; this one may say in a
sentence that it is coming. Recurrent policies belong to stage 6 and get at
most a sentence and a pointer.

## Topic and one idea

An observation is Markov when the distribution of the next observation and
reward depends only on the current observation and action. An environment
that reports only part of its state, for example a position without a
velocity, breaks that property, and a learner that keys its values on the
observation averages over the hidden states that share it. When the missing
part is determined by the last k observations, stacking those k observations
restores the Markov property, at the cost of a larger observation space.

## Case to start from

A new, small environment the reader can hold in a table, built for this idea:
something moves with a velocity the observation does not report (for example a
ball or a target on a short track, which the agent must intercept), so that
one frame aliases states that two frames separate. Tabular Q-learning, taught
in sarsa-and-q-learning, on the single-frame and the two-frame observation.
Show what each learned, not only whether it improved: the values or the
policy at an aliased observation, drawn. A Gymnasium wrapper that stacks
frames, and Stable-Baselines3's frame stacking for the off-the-shelf agent,
are fair to show; whether the second result is an off-the-shelf agent on a
velocity-masked classic task is the writer's call. At most two experimental
results.

The writer designs the experiments and the page's structure. Derivations the
idea supports: why a value keyed on an aliased observation is an average over
hidden states under the visit distribution, and why that average depends on
the policy, which makes the non-Markov problem change under the learner.

## Sources

Sutton and Barto, Chapter 17.3 (observations and state) and the Markov
property sections of Chapter 3; Mnih et al. 2015 for four-frame stacking in
DQN; Gymnasium's FrameStackObservation and SB3's VecFrameStack documentation
as they stand in November 2026 (verify names and signatures). Cite little.

## Recent patterns to avoid

See the writer and editor briefs for notes on recent lessons' openers,
closers and headline shapes.

## Orchestrator decisions after research (researcher/01)

- The derivation is stated with the precision Singh, Jaakkola and Jordan
  (1994) give: Monte Carlo on an aliased observation converges to the average
  of the hidden states' values under P^π(s|X); TD and Q-learning converge to
  fixed points that average the one-step reward and the next observation's
  estimate, which in general differ from it. Policy dependence holds for all
  of them. The lesson may derive one of these in full and must not state the
  Monte Carlo average as what Q-learning learns.
- Q-learning with a changing ε-greedy policy on aliased observations has no
  convergence result in the record. The lesson's runs show what happens; do
  not claim convergence or oscillation beyond them.
- First-step padding: a stack of k frames is still aliased at reset under
  both library wrappers. The lesson states this and the environment's design
  handles it (the writer chooses how, and says so on the page).
- Stacks hold observations only; say that Sutton and Barto's kth-order history
  includes actions, and why omitting them is harmless here or not.
- DQN's stated reason is partial observability and perceptual aliasing, not
  velocity. Attribute the velocity reading to its own source.
- VecFrameStack rejects Discrete spaces; the tabular part uses its own or
  Gymnasium's stacking. Do not publish the researcher's unconfirmed
  VecFrameStack bounds finding as a bug claim.

## Recent patterns: reinforcement-learning (orchestrator notes, 14 Nov 2026)

From the last five lessons (termination-and-truncation through observation-scale).
Template-required furniture (Why this matters, Background, The takeaway, Go
deeper, Problems, Sources) is fixed and not a habit.

- Headlines are a causal claim built "X keeps/sends/passes Y" with a named
  environment or library ("Reporting position in raw millimetres keeps PPO
  from...", "Gymnasium's environment checker passes a grid with...", "A problem
  whose true values are all zero sends..."). Vary the verb and construction.
- Deks open with a prepositional frame: "On Baird's seven-state
  counterexample,", "Of five Stable-Baselines3 runs on SlipperyGrid,", "With a
  target that stops only at...". Open this one differently.
- Why-this-matters bookends end with "you will be able to ..." (deadly triad)
  and close by naming a later lesson that uses the idea ("DQN, later in the
  course, combines all three"). Avoid both as formula.
- The takeaway restates the lesson's equation first, then the run's number,
  then a hedge about what the runs "measure without explaining"
  (observation-scale). Do not reuse "measure without explaining" or similar.
- Section headings often state a run's verdict with a number. Keep headings as
  steps of the argument, built differently from each other.
- Problems have run two per lesson with "Suppose ..." openings. Vary.
- Environments so far: a small grid world (the course's grid, SlipperyGrid,
  SlipBack), Dock (a cart), Baird's counterexample, a 1000-state random walk.
  This lesson builds a new one.

## Orchestrator decision after editor/01

Source 3 (Sutton and Barto, https://incompleteideas.net/book/RLbook2020.pdf)
serves a certificate whose name does not match the host, while the proof
requires https. Kept as printed, matching the published semi-gradient-td
lesson; the http copy is linked in Go deeper. Reported to the owner as a
press-level decision, not blocking.
