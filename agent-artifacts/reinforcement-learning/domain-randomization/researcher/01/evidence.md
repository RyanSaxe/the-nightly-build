# Evidence: reinforcement-learning/domain-randomization (researcher 01)

The sources support the lesson's mechanism. Several papers show that a policy
trained over a physical-parameter range without seeing the parameter scores below
a policy that is given the parameter. The clearest cases are Yu et al. 2017
Fig. 2(b) and RMA's Table II. Peng et al. 2018 and OpenAI 2019 show that a
recurrent policy can recover the parameter from its history. Chen et al. 2022
formalize domain randomization as finding the optimal policy of a latent MDP
whose optimal policy generally needs memory. The evidence is thin or works
against the commission in three places. First, Tobin et al. 2017 does not fit
the commission's description of it. It trains a supervised object detector, not
an RL policy, and randomizes rendering, not physics. Its own related-work section
credits earlier physics-ensemble work and calls CAD2RL, an RL paper posted four
months earlier, the most similar work. Second, the cost of randomization is not
universal. EPOpt's hopper policy trained over torso masses matched each
single-mass specialist at that specialist's own mass (Fig. 1). The papers that
do show a cost show it concentrated at some parameter values, not at "any one
value". Third, history reveals the parameter only after some interaction: OpenAI's
probes are near chance at the start of an episode. Giving the policy the exact
parameter also did not help outside the training range in Yu et al. §IV.F. Every
cost measurement is from deep RL on continuous control with trained (not optimal)
blind policies. No source measures the cost against an exact per-value solve or
in a tabular setting, so the lesson's own runs carry that claim. Gymnasium 1.4.0
(5 Oct 2026) is the current release. The `reset(options=...)` pattern, TimeLimit,
RepeatAction and `check_env` behave as documented, and two checker behaviors
constrain how an environment draws its parameter (see the Gymnasium entries).

## Sources

### Introductions of the idea

```text
URL:         https://arxiv.org/abs/1703.06907
             (published version: IROS 2017, https://doi.org/10.1109/IROS.2017.8202133)
Kind:        primary. The authors (Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider,
             Wojciech Zaremba, Pieter Abbeel; OpenAI and UC Berkeley) define the
             technique and report their own experiments.
Establishes: firsthand: the definition and hypothesis of "domain randomization"
             as the title term, randomized rendering for a sim-to-real object
             detector, 1.5 cm real-world localization error, and 38 of 40 real
             grasps. It does not establish anything about RL policies or physical
             parameters. The detector is trained by supervised L2 regression, and a
             motion planner executes the grasp.
Paraphrase:  The authors train a modified VGG-16 to map one webcam image to an
             object's (x, y, z) using only MuJoCo renders. Each training sample
             randomizes distractor count and shape, object positions and textures,
             table/floor/skybox/robot textures, camera position, orientation and
             field of view, number and placement of lights, and image noise (§III.A).
             Textures are random RGB, gradients or checkers, deliberately not
             realistic. Their hypothesis is that if the simulation varies enough,
             the real world looks like one more variation (§I). On real images the
             detectors average about 1.5 cm error (Table I) against 0.3 to 0.5 cm
             on simulated data (§IV.B). With fewer than 1,000 unique textures,
             performance degrades significantly (Fig. 5). Removing distractors
             from training raises error with real distractors from 1.8 to 7.2 cm
             (Table II). Footnote 2 notes that no real-world validation is possible
             during training, so the target domain stays fully held out. §II.C
             credits physics randomization to earlier work (Mordatch et al. 2015,
             Antonova et al. 2017, Yu et al. 2017, Rajeswaran et al. 2016) and
             calls Sadeghi and Levine's CAD2RL "the most similar to our own".
Locators:    Abstract; §I (hypothesis, p.1-2); §II.C (prior randomization, p.3);
             §III.A (what is randomized, p.3); Table I (p.4); Fig. 5 (p.5);
             Table II and §IV.D grasping (p.6); Fig. 1 (p.1).
Quote:       "Instead of training a model on a single simulated environment, we
             randomize the simulator to expose the model to a wide range of
             environments at training time." (§I)
Quote:       "if the variability in simulation is significant enough, models trained
             in simulation will generalize to the real world with no additional
             training." (§I)
Quote:       "With enough variability in the simulator, the real world may appear to
             the model as just another variation." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1611.04201
             (published version: RSS 2017, https://doi.org/10.15607/RSS.2017.XIII.034)
Kind:        primary. Fereshteh Sadeghi (University of Washington) and Sergey Levine
             (UC Berkeley) report their own method and flights.
Establishes: firsthand: an RL-trained, vision-based collision-avoidance policy
             trained only on randomized renders and flown on real quadrotors. arXiv
             v1 is dated 13 Nov 2016, four months before Tobin et al. (20 Mar 2017).
             The paper does not use the phrase "domain randomization". It randomizes
             appearance and layout, not physical parameters.
Paraphrase:  A fully convolutional VGG16-based network maps one monocular RGB image
             to collision-probability Q-values over a 41 x 41 grid of flight
             directions. It is trained by a Monte Carlo policy-evaluation variant of
             fitted Q-iteration that rolls out every action from sampled states
             (§III.C). The training simulator has 24 hallways built from 12 floor
             plans, with wall textures drawn from a pool of about 200, randomly
             placed lights, and slightly randomized furniture (Appendix XI). In
             real hallway flights on Parrot Bebop drones it had 0.0366 collisions
             per metre in Cory Hall, against 0.080 for a perception-based baseline
             (Table I). On a real-image free-space proxy task, a network trained on
             randomized hallways beat networks trained on fixed textures and on a
             realistic reconstruction of a real hallway (Fig. 8, §V.C).
Locators:    Abstract; Fig. 2 (randomized renders, p.4); §III.C (p.3); Table I
             (p.7); §V.C and Fig. 8 (p.7-9); Appendix XI (p.12).
Quote:       "By highly randomizing the rendering settings for our simulated
             training set, we show that we can train a policy that generalizes to
             the real world, without requiring the simulator to be particularly
             realistic or high-fidelity." (Abstract)
```

```text
URL:         https://arxiv.org/abs/1710.06537
             (published version: ICRA 2018, https://doi.org/10.1109/ICRA.2018.8460528)
Kind:        primary. Xue Bin Peng, Marcin Andrychowicz, Wojciech Zaremba, Pieter
             Abbeel (OpenAI; UC Berkeley) report their own method and robot trials.
Establishes: firsthand: randomizing physical parameters per episode for an RL
             policy and transferring it to a real robot. Also that a memory-based
             policy beats a memoryless one under randomization, both in simulation
             and on the robot. This is the closest published match to the lesson's
             setup of one physical parameter drawn per episode.
Paraphrase:  A 7-DOF Fetch arm pushes a puck to a goal with a sparse reward. The
             policy is trained with RDPG and HER. At the start of each episode 95
             dynamics parameters are sampled and held fixed for the episode,
             including link masses, joint damping, puck mass, friction and damping,
             table height, and controller gains. Action timestep and observation
             noise vary every step (§IV.C; ranges in Table I). The objective is
             expected return under the parameter distribution (§IV, equation before
             §IV.A). The policy does not see the parameters. Only the "omniscient
             critic" does (§IV.E). §IV.D argues that the dynamics "can be inferred
             from a history of past states and actions", either explicitly
             (Yu et al.'s system identification) or implicitly by an LSTM. Table II:
             LSTM succeeds 0.91 in simulation and 0.89 on the real robot. A
             feedforward net (FF) scores 0.83 and 0.67. FF given the 8 previous
             states and actions scores 0.87 and 0.70. FF trained without
             randomization scores 0.51 and 0.0. Table III ablation: holding the
             action timestep fixed drops real success to 0.29, and holding puck
             friction fixed drops it to 0.48.
Locators:    §II.B (domain randomization lineage, p.2); §IV equation and §IV.C
             (p.4); §IV.D (p.4); §IV.E omniscient critic (p.4); Table I (p.5);
             §V.A, Table II, Fig. 7 (p.6-7); Table III (p.7).
Quote:       "At the start of each episode, a random set of dynamics parameters µ
             are sampled according to ρµ and held fixed for the duration of the
             episode." (§IV.C)
Quote:       "In the absence of direct knowledge of the parameters, the dynamics can
             be inferred from a history of past states and actions." (§IV.D)
```

```text
URL:         https://arxiv.org/abs/1610.01283
Kind:        primary. Aravind Rajeswaran, Sarvjeet Ghotra, Balaraman Ravindran,
             Sergey Levine report their own algorithm and experiments (ICLR 2017
             per the PDF header).
Establishes: firsthand: RL training over a distribution of physical parameters
             (torso mass, friction, damping, armature) predates Tobin and CAD2RL
             (arXiv Oct 2016). It also gives a measured case where a parameter-blind
             policy trained over the range lost no return against single-mass
             specialists. This is the main counter-evidence to a universal cost.
Paraphrase:  The authors define a parametrized family of MDPs M(p) and seek one
             policy that performs well for all p without knowing p (§2). EPOpt
             trains with TRPO on sampled models and, for ε < 1, updates only on the
             worst ε-fraction of trajectories, a CVaR objective (§3.1). On the
             hopper, TRPO policies trained at torso mass 3, 6 or 9 each collapse
             away from their own mass. The EPOpt(ε = 0.1) policy trained on a
             Gaussian over mass (mean 6, s.d. 1.5) scores about 3,300 across masses
             3 to 9, level with each specialist at its own mass (Fig. 1, read off
             the plot). The authors state that they saw no significant loss from
             requiring one policy to work on many models. §5 notes that earlier
             work treats uncertain model parameters as unobserved state in a POMDP.
Locators:    §1 (p.2); §2 problem formulation (p.2); §3.1; §4 experimental
             questions (p.5); §4.1 and Fig. 1 (p.5); §5 related work.
Quote:       "In our experiments, we did not observe significant loss in performance
             by requiring the policy to work on multiple models (for example,
             through adopting a more conservative strategy)." (§1)
Quote:       "Note that this robust policy does not have an explicit dependence on p,
             and we require it to perform well without knowledge of p." (§2)
```

### The cost of a hidden parameter, and exposing it

```text
URL:         https://arxiv.org/abs/1702.02453
             (published version: RSS 2017, https://doi.org/10.15607/RSS.2017.XIII.048)
Kind:        primary. Wenhao Yu, Jie Tan, C. Karen Liu, Greg Turk (Georgia Tech;
             Google Brain) report their own method and simulations.
Establishes: firsthand: a side-by-side curve of return against the physical
             parameter for a policy given the true parameter ("UP-true"), a policy
             trained over the same range without it ("Regular"), and one given an
             online estimate ("UP-OSI"). Also: a policy given the true parameter did
             worse than one given an estimate outside the training range.
Paraphrase:  The Universal Policy π(x, µ) takes the state and the dynamics parameters
             µ. It is trained by TRPO with µ drawn uniformly per rollout (§III.A,
             Algorithm 1). Online System Identification predicts µ from the last
             three states and actions (§III.B). On a double inverted pendulum whose
             lower pole's centre of mass is offset by µ in [-0.6, 0.6] m, Fig. 2(b)
             plots normalized reward, where above 1.0 means the pendulum balances.
             Read off the plot: UP-true sits near 1.2 and stays above 1.0 from about
             -0.47 to 0.45. Regular peaks near 1.15, is about 0.1 below UP-true at
             offset 0, and falls below 1.0 for offsets below about -0.22 and above
             about 0.36, reaching about 0.3 near ±0.5. §IV.A says the comparison
             shows that providing the parameters as input makes a more powerful
             policy over the range. §III.A reports that a small parameter change
             can need a "drastically different control policy". §IV.F tests the
             cart-pole 100% beyond its training range: UP-OSI significantly
             outperforms UP-true there. §V offers only a guess at why.
Locators:    §III.A (p.3); §IV.A and Fig. 2(b) (p.5-6); §IV.E, Fig. 4(d) (p.7);
             §IV.F, Fig. 5(d) (p.7); §V discussion.
Quote:       "The purpose of this comparison is to show that providing the model
             parameters as input to UP results in a more powerful control policy
             under a range of dynamic models" (§IV.A)
Quote:       "for many dynamic tasks, sometimes a small change in the model parameter
             requires a drastically different control policy to succeed at the given
             task." (§III.A)
Quote:       "UP-OSI significantly outperforms UP-true in this range of µ unseen
             during training." (§IV.F)
```

```text
URL:         https://arxiv.org/abs/2107.04034
             (published version: RSS 2021, https://doi.org/10.15607/RSS.2021.XVII.011)
Kind:        primary for its Table II numbers. Ashish Kumar (UC Berkeley), Zipeng Fu
             (CMU), Deepak Pathak (CMU), Jitendra Malik (UC Berkeley, Facebook)
             report their own simulations. Its one-sentence claim that domain
             randomization is "over conservative" is a citation of Luo and Hauser,
             which I did not open, so that sentence is a repetition.
Establishes: firsthand: in simulated A1 quadruped locomotion, a policy trained
             without the environment parameters ("Robust") succeeds 62.4% of the
             time, against 76.2% for one given the true extrinsics ("Expert") and
             73.5% for RMA's estimated extrinsics. Explicit parameter estimation
             ("SysID", 56.5%) did worse than Robust.
Paraphrase:  Robust is "trained without z_t to be robust to the variations in the
             training range". Expert uses the true extrinsics vector and is called
             an upper bound on RMA (§V baselines). In Table II, parameters are
             resampled within test episodes with probability 0.01 per step, which
             differs from a per-episode draw. Results average 3 policies x 1,000
             episodes. The authors attribute Robust's shortfall to its being
             "agnostic to extrinsics", so it "learns a very conservative policy"
             (§V.C).
Locators:    §II "Sim-to-Real Reinforcement Learning" (p.4); §V baselines and
             Table II (p.8); §V.C.
Quote:       "domain randomization trades optimality for robustness leading to an
             over conservative policy" (§II)
```

```text
URL:         https://arxiv.org/abs/2011.02404
             (published version: ICRA 2021, https://doi.org/10.1109/ICRA48506.2021.9560837)
Kind:        primary. Zhaoming Xie, Xingye Da, Michiel van de Panne, Buck Babich,
             Animesh Garg report their own Laikago experiments.
Establishes: firsthand: a measured conservatism cost and an argument against
             randomizing parameters that do not need it. Also that, for this robot,
             direct transfer worked without any dynamics randomization.
Paraphrase:  Trotting policies trained with dynamics randomization reach a maximum
             speed of 0.9 m/s, against 1.1 m/s without randomization, in
             simulation and on the robot (§VI.A). Randomizing latency up to 20 ms
             raised tolerated latency from 17 ms to 32 ms (§VI.B). The authors
             conclude that randomizing unneeded parameters produces conservative
             policies, while randomizing the parameter actually responsible for the
             gap helps (§VI.C).
Locators:    Abstract; §I contribution 3; §IV "Dynamic Randomization Is Not
             Necessary"; §VI.A-C (p.6); Table III.
Quote:       "unnecessary randomization of parameters can produce conservative
             policies with limited actual gains in robustness" (§I)
```

```text
URL:         https://arxiv.org/abs/2110.03239
             (ICLR 2022; listing at https://iclr.cc/virtual/2022/poster/6876)
Kind:        primary. Xiaoyu Chen, Jiachen Hu (Peking University), Lihong Li
             (Amazon), Chi Jin (Princeton), Liwei Wang (Peking University) state and
             prove their own theorems.
Establishes: firsthand: the hidden-context formalization. A domain-randomized
             simulator is a latent MDP (a POMDP in which one MDP is drawn at the
             start of each episode and not revealed). Domain randomization is
             modeled as returning that latent MDP's optimal history-dependent
             policy. Without memory, the policy cannot identify the environment,
             and its worst-case loss stays linear in the horizon.
Paraphrase:  The sim-to-real gap is the optimal value in the real MDP minus the
             learned policy's value there (§4.1, Eq. 1). This is the lesson's
             "return given up at one parameter value" measured against the per-value
             optimum. Definition 1 (Eq. 2) defines the domain-randomization oracle
             as the policy maximizing E over MDPs ~ ν of V. The authors note that
             the latent MDP's optimal policy generally depends on history, unlike an
             MDP's (§4.2). After Theorem 2 they argue that randomization and memory
             are both needed for a sublinear gap. §3.2 describes practice:
             randomize per episode, and use an LSTM so the policy can identify the
             current environment.
Locators:    Abstract; §3.2 (p.4); §4.1 Eq. 1 (p.4); §4.2 and Definition 1 (p.5);
             discussion after Theorem 2 (p.6).
Quote:       "Without memory, the policy is not able to implicitly 'identify' the
             environments, so it cannot achieve sublinear loss in the worst case."
             (after Theorem 2)
Quote:       "Since LMDP is a special case of POMDPs, its optimal policy π*_DR in
             general will depend on history. This is in sharp contrast with the
             optimal policy of a MDP, which is history-independent." (§4.2)
```

```text
URL:         https://arxiv.org/abs/1910.07113
Kind:        primary. OpenAI (Ilge Akkaya et al., authors listed alphabetically;
             the paper asks to be cited as "OpenAI et al.") report their own
             system and experiments.
Establishes: firsthand: automatic domain randomization (ADR), and evidence that a
             recurrent policy trained under randomization stores the environment
             parameters in its state over the course of an episode. Also that this
             takes time, since prediction is near chance at the start.
Paraphrase:  ADR starts from a single calibrated environment and widens each
             parameter's range while performance stays above a threshold (§5.1,
             Fig. 10, algorithm in §5.2). The authors hypothesize that a
             distribution too wide for the model to memorize per-environment
             solutions forces it to learn in context (§5). §9 defines this
             "meta-learning" as learning the dynamics of the current MDP, which they
             say is also called online system identification (§9.1). After a
             hidden-state reset, time per cube flip spikes and then falls again
             (Fig. 18). The policy converges to about 4 s per flip, about 1.6 s
             faster than the first flip (§9.2). Probes of the LSTM state predict
             whether cube size, time step, gravity or cube mass is above average.
             Accuracy is near chance at the start of a rollout and exceeds 80% for
             some parameters later. Cube mass reaches only 50 to 60% (§9.3.1,
             Table 7, Fig. 19).
Locators:    Abstract; §5 and §5.1, Fig. 10 (p.10); §5.2; §9.1 (p.24); §9.2 and
             Fig. 18 (p.25-26); §9.3, Table 7 (p.27); Fig. 19 (p.28).
Quote:       "In other words, when we say 'meta-learning', what we really mean is
             learning to learn about the environment dynamics. Within other
             communities, this is also called on-line system identification."
             (§9.1)
```

```text
URL:         https://doi.org/10.1613/jair.1.14174 (arXiv: https://arxiv.org/abs/2111.09794)
Kind:        secondary for who introduced domain randomization: a survey by Robert
             Kirk, Amy Zhang, Edward Grefenstette, Tim Rocktäschel, outside the
             originating papers. Primary for its own definitions. Already cited by
             the held-out-levels lesson (§3.3).
Establishes: firsthand: the contextual-MDP definition with the context either
             observed or unobserved. Repeats: an attribution of domain randomization
             to Tobin et al., Sadeghi and Levine, and Peng et al. jointly.
Paraphrase:  A CMDP is a POMDP whose state includes a context fixed within an
             episode. The CMDP is an MDP only if the context is observed (§3.3,
             Definition 1). Hidden-parameter MDPs (Doshi-Velez and Konidaris 2016)
             are the special case where a hidden parameter controls the transitions
             (§3.7). For sim-to-real, the context could be made observable in
             simulation but not at test time, so a policy conditioned on it "may not
             be useful" (§3.5). Domain randomization is "just the creation of a
             non-singleton training context set" (§5.1.1). Context-inference methods
             such as UP-OSI and RMA are listed under online adaptation (§5.2.4).
Locators:    §3.3 Definition 1 (p.208); §3.5 sim-to-real bullet (p.211); §3.7
             (p.215); §5.1.1 (p.227-228); §5.2.4 (p.233-234), JAIR pagination.
Quote:       "Tobin et al. (2017), Sadeghi and Levine (2017) and Peng et al. (2018)
             introduced this idea in the setting of sim-to-real transfer in
             robotics." (§5.1.1)
Quote:       "The context needs to be observed for the CMDP to be an MDP (and not a
             POMDP)" (§3.3)
```

### Gymnasium, November 2026

```text
URL:         https://pypi.org/project/gymnasium/1.4.0/
             (release notes: https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.4.0)
Kind:        primary. The Farama Foundation's own package index entry and release
             notes.
Establishes: firsthand: 1.4.0 is the latest release (uploaded 2026-10-05,
             requires Python >= 3.10). 1.3.0 was released 2026-04-22. The 1.4.0
             notes list no change to Env.reset options, TimeLimit or RepeatAction.
             They do list env-checker changes: a new check that reset and step
             return distinct observation and info objects each step, determinism
             checks that snapshot reused observations, and comparison of the RNG
             state in check_step_determinism.
Paraphrase:  As above. No 1.4.x patch release exists as of 23 Nov 2026 (PyPI JSON).
Locators:    PyPI release history; GitHub release v1.4.0, "Bug fixes" and env
             checker entries.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/env/#gymnasium.Env.reset
Kind:        primary. Farama's API documentation for the version the lesson pins.
Establishes: firsthand: the reset signature and the meaning of seed and options.
Paraphrase:  `Env.reset(*, seed: int | None = None, options: dict[str, Any] | None = None)`
             returns (observation, info). options is "Additional information to
             specify how the environment is reset (optional, depending on the
             specific environment)". A custom environment's first line of reset
             should be `super().reset(seed=seed)`. Passing an integer seed resets
             the PRNG np_random, and seed=None leaves an existing PRNG alone. As
             of 23 Nov 2026 the /v1.4.0/ page is byte-identical to the unversioned
             page, while /v1.3.0/ differs.
Locators:    Env.reset entry; Env.np_random entry.
Quote:       "For Custom environments, the first line of reset() should be
             super().reset(seed=seed) which implements the seeding correctly."
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/misc_wrappers/#gymnasium.wrappers.TimeLimit
Kind:        primary. Farama's API documentation.
Establishes: firsthand: TimeLimit(env, max_episode_steps) issues truncated=True
             once elapsed >= max_episode_steps, separate from terminated. gym.make
             adds it from the spec's max_episode_steps. Change log: v0.10.6 added,
             v0.25.0 separated termination and truncation.
Paraphrase:  Confirmed by running 1.4.0: TimeLimit counts calls to its own step.
             TimeLimit(RepeatAction(env, 3), 5) truncates after 5 decisions, which
             is 15 inner steps. RepeatAction(TimeLimit(env, 5), 3) truncates after
             5 inner steps, so the second decision stops early. Wrapper order
             therefore decides whether the limit counts decisions or physics steps.
Locators:    TimeLimit entry, "Parameters" (max_episode_steps).
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/action_wrappers/#gymnasium.wrappers.RepeatAction
Kind:        primary. Farama's API documentation. Already cited by the
             action-frequency lesson.
Establishes: firsthand: RepeatAction(env, num_repeats) repeats the action, sums the
             rewards, returns the last observation, and stops early on terminated
             or truncated. It has no vector version. Change log: v1.3.0 added.
Paraphrase:  The 1.4.0 source matches: it sums float(reward) without discounting
             and breaks on terminated or truncated. RepeatAction does not override
             reset, so `reset(options=...)` passes through it to the environment.
             Verified by running 1.4.0: an options dict passed to
             TimeLimit(RepeatAction(env)) reaches the environment's reset.
Locators:    RepeatAction entry and its "Change logs".
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/utils/#gymnasium.utils.env_checker.check_env
             (source at tag: https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/env_checker.py)
Kind:        primary. Farama's documentation and source.
Establishes: firsthand: check_env(env, warn=None, skip_render_check=False,
             skip_close_check=False) checks the spaces and calls reset, step and
             render "with a variety of values". In the source,
             check_reset_options calls `env.reset(options={})`. check_step_determinism
             resets with seed 123 twice, steps the same action, and asserts equal
             observations and rewards. It runs even when env.spec is None, that is,
             for an environment constructed directly. check_reset_seed_determinism
             compares reset observations only when the environment has a spec.
Paraphrase:  Two consequences for an environment that draws a physical parameter
             in reset, verified by running 1.4.0 on a small cart. (1) A parameter
             drawn from self.np_random passes, with the parameter observed or not.
             A parameter drawn from a separate generator fails with "Deterministic
             step observations are not equivalent for the same seed and action".
             The first step's speed depends on the parameter, so the check catches
             the different draw. (2) A reset that reads options["mass"] whenever
             options is not None raises KeyError: 'mass' inside check_env, because
             the checker passes an empty dict. The pattern `if options:`, used by
             Dock in the action-frequency lesson, or `options.get(...)` passes.
Locators:    check_env entry; source functions check_reset_options,
             check_reset_seed_determinism, check_step_determinism,
             check_returned_data_not_reused.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/observation_wrappers/#gymnasium.wrappers.FrameStackObservation
Kind:        primary. Farama's API documentation.
Establishes: firsthand: FrameStackObservation(env, stack_size, *, padding_type="reset")
             stacks the last N observations. The default padding repeats the reset
             observation. Renamed and given padding_type in v1.0.0. Relevant only if
             the lesson gives the agent history instead of the parameter.
Locators:    FrameStackObservation entry.
```

## Contradictions

- **Commission vs Tobin et al. on what Tobin introduced.** The commission calls
  Tobin et al. 2017 "the paper that introduced domain randomization for RL
  transfer". Tobin et al. train a supervised object detector, and a motion
  planner executes the grasps (§III, §IV.D). They randomize rendering, not
  physics (§III.A). Their §II.C credits physics-ensemble training to Mordatch et
  al. 2015 and others, and names CAD2RL (an RL policy, arXiv 13 Nov 2016) as the
  most similar prior work. EPOpt (arXiv Oct 2016) trained RL policies over
  physical-parameter distributions earlier still. Kirk et al. §5.1.1 credits
  Tobin, Sadeghi and Levine, and Peng et al. jointly. The defensible wording:
  Tobin et al. named and defined domain randomization, and CAD2RL first trained
  an RL policy on randomized simulation and flew it in the real world. Peng et
  al. 2018 is the RL paper that randomizes physical parameters per episode and
  transfers the policy to a robot, which is what the lesson builds.
- **EPOpt vs the commission's cost claim.** The commission says the best blind
  policy "gives up return at any one value to avoid failing at others". EPOpt
  Fig. 1 shows a blind policy over hopper torso masses 3 to 9 matching each
  specialist at its own mass. The authors say they "did not observe significant
  loss". EPOpt uses a CVaR (worst ε) objective, not plain averaging. A cost
  appears only where the per-value optimal policies disagree on states the agent
  visits. That is a judgment from the contrasting cases (Yu et al. §III.A's
  "drastically different control policy"), not a sourced theorem. The commission's
  docking-speed rule is the kind of rule that creates such disagreement.
- **Where the cost falls (Yu et al. Fig. 2(b), RMA Table II, Xie et al. §VI.A).**
  In Yu et al. the parameter-blind policy loses about 0.1 normalized reward at
  the centre and fails outright (below 1.0) beyond about -0.22 and 0.36. The loss
  is concentrated at the ends rather than spread evenly. All three blind
  policies are trained deep-RL policies, not optimal blind policies, so their
  shortfall mixes the cost of not knowing the parameter with optimization
  failure. None of the papers separates the two. An exact solve, as the lesson
  plans, can.
- **History reveals the parameter only over time.** The commission says exposing
  the parameter "or history that reveals it" removes the cost. OpenAI §9.3 shows
  probes of the LSTM state near chance at the start of a rollout. §9.2 shows the
  first cube flip takes about 1.6 s longer than later ones. Peng et al. Table II
  shows history narrowing but not closing the gap on the real robot: FF + 8-step
  history scores 0.70 against the LSTM's 0.89. In those papers, history removes
  the cost only after enough of the episode has passed to identify the
  parameter.
- **Exposing the exact parameter does not help outside the training range.** Yu
  et al. §IV.F: 100% beyond the cart-pole's training range, the policy given the
  true parameter does significantly worse than the one given OSI's estimate.
  This bears on the held-out-range test the commission plans. A policy
  conditioned on the parameter has no training at unseen values.
- **Exposing an estimated parameter can do worse than not exposing it.** RMA
  Table II: SysID, which predicts the physical parameters explicitly, scores
  56.5% success against 62.4% for the blind Robust policy.
- **Is randomization needed at all?** Xie et al. §IV found direct sim-to-real
  transfer for Laikago without dynamics randomization. They argue for randomizing
  only the parameters responsible for the reality gap. This matters only for the
  one-sentence sim-to-real mention.
- **Kirk et al. §3.5 vs the lesson's remedy.** The context "won't be observable
  at testing time" in sim-to-real, so a context-conditioned policy "may not be
  useful". In the lesson's simulated Dock the parameter can be observed. The
  remedy of observing it applies to simulation, and to the real world only
  through estimation (UP-OSI, RMA) or memory (Peng, OpenAI).

## Numbers

```text
Figure: 1.5 cm average real-world localization error (per-object, per-condition means 0.6 to 3.2 cm)
Owner:  Tobin et al. 2017, Table I and §IV.B
Scope:  480 real webcam images, 8 geometric objects, 60 images each; objects 70 to 105 cm from camera

Figure: 0.3 to 0.5 cm error on simulated data
Owner:  Tobin et al. 2017, §IV.B
Scope:  same detectors, simulated test images

Figure: 38 of 40 real grasps; 9 of 10 for a Spam can among unseen YCB distractors
Owner:  Tobin et al. 2017, §IV.D
Scope:  Fetch robot, two most accurate detectors, 20 increasingly cluttered scenes each

Figure: error with real distractors 1.8 ± 1.7 cm (full method) vs 7.2 ± 4.5 cm (no distractors in training)
Owner:  Tobin et al. 2017, Table II
Scope:  models trained on 20,000 examples; occlusion column 2.4 ± 3.0 vs 7.4 ± 5.3 cm

Figure: 0.0366 vs 0.080 collisions per metre (CAD2RL vs FS-pred), Cory Hall; 0.072 vs 0.130 in SDH
Owner:  Sadeghi and Levine 2017, Table I
Scope:  real hallway-following flights, about 163 m (Cory) and 54 m (SDH) per method

Figure: real-robot pushing success LSTM 0.89 ± 0.06 (28 trials), FF 0.67 ± 0.14 (12), FF + Hist 0.70 ± 0.10 (20), FF no Rand 0.0 ± 0.0 (10)
Owner:  Peng et al. 2018, Table II
Scope:  Fetch arm, puck pushing; simulation column over 100 episodes with random dynamics: 0.91, 0.83, 0.87, 0.51

Figure: 95 randomized dynamics parameters, drawn at episode start (mass, damping, friction, gains held fixed per episode)
Owner:  Peng et al. 2018, §IV.C
Scope:  per episode of 100 control steps (about 4 s)

Figure: real success with one randomization removed: all 0.89; fixed action timestep 0.29; no observation noise 0.25; fixed link mass 0.64; fixed puck friction 0.48
Owner:  Peng et al. 2018, Table III
Scope:  LSTM policies on the real robot; 28, 17, 12, 22, 27 trials

Figure: success rate Robust 62.4%, SysID 56.5%, RMA 73.5%, Expert 76.2%
Owner:  Kumar et al. 2021 (RMA), Table II
Scope:  simulated A1, 3 policies x 1,000 episodes each; parameters resampled within test episodes at 0.01 per step

Figure: maximum trotting speed 0.9 m/s with dynamics randomization vs 1.1 m/s without
Owner:  Xie et al. 2021, §VI.A
Scope:  Laikago trotting policy, both in simulation and on the robot

Figure: tolerated latency 17 ms without randomization vs 32 ms with latency randomized up to 20 ms
Owner:  Xie et al. 2021, §VI.B
Scope:  Laikago, simulation and robot

Figure: normalized reward vs centre-of-mass offset (read off the plot, approximate): UP-true about 1.2 and above 1.0 from about -0.47 to 0.45 m; Regular peak about 1.15, below 1.0 outside about [-0.22, 0.36] m, about 0.3 near ±0.5 m
Owner:  Yu et al. 2017, Fig. 2(b)
Scope:  double inverted pendulum, training range µ in [-0.6, 0.6] m, 20 rollouts per µ; above 1.0 means the pendulum balances

Figure: hopper return about 3,300 for EPOpt(ε = 0.1) across torso mass 3 to 9 (read off the plot); single-mass TRPO specialists about 3,200 to 3,300 at their own mass, falling below about 1,000 away from it
Owner:  Rajeswaran et al. 2017 (EPOpt), Fig. 1
Scope:  source distribution for EPOpt: Gaussian torso mass, mean 6, s.d. 1.5; shading shows 10th to 90th percentiles

Figure: LSTM-state probe accuracy near chance at rollout start, over 80% for some parameters later, 50 to 60% for cube mass
Owner:  OpenAI 2019, §9.3.1, Fig. 19
Scope:  probe times t in {1, 30, 60, 120} steps of 0.08 s; parameters cube size, time step, gravity, cube mass (Table 7 ranges)

Figure: about 4 s per cube flip after adaptation, about 1.6 s faster than the first flip
Owner:  OpenAI 2019, §9.2, Fig. 18
Scope:  10,000 simulated trials run to 50 flips

Figure: Gymnasium 1.4.0 uploaded 2026-10-05; 1.3.0 on 2026-04-22; requires Python >= 3.10
Owner:  PyPI, gymnasium release history
Scope:  as of 23 Nov 2026, 1.4.0 is the latest
```

## Limits

- No single paper "introduced domain randomization for RL transfer". The
  sources support only the split attribution in Contradictions. Choosing which
  to call the introduction is the writer's judgment.
- No source measures the cost of a hidden parameter against an exact per-value
  optimum, or in a tabular setting. Every cost figure comes from a trained deep-RL
  blind policy, so it mixes the cost with optimization error. The lesson's runs
  must carry the quantitative claim.
- No source states "the best single policy for the mixture" for memoryless
  policies as a theorem. Chen et al.'s Definition 1 is the closest formal
  statement, and it is over history-dependent policies. For a memoryless policy
  the statement is the writer's derivation.
- The Yu et al. Fig. 2(b) and EPOpt Fig. 1 values are read off plots and are
  approximate. Neither paper tabulates them.
- I did not open Mordatch et al. 2015 (Ensemble-CIO), Antonova et al. 2017,
  Luo and Hauser (cited by RMA for "over conservative"), Hallak et al. 2015
  (contextual MDPs) or Doshi-Velez and Konidaris 2016 (hidden-parameter MDPs).
  Anything said about them here repeats Tobin §II.C, Peng §II.B, RMA §II or
  Kirk §3.7.
- The /v1.4.0/ Gymnasium documentation path matches the unversioned pages as of
  23 Nov 2026. The unversioned pages will change at the next release, so cite
  the /v1.4.0/ addresses.
- Gymnasium 1.4.0 has no domain-randomization wrapper (its wrapper list has none).
  The per-episode draw has to live in the environment's reset, as in Peng et
  al. §IV.C.

## Source assets

```text
Asset: Yu et al. 2017, Fig. 2(b), p.6: reward against centre-of-mass offset for UP-true (green), Regular (blue), UP-OSI (red)
Shows: a policy trained over the range without the parameter falls below a policy given it, slightly at the centre and sharply at the ends, and an estimate from three steps of history nearly recovers the gap
Crop:  keep panel (b) alone with its axes, legend and the caption's sentence for (b); omit panels (a), (c), (d)
```

```text
Asset: Rajeswaran et al. 2017 (EPOpt), Fig. 1, p.5: four panels of hopper return against torso mass for TRPO at m = 3, 6, 9 and the EPOpt ensemble
Shows: specialists trained at one mass fail away from it, and a policy trained over the range holds its return across masses 3 to 9 with no visible loss at any one mass, the counter-case to a universal cost
Crop:  keep all four panels with the shared y-axis and the caption's first two sentences; the panels only make the point side by side
```

```text
Asset: OpenAI 2019, Fig. 19, p.28: probe accuracy for environment parameters against time step in the episode
Shows: a recurrent policy's state comes to encode physical parameters only as the episode proceeds, which is the time cost of identifying the parameter from history
Crop:  keep panel (b) (Rubik's cube) or both panels with the legend; omit nothing from the axes
```

```text
Asset: Tobin et al. 2017, Fig. 1, p.1: grid of randomized training renders beside a real test image
Shows: what randomized rendering looks like, for the one-sentence history or sim-to-real mention
Crop:  keep the training grid, the arrow and the real test image with their labels
```

```text
Asset: Peng et al. 2018, Table II, p.7 (and Fig. 7, the same data as bars)
Shows: memory and history help a randomized policy transfer, and no randomization fails on the robot
Crop:  keep the whole table with its caption; a table is better quoted as numbers than captured
```

```text
Asset: Sadeghi and Levine 2017, Fig. 2, p.4: randomized hallway renders
Shows: CAD2RL's randomized textures, lighting and furniture
Crop:  keep the image grid and caption
```

- RMA (Kumar et al. 2021): None found beyond Table II, which is better quoted as
  numbers.
- Xie et al. 2021: None found. The speed figures are in the text.
- Chen et al. 2022: None found (theory, no figures).
- Kirk et al. 2023: None found for this lesson.
- Gymnasium documentation and release notes: None found.

## Discarded

```text
https://iclr.cc/virtual/2022/poster/6876: used only to confirm Chen et al.'s ICLR 2022 venue; the arXiv page holds the text
https://gymnasium.farama.org/main/api/env/: development docs, which differ from the 1.4.0 release pages; not the version the lesson pins
https://gymnasium.farama.org/v1.3.0/api/env/: superseded version; checked only to confirm that /v1.4.0/ is a distinct build
```
