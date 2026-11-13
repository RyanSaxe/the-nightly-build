# Commission: reinforcement-learning/observation-scale

Series: reinforcement-learning (open course, not strict). Template: lesson.
Slug: observation-scale. Bands: 2,500 to 6,000 words including code and printed
output; 2 to 5 flex sections; at least 1 source. Voice guide: pinned by the
series, already written to writing-coach/01.

## Where the course stands

Fourteen lessons are published. Stage 1 is complete through training an
off-the-shelf agent (`training-an-off-the-shelf-agent`, Stable-Baselines3 PPO
on SlipperyGrid, with a separate evaluation environment and several seeds).
Stage 2 closed on 2026-11-12 with `the-deadly-triad`, which read the stability
of linear semi-gradient TD from the eigenvalues of its expected-update matrix.
`checking-a-custom-environment` noted, in one paragraph, that SlipperyGrid's
one-hot observation needs a check of range, not of scale, and cited
Schulman's and SB3's advice to check observation and reward scale. Nothing has
yet taught why scale matters or what normalization does.

This lesson opens stage 3, Designing environments. The curriculum's first
topic is "Observation contents, scale, and normalization". The orchestrator
splits it: this lesson takes scale and normalization; what an observation must
contain goes with the Markov-property lesson that follows, so this lesson does
not teach history, frame stacking or partial observability.

## Topic and the one idea

Topic: observation scale and normalization.

The one idea: a gradient learner uses one step size for every input, and the
largest-scale feature sets the largest step size that stays stable while the
smallest-scale feature sets how slowly the rest learns. So the units an
environment reports its observations in change what an agent can learn, and
normalizing each observation component (centering and dividing by its standard
deviation) removes that dependence.

Derive it. For a linear learner with squared-error updates (gradient Monte
Carlo or semi-gradient TD from `semi-gradient-td`), the expected update is
governed by a matrix built from E[x xᵀ]; scaling one feature by c scales its
row and column, so the eigenvalue it controls moves by about c². The stable
step size is bounded by 2 over the largest eigenvalue, and the slowest
direction converges at a rate set by the smallest, so the condition number is
what the units decide. `the-deadly-triad` read stability from the same kind of
matrix; reuse that notation and link it. Check the derivation with a run.

## The case to start from

A small custom Gymnasium environment whose observation mixes units, built for
this lesson, the same continuous problem reported in two unit systems, e.g. a
position in metres or millimetres beside a velocity, or a raw sensor reading
with an offset. The writer chooses the environment, its rules and its units.
It must be continuous-state, because a one-hot grid has no scale problem, and
it must be small enough to train on a laptop CPU in minutes. Classic
mountain-car-style mismatches (position about 1, velocity about 0.07) are a
fair model, but the lesson builds and owns its environment and prints it in
full; it does not depend on Gymnasium's MountainCar being unchanged.

Then the off-the-shelf agent: Stable-Baselines3 PPO (as in
`training-an-off-the-shelf-agent`) on the raw and on the normalized
observation, with SB3's `VecNormalize` or an observation wrapper, several
seeds, and a separate evaluation environment. The lesson does not explain PPO's
algorithm (stage 5 will). It must teach the practical trap that running
normalization statistics belong to the agent: the evaluation environment uses
the training statistics, frozen, and they are saved with the model. Verify
against the current SB3 and Gymnasium releases that the APIs named work as
written (`VecNormalize(training=False, norm_reward=False)`, `.save`/`.load`,
`gymnasium.wrappers.NormalizeObservation` and its current update flag).

## Boundaries

- At most two reported results. Natural pair: (1) the linear learner, where
  the stable step-size range and learning speed move with the units exactly as
  the eigenvalues predict; (2) PPO on raw versus normalized observations
  across seeds. The writer decides. Removal tests belong to the result they
  explain.
- Reward scale and reward normalization belong to the later reward-
  specification lesson. A sentence and pointer at most.
- Do not teach observation contents, the Markov property, frame stacking,
  action spaces or masking.
- Do not teach PPO, the network's internals, batch norm or layer norm. One
  sentence may say that a network's first layer is a linear map, so the same
  argument applies to it, if the lesson shows it; do not claim more than the
  runs show.
- Show what the learner learned, not only curves: e.g. the weight trajectory
  on the elongated error surface (raw) beside the round one (normalized), or
  the learned value or policy over the state space, as inline SVG.
- Every listing runs with `uv run file.py` on a laptop CPU in a few minutes,
  with pinned versions in inline script metadata.

## Recent patterns to break

From the last three lessons (the-deadly-triad, semi-gradient-td, n-step-returns):

- Headlines have been "<thing> sends/learns/no longer <does X> <qualifier>"
  claims with a number in the dek. Build this headline differently, e.g. around
  the units choice, and do not use "once" or "sends ... to".
- Deks have opened "On <environment>, ..." or with a method name as subject,
  joining two clauses with ", and". Build this dek differently.
- "Why this matters" bookends have opened with a sentence about the previous
  method's property and closed with a second-person roadmap ("You derive ...
  then ...", "you will be able to ..."). Do not reuse either move.
- Background item 04 has been Sutton and Barto in the last several lessons.
  Use whatever this lesson actually leans on; the phrase "in the field's
  standard notation" is retired.
- Takeaways have restated the dek's figure. End on the conclusion built.

## Production

Required directives from series.yaml: researcher, writer and editor run at the
orchestrator's model with effort xhigh; writing-coach is pinned. Subagents run
on the orchestrator's model (inherit) with the Agent tool's effort set to
xhigh.

## Decisions during production
Decided by the orchestrator after researcher/01:

- The derived result is for the linear learner with plain SGD: the
  expected-update bound α < 2/λ_max and convergence time ∝ λ_max/λ_min (LeCun
  et al. 1998, Sec. 5.1). Scaling a feature by c moves its eigenvalue by
  exactly c² only when the feature is uncorrelated with the others; the lesson
  derives that, states the condition, and checks it with a run. Say which
  bound a run tests: the full-batch expected update obeys 2/λ_max; a
  per-sample run is limited by ‖x‖². For a non-symmetric TD matrix the bound
  is not exact; if the lesson uses TD rather than gradient Monte Carlo /
  regression on returns, say so or use the symmetric case for the derivation.
- Centring matters too: a nonzero mean creates a large eigenvalue (LeCun Sec.
  5.3). Per-component standardization removes the dependence on units but does
  not make the surface round when features are correlated; say so in a
  sentence.
- PPO result: SB3's PPO uses a tanh network trained with Adam, so the
  one-step-size argument is exact only for the linear SGD learner. The lesson
  reports the PPO comparison as an observed consequence across seeds and does
  not claim the eigenvalue argument as its measured cause. Any causal claim
  about the PPO gap needs a removal test on the page; otherwise state in a
  sentence that the network adds other mechanisms (Adam's per-parameter step,
  tanh saturation) the lesson does not separate.
- Corrected API facts (use these): `model.save` does not include VecNormalize
  statistics; save them with `vec_env.save(path)` beside the model and load
  with `VecNormalize.load(path, venv)`, then set `training = False` and
  `norm_reward = False` after loading, because load restores the saved flags.
  A freshly built evaluation VecNormalize starts at mean 0, variance 1 and
  passes raw observations (clipped to ±10) unless the training statistics are
  copied or loaded. Train with `norm_reward=False` so the comparison changes
  only observation scale. Gymnasium 1.4.0's `NormalizeObservation` freezes by
  setting `env.update_running_mean = False` after construction and has no
  save/load. Versions: Stable-Baselines3 2.9.2, Gymnasium 1.4.0.

Decided after writer/01:
- Length: the prose runs about 300 words over the template's target. The
  editor cuts where the lesson repeats itself; if a whole idea must go, the
  NormalizeObservation paragraph shrinks to one sentence first. Keep the
  metres row: the headline's comparison needs it.
- nb-meta model: use the bare model ID as earlier articles do; effort is
  recorded here, not in the article.
- torch pinned at 2.14.1 to match the published PPO lesson: accepted.
- W-CITE-DENSITY on the Dock orientation section stays, per the series
  prompt (derivations and printed runs need no citation).
- After editor/01, source 1 (Efficient BackProp): the https address resets
  the TLS handshake from this runtime, as the orchestrator reproduced; the
  http address on the same host serves the PDF. Decision, following the
  precedent recorded in the-deadly-triad: Sources keeps the https address
  the proof requires, and Go deeper uses the working http address. Treated as
  an environment limit, not a broken citation.
- After editor/02 (reader check 1): the editor's response changed no central
  explanation and rewrote no whole section, so no second reader check is run.
  The prose sits about 130 words over the template's target after the
  reader's gaps were filled; accepted, since the remaining cuts would remove
  commissioned or protected material. editor/02 approves with no required
  change; the lesson is settled.
