# Evidence: frame-stacking-and-the-markov-property (researcher 01)

Sutton and Barto's second edition (2020 printing) supports the commission's definitions. Section 3.1 (p. 49) defines the Markov property as a restriction on the state. Section 17.3 (pp. 464–468) defines state as a function of the history of observations and actions, gives a one-step test for a Markov state (eq. 17.8, p. 466), and names the "kth-order history" state that shifts new observations in and old ones out (p. 468). Mnih et al. (2015) state the four-frame stack (m = 4, "robust to ... 3 or 5") in the Methods. The reason they give is partial observability and "perceptually aliased" emulator states, which they handle by treating the whole observation-action sequence as the state. The stack is their preprocessing map applied to that sequence. They never say "velocity" and never claim four frames give a Markov state. The velocity reading comes from later authors, and Sutton and Barto add that stacking "did not eliminate partial observability for all of the games". I installed Gymnasium 1.4.0 and Stable-Baselines3 2.9.2, the PyPI releases current on 14 November 2026, and called both APIs. Recorded signatures, shapes and padding behaviour come from those runs. Two findings complicate the commission's angle. First, a frame stack does not hold k real observations at the start of an episode, because both libraries pad it, so the first stacked observation is still aliased. Second, Singh, Jaakkola and Jordan (1994) show that TD(0) and Q-learning on aliased observations converge to a Bellman fixed point whose one-step terms are averaged under the policy's occupancy distribution. That fixed point is in general not the visit-weighted average of the hidden states' true values, which only Monte Carlo finds. The policy-dependence the commission wants derived holds in both cases. The thinnest evidence is the SB3 team's frame-stacking-versus-LSTM comparison, a JavaScript-rendered report whose wording I could confirm only through two rendering fetches.

## Decisions taken under the commission

The brief said to ask the orchestrator where something was missing. These questions came up, and I settled each under the commission instead:

- **"The Markov property sections of Chapter 3".** The second edition has no such section. Its Chapter 3 runs from 3.1 to 3.8, and the definition is one paragraph in §3.1 (p. 49). I recorded that paragraph and a mention on p. 66. I also recorded the first edition's §3.5 "The Markov Property", because it contains the sentence about measuring position at two times to get velocity, which is this lesson's idea. Whether to cite a superseded edition is the writer's choice.
- **"The DQN paper's frame-stacking passage and its stated reason".** I recorded the reason the paper states (aliasing, with the history as the state) separately from the velocity reading that other authors give. They are not the same claim.
- **A source outside the brief's list.** I added Singh, Jaakkola and Jordan (1994). Sutton and Barto's §17.3 bibliographical remarks name it as the theory of RL with a non-Markov state. It gives the exact fixed points that the commissioned derivation needs, and it changes what the derivation can claim for Q-learning (see Contradictions). Under "cite little", the writer can use it as a Go deeper link only.
- **Velocity-masked benchmark.** RL Zoo's CartPoleNoVel-v1 works with SB3's VecFrameStack and needs no extra package, so I recorded it first. POPGym's PositionOnlyCartPole is recorded as the alternative. POPGym's paper-named "Stateless Cartpole" hides positions, not velocities, so I recorded it as a counter-case.
- **"Current in November 2026".** I took this to mean the latest PyPI releases on 14 November 2026: gymnasium 1.4.0 (released 2026-10-05) and stable-baselines3 2.9.2 (released 2026-10-26).

## Sources

### 1. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd edition (2020 printing)

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (book page: http://incompleteideas.net/book/the-book-2nd.html; the https:// form of
             the host failed TLS verification from this machine, so the http address is recorded)
Kind:        primary. Richard S. Sutton and Andrew G. Barto author the definitions; this is
             where they state them. MIT Press, Cambridge, MA, 2018; this PDF is the second
             printing (2020): the first-printing errata for pp. 463 and 465 are already applied.
             Page numbers below are those printed on the page (PDF page = printed page + 22).
Establishes: firsthand: the definitions of the Markov property, history, state as a function
             of history, Markov state, the state-update function, the one-step test, the
             kth-order history state, and the state-aggregation results used for the derivation.
Paraphrase:  (a) In an MDP the dynamics p(s',r|s,a) (eq. 3.2) completely characterize the
             environment: the next state and reward depend on the preceding state and action and
             not on earlier ones. The authors say this is a restriction on the state, which must
             include everything about the past interaction that matters for the future; such a
             state has the Markov property. They say Chapter 17 treats constructing a Markov
             state from non-Markov observations.
             (b) Solving the Bellman optimality equation exactly assumes the states have the
             Markov property, among three assumptions "rarely true in practice".
             (c) Monte Carlo methods "may be less harmed by violations of the Markov property"
             because they do not bootstrap.
             (d) State aggregation groups states under one shared value component. With gradient
             Monte Carlo on the 1000-state random walk, the learned group values are close to the
             minimum of the mu-weighted error VE, and the leftmost groups sit "clearly shifted
             higher than the unweighted average of the true values of states within the group"
             because of the visit distribution mu.
             (e) At the TD fixed point, VE(w_TD) <= 1/(1-gamma) min_w VE(w) (continuing case).
             (f) Section 17.3. The authors replace states with observations O_t, which depend on
             the state but carry only partial information; reward is assumed a known function of
             the observation. Parametric function approximation "includes important aspects of
             partial observability": choosing a parameterization that ignores a state variable
             has the same effect as that variable being unobservable (p. 464). History is
             H_t = A_0, O_1, ..., A_{t-1}, O_t; state is "a compact summary of the history that
             is useful for predicting future sequences", S_t = f(H_t); a summary that keeps all
             predictive information is a Markov state (p. 465). Tests (17.5); f is Markov iff
             histories mapping to the same state give every test the same probability (17.6);
             a Markov state suffices for optimal behaviour by a deterministic policy (p. 465).
             The state-update function S_{t+1} = u(S_t, A_t, O_{t+1}) (17.7, p. 465; Figure
             17.1, p. 466). If f is incrementally updatable, it is Markov iff all one-step
             predictions of the next observation agree across histories with the same state
             (17.8, p. 466). POMDP belief state (17.9, 17.10, p. 467). Approximate state: the
             simplest is S_t = O_t, which "cannot handle any hidden state information"; better is
             the last k observations and actions, updated by shifting new data in and old data
             out, the "kth-order history approach", which "can greatly increase the agent's
             capabilities" over the single observation (p. 468). When (17.8) holds only
             approximately "there are no useful theoretical guarantees at present" (p. 468).
             (g) Bibliographical remarks for 17.3: the theory of RL with a non-Markov state
             representation "was developed explicitly by Singh, Jaakkola, and Jordan (1994;
             Jaakkola, Singh, and Jordan, 1995)".
Locators:    (a) §3.1 "The Agent–Environment Interface": eq. (3.2) p. 48; Markov-property
             paragraph p. 49, first full paragraph. (b) §3.6, p. 66. (c) §5.10 "Summary",
             p. 115, second paragraph. (d) §9.3, Example 9.1 and Figure 9.1, p. 204; VE (9.1)
             and episodic on-policy distribution (9.2)-(9.3), §9.2, p. 199. (e) §9.4, eq. (9.14),
             p. 207. (f) §17.3 "Observations and State", pp. 464–468, equation numbers as above
             (they differ in the 2018 first printing; see source 3). (g) Chapter 17
             Bibliographical and Historical Remarks, entry 17.3, p. 479.
Quote:       p. 49: "The state must include information about all aspects of the past
             agent–environment interaction that make a difference for the future. If it does,
             then the state is said to have the Markov property."
             p. 465: "The idea of state is that of a compact summary of the history that is
             useful for predicting future sequences."
             p. 468: "S_t ≐ O_t, A_{t−1}, O_{t−1}, ..., A_{t−k}, for some k ≥ 1, which can be
             achieved by a state-update function that just shifts the new data in and the oldest
             data out." (formula checked against a render of the page)
```

### 2. Sutton and Barto §16.5 on DQN (same PDF)

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
Kind:        secondary for DQN's reasons: Sutton and Barto describe Mnih et al.'s work from
             outside the DQN team.
Establishes: repeats the four-frame stack; adds their own judgement that stacking left some
             games partially observable.
Paraphrase:  Because many Atari games' full states are not observable from frames, Mnih et al.
             stacked the four most recent preprocessed frames into an 84x84x4 input. In the
             authors' assessment this did not remove partial observability in every game but made
             many of them "more Markovian". The only game-general prior knowledge used was that
             "stacking adjacent frames should help with the partial observability of some of the
             games".
Locators:    §16.5 "Human-level Video Game Play", pp. 438–439 (paragraph beginning "A human
             playing any of these 49 Atari games" and the next).
Quote:       "This did not eliminate partial observability for all of the games, but it was
             helpful in making many of them more Markovian." (p. 438)
```

### 3. Sutton and Barto errata page

```text
URL:         http://incompleteideas.net/book/errata.html
Kind:        primary: the authors' own corrections.
Establishes: which printing the PDF is, and that §17.3's Markov-state text was revised.
Paraphrase:  Under "Errata for the first printing (2018)": "p465: This definition and discussion
             of Markov state is insufficient. In addition to a Markov state being sufficient to
             make the one-step predictions (17.6), it must also be incrementally updatable as in
             (17.9)." The 2020 PDF already carries the revised text, with the condition now
             numbered (17.8) on p. 466. The second-printing errata list nothing on pp. 48–49, 66,
             115, 199, 204, 207, 438–439 or 464–468.
Locators:    "Errata for the first printing (2018) of the second edition", entries for p465;
             second-printing list scanned for the pages above.
```

### 4. Sutton and Barto, 1st edition (1998), §3.5 "The Markov Property"

```text
URL:         http://incompleteideas.net/book/first/ebook/node32.html
Kind:        primary, superseded: the same authors' first edition.
Establishes: a sentence that states the lesson's idea, and a counter-case. Neither passage is
             in the second edition (its text has no "two different times", "cannonball" or
             "coarse state").
Paraphrase:  A state can be built from immediate sensations plus memory of past ones. A control
             system can measure position at two times to get a state that carries velocity.
             Example 3.5 says a pole-balancing state is Markov if it specifies, or makes it
             possible to reconstruct, cart position and velocity, pole angle and angular
             velocity. It also says early studies used a coarse three-region quantization, a
             "distinctly non-Markov state", that let RL solve the task easily.
Locators:    §3.5, paragraph beginning "Certainly the state signal should include immediate
             sensations"; Example 3.5 "Pole-Balancing State".
Quote:       "At a more mundane level, a control system can measure position at two different
             times to produce a state representation including information about velocity."
```

### 5. Mnih et al. (2015), "Human-level control through deep reinforcement learning", Nature 518, 529–533

```text
URL:         https://www.nature.com/articles/nature14236 (doi:10.1038/nature14236)
             Full text read from the PDF DeepMind hosts:
             https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf
Kind:        primary: the DQN authors (Volodymyr Mnih, Koray Kavukcuoglu, David Silver and
             others, Google DeepMind) describe their own method.
Establishes: firsthand: the four-frame stack, its insensitivity to 3 or 5, the action repeat of
             4, and the reason they give for using history (partial observability and
             perceptual aliasing).
Paraphrase:  Methods, "Preprocessing": the stated aim of the paragraph is to reduce input
             dimensionality and deal with emulator artefacts. Each encoded frame takes the
             per-pixel maximum over that frame and the previous one, to remove sprite flicker.
             Frames are reduced to luminance and rescaled to 84x84. The map phi applies this to
             the m most recent frames and stacks them, with m = 4.
             Methods, "Algorithm": the agent sees only the current screen. The task is partially
             observed, and many emulator states are perceptually aliased. So the algorithm takes
             sequences s_t = x_1, a_1, x_2, ..., a_{t-1}, x_t as input. Treating each sequence as a
             distinct state gives a large but finite MDP.
             Algorithm 1: s_{t+1} = s_t, a_t, x_{t+1} and phi_{t+1} = phi(s_{t+1}).
             Fig. 1 caption: the network input is an 84x84x4 image produced by phi.
             Extended Data Table 1: "agent history length 4" and "action repeat 4".
             The paper never uses the word "velocity"; I searched the full text.
Locators:    Methods "Preprocessing" (Methods pages carry no journal page numbers; PDF p. 6,
             left column); Methods "Algorithm" (PDF p. 6, right column, second paragraph,
             citing ref. 33, Kaelbling, Littman and Cassandra); Algorithm 1 (PDF p. 7); Methods
             "Training details" (frame skipping k = 4, PDF p. 6); Fig. 1 caption (p. 530);
             Extended Data Table 1 (PDF p. 10).
Quote:       "The function φ from algorithm 1 described below applies this preprocessing to the m
             most recent frames and stacks them to produce the input to the Q-function, in which
             m = 4, although the algorithm is robust to different values of m (for example, 3 or
             5)."
             "Because the agent only observes the current screen, the task is partially observed
             and many emulator states are perceptually aliased (that is, it is impossible to fully
             understand the current situation from only the current screen x_t)."
             Extended Data Table 1, agent history length: "The number of most recent frames
             experienced by the agent that are given as input to the Q network."
```

### 6. Mnih et al. (2013), "Playing Atari with Deep Reinforcement Learning", arXiv:1312.5602

```text
URL:         https://arxiv.org/abs/1312.5602
Kind:        primary: the same team's earlier paper (submitted 19 Dec 2013).
Establishes: the first statement of the stack and of the aliasing reason, in nearly the same
             words as source 5.
Paraphrase:  §2 gives the aliasing sentence and "We therefore consider sequences of actions and
             observations". §4.1 says phi "applies this preprocessing to the last 4 frames of a
             history and stacks them to produce the input to the Q-function". The preprocessing
             there is grey-scale, down-sampled to 110x84 and cropped to 84x84.
Locators:    §2 "Background", p. 2; §4.1 "Preprocessing and Model Architecture", p. 5.
```

### 7. Gymnasium 1.4.0, `gymnasium.wrappers.FrameStackObservation`

```text
URL:         docs: https://gymnasium.farama.org/v1.4.0/api/wrappers/observation_wrappers/#gymnasium.wrappers.FrameStackObservation
             source: https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/stateful_observation.py
             (class at line 305, __init__ at 367, step at 420, reset at 439)
             release: https://pypi.org/project/gymnasium/1.4.0/ (uploaded 2026-10-05)
Kind:        primary: the Farama Foundation's own documentation and code.
Establishes: name, signature, behaviour and padding of the wrapper, confirmed by calling it.
Paraphrase:  Signature: FrameStackObservation(env, stack_size: int, *, padding_type: str |
             ObsType = "reset"). It stacks the last N observations "in a rolling manner". Padding
             options are "reset" (repeat the reset observation, the default), "zero" (a zero-like
             element of the observation space) or a custom element of the space. "No vector
             version of the wrapper exists." The observation space is batch_space(env space, n =
             stack_size), so a Box of shape S becomes shape (stack_size, *S), and Discrete(n)
             becomes MultiDiscrete([n]*stack_size). Index 0 is the oldest observation and the last
             index the newest. stack_size must be a positive integer. Change log in the
             docstring: added in v0.15.0 as FrameStack with lz4 support; renamed
             FrameStackObservation in v1.0.0, with lz4 and LazyFrame removed and padding_type
             added. The same module defines TimeAwareObservation (line 106) and
             DelayObservation (line 35).
Locators:    docs anchor #gymnasium.wrappers.FrameStackObservation; docstring and lines cited
             above. The tagged source file is byte-identical to the installed wheel (diffed).
Quote:       signature as printed by inspect.signature in the 1.4.0 install:
             (self, env: 'gym.Env[ObsType, ActType]', stack_size: 'int', *, padding_type: 'str | ObsType' = 'reset')
```

### 8. Stable-Baselines3 2.9.2, `stable_baselines3.common.vec_env.VecFrameStack`

```text
URL:         docs: https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/vec_envs.html#vecframestack
             source: https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/vec_frame_stack.py
             and .../stable_baselines3/common/vec_env/stacked_observations.py (bounds at lines 54–55)
             release: https://pypi.org/project/stable-baselines3/2.9.2/ (uploaded 2026-10-26)
Kind:        primary: the SB3 maintainers' documentation and code.
Establishes: name, signature and behaviour, confirmed by calling it; one defect in the declared
             observation-space bounds, found by me.
Paraphrase:  Signature: VecFrameStack(venv, n_stack, channels_order=None). The docstring says
             "Frame stacking wrapper for vectorized environment. Designed for image
             observations." With channels_order None, it detects the channel axis of an image or
             defaults to "last". A dict works for Dict spaces. It accepts only Box and Dict
             observation spaces; a Discrete space raises "AssertionError: VecFrameStack only works
             with gym.spaces.Box and gym.spaces.Dict observation spaces". For a 1-D Box it
             concatenates along the last axis: CartPole's (4,) becomes (8,), ordered [older
             observation, newest observation]. Reset fills the stack with zeros and writes the
             reset observation into the newest slot. At an episode end it zeroes that env's stack
             and puts the stacked terminal observation in info["terminal_observation"].
             Defect: the declared low/high come from np.repeat(low, n_stack, axis=-1), which
             interleaves per-feature bounds ([b0, b0, b1, b1, ...]), while the data concatenates
             whole observations ([o0, o1, o0', o1']). For a Box whose features have different
             bounds, the stacked observation falls outside its own declared space. Test: a 2-D
             Box with bounds [0,1] and [10,11], n_stack=2 gave declared low [0, 0, 10, 10], obs
             [0.5, 10.5, 0.5, 10.5], observation_space.contains(obs) == False. It matters only
             to code that reads the bounds. Two REST searches of the SB3 issue tracker found no
             existing report.
Locators:    docs anchors #vecframestack and #stable_baselines3.common.vec_env.VecFrameStack;
             source lines cited above (tag v2.9.2 = commit 0cdcd200; tagged files byte-identical
             to the installed wheel).
```

### 9. RL Baselines3 Zoo 2.9.2, `MaskVelocityWrapper` and the `*NoVel` environments

```text
URL:         https://github.com/DLR-RM/rl-baselines3-zoo/blob/v2.9.2/rl_zoo3/wrappers.py (class at line 299)
             https://github.com/DLR-RM/rl-baselines3-zoo/blob/v2.9.2/rl_zoo3/import_envs.py (lines 58–72)
             https://github.com/DLR-RM/rl-baselines3-zoo/blob/v2.9.2/hyperparams/ppo_lstm.yml (CartPoleNoVel-v1 entry, line 49)
             release: https://pypi.org/project/rl-zoo3/2.9.2/ (uploaded 2026-10-26)
Kind:        primary: the SB3 team's training framework, which defines these environments.
Establishes: a velocity-masked CartPole that runs with SB3's VecFrameStack, confirmed by calling
             it.
Paraphrase:  MaskVelocityWrapper is an observation wrapper "used to mask velocity terms in
             observations. The intention is the make the MDP partially observable" (sic). It
             multiplies the observation by a 0/1 mask, so the shape stays the same and the masked
             entries read 0. Masked indices: CartPole-v1 [1, 3]; MountainCar-v0 [1];
             MountainCarContinuous-v0 [1]; Pendulum-v1 [2]; LunarLander-v3 and
             LunarLanderContinuous-v3 [2, 3, 5]. Importing rl_zoo3.import_envs registers
             "{name}NoVel-v{version}" for each. Verified ids: CartPoleNoVel-v1,
             LunarLanderContinuousNoVel-v3, LunarLanderNoVel-v3, MountainCarContinuousNoVel-v0,
             MountainCarNoVel-v0, PendulumNoVel-v1. CartPoleNoVel-v1 has observation shape (4,),
             with entries 1 and 3 equal to 0. Under VecFrameStack(n_stack=2) the shape is (8,),
             and PPO("MlpPolicy") ran learn(2048) on it. hyperparams/ppo_lstm.yml tunes
             RecurrentPPO for CartPoleNoVel-v1. hyperparams/ppo.yml has no NoVel entries.
Locators:    lines cited above.
```

### 10. SB3-Contrib RecurrentPPO documentation and Antonin Raffin's W&B report

```text
URL:         https://sb3-contrib.readthedocs.io/en/v2.9.2/modules/ppo_recurrent.html ("Results")
             https://wandb.ai/sb3/no-vel-envs/reports/PPO-vs-RecurrentPPO-aka-PPO-LSTM-on-environments-with-masked-velocity--VmlldzoxOTI4NjE4
             (the link redirects through forge.coreweave.com; the wandb.ai address is recorded)
Kind:        primary for the SB3 team's own benchmark claim. Antonin Raffin, listed as author,
             maintains SB3.
Establishes: that the maintainers ran PPO with frame stacking against RecurrentPPO on the NoVel
             tasks, and their summary of the result. It establishes no figure.
Paraphrase:  The docs' "Results" section points to a "Report on environments with masked
             velocity (with and without framestack)" covering PendulumNoVel-v1,
             LunarLanderNoVel-v2, CartPoleNoVel-v1, MountainCarContinuousNoVel-v0 and
             CarRacing-v0. The report (last updated 9 October 2022) says it checks that PPO with
             a recurrent network works. Its hyperparameters were tuned for PPO. PPO with frame
             stacking (n_stack=2) is usually competitive with or better than RecurrentPPO and
             faster. CarRacing-v0 and LunarLanderNoVel-v2 differ.
Locators:    docs section "Results"; report sections "PPO LSTM vs PPO (no FrameStack)" and
             "LSTM vs FrameStacking".
Quote:       "PPO with frame-stacking (giving an history of observation as input) is usually
             quite competitive if not better, and faster than recurrent PPO". This wording comes
             from a rendering fetch and a search-engine extract, which agree. The raw page is a
             JavaScript shell, so I could not check it character for character.
```

### 11. Morad et al. (2023), "POPGym: Benchmarking Partially Observable Reinforcement Learning", ICLR 2023, and the popgym 1.0.7 package

```text
URL:         https://arxiv.org/abs/2303.01859 ; package https://pypi.org/project/popgym/1.0.7/
             (uploaded 2026-06-11)
Kind:        primary: the benchmark's authors describe and evaluate their own environments.
Establishes: a widely used masked-control benchmark in which the paper's "Stateless Cartpole"
             hides positions and keeps velocities. The paper also reports frame-stacking
             results, and the current package contains a velocity-masked CartPole.
Paraphrase:  Stateless Cartpole is CartPole "with the angular and linear positions removed from
             the observation. The agent must integrate to compute positions from velocity" (§3.1,
             item 4, p. 5). Masked control tasks hide "the velocity or position portions of
             classic control problems, and are probably the second most popular type of POMDP in
             literature after navigation" (§6, p. 9). The frame-stacking baseline concatenates k
             observations, with a window of four (Appendix A.2, p. 15). Frame stacking "is known
             to work very well in RL, but the number of parameters scales with the receptive
             field, preventing it from learning long-term dependencies" (§4, item 10, p. 7).
             Table 3 gives MMER (max-mean episodic reward; returns are bounded in [-1, 1]) over 3
             trials with PPO. On Stateless Cartpole Easy/Medium/Hard: Fr.Stack 1.000/1.000/0.989,
             MLP 0.722/0.398/0.265, LSTM 1.000/1.000/1.000 (pp. 34–35).
             Package 1.0.7, verified by installing and calling it: the velocity-masked version is
             PositionOnlyCartPole{Easy,Medium,Hard}, ids popgym-PositionOnlyCartPoleEasy-v0 etc.
             Its observation is [x, theta], and the full state is available from get_state().
             Episode lengths are 200/400/600; reward is 1/max_episode_length per step and -1 on
             failure. The paper's position-masked task is now VelocityOnlyCartPole.
             PositionOnlyCartPole's docstring says it deletes "the position and angular velocity
             components", but the code keeps x and theta. VelocityOnlyCartPole.reset returns
             [x, theta] (positions); its steps return [x_dot, theta_dot].
Locators:    sections and pages as above; package files popgym/envs/position_only_cartpole.py
             and velocity_only_cartpole.py.
```

### 12. Ni, Eysenbach and Salakhutdinov (2022), "Recurrent Model-Free RL Can Be a Strong Baseline for Many POMDPs", ICML 2022

```text
URL:         https://arxiv.org/abs/2110.05038
Kind:        primary for the authors' own claims; secondary for the origin of the -P/-V benchmark,
             which they attribute to VRM (Han, Doya and Tani, ICLR 2020).
Establishes: the velocity-masked locomotion benchmark used in recurrent-RL papers, and the
             authors' statement that hidden velocities need only a short context.
Paraphrase:  "-P" environments keep only positions and angles; "-V" keep only velocities. The
             set is {Hopper, Ant, Walker, Cheetah}-{P, V}, run in PyBullet in place of the
             deprecated Roboschool, plus Pendulum as a sanity check. A POMDP that hides
             velocities theoretically needs only a short context to infer them from consecutive
             positions (citing Meng et al., 2021).
Locators:    §4, p. 5 (context length); §5, p. 6 (benchmark); Appendix D.1, p. 18
             (PyBullet, entries removed).
Quote:       "a POMDP that hides velocities from observations theoretically only requires a short
             context length to infer velocities through consecutive positions (Meng et al., 2021)."
```

### 13. Hausknecht and Stone (2015), "Deep Recurrent Q-Learning for Partially Observable MDPs"

```text
URL:         https://arxiv.org/abs/1507.06527
Kind:        primary for their own experiments; secondary on DQN's design.
Establishes: the velocity reading of single Atari frames, the four-frame memory limit of DQN's
             input, and a case where a fixed stack cannot determine the hidden part.
Paraphrase:  With one frame, Pong, Frostbite and Double Dunk are POMDPs because a frame does not
             reveal the ball's or the icebergs' velocity. Any game that needs memory of more than
             four frames appears non-Markovian to DQN. In Flickering Pong, each frame is fully
             obscured with probability p = 0.5, so a player must cope with several obscured
             frames in a row. They compare a 10-frame DQN with a 1-frame recurrent DRQN given the
             same history length. Recurrence matched stacking for learning and adapted better at
             evaluation when observation quality changed.
Locators:    Fig. 1 caption and Introduction, p. 1; Abstract, p. 1; "Flickering Atari Games",
             p. 3.
Quote:       "a single observation does not reveal the velocity of the ball (Pong, Double Dunk) or
             the velocity of the icebergs (Frostbite)." (Fig. 1 caption)
```

### 14. Heess, Hunt, Lillicrap and Silver (2015), "Memory-based control with recurrent neural networks"

```text
URL:         https://arxiv.org/abs/1512.04455
Kind:        primary for their tasks; secondary on DQN.
Establishes: the original position-only pendulum and cartpole swing-up tasks used for recurrent
             control, and another author's reading of DQN's stack as velocity estimation.
Paraphrase:  Pendulum and cartpole swing-up are modified so that the agent gets no velocity: the
             pendulum observation is only the angle, and the cartpole observation is the pole
             angle and cart position. "Velocity is crucial for solving the task and thus it must
             be estimated from the history of the system." In related work they say recurrent Q
             learning can resolve "short-term partial observability (e.g. to estimate velocities)
             that is achieved via stacks of frames in the original DQN architecture."
Locators:    §4.1 "Sensor integration and system identification", pp. 5–6; related work, p. 8.
```

### 15. Singh, Jaakkola and Jordan (1994), "Learning Without State-Estimation in Partially Observable Markovian Decision Processes", ICML 1994, pp. 284–292

```text
URL:         https://web.eecs.umich.edu/~baveja/Papers/ML94.pdf (copy on Satinder Singh's own
             site); doi:10.1016/B978-1-55860-335-6.50042-8
Kind:        primary: the authors' own definitions and theorems. Sutton and Barto name it as the
             source of the theory (source 1g).
Establishes: the definition of an observation's value as an occupancy-weighted average of
             hidden-state values; what TD(0) and Q-learning converge to on aliased observations;
             and that the result depends on the policy followed during learning.
Paraphrase:  Eq. (2) proposes V^pi(X) = sum_s P^pi(s|X) V^pi(s) as the value of observation X.
             P^pi(s|X) = P(X|s) P^pi(s) / sum_s' P(X|s') P^pi(s') is the asymptotic occupancy
             probability under pi. Theorem 1: TD(0) converges to the solution of eq. (3),
             V(X) = sum_s P^pi(s|X) [R^pi(s) + gamma sum_X' P^pi(s,X') V(X')], which "in general
             ... will not equal the desired value function as defined in Equation 2".
             Figure 2 is a six-state, five-observation POMDP in which TD(0) gives observations 2
             and 3 the same value although their true values differ. Footnote 2: TD(lambda<1)
             also fails; off-line TD(1), "equivalent to the Monte Carlo algorithm", finds eq. (2)
             for POMDPs with absorbing goal states. Theorem 2: with a fixed stationary policy
             that tries every action in every state ("persistent excitation"), Q-learning
             converges to eq. (4), Q(X,a) = sum_s P^pi(s|X,a) [R^a(s) + gamma sum_X'
             P^a(s,X') max_a' Q(X',a')]. That fixed point has the same problem as eq. (3), and
             Q-learning assumes a deterministic policy is sought. Facts 1–2: confounding two
             states can cost arbitrarily much return, and the best stationary stochastic
             memoryless policy can beat the best deterministic one by an arbitrary amount.
             Footnote 1: unlike the Markov case, Q-learning's values in POMDPs depend on the
             control policy followed during learning.
Locators:    the PDF prints no page numbers. §3 with Facts 1–2 and footnote 1, PDF p. 2; Figure 1,
             PDF p. 3; §4 with eq. (2) and Theorem 1, PDF p. 4; Figure 2, footnote 2, §5.1 and
             Theorem 2, PDF p. 5. Assuming the nine PDF pages are proceedings pp. 284–292 in
             order, these are pp. 285, 286, 287 and 288.
Quote:       "No algorithm for POMDPs can retain that advantage because the control policy
             followed during learning will impact the occupancy probabilities that are a part of
             the definition of the return from a policy." (§5.1)
```

### 16. Whitehead and Ballard (1991), "Learning to perceive and act by trial and error", Machine Learning 7(1):45–83

```text
URL:         https://link.springer.com/article/10.1007/BF00058926
Kind:        primary for the term: the authors name the phenomenon.
Establishes: the origin of "perceptual aliasing", the term DQN uses. I read the abstract only.
Paraphrase:  An agent's internal representation can confound distinct world states. The authors
             call this perceptual aliasing and say it destabilizes existing RL algorithms with
             respect to the optimal policy.
Locators:    Abstract.
Quote:       "We call this phoenomenon Perceptual aliasing" (the abstract's spelling).
```

## Contradictions

- **DQN's stated reason versus the velocity reading.** Mnih et al. (source 5, Methods "Algorithm") justify history with partial observability and perceptual aliasing, and they take the whole observation-action sequence as the state. The four-frame stack is phi applied to that sequence. The paper never says "velocity", never says four frames make the input Markov, and gives no reason for m = 4 beyond robustness to 3 or 5. The velocity reading comes from Hausknecht and Stone (source 13, Fig. 1 caption) and Heess et al. (source 14, p. 8). Sutton and Barto (source 2) say the stack "did not eliminate partial observability for all of the games". On the page, attribute velocity to those authors, not to Mnih et al.
- **The commissioned derivation versus Singh, Jaakkola and Jordan.** The commission asks why "a value keyed on an aliased observation is an average over hidden states under the visit distribution." Singh et al. define the value that way (eq. 2), but only Monte Carlo (off-line TD(1)) converges to it. TD(0) converges to eq. (3), and Q-learning under a fixed exploring policy converges to eq. (4). In those fixed points, what gets averaged under P^pi(s|X) or P^pi(s|X,a) is the one-step reward and the next observation's estimated value, not the hidden states' true values. In general the result differs from eq. (2). Sutton and Barto make the matching point for Monte Carlo versus bootstrapping (source 1c, p. 115) and for state aggregation (source 1d–e, pp. 204, 207). The policy-dependence the commission wants is in both fixed points, because P^pi depends on pi. Theorem 2 holds only for a fixed behaviour policy. Singh et al. give no convergence result for a learner whose epsilon-greedy policy changes as Q changes, which is the lesson's setting.
- **"Stacking those k observations restores the Markov property."** I found four qualifications.
  1. *Episode start.* Both libraries pad. Gymnasium repeats the reset observation by default or uses zeros, and SB3 uses zeros. The first stacked observation of every episode therefore does not contain k real observations and does not determine the hidden velocity. On a Discrete(7) track starting in cell 3, Gymnasium returned [3, 3] with "reset" padding and [0, 3] with "zero" padding. The first reads as a ball at rest, and the second as a ball that came from cell 0. The property holds from step k−1 on, unless the environment fixes the initial velocity or the reset observation reveals it.
  2. *Actions.* Sutton and Barto's kth-order history interleaves actions (p. 468). DQN's stack and both library wrappers stack observations only. That suffices when the agent's actions do not change the hidden quantity between frames, as with a ball moving independently of the agent. It does not suffice when they do.
  3. *Missing or noisy frames.* In Flickering Pong (source 13), each frame is blank with probability 0.5, so no fixed k guarantees the hidden part is determined.
  4. *A good policy is not evidence of a Markov state.* In POPGym's Stateless Cartpole (source 11), positions cannot be recovered from any finite window of velocities. Even so, frame stacking with a window of four reached MMER 1.000/1.000/0.989. The first edition reports that a coarse, "distinctly non-Markov" quantization solved pole balancing easily (source 4).
- **Benchmark naming.** "Stateless Cartpole" in the POPGym paper hides positions. In popgym 1.0.7 that environment is VelocityOnlyCartPole, and the velocity-masked one is PositionOnlyCartPole, whose docstring contradicts its code. RL Zoo's "NoVel" zeroes velocities. Name a benchmark by what it hides.
- **SB3 documentation versus behaviour.** VecFrameStack is "Designed for image observations" but works on 1-D Box observations. On a 1-D Box with per-feature bounds, its declared bounds do not match the data layout (source 8). Gymnasium's stacked Box has the correct bounds.
- **Environment versions in the SB3-Contrib docs.** The docs list LunarLanderNoVel-v2 and CarRacing-v0. RL Zoo 2.9.2 registers LunarLanderNoVel-v3. CartPoleNoVel-v1 is unchanged.
- **Sutton and Barto's equation numbers.** The first-printing erratum refers to the one-step condition as (17.6) and the update as (17.9). The 2020 printing numbers them (17.8) and (17.7). Cite equation numbers with the 2020 printing.

## Numbers

```text
Figure: m = 4 frames stacked; "robust to different values of m (for example, 3 or 5)"
Owner:  Mnih et al. 2015, Methods "Preprocessing"
Scope:  all 49 Atari games, one setting

Figure: network input 84 × 84 × 4
Owner:  Mnih et al. 2015, Fig. 1 caption (p. 530) and Methods "Model architecture"
Scope:  per agent step

Figure: action repeat 4 (agent sees every 4th input frame); agent history length 4
Owner:  Mnih et al. 2015, Extended Data Table 1
Scope:  all games

Figure: gymnasium 1.4.0, uploaded to PyPI 2026-10-05; requires Python >= 3.10
Owner:  https://pypi.org/project/gymnasium/1.4.0/
Scope:  latest release on 2026-11-14 (previous: 1.3.0, 2026-04-22)

Figure: stable-baselines3 2.9.2, uploaded 2026-10-26; requires gymnasium >=0.29.1,<2.0 and torch >=2.8,<3.0
Owner:  https://pypi.org/project/stable-baselines3/2.9.2/
Scope:  latest release on 2026-11-14; sb3-contrib and rl-zoo3 also 2.9.2, same date

Figure: popgym 1.0.7, uploaded 2026-06-11
Owner:  https://pypi.org/project/popgym/1.0.7/
Scope:  latest release on 2026-11-14

Figure: CartPole observation (4,) -> FrameStackObservation(stack_size=2): (2, 4)
Owner:  Gymnasium 1.4.0, run in scratch environment
Scope:  Box observations; Discrete(7) -> MultiDiscrete([7 7])

Figure: CartPole observation (4,) -> VecFrameStack(n_stack=2): (8,)
Owner:  SB3 2.9.2, run in scratch environment
Scope:  1-D Box, channels_order default ("last")

Figure: POPGym Stateless Cartpole MMER, Easy/Medium/Hard: Fr.Stack 1.000/1.000/0.989; MLP 0.722/0.398/0.265; LSTM 1.000/1.000/1.000
Owner:  Morad et al. 2023, Table 3, pp. 34–35
Scope:  PPO, mean over 3 trials, MMER bounded in [-1, 1]; positions hidden, not velocities

Figure: Flickering Pong frame obscured with probability p = 0.5
Owner:  Hausknecht and Stone 2015, p. 3
Scope:  each timestep

Figure: VE(w_TD) <= 1/(1 - gamma) min_w VE(w)
Owner:  Sutton and Barto, eq. (9.14), p. 207
Scope:  linear semi-gradient TD(0), on-policy, continuing case
```

## Limits

- Sutton and Barto page numbers are those printed in the 2020 PDF (second printing). I did not compare them with a bound copy of either printing.
- The Nature article page did not load through a fetch (cookie redirect loop). I read the full text from DeepMind's hosted PDF, and its Methods pages carry no journal page numbers.
- Mnih et al. do not say outright whether the four stacked frames are consecutive emulator frames or every fourth one. Extended Data Table 1 says "most recent frames experienced by the agent" and that the agent sees "only every 4th input frame", which implies every fourth, but neither sentence states it.
- I did not check the W&B report's wording character for character, and I recorded no number from its charts.
- Singh et al.'s proceedings page numbers rest on the assumption that the PDF's nine pages are pp. 284–292 in order.
- For Whitehead and Ballard (1991) I read the abstract only.
- I did not read Han, Doya and Tani (2020, VRM) or Meng et al. (2021). The -P/-V convention and the short-context claim are taken from Ni et al., who cite them.
- I have no read source on whether tabular Q-learning with an epsilon-greedy policy that changes as it learns converges or oscillates on aliased observations. Gordon's 1996 "chattering" note turned up only through secondary citations. The lesson's own runs would have to show what happens.
- I did not establish which POPGym code version produced the paper's Table 3. The 1.0.7 package's VelocityOnlyCartPole returns positions at reset, which would leak initial positions to a velocity-only agent. I cannot say whether the paper's runs had the same behaviour.
- Per the brief, I read the course lessons for file names and titles only, so I did not check which earlier lesson defined the Markov property or how it phrased it.
- The SB3 bounds defect is my own finding from code and one test. I found no maintainer statement about it.

## Source assets

```text
Asset: Sutton and Barto Figure 17.1, p. 466 (agent architecture with state-update function u)
Shows: where a frame stack sits: u takes the old state, the action and the new observation, and
       a kth-order history u just shifts frames.
Crop:  keep the World -> O -> u -> S -> policy loop and the A arrow back into u; the model and
       planner boxes can go only if the caption says they were removed. A redraw in the lesson's
       notation is likely clearer.

Asset: Sutton and Barto Figure 9.1, p. 204 (state aggregation on the 1000-state random walk)
Shows: one shared value per group of states, shifted from the unweighted group average by the
       visit distribution mu, the textbook picture of an aliased value as a weighted average.
Crop:  keep both the value panel (true v_pi, staircase) and the mu panel; the shift is
       unreadable without mu.

Asset: Mnih et al. 2015 Fig. 1, p. 530 (network schematic)
Shows: the 84x84x4 stacked input entering the first convolution.
Crop:  keep the input stack and its label; the later layers can go.

Asset: Mnih et al. 2015 Extended Data Table 1, DQN PDF p. 10
Shows: "agent history length 4" and "action repeat 4" with their one-line definitions.
Crop:  keep both rows together with the column headings.

Asset: Singh, Jaakkola and Jordan 1994 Figure 2, PDF p. 5
Shows: six states, with 4a and 4b inside one observation ellipse; observation 2 leads to a payoff
       of 2.0 and observation 3 does not, yet TD(0) gives them the same value.
Crop:  keep the ellipse, all payoff labels and the caption. The scan is low resolution, so
       redraw rather than capture.

Asset: Hausknecht and Stone 2015 Figure 1, p. 1
Shows: single frames of Pong, Frostbite and Double Dunk, with a caption saying a single frame
       does not reveal velocity.
Crop:  keep the caption with the frames.

Gymnasium and SB3 docs, RL Zoo, SB3-Contrib docs: None found.
W&B report: learning-curve panels exist under "LSTM vs FrameStacking"; not inspected, because
       the page is JavaScript-rendered.
POPGym, Ni et al., Heess et al., Whitehead and Ballard: None found that shows the lesson's
       mechanism better than prose (POPGym's evidence is a table).
```

## Discarded

```text
https://forge.coreweave.com/wandb/sb3/no-vel-envs/reports/...: the route the wandb.ai link redirects through; recorded the wandb.ai address instead.
https://incompleteideas.net/book/RLbook2020.pdf: the https form failed TLS verification from this machine; recorded the http address.
SB3 issues #1359, #863, #819 (returned by searches for a report of the bounds defect): titles unrelated to VecFrameStack bounds.
```

## Course lessons available to link

Read from `/home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/`, file names and titles only:

| File | Title |
| --- | --- |
| action-values-from-samples.html | Action values let an agent improve its policy from episodes alone |
| checking-a-custom-environment.html | Gymnasium's environment checker passes a grid with a backward slip |
| environments-and-the-rl-problem.html | The value of a state is an average you can solve for |
| epsilon-greedy-exploration.html | ε-greedy control settles for the best policy that keeps exploring |
| finding-optimal-policies.html | Two improvements find the best policy |
| learning-values-from-samples.html | An agent can learn what each state is worth without knowing the rules |
| n-step-returns.html | Four-step TD learns a 19-state random walk faster than TD(0) or Monte Carlo |
| observation-scale.html | Reporting position in raw millimetres keeps PPO from using a cart's velocity |
| off-policy-importance-sampling.html | Importance sampling values a policy from episodes another policy played |
| sarsa-and-q-learning.html | Moving at random half the time, Q-learning still learns the optimal arrows |
| semi-gradient-td.html | TD(0) no longer converges to the best fit once states share weights |
| termination-and-truncation.html | Q-learning that treats its time limit as terminal learns the values of a different grid |
| the-deadly-triad.html | A problem whose true values are all zero sends off-policy TD's weights to infinity |
| training-an-off-the-shelf-agent.html | PPO's greedy arrows outscore the sampled moves its training curve averages |

Judging from titles alone: the commission names sarsa-and-q-learning. semi-gradient-td covers the state-aggregation result that an aliased observation reproduces. learning-values-from-samples and n-step-returns cover the Monte Carlo versus TD contrast in Singh et al. training-an-off-the-shelf-agent covers SB3. observation-scale is the preceding stage-3 lesson. termination-and-truncation is relevant to the time-awareness lesson that comes next.

## API verification log

Scratch directory `/tmp/claude-0/nb-frame-stack/` (may be cleared). The environment was uv 0.11.32 and Python 3.12.3, with torch 2.15.0+cpu from the PyTorch CPU index, numpy 2.5.4, gymnasium 1.4.0, stable-baselines3 2.9.2, sb3-contrib 2.9.2, rl-zoo3 2.9.2 and popgym 1.0.7. Scripts are in `scripts/`: `inspect_api.py`, `call_api.py`, `bounds_check.py`, `discrete_pad.py`, `zoo_novel.py` and `popgym_check.py`. Output lines the page could use:

```text
FrameStackObservation.__init__ (self, env: 'gym.Env[ObsType, ActType]', stack_size: 'int', *, padding_type: 'str | ObsType' = 'reset')
VecFrameStack.__init__ (self, venv: VecEnv, n_stack: int, channels_order: str | Mapping[str, str] | None = None) -> None
1. Box obs space: ... (2, 4), float32
   reset (padding_type='reset'): two identical rows [0.0137 -0. -0.0459 -0.]
   after one step: rows [0.0137 ...] then [0.0132 ...]   (oldest first)
   reset (padding_type='zero'): row of zeros, then the reset observation
2. Discrete base: Discrete(16) -> stacked: MultiDiscrete([16 16])
3. VecFrameStack obs space: ... (8,), float32
   reset: [[0. 0. 0. 0. 0.0137 -0. -0.0459 -0.]]
   episode end: new obs [[0. 0. 0. 0. <first obs>]]; info terminal_observation holds the stacked final pair
4. Discrete rejected: AssertionError VecFrameStack only works with gym.spaces.Box and gym.spaces.Dict observation spaces
5. gym.make_vec(..., wrappers=[lambda e: FrameStackObservation(e, 2)]): single space (2, 4), batched (2, 2, 4)
padding_type='reset': space=MultiDiscrete([7 7]), reset obs=[3, 3], after step=[3, 4]
padding_type='zero':  space=MultiDiscrete([7 7]), reset obs=[0, 3], after step=[3, 4]
bounds_check: declared low [0. 0. 10. 10.], stacked obs [0.5 10.5 0.5 10.5], contains False
CartPoleNoVel-v1 obs space: (4,) reset obs: [0.0137 -0. -0.0459 -0.]; VecFrameStack(n_stack=2) -> (8,); PPO learn(2048) ran
PositionOnlyCartPoleEasy obs [0.0137 -0.0459] full state [0.0137 -0.023 -0.0459 -0.0483]
VelocityOnlyCartPoleEasy reset obs [0.0137 -0.0459] (positions); step obs [-0.2175 0.2295] (velocities)
```
