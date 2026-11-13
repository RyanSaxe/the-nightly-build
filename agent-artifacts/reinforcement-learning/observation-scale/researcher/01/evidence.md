# Evidence: reinforcement-learning/observation-scale (researcher 01)

The sources support the lesson's linear derivation directly. LeCun, Bottou, Orr
and Müller's "Efficient BackProp" (1998) derives that gradient descent on a
quadratic diverges once the step size exceeds 2/λ_max of the Hessian, says that
convergence time is proportional to λ_max/λ_min, shows that for the LMS linear
learner the Hessian is the input second-moment matrix (1/P)Σ x xᵀ, and from that
recommends subtracting input means and equalizing input variances. Goh (Distill,
2017) gives the same step-size interval with the closed-form rate. Sutton and
Barto (2nd ed.) give the expected semi-gradient TD update in the (I − αA) form
the course already uses (Section 9.4) and a step-size rule of thumb set by
E[xᵀx] (Section 9.6). The current releases are Stable-Baselines3 2.9.2
(2026-10-26) and Gymnasium 1.4.0 (2026-10-05). I read the source of both and ran
the named calls under those pins. Andrychowicz et al. found input normalization
"crucial for good performance on all environments apart from Hopper" in a PPO-
style study of five MuJoCo tasks. The record is thin or cuts against the
commission in four places. SB3 does not save VecNormalize statistics inside the
model file, so "saved with the model" has to mean a second file saved beside
it. Gymnasium's freeze flag is a property, `update_running_mean`, and the
constructor rejects it as an argument. SB3's PPO trains a tanh network with
Adam, whose per-parameter step size is invariant to gradient scale (Kingma and
Ba), so the single-step-size eigenvalue argument is exact only for the linear
SGD learner and does not by itself explain a PPO result. No source states the
"one feature scaled by c moves its eigenvalue by about c²" step; it is the
writer's derivation to print and check with a run.

## Sources

### S1. LeCun, Bottou, Orr, Müller, "Efficient BackProp" (1998)

```text
URL:         http://yann.lecun.com/exdb/publis/pdf/lecun-98b.pdf
             (author reprint; published version https://doi.org/10.1007/3-540-49430-8_2,
             Neural Networks: Tricks of the Trade, LNCS 1524, Springer 1998, pp. 9-50.
             Reprinted in the 2012 2nd edition, LNCS 7700, pp. 9-48,
             https://doi.org/10.1007/978-3-642-35289-8_3. HTTPS on yann.lecun.com
             reset the connection during my check; the http address returned the PDF.)
Kind:        primary. The authors make and own the analysis and run the LMS example
             themselves.
Establishes: firsthand: the 1-D and N-D step-size bounds for gradient descent on a
             quadratic; that the LMS Hessian equals the input second-moment matrix;
             that a nonzero input mean creates a very large eigenvalue; the
             recommendation to center inputs, equalize their variances and decorrelate
             them; a worked LMS example where the predicted bound separates
             convergence from divergence.
Paraphrase:  Section 5.1: in one dimension, with E quadratic, the step that reaches
             the minimum in one move is eta_opt = (d²E/dW²)^-1 (eq. 24), and the
             largest step that does not diverge is eta_max = 2 eta_opt (eq. 26). In N
             dimensions the error near a minimum is expanded with the Hessian H
             (eq. 30); the update becomes (W(t+1) - W_min) = (I - eta H)(W(t) - W_min)
             (eq. 33); after rotating to H's eigenbasis each component is multiplied by
             (1 - eta lambda_i) each step (eq. 37), which converges iff
             |1 - eta lambda_i| < 1. With one scalar learning rate for all weights,
             eta < 2/lambda_max is required to avoid divergence (eq. 38), and
             eta_opt = 1/lambda_max is given for fastest convergence (eq. 39). If
             lambda_min is much smaller than lambda_max, convergence along the
             lambda_min direction is very slow; "convergence time is proportional to
             the condition number lambda_max/lambda_min". LMS example (eqs. 28-29):
             for a single-layer linear network with E(W) = (1/2P) Σ_p |d^p - Σ_i w_i
             x_i^p|², the Hessian is H = (1/P) Σ_p x^p x^pᵀ, so each eigenvalue
             measures the spread of the inputs along its eigendirection (Fig. 8).
             "Using a scalar learning rate is problematic in multiple dimensions": a
             large rate is wanted for shallow directions (small eigenvalues) but
             diverges along steep ones (large eigenvalues).
             Section 5.2, Linear Network: 100 examples from two Gaussian classes
             centred at (-0.4,-0.8) and (0.4,0.8); covariance eigenvalues 0.84 and
             0.036; batch LMS with eta = 1.5 and eta = 2.5; eta_max = 2/lambda_max =
             2/.84 = 2.38, so 2.5 diverges (Fig. 11). The stochastic version (Fig. 12)
             uses eta = 0.2.
             Section 5.3: "a nonzero mean in the input variables creates a very large
             eigenvalue", making the condition number large; so subtract the means.
             Inputs with very different spread along different directions give a
             large condition number and slow learning; so normalize the variances.
             If inputs are correlated, normalizing variances "will not make the error
             surface spherical, but it will possibly reduce its eccentricity"; so
             decorrelate them where possible.
             Section 4.3: first-layer weight updates are proportional to delta times
             the input vector x, so the same input-scale effect acts on a network's
             first layer. The "Transforming the Inputs" box: (1) average of each
             input near zero over the training set, (2) scale inputs so their
             covariances are about the same, (3) decorrelate if possible.
             Section 4.4: with sigmoid units (tanh included), "Because of the
             saturation of the sigmoids, the error surface is also flat far from the
             origin."
Locators:    The reprint carries no printed page numbers; PDF pages of the reprint:
             Sec. 4.3 and box, pp. 8-9; Sec. 4.4, pp. 10-12 (saturation sentence on
             p. 12); Sec. 5.1 starts p. 16, eqs. 24 and 26 on p. 18, eqs. 28-29 on
             pp. 18-19, eqs. 33, 37, 38, 39 on p. 20, condition-number sentence at
             top of p. 21; Sec. 5.2 Linear Network example p. 21, Fig. 11 p. 22,
             Fig. 12 p. 23; Figs. 7 and 8 p. 19; Fig. 3 p. 10; Sec. 5.3 p. 24.
Quote:       "If constrained to have a single scalar learning rate for all weights then
             we must require eta < 2/lambda_max in order to avoid divergence, where
             lambda_max is the largest eigenvalue of H." (Sec. 5.1, eq. 38; Greek
             letters spelled out here.)
             "In fact, convergence time is proportional to the condition number
             lambda_max/lambda_min so that it is desirable to have as small an
             eigenvalue spread as possible." (Sec. 5.1, PDF p. 21)
             "The reason for the above trick is that a nonzero mean in the input
             variables creates a very large eigenvalue." (Sec. 5.3)
```

Exact author affiliations as printed: Yann LeCun and Léon Bottou, Image
Processing Research Department, AT&T Labs - Research, Red Bank NJ; Genevieve B.
Orr, Willamette University; Klaus-Robert Müller, GMD FIRST, Berlin.

### S2. Gabriel Goh, "Why Momentum Really Works", Distill (2017)

```text
URL:         https://distill.pub/2017/momentum/   (doi 10.23915/distill.00006)
Kind:        secondary. A textbook exposition of a classical result by an author
             (byline: UC Davis, 4 April 2017) who did not originate it; every step of
             the derivation is printed and can be checked on the page.
Establishes: the closed form of gradient descent on a convex quadratic, the step-size
             interval, the rate as a function of step size, the optimal step and rate,
             and the name "condition number" for lambda_n/lambda_1.
Paraphrase:  For f(w) = ½ wᵀAw - bᵀw with A symmetric and invertible, gradient descent
             w^{k+1} = w^k - alpha(Aw^k - b) decouples in A's eigenbasis:
             x_i^{k+1} = (1 - alpha lambda_i) x_i^k. Each error component decays at
             rate |1 - alpha lambda_i|, so every workable step size satisfies
             0 < alpha lambda_i < 2 for all i. The overall rate is
             max{|1 - alpha lambda_1|, |1 - alpha lambda_n|} (lambda_1 smallest,
             lambda_n largest). It is minimized at alpha = 2/(lambda_1 + lambda_n),
             giving rate (kappa - 1)/(kappa + 1) with kappa = lambda_n/lambda_1, the
             condition number. kappa = 1 converges in one step; larger kappa is slower.
             The loss decomposes as f(w^k) - f(w*) = Σ (1 - alpha lambda_i)^{2k}
             lambda_i [x_i^0]², shown for eigenvalues 0.01, 0.1 and 1.
Locators:    sections "First Steps: Gradient Descent", "Decomposing the Error",
             "Choosing A Step-size" (the article has no page numbers).
Quote:       "In order to converge, each |1-alpha lambda_i| must be strictly less than
             1. All workable step-sizes, therefore, fall in the interval
             0 < alpha lambda_i < 2."
```

### S3. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed. (2018; 2020 PDF)

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (HTTPS on incompleteideas.net failed certificate verification through
             this session's proxy; the http address returned the PDF.)
Kind:        primary for the book's own statements of the linear semi-gradient TD
             expected update and its step-size rule of thumb. The convergence theory
             it reports in the box is attributed to Sutton (1988) and Varga (1962).
Establishes: the expected linear semi-gradient TD(0) update as
             E[w_{t+1}|w_t] = (I - alpha A) w_t + alpha b with A = E[x_t(x_t -
             gamma x_{t+1})ᵀ]; the diagonal-case intuition for choosing alpha; the
             rule of thumb alpha = (tau E[xᵀx])^-1 for linear SGD.
Paraphrase:  Section 9.4 (eqs. 9.10-9.13): once the system reaches steady state,
             E[w_{t+1}|w_t] = w_t + alpha(b - A w_t), b = E[R_{t+1} x_t],
             A = E[x_t (x_t - gamma x_{t+1})ᵀ]; the TD fixed point is w_TD = A^-1 b.
             Box "Proof of Convergence of Linear TD(0)": rewrite as (I - alpha A)w_t +
             alpha b; only A matters for convergence. If A is diagonal with positive
             entries, alpha "can be chosen smaller than one over the largest of them"
             so that I - alpha A has diagonal entries between 0 and 1; in general w_t
             shrinks toward zero whenever A is positive definite. On-policy, A =
             Xᵀ D (I - gamma P) X is positive definite.
             Section 9.6: a tabular step size alpha = 1/tau approaches the mean target
             after about tau experiences. For linear SGD, "A good rule of thumb ... is
             then alpha = (tau E[xᵀx])^-1" (eq. 9.19), where x is a random feature
             vector from the input distribution. "This method works best if the
             feature vectors do not vary greatly in length; ideally xᵀx is a
             constant." The book does not discuss eigenvalue spread or input
             normalization in 9.6.
Locators:    Sec. 9.4 begins p. 204; eqs. 9.10 at foot of p. 205, 9.11-9.13 p. 206;
             convergence box pp. 206-207. Sec. 9.6 pp. 222-223; eq. 9.19 p. 223.
Quote:       "This method works best if the feature vectors do not vary greatly in
             length; ideally xᵀx is a constant." (Sec. 9.6, p. 223)
```

### S4. Kingma and Ba, "Adam: A Method for Stochastic Optimization", ICLR 2015

```text
URL:         https://arxiv.org/abs/1412.6980   (read v9, PDF)
Kind:        primary. The authors define Adam and state its properties.
Establishes: that Adam's per-parameter step is invariant to rescaling of the gradient
             and approximately bounded by the step-size hyperparameter alpha.
Paraphrase:  Section 2.1: the effective step is Delta_t = alpha * m_hat_t /
             sqrt(v_hat_t); its magnitude is approximately bounded by alpha.
             Rescaling the gradients by c scales m_hat_t by c and v_hat_t by c², which
             cancel. The abstract states the method "is invariant to diagonal
             rescaling of the gradients".
Locators:    Abstract (p. 1); Introduction (p. 1); Sec. 2.1 "Adam's update rule",
             pp. 2-3.
Quote:       "The effective stepsize Delta_t is also invariant to the scale of the
             gradients; rescaling the gradients g with factor c will scale m_hat_t
             with a factor c and v_hat_t with a factor c², which cancel out"
             (Sec. 2.1, p. 3; symbols spelled out).
```

Why it is here: SB3's PPO uses Adam by default (S6), so the premise "a gradient
learner uses one step size for every input" holds for the lesson's linear SGD
learner and not as stated for the PPO run. See Contradictions.

### S5. Stable-Baselines3 2.9.2 on PyPI and its changelog

```text
URL:         https://pypi.org/project/stable-baselines3/2.9.2/
             https://stable-baselines3.readthedocs.io/en/master/misc/changelog.html
             (page title "Changelog — Stable Baselines3 2.9.2 documentation")
Kind:        primary. The maintainers publish the release and its notes.
Establishes: the current release, its date and its requirements.
Paraphrase:  The latest release on PyPI on 2026-11-13 is 2.9.2, uploaded
             2026-10-26 09:35 UTC; the changelog heads "Release 2.9.2 (2026-10-26)".
             Requires Python >= 3.10, gymnasium >= 0.29.1, < 2.0, numpy >= 1.20,
             < 3.0, torch >= 2.8, < 3.0. The changelog says 2.9.2 "will be the last
             one supporting Python 3.10" and recommends Python >= 3.11. Release 2.9.0
             (2026-06-15) relaxed the Gymnasium range to < 2.0 and raised the torch
             minimum to 2.8.
Locators:    PyPI JSON `info.version`, `info.requires_python`, `info.requires_dist`;
             changelog sections "Release 2.9.2 (2026-10-26)" and "Release 2.9.0
             (2026-06-15)", Breaking Changes.
```

### S6. Stable-Baselines3 2.9.2 source: VecNormalize, saving, evaluation sync, PPO defaults

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/vec_normalize.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/running_mean_std.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/base_class.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/__init__.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/callbacks.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/policies.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/ppo/ppo.py
             (I read the files from the 2.9.2 wheel and confirmed byte-identical with
             the v2.9.2 tag; WebFetch confirmed the vec_normalize.py page shows tag
             v2.9.2.)
Kind:        primary. The code is the API.
Establishes: constructor arguments and defaults; what `training` gates; the
             normalization formula and clipping; how save and load work; that model
             saving excludes the statistics; how EvalCallback hands statistics to the
             evaluation environment; PPO's default optimizer and activation.
Paraphrase:  VecNormalize.__init__(venv, training=True, norm_obs=True,
             norm_reward=True, clip_obs=10.0, clip_reward=10.0, gamma=0.99,
             epsilon=1e-8, norm_obs_keys=None). Only Box and Dict observation spaces
             are accepted (_sanity_checks). obs_rms is a RunningMeanStd per
             observation component (mean 0, var 1, count 1e-4 at construction;
             parallel-variance update). In step_wait and reset, obs_rms.update runs
             only when `self.training and self.norm_obs`; the return statistics for
             reward scaling update only when `self.training`. Normalization is
             clip((obs - mean)/sqrt(var + epsilon), -clip_obs, clip_obs), cast to
             float32. get_original_obs() returns the unnormalized observation.
             save(save_path) pickles the whole wrapper minus the inner venv ("all
             running statistics and settings (e.g. clip_obs)"), including the
             `training` and `norm_reward` attributes. VecNormalize.load(load_path,
             venv) is a staticmethod that unpickles and calls set_venv(venv); it
             returns the wrapper with the saved attribute values.
             BaseAlgorithm._excluded_save_params lists "env" and
             "_vec_normalize_env", so model.save(...) writes no normalization
             statistics. get_vec_normalize_env() returns the training wrapper.
             sync_envs_normalization(env, eval_env) deep-copies obs_rms and ret_rms
             from the training wrapper to the evaluation wrapper; it does not change
             the evaluation wrapper's `training` or `norm_reward`. EvalCallback calls
             it before every evaluation when the model has a VecNormalize.
             CheckpointCallback(save_vecnormalize=True) saves the statistics beside
             each checkpoint. make_vec_env always wraps each env in Monitor, so
             evaluate_policy reports unnormalized episode returns.
             PPO defaults: learning_rate 3e-4, n_steps 2048, batch_size 64,
             n_epochs 10. ActorCriticPolicy defaults: optimizer th.optim.Adam (eps
             set to 1e-5 when no optimizer kwargs are given), activation nn.Tanh,
             ortho_init True, net_arch pi=[64, 64], vf=[64, 64].
Locators:    vec_normalize.py: __init__ lines 35-98; _sanity_checks 100-126;
             step_wait 174-207 (training gate 186, 195); _normalize_obs 214-221;
             load 310-322; save 324-332. running_mean_std.py lines 4-55.
             base_class.py: _excluded_save_params 303-321; get_vec_normalize_env
             467-473. vec_env/__init__.py: sync_envs_normalization 56-84.
             callbacks.py: CheckpointCallback save_vecnormalize 264-319; EvalCallback
             sync 451-454. env_util.py Monitor wrap 107-113. ppo/ppo.py 84-87.
             policies.py 454-500 (Tanh, ortho_init, Adam, eps 472, net_arch 500).
```

### S7. Stable-Baselines3 2.9.2 documentation: Tips and Tricks, Examples, Callbacks

```text
URL:         https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html
             https://stable-baselines3.readthedocs.io/en/master/guide/examples.html#pybullet-normalizing-input-features
             https://stable-baselines3.readthedocs.io/en/master/guide/vec_envs.html#vecnormalize
             (each page title reads "... Stable Baselines3 2.9.2 documentation"; the
             same pages are served at /en/v2.9.2/. Source files docs/guide/rl_tips.md
             and examples.md at tag v2.9.2 match the rendered text.)
Kind:        primary. The library's maintainers give their own usage advice.
Establishes: SB3's advice to normalize agent input, and its documented save, load and
             freeze pattern for VecNormalize.
Paraphrase:  rl_tips, "General advice when using Reinforcement Learning" (under
             TL;DR): "When applying RL to a custom problem, you should always
             normalize the input to the agent (e.g. using `VecNormalize` for
             PPO/A2C)". Under "Continuous Actions - Multiprocessed" (PPO, TRPO, A2C):
             note "Normalization is critical for those algorithms". Under "Tips and
             Tricks when creating a custom environment": "always normalize your
             observation space if you can, i.e. if you know the boundaries".
             Examples, "PyBullet: Normalizing input features": normalizing input
             features "may be essential for successful training of an RL agent (by
             default, images are scaled, but other types of input are not)";
             VecNormalize "will compute a running average and standard deviation of
             the input features (it can do the same for rewards)". The listing trains
             PPO on VecNormalize(vec_env, norm_obs=True, norm_reward=True,
             clip_obs=10.0), then: "# Don't forget to save the VecNormalize
             statistics when saving the agent"; model.save(...);
             vec_env.save(stats_path) to "vec_normalize.pkl"; reload with
             VecNormalize.load(stats_path, vec_env); then sets
             `vec_env.training = False` ("do not update them at test time") and
             `vec_env.norm_reward = False` ("reward normalization is not needed at
             test time"); then PPO.load(..., env=vec_env).
             Callbacks guide: EvalCallback warns that eval_env must be wrapped the
             same way as the training env; CheckpointCallback can save VecNormalize
             statistics with save_vecnormalize (False by default).
Locators:    rl_tips.md lines 45, 145, 164 (tag v2.9.2); examples.md lines 397-447;
             callbacks.md lines 146-147, 184-187.
Quote:       "always normalize your observation space if you can, i.e. if you know the
             boundaries" (Tips and Tricks when creating a custom environment). The
             wording matters because it describes a fixed rescaling the environment
             author applies from known bounds, which is a different operation from
             VecNormalize's running statistics.
```

### S8. RL Baselines3 Zoo 2.9.2: PPO hyperparameters and normalization handling

```text
URL:         https://github.com/DLR-RM/rl-baselines3-zoo/blob/v2.9.2/hyperparams/ppo.yml
             https://github.com/DLR-RM/rl-baselines3-zoo/blob/v2.9.2/rl_zoo3/exp_manager.py
             https://rl-baselines3-zoo.readthedocs.io/en/master/guide/config.html#env-normalization
             (rl-zoo3 2.9.2 on PyPI, 2026-10-26; tag v2.9.2 commit 61956d9; docs page
             title "Configuration — RL Baselines3 Zoo 2.9.2 documentation")
Kind:        primary. The SB3 maintainers' own training configurations and code.
Establishes: which tuned PPO configurations turn on VecNormalize, and the Zoo's
             train/eval wiring of the statistics.
Paraphrase:  ppo.yml has 22 uncommented `normalize: true` entries, among them
             MountainCar-v0, MountainCarContinuous-v0, Acrobot-v1, BipedalWalker-v3,
             the PyBullet tasks and the MuJoCo v4 tasks; one entry normalizes reward
             only ("{'norm_obs': False, 'norm_reward': True}"); Pendulum-v1 and
             CartPole-v1 have no normalize key. Config docs, "Env Normalization":
             `normalize: True` wraps the training env in VecNormalize with default
             parameters except gamma, which is set to the agent's. exp_manager.py
             _maybe_normalize: an evaluation env gets VecNormalize with
             norm_reward=False and training=False; a pretrained agent's
             vecnormalize.pkl is loaded and then training and norm_reward are set
             False for evaluation. After training, the Zoo saves
             model.get_vec_normalize_env() to vecnormalize.pkl beside the model with
             the comment "Important: save the running average, for testing the agent
             we need that normalization"; EvalCallback's on-new-best callback is
             SaveVecNormalizeCallback.
Locators:    ppo.yml lines 50-63 (MountainCar entries) and passim; exp_manager.py
             lines 301-305 (save), 419-441 (_preprocess_normalization), 584-595
             (eval env and SaveVecNormalizeCallback), 631-666 (_maybe_normalize);
             docs/guide/config.md lines 31-47.
```

### S9. Gymnasium 1.4.0: release, NormalizeObservation source and documentation

```text
URL:         https://pypi.org/project/gymnasium/1.4.0/
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/stateful_observation.py
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/utils.py
             https://gymnasium.farama.org/v1.4.0/api/wrappers/observation_wrappers/#gymnasium.wrappers.NormalizeObservation
             https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.4.0
             (wheel files byte-identical to tag v1.4.0, commit 8ba8c3a; the versioned
             docs page returns 200 and matches the unversioned page; an invented
             version path returns 404.)
Kind:        primary. Farama's code and documentation.
Establishes: the current release; what NormalizeObservation computes; the name and
             form of its freeze flag; what it lacks next to VecNormalize.
Paraphrase:  Gymnasium 1.4.0 uploaded 2026-10-05 11:02 UTC, requires Python >= 3.10.
             NormalizeObservation(env, epsilon=1e-8) "Normalizes observations to be
             centered at the mean with unit variance". It replaces the observation
             space with Box(-inf, inf, shape, float32), keeps self.obs_rms (a
             RunningMeanStd with mean, var, count; count starts at 1e-4, and here its
             dtype follows the float32 observation space), and returns
             float32((obs - obs_rms.mean) / sqrt(obs_rms.var + epsilon)). It updates
             obs_rms on every step and reset while the flag is True. The flag is the
             property `update_running_mean` (backed by `_update_running_mean`,
             default True), set after construction: `env.update_running_mean =
             False`. It is not a constructor argument. There is no clipping and no
             save or load method; to evaluate with training statistics, a program has
             to copy obs_rms to the evaluation wrapper itself. Change log in the
             docstring: "v1.0.0 - Add `update_running_mean` attribute to allow
             disabling of updating the running mean / standard, particularly useful
             for evaluation time". The docstring note: "The normalization depends on
             past trajectories and observations will not be normalized correctly if
             the wrapper was newly instantiated or the policy was changed recently."
             A vector version, gymnasium.wrappers.vector.NormalizeObservation, has
             the same property. Release notes for 1.4.0: NormalizeObservation and
             NormalizeReward "now reject invalid gamma and epsilon values, which
             previously produced nan or diverging outputs" (the source raises
             InvalidBound for epsilon <= 0). RescaleObservation(env, min_obs,
             max_obs) in the same module family affinely maps a bounded Box to given
             bounds, the fixed-bounds alternative.
Locators:    stateful_observation.py: class NormalizeObservation lines 465-562,
             flag initialized line 544, property lines 546-554, observation() lines
             556-562; utils.py RunningMeanStd lines 33-71; vector/stateful_observation.py
             lines 29-140; transform_observation.py RescaleObservation line 517.
Quote:       "The property :attr:`update_running_mean` allows to freeze/continue the
             running mean calculation of the observation statistics. If ``True``
             (default), the ``RunningMeanStd`` will get updated every time ``step`` or
             ``reset`` is called. If ``False``, the calculated statistics are used but
             not updated anymore; this may be used during evaluation." (class
             docstring, identical on the docs page)
```

### S10. Andrychowicz et al., "What Matters In On-Policy Reinforcement Learning? A Large-Scale Empirical Study" (arXiv v1, 2020); published at ICLR 2021 as "What Matters for On-Policy Deep Actor-Critic Methods? A Large-Scale Study"

```text
URL:         https://arxiv.org/abs/2006.05990   (v1, 10 June 2020; the only arXiv version)
             ICLR 2021 version: https://openreview.net/forum?id=nIAxjsniDzg (gated by a
             browser check; not read. Title, authors and venue confirmed on
             https://research.google/pubs/what-matters-for-on-policy-deep-actor-critic-methods-a-large-scale-study/ )
Kind:        primary. The authors (Google Research, Brain Team) ran the experiments
             and report their findings.
Establishes: firsthand: that input normalization strongly affected performance in
             their PPO-style framework on four of five MuJoCo tasks and not on Hopper.
Paraphrase:  The study implements more than 50 choices in one on-policy framework
             (PPO loss among them) and trains over 250,000 agents on five Gym MuJoCo
             tasks (Ant-v1, HalfCheetah-v1, Hopper-v1, Humanoid-v1, Walker2d-v1).
             Observation normalization (choice C64) keeps the empirical mean and
             standard deviation of each observation coordinate over all observations
             seen so far and normalizes by subtracting the mean and dividing by
             max(std, 1e-6); optional clipping to [-o_max, o_max] is C65 (App. B.9).
             Section 3.3, Interpretation: "Input normalization (C64) is crucial for
             good performance on all environments apart from Hopper (Fig. 33)."
             Clipping normalized observations showed "little evidence" of helping.
             Recommendation: "Always use observation normalization and check if value
             function normalization improves performance."
             Design (App. F.1): for each environment, 2000 configurations sampled
             uniformly over PPO clip epsilon, input normalization {Average, None},
             input clipping, gradient clipping, advantage normalization, Adam
             learning rate {3e-5, 1e-4, 3e-4, 1e-3} and value normalization; 3 seeds
             per configuration. Fig. 33 reports, per environment, the 95th percentile
             of performance conditioned on the choice and the share of each option
             among the top 5% of configurations.
Locators:    Abstract; Sec. 3.3 "Normalization and clipping", arXiv v1 p. 6; App.
             B.9 "Data normalization and clipping", p. 16; App. F "Experiment
             Normalization and clipping", F.1 Design and Table 5, p. 28; Fig. 33,
             p. 29.
Quote:       "Input normalization (C64) is crucial for good performance on all
             environments apart from Hopper (Fig. 33)." (Sec. 3.3)
```

The finding is about a 95th-percentile statistic over randomly sampled
configurations, with every agent using Adam and the authors' default network. It
says nothing about tasks outside these five or about the size of the effect
for a tuned configuration.

### S11. Huang, Dossa, Raffin, Kanervisto, Wang, "The 37 Implementation Details of Proximal Policy Optimization", ICLR Blog Track (25 March 2022)

```text
URL:         https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
Kind:        primary for what openai/baselines' ppo2 does (the authors read and
             reimplemented the code; Antonin Raffin is an SB3 maintainer); secondary
             for the empirical finding, which it attributes to Andrychowicz et al.
Establishes: that observation normalization through VecNormalize is part of the
             reference PPO implementation's continuous-action setup, followed by
             clipping to about [-10, 10].
Paraphrase:  Section "9 details for continuous action domains (e.g. Mujoco)", detail 6
             "Normalization of Observation" (pointing at
             baselines common/vec_env/vec_normalize.py): VecNormalize preprocesses
             each observation before it reaches the PPO agent; Duan et al. (2016)
             used a moving-average normalization that "has also become the default
             choice for subsequent implementations"; "Andrychowicz, et al. (2021)
             experimentally determined that normalization for observation is very
             helpful for performance (decision C64, figure 33)". Detail 7
             "Observation Clipping": clipped "usually [-10, 10]"; Andrychowicz et al.
             found clipping did not help. The post runs no ablation of observation
             normalization of its own.
Locators:    section "9 details for continuous action domains (e.g. Mujoco)",
             details 6 and 7.
```

### S12. Gymnasium 1.4.0 MountainCar source (optional, for the commission's scale example)

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/envs/classic_control/mountain_car.py
Kind:        primary. The environment's own code and docstring.
Establishes: the observation ranges behind the commission's "position about 1,
             velocity about 0.07" example.
Paraphrase:  Observation 0, position, in [-1.2, 0.6]; observation 1, velocity, in
             [-0.07, 0.07] (self.min_position, self.max_position, self.max_speed).
Locators:    docstring "Observation Space" table lines 38-45; __init__ lines 109-111.
```

### Verification runs (mine, reproducible)

I ran two throwaway scripts with `uv run` under stable-baselines3==2.9.2,
gymnasium==1.4.0 and CPU torch, Python 3.11, on 2026-11-13. They are not on the
page; they show the named calls behave as described above. The writer's own
printed output supersedes them.

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["stable-baselines3==2.9.2", "gymnasium==1.4.0", "torch"]
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
# [tool.uv.sources]
# torch = { index = "pytorch-cpu" }
# ///
# (core of api_check.py)
train = VecNormalize(make_vec_env("Pendulum-v1", n_envs=1, seed=0))
model = PPO("MlpPolicy", train, n_steps=256, batch_size=64, seed=0, verbose=0)
model.learn(512)
model.save(d + "/ppo"); train.save(d + "/vecnormalize.pkl")
print(zipfile.ZipFile(d + "/ppo.zip").namelist())
loaded = VecNormalize.load(d + "/vecnormalize.pkl", make_vec_env("Pendulum-v1", n_envs=1, seed=1))
print(loaded.training, loaded.norm_reward)
ev = VecNormalize(make_vec_env("Pendulum-v1", n_envs=1, seed=2), training=False, norm_reward=False)
e = NormalizeObservation(gym.make("Pendulum-v1")); e.update_running_mean = False
NormalizeObservation(gym.make("Pendulum-v1"), update_running_mean=False)  # raises
```

Printed results:

```text
sb3 2.9.2 gymnasium 1.4.0
model zip members: ['data', 'pytorch_variables.pth', 'policy.pth', 'policy.optimizer.pth', '_stable_baselines3_version', 'system_info.txt']
after load: training = True norm_reward = True
loaded mean equals train mean: True count 513.0001
count unchanged with training=False: True
fresh eval VecNormalize: training False norm_reward False mean [0. 0. 0.] var [1. 1. 1.]
NormalizeObservation update_running_mean default: True has attr _update_running_mean True
frozen count unchanged: True obs_rms dtype float32 obs space Box(-inf, inf, (3,), float32)
constructor flag rejected: NormalizeObservation.__init__() got an unexpected keyword argument 'update_running_mean'
```

Second script (sync_check.py): a training VecNormalize(norm_reward=False) and an
evaluation VecNormalize(training=False, norm_reward=False) passed to EvalCallback
(eval_freq=256), PPO learns 512 steps.

```text
before: eval mean [0. 0. 0.] train mean [0. 0. 0.]
after: eval mean [-0.56  -0.003  0.135] eval count 513.0 train count 513.0
eval training flag still False ; obs_rms is a copy, not shared: True
```

## Contradictions

1. **Commission: running statistics "are saved with the model".** In SB3 2.9.2
   they are not inside the model file. model.save excludes "env" and
   "_vec_normalize_env" (S6), and the saved zip holds only data, policy and
   optimizer state (verification run). The statistics go to a second file with
   `vec_env.save("vec_normalize.pkl")`, which SB3's own example and the RL Zoo
   both do beside the model (S7, S8). Writing "saved alongside the model, in their
   own file" is accurate.

2. **The commission names `VecNormalize(training=False, norm_reward=False)` and
   `.save`/`.load` as if they compose directly.** They work as written, with two
   traps the page should state. (a) A freshly constructed evaluation wrapper
   starts at mean 0 and variance 1, which normalizes nothing: it passes raw
   observations through, clipped to ±10 (verification run). It only holds the
   training statistics after EvalCallback's sync_envs_normalization copies them
   before each evaluation, or after they are loaded or copied by hand (S6). A
   manual evaluate_policy call on such a wrapper without a sync evaluates the
   policy on unnormalized input. (b) `VecNormalize.load(path, venv)` restores the
   saved attribute values, so a wrapper saved during training comes back with
   training=True and norm_reward=True. Both must be set to False after loading
   (S6, S7; verification run printed `training = True norm_reward = True`).

3. **Commission: "gymnasium.wrappers.NormalizeObservation and its current update
   flag".** In 1.4.0 the flag is the property `update_running_mean`, set after
   construction (`env.update_running_mean = False`). Passing it to the
   constructor raises TypeError (verification run). The wrapper has no clipping
   and no save or load, so freezing for evaluation also means copying
   `obs_rms` from the training wrapper (S9).

4. **VecNormalize's defaults normalize reward too.** `VecNormalize(venv)` has
   norm_reward=True (S6). A raw-versus-normalized PPO comparison built with the
   default wrapper changes observation scale and reward scale at once, and the
   commission reserves reward scale for a later lesson. `norm_reward=False` on the
   training wrapper isolates observation normalization.

5. **One step size for every input (commission) versus Adam (S4, S6).** The
   derivation's premise is plain gradient descent. SB3's PPO uses Adam, whose
   per-parameter step is invariant to the scale of that parameter's gradient and
   bounded by about alpha. Scaling an input by c then no longer multiplies its
   first-layer weights' step by c as in SGD; what still changes is the size of
   the weight the network needs (1/c times smaller) and the output change per
   step (c times larger). That consequence is my arithmetic from Kingma and Ba's
   stated property, not a claim any source makes. Separately, SB3's default
   network uses tanh, and LeCun et al. Sec. 4.4 say saturation makes the error
   surface flat far from the origin, a second way large raw inputs can hurt. The
   commission already bounds the network claim ("do not claim more than the runs
   show"); these two sources are why the eigenvalue argument cannot be offered as
   the measured cause of a PPO gap without a removal test that separates it from
   saturation and Adam.

6. **"Normalizing each observation component removes that dependence"
   (commission).** Per-component centering and scaling makes the observation the
   same in either unit system (an affine change of one component's units leaves
   its standardized value unchanged, up to sign), so the dependence on units is
   removed. It does not make the error surface round. LeCun et al. Sec. 5.3: with
   correlated inputs, normalizing variances "will not make the error surface
   spherical, but it will possibly reduce its eccentricity". A page that shows
   the round surface after normalization should use features that are close to
   uncorrelated, or say that correlation keeps some elongation.

7. **Optimal single step size: LeCun versus Goh.** LeCun et al. eq. 39 give
   eta_opt = 1/lambda_max "for fastest convergence"; Goh gives the rate-minimizing
   step 2/(lambda_min + lambda_max) with rate (kappa - 1)/(kappa + 1). They agree
   on the divergence bound 2/lambda_max. LeCun's 1/lambda_max removes the steepest
   direction's error in one step, and Goh's balances the slowest and fastest
   directions. If the page names an optimal step, Goh's is the one that minimizes
   the overall rate.

8. **Expected update versus per-sample update.** The 2/lambda_max bound in S1 and
   S2 is for the deterministic (batch, expected) update; LeCun et al.'s worked
   bound (2.38) is for batch mode, and their stochastic run uses eta = 0.2. A
   single-sample gradient Monte Carlo update moves w only along x, and the error
   in that direction is multiplied by (1 - alpha ||x||²), so per-sample stability
   depends on ||x||² of the samples, the quantity Sutton and Barto's rule of
   thumb uses through E[xᵀx] (S3, eq. 9.19). This is my derivation, not a sourced
   bound. The consequence for the lesson: a run meant to confirm "stable below
   2/lambda_max" exactly should use the expected (full-batch) update, or the page
   should say which bound the per-sample run tests.

9. **Sutton and Barto's step-size condition is not 2/lambda_max.** In the Sec. 9.4
   box, for a diagonal A, alpha is chosen below one over the largest diagonal
   element so that every diagonal entry of I - alpha A lies between 0 and 1. That
   condition rules out oscillation; it is sufficient and stricter than the
   divergence bound. For semi-gradient TD, A = E[x(x - gamma x')ᵀ] is not
   symmetric and its eigenvalues can be complex, so "stable step below
   2/lambda_max" is exact only for the symmetric gradient Monte Carlo matrix
   E[x xᵀ]. Scaling feature i by c maps either matrix to D A D with D =
   diag(1, ..., c, ..., 1), which scales row i and column i by c and entry (i, i)
   by c²; the eigenvalue tied to feature i moves by exactly c² only when that
   feature is uncoupled from the others, and approximately otherwise (my
   derivation).

10. **Huang et al. misstate the divisor.** S11 says the raw observation is
    "divided by its variance". The code divides by sqrt(var + epsilon), the
    standard deviation (S6, S9). Cite the code, not the post, for the formula.

11. **SB3's custom-environment tip describes a different operation.** "Always
    normalize your observation space if you can, i.e. if you know the boundaries"
    (S7) is a fixed rescaling from known bounds inside or around the
    environment. VecNormalize and NormalizeObservation estimate running
    statistics that belong to the agent. Both appear on SB3's tips page. The
    commission's trap about frozen training statistics applies to the second
    only.

## Numbers

```text
Figure: eta < 2/lambda_max (single learning rate, gradient descent on a quadratic)
Owner:  LeCun et al. 1998, Sec. 5.1, eq. 38 (S1); same interval as 0 < alpha lambda_i < 2 in Goh 2017 (S2)
Scope:  quadratic error, batch (expected) update, H the Hessian

Figure: convergence time proportional to lambda_max/lambda_min
Owner:  LeCun et al. 1998, Sec. 5.1 (S1)
Scope:  quadratic error, one scalar learning rate

Figure: optimal alpha = 2/(lambda_1 + lambda_n); optimal rate = (kappa - 1)/(kappa + 1), kappa = lambda_n/lambda_1
Owner:  Goh 2017, "Choosing A Step-size" (S2)
Scope:  convex quadratic, A symmetric invertible, lambda_1 smallest

Figure: LMS example eigenvalues 0.84 and 0.036; eta_max = 2/0.84 = 2.38; eta = 1.5 converges, eta = 2.5 diverges (batch); eta = 0.2 used stochastically
Owner:  LeCun et al. 1998, Sec. 5.2, Figs. 11-12 (S1)
Scope:  100 examples, two Gaussian classes at (-0.4,-0.8) and (0.4,0.8), 2 inputs plus bias
        (condition number of that example: 0.84/0.036 = 23.3, my arithmetic)

Figure: alpha = (tau E[xᵀx])^-1
Owner:  Sutton and Barto 2nd ed., Sec. 9.6, eq. 9.19, p. 223 (S3)
Scope:  linear SGD, learning in about tau experiences with substantially the same feature vector

Figure: Stable-Baselines3 2.9.2, released 2026-10-26; requires Python >= 3.10, torch >= 2.8, gymnasium >= 0.29.1, < 2.0
Owner:  PyPI and SB3 changelog (S5)
Scope:  latest release as of 2026-11-13

Figure: Gymnasium 1.4.0, released 2026-10-05; requires Python >= 3.10
Owner:  PyPI (S9)
Scope:  latest release as of 2026-11-13

Figure: VecNormalize defaults training=True, norm_obs=True, norm_reward=True, clip_obs=10.0, clip_reward=10.0, gamma=0.99, epsilon=1e-8
Owner:  SB3 2.9.2 vec_normalize.py (S6)
Scope:  constructor

Figure: RunningMeanStd initial state mean 0, var 1, count 1e-4
Owner:  SB3 running_mean_std.py and Gymnasium wrappers/utils.py (S6, S9)
Scope:  both libraries, per observation component

Figure: NormalizeObservation epsilon default 1e-8; output float32; no clipping
Owner:  Gymnasium 1.4.0 stateful_observation.py (S9)

Figure: SB3 PPO defaults learning_rate 3e-4, n_steps 2048, batch_size 64, n_epochs 10; Adam eps 1e-5; Tanh; net_arch pi=[64, 64], vf=[64, 64]
Owner:  SB3 2.9.2 ppo.py, policies.py (S6)

Figure: over 250,000 agents; 5 environments; 2000 configurations per environment and 3 seeds each in the normalization experiment
Owner:  Andrychowicz et al., abstract and App. F.1 (S10)

Figure: input normalization crucial on 4 of 5 tasks (all but Hopper-v1)
Owner:  Andrychowicz et al., Sec. 3.3 and Fig. 33 (S10)
Scope:  95th percentile of performance over sampled configurations, Gym MuJoCo v1 tasks
```

Fig. 33 prints no numbers. My approximate readings of its left panel (95th
percentile score, normalization "Average" versus "None"), for a chart only if
labelled as read off the published figure: Hopper-v1 about equal; Humanoid-v1
about 2,700 versus 450; Walker2d-v1 about 1,800 versus 900; HalfCheetah-v1 about
2,100 versus 1,070; Ant-v1 about 2,450 versus 2,000. Right panel (share of the
top 5% of configurations using normalization): Hopper 0.5, Humanoid 1.0,
Walker2d 1.0, HalfCheetah about 0.87, Ant about 0.9, all tasks about 0.85.
These are readings, not reported values; prefer the paper's sentence.

```text
Figure: MountainCar position in [-1.2, 0.6], velocity in [-0.07, 0.07]
Owner:  Gymnasium 1.4.0 mountain_car.py (S12)
Scope:  observation space bounds; ranges 1.8 and 0.14
```

## Limits

- No source states the commission's specific step "scaling one feature by c moves
  the eigenvalue it controls by about c²". It follows from S1's Hessian
  H = (1/P)Σ x xᵀ and is the writer's to derive and check with a run
  (Contradiction 9 gives where "about" matters).
- No source applies the eigenvalue step-size argument to semi-gradient TD with
  input scaling. Sutton and Barto give the (I - alpha A) form and a diagonal-case
  step condition (Sec. 9.4) and the E[xᵀx] rule (Sec. 9.6), but say nothing on
  eigenvalue spread or normalization. The TD case rests on the course's own
  derivation in the deadly-triad lesson.
- I did not find an openly readable primary for the per-sample (stochastic) LMS
  stability bound in terms of ||x||² or tr E[x xᵀ] (Widrow's and Haykin's
  treatments are paywalled books and papers). Contradiction 8 gives it as my
  derivation only.
- The ICLR 2021 version of Andrychowicz et al. (OpenReview) was gated by a
  browser check and I could not read it. Section numbers, page numbers and the
  quoted sentences are from arXiv v1, which is the only arXiv version. Cite the
  arXiv text or confirm the published wording before quoting it.
- No source I read measures observation normalization for PPO on a small custom
  environment like the lesson's. The lesson's own seeds are the evidence for
  that result.
- No source separates conditioning from tanh saturation or Adam's per-parameter
  scaling as the cause of a PPO gap on raw observations (Contradiction 5).
- Everything else the brief asked for (versions, constructor arguments, training
  flag, norm_reward, save and load, SB3 and Zoo advice, the Gymnasium wrapper and
  its flag) is established from source code, documentation and a run.

## Source assets

```text
Asset: Fig. 7 "Lines of constant E" (a) elliptical contours with the Hessian's eigenvectors along the axes, (b) the same after rotation, with point P and the gradient arrow. LeCun et al. 1998, Sec. 5.1, reprint PDF p. 19.
Shows: the elongated error surface whose axes are the Hessian's eigendirections, and that the gradient does not point at the minimum.
Crop:  keep both panels and their axis labels (omega_1, omega_2; nu_1, nu_2); omit Fig. 8 below.

Asset: Fig. 8, input cloud with the eigenvectors of H drawn on it. LeCun et al. 1998, Sec. 5.1, reprint PDF p. 19.
Shows: for LMS, the eigenvalues of H measure the spread of the inputs; a stretched input cloud gives a stretched error surface.
Crop:  keep the caption sentence about LMS; the figure alone has no labels beyond x1, x2.

Asset: Fig. 11 (a) and (b), weight trajectory in weight space and log MSE per epoch for eta = 1.5 and eta = 2.5. LeCun et al. 1998, Sec. 5.2, reprint PDF p. 22.
Shows: the same linear learner converging just below and diverging just above eta_max = 2.38.
Crop:  keep both columns and the caption giving the two learning rates; the lesson's own SVG of its runs is the series' preference, so this is a reference image at most.

Asset: Fig. 3 "Transformation of inputs" (mean cancellation, KL expansion, covariance equalization). LeCun et al. 1998, Sec. 4.3, reprint PDF p. 10.
Shows: the three-step input transformation as point clouds.
Crop:  keep all three stages and their labels.

Asset: interactive figure under "Decomposing the Error" (per-eigenvalue error components for lambda = 0.01, 0.1, 1 with a step-size slider). Goh 2017.
Shows: how one step size serves eigenvalues of different size.
Crop:  interactive; a static capture loses the slider, so a capture would need the caption's three eigenvalues and one marked step size.

Asset: Fig. 33, left panel (95th-percentile score by input normalization choice, five tasks). Andrychowicz et al., arXiv v1 p. 29.
Shows: the gap on Humanoid, Walker2d, HalfCheetah and Ant, and none on Hopper.
Crop:  keep all five task panels and the "Average"/"None" tick labels and the caption; the right panel (top-5% shares) can be omitted. The bars have no printed values.
```

S2's static equations, S3, S4, S5, S6, S7, S8, S9, S11, S12: None found (text,
code listings and tables only).

## Discarded

```text
https://openreview.net/forum?id=nIAxjsniDzg: gated by a browser verification page; not read (see Limits).
https://openreview.net/pdf?id=nIAxjsniDzg: returned 403 HTML, not the PDF.
https://stable-baselines3.readthedocs.io/en/master/guide/rl_tips.html (WebFetch summary): truncated sentences; replaced by the v2.9.2 Markdown source and the rendered page fetched directly.
https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/docs/guide/rl_zoo.md: read for normalization advice; contains none. The Zoo's own config docs (S8) carry it.
Web search summary of Andrychowicz et al. (third-party blog digest linked from search results): not opened beyond the search snippet; the paper itself was read.
```
