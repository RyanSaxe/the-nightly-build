# Evidence: reinforcement-learning/action-discretization (researcher 01)

The Pendulum-v1 definition and the Gymnasium wrapper question are settled from
Gymnasium 1.4.0's own source, which I installed, ran, and matched byte for byte
against the v1.4.0 tag on GitHub. Gymnasium has shipped `DiscretizeAction` since
1.2.1. It maps index i to the centre of the i-th of k equal bins, so it never
emits the torque limits ±2 and, for even k, never emits zero torque. The
literature supports the learning side of the commission's trade in direction:
Tang and Agrawal measure an inverted U in bin count for policy gradients,
Kleinberg derives the bin count that balances discretization error against
per-arm estimation in a one-step problem, and Seyde et al. (2023) report that
finer bins are "likely to delay convergence" for a Q-learner. The evidence is thin, and
partly contrary, on the ceiling side for stock Pendulum-v1. Seyde et al. (2021)
explain why bang-bang control is optimal for control-affine systems without an action
cost, and Pendulum-v1's torque cost is 0.001·u². A throwaway dynamic-programming
check I ran (not a source; the writer must reproduce it) puts the best two-level
policy {−2, +2} within about 1.5 return units of a 65-level policy over a
200-step episode whose best mean return is about −136. So on stock Pendulum-v1
with levels that include ±2, the "more bins lower the approximation error" side
barely moves. With the wrapper's bin centres the ceiling does rise steeply with
k, but the same check shows the cause is the lost peak torque (2 − 2/k), not the
spacing. No published source reports tabular or deep Q-learning on Gymnasium's
Pendulum-v1 across bin counts.

## Sources

### Gymnasium (all at version 1.4.0, released 5 October 2026, current on PyPI on 16 November 2026)

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/envs/classic_control/pendulum.py
Kind:        primary. The Farama Foundation authors and ships the environment; the file is the definition.
Establishes: firsthand, the Pendulum-v1 dynamics, constants, reward, start state, observation and action spaces.
Paraphrase:  Constructor sets max_speed = 8, max_torque = 2.0, dt = 0.05, g = 10.0 (constructor argument,
             default 10.0), m = 1.0, l = 1.0 (lines 102-108). Action space Box(-2, 2, (1,), float32)
             (lines 121-123). Observation [cos θ, sin θ, θ̇] in Box([-1,-1,-8],[1,1,8]) (lines 117, 124, 169-171).
             step(u) (lines 126-147): clip u to [-2, 2]; cost = angle_normalize(θ)² + 0.1·θ̇² + 0.001·u²,
             computed on the state before the update and the applied torque; then
             θ̇' = clip(θ̇ + (3g/(2l)·sin θ + 3/(m l²)·u)·dt, -8, 8) and θ' = θ + θ̇'·dt
             (velocity first, then position with the new velocity). Returns reward = -cost,
             terminated = False, truncated = False. θ = 0 is upright (docstring lines 59, 62).
             angle_normalize(x) = ((x + π) mod 2π) - π (lines 281-282). The stored θ is never wrapped;
             only the cost and the cos/sin observation see the wrapped angle.
             reset (lines 149-167): θ ~ Uniform[-π, π], θ̇ ~ Uniform[-1, 1] by default
             (DEFAULT_X = π, DEFAULT_Y = 1.0, lines 12-13; low = -high, line 161). options x_init, y_init change
             those bounds.
             Docstring states the per-step minimum reward -(π² + 0.1·8² + 0.001·2²) = -16.2736044 and maximum 0
             (lines 57-62), and "The episode truncates at 200 time steps" (line 70).
             Version history: "v1: Simplify the math equations, no difference in behavior." (line 93).
Locators:    lines as given; file is 282 lines at the tag.
Quote:       costs = angle_normalize(th) ** 2 + 0.1 * thdot**2 + 0.001 * (u**2)
             newthdot = thdot + (3 * g / (2 * l) * np.sin(th) + 3.0 / (m * l**2) * u) * dt
```

I diffed this file across releases. The dynamics, reward and reset are
unchanged from Gymnasium 1.0.0 to 1.4.0; the differences are type hints, a
docstring example for `reset` options, and pygame initialisation in `render`.

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/envs/__init__.py
Kind:        primary. Registration in the library that defines the environment.
Establishes: firsthand, the 200-step time limit is applied at registration, not inside the environment.
Paraphrase:  register(id="Pendulum-v1", entry_point="gymnasium.envs.classic_control.pendulum:PendulumEnv",
             max_episode_steps=200). gym.make("Pendulum-v1") therefore returns
             TimeLimit<OrderEnforcing<PassiveEnvChecker<PendulumEnv>>>, and step 200 returns truncated=True,
             terminated=False (I ran this: 200 steps, term False, trunc True).
Locators:    lines 48-52. The env's own step comment, pendulum.py line 146, says the same.
```

```text
URL:         https://gymnasium.farama.org/environments/classic_control/pendulum/
Kind:        primary. Farama's documentation page, rendered from the same docstring.
Establishes: the same rules as the source, in the form the lesson can link for readers.
Paraphrase:  Action Box(-2.0, 2.0, (1,), float32); observation x = cos θ, y = sin θ, angular velocity in
             [-8, 8]; reward -(θ² + 0.1·θ̇² + 0.001·torque²) with θ normalised to [-π, π] and 0 upright; minimum
             -16.2736044, maximum 0; start state random angle in [-π, π], angular velocity in [-1, 1]; truncation at
             200 steps; argument g default 10.0. It does not print the dynamics equation; only the source does.
Locators:    sections "Action Space", "Observation Space", "Rewards", "Starting State", "Episode Truncation",
             "Arguments", "Version History".
```

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/transform_action.py
Kind:        primary. Library source that defines the wrapper.
Establishes: firsthand, the existence, exact name and behaviour of DiscretizeAction.
Paraphrase:  class DiscretizeAction(TransformAction, RecordConstructorArgs), "Uniformly discretizes a continuous
             Box action space into a single Discrete space." Signature DiscretizeAction(env, bins: int | tuple,
             multidiscrete: bool = False). Raises TypeError unless the action space is a Box, ValueError on an
             infinite bound. bin_centers[i] = midpoints of np.linspace(low, high, bins + 1), i.e.
             low + (j + 0.5)(high - low)/bins for j = 0..bins-1. New action space Discrete(prod(bins)), or
             MultiDiscrete(bins) with multidiscrete=True. action(i) returns the centre of bin i as a float32 array
             of the original shape. revert_action maps a continuous action to the nearest centre's index.
             The class docstring's first example is Pendulum-v1 with bins=10: action space Discrete(10), and
             step(3) reproduces step([-0.6]).
Locators:    class lines 201-348; centres lines 303-310; action() lines 317-329; revert_action lines 331-341;
             exported from gymnasium.wrappers (wrappers/__init__.py lines 77-82 and __all__ line 118).
Quote:       """Uniformly discretizes a continuous Box action space into a single Discrete space."""
```

What I observed by running it on Pendulum-v1 (Gymnasium 1.4.0):

```text
k=2   [-1.0, 1.0]
k=3   [-1.3333, 6e-08, 1.3333]
k=5   [-1.6, -0.8, 6e-08, 0.8, 1.6]
k=9   [-1.7778, -1.3333, -0.8889, -0.4444, 6e-08, 0.4444, 0.8889, 1.3333, 1.7778]
k=17  [-1.8824, -1.6471, ..., -0.2353, 6e-08, 0.2353, ..., 1.6471, 1.8824]  (spacing 4/17 = 0.2353)
```

The middle centre for odd k is 5.96e-08 rather than 0, a float32 rounding
artefact. For a one-dimensional space an out-of-range index wraps modulo k
(index 5 and index -1 both give +1.3333 when k = 3), because `_unflatten_index`
takes `flat_index % b` before the clip on line 324 can act. The sets for
k = 2, 3, 5, 9, 17 are not nested: {±1} is not in {±4/3, 0}.

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/transform_observation.py
Kind:        primary. Library source.
Establishes: firsthand, the companion DiscretizeObservation and what it does to Pendulum's observation.
Paraphrase:  DiscretizeObservation(env, bins, multidiscrete=False) bins each Box dimension uniformly between its
             low and high (np.digitize against interior edges, after clipping to [low, high - 1e-8]) and flattens to
             Discrete(prod(bins)). On Pendulum it bins cos θ, sin θ and θ̇ separately, so bins=10 gives
             Discrete(1000). Because (cos θ, sin θ) lies on the unit circle, I counted that only 28 of the 100
             (cos, sin) cells are reachable at bins=10, and 68 of 400 at bins=20.
Locators:    class lines 761-913; bin edges lines 859-862; observation() lines 869-883.
```

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.2.1
Kind:        primary. Farama's release notes.
Establishes: when the wrappers entered the library.
Paraphrase:  v1.2.1 (PyPI upload 23 September 2025) lists "Added new wrappers to discretize observations and
             actions", crediting sparisi, PR #1411. The v1.4.0 notes add that DiscretizeObservation and
             DiscretizeAction "now support n-dimensional Box spaces by flattening them" and fix their constructor
             arguments. I confirmed by unpacking wheels: the wrapper is absent from 1.0.0, 1.1.1 and 1.2.0 and
             present from 1.2.1. The DiscretizeAction centre logic is the same in 1.2.1 and 1.4.0.
Locators:    v1.2.1 release body; v1.4.0 release body (https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.4.0).
```

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/pull/1411
Kind:        primary. The contributor's own statement of purpose, merged by a maintainer.
Establishes: why the wrapper exists.
Paraphrase:  "Wrapper to discretize observations and actions" by sparisi, merged 3 July 2025. The description says
             few environments have discrete states and actions, and the wrappers let users benchmark tabular
             algorithms such as Q-learning (MountainCar given as the example) before moving to DQN.
Locators:    PR description.
```

```text
URL:         https://gymnasium.farama.org/main/api/wrappers/action_wrappers/
Kind:        primary. Farama documentation for the main branch.
Establishes: the wrapper is documented, but only in the main-branch docs.
Paraphrase:  Lists gymnasium.wrappers.DiscretizeAction, "Uniformly discretizes a continuous Box action space into a
             single Discrete space." The default docs page https://gymnasium.farama.org/api/wrappers/action_wrappers/
             and the wrapper table https://gymnasium.farama.org/api/wrappers/table/ did not list DiscretizeAction
             when I fetched them on 16 November 2026. Link the source or the main-branch page, not the default page.
Locators:    "Implemented wrappers" section.
```

### Papers

```text
URL:         https://proceedings.neurips.cc/paper/2021/hash/e46be61f0050f9cc3a98d5d2192cb0eb-Abstract.html
             (arXiv: https://arxiv.org/abs/2111.02552)
Kind:        primary. The authors' own theory and experiments.
Establishes: firsthand that bang-bang policies are competitive on continuous-control benchmarks, why optimal
             control predicts bang-bang without an action cost, and that a quadratic action cost breaks this.
Paraphrase:  Seyde, Gilitschenski, Schwarting, Stellato, Riedmiller, Wulfmeier, Rus, "Is Bang-Bang Control All You
             Need? Solving Continuous Control with Bernoulli Policies", NeurIPS 2021. Affiliations as printed:
             MIT CSAIL (Seyde, Schwarting, Rus), University of Toronto (Gilitschenski), Princeton (Stellato),
             DeepMind (Riedmiller, Wulfmeier).
             Sec. 3: for control-affine dynamics ṡ = f(s) + g(s)a with |a| ≤ 1 and no action cost, Pontryagin's
             principle reduces the choice of a to a linear program, so the optimal action sits at -1 or +1 wherever
             p*ᵀg(s*) ≠ 0 (bang-bang). An |a| cost gives bang-off-bang (-1, 0, +1). A quadratic a² cost "in general
             leads to non bang-bang optimal control."
             Sec. 5.2: on DeepMind Control Suite tasks, PPO, SAC, MPO and DreamerV2 with a Bernoulli (two-level)
             head perform on par with Gaussian heads; on Cartpole Swingup bang-bang "is able to swing-up and
             stabilize ... but incurs steady-state cost during stabilization as it is unable to select
             low-magnitude actions."
             Sec. 5.4.1: bang-bang policies explore more of the state space ("strong passive exploration") because
             every random action has maximum magnitude.
             Sec. 5.4.2, Fig. 8: on a pendulum swing-up, without action cost both bang-bang and Gaussian policies
             approximate the optimal action map and bang-bang rises faster; with quadratic action cost the
             bang-bang policy "is unable to represent the optimal action mapping and continues to incur
             steady-state cost."
             App. F.1, Fig. 10: optimal policy maps computed by value iteration for no, |a| and a² action costs.
             "While the Gaussian can represent the optimal policy in each scenario, its increased expressiveness can
             require more samples for convergence." Bang-off-bang can explore more slowly "due to the high
             probability of choosing 0 actions".
             The paper does not name the pendulum implementation it used in Figs. 8 and 10.
Locators:    Sec. 3 (pp. 3-4, incl. Fig. 1); Sec. 5.2 and Figs. 2-3 (pp. 5-6); Sec. 5.4.1 (p. 7); Sec. 5.4.2 and
             Fig. 8 (p. 9); App. F.1 and F.2 (p. 16); Figs. 10-11 (p. 17). Page numbers are PDF pages of arXiv v1.
Quote:       "its increased expressiveness can require more samples for convergence" (App. F.1)
Read:        Sec. 3 for why the extremes suffice, then Sec. 5.4.2 with Fig. 8 for the pendulum case.
```

```text
URL:         https://openreview.net/forum?id=U5XOGxAgccS  (arXiv: https://arxiv.org/abs/2210.12566, v2 25 Sep 2023)
Kind:        primary. The authors' agent and experiments.
Establishes: firsthand that a Q-learner over 2 or 3 levels per action dimension matches actor-critic agents on
             DeepMind Control Suite, and the authors' statement on finer bins.
Paraphrase:  Seyde, Werner, Schwarting, Gilitschenski, Riedmiller, Rus, Wulfmeier, "Solving Continuous Control via
             Q-learning", ICLR 2023 (DecQN). Value-based (DQN with double Q, prioritized replay, multi-step
             returns) with one value per bin per action dimension, ε-greedy.
             App. A "Action discretization": levels are "evenly spaced discrete actions including the boundary
             values", so 2 bins = {-a_bound, +a_bound}, 3 bins = {-a_bound, 0, +a_bound}.
             Sec. 5.2: 3-bin (bang-off-bang) DecQN is competitive with D4PG and DMPO over 10 seeds.
             Sec. 5.2.1, Fig. 6: "increasing granularity increases the action space and in turn yields more options
             to explore. While exploration over finer discretizations is likely to delay convergence, we observe
             highly competitive performance with both 3 and 21 bins."
Locators:    Sec. 3-4 (pp. 3-5); Sec. 5.2 and Fig. 5 (p. 7); Sec. 5.2.1 and Fig. 6 (pp. 7-8); App. A "Action
             discretization" (p. 15).
Quote:       "While exploration over finer discretizations is likely to delay convergence, we observe highly
             competitive performance with both 3 and 21 bins." (Sec. 5.2.1)
Read:        Sec. 5.2.1 and App. A. The decoupling (Sec. 4) is factoring, a later lesson.
```

```text
URL:         https://ojs.aaai.org/index.php/AAAI/article/view/6059  (DOI 10.1609/aaai.v34i04.6059;
             arXiv: https://arxiv.org/abs/1901.10500)
Kind:        primary. The authors' analysis and experiments.
Establishes: firsthand a measured inverted U in bin count, with the two named causes, for on-policy policy
             gradients.
Paraphrase:  Tang and Agrawal (Columbia University), "Discretizing Continuous Action Space for On-Policy
             Optimization", AAAI 2020, pp. 5981-5988. K atomic actions per dimension, "evenly spaced between -1
             and 1" (App. A). Sec. 3, "Effects of the Number of Atomic Actions K": "(a) Control capacity. When K is
             small the discretization is too coarse"; "(b) Training difficulty. When K increases, the variance of
             policy gradients also increases"; best performance "when 7 ≤ K ≤ 15". App. B derives gradient
             variance at initialisation growing as (K-1)/K for a one-step bandit, and Fig. 5(b) trains for a fixed
             number of steps across K: K = 2 "degrades drastically, due to the lack of control capacity", K ≈ 50
             "only slightly degrades". Table 3: wall time on Reacher relative to a Gaussian policy is 116%, 120%,
             143%, 240% for K = 5, 11, 30, 100.
             Algorithms are PPO, TRPO, ACKTR. The mechanism on the large-K side is policy-gradient variance, not
             visits per action value.
Locators:    Sec. 3 paragraph "Effects of the Number of Atomic Actions K" (p. 4); App. A "Discrete Policy" (p. 11);
             App. B, Fig. 5 and Table 3 (pp. 11-13). PDF pages of arXiv v4.
Quote:       "When K is small the discretization is too coarse and the policy does not have enough capacity to
             achieve good performance." (Sec. 3)
Read:        Sec. 3's K paragraph and App. B Fig. 5(b), for the same trade under policy gradients (stage 5).
```

```text
URL:         https://proceedings.neurips.cc/paper/2004/hash/b75bd27b5a48a1b48987a18d831f6336-Abstract.html
Kind:        primary. The author's theorem and proof.
Establishes: firsthand, for a one-step problem with a Lipschitz reward on an interval, the bin count that balances
             discretization error against per-arm estimation error, and that uniform discretization is near
             optimal.
Paraphrase:  Robert Kleinberg (M.I.T. CSAIL), "Nearly Tight Bounds for the Continuum-Armed Bandit Problem",
             NIPS 2004, pp. 697-704. Algorithm CAB1 (Fig. 1) restricts play to K equally spaced points
             {1/K, ..., 1} and runs a finite-armed bandit algorithm (UCB1 or Exp3) on them, with
             K = (T / log T)^(1/(2α+1)) in each doubling phase of length T. Theorem 3.1: regret
             O(n^((α+1)/(2α+1)) · log^(α/(2α+1)) n); for Lipschitz reward (α = 1) that is O(n^(2/3) log^(1/3) n).
             The proof splits regret into a discretization term T/K^α (the nearest grid point is within 1/K of the
             best action) and the finite-armed term. Sec. 4 opens by noting CAB1 "treats the strategies ... as an
             unordered set", ignoring that samples of one point predict its neighbours, and then proves
             (Theorem 4.2) that no algorithm beats the exponent (α+1)/(2α+1), so CAB1 is near optimal anyway.
Locators:    Sec. 3, Fig. 1 and proof sketch of Theorem 3.1 (PDF pp. 3-5); Sec. 4 first paragraph (p. 5);
             Theorem 4.2 (p. 6).
Quote:       "it treats the strategies {1/K, 2/K, . . . , 1} as an unordered set, ignoring the fact that experiments
             which sample the cost of one strategy j/K are (at least weakly) predictive of the costs of nearby
             strategies." (Sec. 4)
Read:        Sec. 3 and the proof sketch of Theorem 3.1, for the one-step version of the bin-count trade and its
             cube-root answer.
```

```text
URL:         https://arxiv.org/abs/1509.02971
Kind:        primary. The authors' own argument for building a continuous-action method.
Establishes: that the authors of DDPG made the case against naive discretization; it is an argument, not a measurement.
Paraphrase:  Lillicrap et al., "Continuous control with deep reinforcement learning", ICLR 2016. Introduction:
             discretizing for DQN suffers the curse of dimensionality (3 levels on 7 joints gives 3^7 = 2187
             actions); tasks needing fine control need finer grids; and "naive discretization of action spaces
             needlessly throws away information about the structure of the action domain".
Locators:    Sec. 1 Introduction, third paragraph (p. 1).
Quote:       "naive discretization of action spaces needlessly throws away information about the structure of the
             action domain, which may be essential for solving many problems."
```

```text
URL:         https://ojs.aaai.org/index.php/AAAI/article/view/11798  (arXiv: https://arxiv.org/abs/1711.08946)
Kind:        primary. The authors' architecture and experiments.
Establishes: firsthand, a value-based case of more levels per dimension learning worse, confounded with
             multi-dimensional action counts.
Paraphrase:  Tavakoli, Pardo, Kormushev (Imperial College London), "Action Branching Architectures for Deep
             Reinforcement Learning", AAAI 2018, pp. 4131-4138. Each action dimension is discretized into n equally
             spaced values, giving n^N joint actions. On a 4-joint reaching task, Dueling DDQN with n = 5 converges
             and beats the branching agent at the end, while with n = 9 it "shows a significantly less efficient
             learning performance". With 5 joints, n = 9 (9^5 ≈ 6 × 10^4 actions) was too expensive to run.
Locators:    "Custom Reaching Environments" and Fig. 3 (p. 5 of arXiv v2).
Read:        Only for the later factoring lesson; the 1-D lesson needs at most a pointer.
```

### Reference returns for Pendulum-v1

```text
URL:         https://github.com/DLR-RM/rl-baselines3-zoo/blob/master/benchmark.md
Kind:        primary for its own table (the RL Baselines3 Zoo maintainers trained and evaluated these agents);
             not an independent benchmark.
Establishes: returns that trained continuous-action agents reach on Pendulum-v1, for scale.
Paraphrase:  Mean (std) episode return over 750 deterministic evaluation episodes: TQC -151.340 (87.893),
             TD3 -151.855 (90.227), DDPG -152.099 (94.282), SAC -156.995 (88.714), A2C -162.965 (103.210),
             PPO -172.225 (104.159), TRPO -174.631 (127.577), ARS -212.540 (160.444). The page warns: "this is not
             a quantitative benchmark as it corresponds to only one run".
Locators:    table rows with env_id Pendulum-v1; note under "Performance of trained agents".
```

### Researcher's throwaway check (not a source)

`researcher/01/dp-sanity-check.py` (this directory; `uv run dp-sanity-check.py`,
numpy only). It solves a 200-step finite-horizon DP on a 181 × 161 (θ, θ̇) grid
with bilinear interpolation, using Pendulum-v1's `step()` copied from 1.4.0, then
runs the one-step-lookahead greedy policy in the exact continuous dynamics from
1000 fixed start states drawn like `reset()`. Paired differences use the same
starts. Its returns are lower bounds on each set's true ceiling, approximate to
about ±0.05 on paired differences (k = 9 came out 0.018 above the 65-level
reference on the coarse grid, which only grid error can explain since the sets
are nested). It answers question 4 of the brief; it is not evidence the page
can cite, and the writer's own solve replaces it.

## Contradictions

1. **On stock Pendulum-v1, bang-bang nearly matches fine control (against the
   commission's ceiling side).** Seyde et al. 2021 (Sec. 3) predict bang-bang
   optimality for a control-affine system with no action cost. Pendulum-v1 is
   control-affine in u (θ̇' is linear in u) and its torque cost is 0.001·u²,
   at most 0.004 per step and 0.8 per 200-step episode at full torque
   throughout. My check, on a 361 × 321 grid, gives paired shortfalls against a
   65-level set on [−2, 2] of 1.466 for {−2, 2}, 0.366 for {−2, 0, 2}, 0.112
   for k = 5, 0.010 for k = 9 and 0.000 for k = 17, against a mean return of
   −136.33 and a between-start standard deviation of about 74. The ceiling gap
   that more bins close is about 1% of the return at k = 2 and under 0.3% from
   k = 3 on. Any Q-learning budget the lesson can afford will lose more than
   that to estimation, so on stock Pendulum-v1 with endpoint levels the coarse
   set should win at every budget, and the lesson cannot show a budget where
   the fine set pulls ahead.

2. **The wrapper's bin centres manufacture a ceiling trend that is about peak
   torque, not spacing.** With `DiscretizeAction` centres the check gives mean
   returns of −236.45, −186.28, −163.26, −150.31 and −143.09 for k = 2, 3, 5,
   9, 17 (endpoint reference −137.18). The peak torque is 2 − 2/k: 1.0, 1.333,
   1.6, 1.778, 1.882. Removal test: restricted to |u| ≤ 1, {−1, 1} returns
   −236.45, {−1, 0, 1} −236.15, and 65 levels on [−1, 1] −236.10. The whole
   k = 2 shortfall under the wrapper comes from losing torque above 1, so a
   lesson built on the wrapper would attribute to resolution what is really
   reach. The static picture agrees: holding still needs 15·|sin θ| ≤ 3·|u|,
   so |u| = 2 holds within 23.6° of upright and |u| = 1 only within 11.5°.

3. **Coarse sets may win for a second reason: exploration.** Seyde et al. 2021
   (Sec. 5.4.1, App. F.1, F.2) find bang-bang policies explore more because
   every random action is maximal, and bang-off-bang policies explore more
   slowly because they often pick 0. Under ε-greedy over {−2, 2}, every
   exploratory step pumps energy; over 17 levels most exploratory steps are
   small. A Q-learning comparison across k therefore changes both the number
   of estimates and the exploration behaviour. The series asks for a removal
   test of any causal claim; this is the confound such a test has to remove
   (for example, by holding the behaviour policy or the visited data fixed
   across k).

4. **Larger torque cost restores the ceiling side, at the price of leaving
   Pendulum-v1.** Same check, torque cost raised from 0.001 to 0.1 (a custom
   variant): paired shortfalls of 74.8, 5.12, 1.28, 0.674 and 0.200 for
   k = 2, 3, 5, 9, 17 against 65 levels (reference about −143). At 1.0 the
   k = 3 to 17 shortfalls are 46.7, 12.9, 6.69, 2.03. This matches Seyde et al.
   2021 Fig. 8 (quadratic cost makes bang-bang unable to represent the optimal
   map). I did not test any other lever (time step, different reward).

5. **Deep agents show little cost from more bins.** DecQN (Seyde et al. 2023,
   Sec. 5.2.1) reports 3 and 21 bins both "highly competitive", while saying
   finer grids are "likely to delay convergence". Tang and Agrawal (App. B) find
   K ≈ 50 "only slightly degrades" PPO. The steep learning-side penalty the
   commission describes is a tabular, no-sharing effect; at deep-RL budgets and
   with shared network layers it is weak. Lillicrap et al. and Kleinberg (Sec. 4)
   both name the cause in the tabular case: each level is learned with no use of
   its neighbours' samples.

6. **Bang-bang competitive (Seyde 2021) versus K = 2 "degrades drastically"
   (Tang and Agrawal, App. B).** Different algorithms (MPO and others versus
   PPO with a categorical head), different tasks, and Tang and Agrawal do not
   name the task behind Fig. 5(b). They disagree about whether two levels are
   enough on MuJoCo-style tasks; neither tested Pendulum-v1.

7. **Docs versus source.** The default Gymnasium docs pages for action wrappers
   did not list `DiscretizeAction` on 16 November 2026, though the class has
   shipped since 1.2.1 and the main-branch docs list it. Cite the source.

## Numbers

```text
Figure: max_speed 8 rad/s; max_torque 2.0 N·m; dt 0.05 s; g 10.0 m/s²; m 1.0; l 1.0
Owner:  Gymnasium 1.4.0 pendulum.py lines 102-108
Scope:  Pendulum-v1 defaults; g is a make() argument
```

```text
Figure: per-step reward -(θ_norm² + 0.1·θ̇² + 0.001·u²), range [-16.2736044, 0]
Owner:  Gymnasium 1.4.0 pendulum.py line 136; docstring lines 57-62
Scope:  per step, evaluated on the pre-step state and the clipped torque
```

```text
Figure: θ̇' = clip(θ̇ + (15·sin θ + 3·u)·0.05, -8, 8); θ' = θ + θ̇'·0.05
Owner:  Gymnasium 1.4.0 pendulum.py lines 138-140, with the default constants substituted
Scope:  every step; semi-implicit Euler (velocity first)
```

```text
Figure: start state θ ~ U[-π, π], θ̇ ~ U[-1, 1]
Owner:  Gymnasium 1.4.0 pendulum.py lines 12-13, 149-162
Scope:  default reset, no options
```

```text
Figure: 200 steps per episode (10 s simulated), truncated=True at step 200, never terminated
Owner:  Gymnasium 1.4.0 envs/__init__.py lines 48-52; pendulum.py line 147
Scope:  gym.make("Pendulum-v1")
```

```text
Figure: worst possible episode return 200 × -16.2736044 = -3254.72
Owner:  derived from the docstring minimum and the 200-step limit
Scope:  per episode
```

```text
Figure: torque adds at most 3·2 = 6 rad/s² against gravity up to 15 rad/s²; holding still possible only within
        asin(0.4) = 23.6° of upright at |u| = 2, asin(0.2) = 11.5° at |u| = 1; full torque changes θ̇ by 0.3 rad/s
        per step
Owner:  derived from pendulum.py line 138 (no source states it)
Scope:  static balance, defaults
```

```text
Figure: DiscretizeAction centres = -2 + (j + 0.5)·4/k; peak |u| = 2 - 2/k = 1.0, 1.333, 1.6, 1.778, 1.882 for
        k = 2, 3, 5, 9, 17; spacing 4/k
Owner:  Gymnasium 1.4.0 transform_action.py lines 303-310 (values from running it)
Scope:  Pendulum-v1, single Discrete
```

```text
Figure: endpoint levels np.linspace(-2, 2, k), spacing 4/(k-1) = 4, 2, 1, 0.5, 0.25 for k = 2, 3, 5, 9, 17;
        each set contains the previous one
Owner:  arithmetic; DecQN App. A and Tang and Agrawal App. A use endpoint-including evenly spaced levels
Scope:  the commission's example k values
```

```text
Figure: DiscretizeAction first released in Gymnasium 1.2.1 (23 September 2025); PR #1411 merged 3 July 2025;
        Gymnasium 1.4.0 released 5 October 2026
Owner:  Gymnasium release notes; PyPI upload times; PR #1411
Scope:  library history
```

```text
Figure: DP shortfall vs 65 levels, stock reward, 361 × 321 grid: k=2 -1.466, k=3 -0.366, k=5 -0.112, k=9 -0.010,
        k=17 0.000; reference mean -136.33 (SE 2.33, 1000 starts)
Owner:  none; researcher's throwaway check (dp-sanity-check.py --grid 361 321). Writer must reproduce.
Scope:  200-step episodes from reset() starts, greedy one-step lookahead on the approximate DP
```

```text
Figure: same on 181 × 161 grid: means -138.65, -137.62, -137.21, -137.17, -137.18 (k = 2, 3, 5, 9, 17),
        reference -137.18; wrapper centres -236.45, -186.28, -163.26, -150.31, -143.09
Owner:  none; researcher's throwaway check (default arguments). Writer must reproduce.
Scope:  as above
```

```text
Figure: |u| ≤ 1 removal test: {-1, 1} -236.45, {-1, 0, 1} -236.15, 65 levels -236.10
Owner:  none; researcher's throwaway check (--authority-test)
Scope:  as above
```

```text
Figure: torque cost 0.1: shortfalls 74.819, 5.122, 1.280, 0.674, 0.200 (k = 2, 3, 5, 9, 17); torque cost 1.0:
        755.2, 46.7, 12.9, 6.69, 2.03
Owner:  none; researcher's throwaway check (--torque-cost 0.1; the 1.0 run used an earlier copy of the same code)
Scope:  custom reward, not Pendulum-v1
```

```text
Figure: trained continuous agents on Pendulum-v1: TQC -151.3, TD3 -151.9, DDPG -152.1, SAC -157.0, PPO -172.2
        (std about 88 to 104)
Owner:  RL Baselines3 Zoo benchmark.md
Scope:  one training run each, 750 evaluation episodes, deterministic policy
```

```text
Figure: best bin count 7 ≤ K ≤ 15 for PPO; K = 2 degrades drastically; K ≈ 50 slightly
Owner:  Tang and Agrawal 2020, Sec. 3 and App. B Fig. 5(b)
Scope:  fixed training steps, MuJoCo-style tasks (task for Fig. 5(b) not named), on-policy policy gradients
```

```text
Figure: K ≈ (T / log T)^(1/3) for a Lipschitz one-step reward; regret O(n^(2/3) log^(1/3) n), lower bound
        exponent 2/3
Owner:  Kleinberg 2004, Fig. 1 (α = 1), Theorems 3.1 and 4.2
Scope:  one-step continuum-armed bandit on an interval, n trials
```

```text
Figure: DecQN competitive with 3 and 21 bins; 10 seeds; Humanoid dim(A) = 21, Dog dim(A) = 38
Owner:  Seyde et al. 2023, Sec. 5.2-5.2.1
Scope:  DeepMind Control Suite, deep Q-learning with decoupled heads
```

```text
Figure: DiscretizeObservation on Pendulum: Discrete(bins³); reachable (cos, sin) cells 28 of 100 at bins = 10,
        68 of 400 at bins = 20
Owner:  Gymnasium 1.4.0 transform_observation.py (counts from my run)
Scope:  angle part only; θ̇ bins all reachable
```

## Limits

- No published source runs tabular or deep Q-learning on Gymnasium Pendulum-v1 across bin counts. The searches
  turned up only hobby repositories and a MATLAB example, none read as evidence. The lesson's own runs are the
  only evidence for that comparison.
- The Pendulum-v1 DP ceilings above are my approximate check, not a source. The writer's solve must replace them.
- Seyde et al. 2021 do not say which pendulum implementation, time step or reward their Figs. 8 and 10 use, so
  their pendulum results cannot be read as Pendulum-v1 numbers.
- Tang and Agrawal's bin-count result is for policy gradients (stage 5). The page can point to it but cannot
  teach its mechanism, and their Fig. 5(b) does not name its task.
- Kleinberg's result is for a one-step problem with a Lipschitz reward, not for a sequential problem or for
  Q-learning. Mapping it to Pendulum is an analogy. I did not check whether the course has taught bandits (the
  brief told me not to tour the archive).
- I found no paper that introduced discretizing continuous actions for value-based RL; the practice predates the
  papers above. The page should not credit anyone with introducing it.
- I did not look for evidence on how the observation grid's resolution interacts with the bin count; the brief
  did not ask, and it will matter for the writer's tabular runs.

## Source assets

```text
Asset: Seyde et al. 2021, Fig. 8 (p. 9): two panels, pendulum swing-up without and with quadratic action cost;
       learned policy maps for bang-bang and Gaussian heads with swing-up trajectories overlaid, plus returns.
Shows: without action cost a two-level policy draws the same action map as a continuous one; with a quadratic
       cost it cannot, and pays a steady cost at the top.
Crop:  keep both panels, their titles and the colour key; the caption is needed to read it.
```

```text
Asset: Seyde et al. 2021, Fig. 10 (p. 17): rows for no, |a| and a² action cost; columns for the value-iteration
       policy map, bang-bang, bang-off-bang and Gaussian maps, and a return comparison.
Shows: which number of levels the optimal map needs under each cost, computed by value iteration.
Crop:  keep the row and column labels and the green highlight that marks the optimal parameterization.
```

```text
Asset: Tang and Agrawal 2020, Fig. 5(b) (App. B): final performance against number of bins K.
Shows: the inverted U, low at K = 2, best near 7 to 15, slightly lower at large K.
Crop:  keep both axes and the K tick labels; drop panel (a) unless gradient variance is discussed.
```

```text
Asset: Seyde et al. 2023, Fig. 6 (p. 8): DecQN against DQN, including 21-bin DecQN curves.
Shows: on Control Suite tasks, 3 and 21 bins reach similar returns.
Crop:  keep the legend that distinguishes 3-bin and 21-bin runs; the dotted memory-error lines need the caption.
```

```text
Asset: Gymnasium Pendulum coordinate diagram, https://gymnasium.farama.org/_images/pendulum.png (227 × 209 px;
       the docstring references /_static/diagrams/pendulum.png, same image).
Shows: θ measured from upright, x axis up, y axis left, torque τ positive counter-clockwise.
Crop:  whole image. It is small; an SVG redraw following it would read better.
```

Gymnasium source files, Kleinberg 2004, Lillicrap et al. 2016, Tavakoli et al.
2018, RL Baselines3 Zoo benchmark: None found.

## Discarded

```text
https://gymnasium.farama.org/api/wrappers/action_wrappers/: default docs page; does not list DiscretizeAction, superseded by the source and the main-branch page.
https://gymnasium.farama.org/api/wrappers/table/: wrapper table; does not list DiscretizeAction or DiscretizeObservation.
```

## Questions for the orchestrator

1. **The stock Pendulum-v1 ceiling barely moves with k when the levels include
   ±2 (Contradiction 1).** The commission's required contribution sets a
   computable ceiling per k against a Q-learning run. On stock Pendulum-v1 that
   ceiling is flat to about 1% from k = 2 and 0.3% from k = 3, so the lesson
   can show coarse beating fine but not the crossover. Options I can see: (a)
   keep stock Pendulum-v1 and make the flat ceiling part of the lesson's
   finding (the bin-count trade exists, and here one side is nearly empty,
   which is what Seyde et al. 2021 predict); (b) a Pendulum variant with a
   larger torque cost, where the ceiling side is real (Contradiction 4) but the
   environment is no longer Pendulum-v1; (c) the substitute environment the
   commission already allows. My working assumption is that the writer decides
   with this record in hand. I have not researched (b) or (c) further.
2. **Bin centres or endpoints.** If the lesson uses `DiscretizeAction`, its
   ceiling trend comes from peak torque (Contradiction 2). I assumed the
   commission's "k evenly spaced levels" means endpoint-including
   `np.linspace(-2, 2, k)`, which nests for k = 2, 3, 5, 9, 17 and guarantees a
   ceiling that can only rise with k.
