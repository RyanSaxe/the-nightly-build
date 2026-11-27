# Evidence: reinforcement-learning/factored-action-spaces (researcher 01)

Retrieved 2026-11-27. The sources support three parts of the lesson directly. The first is the
count: a joint table stores Π n_d values per state and per-component tables store Σ n_d (BDQ p. 1
and Table 1; Tang et al. Figure 1; Matignon et al. p. 5). Tang et al. add that the sum has
Σ n_d − D + 1 free parameters, one fewer per extra component than the number of stored values. The
second is that greedy action selection on a sum splits into one argmax per component (VDN p. 4;
hypergraph paper p. 9). The third is the current tooling. Gymnasium 1.4.0's `MultiDiscrete`
exists and behaves as documented; I read the live page and ran it. Stable-Baselines3 2.9.2 gives
PPO and A2C one independent categorical per component, and its DQN rejects `MultiDiscrete`; I read
the docs and the source and ran both. The evidence contradicts the commission in two places, and a
third finding changes what the second run can predict. First, the action-branching form in
Tavakoli et al. does not write Q as a sum. Each branch is regressed on its own onto a common target
that averages the branches' greedy values (equations 6 and 7). So "the action-branching form" and
"Q(s, a) ≈ Σ_d Q_d(s, a_d)" are two different learners. The sum trained on one shared TD error is
the form in VDN (multi-agent) and in Tang et al. (single-agent). Second, the "exactly when"
condition is sufficient but not necessary. Tang et al.'s Proposition 6 and Figure 5, and QTRAN's
introduction, show factored greedy choices that hit the joint optimum even where the components
interact. Third, where Q* is not additive, which pair the factored learner picks depends on how
often each joint action was tried (Matignon et al. eq. 8; QTRAN's use of ε = 1). The
non-additivity can also come from transitions, not only from a reward term (Tang et al. Theorem 1,
eqs. 2 and 3). No source analyzes the convergence of tabular factored Q-learning, or how its sample
efficiency scales with the number of components. The lesson's own runs have to establish both.

## Sources

### 1. Tavakoli, Pardo and Kormushev, "Action Branching Architectures for Deep Reinforcement Learning" (AAAI 2018)

```text
URL:         https://arxiv.org/abs/1711.08946 (v2, 25 Jan 2019; the arXiv comment says "AAAI 2018,
             NIPS 2017 Deep RL Symposium"). Published record:
             https://ojs.aaai.org/index.php/AAAI/article/view/11798 (DOI 10.1609/aaai.v32i1.11798,
             vol. 32, dated 2018-04-29); page opened, HTTP 200. Locators below are arXiv v2 PDF
             pages.
Kind:        primary. The authors (Arash Tavakoli, Fabio Pardo, Petar Kormushev, Imperial College
             London) define the architecture, its targets and its loss, and report their own runs.
Establishes: firsthand: the per-branch value form, the three TD targets they tried, the loss, the
             output count, and their reaching and MuJoCo results. Merely repeats: the coordination
             problems of independent learners (cites Matignon et al. 2012, entry 11).
Paraphrase:  A discrete-action method over N action dimensions with n_d levels each has to consider
             Π_d n_d joint actions. BDQ instead gives each dimension its own output branch on a
             shared state representation. Each branch outputs Q_d(s, a_d) = V(s) + (A_d(s, a_d) −
             mean over a'_d of A_d(s, a'_d)) (eq. 1). The joint action is the tuple of per-branch
             argmaxes. Three TD targets were tried: a separate target per branch (eq. 4), one
             target taking the max over branches (eq. 5), and one target taking the mean over
             branches (eq. 6). The paper introduces eq. 6 as "The best performing method, also used for
             BDQ". The loss is the mean over branches of each branch's squared error against the
             target (eq. 7). No equation forms a joint value or sums the branches; each Q_d is
             regressed on its own onto the full return target.
Locators:    p. 1 Abstract ("linear increase of the number of network outputs"); p. 1 right column
             (Π n_d actions "need to be considered"); p. 1 Figure 1 caption ("the concatenation of
             the selected sub-actions results in a joint-action tuple"); p. 2 (IDQ ablation and the
             five independent-learner issues); p. 3 Action Branching Architecture ("naïve
             distribution ... convergence problems"); p. 4 eqs. 1, 4, 5, 6, 7 (I checked this page
             against a rendered image); p. 5 reaching results and Figure 3; p. 6 Figure 5 and the
             N = 5 result; p. 7 Table 1 and "highly robust".
Quote:       "using the existing discrete-action algorithms, a total of Π_{d=1}^N n_d possible
             actions need to be considered." (p. 1)
             "The best performing method, also used for BDQ, replaces the maximum operator in
             Equation 5 with a mean operator: y = r + γ (1/N) Σ_d Q_d^−(s', argmax_{a'_d ∈ A_d}
             Q_d(s', a'_d))." (p. 4, eq. 6)
             "In practice, we found that defining the loss to be the expected value of the mean
             squared TD error across the branches mildly enhances the performance:
             L = E_{(s,a,r,s')∼D}[ (1/N) Σ_d (y_d − Q_d(s, a_d))² ]" (p. 4, eq. 7)
             "it is well-known that the naïve distribution of the value function or the policy
             representation across several independent function approximators is subject to
             numerous challenges which can lead to convergence problems" (p. 3)
             "BDQ is highly robust against the specifications of the TD target and loss function,
             while it highly deteriorates with the ablation of the prioritized replay." (p. 7)
             "In the task with N = 4, we see that the Dueling DDQN agent with n = 5 starts off less
             efficiently (i.e. slower learning curve) than its corresponding BDQ agent, but
             eventually converges and outperforms both BDQ agents in their final performance."
             (p. 5)
```

The joint learner beats the branching learner at the end of the N = 4, n = 5 reaching task. The
N = 3 task shows "all agents learn at about the same rate" (p. 5). The branching advantage in that
paper grows with N and n. It does not hold at every size.

### 2. Kanervisto, Scheller and Hautamäki, "Action Space Shaping in Deep Reinforcement Learning" (IEEE CoG 2020)

```text
URL:         https://arxiv.org/abs/2004.00980 (v2, 26 May 2020; comment: "To appear in IEEE
             Conference on Games 2020"). The published DOI 10.1109/CoG47356.2020.9231687 resolves
             to https://ieeexplore.ieee.org/document/9231687/, which returned HTTP 202 to a
             scripted request (gated). I worked from arXiv v2; locators are its PDF pages.
Kind:        primary for its own experiments and its recommendation. Authors: Anssi Kanervisto
             (School of Computing, University of Eastern Finland), Christian Scheller (Institute
             for Data Science, University of Applied Sciences Northwestern Switzerland), Ville
             Hautamäki (School of Computing, University of Eastern Finland). Secondary for Table I,
             which compiles other teams' competition entries. One row, MineRL 3rd place [28], is
             co-author Scheller's own entry.
Establishes: firsthand: PPO and IMPALA runs comparing MultiDiscrete with Discrete versions of the
             same controls, and the authors' guideline. Secondhand: which action-space changes
             competition entrants made (Table I).
Paraphrase:  The paper names three common changes to a game's action space: removing actions (RA),
             discretizing continuous actions (DC), and converting a multi-discrete space into one
             discrete action covering all combinations (CMD). It says MultiDiscrete spaces are
             usually handled as independent discrete decisions. It also says Q-learning works only
             for Discrete spaces, and that the Tavakoli et al. variant for MultiDiscrete "is not
             commonly used". Every experiment trains policy-gradient agents (PPO; IMPALA on
             StarCraft II). None trains a factored Q-learner. Atari compares MultiDiscrete
             (joystick 9 × fire 2) with the full Discrete(18): "no clear difference", except
             MsPacman. ViZDoom finds multi-discrete "performs as well as discretized versions".
             Obstacle Tower finds "no significant difference" for CMD. The conclusion: CMD "has no
             clear positive effect and can suffer from poor scaling". Its guide says to avoid CMD.
             In Get-To-Goal, the Discrete variant also forbids diagonal moves. So that comparison
             changes both the factoring and the set of reachable actions.
Locators:    p. 2 §II-B (the MultiDiscrete definition) and §II-C a)–c) start; p. 3 Table I and the
             end of §II-C c); p. 3 §III-B Get-To-Goal setup, continued on p. 4 with the list of variants; p. 4 Figs. 1–2 and the Get-To-Goal and
             Atari results; p. 5 Fig. 3, the Doom results and §III-E Obstacle Tower; p. 7 §IV
             Discussion and conclusions.
Quote:       "MultiDiscrete spaces are often treated as independent Discrete decisions" (p. 2)
             "For example, methods like Q-learning [6] only work for Discrete action spaces. While a
             modified version of Q-learning exists for MultiDiscrete spaces [19], this is not
             commonly used." (p. 3; [19] is Tavakoli et al., AAAI 2018)
             "Converting multi-discrete to discrete action spaces has no clear positive effect and
             can suffer from poor scaling in cases with large action spaces." (p. 7)
             "Avoid turning multi-discrete actions into a single discrete action and limit the
             number of choices per discrete action." (p. 7)
             "Discrete: A flattened version of above, where only one of the buttons may be pressed
             at a time, i.e. no diagonal movement allowed" (p. 4, Get-To-Goal variants)
```

### 3. Gymnasium 1.4.0 documentation and package: `gymnasium.spaces.MultiDiscrete`

```text
URL:         https://gymnasium.farama.org/api/spaces/fundamental/#gymnasium.spaces.MultiDiscrete
             (live page fetched 2026-11-27; its MultiDiscrete section is identical to
             https://gymnasium.farama.org/v1.4.0/api/spaces/fundamental/). Source view:
             https://gymnasium.farama.org/_modules/gymnasium/spaces/multi_discrete/. Release:
             https://pypi.org/project/gymnasium/1.4.0/ (PyPI's latest, uploaded 2026-10-05).
Kind:        primary. The Farama Foundation writes and ships the library and its documentation.
Establishes: firsthand: the constructor, the start offset, sampling, masks, and flattening.
Paraphrase:  The constructor is MultiDiscrete(nvec, dtype=np.int64, seed=None, start=None). The
             space is "the cartesian product of arbitrary Discrete spaces". Component d takes
             values start[d], ..., start[d] + nvec[d] − 1, and start defaults to 0. Sampling with
             no arguments draws each component independently and uniformly. The source line is
             (np_random.random(nvec.shape) * nvec).astype(dtype) + start. sample() accepts mask or
             probability, not both. Each must be a tuple with one array per component, so a mask
             can forbid a level of one component but cannot forbid a combination. If a component's
             mask is all zeros, start is returned for that component. A Note says some wrappers
             treat 0 as the no-op.
Locators:    class entry and sample() on the page above. Source: sample() and _apply_mask() in
             gymnasium/spaces/multi_discrete.py at v1.4.0 (sample at line 143 of the installed
             file).
Quote:       "This represents the cartesian product of arbitrary Discrete spaces."
             "start – Optionally, the starting value the element of each class will take (defaults
             to 0)."
             "Only mask values == 1 are possible to sample unless all mask values for an action are
             0 then the default action self.start (the smallest element) is sampled."
             "Some environment wrappers assume a value of 0 always represents the NOOP action."
```

What I checked. I installed gymnasium==1.4.0 on Python 3.11 in a scratch environment and ran the
following.

- `MultiDiscrete([3, 4])`: shape `(2,)`, dtype int64, start `[0 0]`. `contains([2, 3])` is True
  and `contains([3, 0])` is False.
- `MultiDiscrete([3, 4], start=[-1, 1])`: samples fall in {−1, 0, 1} × {1, ..., 4},
  `contains([0, 0])` is False, and the repr prints the start.
- `sample(mask=(int8 array of length 3, int8 array of length 4))` returns only unmasked levels. An
  all-zero mask returns start for that component. `probability=` takes one float array per
  component. Passing both `mask` and `probability` raises `ValueError` (read in the source).
- `MultiDiscrete(np.array([[1, 2], [3, 4]]), seed=42).sample()` returns `[[0, 0], [2, 2]]`, the
  same as the docs example.
- `gymnasium.utils.env_checker.check_env` on a small env with this action space gives no
  MultiDiscrete-specific warning, with or without a non-zero start. The only warning concerned
  render modes.

### 4. Gymnasium 1.4.0: flattening utilities and the `DiscretizeAction` wrapper

```text
URL:         https://gymnasium.farama.org/api/spaces/utils/#gymnasium.spaces.utils.flatten_space
             (live page fetched 2026-11-27). The wrapper's docstring is in the 1.4.0 package at
             gymnasium/wrappers/transform_action.py. It is not listed on
             https://gymnasium.farama.org/api/wrappers/action_wrappers/, which shows
             TransformAction, ClipAction, RescaleAction, StickyAction and RepeatAction.
Kind:        primary (library documentation and source).
Establishes: firsthand: what Gymnasium means by "flatten" for a MultiDiscrete space, and how its
             discretizing wrapper builds a joint Discrete space.
Paraphrase:  flatten_space turns Discrete, MultiBinary or MultiDiscrete into a Box. For a
             MultiDiscrete space, flatten is the concatenation of one one-hot vector per component,
             of length Σ n_d. It is not one index into the Π n_d joint actions. The
             DiscretizeAction wrapper maps a continuous Box action space to Discrete(bins^dims) by
             default. With multidiscrete=True it gives MultiDiscrete([bins, ..., bins]).
Locators:    flatten_space, flatten and flatdim entries on the utils page; DiscretizeAction
             docstring, Examples 2 and 3 (Reacher-v5: Discrete(100) versus MultiDiscrete([10 10])).
Quote:       "gymnasium.spaces.utils.flatten_space(space: Discrete | MultiBinary | MultiDiscrete) →
             Box" (signature on the utils page)
             "multidiscrete: If True, use MultiDiscrete action space instead of flattening to
             Discrete." (DiscretizeAction docstring)
```

Run in 1.4.0: `flatdim(MultiDiscrete([3, 4]))` is 7. `flatten(space, [2, 3])` is
`[0 0 1 0 0 0 1]`. `flatten_space` gives `Box(0, 1, (7,), int64)`. The joint count Π n_d for the
same space is 12.

### 5. Stable-Baselines3 2.9.2 documentation: which algorithms accept `MultiDiscrete`

```text
URL:         https://stable-baselines3.readthedocs.io/en/master/guide/algos.html (page title
             "RL Algorithms — Stable Baselines3 2.9.2 documentation"; the /en/stable/ path returned
             404). Release: PyPI stable-baselines3 2.9.2, uploaded 2026-10-26.
Kind:        primary. The SB3 maintainers document their own library.
Establishes: firsthand: which algorithms accept each action space.
Paraphrase:  Core SB3: A2C and PPO accept MultiDiscrete. DQN, DDPG, SAC, TD3 and HER do not. In the
             contrib and SBX rows (marked [1] and [2]), MaskablePPO, RecurrentPPO and TRPO accept
             MultiDiscrete, while QR-DQN and ARS do not. No value-based algorithm in the table
             accepts MultiDiscrete.
Locators:    the algorithm table at the top of the page, and the "Actions gym.spaces" list under it.
Quote:       "MultiDiscrete: A list of possible actions, where each timestep only one action of each
             discrete set can be used."
```

### 6. Stable-Baselines3 2.9.2 source: `MultiCategoricalDistribution`, env checker, DQN

```text
URL:         https://stable-baselines3.readthedocs.io/en/master/common/distributions.html (class
             entry for MultiCategoricalDistribution);
             https://stable-baselines3.readthedocs.io/en/master/_modules/stable_baselines3/common/distributions.html;
             https://stable-baselines3.readthedocs.io/en/master/_modules/stable_baselines3/common/env_checker.html;
             https://stable-baselines3.readthedocs.io/en/master/_modules/stable_baselines3/dqn/dqn.html
             (all HTTP 200). The same files at tag v2.9.2 live at
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/distributions.py
             and env_checker.py and dqn/dqn.py. github.com blob pages returned 403 through this
             session's proxy (gated); I read the files from raw.githubusercontent.com at the same
             tag (HTTP 200).
Kind:        primary (library source).
Establishes: firsthand: how SB3's policy-gradient agents represent a MultiDiscrete policy, what its
             checker warns about, and that its DQN refuses MultiDiscrete.
Paraphrase:  make_proba_distribution maps MultiDiscrete to MultiCategoricalDistribution(list(nvec)).
             One linear layer outputs sum(nvec) logits. They are split per component into
             independent Categoricals. log_prob and entropy are sums over components, and the
             deterministic action is the per-component argmax. The policy is therefore a product
             of per-component distributions. Its output count is Σ n_d, the same count as
             per-component value tables. The env checker warns when a Discrete or MultiDiscrete
             space has a non-zero start, and when nvec has more than one axis. DQN declares
             supported_action_spaces=(spaces.Discrete,).
Locators:    distributions.py: class MultiCategoricalDistribution (line 318 at v2.9.2), the
             proba_distribution_net / log_prob / mode methods, and make_proba_distribution
             (lines 690–691). env_checker.py: _starts_at_zero and _check_non_zero_start
             (lines 32–55); multi-axis nvec warning (lines 171–177). dqn.py line 132.
Quote:       "action_logits = nn.Linear(latent_dim, sum(self.action_dims))"
             "{type(space).__name__} {space_type} space {maybe_key} with a non-zero start
             (start={space.start}) is not supported by Stable-Baselines3."
```

What I ran with stable-baselines3==2.9.2 and torch 2.15.0+cpu on a toy env with
`MultiDiscrete([3, 4])`:

- `check_env` is silent with the default start. With `start=[1, 0]` it warns: "MultiDiscrete
  action space with a non-zero start (start=[1 0]) is not supported by Stable-Baselines3."
- `make_proba_distribution(MultiDiscrete([3, 4]))` returns `MultiCategoricalDistribution`.
- PPO's `policy.action_net` is `Linear(in_features=64, out_features=7)`. `predict` returns a
  length-2 integer array.
- `DQN("MlpPolicy", env)` raises `AssertionError: The algorithm only supports (<class
  'gymnasium.spaces.discrete.Discrete'>,) as action spaces but MultiDiscrete([3 4]) was
  provided`.

### 7. Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed.

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf (the authors' PDF; book page
             http://incompleteideas.net/book/the-book-2nd.html). Locators are printed page
             numbers; PDF page = printed + 22.
Kind:        primary for the textbook statement of the update rules and the deadly triad.
             Secondary for the convergence proofs it summarizes (Watkins and Dayan 1992 and
             others).
Establishes: firsthand: the Q-learning update (eq. 6.8), the semi-gradient action-value update
             (eq. 10.1), the step-size rule of thumb for linear features (eq. 9.19), and the
             deadly triad statement.
Paraphrase:  Q-learning updates Q(S_t, A_t) toward R_{t+1} + γ max_a Q(S_{t+1}, a). It converges
             to q* with probability 1 if every state–action pair keeps being updated and the step
             sizes meet the usual conditions; the result is stated for a table indexed by the
             (joint) action. The semi-gradient update moves the weights by
             α[U_t − q̂(S_t, A_t, w)] ∇q̂(S_t, A_t, w). With one-hot features per (state,
             component, level) and q̂ = Σ_d Q_d, each gradient entry is 1 for the D entries in use.
             That makes the shared-TD-error sum learner a semi-gradient method; this is my
             application of eq. 10.1, not the book's. For linear features, eq. 9.19 suggests
             α = (τ E[xᵀx])⁻¹. Here xᵀx = D, so a per-entry step of α/D matches a tabular step of
             α; again my application. The deadly triad (function approximation, bootstrapping,
             off-policy training) can cause instability even with linear approximation.
Locators:    §6.5, p. 131, eq. 6.8 and the paragraph below it (checked against a rendered image);
             §9.6, p. 223, eq. 9.19; §10.1, p. 244, eq. 10.1 and the paragraph after eq. 10.2;
             §11.3, p. 264.
Quote:       "Q(S_t, A_t) ← Q(S_t, A_t) + α[R_{t+1} + γ max_a Q(S_{t+1}, a) − Q(S_t, A_t)]"
             (p. 131, eq. 6.8)
             "Under this assumption and a variant of the usual stochastic approximation conditions
             on the sequence of step-size parameters, Q has been shown to converge with probability
             1 to q*." (p. 131)
             "Suitable techniques applicable to continuous actions, or to actions from large
             discrete sets, are a topic of ongoing research with as yet no clear resolution."
             (p. 244)
             "the danger of instability and divergence arises whenever we combine all of the
             following three elements" (p. 264)
```

### 8. Tang, Makar, Sjoding, Doshi-Velez and Wiens, "Leveraging Factored Action Spaces for Efficient Offline Reinforcement Learning in Healthcare" (NeurIPS 2022)

```text
URL:         https://papers.neurips.cc/paper_files/paper/2022/file/dda7f9378a210c25e470e19304cce85d-Paper-Conference.pdf
             (main text; locators "NeurIPS p."). Appendices from https://arxiv.org/abs/2305.01738
             (2 May 2023; comment "NeurIPS 2022"; locators "arXiv p."). OpenReview forum
             https://openreview.net/forum?id=Jd70afzIvJ4 (HTTP 200).
Kind:        primary for the linear decomposition analysis, the theorem and the bandit example.
             Authors: Shengpu Tang, Maggie Makar and Jenna Wiens (Division of Computer Science &
             Engineering, University of Michigan); Michael W. Sjoding (Division of Pulmonary and
             Critical Care, Michigan Medicine); Finale Doshi-Velez (SEAS, Harvard University).
Establishes: firsthand: the single-agent sum form Q(s, a) = Σ_d q_d(s, a_d); sufficient
             conditions for it to be exact; that none of those conditions is necessary; the
             free-parameter count; and a two-component bandit in which an interaction term makes
             the factored greedy choice wrong for some settings and right for others.
Paraphrase:  Eq. 1 writes Q^π(s, a) = Σ_{d=1}^D q_d(s, a_d), each term seeing the full state and one
             component. Theorem 1: the sum is exact for Q^π if, under some state abstractions,
             transitions factor per component (eq. 2), reward is a sum of per-component terms
             (eq. 3), and the policy factors (eq. 4). Propositions 2–4 show each condition can fail
             while Q^π is still additive. §3.3.1 says the sum cuts the free parameters from
             |S| Π_d |A_d| to |S|(Σ_d |A_d| − D + 1). Proposition 6 gives a one-step bandit with
             two binary components and rewards ↙ = [Left, Down] = 0, ↖ = [Left, Up] = α,
             ↘ = [Right, Down] = 1, ↗ = [Right, Up] = 1 + α + β. Fitting the sum by unweighted
             least squares, which drops the interaction β, gives Q̂ = (−β/4, α + β/4, 1 + β/4,
             1 + α + 3β/4) for (↙, ↖, ↘, ↗). Q̂ equals Q* only when β = 0. With α = 1 the greedy
             choice on Q̂ is still optimal for every β ≥ −1. The paper analyzes only this one-step
             case and says the sequential extension is "possible by applying induction". Appendix
             B.9 suggests adding interaction terms back (Q = Σ q_d + R(a)), pointing to Tavakoli
             et al.'s hypergraph paper.
Locators:    NeurIPS p. 2 Figure 1 and §2.2 eq. 1; p. 3 §3.1 Theorem 1 (eqs. 2–4); p. 4 §3.2
             Propositions 2–4; p. 5 §3.3.1 (parameter count, Proposition 5) and §3.3.2
             (Proposition 6, Figure 4); p. 6 the α = 1 and α, β sweeps, Figure 5 and §3.4. arXiv pp. 20–21 App. B.4
             (Definitions 3–5, Proposition 9, Corollaries 10–11); arXiv pp. 24–25 App. B.7–B.8
             (standardization and the omitted-variable derivation); App. B.9 follows B.8.
Quote:       "the linear parameterization reduces the number of free parameters from
             |S||A| = |S|(Π_{d=1}^D |A_d|) to |S|(Σ_{d=1}^D |A_d| − D + 1)" (NeurIPS p. 5)
             "Perhaps surprisingly, none of the conditions are necessary." (NeurIPS p. 4)
             "Note that Q̂ = Q* only when β = 0, i.e., there is no interaction between the two
             sub-actions." (NeurIPS p. 6)
             "When β ≠ 0, Q̂ is biased and RMSE > 0; however, for β ≥ −1, Q̂ corresponds to a
             policy that correctly identifies the optimal action." (NeurIPS p. 6)
             "Figure 1: ... (a) Learning with the combinatorial action space requires 2³ = 8 output
             heads (exponential in D), one for each combination of sub-actions. (b) Incorporating
             the linear Q decomposition for the factored action space requires 2 × 3 = 6 output
             heads (linear in D)." (NeurIPS p. 2)
```

### 9. Sunehag et al., "Value-Decomposition Networks For Cooperative Multi-Agent Learning" (2017)

```text
URL:         https://arxiv.org/abs/1706.05296 (v1, 16 Jun 2017). Locators are arXiv PDF pages.
Kind:        primary for the VDN method. Authors: Peter Sunehag and nine co-authors at DeepMind;
             Karl Tuyls is listed at "DeepMind & University of Liverpool".
Establishes: firsthand: a sum of per-agent action values trained with the Q-learning rule on one
             shared reward, through the sum; and that greedy per-agent choice maximizes the sum.
Paraphrase:  VDN assumes the joint action value is approximately the sum of per-agent terms
             Q̃_i(h_i, a_i). It trains them by backpropagating the Q-learning error on the joint
             reward through the summation, so no term has its own reward. Each agent acting
             greedily on its own Q̃_i picks the same joint action as maximizing the sum. If the
             reward splits as r1(o1, a1) + r2(o2, a2), Q^π splits into two matching terms. The
             setting is multi-agent; in the lesson the "agents" are action components of one
             agent.
Locators:    §3, p. 4 (the decomposition display, the training sentence, the central-arbiter
             sentence); p. 5 (the two-agent reward example).
Quote:       "We learn Q̃_i by backpropagating gradients from the Q-learning rule using the joint
             reward through the summation, i.e. Q̃_i is learned implicitly rather than from any
             reward specific to agent i" (p. 4)
             "each agent acting greedily with respect to its local value Q̃_i is equivalent to a
             central arbiter choosing joint actions by maximizing the sum Σ_{i=1}^d Q̃_i." (p. 4)
```

### 10. Son, Kim, Kang, Hostallero and Yi, "QTRAN" (ICML 2019)

```text
URL:         https://arxiv.org/abs/1905.05408 (v1, 14 May 2019; "Accepted to ICML 2019");
             proceedings page https://proceedings.mlr.press/v97/son19a.html (HTTP 200). Locators
             are arXiv PDF pages.
Kind:        primary for the IGM definition and for its own matrix-game runs. Authors: Kyunghwan
             Son, Daewoo Kim, Wan Ju Kang, David Hostallero, Yung Yi (School of Electrical
             Engineering, KAIST). Stake: QTRAN is the method proposed against VDN, so its VDN
             result comes from VDN's competitor.
Establishes: firsthand: the name and definition of the condition the lesson derives (the joint
             argmax equals the tuple of per-component argmaxes); that additivity is only
             sufficient for it; and a 3 × 3 one-step game where a trained sum picks a wrong pair.
Paraphrase:  Definition 1 (IGM, "Individual-Global-Max"): per-agent functions Q_i satisfy IGM for
             Q_jt if argmax over joint actions of Q_jt equals the tuple of per-agent argmaxes.
             Additivity (eq. 2) and monotonicity (eq. 3) are each sufficient for IGM. The game has
             payoff rows A: (8, −12, −12), B: (−12, 0, 0), C: (−12, 0, 0); the optimum is (A, A).
             The runs use "full exploration (i.e., ε = 1 in ε-greedy)". VDN learns
             Q1 = (−2.29, −1.22, −0.73) and Q2 = (−3.14, −2.29, −2.41), so the greedy pair is
             (C, B), with payoff 0 instead of 8.
Locators:    p. 1 Introduction right column ("only sufficient"); p. 3 §2.2 Definition 1 and the
             §2.3 eqs. 2–3; p. 6 §3.5 "Example: Single-state Matrix Game" and Table 1 (a), (e).
Quote:       "A task is factorizable if the optimal actions of the joint action-value function are
             the same as the optimal ones of the individual action-value functions, where additive
             decomposability and monotonicity are only sufficient — somewhat excessively
             restrictive — for factorizability." (p. 1)
             "However, in VDN, agents 1's and 2's individual optimal actions are C and B,
             respectively." (p. 6)
```

### 11. Matignon, Laurent and Le Fort-Piat, "Independent reinforcement learners in cooperative Markov games: a survey regarding coordination problems" (Knowledge Engineering Review 27(1), 2012)

```text
URL:         https://hal.science/hal-00720669 (author manuscript, HAL; PDF at
             https://hal.science/hal-00720669/document, HTTP 200). Journal DOI
             10.1017/S0269888912000057. Locators are the manuscript's printed page numbers.
Kind:        primary for its definitions, its decomposition of the coordination problem, and its
             worked computation (eq. 8). Secondary for the climbing and penalty games, which it
             credits to Claus and Boutilier (1998). Authors: Laëtitia Matignon, Guillaume J.
             Laurent, Nadine Le Fort-Piat (FEMTO-ST Institute, Besançon, France).
Establishes: firsthand: that an independent learner's local value Q_i(s, a_i) is defined under the
             others' policy, so its argmax moves with their exploration; the storage count Σ versus
             Π; and that local greedy choices can combine into a non-optimal joint action.
Paraphrase:  An independent learner stores Q_i(s, a_i), the expected return from taking a_i "and
             following π from then on" (eq. 5). So its value depends on the other agents' policy.
             Seven agents with six actions each store 42 values per state instead of 6^7. In the
             climbing game (rows agent 1, columns agent 2: a: 11, −30, 0; b: −30, 7, 6; c: 0, 0,
             5), (a, a) is optimal. If agent 2 plays uniformly, agent 1's values are
             Q1(a) = −6.33, Q1(b) = −5.67, Q1(c) = 1.67, so c looks best. This is the same
             computation a BDQ-form branch performs at a one-step state: averaging the reward over
             the other component's behavior.
Locators:    p. 4 Figure 1 (climbing and penalty games); p. 4 §3.1 and p. 5 eq. 5 and the 42
             versus 6^7 sentence; p. 5 §3.2; p. 6 §3.3 (non-stationarity); p. 7 §3.6, Definition 7
             and eq. 8.
Quote:       "For example, with 7 agents and 6 actions per agent only 42 Q-values have to be stored
             per state rather than 6^7 Q-values for joint-action learners." (p. 5)
             "It can happen that every agent selects an action that maximizes its own local
             Q-function, but that the combination of all agents' elementary actions is not
             Pareto-optimal." (p. 5)
             "The theoretical-optimal individual action is a but the action c has the highest
             current action-value due to the exploration policy of agent 2." (p. 7)
```

### 12. Tavakoli, Fatemi and Kormushev, "Learning to Represent Action Values as a Hypergraph on the Action Vertices" (ICLR 2021)

```text
URL:         https://arxiv.org/abs/2010.14680 (v2, 20 Jun 2021; comment "ICLR 2021"). Locators are
             arXiv PDF pages.
Kind:        primary. Authors: Arash Tavakoli (Imperial College London), Mehdi Fatemi (Microsoft
             Research Montréal), Petar Kormushev (Imperial College London). The first author also
             wrote BDQ, so this paper's description of BDQ comes from the BDQ authors.
Establishes: firsthand: that BDQ's authors describe BDQ as predicting per-dimension values
             "independently", distinct from a sum model; that their rank-1 model with a summation
             mixer is the sum form; and that a sum of per-dimension terms allows the maximizing
             action to be found per dimension in linear time.
Paraphrase:  The framework mixes per-hyperedge values into Q(s, a) (eq. 5). Hyperedges of size 1
             with a summation mixer give Q(s, a) = Σ_d Q_d(s, a_d). Leaving out the full
             interaction term limits what the model can represent and can bias it. With all
             hyperedges present, "even the simple summation mixer can be used without causing
             bias". Related work says earlier methods factor the action space and predict values
             "sequentially (Metz et al., 2017) or independently (Tavakoli et al., 2018)".
Locators:    p. 3 §3 eq. 5; p. 4 §3.1 (summation as the mixer); pp. 4–5 §3.2; p. 8 §7 Related Work;
             p. 9 (linear time with a strictly monotonic mixer).
Quote:       "Existing methods deal with the curse of dimensionality by factoring the action space
             and predicting action values sequentially (Metz et al., 2017) or independently
             (Tavakoli et al., 2018) across the action vertices." (p. 8)
             "1-complete models can achieve linear time complexity when used with a strictly
             monotonic mixer (e.g. summation) by enabling to find the action-value maximising
             actions in a decentralised manner." (p. 9)
```

## Contradictions

**C1. The action-branching form is not the sum form.** The commission's one idea writes
Q(s, a) ≈ Σ_d Q_d(s, a_d). It then asks for "a factored Q-learner with one table per component
trained on the shared TD target (the action-branching form)". BDQ never sums its branches. Each
branch's Q_d(s, a_d) is regressed onto the full target y = r + γ (1/N) Σ_d max Q_d(s', ·) (entry
1, eqs. 6–7). So each branch estimates the whole return given its own component, with the other
components drawn from the behavior. BDQ's own authors later call this predicting values
"independently" (entry 12, p. 8). The sum form trained on one shared TD error is VDN's (entry 9,
p. 4) and Tang et al.'s (entry 8, eq. 1). The tabular versions follow; these are my derivations,
not quoted from either source.

- Sum form. Compute δ = r + γ Σ_d max_b Q_d(s', b) − Σ_d Q_d(s, a_d), then do
  Q_d(s, a_d) += α δ for every d. The target is the ordinary Q-learning target max_a Q̂(s', a),
  because the max of a sum splits into per-component maxes. That split is the lesson's
  derivation. The update is semi-gradient (entry 7, eq. 10.1).
- BDQ form. Compute y = r + γ (1/N) Σ_d max_b Q_d(s', b), then do
  Q_d(s, a_d) += α (y − Q_d(s, a_d)) for every d. Each table holds a full return estimate.

I ran a throwaway least-squares check on one-step games. With each component explored
independently, the two forms rank each component's levels the same way. Their values differed
by a constant: −0.64 on every level in the QTRAN game with exploration weight 0.8 on A. The two
forms still differ in what a table means, in the bootstrapped target (sum of maxes or mean of
maxes), and whenever the exploration does not factor across components. The commission's
instruction to "name which target the factored learner uses and why" therefore needs the form
settled first. My question to the orchestrator is in the report.

**C2. "Exactly when" is too strong.** The commission says the per-component greedy choice is
the joint optimum "exactly when, at the state, the best level of each component does not depend on
the levels of the others". The sources make that condition sufficient, not necessary.

- Tang et al. Proposition 6 and Figure 5: with α = 1, Q̂ ≠ Q* for every β ≠ 0, yet the greedy
  choice is optimal for all β ≥ −1 (NeurIPS p. 6). Figure 5c shows zero suboptimality over "a wide
  range of α and β" (p. 6).
- QTRAN, p. 1: additivity is "only sufficient — somewhat excessively restrictive".
- The hypergraph paper, p. 8: strict monotonicity of the mixer is "a sufficient but not necessary
  condition".

A point inside Tang's family where the components depend on each other but the factored choice is
still right: α = −0.5, β = 2. The rewards are ↙ 0, ↖ −0.5, ↘ 1, ↗ 2.5. Down is best with Left
and Up is best with Right, so the best level depends on the other component. Tang's closed form
(arXiv App. B.8) gives Q̂ = (−0.5, 0.0, 1.5, 2.0), which picks ↗, the joint optimum. I computed
this value from Tang's formula; the paper does not print it. The reverse direction does hold in my
derivation: if each component's best level is the same whatever the others do, then any average
over the other components under product weights keeps that level on top. Proving that is the
page's own work. A defensible wording is: the factored choice can depart from the joint optimum
only at states where the best level of some component depends on the others, and it need not
depart at every such state.

**C3. Where Q* is not additive, the factored choice depends on the data.** An independent
learner's value is defined under the other agents' policy (Matignon et al., eq. 5). In the climbing
game, uniform exploration by agent 2 makes c look best to agent 1 (eq. 8, p. 7). QTRAN runs with
ε = 1 so that "we can compare only the expressive power of the methods" (p. 6), and Tang et al.'s
bandit fit weights all arms equally (App. B.8). So the published counterexamples assume uniform
data. In my throwaway check on the QTRAN game, putting exploration weight 0.8 on A for each
component made both factored forms choose (A, A), the optimum. Under ε-greedy, the learner's own
greedy choice shapes its data. So in an MDP run, whether and where it departs at an interacting
state can change with ε, the initial values and the seed. The commission's second result ("it
departs exactly at the interacting states") is safer stated as "departs only at interacting
states", with the departure checked across seeds.

**C4. The interaction need not be a reward term, and bias can travel through the target.**
Tang et al.'s Theorem 1 needs transitions to factor (eq. 2) as well as rewards (eq. 3) (NeurIPS
p. 3). The commission allows "a reward or transition term that depends on two components
together", which matches this. But a transition interaction makes Q* non-additive at that state,
and it can also make Q* non-additive at earlier states whose next state is chosen by the
components. The factored learner's target at a predecessor uses its own biased values at the
interacting successor. If the bias differs across successors in a non-additive way, the
predecessor's choice can shift too. That is my reasoning; no source here runs this sequential
case. Tang et al. analyze only the one-step bandit and say the sequential extension is "possible
by applying induction" (p. 5). For the "departs exactly at" prediction to be testable, the
environment has to keep interacting states from feeding a non-additive bias back into states the
lesson calls non-interacting. Two ways: interaction terms only on transitions into terminal
states, or successor states that the interacting components do not choose. Otherwise the
prediction has to include those predecessor states.

**C5. Stored values and free parameters are different counts.** The commission's Π n_d → Σ n_d
counts stored estimates per state, and BDQ Table 1, Tang Figure 1 and Matignon p. 5 count the same
way. Tang et al. count Σ n_d − D + 1 free parameters (§3.3.1), because adding c to one table and
subtracting c from another leaves every sum unchanged. The page should say which it counts.

**C6. In deep RL the sample-efficiency evidence is mixed.** In BDQ's N = 4, n = 5 reaching task
the joint learner "eventually converges and outperforms both BDQ agents" (p. 5). At N = 3 all
agents learn "at about the same rate". Kanervisto et al. "did not find notable difference" between
MultiDiscrete and Discrete outside Get-To-Goal (p. 7), and Get-To-Goal's Discrete variant also
removes diagonal moves (p. 4). Their agents are policy-gradient, not factored Q-learners. None of
this contradicts a tabular result. It does mean a general claim that factoring speeds learning
goes beyond the sources; the lesson's run has to carry its own claim.

**C7. Kanervisto's advice runs against what competition winners did.** Their Table I (p. 3)
reports that the 1st and 2nd places in MineRL (Discrete(10), Discrete(216)) and in Obstacle Tower
(Discrete(12), Discrete(6), from MultiDiscrete(3, 3, 2, 3)) used single Discrete spaces after
removing actions. Kanervisto et al. still advise against converting (p. 7). Both are accurate. A
sentence on "what practitioners do" should give both: winners often flattened after pruning, and
the controlled comparisons found no clear benefit from flattening.

**C8. No convergence guarantee covers either factored learner.** Sutton and Barto's convergence
statement for Q-learning is for a table over the actions the agent chooses, here the joint actions
(p. 131). The sum form is linear function approximation with bootstrapping trained off-policy, the
deadly triad (p. 264). BDQ, p. 3, says spreading the value over independent approximators "can lead
to convergence problems". BDQ and VDN both use deep networks with replay. Neither is tabular, and
neither proves convergence. I found no source proving convergence for tabular factored Q-learning
in either form.

**C9. Gymnasium's "flatten" means the opposite of the commission's "flattened".** The commission's
baseline uses "the flattened joint action", one Discrete index over Π n_d values. In Gymnasium,
`flatten_space(MultiDiscrete)` is a one-hot Box of length Σ n_d (entry 4). The lesson code should
build the joint index itself, for example with `np.ravel_multi_index`, and should not call
`gymnasium.spaces.utils.flatten` for this. The prose should say "joint action" or "one Discrete
action over all combinations" so that "flatten" does not carry two meanings. Gymnasium's
`DiscretizeAction` does produce a joint Discrete(bins^dims) by default (entry 4).

**C10. SB3 factors the policy by default.** Practice is not "flatten everything". SB3's PPO and A2C
treat a MultiDiscrete action as independent per-component categoricals with summed log-probability
(entry 6). Kanervisto et al. state the same as common practice (p. 2). That is the same
independence assumption on the policy side, with Σ n_d outputs. On the value side, SB3 has no
off-the-shelf learner for MultiDiscrete (DQN rejects it; entries 5–6).

## Numbers

```text
Figure: Π_d n_d joint actions versus Σ_d n_d per-component outputs (count, per state)
Owner:  Tavakoli et al. 2018, p. 1 and Table 1 (p. 7); Tang et al. 2022, Figure 1 (NeurIPS p. 2)
Scope:  any factored space; Tang's example D = 3 binary components: 2³ = 8 versus 2 × 3 = 6
```

```text
Figure: BDQ Table 1 series at n = 33 levels per dimension:
        Reacher-v1   N = 2   n^N = 1.1 × 10³    n × N = 66
        Hopper-v1    N = 3   n^N = 3.6 × 10⁴    n × N = 99
        Walker2d-v1  N = 6   n^N = 1.3 × 10⁹    n × N = 198
        Humanoid-v1  N = 17  n^N = 6.5 × 10²⁵   n × N = 561
Owner:  Tavakoli et al. 2018, Table 1, p. 7
Scope:  joint actions versus branch outputs per state; my arithmetic agrees (33¹⁷ ≈ 6.53 × 10²⁵)
```

```text
Figure: Reacher5DOF at n = 9: 9⁵ ≈ 6 × 10⁴ joint actions; the joint Dueling DDQN was not run
Owner:  Tavakoli et al. 2018, p. 6
Scope:  one custom task; the reason given is compute cost
```

```text
Figure: free parameters |S| Π_d |A_d| (joint) versus |S|(Σ_d |A_d| − D + 1) (sum form)
Owner:  Tang et al. 2022, §3.3.1, NeurIPS p. 5; derivation in arXiv App. B.4
Scope:  tabular MDP, per state times |S|
```

```text
Figure: 42 stored values per state for 7 independent learners × 6 actions, versus 6⁷ (= 279,936)
Owner:  Matignon et al. 2012, p. 5
Scope:  per state
```

```text
Figure: Tang bandit rewards (↙, ↖, ↘, ↗) = (0, α, 1, 1 + α + β); least-squares sum
        Q̂ = (−β/4, α + β/4, 1 + β/4, 1 + α + 3β/4)
Owner:  Tang et al. 2022, Figure 4 (NeurIPS p. 5), App. B.8 (arXiv pp. 24–25)
Scope:  one state, two binary components, unweighted fit (all four arms weighted equally)
```

```text
Figure: with α = 1, the greedy choice on Q̂ is optimal for β ≥ −1; Q̂ = Q* only at β = 0
Owner:  Tang et al. 2022, §3.3.2 and Figure 5a (NeurIPS pp. 5–6)
Scope:  β ∈ [−4, 4] in the paper's sweep
```

```text
Figure: QTRAN game payoff rows A (8, −12, −12), B (−12, 0, 0), C (−12, 0, 0); VDN learned
        Q1 = (−2.29, −1.22, −0.73), Q2 = (−3.14, −2.29, −2.41); greedy pair (C, B) earns 0, optimum
        (A, A) earns 8
Owner:  Son et al. 2019, Table 1 (a), (e), arXiv p. 6
Scope:  one-step game, ε = 1 for 20,000 steps
```

```text
Figure: climbing game rows a (11, −30, 0), b (−30, 7, 6), c (0, 0, 5); with agent 2 uniform,
        Q1(a) = −6.33, Q1(b) = −5.67, Q1(c) = 1.67
Owner:  Matignon et al. 2012, Figure 1 (p. 4) and eq. 8 (p. 7); the game is from Claus and
        Boutilier 1998
Scope:  one-step game, agent 2 uniform
```

```text
Figure: Kanervisto Atari: MultiDiscrete (joystick 9 × fire 2) versus Discrete(18); in MsPacman the
        multi-discrete agent scored "almost one-quarter higher"; elsewhere "no clear difference"
Owner:  Kanervisto et al. 2020, §III-C, p. 4 and Fig. 3 (p. 5)
Scope:  six games, PPO, five seeds, 10⁷ agent steps
```

```text
Figure: Gymnasium 1.4.0, MultiDiscrete([3, 4]): flatdim 7 (Σ n_d), joint count 12 (Π n_d);
        SB3 2.9.2 PPO action_net out_features = 7
Owner:  Gymnasium 1.4.0 and SB3 2.9.2 (runs described in entries 4 and 6)
Scope:  the toy space only
```

## Limits

- No source proves tabular factored Q-learning converges, in the sum form or in the BDQ form.
  Sutton and Barto's guarantee covers the joint table only (C8).
- No source measures how factored Q-learning's sample efficiency scales with the number of
  components in a tabular MDP. The nearest are BDQ's deep runs at N = 3, 4, 5 (mixed) and Tang et
  al.'s Proposition 5 (smaller function class, offline). The lesson's first result has to be
  established by its own run.
- No source states the commission's condition (each component's best level does not depend on the
  others) in those words. QTRAN defines the argmax condition (IGM), and Tang et al. and QTRAN show
  that additivity is sufficient but not necessary. The dominance condition and its proof have to
  be derived on the page (C2).
- No source runs a sequential MDP showing that departures stay confined to interacting states.
  Tang et al.'s bandit is one step (C4).
- BDQ says which target performed best (eq. 6) and that BDQ was "highly robust" to the target
  choice. It gives no theoretical reason for the mean target, so "why this target" cannot be
  quoted from BDQ.
- I could not open the IEEE Xplore record for Kanervisto et al. (gated). The arXiv v2 text was
  used.
- The commission names the lessons `finding-optimal-policies` and `sarsa-and-q-learning`. Per the
  brief I did not read the library, so I have not confirmed those slugs or what those lessons
  printed.

## Source assets

```text
Asset: Tavakoli et al. 2018, Figure 1 (arXiv p. 1), the shared module feeding N action branches
Shows: one shared state representation feeding one output branch per action dimension, with the
       joint action read off branch by branch
Crop:  keep the diagram and its labels; omit the surrounding text. It is a pointer figure; the
       lesson's learner is tabular.
```

```text
Asset: Tavakoli et al. 2018, Table 1 (arXiv p. 7)
Shows: n^N against n × N for four MuJoCo tasks at n = 33, from 1.1 × 10³ to 6.5 × 10²⁵ joint actions
Crop:  better retyped as a table on the page than cropped; keep all four rows and the n = 33 note
```

```text
Asset: Tang et al. 2022, Figure 1 (NeurIPS p. 2), combinatorial versus factored output heads
Shows: 8 heads, one per combination of three binary components, against 6 heads, two per component
Crop:  keep both panels (a) and (b) and the caption's head counts; a redrawn SVG would follow the
       site's themes better
```

```text
Asset: Tang et al. 2022, Figure 4 (NeurIPS p. 5), the two-component bandit, its linear system
       and the biased Q̂
Shows: where the interaction β enters the true values and how the least-squares sum spreads it
       over all four arms
Crop:  keep (a) the reward square and (c) the Q* versus Q̂ columns; (b) can go if the page derives
       the fit itself
```

```text
Asset: Tang et al. 2022, Figure 5 (NeurIPS p. 6), RMSE and suboptimality over α and β
Shows: Q̂ has error everywhere except β = 0, while the greedy choice is optimal over a much larger
       region
Crop:  panel (a) alone carries the point for α = 1; keep both of its curves and the β axis
```

```text
Asset: Son et al. 2019, Table 1 (a) and (e) (arXiv p. 6)
Shows: the 3 × 3 payoff with optimum (A, A) beside VDN's learned per-agent values selecting (C, B)
Crop:  keep (a) and (e) only; omit the QTRAN columns (b)–(d) and the QMIX column (f)
```

```text
Asset: Matignon et al. 2012, Figure 1 (p. 4), climbing and penalty games
Shows: small payoff tables where independent greedy choices miss the optimum
Crop:  better retyped as a table than cropped
```

```text
Asset: Kanervisto et al. 2020, Table I (arXiv p. 3)
Shows: original and transformed action spaces of competition entries, with RA, DC and CMD marks
Crop:  if used, keep the MineRL, Obstacle Tower and ViZDoom rows with their placings and
       references; retyping is clearer than a crop
```

```text
Asset: Gymnasium MultiDiscrete documentation (entry 3)
Shows: None found. The page is text and code; the Nintendo controller example is text.
```

```text
Asset: Stable-Baselines3 algorithm table (entry 5)
Shows: None found as an image. The table is text; retype the MultiDiscrete column if needed.
```

```text
Asset: Sutton and Barto (entry 7)
Shows: None found. The Q-learning box on p. 131 is better set as an equation.
```

```text
Asset: Sunehag et al. 2017 (entry 9), Tavakoli et al. 2021 (entry 12)
Shows: None found that the lesson needs. VDN's Figure 2 and the hypergraph paper's Figure 1 show
       deep architectures the lesson does not teach.
```

## Discarded

```text
https://stable-baselines3.readthedocs.io/en/stable/guide/algos.html: returned 404; the master docs, labelled 2.9.2, were used.
https://sb3-contrib.readthedocs.io/en/master/modules/ppo_mask.html: confirms MaskablePPO accepts MultiDiscrete actions; masking was taught earlier and removal is a later lesson, so the page has no use here.
https://gymnasium.farama.org/api/wrappers/action_wrappers/: read only to confirm that DiscretizeAction is not listed there (recorded in entry 4); nothing else used.
```
