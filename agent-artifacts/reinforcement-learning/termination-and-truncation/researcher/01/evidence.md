# Evidence: reinforcement-learning/termination-and-truncation (researcher 01)

The sources support the commission's idea, with two qualifications the page has to carry. Gymnasium 1.4.0 is the current release on PyPI (uploaded 5 October 2026). Its documented `step` contract defines `terminated` as reaching a terminal state of the MDP and `truncated` as a condition outside the MDP, typically a time limit. Its "Handling Time Limits" tutorial says to bootstrap after truncation and not after termination. Pardo, Tavakoli, Levdik and Kormushev (ICML 2018) derive the same target as partial-episode bootstrapping, their Eq. (6) on p. 4050. Sutton and Barto give the terminal state a value of zero (p. 58) and initialise Q(terminal, ·) = 0 in the Q-learning box (p. 131). A uv run against gymnasium 1.4.0 confirmed every documented behaviour recorded below. The first qualification is that a time limit counts as truncation only when it is outside the task. Gymnasium's own tutorial and Pardo's case (i) both treat a limit that belongs to the task as a termination, with the remaining time added to the observation. The second is that both flags can be True on the same step: the run returned `terminated=True, truncated=True` when the goal was reached on the limit's last step. A correct target must therefore test `terminated` alone. The record is thin in one place. No source measures what treating the time limit as terminal does to values on the course's own grid. Pardo's tabular evidence comes from a different, deterministic grid with T = 3. The course's code also already has a time limit (`CAP = 200`), and its Q-learning code already bootstraps through that limit. So the commission's statement that the course "has never mentioned ... time limits" is wrong, and the faulty variant has to be written on purpose.

## Sources

### PyPI: gymnasium project page

```text
URL:         https://pypi.org/project/gymnasium/   (release page: https://pypi.org/project/gymnasium/1.4.0/)
Kind:        primary. The Farama Foundation publishes the package here, and the upload record is the index's own.
Establishes: firsthand: the latest version is 1.4.0, uploaded 2026-10-05T11:02:14Z; requires-python >=3.10; core dependency numpy>=1.22.0. Previous release 1.3.0, uploaded 2026-04-22.
Paraphrase:  The index lists 1.4.0 as the newest gymnasium release. Its install requirements are Python 3.10 or later, numpy 1.22 or later, cloudpickle, typing-extensions and farama-notifications. No 1.4.x patch release follows it.
Locators:    project page "Release history"; read through the index's JSON view of the same record (https://pypi.org/pypi/gymnasium/json), fields info.version, info.requires_python, info.requires_dist, releases["1.4.0"][0].upload_time_iso_8601
Quote:       none needed
```

### Gymnasium release notes, v1.4.0

```text
URL:         https://gymnasium.farama.org/v1.4.0/gymnasium_release_notes/#release-v1-4-0
Kind:        primary. Release notes written by the Gymnasium maintainers (Farama Foundation) for their own release.
Establishes: firsthand: v1.4.0 "Released on 2026-10-05". None of its changes alters what Env.step, Env.reset or TimeLimit return. One new check bears on writing an Env: "The environment checkers (check_env and the passive checker run by make) now verify that reset and step return distinct observation and info objects each timestep" (#1683). One bug fix touches Discrete: Discrete.contains now returns False for integers outside the dtype range instead of raising OverflowError (#1648, #1663).
Paraphrase:  The release adds max_concurrency to AsyncVectorEnv, Dict/Tuple node and edge spaces for Graph, sort_keys for Dict and generic vector-env typing, plus bug fixes in spaces, wrappers, vector envs and MuJoCo rendering. The checker change means an env that hands back the same info dict on every call now gets a warning under gymnasium.make.
Locators:    section "v1.4.0", subsections "New Features" (fifth bullet) and "Bug Fixes > Spaces" (first bullet)
Quote:       "verify that reset and step return distinct observation and info objects each timestep"
```

### Gymnasium API: Env.step and Env.reset

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/env/#gymnasium.Env.step
             https://gymnasium.farama.org/v1.4.0/api/env/#gymnasium.Env.reset
             (the unversioned https://gymnasium.farama.org/api/env/ currently serves identical text; the versioned URL stays fixed to 1.4.0)
Kind:        primary. The maintainers' API reference, generated from the 1.4.0 docstrings.
Establishes: firsthand: the signatures and the meaning of each return value.
Paraphrase:  Env.step(action) returns (observation, reward, terminated, truncated, info).
             terminated: the agent reached a terminal state as defined by the task's MDP, for example the goal or the lava in Sutton and Barto's gridworld. truncated: a truncation condition outside the MDP, typically a time limit, that can end the episode before a terminal state. If either is True the user must call reset().
             The info entry notes that Gym before v26 put "TimeLimit.truncated" in info, now deprecated. The deprecated done flag was removed "in OpenAI Gym v26".
             Env.reset(*, seed=None, options=None) returns (observation, info). A custom env's reset should begin with super().reset(seed=seed), which seeds self.np_random. Passing seed=None to an env that already has an RNG does not reset that RNG. The docs advise seeding once, right after construction.
             Both methods must return new observation and info objects on each call, not a mutated buffer, and check_env checks this.
Locators:    #gymnasium.Env.step: signature line, "Changed in version 0.26" box, Returns list (terminated, truncated, info, done), Note below; #gymnasium.Env.reset: signature, seed parameter, Note below
Quote:       step signature: "Env.step(action: ActType) → tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]"
             "Changed in version 0.26: The Step API was changed removing done in favor of terminated and truncated to make it clearer to users when the environment had terminated or truncated which is critical for reinforcement learning bootstrapping algorithms."
             "terminated (bool) – Whether the agent reaches the terminal state (as defined under the MDP of the task) which can be positive or negative."
             "truncated (bool) – Whether the truncation condition outside the scope of the MDP is satisfied. Typically, this is a timelimit, but could also be used to indicate an agent physically going out of bounds."
             reset signature: "Env.reset(*, seed: int | None = None, options: dict[str, Any] | None = None) → tuple[ObsType, dict[str, Any]]"
             "For Custom environments, the first line of reset() should be super().reset(seed=seed) which implements the seeding correctly."
```

### Gymnasium API: Discrete space

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/spaces/fundamental/#gymnasium.spaces.Discrete
Kind:        primary. Maintainers' API reference.
Establishes: firsthand: Discrete(n, seed=None, start=0, dtype=np.int64) is the set {start, ..., start + n - 1}. sample() returns a NumPy integer of the space's dtype and accepts an optional mask or probability vector.
Paraphrase:  A grid of 16 cells and 4 moves is observation_space = Discrete(16), action_space = Discrete(4), with elements 0..15 and 0..3. The Env class docs (same page as Env.step, #gymnasium.Env.action_space) show Discrete(2) meaning actions 0 and 1.
Locators:    #gymnasium.spaces.Discrete (class signature, Example, Parameters); #gymnasium.spaces.Discrete.sample
Quote:       "This class represents a finite subset of integers, more specifically a set of the form {a, a+1, ..., a+n-1}."
```

### Gymnasium API: TimeLimit wrapper

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/misc_wrappers/#gymnasium.wrappers.TimeLimit
             source view: https://gymnasium.farama.org/v1.4.0/_modules/gymnasium/wrappers/common/#TimeLimit
Kind:        primary. Maintainers' reference and their published source.
Establishes: firsthand: TimeLimit(env, max_episode_steps) sets truncated=True when elapsed >= max_episode_steps. It never changes terminated. It is the only place a truncation signal is issued if the env defines none itself. The separate termination and truncation signals date from v0.25.0. No vector version exists.
Paraphrase:  The wrapper counts steps since the last reset. On the step where the count reaches max_episode_steps it forces truncated to True, so an episode has at most max_episode_steps transitions. The documented CartPole example with max_episode_steps=3 prints (False, False), (False, False), (False, True).
             Source (gymnasium/wrappers/common.py, 1.4.0), TimeLimit.step:
                 observation, reward, terminated, truncated, info = self.env.step(action)
                 self._elapsed_steps += 1
                 if self._elapsed_steps >= self._max_episode_steps:
                     truncated = True
                 return observation, reward, terminated, truncated, info
Locators:    class docstring paragraphs 1-2; "Example of TimeLimit determining the episode step"; "Change logs"; Parameters
Quote:       "If a truncation is not defined inside the environment itself, this is the only place that the truncation signal is issued. Critically, this is different from the terminated signal that originates from the underlying environment as part of the MDP."
             "max_episode_steps – the environment step after which the episode is truncated (elapsed >= max_episode_steps)"
```

### Gymnasium API: make, register, EnvSpec

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/registry/#gymnasium.make
             https://gymnasium.farama.org/v1.4.0/api/registry/#gymnasium.register
             https://gymnasium.farama.org/v1.4.0/api/registry/#gymnasium.envs.registration.EnvSpec
Kind:        primary. Maintainers' reference.
Establishes: firsthand: how max_episode_steps reaches TimeLimit.
Paraphrase:  gymnasium.register(id, entry_point, ..., max_episode_steps=None, ...) stores max_episode_steps in the EnvSpec. "Used by the gymnasium.wrappers.TimeLimit wrapper if not None." gymnasium.make(id, max_episode_steps=None, disable_env_checker=None, **kwargs) overrides the registered value "with the value being passed to gymnasium.wrappers.TimeLimit", and max_episode_steps=-1 skips the wrapper. kwargs go to the env constructor. make also adds PassiveEnvChecker unless disabled, and OrderEnforcing if order_enforce is True (the default).
Locators:    #gymnasium.make Parameters (max_episode_steps, disable_env_checker, kwargs); #gymnasium.register Parameters (max_episode_steps, order_enforce, disable_env_checker); #gymnasium.envs.registration.EnvSpec field list
Quote:       "max_episode_steps – Maximum length of an episode, can override the registered EnvSpec max_episode_steps with the value being passed to gymnasium.wrappers.TimeLimit. Using max_episode_steps=-1 will not apply the wrapper to the environment."
```

### Gymnasium tutorial: Handling Time Limits

```text
URL:         https://gymnasium.farama.org/v1.4.0/tutorials/gymnasium_basics/handling_time_limits/
             anchors: #termination, #truncation, #importance-in-learning-code, #solution
Kind:        primary. The maintainers' own statement of how their flags should be used in learning code. The page states "This tutorial is compatible with Gymnasium version 1.4.0."
Establishes: firsthand: the documented rule for the TD target, and that a time limit inherent to a finite-horizon task is a termination, not a truncation.
Paraphrase:  Termination is the end of an episode at a terminal state defined by the environment, including the end of a finite-horizon task at a time limit that belongs to the task. For such a task the remaining time must be in the observation to keep the Markov property. Truncation is an end imposed by a condition outside the MDP, such as a practical time limit on an infinite-horizon task. The last state then is not terminal, because it can still move to other states.
             The Q-learning target bootstraps, r + γ max_a Q(o_{t+1}, a). At a terminal state it is r alone. Using the old done flag in (1 - done) is wrong at truncations. The correct form uses (1 - terminated). Before v0.26 the truncation information came in the info key TimeLimit.truncated. The "(Reference)" link on the page goes to Pardo et al., https://arxiv.org/abs/1712.00378.
Locators:    #termination (whole subsection), #truncation (whole subsection), #importance-in-learning-code (two formulas and the INCORRECT block), #solution (code block)
Quote:       "This is where the distinction between termination and truncation becomes important. When an episode ends due to termination we don't bootstrap, when it ends due to truncation, we bootstrap."
             "Notably, this also includes episodes ending in finite-horizon environments due to a time-limit inherent to the environment. Note that to preserve Markov property, a representation of the remaining time must be present in the agent's observation in finite-horizon environments."
             "vf_target = rew + gamma * (1 - terminated) * vf_next_state"
             "# terminated = done and 'TimeLimit.truncated' not in info"   (see Contradictions 4)
```

### Gym release notes 0.25.0 and 0.26.0, and Gymnasium v0.26.0

```text
URL:         https://gymnasium.farama.org/v1.4.0/gym_release_notes/#release-0-26-0
             https://gymnasium.farama.org/v1.4.0/gym_release_notes/#release-0-25-0
             https://gymnasium.farama.org/v1.4.0/gym_release_notes/#release-0-25-2
             https://gymnasium.farama.org/v1.4.0/gymnasium_release_notes/#release-v0-26-0
             (the GitHub release pages these mirror, github.com/Farama-Foundation/Gymnasium/releases and the openai/gym releases, returned 403 in this session; see Limits)
Kind:        primary. The Gym and Gymnasium maintainers' notes for their own releases, kept on the Gymnasium docs site.
Establishes: firsthand: when done was split. Gym 0.25.0 (released 2022-07-13) added the five-value step as the new API. Gym 0.26.0 (released 2022-09-06) made it the default ("now expected by default"). Gymnasium v0.26.0 (released 2022-09-13) is "identical to the Gym v0.26.0 except for the project name".
Paraphrase:  0.26.0 "Breaking backward compatibility": Env.step returns 5 values (observations, reward, termination, truncation, info) instead of 4, and Env.reset returns (obs, info). EnvCompatibility converts old v21/v22 environments.
             0.25.0 "API Changes > Step": the change exists because done is not the same as termination, and the release note claims most deep-RL implementations were wrong for that reason.
             0.25.2 "Updates": under the old done API, the compatibility step functions favour terminated over truncated when both hold, because done can encode only three states.
Locators:    gym_release_notes "0.26.0" > "Breaking backward compatibility", first bullet; "0.25.0" > "API Changes", first bullet; "0.25.2" > "Updates", first bullet; gymnasium_release_notes "v0.26.0: Initial Release"
Quote:       0.26.0: "Step Termination / truncation - The Env.step function returns 5 values instead of 4 previously (observations, reward, termination, truncation, info)."
             0.25.0: "A majority of deep reinforcement learning algorithm implementations are incorrect due to an important difference in theory and practice as done is not equivalent to termination."
```

### Gymnasium: Gym Migration Guide

```text
URL:         https://gymnasium.farama.org/v1.4.0/introduction/migration_guide/#step-function-the-done-terminated-truncated-split
             https://gymnasium.farama.org/v1.4.0/introduction/migration_guide/#timelimit-wrapper-changes
Kind:        primary. Maintainers' guide to their own API change.
Establishes: firsthand: the old v0.21 idiom and the v0.26+ replacement. It also repeats the bootstrapping rule from the tutorial.
Paraphrase:  The v0.21 step returned (obs, reward, done, info), and a time-limit end was detected with info.get('TimeLimit.truncated', False). From v0.26, terminated means the task ended (goal reached, agent died) and truncated means an external limit ended it. The "better migration" branches on terminated first (target = reward), then on truncated (target = reward + discount * estimate). This order is correct when both flags are True.
Locators:    section "4. Step Function: The done → terminated/truncated Split" (both code blocks); section "TimeLimit Wrapper Changes"; comparison table rows "Time Limit Detection" and "Value Bootstrapping"
Quote:       "target = reward + (1-terminated) * gamma * next_value"   (table row "Value Bootstrapping")
```

### Farama Foundation blog: "Deep Dive: Gymnasium Terminated - Truncated Step API"

```text
URL:         https://farama.org/Gymnasium-Terminated-Truncated-Step-API
Kind:        primary for the maintainers' stated reason for the change (the Foundation explaining its own decision). For the RL theory it states, it is a restatement of Pardo et al., which it cites.
Establishes: firsthand: why the API returns two flags instead of a richer done (a custom bool, an integer or a discount factor would all have let old code run silently). It repeats Pardo's point that a terminal state has value zero and a truncated one does not.
Paraphrase:  Published 27 October 2023, originally drafted for Gym v0.26. The authors surveyed four "DQN tutorial" search results on 21 July 2022 and found only TensorFlow Agents handled truncation correctly. They chose the five-tuple because old code breaks loudly under it. A finite-horizon task's built-in time limit is a termination, and the remaining time should then be in the state (TimeAwareObservation exists for this).
Locators:    "Introduction" paragraphs 2-4 and the pseudocode block; "Alternative Implementations" (four items); "Related Reinforcement Learning Theory" last two paragraphs. Publication date from the page's article:published_time metadata. No author is named on the page.
Quote:       "a terminal state has a value of zero, but a truncated state does not, so its value should still be bootstrapped"
```

### Gymnasium tutorial: Create a Custom Environment

```text
URL:         https://gymnasium.farama.org/v1.4.0/introduction/create_custom_env/#registering-and-making-the-environment
             step section: https://gymnasium.farama.org/v1.4.0/introduction/create_custom_env/#step-function
Kind:        primary. Maintainers' tutorial.
Establishes: firsthand: the documented pattern for a grid env: Discrete(4) actions, terminated on reaching the target, truncated always False inside the env, and the step limit supplied by register(..., max_episode_steps=300).
Paraphrase:  The tutorial's GridWorldEnv.step sets terminated when the agent reaches the target and leaves truncated False ("We don't use truncation in this simple environment"). It registers the env with max_episode_steps=300 "to prevent infinite episodes". The printed wrapper stack it shows after make omits TimeLimit (see Contradictions 6).
Locators:    "Step Function" code block; "Registering and making the environment" code blocks
Quote:       none needed
```

### Gymnasium: Basic Usage

```text
URL:         https://gymnasium.farama.org/v1.4.0/introduction/basic_usage/#explaining-the-code-step-by-step
Kind:        primary. Maintainers' introductory page.
Establishes: firsthand: only that the introductory page describes the two flags loosely (Contradictions 7). Do not cite it for the definitions.
Paraphrase:  The paragraph says an environment may "end - this is called the terminal state", and lists a robot crashing, a task completed and stopping after a fixed number of timesteps as instances. It then separates terminated=True from truncated=True.
Locators:    "Explaining the Code Step by Step", fifth paragraph
Quote:       "However, after some timesteps, the environment may end - this is called the terminal state. For instance, the robot may have crashed, or succeeded in completing a task, or we may want to stop after a fixed number of timesteps."
```

### Gymnasium: FrozenLake (optional real case)

```text
URL:         https://gymnasium.farama.org/v1.4.0/environments/toy_text/frozen_lake/#episode-end
Kind:        primary. Maintainers' environment documentation.
Establishes: firsthand: Gymnasium's own slippery 4x4 grid ends by termination at a hole or the goal, and by truncation at 100 steps (200 for 8x8) through the TimeLimit wrapper. Its slip differs from the course's grid: by default 1/3 intended and 1/3 to each perpendicular side.
Paraphrase:  gymnasium.make("FrozenLake-v1") returns <TimeLimit<OrderEnforcing<PassiveEnvChecker<FrozenLakeEnv<FrozenLake-v1>>>>> with Discrete(16) observations and Discrete(4) actions (confirmed in the run below; spec max_episode_steps 100).
Locators:    "Episode End"; "Arguments" (is_slippery, success_rate)
Quote:       none needed
```

### Gym 0.21.0 TimeLimit source (for the old TimeLimit.truncated key)

```text
URL:         https://pypi.org/project/gym/0.21.0/   (file gym-0.21.0/gym/wrappers/time_limit.py inside the sdist gym-0.21.0.tar.gz, uploaded 2021-10-06)
Kind:        primary. OpenAI Gym's own released code.
Establishes: firsthand: what the old info key meant.
Paraphrase:  When elapsed steps reached the limit, TimeLimit set info["TimeLimit.truncated"] = not done and then forced done = True. So the key was present, with value False, when the env terminated on the limit's last step. The key was absent on every step before the limit.
Locators:    TimeLimit.step, lines 16-23 of the file
Quote:       "info["TimeLimit.truncated"] = not done"
```

### Pardo, Tavakoli, Levdik and Kormushev, "Time Limits in Reinforcement Learning", ICML 2018

```text
URL:         https://proceedings.mlr.press/v80/pardo18a.html   (PDF: https://proceedings.mlr.press/v80/pardo18a/pardo18a.pdf)
             preprint linked by the Gymnasium tutorial: https://arxiv.org/abs/1712.00378 (v1 1 Dec 2017, v3 5 Jul 2018, v4 27 Jan 2022). Use the PMLR pages for page numbers.
Kind:        primary. The authors' own peer-reviewed paper introducing the terms.
Authors:     Fabio Pardo, Arash Tavakoli, Vitaly Levdik, Petar Kormushev, all Robot Intelligence Lab, Imperial College London (p. 4045 footnote). Proceedings of the 35th International Conference on Machine Learning, PMLR 80:4045-4054, 2018.
Establishes: firsthand: the two cases, the names time-awareness (TA) and partial-episode bootstrapping (PEB), the TD targets for each, and tabular Q-learning results on a gridworld.
Paraphrase:  Abstract and Section 1 (pp. 4045-4046) set out two cases. (i) The task is to do well over the fixed period. Then a timeout is part of the environment, and the remaining time must be in the agent's input (TA). (ii) The task is indefinite, and time limits only diversify training experience. Then the agent should bootstrap from the value of the last state of each partial episode (PEB). Treating timeouts as environmental terminations in case (ii) is "a common mistake" and is "equivalent to optimizing for returns G_{t:T}" (Section 3, p. 4049).
             Section 2 (p. 4047): a time-unaware agent sees the same state sometimes bootstrapped and sometimes not. The "conflicting updates ... result in an inaccurate average". The perceived chance of termination from a state depends on the behaviour policy: staying in a start state for a whole episode gives a perceived 1/T.
             Eq. (5) (p. 4050): v_π(s) = E_π[G_{t:T} + γ^{T−t} v_π(S_T) | S_t = s].
             Eq. (6) (p. 4050): y = r at environmental terminations, y = r + γ v̂_π(s′) otherwise, including timeouts.
             Section 2.2 and Section 3.1 (pp. 4047-4048, 4050): Two-Goal Gridworld, deterministic. Goals pay 50 (top right) and 20 (bottom left). Five actions (four moves and stay). Each move pays −1 and staying pays 0. Episodes end after 3 steps or at a goal, from a random non-goal start. Tabular Q-learning with random actions, decaying step size, γ = 0.99. The time-unaware agent that treats timeouts as terminal learns v(s) = 2/3(−1 + γ max_{s′∈N(s)} v(s′)) + 1/3(−1) away from the goals and always heads for the nearest goal. With PEB the agent learns the indefinite-horizon optimal policy of going to the 50 goal (Fig. 1c).
             Section 3.4 (p. 4051-4052): on Zhang and Sutton's gridworld (T = 200, ε = 0.1, values initialised to 0, −1 per step), tabular Q-learning with experience replay degrades sharply with buffer size unless it bootstraps at timeouts. With PEB, buffer size "has almost no effect" (Fig. 7).
             Section 4 (p. 4052): PEB needs reliable value predictions, so exploration and randomised start states matter. PEB applies to any early termination that is not environmental.
Locators:    Abstract and Section 1, pp. 4045-4046; Section 2 with Eqs. (3)-(4), p. 4047; Section 2.2, pp. 4047-4048; Section 3 opening, p. 4049; Eqs. (5)-(6) and Section 3.1, p. 4050; Section 3.4 and Fig. 7, pp. 4051-4052; Section 4, p. 4052. PDF page n = printed page 4044 + n.
Quote:       Eq. (6), p. 4050: "y = r at environmental terminations; r + γv̂π(s′) otherwise (including timeouts)"
             p. 4049: "A common mistake, however, is to then consider the terminations due to such time limits as environmental ones. This is equivalent to optimizing for returns Gt:T (Equation 2), not accounting for the possible future rewards that could have been experienced if no time limits were used."
             p. 4050: "the problem presented here is when systematic bootstrapping is not performed from states at the time limit and thus, forgetting that more rewards would actually be available thereafter."
```

### Sutton and Barto, Reinforcement Learning: An Introduction, 2nd edition

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf   (book page: http://incompleteideas.net/book/the-book-2nd.html; the https address failed TLS verification from this session, the http address served the PDF)
Kind:        primary. The authors' own text (MIT Press 2018; this PDF © 2018, 2020 Richard S. Sutton and Andrew G. Barto).
Establishes: firsthand: definitions of episodes, the terminal state, episodic and continuing tasks, G_T = 0, the absorbing-state convention, v(terminal) = 0 and the Q(terminal, ·) = 0 initialisation. The book does not discuss time-limit truncation of episodes. Its "truncated return" is a different notion (Contradictions 10).
Paraphrase:  p. 54 (Section 3.3): an episode ends in a special state called the terminal state, followed by a reset. Tasks with such episodes are episodic tasks. S is the set of nonterminal states and S+ adds the terminal state. The termination time T is a random variable. Continuing tasks go on without limit.
             p. 55 (after Eq. 3.9): G_t = R_{t+1} + γG_{t+1} holds for all t < T if G_T = 0.
             p. 57 (Section 3.4): termination is treated as entering an absorbing state that transitions only to itself and pays only zero rewards, which unifies the episodic and continuing returns. γ = 1 is allowed if all episodes terminate.
             p. 58 (Section 3.5): defines v_π (Eq. 3.12) and says the value of the terminal state is always zero.
             p. 120: the tabular TD(0) box initialises V(terminal) = 0. p. 131: the Q-learning box initialises Q(terminal, ·) = 0 and loops "until S is terminal".
             p. 143 (Section 7.1): G_{t:t+1} = R_{t+1} + γV_t(S_{t+1}) is "a truncated return", with the estimate standing in for the missing rewards. If the n-step return reaches termination, the missing terms are taken as zero.
             p. 185 (Section 8.11): MCTS can "truncate the simulated trajectories short of complete episodes, correcting the truncated returns by means of a stored evaluation function". This is the book's closest statement of bootstrapping a cut-off trajectory.
Locators:    printed pp. 54, 55, 57, 58, 120, 131, 143, 185 (PDF page = printed + 22)
Quote:       p. 54: "Each episode ends in a special state called the terminal state, followed by a reset to a standard starting state or to a sample from a standard distribution of starting states."
             p. 54: "Tasks with episodes of this kind are called episodic tasks."
             p. 58: "Note that the value of the terminal state, if any, is always zero."
             p. 131: "Initialize Q(s, a), for all s ∈ S+, a ∈ A(s), arbitrarily except that Q(terminal, ·) = 0"
```

### The course's published lessons (grid rules and code to reuse)

```text
URL:         read with `nb history --show reinforcement-learning/<slug>` for
             environments-and-the-rl-problem ("The value of a state is an average you can solve for", 2026-10-31),
             learning-values-from-samples ("An agent can learn what each state is worth without knowing the rules", 2026-11-02),
             action-values-from-samples ("Action values let an agent improve its policy from episodes alone", 2026-11-03),
             sarsa-and-q-learning ("Moving at random half the time, Q-learning still learns the optimal arrows", 2026-11-05)
Kind:        primary for what the course has taught and printed (the paper's own published lessons and code).
Establishes: firsthand: the grid's exact rules, the code files a new listing can import, and the course's existing episode cap.
Paraphrase:  Grid (environments-and-the-rl-problem, "One episode on a slippery grid" and gridworld.py): 16 cells numbered 0-15 row by row from the top left. Goal = cell 3, arrival pays +10. Pit = cell 6, arrival pays −20. Any other move pays −1. Goal and pit are terminal: arriving ends the run. Actions up, right, down, left are numbered 0-3 (ARROWS = "^>v<"). Slip 0.2: the intended move with probability 0.8, each perpendicular side 0.1. A move into an edge leaves the agent in place. γ = 0.9. gridworld.py exports N, GOAL, PIT, TERMINAL, ARROWS, STEPS, R (reward per arrival cell), draw, PI (fixed policy), STUCK, move(s, a), transitions(slip), fixed_policy, episode, discounted, radius.
             The same lesson already taught that a value "is 0 at a terminal state" ("Value is an average of returns"). It also defined the STUCK policy, whose bottom row presses the bottom wall so that no episode entering that row ever ends. Its printed value at cell 13 is −10 at γ = 0.9 and −100 at γ = 0.99, and it falls without bound at γ = 1.
             learning-values-from-samples, estimators.py: GAMMA = 0.9; td0(steps, V, count, step=None, decay=0.7) sets target = reward + GAMMA * V[next_cell] with step size count**-0.7. Terminal entries stay 0 because they are never updated. The section "The TD errors add up to Monte Carlo's correction" says the return and the value are both 0 at the end time T.
             action-values-from-samples, mc_control.py: SLIP = 0.2, LIVE = non-terminal cells, CAP = 200 ("an episode stops after this many moves"). step(s, a, rng) is the environment and returns (R[s_next], s_next). play stops at a terminal cell or after CAP moves. The lesson's text in "Monte Carlo ES improves the policy after every episode" says a greedy policy in mid-training can press the bottom row into the wall, that play cuts every episode at 200 moves, and that a cut episode's returns "leave out whatever would have come later". In the main runs, 84 of 2,000,000 episodes were cut.
             sarsa-and-q-learning, td_control.py: td_control(eps, episodes, rng, target="sarsa", watch=None) imports GAMMA, td0 from estimators, N, TERMINAL from gridworld, and CAP, LIVE, step from mc_control. Episodes start in a uniformly random LIVE cell. The loop runs `while s not in TERMINAL and t < CAP`. Each move calls td0 on (4 * s + a, a, reward, 4 * s_next + b), with b = a_next for SARSA and argmax Q[s_next] for Q-learning. Because td0 reads Q[s_next, b] on every move, including the move that hits CAP, the published code already bootstraps at the cap. Terminal rows of Q stay 0 because no update ever targets them.
Locators:    environments-and-the-rl-problem: "One episode on a slippery grid", "Value is an average of returns", "Only a policy that never ends needs the discount", gridworld.py, output of evaluate.py; learning-values-from-samples: "The updates in code" (estimators.py); action-values-from-samples: "Monte Carlo ES improves the policy after every episode" (paragraph before mc_control.py, and mc_control.py); sarsa-and-q-learning: "The update rules differ in one term" (td_control.py)
Quote:       action-values-from-samples: "play stops every episode after 200 moves, so a cut episode's returns leave out whatever would have come later. In the main runs, 84 of 2,000,000 episodes were cut."
```

### Verification run: gymnasium 1.4.0 under uv

```text
URL:         own run, not a public document. Script reproduced in full below; run with `uv run check_api.py` from an empty directory on 2026-11-06.
Kind:        primary for what the installed 1.4.0 code does (direct observation).
Establishes: firsthand: each documented behaviour above holds in 1.4.0, plus two cases the docs do not show (both flags True on one step; the 1.4.0 checker warning on a reused info dict).
Paraphrase:  uv resolved gymnasium 1.4.0 with numpy 2.4.6 on Python 3.11.
             A minimal gymnasium.Env built on the course's grid rules, with Discrete(16) observations and Discrete(4) actions, returned (obs, info) from reset(seed=...) and a 5-tuple from step. The same seed and actions gave the same trajectory. reset() without a seed continued the RNG.
             TimeLimit(env, 4) on a wall-bumping episode returned truncated False, False, False, True. It kept returning truncated=True on steps 5 and 6 when stepped without reset; the wrapper does not stop the env. The count returned to 0 on reset. info stayed {} throughout: there is no TimeLimit.truncated key in 1.4.0.
             With max_episode_steps=1, a deterministic move from cell 2 into the goal returned terminated=True and truncated=True on the same step.
             The bare env, stepped after terminating without reset, kept returning terminated=True. Gymnasium does not enforce a reset at episode end.
             register(..., max_episode_steps=50) then make() gave <TimeLimit<OrderEnforcing<PassiveEnvChecker<Grid<CourseGrid-v0>>>>> and spec.max_episode_steps 50. make(..., max_episode_steps=7) gave 7. make(..., max_episode_steps=-1) dropped TimeLimit and gave spec.max_episode_steps None. An id registered without max_episode_steps gets no TimeLimit. A made env stepped before reset raised ResetNeeded.
             PassiveEnvChecker raised no warning for a Python int or np.int64 observation from a Discrete space. Returning one shared info dict from every call raised UserWarning "The infos returned by `reset` and the following `step` share an object ...", a warning rather than an error.
             gym.spec("FrozenLake-v1").max_episode_steps = 100, "FrozenLake8x8-v1" 200, "CartPole-v1" 500, "CliffWalking-v1" None.
Locators:    printed sections A-H of the output below
Quote:       none
```

Script (`check_api.py`):

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["gymnasium==1.4.0", "numpy"]
# ///
"""Check the Gymnasium contract the lesson will teach, on the course's grid.

Grid rules as in lesson 1: cells 0-15 row by row, goal 3 (+10), pit 6 (-20),
any other arrival -1, actions up/right/down/left = 0..3, intended move with
p = 1 - slip, each perpendicular side slip / 2, an edge leaves the agent put.
"""
import inspect
import warnings

import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.wrappers import TimeLimit

GOAL, PIT = 3, 6
STEPS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def move(s, a):
    row, col = s // 4 + STEPS[a][0], s % 4 + STEPS[a][1]
    return 4 * row + col if 0 <= row < 4 and 0 <= col < 4 else s


class Grid(gym.Env):
    def __init__(self, slip=0.2, start=None, int_type=int, shared_info=False):
        self.observation_space = spaces.Discrete(16)
        self.action_space = spaces.Discrete(4)
        self.slip, self.start, self.int_type = slip, start, int_type
        self._shared = {} if shared_info else None

    def _info(self):
        return self._shared if self._shared is not None else {}

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        live = [s for s in range(16) if s not in (GOAL, PIT)]
        self.s = self.start if self.start is not None else int(
            self.np_random.choice(live))
        return self.int_type(self.s), self._info()

    def step(self, action):
        u = self.np_random.random()
        aim = (action if u < 1 - self.slip else
               (action + 1) % 4 if u < 1 - self.slip / 2 else (action + 3) % 4)
        self.s = move(self.s, aim)
        reward = 10.0 if self.s == GOAL else -20.0 if self.s == PIT else -1.0
        terminated = self.s in (GOAL, PIT)
        return self.int_type(self.s), reward, terminated, False, self._info()


def caught(fn):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try:
            out = fn()
        except Exception as e:  # report the exception as a result
            out = f"raised {type(e).__name__}: {e}"
    return out, [f"{x.category.__name__}: {x.message}" for x in w]


def main():
    print("A gymnasium", gym.__version__, "numpy", np.__version__)

    print("\nB reset signature:", inspect.signature(gym.Env.reset))
    print("  step signature:", inspect.signature(gym.Env.step))
    env = Grid()
    out = env.reset(seed=0)
    print("  reset(seed=0) ->", out, type(out[0]).__name__)
    out = env.step(1)
    print("  step(1) ->", out, "len", len(out))
    print("  Discrete(16):", env.observation_space, "contains 15:",
          env.observation_space.contains(15), "contains 16:",
          env.observation_space.contains(16), "start", env.observation_space.start,
          "n", env.observation_space.n, "dtype", env.observation_space.dtype)
    print("  action_space.sample type:", type(env.action_space.sample()).__name__)

    # same seed, same actions -> same trajectory; reset(seed=None) keeps the RNG
    def traj(e, seed, n=6):
        obs, _ = e.reset(seed=seed)
        return [obs] + [e.step(1)[0] for _ in range(n)]
    print("  same seed twice equal:", traj(Grid(), 7) == traj(Grid(), 7))
    e = Grid(); e.reset(seed=7); a = [e.step(1)[0] for _ in range(5)]
    e.reset(); b = [e.step(1)[0] for _ in range(5)]
    e2 = Grid(); e2.reset(seed=7); [e2.step(1) for _ in range(5)]
    e2.reset(); c = [e2.step(1)[0] for _ in range(5)]
    print("  reset() without seed continues the RNG (two copies agree):", b == c,
          "| differs from first episode:", a != b)

    print("\nC TimeLimit(env, 4) from cell 12 aiming left (into the wall), slip 0:")
    env = TimeLimit(Grid(slip=0.0, start=12), max_episode_steps=4)
    obs, info = env.reset(seed=0)
    for t in range(1, 7):
        obs, r, term, trunc, info = env.step(3)
        print(f"  step {t}: obs {obs} r {r} terminated {term} truncated {trunc}"
              f" info {info} elapsed {env._elapsed_steps}")
    env.reset(seed=1)
    print("  after reset, elapsed:", env._elapsed_steps)

    print("\nD terminal on the limit's last step: cell 2, aim right, slip 0, limit 1")
    env = TimeLimit(Grid(slip=0.0, start=2), max_episode_steps=1)
    env.reset(seed=0)
    obs, r, term, trunc, info = env.step(1)
    print(f"  obs {obs} r {r} terminated {term} truncated {trunc}")

    print("\nE stepping after terminated without reset (unwrapped Grid, slip 0):")
    env = Grid(slip=0.0, start=2)
    env.reset(seed=0)
    print("  ", env.step(1)[:4], "then", env.step(1)[:4])

    print("\nF register and make")
    gym.register(id="CourseGrid-v0", entry_point=Grid, max_episode_steps=50)
    gym.register(id="CourseGridNoLimit-v0", entry_point=Grid)
    for kwargs in ({}, {"max_episode_steps": 7}, {"max_episode_steps": -1}):
        (env, w) = caught(lambda: gym.make("CourseGrid-v0", **kwargs))
        print(f"  make(CourseGrid-v0, {kwargs}) -> {env}; "
              f"spec.max_episode_steps {env.spec.max_episode_steps}; warnings {w}")
    env = gym.make("CourseGridNoLimit-v0")
    print("  make(CourseGridNoLimit-v0) ->", env, env.spec.max_episode_steps)
    env = gym.make("CourseGrid-v0", max_episode_steps=3, slip=0.0, start=12)
    env.reset(seed=0)
    print("  made env, 3 steps into the wall:",
          [env.step(3)[2:4] for _ in range(3)])
    print("  step before reset on a fresh make:",
          caught(lambda: gym.make("CourseGrid-v0").step(0))[0])

    print("\nG passive checker (run by make) on observation and info types")
    for name, kw in (("python int obs, fresh info", {}),
                     ("numpy int64 obs, fresh info", {"int_type": np.int64}),
                     ("python int obs, one shared info dict", {"shared_info": True})):
        env = gym.make("CourseGrid-v0", slip=0.0, start=12, **kw)
        r1 = caught(lambda: env.reset(seed=0))
        s1 = caught(lambda: env.step(3))
        s2 = caught(lambda: env.step(3))
        print(f"  {name}: reset warnings {r1[1]}; step 1 warnings {s1[1]};"
              f" step 2 {s2[0] if isinstance(s2[0], str) else 'ok'} warnings {s2[1]}")

    print("\nH TimeLimit.step source:")
    print(inspect.getsource(TimeLimit.step))
    print("  TimeLimit defined in:", inspect.getsourcefile(TimeLimit))


if __name__ == "__main__":
    main()
```

Output (ANSI colour codes removed, cache path shortened):

```text
A gymnasium 1.4.0 numpy 2.4.6

B reset signature: (self, *, seed: 'int | None' = None, options: 'dict[str, Any] | None' = None) -> 'tuple[ObsType, dict[str, Any]]'
  step signature: (self, action: 'ActType') -> 'tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]'
  reset(seed=0) -> (13, {}) int
  step(1) -> (14, -1.0, False, False, {}) len 5
  Discrete(16): Discrete(16) contains 15: True contains 16: False start 0 n 16 dtype int64
  action_space.sample type: int64
  same seed twice equal: True
  reset() without seed continues the RNG (two copies agree): True | differs from first episode: True

C TimeLimit(env, 4) from cell 12 aiming left (into the wall), slip 0:
  step 1: obs 12 r -1.0 terminated False truncated False info {} elapsed 1
  step 2: obs 12 r -1.0 terminated False truncated False info {} elapsed 2
  step 3: obs 12 r -1.0 terminated False truncated False info {} elapsed 3
  step 4: obs 12 r -1.0 terminated False truncated True info {} elapsed 4
  step 5: obs 12 r -1.0 terminated False truncated True info {} elapsed 5
  step 6: obs 12 r -1.0 terminated False truncated True info {} elapsed 6
  after reset, elapsed: 0

D terminal on the limit's last step: cell 2, aim right, slip 0, limit 1
  obs 3 r 10.0 terminated True truncated True

E stepping after terminated without reset (unwrapped Grid, slip 0):
   (3, 10.0, True, False) then (3, 10.0, True, False)

F register and make
  make(CourseGrid-v0, {}) -> <TimeLimit<OrderEnforcing<PassiveEnvChecker<Grid<CourseGrid-v0>>>>>; spec.max_episode_steps 50; warnings []
  make(CourseGrid-v0, {'max_episode_steps': 7}) -> <TimeLimit<OrderEnforcing<PassiveEnvChecker<Grid<CourseGrid-v0>>>>>; spec.max_episode_steps 7; warnings []
  make(CourseGrid-v0, {'max_episode_steps': -1}) -> <OrderEnforcing<PassiveEnvChecker<Grid<CourseGrid-v0>>>>; spec.max_episode_steps None; warnings []
  make(CourseGridNoLimit-v0) -> <OrderEnforcing<PassiveEnvChecker<Grid<CourseGridNoLimit-v0>>>> None
  made env, 3 steps into the wall: [(False, False), (False, False), (False, True)]
  step before reset on a fresh make: raised ResetNeeded: Cannot call env.step() before calling env.reset()

G passive checker (run by make) on observation and info types
  python int obs, fresh info: reset warnings []; step 1 warnings []; step 2 ok warnings []
  numpy int64 obs, fresh info: reset warnings []; step 1 warnings []; step 2 ok warnings []
  python int obs, one shared info dict: reset warnings []; step 1 warnings ['UserWarning: WARN: The infos returned by `reset` and the following `step` share an object, therefore, modifying one will modify the other. Environments should return new info data on every call as users commonly keep the data returned to them.']; step 2 ok warnings ['UserWarning: WARN: The infos returned by `step` and the following `step` share an object, therefore, modifying one will modify the other. Environments should return new info data on every call as users commonly keep the data returned to them.']

H TimeLimit.step source:
    def step(
        self, action: ActType
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        """Steps through the environment and if the number of steps elapsed exceeds ``max_episode_steps`` then truncate.
        ...
        """
        observation, reward, terminated, truncated, info = self.env.step(action)
        self._elapsed_steps += 1

        if self._elapsed_steps >= self._max_episode_steps:
            truncated = True

        return observation, reward, terminated, truncated, info

  TimeLimit defined in: <uv cache>/site-packages/gymnasium/wrappers/common.py
```

A second script printed the FrozenLake, CliffWalking and CartPole specs: `gym.spec(id).max_episode_steps` gave FrozenLake-v1 100 (map_name 4x4), FrozenLake8x8-v1 200, CliffWalking-v1 None, CartPole-v1 500. `gym.make("FrozenLake-v1")` gave `<TimeLimit<OrderEnforcing<PassiveEnvChecker<FrozenLakeEnv<FrozenLake-v1>>>>> Discrete(16) Discrete(4)`.

## Contradictions

1. **The course already has a time limit.** The commission says "The course has never mentioned Gymnasium, an environment API, time limits, or truncation." Gymnasium is in fact unmentioned. A time limit is not: action-values-from-samples sets `CAP = 200` and says a cut episode's returns "leave out whatever would have come later" (84 of 2,000,000 episodes cut). sarsa-and-q-learning's `td_control.py` loops `while s not in TERMINAL and t < CAP`. That loop already bootstraps on the capped move, because td0 always reads `Q[s_next, b]` and only terminal rows are fixed at 0. The course's Q-learning is therefore already correct at its cap. A version that treats the limit as terminal has to be written deliberately, for example by making the target `reward` alone when the cap is hit. The lesson can name `CAP` as the time limit it already used and link that lesson.
2. **A time limit is not always a truncation.** The commission's idea says `truncated` means "an outside limit (a time limit) cut the episode off". Gymnasium's own tutorial (#termination) counts the end of a finite-horizon task at "a time-limit inherent to the environment" as a termination, with remaining time in the observation. Pardo et al. case (i) (Abstract; Section 2, p. 4047) says the same and gives the target y = r at all terminations, timeouts included, for a time-aware agent (Eq. 4). So which flag a limit raises depends on whether the limit is part of the task. TimeLimit always raises `truncated`, so it encodes the "outside the task" reading. On the course's grid the task ends only at the goal or the pit (environments-and-the-rl-problem), so a limit there is outside the MDP and the commission's reading holds. The page should say which reading it uses and why.
3. **The two flags can both be True.** The commission describes "two different reasons" an episode ends. They can coincide: the verification run (section D) returned `terminated=True, truncated=True` when the goal was reached on the limit's last step. A target that branches on `truncated` first, or bootstraps whenever `truncated` is True, would bootstrap from the goal. Every maintainer source writes the target with `terminated` alone: tutorial `(1 - terminated)`, migration guide `if terminated ... elif truncated`, blog `(not terminated)`. Gym 0.25.2's compatibility layer likewise favours terminated when both hold.
4. **The tutorial's old-API one-liner misreads a termination on the last step.** The Handling Time Limits #solution block comments "terminated = done and 'TimeLimit.truncated' not in info". Gym 0.21's TimeLimit set `info["TimeLimit.truncated"] = not done` on the limit step, so the key is present, with value False, when the env terminated exactly at the limit. The tutorial's test would call that real termination non-terminal. The migration guide's `info.get('TimeLimit.truncated', False)` reads the key correctly. This matters only if the page shows the old idiom, which the commission allows as a mention.
5. **"0.26 replaced done" is the default switch, not the first appearance.** Gym 0.25.0 (2022-07-13) introduced the five-value step, intending it to stay backward compatible "for now", and the TimeLimit changelog dates separate signals to v0.25.0. Gym 0.26.0 (2022-09-06) made it the expected default, and Env.step's docs say "Changed in version 0.26". Gymnasium's first release, v0.26.0 (2022-09-13), is identical to Gym 0.26.0. "Gymnasium has returned both flags since its first release, 0.26" is accurate. "0.26 introduced terminated and truncated" is accurate only for the default API.
6. **The custom-environment tutorial's printed wrapper stack is stale.** It registers GridWorld-v0 with `max_episode_steps=300`, then shows `make` returning `<OrderEnforcing<PassiveEnvChecker<GridWorld<gymnasium_env/GridWorld-v0>>>>`, with no TimeLimit. In 1.4.0 the same registration pattern returns `<TimeLimit<OrderEnforcing<PassiveEnvChecker<...>>>>` (run, section F). Do not copy that printed output.
7. **Basic Usage blurs the terms.** That page calls the end of an episode "the terminal state" and includes "we may want to stop after a fixed number of timesteps" among its instances. Env.step's own definitions separate the two. Cite Env.step, not Basic Usage, for definitions.
8. **Pardo et al. on the discount.** Eq. (1) is introduced with "A discount factor 0 ≤ γ < 1 is necessary to exponentially decay the future rewards ensuring bounded returns" (p. 4045). The course showed γ = 1 works for its fixed policy because every episode ends (environments-and-the-rl-problem), and Sutton and Barto p. 57 allow γ = 1 when all episodes terminate. This matters only if the page quotes Pardo's Eq. (1). The lesson runs at γ = 0.9.
9. **Internal inconsistency in Pardo Section 3.4.** The text on p. 4051 gives the Zhang and Sutton replication "no discount". The Figure 7 caption on p. 4052 says "γ = 0.99". Do not cite a discount for that experiment.
10. **"Truncated" means two things.** Sutton and Barto's "truncated return" (p. 143, and the truncated λ-return of Section 12.3) is a return cut after n steps and completed with an estimate. Gymnasium's `truncated` is a flag saying why an episode ended. The two agree in spirit: a return cut short is completed with a bootstrap, and Section 8.11 (p. 185) says exactly that for cut-off MCTS rollouts. They are still different objects, and the page should not use the word for both without saying so.
11. **No source argues against bootstrapping at truncation in the indefinite-horizon case.** I searched for a critique of partial-episode bootstrapping and found none. The sources that state the rule are Pardo et al. and the Farama maintainers, who cite Pardo et al. Those are one line of origin, not two independent ones. Pardo's own caveat (Section 4, p. 4052) is that PEB needs reliable value estimates, so exploration and varied start states matter.

## Numbers

```text
Figure: gymnasium 1.4.0, uploaded 2026-10-05 (11:02:14 UTC); release notes say "Released on 2026-10-05"
Owner:  PyPI project page (https://pypi.org/project/gymnasium/); Gymnasium release notes #release-v1-4-0
Scope:  latest release as of 2026-11-06; previous release 1.3.0 on 2026-04-22

Figure: requires-python >=3.10; numpy>=1.22.0; the uv run resolved numpy 2.4.6
Owner:  PyPI metadata for gymnasium 1.4.0; verification run
Scope:  the inline script metadata can pin "gymnasium==1.4.0" and "numpy"

Figure: Gym 0.25.0 released 2022-07-13 (five-value step introduced); Gym 0.26.0 released 2022-09-06 (made default); Gymnasium v0.26.0 released 2022-09-13 (identical to Gym 0.26.0)
Owner:  gym_release_notes #release-0-25-0, #release-0-26-0; gymnasium_release_notes #release-v0-26-0
Scope:  dates of the API change

Figure: env.step returns 5 values (observation, reward, terminated, truncated, info); before Gym 0.26 it returned 4 (observation, reward, done, info)
Owner:  Env.step docs; Gym 0.26.0 release note
Scope:  single-environment API

Figure: TimeLimit sets truncated=True when elapsed steps >= max_episode_steps; max_episode_steps=4 gives truncated on step 4
Owner:  TimeLimit docs and 1.4.0 source; verification run section C
Scope:  steps counted since the last reset; at most max_episode_steps transitions per episode

Figure: max_episode_steps=-1 in gymnasium.make applies no TimeLimit
Owner:  gymnasium.make docs; verification run section F
Scope:  1.4.0

Figure: CAP = 200 moves per episode in the course's code; episodes cut at 200 moves: 84 (policy improved every episode), 277 (every 5,600 episodes), 2,902 (every 5,600, averages cleared)
Owner:  action-values-from-samples (mc_control.py and the line "episodes cut off at 200 moves: {'every episode': 84, 'every 5,600': 277, 'every 5,600, cleared': 2902}" in its printed output)
Scope:  Monte Carlo ES, each count out of 20 runs x 100,000 = 2,000,000 episodes for that schedule; epsilon-greedy-exploration and td_control.py reuse the same CAP, and neither printed a cut count

Figure: course grid: 16 cells, goal 3 (+10), pit 6 (−20), other moves −1, slip 0.2 (0.8 / 0.1 / 0.1), γ = 0.9
Owner:  environments-and-the-rl-problem (gridworld.py, "One episode on a slippery grid")
Scope:  every control lesson so far

Figure: STUCK policy value at cell 13: −10 at γ = 0.9, −100 at γ = 0.99, unbounded at γ = 1
Owner:  environments-and-the-rl-problem, output of evaluate.py ("stuck: ... -1000 -10 -100")
Scope:  a policy whose episodes from the bottom row never end; −1/(1−γ) per that lesson

Figure: FrozenLake-v1 max_episode_steps 100 (4x4), FrozenLake8x8-v1 200, CartPole-v1 500
Owner:  FrozenLake docs #episode-end; gym.spec in the verification run; TimeLimit docs example (CartPole 500)
Scope:  Gymnasium 1.4.0 registry

Figure: Pardo et al. Two-Goal Gridworld: goals 50 and 20, move −1, stay 0, T = 3, γ = 0.99; time-unaware greedy values beside the goals converge to 49 and 19; v(s) = 2/3(−1 + γ max v(s′)) + 1/3(−1) elsewhere
Owner:  Pardo et al., Sections 2.2 and 3.1, pp. 4047-4048, 4050
Scope:  deterministic grid, tabular Q-learning with random actions, trained to convergence

Figure: Pardo et al. replay experiment: T = 200, ε = 0.1, −1 per step, buffers 40, 60, 100 and 1M, 30 seeds (0 to 29)
Owner:  Pardo et al., Section 3.4 and Fig. 7, pp. 4051-4052
Scope:  Zhang and Sutton's Difficult Gridworld; the discount is stated inconsistently (Contradictions 9)

Figure: Pardo et al., PMLR 80:4045-4054, 2018
Owner:  PMLR proceedings page
Scope:  page numbers used throughout this record
```

## Limits

- No source measures what treating a time limit as terminal does to Q-learning's values on the course's grid, at any limit length. Pardo's tabular result is on a deterministic grid with T = 3 and different rewards. The page's claim about the grid has to come from the writer's own run and derivation.
- Nothing establishes how often `td_control.py` episodes hit `CAP = 200` at ε = 0.5. The course printed cut counts only for Monte Carlo ES with exploring starts (84 of 2,000,000 when the policy improves every episode). If the lesson keeps CAP at 200, the effect may be too small to see, which is the writer's experiment to settle.
- Sutton and Barto do not state the truncation rule. They give v(terminal) = 0, Q(terminal, ·) = 0, the absorbing-state convention and the bootstrap-corrected truncated return, but say nothing about time limits that end an episode early. The bootstrap-at-truncation rule rests on Pardo et al. and the Gymnasium documentation, a single line of origin (Contradictions 11).
- The GitHub release pages and GitHub-hosted source (Farama-Foundation/Gymnasium, openai/gym) returned 403 in this session. I read the release notes from the maintainers' mirror on gymnasium.farama.org, the 1.4.0 source from the installed wheel and the docs' source view, and the Gym 0.21.0 source from the PyPI sdist. I did not compare GitHub's text with the mirror.
- The Farama blog post names no author. It is attributable to the Farama Foundation only.
- The brief's "0.26 release note that replaced done" is resolved in Contradictions 5. I decided to treat Gym 0.26.0 as the release that made the split the default and Gymnasium 0.26.0 as identical to it, and to mention 0.25.0 only if the page needs the first appearance.
- The commission's statement that the course never mentioned time limits is wrong (Contradictions 1). I decided this changes nothing in the commission's scope. The writer should link the CAP passage in action-values-from-samples when introducing TimeLimit.
- I did not check vector environments, autoreset or `final_obs` handling. The series schedules those for a later lesson.
- Pardo's arXiv v4 (2022) may paginate differently from PMLR. I did not compare them, and all page numbers here are PMLR's.

## Source assets

```text
Asset: Pardo et al., Figure 1, p. 4046: three panels, (a) Standard, (b) Time-awareness, (c) Partial-episode bootstrapping, showing colour-coded state values and policies learned by tabular Q-learning on the Two-Goal Gridworld
Shows: on another grid (deterministic, with interior walls), the same comparison the lesson makes: values and arrows when a timeout is treated as terminal versus when the agent bootstraps at the timeout
Crop:  keep all three panels with their (a)/(b)/(c) labels and the caption's first sentence; the figure has no colour bar (checked on the rendered page), so no crop can show the values' scale
```

```text
Asset: Pardo et al., Figure 7, p. 4052: left, the Difficult Gridworld map; middle and right, tabular Q-learning with experience replay without and with PEB, for buffers of 40, 60, 100 and 1M (T = 200)
Shows: the same tabular method degrading with buffer size when timeouts are treated as terminal, and barely affected by buffer size with PEB
Crop:  keep both curve panels, their titles, the legend and the axes; the map panel can go; omit the γ in the caption or note that it conflicts with the text (Contradictions 9)
```

```text
Asset: Sutton and Barto, p. 57, Section 3.4: the state-transition diagram S0 → S1 → S2 → solid square, rewards R1 = R2 = R3 = +1, then R4 = R5 = 0 looping on the square
Shows: termination as an absorbing state that pays zero forever, which is why a terminal state's value is 0
Crop:  keep the three states, the absorbing square and all reward labels; omit the surrounding prose
```

```text
Asset: Gymnasium documentation (Env.step, TimeLimit, make, Discrete, Handling Time Limits, migration guide, release notes, FrozenLake)
Shows: None found. These pages are text and code; FrozenLake's page has an environment render but no diagram of termination or truncation
Crop:  n/a
```

```text
Asset: Farama blog post
Shows: None found (a decorative banner only)
Crop:  n/a
```

```text
Asset: PyPI project page
Shows: None found
Crop:  n/a
```

## Discarded

```text
https://gymnasium.farama.org/ (docs home page): read only to confirm which version the unversioned docs serve; it carries no claim the page needs
https://gymnasium.farama.org/main/api/env/ (development docs): differs from the 1.4.0 docs and documents unreleased code; the record cites the /v1.4.0/ pages
https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.4.0 and .../v0.26.0: returned 403 in this session; replaced by the maintainers' release-note mirror on gymnasium.farama.org
https://incompleteideas.net/book/RLbook2020.pdf (https form): failed TLS verification from this session; the same file at the http address was used
```
