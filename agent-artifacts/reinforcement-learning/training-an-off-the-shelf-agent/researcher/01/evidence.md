# Evidence: reinforcement-learning/training-an-off-the-shelf-agent (researcher 01)

The record supports the library half of the lesson in full. Stable-Baselines3 2.9.2 is the current release (PyPI, 26 October 2026). Its metadata admits gymnasium 1.4.0, and a two-line training call installed and ran under `uv run` with gymnasium 1.4.0 on Python 3.10 and on Python 3.13. Every mechanism the brief named has a line-level locator in the 2.9.2 source: one-hot preprocessing, `evaluate_policy` and `deterministic`, `EvalCallback`, Monitor, and the default hyperparameters. The SB3 docs give the separate-evaluation and several-runs advice in their own words. Henderson et al. 2018 show the seed effect in Fig. 5. Machado et al. 2018 is the strongest evidence against the commission's angle. For the Arcade Learning Environment they argue that a separate frozen-policy evaluation hides sample efficiency, and they propose the training curve's last episodes as the standard measure. Henderson et al. call that the "online view" and set it beside the "policy optimization view" the commission takes. Two findings from the course's own files change how the lesson's evaluation numbers can be read. First, SB3's Monitor and `evaluate_policy` report undiscounted episode sums, and the solved baseline values (−10.90 and 1.36) are discounted at `GAMMA = 0.9`. Second, the hand-drawn policy is already optimal in 12 of the 14 start cells, and the researcher computed the optimal mean over those cells as 1.61, only 0.25 above it. One episode's return has a standard deviation of about 8.5, so SB3's 5 to 20 evaluation episodes cannot place an agent between the hand-drawn policy and the optimum. The frozen greedy policy's value can, however, be solved exactly with the course's `exact_value`. The record is thin in two places. The course files that `grid_env.py` and `baselines.py` import (`mc_control.py`, `estimators.py`, `control.py`) were not opened, because the brief allowed `nb history` on three lessons only. The algorithm feasibility runs used the researcher's stand-in for `SlipperyGrid` and are not page evidence.

## Sources

### Stable-Baselines3 release and packaging

```text
URL:         https://pypi.org/project/stable-baselines3/2.9.2/
Kind:        primary. The maintainers' release record on PyPI owns the version, date and declared dependencies.
Establishes: Firsthand: 2.9.2 is the latest release (uploaded 2026-10-26T09:35:28; the previous release is 2.9.0 of 2026-06-15; there is no 2.9.1). Requires-Python >=3.10. Core dependencies: gymnasium>=0.29.1,<2.0; numpy>=1.20,<3.0; torch>=2.8,<3.0; cloudpickle.
Paraphrase:  The package declares that it works with any Gymnasium from 0.29.1 up to, not including, 2.0, so gymnasium==1.4.0 is inside the declared range.
Locators:    Project page "Meta" and "Requires" fields; same data in the JSON API's info.requires_dist. setup.py lines 82-84 and 140 of the 2.9.2 sdist carry the same pins.
Quote:       none needed
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/misc/changelog.html#release-2-9-2-2026-10-26
Kind:        primary. The maintainers' changelog for the release.
Establishes: Firsthand: 2.9.2 lists no new features and no breaking changes, only bug fixes, test and documentation changes. Its warning says 2.9.2 "will be the last one supporting Python 3.10". The 2.9.0 entry (2026-06-15) says "gymnasium 1.3.0 support" and, under Breaking Changes, relaxed the range from "gymnasium>=0.29.1,<1.3.0" to "gymnasium>=0.29.1,<2.0".
Paraphrase:  No changelog entry names Gymnasium 1.4.0. Support for 1.4.0 rests on the declared range and on the install check below, not on a statement from the maintainers.
Locators:    #release-2-9-2-2026-10-26 (warning box at top); #release-2-9-0-2026-06-15, first line and first Breaking Changes item.
Quote:       "Stable-Baselines3 (SB3) v2.9.2 will be the last one supporting Python 3.10 (end of life in October 2026)."
```

```text
URL:         https://pypi.org/project/torch/2.14.1/  and  https://pypi.org/project/torch/2.15.0/
Kind:        primary. PyTorch's release records own their supported Pythons and platforms.
Establishes: torch 2.15.0 (2026-10-28) requires Python >=3.11. torch 2.14.1 (2026-09-30) requires >=3.10 and ships wheels for cp310 to cp314 on macOS arm64, Linux x86_64 and aarch64, and Windows amd64. On Linux, the PyPI torch wheel depends on the nvidia-* CUDA 13 packages.
Paraphrase:  The same inline metadata resolves to torch 2.14.1 on Python 3.10 and to 2.15.0 on 3.11 and later, unless the script pins torch.
Locators:    each page's "Requires: Python" field and its file list.
```

```text
URL:         https://pypi.org/project/gymnasium/1.4.0/
Kind:        primary.
Establishes: gymnasium 1.4.0, uploaded 2026-10-05, Requires-Python >=3.10. This matches the date termination-and-truncation printed.
Locators:    project page "Meta".
```

### Stable-Baselines3 2.9.2 source

The source lives on GitHub at tag v2.9.2 (commit 0cdcd200deef06b9ad0af72f6ddfb07c06c6df39). The github.com blob pages returned 403 to an automated fetch, so they are gated, not dead. Each file below was read from the 2.9.2 sdist on PyPI and diffed against raw.githubusercontent.com at tag v2.9.2, and all 13 files are byte-identical. Line numbers are those of the tag. Each URL takes a `#Lnn-Lmm` anchor.

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/preprocessing.py
Kind:        primary. The library's own code owns what the network receives.
Establishes: preprocess_obs (L91) one-hot encodes a Discrete observation: L122-L124, `F.one_hot(obs.long(), num_classes=int(observation_space.n)).float()`. A non-image Box is cast to float (L116-L119). The replay and rollout buffers store a Discrete observation with shape (1,) (get_obs_shape, L153-L155). The flattened input size is gymnasium's flatdim (L169-L185), which is 16 for Discrete(16).
Paraphrase:  SlipperyGrid's integer cell s reaches the network as a vector of 16 floats with a 1 in position s. The researcher's check printed preprocess_obs(13) as a one-hot vector with the 1 in position 13, and the policy's input dimension as 16.
Locators:    L91-L124 (function), L122-L124 (Discrete branch), L153-L155.
Quote:       `return F.one_hot(obs.long(), num_classes=int(observation_space.n)).float()`
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/custom_policy.html#sb3-policy
Kind:        primary. The maintainers' documentation of the same behaviour.
Establishes: "All observations are first pre-processed (e.g. images are normalized, discrete obs are converted to one-hot vectors, ...) before being fed to the features extractor." The section #default-network-architecture gives the default MLP sizes.
Locators:    section "SB3 Policy", the Note box after the two-item list. Its next sentence: "In the case of vector observations, the features extractor is just a Flatten layer."
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/evaluation.py
Kind:        primary.
Establishes: evaluate_policy(model, env, n_eval_episodes=10, deterministic=True, render=False, callback=None, reward_threshold=None, return_episode_rewards=False, warn=True), L12-L22. The docstring says it returns "the average return per episode (sum of undiscounted rewards)" (L24-L25). A plain gym.Env is wrapped in a new DummyVecEnv (L65-L66). It warns when the env is not Monitor-wrapped (L68-L76). It calls env.reset() once with no seed (L88), then passes `deterministic` to model.predict on every step (L92-L97). If Monitor is present, it takes each episode's return from info["episode"]["r"] (L112-L124). Otherwise it sums the rewards as step returns them (L125-L128). It returns np.mean and np.std of the episode sums, or the lists themselves (L137-L143). Nothing in the loop bounds an episode's length.
Paraphrase:  The default evaluation is 10 greedy episodes, scored as undiscounted reward sums, from whatever random state the env's generator is in. A policy that never ends an episode makes the call run forever unless the env has a TimeLimit.
Locators:    L12-L22 signature; L24-L25; L31-L37 Monitor note; L65-L66; L88; L92-L97; L112-L128; L137-L143.
Quote:       "Runs the policy for ``n_eval_episodes`` episodes and outputs the average return per episode (sum of undiscounted rewards)."
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/common/evaluation.html
Kind:        primary (docs page generated from the same docstring).
Establishes: The same signature and defaults, and the note that wrappers that change rewards or lengths change the evaluation unless Monitor wraps the env first.
Locators:    "Evaluation Helper", the single entry.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/monitor.py
Kind:        primary.
Establishes: class Monitor(gym.Wrapper) (L17). step appends float(reward) every step (L97). When terminated or truncated, it sets ep_rew = sum(self.rewards), the plain undiscounted sum (L100), and ep_len = len(self.rewards) (L101). It writes ep_info = {"r": round(ep_rew, 6), "l": ep_len, "t": elapsed seconds} (L102), optionally to a CSV (L109-L110), and puts it in info["episode"] (L111). get_episode_rewards() returns every episode's sum (L131-L137).
Paraphrase:  Monitor's "episode reward" is the undiscounted total of the episode's rewards, recorded when either flag ends the episode. A TimeLimit cut counts as an episode end.
Locators:    L17; L87-L113 (step); L100-L102; L111; L131-L137.
Quote:       `ep_rew = sum(self.rewards)` (L100)
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/common/monitor.html
Kind:        primary.
Establishes: Monitor(env, filename=None, allow_early_resets=True, reset_keywords=(), info_keywords=(), override_existing=True); "it is used to know the episode reward, length, time and other data"; get_episode_rewards, get_episode_lengths.
Locators:    "Monitor Wrapper".
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/base_class.py
Kind:        primary.
Establishes: When an algorithm is given a gym.Env that is not yet Monitor-wrapped, _wrap_env wraps it in Monitor (L218-L221) and then in a one-env DummyVecEnv (L224). The full method is L204-L224. stats_window_size defaults to 100 (L112), and ep_info_buffer is a deque of that length (L405), filled from info["episode"] (L438-L457). The default predict has deterministic=False (L537-L557, the default at L541). set_random_seed(seed) seeds Python, NumPy and torch, the action space, and the training VecEnv (L559-L572; the env.seed call is L572).
Paraphrase:  PPO("MlpPolicy", TimeLimit(SlipperyGrid(), 200)) trains on DummyVecEnv[Monitor[TimeLimit[SlipperyGrid]]], as the researcher's check printed. The logged training curve is the mean undiscounted Monitor return over the last 100 training episodes. The model's seed seeds the training env and does not reach a separate evaluation env.
Locators:    L112; L204-L224; L405; L438-L457; L537-L557; L559-L572.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/on_policy_algorithm.py  (also off_policy_algorithm.py)
Kind:        primary.
Establishes: The training curve is logged as rollout/ep_rew_mean = safe_mean of ep_info["r"] over ep_info_buffer (on_policy_algorithm.py L291; off_policy_algorithm.py L440). PPO's rollout collection bootstraps a truncated episode's last reward with gamma times the value of info["terminal_observation"] when info["TimeLimit.truncated"] is set (on_policy_algorithm.py L234-L245).
Paraphrase:  SB3 applies the partial-episode bootstrapping that termination-and-truncation derived, through the TimeLimit.truncated flag.
Locators:    on_policy_algorithm.py L234-L245, L291; off_policy_algorithm.py L440.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/buffers.py
Kind:        primary.
Establishes: ReplayBuffer has handle_timeout_termination=True by default (L193). It records info["TimeLimit.truncated"] as a timeout (L277-L278) and, when sampling, removes the done mask for timeouts (L320-L322).
Paraphrase:  DQN's targets also bootstrap through a TimeLimit cut.
Locators:    L193; L277-L278; L320-L322.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/dummy_vec_env.py
Kind:        primary.
Establishes: step_wait (L56-L73) folds the two flags into done = terminated or truncated (L63) and sets info["TimeLimit.truncated"] = truncated and not terminated (L66). When an episode ends, it stores info["terminal_observation"] and resets the env at once (L68-L71). reset passes the stored seed, None unless .seed() was called (L75-L82).
Paraphrase:  Inside the library the reader meets a 4-tuple step and automatic resets. Stage 5 teaches that contract. To read the lesson's code, the reader needs only that model.get_env() returns this wrapper.
Locators:    L56-L73; L63; L66; L68-L71; L75-L82.
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/vec_envs.html#vecenv-api-vs-gym-api
Kind:        primary.
Establishes: The maintainers' statement of the same differences. reset() returns only the observation. Envs reset automatically. step returns (obs, rewards, dones, infos) with dones = terminated or truncated. infos[i]["TimeLimit.truncated"] marks a cut.
Locators:    section "VecEnv API vs Gym API", bullets 1-5.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/callbacks.py
Kind:        primary.
Establishes: EvalCallback(eval_env, callback_on_new_best=None, callback_after_eval=None, n_eval_episodes=5, eval_freq=10000, log_path=None, best_model_save_path=None, deterministic=True, render=False, verbose=1, warn=True) is defined at L342-L532, with defaults at L370-L383. The docstring calls eval_env "The environment used for initialization" and warns that with n_envs training envs one step is n_envs steps (L346-L350). A plain eval_env is wrapped in its own DummyVecEnv (L399-L403). The callback warns if the training and eval envs are not of the same type (L416-L419). Every eval_freq callback calls (L450), it runs evaluate_policy on eval_env with return_episode_rewards=True (L465-L474). It logs eval/mean_reward (L505), saves the results to evaluations.npz if log_path is set (L476-L495), and keeps the model with the highest mean so far as best_model (L518-L523). It never seeds eval_env.
Paraphrase:  The callback evaluates the current policy greedily on a second env object, 5 episodes at a time, as training runs. Its "best model" is the maximum over noisy evaluations.
Locators:    L342-L368 docstring; L370-L383; L399-L403; L447-L474; L505; L518-L523.
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/callbacks.html#evalcallback
Kind:        primary.
Establishes: "Evaluate periodically the performance of an agent, using a separate test environment." It also warns that eval_env must be wrapped the same way as the training env. The example uses a separate gym.make("Pendulum-v1") with deterministic=True.
Locators:    section "EvalCallback", first paragraph and Warning box.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/dqn/dqn.py  (with dqn/policies.py)
Kind:        primary.
Establishes: DQN defaults (L80-L108): learning_rate=1e-4, buffer_size=1_000_000, learning_starts=100, batch_size=32, tau=1.0, gamma=0.99, train_freq=4, gradient_steps=1, n_steps=1, target_update_interval=10000, exploration_fraction=0.1, exploration_initial_eps=1.0, exploration_final_eps=0.05, max_grad_norm=10, stats_window_size=100, seed=None. The exploration rate falls linearly from 1.0 to 0.05 over the first 10% of training (L155-L159, L187). predict (L236-L264) takes a uniformly random action with probability exploration_rate unless deterministic=True (L253). Otherwise it takes the argmax of the Q-network (dqn/policies.py L68-L72). MlpPolicy = DQNPolicy (dqn/policies.py L214), with net_arch [64, 64] (L134-L138) and ReLU (L117).
Paraphrase:  After training, DQN's predict(obs) with the base default deterministic=False still explores 5% of the time. evaluate_policy's default deterministic=True takes the greedy action.
Locators:    dqn.py L80-L108, L155-L159, L187, L236-L264 (L253); dqn/policies.py L68-L72, L117, L134-L138, L214.
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/modules/dqn.html
Kind:        primary.
Establishes: The same signature and defaults (section #parameters). "Default hyperparameters are taken from the Nature paper, except for the optimizer and learning rate that were taken from Stable Baselines defaults." The Notes say: "This implementation provides only vanilla Deep Q-Learning and has no extensions such as Double-DQN, Dueling-DQN and Prioritized Experience Replay." The Can I use? table lists Discrete observations as supported.
Locators:    #notes (Note box); #parameters (class signature and first paragraph); #can-i-use.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/ppo/ppo.py  (with common/policies.py, common/distributions.py)
Kind:        primary.
Establishes: PPO defaults (L80-L108): learning_rate=3e-4, n_steps=2048, batch_size=64, n_epochs=10, gamma=0.99, gae_lambda=0.95, clip_range=0.2, clip_range_vf=None, normalize_advantage=True, ent_coef=0.0, vf_coef=0.5, max_grad_norm=0.5, target_kl=None, stats_window_size=100, seed=None. MlpPolicy = ActorCriticPolicy (ppo/policies.py L5). Its default net_arch is dict(pi=[64, 64], vf=[64, 64]) (common/policies.py L496-L500), with Tanh (L454). With deterministic=True the action is the distribution's mode (distributions.py get_actions L82-L91), which for a Categorical is the argmax of the action probabilities (L304-L305). Otherwise the action is sampled.
Paraphrase:  PPO's training episodes sample actions from its policy. The frozen policy under deterministic=True picks the most probable action in each cell.
Locators:    ppo.py L80-L108; ppo/policies.py L5; common/policies.py L454, L496-L500; distributions.py L82-L91, L265, L304-L305.
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/modules/ppo.html
Kind:        primary.
Establishes: The same PPO signature and defaults.
Locators:    "Parameters", class signature.
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/algos.html#reproducibility
Kind:        primary.
Establishes: "Completely reproducible results are not guaranteed across PyTorch releases or different platforms." Results also need not match between CPU and GPU. For determinism on one platform, pass seed at model creation, and seed the env first if it is set with set_env(). The section "Training exceeds total_timesteps" adds that total_timesteps is a lower bound: PPO collects n_steps * n_envs = 2048 steps at a time.
Paraphrase:  A lesson's printed SB3 numbers will repeat on the writer's machine with fixed seeds, but a reader with another torch build or platform may print different numbers.
Locators:    #reproducibility, first two paragraphs; #training-exceeds-total-timesteps.
Quote:       "Completely reproducible results are not guaranteed across PyTorch releases or different platforms."
```

### Stable-Baselines3 advice on evaluation

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/rl_tips.html
Kind:        primary. The maintainers' own advice; they own the recommendation, not its truth on this grid.
Establishes: Firsthand, the library's recommendations.
             #tl-dr: "Evaluate the performance using a separate test environment (remember to check wrappers!)".
             #general-advice-when-using-reinforcement-learning, 3rd paragraph after the TL;DR list: results "may vary from one run to another (i.e., when only the seed of the pseudo-random generator changes). For this reason, you should always do several runs to obtain quantitative results." The 4th paragraph says: "don't expect the default ones to work in every environment."
             #how-to-evaluate-an-rl-algorithm: "Because most algorithms use exploration noise during training, you need a separate test environment to evaluate the performance of your agent at a given time. It is recommended to periodically evaluate your agent for n test episodes (n is usually between 5 and 20) and average the reward per episode to have a good estimate." It also advises trying deterministic=True with stochastic policies such as A2C or PPO, which "frequently leads to better performance", and says: "Looking at the training curve (episode reward as a function of timesteps) is a good proxy but underestimates the agent's true performance." It points to EvalCallback, to Deep Reinforcement Learning that Matters (arXiv 1709.06560), to rliable, and to Empirical Design in Reinforcement Learning (arXiv 2304.01315).
             #discrete-actions-single-process: "DQN with extensions (double DQN, prioritized replay, ...) are the recommended algorithms. We notably provide QR-DQN in our contrib repo. DQN is usually slower to train (regarding wall clock time) but is the most sample efficient (because of its replay buffer)."
             #discrete-actions-multiprocessed: "You should give a try to PPO or A2C."
             #tips-and-tricks-when-creating-a-custom-environment: return truncated=True for a timeout; TimeLimit does this automatically.
Paraphrase:  For one process and discrete actions, the docs recommend DQN with extensions, which SB3's own DQN lacks (see the DQN page). They recommend a separate test env, 5-20 test episodes, deterministic actions and several seeds. They say the training curve underestimates the agent.
Locators:    anchors as listed. In #how-to-evaluate-an-rl-algorithm, the separate-test-env and 5-20 episodes advice is the paragraph after the first Note box; deterministic=True and the training-curve sentence are the paragraph after the second Note box; the reading list follows.
Quote:       "Looking at the training curve (episode reward as a function of timesteps) is a good proxy but underestimates the agent's true performance."
```

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/examples.html#callbacks-evaluate-agent-performance
Kind:        primary.
Establishes: The maintainers' EvalCallback example. It builds the eval env with make_vec_env(..., n_envs=5, seed=0, env_kwargs={'g': 0.7}), a separate env deliberately given different physics, and evaluates 5 deterministic episodes every 500 steps. The "Basic Usage" example (first example on the page) instead calls evaluate_policy(model, model.get_env(), n_eval_episodes=10) on the training env after training.
Paraphrase:  The library's own examples use both a separate env during training and the training env after training. After training, nothing in the library requires a new object, so the separate env matters during training and for an independent random stream.
Locators:    #callbacks-evaluate-agent-performance (code comments); first example under "Basic Usage: Training, Saving, Loading".
```

### Primary sources on evaluation practice

```text
URL:         https://arxiv.org/abs/1709.06560  (published: Proceedings of the AAAI Conference on Artificial Intelligence 32(1), 2018, https://ojs.aaai.org/index.php/AAAI/article/view/11694, DOI 10.1609/aaai.v32i1.11694)
Kind:        primary. The authors ran and own the seed experiment and the recommendations.
Authors:     Peter Henderson, Riashat Islam, Joelle Pineau, Doina Precup, David Meger (McGill University); Philip Bachman (Microsoft; the paper prints "Microsoft Maluuba, Montreal"). Riashat Islam is listed with both. Henderson and Islam are marked as equal contributors.
Establishes: Firsthand: "Random Seeds and Trials" (subsection of Experimental Analysis, starting at arXiv v3 p. 3, results on p. 5). The authors ran 10 TRPO trials on HalfCheetah-v1 with one hyperparameter configuration, varying only the seed, and split them into two sets of 5. The two averaged learning curves are statistically different: Fig. 5 caption, "The average 2-sample t-test across entire training distribution resulted in t = −9.0916, p = 0.0016". They note that papers often report the top-N trials or average fewer than 5. They give no recommended number of trials and point to power analysis as an open question.
             "Reporting Evaluation Metrics", paragraph "Online View vs. Policy Optimization" (p. 6): in the online view, evaluation can use average cumulative reward across the whole learning process. In the policy optimization view, "evaluation is performed using a target policy in an offline manner", run over the full task trajectory. The authors say they focus on the policy optimization view.
             "Discussion and Conclusion", "What recommendations can we draw from our experiments?" (p. 7): "many trials must be run with different random seeds when comparing performance."
             Repeats only, not evidence for the angle: Tables 1 and 2 (p. 4) report "returns across the last 100 trajectories after 2M training samples", which are training trajectories.
Paraphrase:  Same code, same hyperparameters and different seeds gave two 5-seed averages from different distributions. The paper separates evaluating a frozen target policy from scoring returns while learning, and it chooses the first.
Locators:    arXiv v3 (30 Jan 2019, 26 pages including supplement): p. 3 right column ("Random Seeds and Trials"), p. 5 (Results paragraph and Fig. 5), p. 6 ("Online View vs. Policy Optimization"), p. 7 (recommendations). Supplement, "Modifications to Baseline Implementations": DDPG evaluation was changed to 10 full trajectories at the end of each epoch "while we take a policy optimization view when evaluating algorithms". The AAAI proceedings page range was not confirmed.
Quote:       "evaluation is performed using a target policy in an offline manner" (p. 6); "We demonstrate that the variance between runs is enough to create statistically different distributions just from varying random seeds." (p. 5)
```

```text
URL:         https://www.jair.org/index.php/jair/article/view/11182  (DOI 10.1613/jair.5699; Journal of Artificial Intelligence Research 61, 523-562, 2018; author version https://arxiv.org/abs/1709.06009, v2 of 1 Dec 2017)
Kind:        primary. The authors own the protocol proposal and its argument.
Authors:     Marlos C. Machado (University of Alberta), Marc G. Bellemare (Google Brain, Montréal), Erik Talvitie (Franklin & Marshall College), Joel Veness (DeepMind, London), Matthew Hausknecht (Microsoft Research, Redmond), Michael Bowling (University of Alberta and DeepMind, Edmonton), as printed on arXiv v2 p. 1.
Establishes: Firsthand, an argued position on evaluation protocol for the Arcade Learning Environment (ALE).
             §3.1 "Methodological Differences" (arXiv p. 5-7) lists divergent protocols: episode termination (training episodes ended at a lost life while evaluation episodes lasted the whole game), hyperparameter selection on a train/test split of games, measuring training data in frames, and summarizing performance. It also covers injecting stochasticity, because the deterministic ALE lets a memorized open-loop action sequence score well.
             §4.1 "Common Performance Measures" (p. 8). "Evaluation after learning", where a frozen policy is scored in evaluation episodes, "hides issues of sample efficiency". The authors add that "an agent could spend its training period in a purely exploratory mode ... and then at evaluation time switch to an exploitative mode", and that "ε-greedy policies tend to perform better than greedy policies in the ALE". "Evaluation of the best policy" adds a further problem: "the best score achieved across training is a statistically biased estimate of an agent's best performance", which needs "a second, independent evaluation". "Area under the learning curve" cannot tell unstable learning from steady progress.
             §4.2 "Proposal: Performance During Training" (p. 9): "At the end of training (and ideally at other points as well) report the average performance of the last k episodes. This protocol does not use the explicit evaluation phase, thus requiring an agent to perform well while it is learning."
             §6.1 "Experimental Method": the authors' benchmark reports the average of the last 100 training episodes before 10, 50, 100 and 200 million frames, averaged over 5 trials (DQN) and 24 trials (Sarsa(λ) + Blob-PROST), with sticky actions ς = 0.25.
Paraphrase:  For a benchmark meant to test continual learning, the authors prefer the training curve's tail to a separate frozen evaluation. They also warn that keeping the best of several evaluations during training is biased upward.
Locators:    §3.1 (arXiv pp. 5-7), §4.1 (p. 8), §4.2 (p. 9), §6.1; Fig. 1 (p. 9). JAIR printed page numbers not confirmed.
Quote:       "This protocol does not use the explicit evaluation phase, thus requiring an agent to perform well while it is learning." (§4.2)
```

### The course's earlier lessons (read only through `nb history --show reinforcement-learning/<slug>`)

`nb history` prints listings with their indentation stripped. Names and values below are exact. Indentation has to come from the published listing.

```text
URL:         nb history --show reinforcement-learning/environments-and-the-rl-problem
Kind:        primary. The course's own published lesson owns its files and printed numbers.
Title/date:  "The value of a state is an average you can solve for", 2026-10-31.
Establishes: gridworld.py, printed in full, with dependencies ["numpy"] and requires-python >=3.10. Names: N = 16; GOAL, PIT = 3, 6; TERMINAL = [GOAL, PIT]; ARROWS = "^>v<" (actions up, right, down, left are 0, 1, 2, 3); STEPS; R (np.full(N, -1.0) with R[GOAL] = 10.0, R[PIT] = -20.0, the reward for arriving in s'); draw(rows); PI, the hand-drawn fixed policy "> > > . / ^ ^ . ^ / ^ ^ > ^ / ^ ^ ^ ^"; STUCK, the same with the bottom row "v v v v"; move(s, a); transitions(slip), giving P[s, a, s'] with all-zero rows for terminal cells; fixed_policy(policy, slip), giving (Q, b); episode(P, policy, start, rng); discounted(steps, gamma); radius(A). evaluate.py defines its own GAMMA, SLIP = 0.9, 0.2 and LIVE.
             Behaviour that matters here: under STUCK, "no episode that enters the bottom row ever leaves it" (section "Only a policy that never ends needs the discount"). The hand-drawn policy's γ = 1 values are in Fig. 6.
Locators:    listing gridworld.py · complete; section "Only a policy that never ends needs the discount" (STUCK); Fig. 6 (γ = 1 panel).
```

```text
URL:         nb history --show reinforcement-learning/termination-and-truncation
Kind:        primary.
Title/date:  "Q-learning that treats its time limit as terminal learns the values of a different grid", 2026-11-06.
Establishes: grid_env.py, printed in full, with dependencies ["gymnasium==1.4.0", "numpy"] and requires-python >=3.10. It imports gymnasium as gym, mc_control, from gridworld import N, TERMINAL, and from gymnasium.wrappers import TimeLimit. class SlipperyGrid(gym.Env): observation_space = gym.spaces.Discrete(N), action_space = gym.spaces.Discrete(4). reset(self, *, seed=None, options=None) calls super().reset(seed=seed). It starts in options["start"] if given, otherwise in live[self.np_random.integers(len(live))] with live = mc_control.LIVE, and returns (self.cell, {}). step(action) runs reward, self.cell = mc_control.step(self.cell, action, self.np_random), sets terminated = self.cell in TERMINAL, and returns (self.cell, float(reward), terminated, False, {}).
             Reset distribution: uniform over the 14 non-terminal cells, or a fixed start through options={"start": s}. "A seed passed to the first reset makes a run repeatable, and later resets without one continue the same generator."
             Time limit: SlipperyGrid has none and "never returns truncated, because the grid has no limit of its own." The lesson wraps it as TimeLimit(SlipperyGrid(), max_episode_steps=4) in the demo and the main runs, and limits.py uses LIMITS = (2, 3, 4, 6, 10, 20, 200). The earlier Monte Carlo control capped episodes at CAP = 200 moves.
             Also printed: q_gym.py, with q_learning(env, eps, episodes, seed, cut_is_terminal=False, watch=None), which imports GAMMA from estimators and choose from td_control. limits.py computes Q_STAR = action_values(value_iteration(1e-12)[0], P) from control.py with P = transitions(SLIP). Its output prints the exact optimal values v* by cell:
               2.16  4.04  6.48  0.00
               0.61  0.06  0.00  6.48
              -0.71 -1.01  0.06  4.04
              -1.73 -0.71  0.61  2.16
             The lesson says "uv run limits.py needs gridworld.py, control.py, estimators.py, mc_control.py, td_control.py, grid_env.py and q_gym.py in one folder."
Locators:    section "Gymnasium's step reports the two endings as two flags" (grid_env.py and its output); section "The runs settle where each target's average puts them" (limits.py and its output, "exact optimal values v*").
```

```text
URL:         nb history --show reinforcement-learning/checking-a-custom-environment
Kind:        primary.
Title/date:  "Gymnasium's environment checker passes a grid with a backward slip", 2026-11-07.
Establishes: baselines.py, printed in full, with dependencies ["gymnasium==1.4.0", "numpy"]. It imports GAMMA from estimators; N, PI, R, TERMINAL, transitions from gridworld; LIVE, SLIP from mc_control. Names:
               random_policy(obs, rng) -> int(rng.integers(4))   # never reads the observation
               hand_drawn(obs, rng)    -> int(PI[obs])
               exact_value(probs)      -> mean of v_pi over the 14 cells reset starts from; probs[s, a] is the policy's probability of move a in cell s
               EXACT = {"random": exact_value(np.full((N, 4), 0.25)), "hand-drawn": exact_value(np.eye(4)[PI])}
               returns(env, policy, episodes, seed, watch=None) -> array of each episode's discounted return (GAMMA) from its start; first reset uses seed, later resets None; the policy's rng is np.random.default_rng((seed, 1))
             Solved values, as printed: −10.90 for random moves and 1.36 for the hand-drawn policy, "the mean of those values over the 14 cells reset starts from". These are discounted at GAMMA.
             GAMMA: "estimators.py, whose discount, GAMMA = 0.9, every return here uses" (Background band, row 04).
             behaviour.py (EPISODES, LIMIT = 4000, 200) printed sample sds of the discounted return: 7.30 (random) and 8.79 (hand-drawn), from 4,000 episodes, seed 0, under TimeLimit 200. In 4,000 random episodes no episode was cut at 200 moves, and undiscounted returns ran from −177 to 10.
             Folder: "The listings run with uv run from one folder that also holds gridworld.py, estimators.py, mc_control.py and grid_env.py".
             SB3 as stated in this lesson: "Stable-Baselines3 2.9.2, the current release ..., turns it into a one-hot vector of 16 floats before its network reads it." Confirmed above.
             The lesson's opening says a later lesson hands SlipperyGrid to an off-the-shelf agent. Its Go deeper band already links SB3's "Tips and Tricks when creating a custom environment".
Locators:    section "The rules fix what each baseline should earn" (baselines.py, behaviour.py, output); Background band row 04; section "The rules bound every number an agent will receive" (SB3 one-hot).
```

## Checks run for this record (researcher's scratch, under /tmp/claude-0/rl-research/)

These are checks, not page evidence. The writer's own runs must print every number the page uses.

1. Install. A script with inline metadata `dependencies = ["gymnasium==1.4.0", "stable-baselines3==2.9.2"]` and `requires-python = ">=3.10"`, containing `PPO("MlpPolicy", gym.make("FrozenLake-v1"), seed=0).learn(total_timesteps=4096)` and `DQN("MlpPolicy", gym.make("FrozenLake-v1"), seed=0).learn(total_timesteps=2000)`, ran under `uv run --python 3.10` (uv 0.11.32, Linux x86_64). It printed `python 3.10.20 gymnasium 1.4.0 sb3 2.9.2 torch 2.14.1+cu130` and the wrapper chain `DummyVecEnv <Monitor<TimeLimit<OrderEnforcing<PassiveEnvChecker<FrozenLakeEnv<FrozenLake-v1>>>>>>`. With an empty cache, uv downloaded about 2.9 GB of packages (torch 528.9 MiB plus the nvidia-* CUDA 13 wheels) and finished in 132 s on this machine's network. The same script with torch taken from https://download.pytorch.org/whl/cpu, through `[[tool.uv.index]]` (explicit) and `[tool.uv.sources]` in the inline metadata, installed torch 2.14.1+cpu (187.1 MiB) and ran in 22 s. Under `uv run --python 3.13` with the default index, the same two-line script printed `python 3.13.18 gymnasium 1.4.0 sb3 2.9.2 torch 2.15.0+cu132` and the same wrapper chain, after about 2.5 GB of listed downloads (860 s, with other jobs sharing the network).
2. A stand-in SlipperyGrid, built from the descriptions above with the slip rule as SlipBack's docstring states it, plus a copy of the printed gridworld.py. SB3's own `stable_baselines3.common.env_checker.check_env` passed it with no warnings. `PPO("MlpPolicy", TimeLimit(SlipperyGrid(), 200))` wrapped it as `Monitor<TimeLimit<SlipperyGrid>>` inside a DummyVecEnv, and check 6 trained on that. An unregistered instance needs no gym.make.
3. `evaluate_policy` with a fixed predictor playing STUCK, 20 episodes: without a TimeLimit it was still running after 10 s. Under TimeLimit(…, 200) it returned, with the longest episodes cut at 200 moves and a mean of −47.8. Six untrained DQN networks happened to end every episode.
4. `evaluate_policy` on an env without Monitor emitted the UserWarning "Evaluation environment is not wrapped with a ``Monitor`` wrapper." It returned undiscounted sums such as −27.0 for an 8-move episode. Two calls on identically pre-seeded envs (`env.reset(seed=123)` before the call) returned identical episodes.
5. Exact reference values from the printed gridworld.py: the researcher's value iteration, a policy solve, and the second moment of the return for its sd. The v* grid matches termination-and-truncation's printed v* in all 16 cells to two decimals. The figures are listed under Numbers.
6. Feasibility, 50,000 timesteps, gamma=0.9, all other hyperparameters at their defaults, TimeLimit 200, torch threads 1, Intel Xeon 2.80 GHz. Two seeds each, on the stand-in env.
   - DQN: 42 s and 38 s. The frozen greedy policies were worth 1.360 (exactly PI) and 1.356 (exact, γ = 0.9). The last-100 training ep_rew_mean values (undiscounted) were 2.35 and −0.72.
   - PPO: 49 s and 48 s. Both greedy policies were worth 1.609, the optimum. The last-100 training ep_rew_mean values were 1.82 and 1.05, against the optimum's undiscounted value of 2.67.
   - The values are exact solves of the extracted greedy policies, not sampled.
   Two seeds on a stand-in env settle nothing. They show only that either algorithm runs in under a minute per seed at this budget, and that SB3's DQN at its defaults can stop at the hand-drawn level.


## Contradictions

- **Machado et al. 2018 against the commission's idea.** The commission says the training curve alone does not show how good a trained agent is, and that the agent is judged by its frozen policy in a separate evaluation env. Machado et al. argue the opposite as the standard for the ALE. In §4.1, evaluation after learning "hides issues of sample efficiency" and rewards an agent that explores in training and exploits at evaluation. In §4.2, they propose the average of the last k training episodes, with no evaluation phase. They report their own benchmark that way (§6.1). Henderson et al. (p. 6) name the two positions as the online view and the policy optimization view, and choose the second. The two papers ask different questions. Machado et al. ask how well the agent does while it learns, and Henderson et al. ask what the learned policy earns. The commission's question is Henderson's. The lesson can state Machado's view in their words ("requiring an agent to perform well while it is learning") and say which question each measure answers. The view does not refute the idea, but it is a real disagreement about what to report.
- **Greedy or exploring at evaluation.** SB3 says deterministic=True "frequently leads to better performance" (RL Tips, #how-to-evaluate-an-rl-algorithm). Machado et al. (§4.1) report that ε-greedy beats greedy in the ALE and that many evaluations there are run ε-greedy. On SlipperyGrid, a greedy policy can loop for ever: STUCK keeps any episode that enters the bottom row there, and check 3 confirms that evaluate_policy never returns without a TimeLimit. Whether greedy evaluation helps depends on the environment.
- **"Best model" selection.** EvalCallback keeps the model with the highest mean over 5-episode evaluations (callbacks.py L518-L523). Machado et al. (§4.1) call the best score across training "a statistically biased estimate" that needs an independent second evaluation. A lesson that reports EvalCallback's best_mean_reward reports a biased maximum.
- **Henderson's own tables.** The paper says it takes the policy optimization view, yet Tables 1 and 2 report returns over the last 100 training trajectories. Henderson et al. can be cited for the seed experiment and the two-view distinction, and not as an example of reporting frozen-policy evaluations.
- **The docs' algorithm recommendation.** RL Tips recommends "DQN with extensions (double DQN, prioritized replay, …)" for one process and discrete actions. SB3's DQN page says its DQN has no extensions. In two stand-in seeds (check 6), default DQN stopped at the hand-drawn policy's value and default PPO reached the optimum. The writer's choice is open on the evidence. It needs the writer's own seeds before the handoff justifies it.
- **The docs' episode count against this grid's noise.** The docs' "n is usually between 5 and 20" gives a standard error of 3.81 to 1.91 on one policy's mean discounted return here (sd ≈ 8.5), against a 0.25 gap between the hand-drawn policy and the optimum. The docs' default cannot separate an agent from the hand-drawn baseline on SlipperyGrid.
- **The commission's "fixed reference above and below".** The references exist and are exact: random −10.90, hand-drawn 1.36, optimal 1.61, mean over the 14 start cells at γ = 0.9. The hand-drawn policy, however, already takes an optimal action in 12 of the 14 cells. The band above it is 0.25 wide, and the band below it is 12.26.
- **"The optimal arrows from the exact solve" are not unique.** The grid is symmetric about its anti-diagonal: the goal (3) and the pit (6) lie on it, and the reflection swaps up with right and down with left. So q*(9, up) = q*(9, right) and q*(12, up) = q*(12, right) exactly. The researcher checked this numerically at γ = 0.9 and 0.99, and the symmetry argument covers any discount. An argmax over q* picks one of the tied actions by floating-point noise. A learned policy that aims right in cell 9 or 12 is optimal. The researcher's value iteration printed "right" in cell 12 at γ = 0.9 and "up" at γ = 0.99, with identical policy values.
- **Units.** The course's solved values are discounted (GAMMA = 0.9, from each start). Monitor, rollout/ep_rew_mean, evaluate_policy and EvalCallback all report undiscounted episode sums. SB3's default gamma is 0.99. These are not disagreements between sources. They will produce a false comparison if a listing sets −10.90 or 1.36 beside an evaluate_policy mean. The undiscounted equivalents are under Numbers.
- Searched and not found: an SB3 statement that contradicts its own evaluation advice. Its "Basic Usage" example evaluates on model.get_env() after training, and its EvalCallback example uses a separate env during training. The docs give exploration noise during training as the reason for a separate env (RL Tips, #how-to-evaluate-an-rl-algorithm), and that reason does not apply once training has stopped.

## Numbers

```text
Figure: Stable-Baselines3 2.9.2, uploaded 2026-10-26; Requires-Python >=3.10; gymnasium>=0.29.1,<2.0; torch>=2.8,<3.0
Owner:  PyPI release record (stable-baselines3 2.9.2)
Scope:  the current release as of 2026-11-08
```

```text
Figure: Python 3.10 resolves torch 2.14.1; Python >=3.11 resolves torch 2.15.0 (torch 2.15.0 requires >=3.11)
Owner:  PyPI release records for torch 2.14.1 and 2.15.0; observed in check 1 (3.10 gave 2.14.1+cu130, 3.13 gave 2.15.0+cu132)
Scope:  unpinned torch under SB3's torch>=2.8,<3.0, November 2026
```

```text
Figure: about 2.9 GB of package downloads (torch 528.9 MiB plus CUDA 13 wheels) on Linux x86_64 with the default index; 187.1 MiB torch with the CPU index
Owner:  researcher's check 1 (uv output)
Scope:  first run with an empty uv cache, Python 3.10, Linux x86_64 (Python 3.13 listed about 2.5 GB more for its own wheels); macOS and Windows not tested
```

```text
Figure: evaluate_policy defaults: n_eval_episodes=10, deterministic=True; returns mean and std of undiscounted episode sums
Owner:  SB3 2.9.2 common/evaluation.py L12-L25
Scope:  per call
```

```text
Figure: EvalCallback defaults: n_eval_episodes=5, eval_freq=10000 (callback calls), deterministic=True
Owner:  SB3 2.9.2 common/callbacks.py L370-L383
Scope:  per evaluation
```

```text
Figure: training curve window: last 100 episodes (stats_window_size=100), undiscounted Monitor sums
Owner:  SB3 2.9.2 common/base_class.py L112, L405; on_policy_algorithm.py L291
Scope:  rollout/ep_rew_mean at each log
```

```text
Figure: DQN defaults: learning_rate 1e-4, buffer_size 1,000,000, learning_starts 100, batch_size 32, tau 1.0, gamma 0.99, train_freq 4, gradient_steps 1, n_steps 1, target_update_interval 10,000, exploration 1.0 -> 0.05 over the first 10% of training, max_grad_norm 10, net [64, 64] ReLU
Owner:  SB3 2.9.2 dqn/dqn.py L80-L108; dqn/policies.py L117, L134-L138
Scope:  constructor defaults
```

```text
Figure: PPO defaults: learning_rate 3e-4, n_steps 2048, batch_size 64, n_epochs 10, gamma 0.99, gae_lambda 0.95, clip_range 0.2, ent_coef 0.0, vf_coef 0.5, max_grad_norm 0.5, nets pi [64, 64] and vf [64, 64] Tanh
Owner:  SB3 2.9.2 ppo/ppo.py L80-L108; common/policies.py L454, L496-L500
Scope:  constructor defaults
```

```text
Figure: SB3 advice: 5 to 20 test episodes per evaluation
Owner:  SB3 RL Tips and Tricks, #how-to-evaluate-an-rl-algorithm
Scope:  per evaluation, general advice
```

```text
Figure: GAMMA = 0.9
Owner:  estimators.py, as stated in checking-a-custom-environment (Background band, row 04)
Scope:  every discounted return in the course's baselines
```

```text
Figure: solved baseline values: random −10.90, hand-drawn 1.36 (discounted return at GAMMA = 0.9, mean of v_pi over the 14 non-terminal start cells)
Owner:  baselines.py EXACT, printed in checking-a-custom-environment
Scope:  uniform start over the 14 cells reset draws from; slip 0.2
```

```text
Figure: optimal policy's value: 1.6089, mean of v* over the 14 start cells at γ = 0.9 (researcher's value iteration; equals the mean of the printed v* grid, 22.54 / 14 = 1.61)
Owner:  derived from the v* grid printed by limits.py in termination-and-truncation; the lesson's own script must print it (control.py's value_iteration)
Scope:  same start distribution and discount as EXACT
```

```text
Figure: gaps between the references: optimal − hand-drawn = 0.249; hand-drawn − random = 12.26
Owner:  arithmetic on the two lines above
Scope:  discounted, γ = 0.9
```

```text
Figure: hand-drawn policy versus optimal, per cell (γ = 0.9): optimal in 12 of 14 cells; suboptimal only in cell 13 (q* gap 1.117) and cell 14 (gap 1.439), where right is optimal and PI aims up; exact ties between up and right in cells 9 and 12
Owner:  researcher's q* from the printed gridworld.py (check 5); v* matches the published grid
Scope:  slip 0.2; the optimal actions were checked cell by cell at γ = 0.9 and 0.99 and are the same set; at γ = 1 the solved optimal policies have the same value
```

```text
Figure: sd of one episode's discounted return from a uniform start (γ = 0.9): random 7.215, hand-drawn 8.787, optimal 8.524 (exact second moment). Lesson 8's sample sds: 7.30 and 8.79
Owner:  researcher's check 5; behaviour.py output for the sample values
Scope:  one episode, start uniform over 14 cells
```

```text
Figure: standard error of a mean over n evaluation episodes, optimal policy, discounted: n=5: 3.81; n=10: 2.70; n=20: 1.91; n=100: 0.85; n=1000: 0.27; n=4000: 0.13; n=10000: 0.09. Episodes needed for SE = 0.083 (one third of the 0.249 band): about 10,500
Owner:  arithmetic on sd 8.524
Scope:  independent episodes from uniform starts; no stratification by start cell
```

```text
Figure: undiscounted (γ = 1) means over the 14 start cells, the units Monitor and evaluate_policy report: random −29.96, hand-drawn 2.35, optimal 2.67; sds of one episode: random 23.43, hand-drawn 10.96, optimal 10.65
Owner:  researcher's check 5; the hand-drawn per-cell γ = 1 values match Fig. 6 of environments-and-the-rl-problem (their mean is 32.93 / 14 = 2.35)
Scope:  no time limit; under TimeLimit 200 the random value moves negligibly (lesson 8: no random episode was cut at 200 moves in 4,000)
```

```text
Figure: Henderson et al. Fig. 5: two sets of 5 seeds, same hyperparameters, TRPO on HalfCheetah-v1; t = −9.0916, p = 0.0016
Owner:  Henderson et al. 2018, arXiv v3 p. 5
Scope:  10 trials, average 2-sample t-test across the training distribution
```

```text
Figure: Machado et al. benchmark protocol: mean of the last 100 training episodes before 10, 50, 100 and 200 million frames; 5 trials (DQN), 24 trials (Sarsa(λ) + Blob-PROST)
Owner:  Machado et al. 2018, §6.1
Scope:  60 Atari games, sticky actions ς = 0.25
```

```text
Figure: feasibility timing: 38-49 s per 50,000-timestep run (DQN or PPO, one torch thread, Xeon 2.80 GHz)
Owner:  researcher's check 6 (stand-in env)
Scope:  one seed per run; the writer's machine and env will differ
```

## Limits

- The supporting course files were not opened: `mc_control.py`, `estimators.py`, `control.py` and `td_control.py`, from action-values-from-samples, learning-values-from-samples, finding-optimal-policies and sarsa-and-q-learning. The brief allowed `nb history --show` for three lessons only. Their names are known only from imports and uses: `mc_control.step(cell, action, rng)` returns `(reward, cell)`, and the module also holds `mc_control.LIVE`, `mc_control.SLIP` and `CAP = 200`. Elsewhere: `estimators.GAMMA = 0.9`, `control.value_iteration(1e-12)[0]` is v*, and `control.action_values(v, P)` is q*. The writer must confirm the signatures and print the folder list. Running `baselines.py` and `grid_env.py` needs at least gridworld.py, estimators.py, mc_control.py, grid_env.py and baselines.py. The optimal solve also needs control.py, and whatever control.py imports.
- The published URLs of the three earlier lessons were not recorded. `nb history` gives titles, dates and text, not addresses.
- No maintainer statement names Gymnasium 1.4.0. Support rests on the declared range `<2.0` and on check 1. The last explicit statement is "gymnasium 1.3.0 support" in 2.9.0.
- The install was tested on Linux x86_64 only: Python 3.10 and 3.13 with the default index, and the CPU-index variant on 3.10. Python 3.11, 3.12 and 3.14, macOS and Windows were not tested.
- The numbers a reader prints from an SB3 run may differ from the page's. SB3 does not guarantee reproducibility across torch releases or platforms, and an unpinned torch resolves to 2.14.1 or 2.15.0 depending on the Python version. Pinning `torch==2.14.1` gives one torch version on Python 3.10 to 3.14 (wheels exist for cp310-cp314), but it does not make CPU and CUDA builds agree.
- The optimal mean value 1.6089 and every γ = 1 and sd figure are the researcher's computations from the printed gridworld.py, not printed course output. The lesson's script must print whichever of them the page uses.
- The feasibility runs (check 6) used a stand-in SlipperyGrid, two seeds and one budget. They establish nothing about which algorithm learns the grid reliably, and the writer's runs must replace them.
- The AAAI page range for Henderson et al. and the JAIR page numbers for Machado et al. were not confirmed. The locators are arXiv pages and section titles.
- Not read: Empirical Design in Reinforcement Learning (Patterson et al., arXiv 2304.01315), which SB3's RL Tips recommends, and rliable. Interval estimates belong to stage 4, so the lesson does not need them.
- The record does not establish why SB3's training curve "underestimates" the agent on this grid. SB3 states it, and the gap's size and cause are the writer's experiment.

## Source assets

```text
Asset: Henderson et al. 2018, Fig. 5, "HalfCheetah-v1 (TRPO, Different Random Seeds)", arXiv v3 p. 5, top of the left column: two learning curves (blue and orange), both labelled "Random Average (5 runs)", with shaded bands; y-axis "Average Return" (0 to 5000), x-axis "Timesteps" (0 to 2.00 × 10^6). The paper states that all its graphs show mean and standard error across seeds (Experimental Analysis, p. 2).
Shows: one algorithm and one configuration, split only by seed, giving two curves whose bands separate from early in training and end roughly 1,000 to 1,500 apart (read off the plot, not printed).
Crop:  keep both curves, the legend, both axes with their labels and the caption with t = −9.0916, p = 0.0016; omit the neighbouring Fig. 4 panels.
```

```text
Asset: Machado et al. 2018, Fig. 1, arXiv v2 p. 9 (§4.1): learning curves in Centipede, (a) Sarsa(λ) + Blob-PROST and (b) DQN; grey curves are individual trials and the red curve is their average; each point averages the last one million episodes.
Shows: individual runs beside their mean. In (a) the score climbs for most of training and then collapses near 150M timesteps; in (b) it peaks early, drops and recovers partly. Reporting the best policy would hide both.
Crop:  keep both panels and their caption, which says the y-axes differ in scale; the panels must not be shown on a shared axis.
```

```text
Asset: SB3 documentation and source.
Shows: None found. The evaluation, callback, Monitor and RL Tips pages carry no figure that bears on evaluation; the code lines themselves are the evidence.
Crop:  n/a
```

```text
Asset: termination-and-truncation Fig. 2 (heatmaps of each cell's largest estimate beside the exact v*) and checking-a-custom-environment Fig. 3 (each baseline's mean return minus its exact value with ±3 standard-error bars).
Shows: the course's own visual vocabulary for "learned values against v*" and "mean against exact value with its noise"; the series asks for the lesson's own runs as inline SVG, so these are formats to reuse, not images to capture.
Crop:  n/a
```

## Discarded

```text
https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/quickstart.html: adds only predict(obs, deterministic=True) in a loop, which the module pages and source already establish.
https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/vec_envs.html (beyond #vecenv-api-vs-gym-api): SubprocVecEnv, VecNormalize and the other wrappers are stage 5 material the lesson must not teach.
https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/rl_tips.html#tips-and-tricks-when-implementing-an-rl-algorithm: about writing an algorithm, not using one.
Gymnasium FrozenLake-v1 (used only as a built-in env for the two-line install call): not a source for the lesson; the lesson's case is SlipperyGrid.
```
