# Evidence: reinforcement-learning/action-frequency (researcher 01)

The derivation the commission asks for is in the paper it names. Tallec, Blier and Ollivier (ICML 2019, PMLR §3.2, Theorem 2, eqs. 11–18) prove Q^π_δt(s,a) = V^π_δt(s) + O(δt) for a deterministic system ds/dt = F(s,a), held for δt per step, with reward r·δt per step and discount γ^δt per step. Their supplement (Theorem 2, eqs. 37–39) gives the first-order term, A^π(s,a) = r(s,a) + ∂_sV^π(s)·F(s,a) + ln γ·V^π(s), so the gap between two actions is δt times a difference that does not vanish. The paper credits the observation to Baird (1994). I could not open Baird's paper, but his group's NIPS 1994 paper reports Q-learning failing as the time step shrinks. DQN's k = 4 and its stated reason, which was computation, are confirmed in the Nature Methods and Extended Data Table 1. Current Gymnasium (1.4.0, 5 Oct 2026) and ALE (ale-py 0.12.1) behaviour is confirmed from documentation and from the released code. Gymnasium 1.3.0 added a general `RepeatAction` wrapper. Four primaries document action repeat as a tuned choice whose best value differs by task, and three of them show that too much repeat destroys control. The evidence is thin or breaks the angle in five places. (1) The commission's "noise in a sampled target does not shrink with dt" is not what the sources say. Tallec et al. place the failure in approximation error that does not scale with δt. In stochastic systems they put the variance of δQ/δt at O(1/δt), so the TD error's spread shrinks as √δt, more slowly than the O(δt) gap. (2) No source runs tabular Q-learning on a gridded continuous-time task across δt, so the lesson's runs will be the only evidence for that case. (3) Action repeat also restores exploration, since ε-greedy dithering averages out as δt → 0 (Tallec Theorem 4), and it shortens the horizon in decisions (Kalyanakrishnan et al. Theorem 6). Attributing run 2 to the action gap therefore needs a removal test. (4) The O(δt) result assumes a smooth value function, and at a value discontinuity the gap stays finite (Tallec §6). (5) Gymnasium's `MaxAndSkipObservation` returns the elementwise maximum of the last two observations, which is wrong for a position-and-speed state vector.

## Sources

### S1. Tallec, Blier and Ollivier, "Making Deep Q-learning Methods Robust to Time Discretization" (ICML 2019)

- URL: https://proceedings.mlr.press/v97/tallec19a.html (main PDF https://proceedings.mlr.press/v97/tallec19a/tallec19a.pdf; supplementary https://proceedings.mlr.press/v97/tallec19a/tallec19a-supp.pdf). The arXiv version is https://arxiv.org/abs/1901.09732 (v2, 29 Jan 2019). Its equation numbers run one higher than PMLR's, and its appendix theorem numbers differ (arXiv Theorem 7 is PMLR supplement Theorem 2). Cite the PMLR numbering.
- Authors as printed: Corentin Tallec (TAckling the Underspecified, Université Paris Sud), Léonard Blier (Université Paris Sud and Facebook Artificial Intelligence Research), Yann Ollivier (Facebook Artificial Intelligence Research). Proceedings of the 36th ICML, PMLR 97:6096–6104.
- Kind: primary. The authors own the theorems and proofs, and they ran the experiments they report. For the claim that Baird first identified the collapse it is secondary, a repetition of Baird's priority (see S3, S4).
- Establishes firsthand:
  - The near-continuous MDP M_δt holds each action for δt. Its transition is "the state obtained when starting at s0 = s and maintaining at = a constant for a time δt". Reward per step is δt·r and discount per step is γ^δt, where γ is the discount per unit of physical time (§3.1, eq. 4).
  - The horizon in physical time is δt/(1−γ^δt) = −1/ln γ + O(δt), which stays fixed as δt → 0. A per-step discount held constant gives a physical horizon of about δt/(1−γ_δt), which goes to 0, and the agent becomes "increasingly short-sighted" (§3.1, eq. 5).
  - Theorem 2 states Q^π_δt(s,a) = V^π_δt(s) + O(δt) for every (s,a). The proof starts from the Bellman equation Q = rδt + γ^δt E[V(s′)] (eq. 12) and s′ = s + F(s,a)δt + o(δt) (eq. 13). Assuming V^π_δt is continuously differentiable with uniformly bounded derivatives, V(s′) = V(s) + ∇V·Fδt + o(δt) = V(s) + O(δt) (eqs. 14–15). Substitution gives Q = O(δt) + (1+O(δt))(V+O(δt)) = V + O(δt) (eqs. 16–18). In exact continuous time Q^π = V^π, "There is no continuous-time Q-learning" (§3.2).
  - With δt small but nonzero, Q still depends on the action. When Q is approximated, an approximation error much larger than O(δt) decides the ranking of actions (§4.1).
  - The rescaled advantage A_δt = (Q−V)/δt (eq. 19) has a nondegenerate limit (Theorem 3). The supplement's Theorem 2 adds the assumption of a bounded Hessian and gives A^π_δt = r + ln γ·V + ∂_sV·F + O(δt) (supp. eq. 38), with limit A^π(s,a) = r(s,a) + ∂_sV^π(s)F(s,a) + log γ·V^π(s) (supp. eqs. 34, 39).
  - Theorem 4 (§4.2; proof in supp. Theorem 5): an agent mixing a deterministic policy with random actions at probability ε each step follows, as δt → 0, the deterministic ODE ds/dt = (1−ε)F(s,π(s)) + ε·E_noise F(s,a). ε-greedy exploration "is likely not to explore".
  - Theorem 5 (§4.4): for the parameter updates of their algorithm to have a continuous-time limit, learning rates must scale as δt^β with β = 1. With β > 1 the parameters do not move, and with β < 1 they can diverge in arbitrarily small physical time.
  - Experiments (§5; supp. §2): the DQN and DDPG baselines use the scaled discount γ^δt. One variant leaves the other hyperparameters fixed and the other rescales them. Physical γ = 0.8, five runs, and time on the x-axis is physical time, not steps. DDPG degrades as δt decreases on Ant and Cheetah. "On Cartpole, noise dominates, making interpretation difficult." Cartpole is the paper's only discrete-action environment (supp. §2.2 marks it "(D)").
  - Discussion (§6): the proofs assume V^π is continuously differentiable, which "is not always satisfied in practice". In pendulum swing-up the optimal value function is discontinuous where oscillation becomes necessary, which "results in non-infinitesimal advantages for actions on the boundary", and the analysis "only holds almost-everywhere". In deterministic environments the gradients are O(1) in δt. In stochastic ones, "variance of δQδt/δt and of the gradients typically scales as O(1/δt)".
  - The paper does not test action repeat or frame skip. Its remedy is advantage updating.
- Paraphrase: holding an action for δt changes the value of a state by only O(δt), so Q-values of different actions in one state differ by O(δt) while the value itself stays O(1). Scaling the discount as γ^δt keeps the horizon fixed in seconds but does not remove the collapse.
- Locators: PMLR p. 6096 (§1, intuition paragraph); p. 6097 (§2, Baird credit); p. 6098 (§3.1, eqs. 3–5); p. 6099 (§3.2, Theorem 2, eqs. 11–18; §4.1, eq. 19, Theorem 3); p. 6100 (§4.2, Theorem 4); p. 6101 (§4.4, Theorem 5; §5 begins); p. 6102 (§5 Cartpole sentence; Figure 1); p. 6102–6103 (§6 Discussion, "Smoothness of the value function" and "Near-continuous reinforcement learning and RMSProp"; Figure 2). Supplement: §1 Theorem 2 with eqs. 34–39 and its stated assumptions; §1 Theorem 5 (ε-greedy proof, eqs. 62–64); §2.2 hyperparameters (physical γ 0.8; Cartpole δt range [0.01, 0.005, 0.002, 0.001, 0.0005]).
- Quote (the theorem is the evidence): "Theorem 2. Under suitable smoothness assumptions, The action-value function of a near-continuous MDP is related to its value function via Qπδt(s, a) = Vδtπ(s) + O(δt) when δt → 0, for every (s, a)."
- Quote (where the failure comes from): "However, when approximating Qπδt, if the approximation error is much larger than O(δt), this error dominates, the ranking of actions given by the approximated Qπδt is likely to be erroneous." (§4.1)
- Quote (discount scaling does not save Q): "(This occurs even with a suitably adjusted decay factor γ.)" (§1)
- Quote (exploration): "Intuitively, with very small δt, changing the action at random every δt time step just averages out the randomness due to the law of large numbers." (§4.2)
- Notation for the writer: Tallec's γ is per unit time. The commission's γ = e^{−dt/τ} is the same thing with τ = −1/ln γ, which is Doya's time constant (S5). Tallec's physical γ = 0.8 corresponds to τ ≈ 4.48 time units (my arithmetic).

### S2. Tallec et al. as the source of a derived gap formula (researcher's arithmetic, flagged)

- URL: as S1, supplement Theorem 2, eq. 39.
- Kind: researcher's derivation from a primary. Nothing in the paper states it in this form.
- Establishes: subtracting eq. 39 for two actions a1, a2 gives Q(s,a1) − Q(s,a2) ≈ δt·[r(s,a1) − r(s,a2) + ∂_sV(s)·(F(s,a1) − F(s,a2))]. For a point mass whose action sets the acceleration to ±u, with a reward rate that does not depend on the action, the bracket is 2u·∂V/∂v, so the gap is about 2u·dt·∂V/∂v. With action repeat k, the same expansion on M_{k·dt} gives a gap of order k·dt, as long as k·dt stays small against the time over which ∂V/∂v changes. The writer can check this against the measured gaps in run 1.
- Paraphrase: the gap is linear in dt, with a slope set by how strongly the value depends on the coordinate the action pushes.
- Locators: supp. §1, Theorem 2, eqs. 37–39 and the assumptions stated above it (V^π and V^π_δt continuously differentiable, with gradient and Hessian uniformly bounded in s and δt).

### S3. Harmon, Baird and Klopf, "Advantage Updating Applied to a Differential Game" (NIPS 7, 1994)

- URL: https://proceedings.neurips.cc/paper_files/paper/1994/hash/2a9d121cd9c3a1832bb6d2cc6bd7a8a7-Abstract.html (PDF https://papers.neurips.cc/paper_files/paper/1994/file/2a9d121cd9c3a1832bb6d2cc6bd7a8a7-Paper.pdf)
- Authors as printed: Mance E. Harmon (Wright Laboratory), Leemon C. Baird III (Wright Laboratory; the footnote gives the U.S.A.F. Academy address), A. Harry Klopf (Wright Laboratory). Advances in Neural Information Processing Systems 7, pp. 353–360.
- Kind: primary. The authors ran the comparison and report their own results. It is the earliest accessible paper from Baird's group to show the effect.
- Establishes firsthand: on a linear-quadratic missile-and-plane differential game with a quadratic function approximator, the error of non-residual Q-learning after 40,000 steps grows as the time step falls from 0.05 to 0.00005. Residual-gradient advantage updating stays accurate at every step size. "For small time steps, nonresidual-gradient Q-learning performed so poorly that the error was lower for a learning rate of zero (no learning) than it was for a learning rate of 10^-8." Advantage updating defines the advantage with a 1/Δt factor so that "for small time step duration Δt, the advantages will not all go to zero."
- Paraphrase: Q-learning's policy error rises as the time step shrinks, and an algorithm that rescales the advantage by 1/Δt is unaffected.
- Locators: Abstract (p. 353); §1, the sentence after eq. 1 (p. 354); §4.2.1, Experiment Set 1, Figure 2 and Table 1 (pp. 358–359); §4.2.2, Figure 3; §5 Conclusion (p. 359).
- Quote: "The results also show advantage updating converges regardless of the time step duration; Q-learning is unable to converge as the time step duration grows small." (Abstract)
- Caveat: Figure 2 holds the number of steps at 40,000, not the simulated time, so the smallest step covers 1/1,000 of the simulated time of the largest (my arithmetic: 40,000 × 0.05 = 2,000 time units against 40,000 × 0.00005 = 2). Q-learning's learning rate was tuned per step size (Table 1: 0.02, 0.06, 0.2, 0.4).

### S4. Baird, "Reinforcement learning in continuous time: advantage updating" (ICNN 1994), not opened

- URL: https://doi.org/10.1109/ICNN.1994.374604 (IEEE Xplore, gated). Crossref metadata: L. C. Baird, Proceedings of 1994 IEEE International Conference on Neural Networks (ICNN'94), vol. 4, pp. 2448–2453.
- Kind: primary for the priority claim. I did not read it.
- Establishes: nothing firsthand in this record. Tallec et al. (S1 §2) credit it with identifying "the collapse of Q-learning for small time steps" and note that "testing was only done on a quadratic-linear problem". Baird's 1993 technical report (DTIC ADA280862) returned 403 to every request, including WebFetch.
- Locators: none read.

### S5. Doya, "Reinforcement Learning in Continuous Time and Space" (Neural Computation 2000)

- URL: https://doi.org/10.1162/089976600300015961 (MIT Press, which returned 403 to automated requests). I read the author's manuscript as distributed in a Hebrew University course handout, https://www.cs.huji.ac.il/course/2009/control/handouts/Doya2000.pdf, whose header reads "Neural Computation, 12(1), 219-245 (2000)". Cite the DOI.
- Author as printed: Kenji Doya, ATR Human Information Processing Research Laboratories, Kyoto.
- Kind: primary. Doya defines the formulation the commission's τ comes from, and S1 cites it for the continuous-time return.
- Establishes firsthand: the value is V^μ(x(t)) = ∫_t^∞ e^{−(s−t)/τ} r(x(s),u(s)) ds, with "τ ... the time constant for discounting future rewards" (eq. 4). The Euler-discretized TD error equals the usual δ_t = r_t + γV_t − V_{t−1} "by taking the discount factor γ = 1 − Δt/τ ≃ e^{−Δt/τ} and rescaling the values as V_t = (1/Δt)V(t)". The Euler step Δt "does not have to be equal to the control cycle of the physical system".
- Paraphrase: the discount per step that keeps the time constant τ fixed is e^{−Δt/τ}, about 1 − Δt/τ.
- Locators: §2, eq. 4 (manuscript p. 4); §3.2 "Backward Euler Differentiation: Residual Gradient and TD(0)", the paragraph after eq. 15 (manuscript p. 8).

### S6. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed. (MIT Press, 2018)

- URL: http://incompleteideas.net/book/the-book-2nd.html (PDF http://incompleteideas.net/book/RLbook2020.pdf)
- Kind: primary. It is the standard text, and the authors own the statements.
- Establishes firsthand: the discounted return G_t = Σ γ^k R_{t+k+1} (eq. 3.8). With a constant reward of +1 the return is Σ γ^k = 1/(1−γ) (eq. 3.10), the basis for reading 1/(1−γ) as a horizon in steps. §17.2 "Temporal Abstraction via Options" (p. 461) is the pointer for semi-MDPs and options. Its bibliographical remarks credit options to Sutton, Precup and Singh (1999), "building on ... classical work on Semi-MDPs".
- Paraphrase: a per-step discount γ weights roughly 1/(1−γ) steps.
- Locators: §3.3 "Returns and Episodes", eqs. 3.8 and 3.10, p. 55; §17.2, p. 461; Bibliographical and Historical Remarks for 17.2.

### S7. Mnih et al., "Human-level control through deep reinforcement learning" (Nature 518, 2015)

- URL: https://www.nature.com/articles/nature14236 (doi:10.1038/nature14236; paywalled, so the Methods text is not visible on the page). I read the publisher PDF hosted by DeepMind at https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf.
- Authors: Volodymyr Mnih, Koray Kavukcuoglu, David Silver and 16 others. Affiliation as printed: Google DeepMind, London.
- Kind: primary. It is DQN's own specification of its setting.
- Establishes firsthand: DQN acts on every kth frame and repeats its last action on the skipped frames, with k = 4 for all games. The stated reason is computation: emulating a frame is far cheaper than choosing an action, so the agent plays about k times more games in the same runtime. Extended Data Table 1 lists "action repeat 4" separately from "agent history length 4" (frame stacking) and "update frequency 4". The discount is 0.99 per agent step, "c was set to 0.99 throughout". The emulator runs at 60 Hz. The random-agent baseline acts at 10 Hz, every sixth frame, because 10 Hz is about the fastest a human can press 'fire'. The hyperparameters came from "an informal search on the games Pong, Breakout, Seaquest, Space Invaders and Beam Rider", with no systematic grid search.
- Paraphrase: DQN's k = 4 was a computational economy fixed across games, not a value derived from the dynamics.
- Locators: Methods, "Training details", second-to-last paragraph (frame-skipping); Methods, "Evaluation procedure" (10 Hz random agent); Methods, "Algorithm" (γ per time-step); Extended Data Table 1 (p. 10 of the DeepMind PDF), rows "action repeat", "agent history length", "update frequency", "discount factor".
- Quote: "Following previous approaches to playing Atari 2600 games, we also use a simple frame-skipping technique. More precisely, the agent sees and selects actions on every kth frame instead of every frame, and its last action is repeated on skipped frames. Because running the emulator forward for one step requires much less computation than having the agent select an action, this technique allows the agent to play roughly k times more games without significantly increasing the runtime. We use k = 4 for all games." (The citation marker after "technique" is to Bellemare, Veness and Bowling, AAAI 2012.)
- Quote (Extended Data Table 1): "action repeat | 4 | Repeat each action selected by the agent this many times. Using a value of 4 results in the agent seeing only every 4th input frame."

### S8. Mnih et al., "Playing Atari with Deep Reinforcement Learning" (arXiv 1312.5602, 2013)

- URL: https://arxiv.org/abs/1312.5602
- Kind: primary. It is the authors' earlier specification of their own setting.
- Establishes firsthand: the same frame-skipping technique with k = 4, except k = 3 for Space Invaders.
- Locators: §5 "Experiments", paragraph on frame-skipping.
- Quote: "We use k = 4 for all games except Space Invaders where we noticed that using k = 4 makes the lasers invisible because of the period at which they blink. We used k = 3 to make the lasers visible and this change was the only difference in hyperparameter values between any of the games."

### S9. Gymnasium 1.4.0: `RepeatAction` (documentation and released code)

- URL: https://gymnasium.farama.org/v1.4.0/api/wrappers/action_wrappers/ (class `gymnasium.wrappers.RepeatAction`). Release page https://pypi.org/project/gymnasium/1.4.0/ (uploaded 2026-10-05, the latest release on PyPI on 15 Nov 2026). I read the code in the released wheel, `gymnasium/wrappers/stateful_action.py`. GitHub was not reachable from this session.
- Kind: primary. The Farama Foundation's documentation and code define the library's behaviour.
- Establishes firsthand: `RepeatAction(env, num_repeats)` has no default for `num_repeats` and requires it to be ≥ 1. It runs the action `num_repeats` times, adds the rewards without discounting (`total_reward += float(reward)`), returns the last observation and info, and stops early on termination or truncation. It was added in v1.3.0, released 2026-04-22. The class docstring calls it `ActionRepeat` in one sentence, which is a naming slip; the class is `RepeatAction`. `gym.make` applies `TimeLimit` inside the environment it returns (registration.py, lines 814–816), so a `RepeatAction` wrapped around it counts the time limit in base steps.
- Paraphrase: Gymnasium now ships a deterministic action repeat for any environment. It sums rewards and keeps the last observation.
- Locators: Action Wrappers page, `RepeatAction` entry, including "Change logs: v1.3.0 - Initially added". Wrapper table page https://gymnasium.farama.org/v1.4.0/api/wrappers/table/: "Repeats an action N times, returning the cumulative reward and last observation / info."
- Quote: "By repeating actions, the effective decision frequency is reduced, which can speed up training and make exploration more efficient."

### S10. Gymnasium 1.4.0: `AtariPreprocessing` and `MaxAndSkipObservation`

- URL: https://gymnasium.farama.org/v1.4.0/api/wrappers/misc_wrappers/ (`AtariPreprocessing`); https://gymnasium.farama.org/v1.4.0/api/wrappers/observation_wrappers/ (`MaxAndSkipObservation`). Code read in the 1.4.0 wheel (`wrappers/atari_preprocessing.py`, `wrappers/stateful_observation.py`).
- Kind: primary, for the same reason as S9.
- Establishes firsthand:
  - `AtariPreprocessing(env, noop_max=30, frame_skip=4, ...)` "follows the guidelines in Machado et al. (2018)". It repeats the action `frame_skip` times, sums the rewards without discounting, and max-pools the last two frames. Its docstring lists "Frame skipping: The number of frames skipped between steps, 4 by default." It raises `ValueError` unless the base environment's own frameskip is 1 ("Disable frame-skipping in the original env. Otherwise, more than one frame-skip will happen as through this wrapper"). The documented example builds `gym.make("ALE/Pong-v5", frameskip=1)` first.
  - `MaxAndSkipObservation(env, skip=4)` requires skip ≥ 2. It repeats the action, sums the reward, and returns `np.max` over the last two observations. Its documented example applies it to CartPole-v1 and checks that the wrapped observation equals the elementwise max of obs3 and obs4. The wrapper is "based on the wrapper from stable-baselines3".
- Paraphrase: the Atari path makes the base environment act every frame and puts the repeat in a wrapper. The generic skip wrapper is built for flickering images.
- Locators: `AtariPreprocessing` docstring and Raises section; `step` loop in the code. `MaxAndSkipObservation` docstring, example and `step`.

### S11. Gymnasium 1.4.0: time steps built into stock environments

- URL: https://gymnasium.farama.org/v1.4.0/environments/mujoco/half_cheetah/ ; https://gymnasium.farama.org/v1.4.0/environments/classic_control/acrobot/ . Code checked in the 1.4.0 wheel (`envs/mujoco/mujoco_env.py`, `envs/classic_control/cartpole.py`, `pendulum.py`, `acrobot.py`, `envs/__init__.py`).
- Kind: primary, for the same reason as S9.
- Establishes firsthand: MuJoCo environments define `dt = model.opt.timestep * frame_skip`. For HalfCheetah-v5, frame_skip defaults to 5 and the frame time is 0.01, "so the default is dt = 5 × 0.01 = 0.05". Acrobot-v1 integrates with RK4 at dt = 0.2, and its page, under "Integration timestep", shows changing it with `env.unwrapped.dt = 0.05`. Acrobot-v1 truncates at 500 steps (`max_episode_steps=500`) and gives −1 per step, both counted in steps. CartPole uses `self.tau = 0.02  # seconds between state updates`. Pendulum uses `self.dt = 0.05`.
- Paraphrase: Gymnasium environments fix their own control interval. Where one can be changed, the step-counted time limit and per-step reward do not change with it.
- Locators: HalfCheetah page, Rewards section and Version History ("Added frame_skip argument, used to configure the dt"); Acrobot page, "Integration timestep" and Episode End ("Episode length is greater than 500").

### S12. Arcade Learning Environment documentation and ale-py 0.12.1 code

- URL: https://ale.farama.org/v0.12.1/environments/ ; release https://pypi.org/project/ale-py/0.12.1/ (uploaded 2026-08-16, the latest on PyPI on 15 Nov 2026). Code read in the released wheel (`ale_py/registration.py`, `ale_py/env.py`).
- Kind: primary, the Farama Foundation's own documentation and code for ALE.
- Establishes firsthand: `ALE/{Game}-v5` is registered with `frameskip=4`, `repeat_action_probability=0.25` and `max_num_frames_per_episode=108_000`. A code comment reads "108k frames which is 30 mins of gameplay ... 108k / 4 = 27,000 steps". `{Game}NoFrameskip-v4` has frameskip 1 and sticky-action probability 0.0. `AtariEnv.step` repeats the action `frameskip` times and sums the rewards. An integer frameskip is deterministic. A tuple (low, high) draws the count uniformly from [low, high) at each step. The docs list both frame-skipping and sticky actions under "Stochasticity", and the `AtariEnv` docstring says its defaults "are taken from Machado et al., 2018".
- Paraphrase: the current default Atari environment repeats each action for four frames and, with probability 0.25, repeats the previous action instead of the new one.
- Locators: Environments page, "Stochasticity" and "Version History and Naming Schemes" tables; `registration.py` `register_v5_envs`; `env.py` `AtariEnv.__init__` docstring and `step`.
- Quote: "If frameskip is an integer, frame skipping is deterministic, and in each step the action is repeated frameskip many times."

### S13. Braylan, Hollenbeck, Meyerson and Miikkulainen, "Frame Skip Is a Powerful Parameter for Learning to Play Atari" (AAAI-15 Workshop)

- URL: https://cdn.aaai.org/ocs/ws/ws0098/10156-45978-1-PB.pdf (AAAI's own host). Published in "Learning for General Competency in Video Games: Papers from the 2015 AAAI Workshop", pp. 10–11.
- Authors as printed: Alex Braylan, Mark Hollenbeck, Elliot Meyerson and Risto Miikkulainen, Computer Science Department, The University of Texas at Austin.
- Kind: primary. The authors ran the experiment.
- Establishes firsthand: neuroevolution (Enforced SubPopulations, not value-based RL) on six Atari games at frame skips 0, 20, 60 and 180, averaged over five runs for 200 generations. Their frame skip counts frames skipped, so 0 means a new action every frame. The best frame skip differs by game. Seaquest scored best at 180 ("pausing for a full three seconds between decisions"). Space Invaders and Beam Rider scored best at 60. Pong and Breakout scored best at low frame skip, and "Breakout with frame skip 180 always scored 0". The authors argue that agents with a high frame skip "do not learn action selection for states that are skipped", and that longer decisions "lead to broader exploration of the behavior space".
- Paraphrase: the best decision interval spans two orders of magnitude across six games, and the longest interval tested fails completely on Breakout.
- Locators: p. 10, text; p. 11, Figure 1 and Table 1 (frame skip as subscript).
- Quote: "When action selection is computationally intensive, setting a higher frame skip can significantly decrease the time it takes to simulate an episode, at the cost of missing opportunities that only exist at a finer resolution."
- Caveat: Table 1 gives DQN's frame skip as subscript 2 for most games and 3 for Space Invaders. That is the reverse of what S8 implies (k = 4 skips 3 frames, k = 3 skips 2). The text says "DQN (Mnih et al. 2013) uses a frame skip of 2-3".

### S14. Lakshminarayanan, Sharma and Ravindran, "Dynamic Action Repetition for Deep Reinforcement Learning" (AAAI 2017)

- URL: https://ojs.aaai.org/index.php/AAAI/article/view/10918 (behind a bot check that returned a challenge page to curl and WebFetch). I read the PDF on AAAI's CDN, https://cdn.aaai.org/ojs/10918/10918-13-14446-1-2-20201228.pdf. DOI 10.1609/aaai.v31i1.10918; Proceedings of AAAI-17, pp. 2133–2139.
- Authors as printed: Aravind S. Lakshminarayanan, Sahil Sharma and Balaraman Ravindran, Indian Institute of Technology, Madras.
- Kind: primary. The authors ran the experiments.
- Establishes firsthand: they call the repeat count the action repetition rate (ARR). A DQN with a doubled action set chooses each action at repeat 4 or repeat 20, with the same two rates for every game. On Seaquest, DQN at a static ARR of 20 scored 1,707 against 5,450 at ARR 4, and the dynamic choice scored 10,458. On Enduro the scores were 124 (ARR 20), 707 (ARR 4) and 1,002 (dynamic). The dynamic agent chose the longer action 67.84–78.87% of the time. Scores are the best testing epoch, and no seed count or interval is reported. An A3C variant shows gains on all five games tested.
- Paraphrase: repeating 20 frames everywhere hurts DQN badly on two games, while letting the agent choose between 4 and 20 helps.
- Locators: §"Experimental Setup and Results", Table 1 and Table 2 (p. 2137); Table 3 and Figure 2 (p. 2138).
- Quote: "To strengthen our claim that there is a need for dynamic action repetition, we show results on two of the games (Seaquest and Enduro) in which the DQN operates with just the higher but static ARR of 20. Not surprisingly, it scores poorly during gameplay."

### S15. Metelli, Mazzolini, Bisi, Sabbioni and Restelli, "Control Frequency Adaptation via Action Persistence in Batch Reinforcement Learning" (ICML 2020)

- URL: https://proceedings.mlr.press/v119/metelli20a.html (PMLR 119:6862–6873)
- Authors as printed: Politecnico di Milano; Bisi, Sabbioni and Restelli also at the Institute for Scientific Interchange Foundation, Turin.
- Kind: primary for its own theorems and Table 1. Its introduction's statement about indistinguishable actions is secondary, a repetition of S1, and should be cited as such.
- Establishes firsthand: in the k-persistent MDP M_k, the loss from persistence ‖Q* − Q*_k‖ increases with k (Theorem 4.1). The estimation term of Persistent Fitted Q-Iteration decreases with k (§5.1). Table 1 reports 20 runs of PFQI with extra-trees, trained on data collected at persistence 1. On Cartpole the mean returns are k=1 169.9 ± 5.8, k=2 176.5 ± 5.0, k=4 239.5 ± 4.4, k=8 10.0 ± 0.0, and k=16, 32 and 64 9.8 ± 0.0. The authors note that "persistence 1 rarely leads to the best performance" and that "excessively increasing persistence prevents the control at all".
- Paraphrase: control frequency trades a larger policy space at high frequency against lower sample complexity at low frequency, and the best persistence is intermediate and differs by task.
- Locators: §1, paragraphs 2–3 (p. 6862); §4, Theorem 4.1 (p. 6865); §5.1 (trade-off decomposition); §8 and Table 1 (p. 6869); Figure 2 (p. 6870).
- Quote (secondary, citing S1): "When increasing the control frequency, the advantage of individual actions becomes infinitesimal, making them almost indistinguishable for standard value-based RL approaches (Tallec et al., 2019). As a consequence, the sample complexity increases. Instead, low frequencies allow the environment to evolve longer, making the effect of individual actions more easily detectable."

### S16. Kalyanakrishnan et al., "An Analysis of Frame-skipping in Reinforcement Learning" (arXiv 2102.03718, 2021)

- URL: https://arxiv.org/abs/2102.03718 (v1, 7 Feb 2021). I found no peer-reviewed venue. The Semantic Scholar lookup was rate-limited, so treat it as a preprint.
- Authors as printed: Shivaram Kalyanakrishnan (IIT Bombay), with Siddharth Aravindan, Vishwajeet Bagdawat, Varun Bhatt, Harshith Goka, Archit Gupta, Kalpesh Krishna and Vihari Piratla.
- Kind: primary for its theorems and experiments.
- Establishes firsthand:
  - With frame-skip d, the induced MDP M_d has reward R_d = R + γTR + … + γ^{d−1}T^{d−1}R and discount γ^d (§3), so rewards inside the repeat are discounted.
  - The "price of inertia" Δ_M = max over (s,a) of [Q*(s,a) − Q*(s,a²)] is the cost of one extra repetition (§5.1).
  - Theorem 6 bounds the loss of a greedy policy with frame-skip d by Δ_M·C1(γ,d) + γ^d/(1−γ^d)·C2(M, Q̂). The first term grows with d and the second falls "on account of the shortening horizon", so the bound is smallest at an intermediate d.
  - On Gym Acrobot (5 actions per second), Sarsa_d(λ) with tile coding was best at d = 3 after 8,000 episodes. "Sarsa_d(λ) with d up to 5 dominates Sarsa(λ)."
  - Reducing γ without repetition also helps: γ = 0.99 finishes in 95.6 steps, 11.8 steps better than regular Sarsa(λ). The setting γ = 1, d = 5 does better still, and the best combination is d = 3, γ = 0.999.
  - Its literature survey credits McGovern et al. with two benefits of action repetition, "improved exploration" and "the shorter resulting task horizon".
- Paraphrase: action repeat shortens the horizon in decisions and so reduces the cost of value-estimation error, at a price set by how much one extra repetition can cost.
- Locators: Abstract; §2 Literature survey; §3.2 (definition of M_d); §5.1, price of inertia (p. 4); Lemma 5 and Theorem 6 with the paragraph that follows (p. 5); Figure 2 (p. 5); §6.1 Acrobot and "Frame-skipping versus reducing discount factor" (p. 7); Figure 3 (p. 7).
- Quote: "We show that this loss may be offset by the gain brought to learning by a smaller task horizon." (Abstract)

### S17. Bellemare, Ostrovski, Guez, Thomas and Munos, "Increasing the Action Gap: New Operators for Reinforcement Learning" (AAAI 2016)

- URL: https://arxiv.org/abs/1512.04860 (Google DeepMind). arXiv's own citation line gives Proceedings of the AAAI Conference on Artificial Intelligence, 2016. I did not try the AAAI page.
- Kind: primary for the definition it uses and for its bicycle-domain setup.
- Establishes firsthand: it defines the action gap as "the value difference between optimal and second best actions". It says that "Increasing the action gap is advantageous in the presence of approximation or estimation error (Farahmand 2011), and may be crucial for systems operating at a fine time scale such as video games". In the bicycle domain each time step is 0.01 s and episodes last 50,000 steps or more. On the 10-point grid used for the value function, "each grid cell covers an arc of 2π/10 = π/5, while a single time step typically changes ψ by less than π/1000", so most trajectories lie far from grid points. It also says the ALE setting resembles such continuous domains because "each individual action has little effect on the game".
- Paraphrase: the term "action gap" and its link to estimation error predate this lesson's sources, and a fine time step on a coarse grid makes one step move the state a small fraction of a cell.
- Locators: §1 Introduction (p. 1); "Experiments on the Bicycle Domain" (p. 4); "Persistent Advantage Learning" and "Experimental Results on Atari 2600" (p. 6).

### S18. Munos and Bourgine, "Reinforcement Learning for Continuous Stochastic Control Problems" (NIPS 10, 1997)

- URL: https://proceedings.neurips.cc/paper_files/paper/1997/hash/186a157b2992e7daed3677ce8e9fe40f-Abstract.html (pp. 1029–1035)
- Authors as printed: Rémi Munos (CEMAGREF, LISC, Antony) and Paul Bourgine (École Polytechnique, CREA, Palaiseau).
- Kind: primary. The authors own the scheme and its convergence theorem.
- Establishes firsthand: a convergent finite-difference scheme on a grid of spacing δ uses a state- and action-dependent time step τ(ξ,u) = δ²/Σ_i[δ|f_i(ξ,u)| + a_ii(ξ,u) − ½Σ_{j≠i}|a_ij(ξ,u)|] (eq. 5) and discounts by γ^{τ(ξ,u)} (eq. 4). With no noise (a = 0) this is τ = δ/Σ_i|f_i|, the time for the dynamics to cross one grid spacing (my reduction). The value function of the scheme converges to the true one as δ → 0 (Theorem 2).
- Paraphrase: when values live on a grid, the convergent scheme makes one decision per cell crossing, not one per fixed clock tick.
- Locators: §2, eqs. 4–6 and Theorem 2 (pp. 1031–1032).

### S19. Dabney, Ostrovski and Barreto, "Temporally-Extended ε-Greedy Exploration" (arXiv 2006.01782, 2020)

- URL: https://arxiv.org/abs/2006.01782 (v1, 2 Jun 2020; DeepMind). The ICLR 2021 publication was not verified.
- Kind: primary for the algorithm it defines.
- Establishes firsthand: εz-greedy acts greedily with probability 1−ε. With probability ε it picks a random action and repeats it for a duration n drawn from a distribution z (exponential, uniform or zeta); a duration of 1 recovers ε-greedy. Figure 1 compares first-visit times in an open gridworld with and without temporal persistence.
- Paraphrase: random actions can be repeated without repeating greedy ones, which separates exploration from the decision interval.
- Locators: Abstract; §4.2 "εz-Greedy" (pp. 5–6); Figure 1 (p. 3).
- Quote: "We propose a temporally extended form of ε-greedy that simply repeats the sampled action for a random duration." (Abstract)

### S20. The course record (`nb history`)

- URL: the published lessons `reinforcement-learning/sarsa-and-q-learning` (2026-11-05), `reinforcement-learning/frame-stacking-and-the-markov-property` (2026-11-14) and `reinforcement-learning/epsilon-greedy-exploration` (2026-11-04).
- Kind: primary. These are the paper's own published lessons.
- Establishes firsthand: sarsa-and-q-learning writes the update as Q(S_t,A_t) ← Q(S_t,A_t) + αδ_t with δ_t = R_{t+1} + γ max_a Q(S_{t+1},a) − Q(S_t,A_t) and q_* for optimal action values. Its step size is N(s,a)^{-0.7}. The frame-stacking lesson pins `gymnasium==1.4.0` in its script metadata and cites Mnih et al. 2015 (S7) for DQN's four-frame stack, which its Why-this-matters box mentions. No published lesson mentions frame skip, action repeat or Tallec (`nb history` searches for "frame skip", "action repeat" and "Tallec" returned nothing).
- Locators: `nb history --show reinforcement-learning/sarsa-and-q-learning` (section "The update rules differ in one term"); `nb history --show reinforcement-learning/frame-stacking-and-the-markov-property` (opening card; script headers; Sources).

## Contradictions

1. **Target noise (the commission against S1).** The commission says the noise in a sampled Q-learning target "does not shrink" with dt. S1 does not say that. In S1's deterministic setting the TD error is itself O(δt) (§4.4: "δQδt is of order O(δt), because s′ = s + O(δt)"). The failure comes from approximation error in the estimate that is "much larger than O(δt)" (§4.1). For stochastic systems S1 §6 puts the variance of δQ/δt at O(1/δt), so the spread of the TD error is O(√δt): it shrinks, but more slowly than the O(δt) gap, and the ratio of noise to gap grows as 1/√δt. A wording the sources support: the error in the estimate does not shrink in proportion to dt, and the gap does. My own arithmetic suggests that state aliasing in the writer's table of cells behaves like the stochastic case. With cell width w and speed v, a step leaves the cell with probability about |v|·dt/w, so the target's variance is about (|v|dt/w)·Δ², where Δ is the difference between neighbouring cells' values, and its spread is about √dt. This is unsourced. S17's bicycle-domain remark is sourced support for the geometry: one step moves the state a small fraction of a cell.

2. **Smooth value function.** S1's Theorem 2 assumes V^π_δt is continuously differentiable with bounded derivatives. S1 §6 reports that the assumption fails in pendulum swing-up, where V is discontinuous and the advantages at the boundary are non-infinitesimal. It also attributes DAU's weaker result on Half-Cheetah to value discontinuities. My reading of eqs. 14–15 is that a Lipschitz V is enough for the O(δt) order: a kink, as on the switching curve of a bang-bang controller for a point mass, still gives O(δt), while a jump does not. That reading is unsourced. For the writer this is the "case the explanation fits worst": cells at a value discontinuity or next to the goal boundary may show gaps that do not shrink.

3. **Policy value against optimal value.** S1's Theorem 2 is stated for a fixed deterministic policy π (Q^π, V^π). The commission states it for Q and V without a policy. Applying it to Q* needs a deterministic optimal policy and a smooth V*, and the optimal policy of M_δt itself depends on δt. The supplement's Theorem 3 (policy improvement through A) is the paper's bridge from Q^π to action choice.

4. **Exploration confound in run 2.** S1 Theorem 4: at fine δt, ε-greedy trajectories converge to a deterministic averaged ODE, so random actions stop moving the agent anywhere new. Action repeat makes each random action persist for k·dt and restores exploration (S13 and S16 §2 name improved exploration as a benefit; the S9 docstring says repeat can "make exploration more efficient"). An improvement from repeat in run 2 therefore does not by itself show that the action gap was the cause. S19's εz-greedy repeats only the random actions and gives a removal test for exploration. A complementary removal test is an exact solve (value iteration on the gridded model) that measures the gap without any exploration.

5. **Horizon as a competing explanation.** S16 attributes the benefit of repetition to the shorter horizon 1/(1−γ^d) (Theorem 6), and shows that lowering γ without repetition recovers part of the gain on Acrobot. In a near-continuous system with γ_dt = e^{−dt/τ}, both mechanisms scale the same way (my arithmetic): γ^k/(1−γ^k) ≈ τ/(k·dt), and the gap is about k·dt. The two are still separable in a run. Lowering the discount without repeating actions shortens the horizon in decisions but leaves the gap at O(dt).

6. **More repeat is not always better.** S13 (Breakout at frame skip 180 always scored 0), S14 (Seaquest falls from 5,450 to 1,707 and Enduro from 707 to 124 when ARR goes from 4 to 20) and S15 (Cartpole return collapses from 239.5 at k = 4 to 10.0 at k = 8) show that repeat has a cost, and that the best k is intermediate and depends on the task. This supports the commission's "at the cost of coarser control". S15 Theorem 4.1 and S16 Theorem 6 state that cost formally.

7. **DQN's reason for k = 4.** S7 gives computation as the reason ("play roughly k times more games without significantly increasing the runtime"), and S8 changed k to 3 on one game so the lasers stayed visible. Neither paper gives the action gap as a reason. The lesson can present k = 4 as classic practice but should not attribute the action-gap argument to DQN.

8. **Strength of the empirical collapse evidence.** S1's only discrete-action quantitative result (Cartpole) is inconclusive ("noise dominates"). Its clearest degradation with δt is for DDPG (Ant, Cheetah). S3 is a linear-quadratic game with a quadratic approximator, and its Figure 2 holds steps fixed, not simulated time (see S3 caveat). No source shows tabular Q-learning failing on a gridded continuous-time task.

9. **Grid resolution sets a natural time step.** S18's convergent grid scheme ties the decision interval to the cell-crossing time, δ/|f|. My inference is that a tabular agent at dt far below the cell-crossing time already holds one action per cell, because its policy is a table indexed by cell. Repeat therefore costs little control until k·dt approaches the crossing time, and a fine dt adds decisions the table cannot use. This could make run 2's "coarser control" cost invisible for small k. It is unsourced beyond S18's equation.

10. **Rewards inside the repeat.** S9, S10 and S12 add rewards over the repeated frames without discounting. S16's M_d and S1's M_{k·dt} discount inside the repeat, and S1 also scales reward by δt. The difference is O(k·dt/τ) per decision (my arithmetic). It matters only if the lesson claims exact equivalence between "repeat k at dt" and "step k·dt".

11. **`MaxAndSkipObservation` on a state vector.** S10's generic skip wrapper returns the elementwise maximum of the last two observations, which is correct for flickering Atari frames. On a position-and-speed observation the result is not a state the system was in. Its own CartPole example shows this. `RepeatAction` (S9) returns the last observation and is the wrapper to use.

12. **Frame-skip counting conventions.** S13 counts frames skipped (0 = act every frame). S7, S8, S10 and S12 count frames per action (1 = act every frame). S14 defines its rate as the number of times an action is repeated. S10's docstring says "frames skipped between steps" for `frame_skip=4`, but its code applies the action on 4 frames.

13. **ALE docs against ALE code.** The 0.12.1 docs say v0.11 cut registrations to "{rom_name}NoFrameskip-v4 ... and ALE/{rom_name}-v5", but the 0.12.1 `registration.py` still registers {Game}-v0 and -v4 with frameskip (2, 5), and NoFrameskip variants, for the legacy games. The docs and the code agree on the v5 settings (frameskip 4, sticky 0.25) and NoFrameskip-v4 (1, 0.0). Cite only those.

I found no source that contradicts the central derivation, Q − V = O(dt) for smooth V.

## Numbers

```text
Figure: Q^π_δt(s,a) − V^π_δt(s) = O(δt), for every (s,a)
Owner:  S1, PMLR §3.2 Theorem 2, eq. 11
Scope:  deterministic dynamics, fixed deterministic policy π, V^π_δt C¹ with bounded derivatives; δt → 0

Figure: A^π(s,a) = r(s,a) + ∂_sV^π(s)·F(s,a) + ln γ·V^π(s), the limit of (Q−V)/δt
Owner:  S1, supplement Theorem 2, eqs. 34 and 39
Scope:  adds a bounded-Hessian assumption; γ is the discount per unit time

Figure: physical horizon δt/(1−γ^δt) = −1/ln γ + O(δt)
Owner:  S1, §3.1 eq. 5
Scope:  per-step discount γ^δt

Figure: discount per step γ = 1 − Δt/τ ≃ e^{−Δt/τ}; τ is the discounting time constant
Owner:  S5, §3.2
Scope:  Euler discretization of the continuous-time TD error

Figure: return with constant reward +1 is 1/(1−γ)
Owner:  S6, eq. 3.10, p. 55
Scope:  discounted continuing return

Figure: physical γ = 0.8 per unit time in S1's experiments (τ ≈ 4.48 time units, my arithmetic)
Owner:  S1, supplement §2.1
Scope:  all S1 environments

Figure: S1 Cartpole δt values 0.01, 0.005, 0.002, 0.001, 0.0005; five runs per setting
Owner:  S1, supplement §2.2; main §5
Scope:  the paper's only discrete-action environment

Figure: DQN action repeat k = 4 frames; agent history length 4; update frequency 4; discount 0.99 per agent step
Owner:  S7, Methods "Training details" and Extended Data Table 1
Scope:  all 49 games; hyperparameters set by informal search on 5 games

Figure: DQN decision interval 4/60 s ≈ 0.067 s; horizon 1/(1−0.99) = 100 decisions ≈ 6.7 s
Owner:  derived from S7 (60 Hz, k = 4, γ = 0.99); my arithmetic
Scope:  DQN on ALE

Figure: DQN random-agent baseline at 10 Hz (every sixth frame)
Owner:  S7, Methods "Evaluation procedure"
Scope:  baseline only

Figure: k = 4 for all games except Space Invaders, k = 3
Owner:  S8, §5
Scope:  the seven games of the 2013 paper

Figure: ALE/{Game}-v5 frameskip 4, repeat_action_probability 0.25, max 108,000 frames per episode (30 min; 27,000 agent steps)
Owner:  S12, registration.py and Environments page
Scope:  ale-py 0.12.1 (2026-08-16)

Figure: {Game}NoFrameskip-v4 frameskip 1, repeat_action_probability 0.0
Owner:  S12
Scope:  ale-py 0.12.1

Figure: AtariPreprocessing frame_skip default 4, noop_max default 30; base env frameskip must be 1
Owner:  S10
Scope:  Gymnasium 1.4.0

Figure: MaxAndSkipObservation skip default 4, minimum 2
Owner:  S10
Scope:  Gymnasium 1.4.0

Figure: RepeatAction num_repeats ≥ 1, no default; added in v1.3.0 (released 2026-04-22)
Owner:  S9
Scope:  Gymnasium 1.3.0 onward; 1.4.0 released 2026-10-05

Figure: HalfCheetah-v5 dt = 5 × 0.01 = 0.05 s; Acrobot-v1 dt = 0.2 s with truncation at 500 steps; CartPole tau 0.02 s; Pendulum dt 0.05 s
Owner:  S11
Scope:  Gymnasium 1.4.0 defaults

Figure: Acrobot-v1 time limit 500 × 0.2 = 100 s at default dt; 500 × 0.05 = 25 s if dt is set to 0.05
Owner:  derived from S11; my arithmetic
Scope:  step-counted truncation

Figure: Q-learning policy error rises as the time step falls through 0.05, 0.005, 0.0005, 0.00005; tuned Q learning rates 0.02, 0.06, 0.2, 0.4; RAU rate 0.005 at all four
Owner:  S3, Figure 2 and Table 1
Scope:  40,000 learning steps at each step size (2,000 down to 2 simulated time units, my arithmetic)

Figure: frame skips 0, 20, 60, 180 at 60 fps; Seaquest best at 180 (3 s); Space Invaders and Beam Rider best at 60; Pong and Breakout best at low skip; Breakout at 180 always 0
Owner:  S13, text and Figure 1
Scope:  ESP neuroevolution, 5 runs, 200 generations, six games

Figure: S13 Table 1, ESP after 200 generations (frame skip): Beam Rider 1663.2 (60), Breakout 34.2 (0), Pong 15.4 (0), Q*Bert 3380 (20), Seaquest 2258 (180), Space Invaders 1912 (60)
Owner:  S13, Table 1
Scope:  best average score per game over the four skips

Figure: DQN Seaquest 5,450 (ARR 4), 1,707 (ARR 20), 10,458 (dynamic 4|20); Enduro 707, 124, 1,002; Space Invaders 1,189 (ARR 4), 2,796 (dynamic); Alien 2,085 (ARR 4), 3,114 (dynamic)
Owner:  S14, Table 1 (p. 2137)
Scope:  1024-unit DQN; best testing epoch; no seed count or interval reported

Figure: dynamic agent chose the 20-frame action 69.99% (Seaquest), 78.87% (Space Invaders), 71.31% (Alien), 67.84% (Enduro)
Owner:  S14, Table 2
Scope:  one testing run of 10,000 decisions per game

Figure: PFQI Cartpole mean return by persistence k = 1, 2, 4, 8, 16, 32, 64: 169.9, 176.5, 239.5, 10.0, 9.8, 9.8, 9.8 (std 5.8, 5.0, 4.4, 0.0, 0.0, 0.0, 0.0)
Owner:  S15, Table 1 (p. 6869)
Scope:  20 runs; batch FQI with extra-trees; data collected at k = 1

Figure: highest mean return by environment in S15 Table 1: MountainCar k = 32 (−92.4); LunarLander k = 8 (2.0); Pendulum k = 2 (−113.1); Acrobot k = 2 (−82.5); Swimmer k = 2 (25.2); Hopper k = 64 (73.4); Walker 2D k = 16 (102.1)
Owner:  S15, Table 1
Scope:  20 runs; the bold marks in the table show statistical ties, which I could not read from the text extraction

Figure: Acrobot (5 Hz) Sarsa_d(λ): best d = 3 at 8,000 episodes; d ≤ 5 beats d = 1; γ = 0.99 alone reaches 95.6 steps (11.8 better than Sarsa(λ)); best combination d = 3, γ = 0.999
Owner:  S16, §6.1 and Figure 3
Scope:  tile coding, λ = 0.9, α = 0.1

Figure: bicycle domain step 0.01 s; grid cell π/5 in ψ against a per-step change below π/1000
Owner:  S17, "Experiments on the Bicycle Domain"
Scope:  10-point-per-dimension grid over 6 features

Figure: grid time step τ(ξ,u) = δ²/Σ_i[δ|f_i| + a_ii − ½Σ_{j≠i}|a_ij|]; with no noise, δ/Σ|f_i|
Owner:  S18, eq. 5
Scope:  finite-difference scheme on a grid of spacing δ
```

Series worth charting: S15's Cartpole row (return against k, with the collapse at k = 8), and S1's horizon relation against S6 (horizon in steps τ/dt against horizon in seconds τ, for a fixed τ). S3's Figure 2 has four points per algorithm, and Table 1 gives the learning rates behind them.

## Limits

- Baird (1994) was not opened (IEEE paywall), and neither was Baird's 1993 technical report (DTIC returned 403). The priority claim rests on S1 §2 and S1 §3.2 ("This argument appears informally in (Baird, 1994)") and on S3, which comes from Baird's group.
- No source runs tabular Q-learning on a discretized continuous-time task across dt. For the commission's case, the lesson's runs are the only evidence.
- The commission's statement that the target's noise "does not shrink" with dt is not supported as worded (Contradiction 1).
- The commission's claim that repeat "restores an action gap of order k·dt" is not stated in any source. It follows from S1's Theorem 2 applied to M_{k·dt}, since S1 defines a transition as holding the action for the step, together with S15's qualitative statement (§1). The order holds only while k·dt is small against the system's own time scale.
- None of S13–S16 isolates the action gap as the cause of repeat's benefit. They name exploration, horizon, computation and skipping non-Markov frames.
- S13 and S14 report best runs or best epochs without intervals. S16 is a preprint. S19's venue was not verified.
- I did not open Machado et al. (2018), which Gymnasium and ALE cite for their defaults, or Sutton, Precup and Singh (1999). The semi-MDP pointer is S6 §17.2.
- GitHub was not reachable from this session (403). Gymnasium and ALE code was read from the PyPI wheels of the same releases the documentation describes.
- Everything else the commission asked for was established: the S1 section and proof, DQN's frame skip, current Gymnasium/ALE frame-skip handling, and a source on action repeat as a tuned choice.

## Source assets

```text
Asset: S1 Figure 1 (PMLR p. 6102): learned value functions on pendulum swing-up for DDPG and DAU at several δt and several physical times
Shows: DDPG's value function changes with δt while DAU's does not
Crop:  must keep the δt labels and the algorithm labels; it shows DDPG, not tabular Q-learning, and the caption must say so

Asset: S1 Figure 2 (PMLR p. 6103): learning curves of DAU and DDPG against physical time for each δt on five environments
Shows: degradation with smaller δt for DDPG on Ant and Cheetah
Crop:  keep the axis "physical time" and the δt legend; same caveat as Figure 1

Asset: S3 Figure 2 (p. 358): final error against time step (0.05 to 0.00005) for Q, RQ and RAU
Shows: Q-learning's error rising as the step shrinks while RAU stays flat
Crop:  keep the axis labels and legend; the caption must say steps were fixed at 40,000; scan quality is poor

Asset: S7 Extended Data Table 1 (DeepMind PDF p. 10)
Shows: "action repeat 4" next to "agent history length 4"
Crop:  keep both rows and the column headers, so the two 4s are not conflated

Asset: S13 Figure 1 (p. 11): six panels of ESP score by generation at frame skips 0, 20, 60, 180
Shows: the best frame skip differs by game, and skip 180 scores lowest on Breakout (always 0) and Pong
Crop:  keep all six game titles and the shared legend

Asset: S14 Table 1 (p. 2137)
Shows: DQN at ARR 4, ARR 20 and dynamic on Seaquest, Space Invaders, Alien, Enduro
Crop:  keep the HLS and ARR columns; rows 1–3 and 11–14 carry the static-20 comparison

Asset: S15 Table 1 (p. 6869), Cartpole row
Shows: return peaks at k = 4 and collapses at k ≥ 8
Crop:  keep the header row with k values and the caption's note on 20 runs and bolding

Asset: S16 Figure 3c (p. 7): Acrobot reward after 8,000 episodes over d and γ
Shows: repeat and a lower discount both help, and repeat helps more
Crop:  keep both axes and the γ legend

Asset: S19 Figure 1 (p. 3): first-visit times in an open gridworld for ε-greedy with and without temporal persistence
Shows: ε-greedy dithers near the start while persistent random actions spread out
Crop:  keep both panels and the colour key

S5, S6, S8, S9, S10, S11, S12, S17, S18: None found (text, code or equations only; equations should be typeset, not cropped).
```

## Discarded

```text
https://arxiv.org/abs/1605.05365: Lakshminarayanan, Sharma and Ravindran's IJCAI 2016 workshop preprint "Dynamic Frame skip Deep Q Network"; superseded by the peer-reviewed AAAI 2017 version (S14), which repeats its Seaquest numbers and adds Enduro and A3C
https://arxiv.org/abs/1901.09732: arXiv v2 of S1; same content, different equation and appendix numbering; cite PMLR
https://www.nature.com/articles/nature14236 (page text): paywalled; Methods not visible; content read from the DeepMind-hosted PDF and recorded under S7
https://ojs.aaai.org/index.php/AAAI/article/view/10918: bot-check page returned instead of the article; the paper itself was read from AAAI's CDN (S14)
https://apps.dtic.mil/sti/citations/ADA280862: Baird's 1993 "Advantage Updating" report; 403 to curl and WebFetch; not read (see S4)
https://ieeexplore.ieee.org/document/374604: Baird 1994; empty response to WebFetch; metadata taken from Crossref (S4)
```
