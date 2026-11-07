# Evidence: reinforcement-learning/checking-a-custom-environment (researcher 01)

The gymnasium 1.4.0 source settles the central claim. `check_env` and the `PassiveEnvChecker` test the form of what `reset` and `step` return and whether a seed repeats. No function in either checker compares a transition or a reward with anything except a second seeded run of the same environment. On the course's SlipperyGrid, `check_env` makes 12 resets and 5 steps, all from cells 8 and 0. It passes copies whose goal does not terminate, whose slip reverses the move, or that pay +10 in cell 2. Two findings qualify the commission's wording. First, in `step`'s return the checker only warns about most type errors, an observation outside Discrete(16) included, and still returns normally, so a pass does not confirm types. Second, an exact calculation shows that a uniformly random policy has identical dynamics under any slip-direction or action-label error on this grid. Random actions therefore cannot catch "a slip that goes the wrong way". The hand-drawn policy can: its start-averaged value moves from 1.36 to 3.70. Stable-Baselines3 2.9.2, the current release, one-hot encodes a Discrete(16) observation into 16 floats. Its source, its docs and a model built here all confirm this. For sanity checks, Schulman's 2016 slides are the clearest text to link. No paper introduced random or scripted baselines as a method, and DQN's random-play anchor is the best-known use of one. The record is thin on detection power: how many episodes each behavioural check needs for each error is unmeasured beyond one rough estimate, and it belongs to the writer's runs.

## Sources

### 1. gymnasium 1.4.0, `gymnasium/utils/env_checker.py`

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/env_checker.py
Kind:        primary. The Farama Foundation's own source for the release. The file at
             tag v1.4.0 is byte-identical to the one in the gymnasium-1.4.0 wheel on
             PyPI (checked with cmp), and the GitHub page shows 508 lines.
Establishes: firsthand, everything check_env runs and in what order.
Locators:    line numbers below are the file's own.
```

Paraphrase, `check_env` (L406–508), in call order:

- L430–443: the environment must be a `gymnasium.Env`, else `TypeError`.
- L444–447: a warning if the environment is wrapped, recommending `env.unwrapped`.
- L455–467: both spaces must exist (else `AttributeError`) and be well formed, via the passive checker's `check_action_space` and `check_observation_space`. `check_space_limit` (L368–403) adds warnings only for Box spaces (infinite bounds, unnormalized Box actions). It does nothing for Discrete.
- L470: `check_seed_deprecation` (L327–340) warns if the environment still has a callable `seed` method.
- L471: `check_reset_return_info_deprecation` (L310–324) warns if `reset` takes `return_info`.
- L472: `check_reset_return_type` (L343–365) calls `reset()` and asserts a 2-tuple, an observation inside the observation space, and a dict for info.
- L473: `check_reset_seed_determinism` (L79–173) calls `reset(seed=123)`, `reset()`, `reset(seed=123)`, `reset()`, `reset(seed=456)`. It asserts every observation is in the space, that `_np_random` exists after seeding (L102–104, the message names a missing `super().reset(seed=seed)`), that the same seed gives the same generator state (L140–144), and that a different seed gives a different state (L150–155). It compares the observations themselves only when `env.spec is not None` and the spec is not marked nondeterministic (L124–138). It warns if the default seed is not `None` (L163–169) and raises `gym.error.Error` if `reset` has neither `seed` nor `**kwargs` (L170–173).
- L474: `check_reset_options` (L176–201) calls `reset(options={})` and raises `gym.error.Error` if the signature has neither `options` nor `**kwargs`.
- L477–478: the passive checker's `env_reset_passive_checker`, then `env_step_passive_checker` with an unseeded `env.action_space.sample()`.
- L481: `check_step_determinism` (L204–270) is skipped only if the spec says nondeterministic (L214–215). It seeds the action space with 123, samples one action, then twice resets with seed 123 and takes that one step. It asserts that the observations, rewards, terminated flags and infos match (tolerance 1e-5, L240–270) and that the generator states match (L233–238). It asserts truncated is `False` after one step (L259–261).
- L482: `check_returned_data_not_reused` (L273–307) seeds, resets, takes up to two steps and resets again. It asserts that no two calls return observations or infos that share a mutable object (L295–307).
- L485–498: `render` is checked only if `env.render_mode is not None`. With a spec, the environment is made once in each declared render mode. Without a spec, it warns "Not able to test alternative render modes due to the environment not having a spec" (L496–498).
- L500–508: the close check runs only when `env.spec is not None`.

Nothing in the file receives a model of the environment, an expected next state or an expected reward. The only comparison made on `step`'s output is between two seeded runs of the same environment.

Quote (the exact wording shows what the checker means by checking transitions), docstring of `check_step_determinism`, L208:

> Note: A single step should be enough to assert that the state transition function is deterministic (at least for most environments).

### 2. gymnasium 1.4.0, `gymnasium/utils/passive_env_checker.py`

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/passive_env_checker.py
Kind:        primary, as source 1 (byte-identical to the wheel).
Establishes: firsthand, which faults fail and which only warn.
Locators:    line numbers below.
```

- `check_space` (L61–106): for Discrete, asserts `n > 0` and shape `()` (L77–83).
- `check_obs` (L131–176): for a Discrete space, warns if the observation is not an `int` or `np.int64` (L140–142). An observation outside the space produces a warning only: "is not within the observation space" (L172–176).
- `env_reset_passive_checker` (L250–290): a deprecation warning if `reset` lacks `seed` or `options`, a warning if the result is not a 2-tuple, and an assertion that info is a dict (L287–289).
- `env_step_passive_checker` (L293–350): it asserts a tuple (L299–301). A 4-tuple gets a deprecation warning (L302–311), and any other length except 5 raises `error.Error` (L325–328). Non-bool terminated or truncated is a warning (L316–324). The observation goes through `check_obs` (L330). A reward that is not an int or float type is a warning, and NaN and inf are warnings (L332–344). Info must be a dict, as an assertion (L346–348). Nothing checks the reward's value beyond NaN and inf.
- `data_shares_objects` (L179–218) ignores immutable values such as `int`, because they are interned (L215–218). `env_data_reuse_passive_checker` (L221–247) warns when two calls share an object.
- `env_render_passive_checker` (L405–457): checks the declared render modes and fps, then calls `render`.

### 3. gymnasium 1.4.0, `PassiveEnvChecker` and `gymnasium.make`

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/common.py#L225-L368
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/envs/registration.py#L801-L816
Kind:        primary, as source 1 (both byte-identical to the wheel).
Establishes: firsthand, when the passive checker runs and how much of an episode it sees.
Locators:    common.py L225-368 (class); registration.py L769-780, L801-816.
```

- `__init__` (L248–285): the environment must be a `gymnasium.Env`, and both spaces must exist and be well formed (L265–275).
- `step` (L287–313): the first call runs `env_step_passive_checker` and the reset-to-step data-reuse check (L291–301). The second call runs only the step-to-step data-reuse check (L305–311). Every later call passes straight through.
- `reset` (L315–326): only the first call runs `env_reset_passive_checker`. `render` (L328–334): only the first call is checked.
- `make` (registration.py L801–805) adds `PassiveEnvChecker` as the innermost wrapper unless `disable_env_checker` is set, then `OrderEnforcing` (L808–809), then `TimeLimit` (L811–816). `make` also sets `env.unwrapped.spec` (L769–780). That is why `check_env` on the unwrapped environment from `make` compares reset observations and skips the render-mode warning.
- The course's SlipperyGrid has never been registered. Every listing so far constructs it directly, so the passive checker has never run on it.

### 4. Gymnasium 1.4.0 documentation, Utility functions: Environment Checking and `play`

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/utils/#gymnasium.utils.env_checker.check_env
             (same page, #gymnasium.utils.play.play)
Kind:        primary. Farama documents its own function.
Establishes: the stated scope of check_env.
Locators:    section "Environment Checking"; section "Visualization", play().
```

Paraphrase: `check_env` checks that an environment follows Gymnasium's API. It checks that the two spaces are correct and "will call the reset(), step() and render() functions with a variety of values". The page recommends calling it after constructing an environment and in a project's continuous integration. `warn` is ignored. `play()` lets a user play an environment with the keyboard.

Quote (the scope claim itself is the evidence):

> Check that an environment follows Gymnasium’s API.

### 5. Gymnasium 1.4.0 documentation, PassiveEnvChecker and `make`

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/misc_wrappers/#gymnasium.wrappers.PassiveEnvChecker
             https://gymnasium.farama.org/v1.4.0/api/registry/#gymnasium.make
Kind:        primary, as source 4.
Establishes: the documented behaviour of the wrapper.
Locators:    class entry PassiveEnvChecker; gymnasium.make, parameter disable_env_checker.
```

Paraphrase: the wrapper surrounds `step`, `reset` and `render` to check they follow Gymnasium's API. `make` applies it automatically, and `disable_env_checker` turns it off. No vector version exists. The example shows `<TimeLimit<OrderEnforcing<PassiveEnvChecker<CartPoleEnv<CartPole-v1>>>>>`. The docs do not say that only the first reset and the first one or two steps are checked. The source does (source 3).

### 6. Gymnasium 1.4.0 documentation, Create a Custom Environment: Debugging Your Environment

```text
URL:         https://gymnasium.farama.org/v1.4.0/introduction/create_custom_env/#debugging-your-environment
Kind:        primary. Farama's own guidance for custom environments.
Establishes: that Gymnasium's tutorial pairs check_env with a known-action test.
Locators:    subsections "Check Environment Validity", "Manual Testing with Known
             Actions", "Common Debug Issues".
```

Paraphrase: "Check Environment Validity" runs `check_env`, with a comment saying it will catch many common issues. "Manual Testing with Known Actions" resets with a seed, steps through actions 0 to 3 and prints the position change and reward of each. "Common Debug Issues" lists forgetting `super().reset()` (`check_env` catches it, see source 10) and mixing coordinate conventions so that an action meant as "right" changes the row. That second error is a rule error, and the checker cannot see it.

### 7. Gymnasium v1.4.0 release notes

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.4.0
Kind:        primary. Farama's release notes.
Establishes: what 1.4.0 changed in the checker.
Locators:    "New Features"; "Utilities".
```

Paraphrase: released 5 October 2026 (PyPI upload 2026-10-05 11:02 UTC). Under New Features: `check_env` and the passive checker run by `make` now verify that `reset` and `step` return distinct observation and info objects each step. Under Utilities: the checker's determinism checks were fixed by snapshotting reused observations and comparing the current generator state in `check_step_determinism`. github.com refused curl from this session, so I read this page through a summarizing fetch. The fragments above are confirmed, but I have not seen the full bullet text verbatim. The source (source 1, L273–307 and L224, L233–238) matches both items.

### 8. gymnasium 1.4.0, `gymnasium/utils/play.py`

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/play.py
Kind:        primary, as source 1 (byte-identical to the wheel).
Establishes: why play() cannot drive SlipperyGrid.
Locators:    L24-31; L78-82.
```

Paraphrase: importing the module raises `DependencyNotInstalled` without pygame and points to `gymnasium[classic_control]` (L24–31). `PlayableGame` raises `ValueError` unless `render_mode` is `rgb_array` or `rgb_array_list` (L78–82). SlipperyGrid has no render mode, so the commission's short keyboard loop (for example `input()`) is the route that needs no new dependency.

### 9. gymnasium 1.4.0, `gymnasium/core.py`, class `Env`

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/core.py#L64-L77
Kind:        primary, as source 1 (byte-identical to the wheel).
Establishes: that the API declares no reward scale.
Locators:    L64-77 (class attributes); L169-171 (reset seeding).
```

Paraphrase: the class attributes are `metadata = {"render_modes": []}`, `render_mode = None`, `spec = None`, the two spaces and `_np_random`. There is no `reward_range`. A search of the 1.4.0 package finds `reward_range` only in `envs/toy_text/frozen_lake.py` L247, where FrozenLake sets it as an ordinary attribute. `Env.reset` creates a new generator only when `seed` is not `None` (L169–171). An environment therefore declares the range of its observations through its space, and nothing in the API or the checkers declares or tests the scale of its rewards.

### 10. Researcher runs: gymnasium's `check_env` on SlipperyGrid and altered copies

```text
URL:         none. Throwaway scripts outside the repository, in /tmp/claude-0/run/
             (check1.py, check2.py, check3.py), using the course files extracted
             verbatim from the published lessons, gymnasium 1.4.0, Python 3.11.
Kind:        primary. My own runs. The writer's printed run supersedes them on the page.
Establishes: what check_env does to this environment.
Locators:    results below.
```

- `check_env(SlipperyGrid())` returns normally and prints one warning: "Not able to test alternative render modes due to the environment not having a spec. Try instantiating the environment through `gymnasium.make`". It prints as a `UserWarning` whose text carries ANSI colour codes (`[33mWARN: ...[0m`). `check_env` prints nothing on success.
- `check_env(TimeLimit(SlipperyGrid(), max_episode_steps=4))` also passes, with the wrapped-environment warning (source 1, L444–447) added.
- After `gym.register("SlipperyGrid-v0", entry_point=SlipperyGrid, max_episode_steps=200)` and `gym.make`, `check_env(env.unwrapped)` passes with no warnings. `print(env)` gives `<TimeLimit<OrderEnforcing<PassiveEnvChecker<SlipperyGrid<SlipperyGrid-v0>>>>>`.
- A counting subclass records 12 resets and 5 steps per call. In three calls the five transitions were (cell 8, a random move), then (cell 0, up → 0) three times, then (cell 0, down → 4). Cell 8 comes from the stream of seed 456 and is the same every call. The move from it is the unseeded sample at L478 and varies. Every other step starts from seed 123's start cell, 0. No step reaches the goal or the pit.
- Altered copies, each a subclass of SlipperyGrid:

```text
change to SlipperyGrid                               check_env result
goal does not terminate (terminated only at pit)     pass, render-mode warning only
slip reverses the move (aim + 2 with prob. 0.2)      pass, render-mode warning only
+10 paid on arrival in cell 2                        pass, render-mode warning only
every reward multiplied by 1e6                       pass, render-mode warning only
step returns np.array([cell])                        pass, warnings: type; not in space
terminated returned as int                           pass, warning: not a boolean
step returns cell + 16                               pass, warning: not in space
reset skips super().reset(seed=seed)                 AssertionError (L102-104 message)
reset has no seed parameter                          gym.error.Error (L170-173)
step always returns truncated True                   AssertionError "Environment truncates after 1 step..."
step returns 4 values                                deprecation warning, then ValueError unpacking
reward is NaN                                        warning, then AssertionError: rewards not equivalent (NaN != NaN)
```

- Through `gym.make`, a copy whose observation leaves the space from the third step of an episode on (cells 17, 18) produced no warning from the `PassiveEnvChecker` over five steps. `check_env(env.unwrapped)` on it passed with no warnings, because the checker never takes a third step in an episode.

### 11. stable-baselines3 2.9.2 on PyPI

```text
URL:         https://pypi.org/project/stable-baselines3/2.9.2/
Kind:        primary. The maintainers' release record.
Establishes: the current release and its dependency pins.
Locators:    PyPI JSON API (checked 7 Nov 2026); wheel METADATA lines 3, 21, 25-28.
```

Paraphrase: 2.9.2 is the latest release, uploaded 26 October 2026 (the changelog dates it 2026-10-26). It requires Python >=3.10, `gymnasium>=0.29.1,<2.0`, `numpy>=1.20,<3.0`, `torch>=2.8,<3.0` and `cloudpickle`. gymnasium 1.4.0 satisfies the pin.

### 12. stable-baselines3 2.9.2 source: preprocessing of a Discrete observation

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/preprocessing.py#L91-L139
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/policies.py#L122-L131
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/torch_layers.py#L31-L44
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/spaces/utils.py#L134-L136
Kind:        primary. DLR-RM's own source at tag v2.9.2, byte-identical to the
             2.9.2 wheel (checked with cmp).
Establishes: firsthand, what an SB3 network receives for a Discrete(16) observation.
Locators:    line numbers below.
```

- `preprocess_obs` (preprocessing.py L91–139): its docstring says "For discrete observations, it create a one hot vector" (L99). The Discrete branch is `F.one_hot(obs.long(), num_classes=int(observation_space.n)).float()` (L122–124).
- `get_obs_shape` (L142–166) stores a Discrete observation with shape `(1,)` (L153–155, comment "Observation is an int").
- `get_flattened_obs_dim` (L169–185) falls through to gymnasium's `flatdim`, which returns `n` for Discrete (gymnasium spaces/utils.py L134–136).
- `BaseModel.extract_features` (policies.py L122–131) calls `preprocess_obs` before the features extractor.
- `FlattenExtractor` (torch_layers.py L31–44) sets its output size to `get_flattened_obs_dim(observation_space)`, which is 16 here.

### 13. stable-baselines3 2.9.2 documentation, Policy Networks

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/custom_policy.html#sb3-policy
Kind:        primary. SB3 documents its own library.
Establishes: the documented one-hot behaviour, for a pointer on the page.
Locators:    section "SB3 Policy", first Note.
```

Quote (the commission asks for the library's own wording):

> All observations are first pre-processed (e.g. images are normalized, discrete obs are converted to one-hot vectors, …) before being fed to the features extractor.

The same note adds that for vector observations the features extractor is just a Flatten layer.

### 14. stable-baselines3 2.9.2 documentation, Reinforcement Learning Tips and Tricks

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/rl_tips.html#tips-and-tricks-when-creating-a-custom-environment
Kind:        primary for SB3's own advice.
Establishes: what an off-the-shelf library recommends before training on a custom environment.
Locators:    section "Tips and Tricks when creating a custom environment"; section
             "General advice", TL;DR and the paragraph on normalizing input.
```

Paraphrase: the advice is to normalize the observation space when its bounds are known and to rescale continuous actions to [−1, 1]. It recommends starting with a shaped reward and a simplified problem, and to "debug with random actions to check if your environment works and follows the gym interface (with check_env, see below)". A 10-step random-action loop follows. It says a timeout must return truncated, which `TimeLimit` does. General advice: when applying RL to a custom problem, always normalize the agent's input. Use a separate test environment for evaluation, and do several runs. The section on implementing an algorithm links Schulman's "nuts and bolts" slides (source 17) at http://joschu.net/docs/nuts-and-bolts.pdf.

### 15. stable-baselines3 2.9.2's own environment checker

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/env_checker.py#L467-L547
             https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/custom_env.html
Kind:        primary, as sources 12 and 13.
Establishes: that the library the next lesson uses has a stricter but equally rule-blind checker.
Locators:    env_checker.py L190-196, L254-308, L331-410, L467-547; custom_env page,
             paragraph after the check_env example.
```

Paraphrase: SB3's `check_env` calls `reset(seed=0)`. It warns about spaces SB3 does not support, including Discrete spaces that do not start at 0. `_check_returned_values` (L331–410) runs one reset and one step. An observation outside the space is an `AssertionError` (L305–308), and non-bool terminated or truncated is an assertion (L402–403). `_check_nan` (L190–196) takes 10 random steps through `VecCheckNan`. The docs page says Gymnasium's checker "checks a superset of what SB3 supports". Researcher run (source 16): SB3's `check_env` passes SlipperyGrid with no warnings. It also passes the goal-does-not-terminate and reversed-slip copies, and it fails the cell + 16 copy with "does not match the given observation space Discrete(16)".

### 16. Researcher run: Stable-Baselines3 2.9.2 on SlipperyGrid

```text
URL:         none. Throwaway scripts /tmp/claude-0/run/sb3_onehot.py and sb3_check2.py;
             SB3 2.9.2, torch 2.15.0+cpu (from the PyTorch CPU index), gymnasium 1.4.0.
Kind:        primary. My own run.
Establishes: what a neural agent receives from this environment.
Locators:    printed output, summarized below.
```

`PPO("MlpPolicy", SlipperyGrid())` builds a `FlattenExtractor`, and the first layer of both its policy and value networks is `Linear(in_features=16, out_features=64)`. `features_dim` is 16. `DQN("MlpPolicy", ...)` also has a features dimension of 16. `policy.obs_to_tensor(13)` gives `tensor([13])` (int64), and `preprocess_obs` turns it into a 16-vector with a 1 at index 13 and 0 elsewhere. No training was run.

### 17. John Schulman, "The Nuts and Bolts of Deep RL Research" (slides)

```text
URL:         http://joschu.net/docs/nuts-and-bolts.pdf
Kind:        primary for Schulman's own advice. It is a talk deck, not a study, and
             it reports no measurements.
Establishes: a practitioner's checklist for a new task that names random behaviour,
             human control, and the scale of observations and rewards.
Locators:    PDF pages (one slide each): 5, 6, 7, 16, 18. Title slide dated
             December 9th, 2016. 26 pages.
```

Paraphrase: the section "Approaching New Problems" includes slide 6, "POMDP Design". It says to visualize the random policy and ask whether it sometimes shows the desired behaviour, to try human control, to plot time series of observations and rewards and ask whether they are on a reasonable scale, and to histogram observations and rewards. Slide 5: make a new task easier until there are signs of life, with good input features and a shaped reward. Slide 16: standardize observations of unknown range, and rescale rewards without shifting their mean. Slide 18: look at the minimum, maximum and standard deviation of episode returns, and at episode lengths. Slide 7, "Run Your Baselines", means algorithm baselines (cross-entropy method, policy gradient, Q-learning with SARSA), not random or scripted policies. The slides do not suggest comparing an environment with exact values. That comparison is the course's own addition, possible because its earlier lessons solved the grid exactly. The slides print no affiliation. Over https the host reset the connection from this session, but http serves the file, and SB3's docs (source 14) link the same http address.

### 18. Mnih et al., "Human-level control through deep reinforcement learning", Nature 518 (2015)

```text
URL:         https://www.nature.com/articles/nature14236 (DOI 10.1038/nature14236).
             The publisher page redirects to a login. I read the full text from
             DeepMind's copy at https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf
Kind:        primary. The authors define their own normalized score.
Establishes: the best-known use of a random policy as a baseline that anchors a score scale.
Locators:    Fig. 3 caption (PDF page 3); Methods, "Evaluation procedure" (PDF page 6);
             Extended Data Table 2 caption.
```

Paraphrase: Fig. 3 normalizes DQN's score so that a professional human games tester is 100% and random play is 0%: 100 × (DQN score − random play score)/(human score − random play score). Under "Evaluation procedure", the random agent chose a random action at 10 Hz, every sixth frame, repeating its last action in between. Moving the random agent to 60 Hz changed DQN's normalized performance by more than 5% in only six games. This source is optional here. It fits the next lesson's random baseline for a trained agent better than this lesson's checks.

### 19. The course's code, from the published lessons

```text
URL:         published lessons environments-and-the-rl-problem (gridworld.py),
             action-values-from-samples (mc_control.py), learning-values-from-samples
             (estimators.py), termination-and-truncation (grid_env.py); read with
             nb history --show and extracted verbatim from the library HTML.
Kind:        primary for the course's rules.
Establishes: the rules, rewards and observation type the checks act on.
Locators:    file line numbers below.
```

- gridworld.py: `N = 16`, `GOAL, PIT = 3, 6` (L9–11). `R[s']` is the reward for arriving in `s'`: −1, with +10 at the goal and −20 at the pit (L15–17). `move` leaves the agent in place at an edge (L38–41). The hand-drawn policy is `PI` (L26–29), and `fixed_policy` solves it (L55–61).
- mc_control.py: `SLIP = 0.2`. `LIVE` lists the 14 non-terminal cells (L15–16). `step` (L20–26) moves as aimed with probability 0.8 and otherwise slips to `(a + 1) % 4` or `(a + 3) % 4`, 0.1 each.
- estimators.py: `GAMMA = 0.9`.
- grid_env.py: `reset` starts uniformly over `LIVE` unless `options["start"]` is given. `step` returns a Python `int` cell, a float reward, terminated at the goal or the pit, and truncated `False`. A Python `int` passes `check_obs`'s `int`/`np.int64` test (source 2, L140–142).

### 20. Researcher calculation: which baseline can see which rule error

```text
URL:         none. Throwaway scripts /tmp/claude-0/calc/bugs.py, bugs2.py, spread.py,
             importing the course files of source 19.
Kind:        primary. My own derivation and exact solves, for the writer and editor to
             check, not for the page as printed.
Establishes: that the random baseline is blind to slip-direction and action-label errors
             on this grid.
Locators:    derivation and printed values below.
```

Derivation. Under the uniformly random policy the agent moves from s to s′ with probability ¼ Σₐ P(s′ | s, a). The slip rule moves in direction (a + k) mod 4, with k = 0, +1 or −1 at probabilities 0.8, 0.1, 0.1, independent of a. Averaging over a uniform a gives ¼ Σ_d 1[move(s, d) = s′] for any distribution of k. A rule error that changes the distribution of k leaves the random policy's transition probabilities unchanged, and so does any relabelling of the four actions. Examples are a slip backward and a slip to one side only. The values, and the whole distribution of returns, stay the same. The random policy also ignores observations, so it cannot see an error confined to the observation `step` returns. The hand-drawn policy reads the observation and aims by it, so it sees both kinds.

Exact values, mean over the 14 starts that `reset` draws from, γ = 0.9:

```text
rule                          uniform random    hand-drawn PI    PI, v(13)
correct                          -10.904            1.360          -2.01
slip reverses the move           -10.904            3.698           0.33
slip only to one side            -10.904            1.145          -2.56
up and down swapped              -10.904           -7.431         -10.00
+10 on arrival in cell 2          -9.170            6.271
goal does not terminate          -10.568           46.556
```

The random column is identical to machine precision (max |Δv| = 0) for the first four rows. The hand-drawn PI's 1.360 and v(13) = −2.01 match the course's published values. With the goal not terminating, PI's 46.6 comes from PI's entry for the goal cell, up, which bumps the top wall and arrives in the goal again. Simulated spread, 20,000 episodes, 200-move cap, seed 0: random returns have mean −10.82 and sd 7.29, and PI returns have mean 1.34 and sd 8.82. Each mean is within 1.6 standard errors of its exact value. At that spread, telling the random baseline's −10.57 from −10.90 at three standard errors needs about 4,000 episodes. I did not measure detection power further.

```python
# bugs.py core (imports from the course files)
def P_of(slip_dirs):
    P = np.zeros((N, 4, N))
    for s in LIVE:
        for a in range(4):
            for d, p in slip_dirs(a):
                P[s, a, move(s, d)] += p
    return P
correct  = lambda a: [(a, 0.8), ((a + 1) % 4, 0.1), ((a + 3) % 4, 0.1)]
backward = lambda a: [(a, 0.8), ((a + 2) % 4, 0.2)]
oneside  = lambda a: [(a, 0.8), ((a + 1) % 4, 0.2)]
swapped  = lambda a: correct({0: 2, 2: 0}.get(a, a))
def values(P, pol):                      # pol[s, a]: move probabilities
    Pp = np.einsum("sa,sat->st", pol, P)
    Q = Pp.copy(); Q[:, TERMINAL] = 0
    v = np.linalg.solve(np.eye(N) - GAMMA * Q, Pp @ R); v[TERMINAL] = 0
    return v
# uniform: np.full((N, 4), 0.25); hand-drawn: one-hot rows of PI
```

## Contradictions

- **Gymnasium's docs against its source, on how much `check_env` exercises.** The docs say it calls `reset`, `step` and `render` "with a variety of values" (source 4). The source makes 12 resets and at most 5 steps (source 1). On SlipperyGrid every step starts from cell 8 or cell 0 (source 10), and `render` is never called when `render_mode` is `None` (source 1, L485–487).
- **The commission's "confirms spaces, types, seeding and the reset and step signatures" against the source.**
  - Spaces: confirmed, as well-formedness only. For Discrete that means `n > 0` and shape `()`.
  - Types: at `reset`, an observation outside the space fails (source 1, L360–362). In `step`, a wrong observation type, an observation outside the space, a non-bool terminated or truncated, and a non-numeric reward only warn, and `check_env` still returns normally (source 2; source 10 rows 5–7).
  - Seeding: confirmed for the generator. Reset observations are compared only when the environment has a spec, which means it came through `gym.make`. The directly constructed SlipperyGrid gets the generator-state comparisons and the one-step determinism check, but no comparison of reset observations (source 1, L124–138).
  - Signatures: only `reset`'s parameters are inspected, for `seed` and `options`. `step`'s signature is not inspected, only its return.
  - Accurate wording: "a pass means no assertion fired; warnings may still have printed."
- **The commission's angle against the exact calculation.** The commission names "what random actions earn" as a check that catches a wrong rule, and it offers "a slip that goes the wrong way" as an example error. On this grid random actions cannot see any slip-direction error or action relabelling (source 20). They see reward and termination errors, a non-terminating goal only weakly (−10.90 against −10.57). The hand-drawn policy sees all six errors in the table. Play by hand would show an action-label error at once.
- **SB3's advice against the commission's use of random actions.** SB3 recommends random actions "to check if your environment works and follows the gym interface" (source 14). That is an interface check, not a comparison with known values. The two uses differ and do not conflict.
- **Gymnasium's checker against SB3's.** SB3's checker fails an observation outside the space, where gymnasium's only warns (sources 2 and 15). SB3's docs call gymnasium's checker a superset of what SB3 supports. Both pass the rule errors.

## Numbers

```text
Figure: 12 resets and 5 steps per check_env call
Owner:  gymnasium 1.4.0 env_checker.py resets at L351, L95/107/113/119/146, L192, L220/230, L285/293, plus passive_env_checker.py L274; steps at passive_env_checker.py L298, env_checker.py L221/231, L287; researcher count on SlipperyGrid (source 10)
Scope:  one check_env call; never more than 2 steps after any reset
```
```text
Figure: transitions check_env takes on SlipperyGrid: one from cell 8 (unseeded move), four from cell 0 (up, up, up, down)
Owner:  researcher runs (source 10), three calls
Scope:  SlipperyGrid constructed directly, gymnasium 1.4.0
```
```text
Figure: PassiveEnvChecker checks the 1st reset, the 1st step, and data reuse across reset→step 1 and step 1→step 2
Owner:  gymnasium 1.4.0 wrappers/common.py L287-326
Scope:  per wrapped environment instance, for its whole life
```
```text
Figure: reward per step: -1 (ordinary arrival), +10 (goal, cell 3), -20 (pit, cell 6)
Owner:  gridworld.py L15-17 (environments-and-the-rl-problem)
Scope:  every step of SlipperyGrid
```
```text
Figure: undiscounted episode return under a T-move limit lies in [-T - 19, +10]; T = 200 gives [-219, +10]
Owner:  researcher arithmetic from the rewards above (pit on move T after T-1 ordinary moves; goal on move 1). Writer to confirm.
Scope:  one episode
```
```text
Figure: discounted return (γ = 0.9) of any episode lies in [-20, +10]
Owner:  researcher arithmetic: ending in the pit on move k gives -10 - 10(0.9)^(k-1), lowest at k = 1; the goal on move k gives -10 + 20(0.9)^(k-1), highest at k = 1. Writer to confirm.
Scope:  one episode, any limit
```
```text
Figure: observation: one integer 0-15 (Discrete(16)); SB3 input: 16 floats, one-hot
Owner:  grid_env.py; SB3 2.9.2 preprocessing.py L122-124; researcher PPO build (Linear(16, 64))
Scope:  every observation
```
```text
Figure: exact mean value over the 14 starts, uniform random policy: -10.904; hand-drawn PI: 1.360
Owner:  researcher exact solve (source 20); PI's values are published in environments-and-the-rl-problem (v(13) = -2.01)
Scope:  γ = 0.9, start uniform over the 14 non-terminal cells, no time limit
```
```text
Figure: under reversed slip / one-sided slip / up-down swap: random -10.904 each; PI 3.698 / 1.145 / -7.431
Owner:  researcher exact solve (source 20)
Scope:  as above
```
```text
Figure: sd of discounted episode return: random 7.29, hand-drawn 8.82
Owner:  researcher simulation, 20,000 episodes, seed 0, 200-move cap
Scope:  start uniform over 14 cells
```
```text
Figure: gymnasium 1.4.0 released 2026-10-05; stable-baselines3 2.9.2 released 2026-10-26; torch 2.15.0 released 2026-10-28
Owner:  PyPI upload records (sources 7, 11); torch PyPI JSON
Scope:  current releases as of 7 Nov 2026
```
```text
Figure: DQN normalized score = 100 × (DQN − random play)/(human − random play); random agent acts at 10 Hz
Owner:  Mnih et al. 2015, Fig. 3 caption; Methods, Evaluation procedure
Scope:  49 Atari games
```

## Limits

- Detection power is unmeasured: how many episodes the random and hand-drawn comparisons need for each candidate error. The one estimate (about 4,000 random episodes for the non-terminating goal) is rough and mine.
- The exact values for the uniform random policy and for the altered rules are my calculations (source 20). The course has not published the random policy's value. The writer has to compute and print them.
- The per-episode reward ranges are my arithmetic, not a source's.
- No paper introduced random or scripted baselines as a method, as far as I found. Schulman's slides are advice, not a study. DQN uses random play as a score anchor on Atari.
- I could not establish when `reward_range` left gymnasium's `Env`. The 1.0.0 release notes do not mention it. I can show only that 1.4.0 has no such attribute.
- The 1.4.0 release notes reached me through a summarizing fetch (github.com refused curl), so their exact bullet wording is unverified beyond the fragments in source 7.
- Schulman's slides answered only over http from here.
- CleanRL and PufferLib were not researched. The brief did not ask.
- SB3 was built, not trained. Nothing here says how an SB3 agent behaves on the grid.

## Source assets

```text
Asset: Schulman slide 6, "POMDP Design" (PDF page 6 of nuts-and-bolts.pdf)
Shows: a 2016 practitioner's checklist naming the random policy, human control, and the scale of observations and rewards
Crop:  the whole slide with its title; it is all text, so a quotation in prose may carry it better
```
```text
Asset: SB3 docs "SB3 Policy" figure (https://stable-baselines3.readthedocs.io/en/v2.9.2/_images/sb3_policy.png)
Shows: observation → features extractor → network architecture, for actor and critic
Crop:  keep the actor panel only; the figure does not show the one-hot step, so a drawn diagram of cell 13 becoming a 16-vector shows the point better
```
```text
Asset: DQN Fig. 3 (Mnih et al. 2015, PDF page 3)
Shows: per-game scores normalized between random play (0%) and a human tester (100%)
Crop:  must keep the axis and the caption's formula; it suits the next lesson, not this one
```
- Gymnasium docs and source (sources 1–9): none found. The evidence is text and code.
- SB3 source (sources 12, 15): none found.

## Discarded

```text
https://github.com/Farama-Foundation/Gymnasium/releases/tag/v1.0.0: searched for the removal of reward_range; not mentioned
https://stable-baselines3.readthedocs.io/en/v2.9.2/misc/changelog.html: the 2.9.2 entry gave only its date and empty headings in the fetched HTML; PyPI carries the same date
https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/algos.html: read for statements on Discrete observations; it covers action spaces only
https://www.youtube.com/watch?v=8EcdaCk9KaQ: linked from SB3's tips page; a "Deep RL Bootcamp Lecture 6" recording uploaded by a third-party channel (title from YouTube oEmbed); not watched, and the slides are the primary
```

## Questions for the orchestrator

1. **The random baseline cannot see a slip-direction error on this grid** (source 20). The commission offers "a slip that goes the wrong way" as an example. Provisional: I pass this to the writer as material. If the writer keeps the slip error, the page needs the hand-drawn policy to catch it and a sentence on why random actions cannot. Otherwise a reward or termination error suits the random check. The derivation is three lines and is not an extra experimental result.
2. **The PassiveEnvChecker runs only through `gym.make`, and SlipperyGrid has never been registered.** Provisional: the writer either describes the wrapper from source or registers SlipperyGrid in a listing. Registering also lets `check_env` compare reset observations (source 1, L124–138).
3. **Schulman's slides answer only over http.** Provisional: cite http://joschu.net/docs/nuts-and-bolts.pdf, the document's own address, which SB3's docs also link.
4. **For the next lesson only:** SB3 2.9.2 ran here with gymnasium 1.4.0 and torch 2.15.0 from the PyTorch CPU index. torch 2.15.0 from PyPI on Linux requires CUDA packages (cuda-toolkit, nvidia-cudnn-cu13 and others), and its wheel alone is 539 MB. Provisional: note only, no action in this lesson.
