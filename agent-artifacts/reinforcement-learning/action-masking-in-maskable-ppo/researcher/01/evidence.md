# Evidence: reinforcement-learning/action-masking-in-maskable-ppo (researcher 01)

Retrieved 2026-11-18. The release and API questions are settled from source. sb3-contrib 2.9.2,
uploaded to PyPI on 26 October 2026, is the current release. It requires stable-baselines3 >=2.9.2
and <3.0, and `uv run` resolved it in one pass with gymnasium 1.4.0, stable-baselines3 2.9.2 and
torch 2.14.1+cpu, using agent.py's CPU-index block unchanged. In that release MaskablePPO gets the
mask by calling the environment's `action_masks()` method before every action, through wrappers
and vectorized environments. It never reads `info["action_mask"]`. It replaces each illegal logit
with −1e8, stores every mask in the rollout buffer and applies it again in the update. `predict`
without `action_masks` applies no mask and gives no warning. During evaluation only sb3-contrib's
own `evaluate_policy` and `MaskableEvalCallback` fetch masks; SB3's `evaluate_policy` and
`EvalCallback` do not. Huang and Ontañón analysed masking; they did not introduce it, and they say
earlier systems already used it. Their Table 2 (arXiv v3, p. 5) compares masking with an
invalid-action penalty on µRTS maps from 4×4 to 24×24. The evidence is thin for the angle in one
place. On the paper's 4×4 map a penalty of −0.01 reached the same final return as masking. In one
researcher's seed, plain PPO under hanoi.py's no-op rule also learned the 15-move solution in
50,000 steps, after spending 28% of its training steps on illegal no-ops. The gap the writer can
expect is in training steps spent and in evaluation without the mask, more than in the final greedy
policy. The researcher's runs below are single-seed checks for the writer, not results to print.

## Sources

### sb3-contrib 2.9.2 on PyPI

```text
URL:         https://pypi.org/project/sb3-contrib/2.9.2/
Kind:        primary. The package index entry the Stable-Baselines Team publishes; it owns the
             release's version, date and declared dependencies.
Establishes: firsthand: version 2.9.2 is the latest release, files uploaded 2026-10-26T09:51:48Z;
             requires_dist ['stable_baselines3<3.0,>=2.9.2']; requires_python >=3.10. No later
             release or pre-release exists (full release list ends 2.9.0a2, 2.9.0, 2.9.2).
Paraphrase:  The only declared runtime dependency is stable-baselines3 from 2.9.2 up to but not
             including 3.0.
Locators:    project page "Release history"; JSON at https://pypi.org/pypi/sb3-contrib/json,
             info.version, info.requires_dist, releases["2.9.2"].
```

### stable-baselines3 2.9.2, torch and gymnasium on PyPI

```text
URL:         https://pypi.org/project/stable-baselines3/2.9.2/
             https://pypi.org/project/torch/2.14.1/
Kind:        primary. Index entries published by each project.
Establishes: stable-baselines3 2.9.2 (uploaded 2026-10-26T09:35:28Z) requires gymnasium>=0.29.1,<2.0,
             numpy>=1.20,<3.0, torch>=2.8,<3.0, cloudpickle; requires_python >=3.10. torch 2.14.1
             was uploaded 2026-09-30; torch 2.15.0 (2026-10-28) is now the latest torch. gymnasium's
             latest is 1.4.0.
Paraphrase:  Every course pin sits inside SB3 2.9.2's declared ranges. torch 2.15.0 also does, but
             agent.py pins 2.14.1 and nothing here requires moving.
Locators:    JSON info.requires_dist and releases[...] upload_time for each project.
```

### sb3-contrib v2.9.2 release notes and changelog

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/releases/tag/v2.9.2
             https://sb3-contrib.readthedocs.io/en/v2.9.2/misc/changelog.html
Kind:        primary. The maintainers' own release notes.
Establishes: firsthand: release titled "v2.9.2: Updated dependencies", dated 26 Oct; its only
             breaking change is "Upgraded to Stable-Baselines3 >= 2.9.2"; no new features or bug
             fixes listed. Warns that SB3 2.9.2 "will be the last one supporting Python 3.10".
             2.8.0 (2026-04-01) fixed MaskablePPO's n_updates count under target_kl, an action
             reshape before clipping, and a `ValueError: Simplex` crash in
             MaskableCategorical.apply_masking with torch 2.9+.
Paraphrase:  Nothing in MaskablePPO's masking changed between 2.9.0 and 2.9.2.
Locators:    docs/misc/changelog.md lines 5–13 (2.9.2), 25–40 (2.9.0), 43–60 (2.8.0) at tag v2.9.2.
```

### sb3-contrib 2.9.2 source (tag v2.9.2, commit a8af63682070df0bda9707400b2e971055600910)

Read from a clone of tag v2.9.2. `diff -r` against the installed 2.9.2 wheel found no difference, so
the line numbers hold for what `uv run` installs. github.com blob pages returned 403 to curl
through this session's proxy and loaded through WebFetch; that is a session restriction, and the
pages are public.

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/utils.py
Kind:        primary. The library's own code owns how it behaves.
Establishes: firsthand: EXPECTED_METHOD_NAME = "action_masks" (line 5). get_action_masks(env)
             (lines 8–19) returns np.stack(env.env_method("action_masks")) for a VecEnv and
             env.get_wrapper_attr("action_masks")() otherwise. is_masking_supported(env)
             (lines 22–37) checks env.has_attr for a VecEnv, else tries get_wrapper_attr.
Paraphrase:  The method name is fixed. The mask is whatever that method returns at the moment it is
             called.
Locators:    lines 5, 8–19, 22–37.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/wrappers/action_masker.py
Kind:        primary.
Establishes: firsthand: ActionMasker(env, action_mask_fn) (lines 7–29) takes a callable or a
             method name string. Its docstring: "This wrapper is not needed if the env exposes the
             expected method itself" (line 12). action_masks() returns
             self._action_mask_fn(self.env) (lines 31–32). For a string, line 23 stores
             getattr(self.env, name), a bound method, which line 32 then calls with self.env as an
             extra argument.
Paraphrase:  The callable form works. The string form calls the bound method with one argument
             too many (see Contradictions; researcher run R7 raised TypeError).
Locators:    lines 7–32; docstring 15–16; string branch 22–27; call 31–32.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/ppo_mask/ppo_mask.py
Kind:        primary.
Establishes: firsthand:
             - Docstring cites "Background on Invalid Action Masking: https://arxiv.org/abs/2006.14171"
               (line 30).
             - Constructor defaults (lines 76–102) are PPO's: n_steps 2048, batch_size 64,
               n_epochs 10, gamma 0.99, gae_lambda 0.95, clip_range 0.2, ent_coef 0.0. Supported
               action spaces: Discrete, MultiDiscrete, MultiBinary (lines 124–128).
             - Default rollout buffer is MaskableRolloutBuffer (lines 156–160).
             - collect_rollouts(..., use_masking=True) raises ValueError("Environment does not
               support action masking. Consider using ActionMasker wrapper") when use_masking and
               the env lacks the method (lines 216–217).
             - Each step: "This is the only change related to invalid action masking" (line 226);
               action_masks = get_action_masks(env) (line 228); self.policy(obs_tensor,
               action_masks=action_masks) (line 230); then env.step (line 233).
             - rollout_buffer.add(..., action_masks=action_masks) (lines 262–270).
             - Bootstrap value for the last observation is computed without a mask: "Masking is not
               needed here, the choice of action doesn't matter" (lines 274–278).
             - predict(observation, state, episode_start, deterministic, action_masks=None) passes
               action_masks straight to self.policy.predict (lines 286–307).
             - train() passes rollout_data.action_masks to policy.evaluate_actions (lines 339–343).
             - learn(total_timesteps, ..., use_masking=True, ...) (lines 428–437) calls
               collect_rollouts with use_masking (line 453).
Paraphrase:  During training the agent asks the env for a fresh mask before every action, samples
             from the masked distribution, stores the mask with the transition, and recomputes
             log-probabilities and entropy under that stored mask in every update epoch. The
             masking is on by default and cannot silently fall back to unmasked training.
Locators:    lines 30, 76–102, 124–128, 156–160, 216–217, 226–233, 262–270, 274–278, 286–307,
             339–343, 428–453.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/distributions.py
Kind:        primary.
Establishes: firsthand: MaskableCategorical.apply_masking (lines 46–70): masks become a bool tensor
             reshaped to the logits (line 58); HUGE_NEG = th.tensor(-1e8, ...) (line 59);
             logits = th.where(self.masks, self._original_logits, HUGE_NEG) (line 61); the
             distribution is rebuilt from those logits (line 70). masks=None restores the original
             logits (lines 62–64). entropy() (lines 72–82) zeroes the masked terms: "masked actions
             possess no uncertainty". MultiDiscrete and MultiBinary masks are split per component
             (lines 235–247).
Paraphrase:  An illegal action's logit is replaced by −1e8 before the softmax, so its probability is
             0 in float32 (researcher run R3) and its log-probability is −1e8.
Locators:    lines 18–82 (class), 59 and 61 (the masking), 72–82 (entropy).
Quote:       "HUGE_NEG = th.tensor(-1e8, dtype=self.logits.dtype, device=device)" (line 59), the
             exact constant.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/policies.py
Kind:        primary.
Establishes: firsthand: MaskableActorCriticPolicy.forward applies the mask, if given, before
             get_actions (lines 113–143, mask at 138–140). _predict calls
             get_distribution(observation, action_masks) (lines 253–267). predict (lines 269–323)
             takes action_masks=None and never looks up a mask itself. evaluate_actions applies the
             stored mask before log_prob and entropy (lines 325–353). get_distribution applies
             the mask only "if action_masks is not None" (lines 355–368).
Paraphrase:  With no mask passed, predict samples from, or with deterministic=True takes the argmax
             of, all actions, legal or not.
Locators:    lines 138–140, 253–267, 269–323, 349–351, 366–367.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/buffers.py
Kind:        primary.
Establishes: firsthand: MaskableRolloutBuffer.reset allocates action_masks as float32 ones of shape
             (buffer_size, n_envs, mask_dims), with mask_dims = action_space.n for Discrete
             (lines 60–77). add stores the step's masks at self.pos when given (lines 79–86). get
             and _get_samples return them in each minibatch as the action_masks field
             (lines 88–124).
Paraphrase:  The mask in force when an action was sampled travels with that transition into the
             update. If learn is called with use_masking=False, the stored rows stay all ones,
             which leaves every action unmasked.
Locators:    lines 12–19 (sample fields), 60–86, 114–124.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/evaluation.py
Kind:        primary.
Establishes: firsthand: evaluate_policy(model, env, n_eval_episodes=10, deterministic=True, ...,
             use_masking=True) (lines 14–25). Raises the same ValueError when masking is
             unsupported (lines 62–63). Wraps a plain env in DummyVecEnv (lines 67–68). In each step
             it calls get_action_masks(env) and passes them to model.predict (lines 94–102);
             with use_masking=False it calls predict without masks (lines 103–109). Rewards are
             summed undiscounted (line 111) unless a Monitor supplies episode totals
             (lines 125–136).
Paraphrase:  sb3-contrib's evaluate_policy fetches a fresh mask before every evaluation action.
Locators:    lines 14–25, 62–63, 67–68, 94–111.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/callbacks.py
Kind:        primary.
Establishes: firsthand: MaskableEvalCallback subclasses SB3's EvalCallback, adds use_masking=True
             (lines 10–36), and in _on_step calls sb3-contrib's evaluate_policy with
             use_masking=self.use_masking (lines 57–67), commented "evaluate_policy() has been
             patched to support masking" (line 56). Everything else (best-model saving, logging)
             follows EvalCallback.
Paraphrase:  The only difference from EvalCallback is which evaluate_policy it calls.
Locators:    lines 7, 34–36, 56–67.
```

```text
URL:         https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/tests/wrappers/test_action_masker.py
Kind:        primary.
Establishes: firsthand: test_wrapper_accepts_attr_name (lines 43–52) builds ActionMasker(env,
             "_action_masks") and asserts only hasattr(env, "action_masks"); it never calls
             action_masks().
Paraphrase:  The string form is tested for construction only.
Locators:    lines 43–52.
```

### sb3-contrib 2.9.2 documentation, Maskable PPO page

```text
URL:         https://sb3-contrib.readthedocs.io/en/v2.9.2/modules/ppo_mask.html
             (source: docs/modules/ppo_mask.md at tag v2.9.2)
Kind:        primary. The maintainers' documentation of their own API.
Establishes: firsthand, as the maintainers' statements:
             - "Implementation of invalid action masking for the Proximal Policy Optimization (PPO)
               algorithm. Other than adding support for action masking, the behavior is the same as
               in SB3's core PPO algorithm." (lines 9–10), linking arXiv 2006.14171.
             - Warning: "You must use MaskableEvalCallback ... instead of the base EvalCallback ...
               Similarly, you must use evaluate_policy from sb3_contrib.common.maskable.evaluation
               instead of the SB3 one." (lines 46–49)
             - Warning: with SubprocVecEnv "you must implement the action_masks inside the
               environment (ActionMasker cannot be used)" (lines 51–54).
             - Example: get_action_masks(env) then model.predict(obs, action_masks=action_masks)
               in a manual loop (lines 81–86).
             - check_env "will execute the method step passing a random action ... without taking
               into account the invalid actions mask" (lines 92–96).
             - Code comment: "Note that use of masks is manual and optional outside of learning,
               so masking can be 'removed' at testing time" (lines 124–126).
             - Comment: "MaskablePPO behaves the same as SB3's PPO unless the env is wrapped with
               ActionMasker" (lines 117–120); contradicted by the source (see Contradictions).
             - Results: MicroRTS 4x4 (600K steps) and 10x10 (1.5M steps), with and without
               masking, 3 seeds (lines 129–170).
Paraphrase:  The library's own documentation says evaluation must use the maskable helpers, and that
             outside learn() the caller supplies masks by hand.
Locators:    docs/modules/ppo_mask.md lines 9–10, 46–54, 81–86, 92–96, 117–126, 129–170.
Quote:       "Note that use of masks is manual and optional outside of learning" (line 124). The
             wording is the library's own statement of the trap the lesson is about.
```

### stable-baselines3 2.9.2 source (tag v2.9.2, commit 0cdcd200deef06b9ad0af72f6ddfb07c06c6df39)

Clone matched the installed 2.9.2 wheel with no differences.

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/evaluation.py
Kind:        primary.
Establishes: firsthand: SB3's evaluate_policy has no use_masking or action_masks parameter
             (lines 12–22) and calls model.predict(observations, state=..., episode_start=...,
             deterministic=...) without masks (lines 92–97).
Paraphrase:  Handed a MaskablePPO model, SB3's evaluate_policy evaluates the unmasked policy.
Locators:    lines 12–22, 92–97.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/callbacks.py
Kind:        primary.
Establishes: firsthand: callbacks.py imports SB3's evaluate_policy (line 24); EvalCallback
             (class at line 342) calls it in _on_step without masks (lines 465–474).
Paraphrase:  The base EvalCallback evaluates a MaskablePPO model unmasked.
Locators:    lines 24, 342, 465–474.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/dummy_vec_env.py
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/subproc_vec_env.py
Kind:        primary.
Establishes: firsthand: DummyVecEnv.env_method calls env_i.get_wrapper_attr(method_name)(...) on
             each sub-env (dummy_vec_env.py lines 127–130). step_wait resets a finished sub-env
             inside the same step and stores the new episode's first observation (lines 68–72),
             so the next action_masks() call reads the new episode's state. The SubprocVecEnv
             worker does the same with get_wrapper_attr (subproc_vec_env.py lines 56–58); the
             default start method is forkserver where available, else spawn (lines 100,
             108–113).
Paraphrase:  In a vectorized env each copy answers action_masks() for its own current state, and
             after an automatic reset that is the new episode's start.
Locators:    dummy_vec_env.py 68–72, 127–130; subproc_vec_env.py 56–58, 100, 108–113.
```

```text
URL:         https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/preprocessing.py
Kind:        primary.
Establishes: firsthand: a Discrete observation is one-hot encoded,
             F.one_hot(obs.long(), num_classes=observation_space.n).float() (lines 122–124).
Paraphrase:  hanoi.py's Discrete(81) state reaches MlpPolicy as an 81-long one-hot vector.
Locators:    lines 122–124.
```

### Gymnasium 1.4.0 source

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/core.py
Kind:        primary.
Establishes: firsthand: Env.get_wrapper_attr returns getattr(self, name) (lines 286–288).
             Wrapper.get_wrapper_attr returns the wrapper's own attribute if it has one, otherwise
             asks the wrapped env, recursively (lines 427–444). Identical to the installed 1.4.0
             wheel.
Paraphrase:  action_masks() defined on Hanoi is found through TimeLimit, Monitor and any other
             wrapper; an outer wrapper that defines its own action_masks would shadow it.
Locators:    lines 286–288, 427–444.
```

### Huang and Ontañón, "A Closer Look at Invalid Action Masking in Policy Gradient Algorithms"

```text
URL:         https://arxiv.org/abs/2006.14171v3 (PDF https://arxiv.org/pdf/2006.14171v3)
             Published version: https://journals.flvc.org/FLAIRS/article/view/130584,
             DOI 10.32473/flairs.v35i.130584
Kind:        primary for its own experiments and proposition; the authors ran them. It is not
             primary for who first used masking: it attributes that to Vinyals et al. 2017,
             Berner et al. 2019 and Ye et al. 2020.
Establishes: firsthand:
             - Authors: Shengyi Huang and Santiago Ontañón, College of Computing & Informatics,
               Drexel University (p. 1); a footnote on Ontañón reads "Currently at Google".
               arXiv v1 25 Jun 2020, v2 26 Jun 2020, v3 31 May 2022; v3 comment "Accepted into the
               proceedings of International FLAIRS Conference Proceedings, Vol. 35 (2022)". The
               FLAIRS page dates it 2022/05/04, volume 35, track "Special Track: Artificial
               Intelligence in Games, Serious Games, and Multimedia", licence CC BY-NC 4.0.
             - Masking was already "a common technique" in earlier work, and "there is no literature
               providing detailed descriptions of the implementation" (p. 2, "Invalid Action
               Masking").
             - Masking replaces invalid logits with a large negative M, "e.g. M = −1 × 10^8"
               (p. 2, Eq. 2–4). Worked example with logits [1,1,1,1], a2 invalid: gradient
               [0.75, −0.25, −0.25, −0.25] unmasked vs [0.67, −0.33, 0.0000, −0.33] masked (p. 2,
               Eq. 1 and Eq. 6); masking "makes the gradient corresponding to the logits of the
               invalid action to zero" (p. 3).
             - Proposition 1: the masked gradient is the policy gradient of the masked policy
               (p. 3, "Masking Still Produces a Valid Policy Gradient"). Stage 6 material.
             - Strategies compared (p. 4, "Strategies to Handle Invalid Actions"): (1) invalid
               action penalty r_invalid ∈ {0, −0.01, −0.1, −1} added to the step's reward;
               (2) invalid action masking, applied only to the Source Unit and Attack Target Unit
               components, so "invalid actions still could be sampled"; (3) naive masking, which
               samples from the masked distribution but takes gradients through the unmasked one;
               (4) masking removed: trained as (2), "then evaluate the agent without providing the
               mask".
             - Setup: µRTS harvesting task, +1 per harvest and +1 per return, 200-step games, maps
               4×4, 10×10, 16×16, 24×24, PPO, 500,000 time steps, γ 0.99, 4 seeds (pp. 3–4;
               Table 4, p. 10). A valid Source Unit drawn at random has probability 2/16 = 0.125 on
               4×4 and 2/576 = 0.0034 on 24×24 (p. 4).
             - Table 2 (p. 5), "Results averaged over 4 random seeds": masking reaches r_episode
               40.00 on all four maps with t_solve 8.67%–18.38% and t_first 0.05%–0.08%; penalty
               reaches 30.00–40.00 on 4×4 only and 0.00–1.00 on 10×10 and larger; masking removed
               scores 33.53, 25.93, 17.32, 17.37 with a_null 63.57–165.12.
             - Prose (pp. 5–6): "Invalid action masking scales well"; "Invalid action penalty does
               not scale"; r_invalid = −1 "seems to have an adverse effect of discouraging
               exploration"; "Masking removed still behaves to some extent ... starts to execute
               more invalid actions ... most prominently, selecting an invalid Source Unit".
             - Figure 2 (p. 4): episodic return (a: 4×4, b: 10×10) and PPO KL divergence
               (c, d) over 5×10^5 time steps for all strategies; 4 seeds, smoothed with weight 0.9.
               Figure 3 (p. 9, appendix) repeats this for all four maps (a–d return, e–h KL).
Paraphrase:  On a game whose invalid action space grows with the map, PPO with a mask on two
             action components found the first reward within about 0.05%–0.08% of training and
             solved every map; with a reward penalty instead, it solved only the 4×4 map. An agent
             trained with the mask and run without it still collected reward but chose invalid
             units tens to hundreds of times per episode.
Locators:    p. 2 "Invalid Action Masking" and Eqs. 1–6; p. 3 Proposition 1; p. 4 "Strategies to
             Handle Invalid Actions", "Evaluation Metrics" (p. 5) and Figure 2; p. 5 Table 2;
             pp. 5–6 "Evaluation Results"; p. 9 Figure 3; p. 10 Table 4. Page numbers are arXiv v3
             PDF pages.
Quote:       "Invalid action penalty does not scale." (p. 5). The paper's own heading for the
             comparison.
```

### The FLAIRS article page

```text
URL:         https://journals.flvc.org/FLAIRS/article/view/130584
Kind:        primary for publication metadata (the proceedings' own record).
Establishes: title, authors, Drexel University affiliation, volume 35, date 2022/05/04, DOI, CC BY-NC
             4.0 licence, track (from the page's citation_* and DC.* meta tags, fetched with curl,
             HTTP 200). WebFetch of the same page returned 403.
Paraphrase:  The 2022 publication is the FLAIRS-35 proceedings paper; arXiv v3 is the authors'
             posted version of it.
Locators:    page meta tags citation_date, citation_volume, citation_doi, DC.Rights.
```

### The researcher's runs (verification, not a source to cite)

All on Linux x86_64, uv 0.11.32, Python 3.11.18 (chosen by uv), torch 2.14.1+cpu with
torch.set_num_threads(1), hanoi.py exactly as printed in the 17 November lesson. Scripts were in
the scratchpad (`/tmp/claude-0/-home-user-the-nightly-build/efbdeaae-8835-5515-95b0-8d4030ac57a4/scratchpad/rl-research/run/`),
which may be cleared, so the setups that bear on the angle are given in full under R11 and R12.

```text
R0  uv run with agent.py's block plus "sb3-contrib==2.9.2" resolved and installed 16 packages in
    15.9 s on a cold cache (torch wheel 187.1 MiB): gymnasium 1.4.0, stable-baselines3 2.9.2,
    sb3-contrib 2.9.2, torch 2.14.1+cpu, numpy 2.4.6, cloudpickle 3.1.2, farama-notifications 0.0.6,
    filelock 4.2.12, fsspec 2026.9.0, jinja2 3.1.6, markupsafe 3.0.4, mpmath 1.3.0, networkx 3.6.1,
    setuptools 84.2.1, sympy 1.14.0, typing-extensions 4.16.0. torch.cuda.is_available() False.
    Imports of MaskablePPO, ActionMasker, get_action_masks, is_masking_supported, the maskable
    evaluate_policy and MaskableEvalCallback all succeeded.
R1  is_masking_supported(Count(TimeLimit(Hanoi()))) True; mask at state 0 [True True False False
    False False].
R2  MaskablePPO("MlpPolicy", env, gamma=0.9, seed=0).learn(4096): 4096 steps, 0 illegal, 9.0 s.
    Rollout buffer action_masks shape (2048, 6) float32, 8 distinct mask rows.
R3  Masked logits at state 0 after R2: [-0.755, -0.635, -1e8, -1e8, -1e8, -1e8]; probabilities
    [0.4701, 0.5299, 0, 0, 0, 0] (exact zeros); log_prob of illegal action 2 = -1e8. Unmasked
    probabilities at the same state: [0.162, 0.182, 0.167, 0.151, 0.167, 0.171].
R4  predict(s, deterministic=True) with no action_masks chose an illegal move in 45 of 80 non-goal
    states for an untrained model (seed 1), 7 of 80 after 4,096 steps, 10 of 80 after 50,000
    steps (seed 0); with action_masks, 0 of 80.
R5  Untrained model (seed 1), 20 episodes under TimeLimit 100: SB3 evaluate_policy took 2000 steps,
    1986 illegal, every episode cut at 100; sb3-contrib evaluate_policy took 1902 steps, 0 illegal,
    mean length 95.1.
R6  MaskablePPO.learn on CartPole-v1 (no action_masks method): ValueError "Environment does not
    support action masking. Consider using ActionMasker wrapper". learn(..., use_masking=False) ran.
R7  ActionMasker(Renamed(), "legal_moves").action_masks(): TypeError "Renamed.legal_moves() takes 1
    positional argument but 2 were given". ActionMasker(env, lambda e: e.legal_moves()) worked.
R8  make_vec_env(..., n_envs=4) (DummyVecEnv): get_action_masks shape (4, 6) after reset; learn ran.
    Calling Hanoi.action_masks() before any reset raises AttributeError ('Hanoi' object has no
    attribute 's'); MaskablePPO resets before its first call, so only hand-written code hits this.
R9  make_vec_env(..., n_envs=2, vec_env_cls=SubprocVecEnv) ran learn() both with Hanoi's own
    action_masks and with ActionMasker(TimeLimit(Hanoi()), lambda ...).
R10 MaskablePPO seed 0, learn(50_000): 54 s. Then 100 deterministic evaluation episodes on a
    separate TimeLimit(Hanoi(), 100) reset with seed 1000:
      SB3 evaluate_policy (no mask):          mean return -33.22, mean length 40.4, 35 cut at 100
      sb3-contrib evaluate_policy (masked):   mean return   1.09, mean length  9.9,  0 cut at 100
    (returns are undiscounted sums, as both functions compute them.)
R11 Plain PPO vs MaskablePPO, seed 0, learn(50_000) each on TimeLimit(Hanoi(), 100), gamma=0.9,
    then the greedy policy (predict deterministic=True; MaskablePPO given the true mask) run from
    each of the 80 non-goal starts for at most 100 moves, illegal moves as hanoi.py's no-op:
      PPO, no mask:  44 s; 15 moves from state 0 (fewest 15); fewest moves from 73 of 80 starts;
                     1 start never reaches the goal, making 100 illegal moves
      MaskablePPO:   48 s; 15 moves from state 0; fewest moves from 77 of 80 starts; 0 stuck;
                     0 illegal
R12 Plain PPO, seed 0, learn(50_000) ran 51,200 steps (25 rollouts of 2,048); 14,510 were illegal
    no-ops. Illegal fraction by block of 10,240 steps: 0.510, 0.488, 0.344, 0.066, 0.009.
R13 MaskableCategorical on the paper's example, logits [1,1,1,1], mask [T,T,F,T]: probabilities
    [0.3333, 0.3333, 0, 0.3333]; gradient of log π'(a0) w.r.t. the logits
    [0.6667, -0.3333, -0, -0.3333]; unmasked Categorical [0.75, -0.25, -0.25, -0.25]; gradient of
    the masked entropy w.r.t. the logits all zero at uniform legal logits. Matches the paper's
    Eq. 1 and Eq. 6 (p. 2).
```

R11 setup in full (R12 is the same plain-PPO training with a wrapper that appends
`not legal(self.unwrapped.s)[a]` on every step):

```python
# dependency block: agent.py's, plus "sb3-contrib==2.9.2"
import numpy as np, torch
from gymnasium.wrappers import TimeLimit
from stable_baselines3 import PPO
from sb3_contrib import MaskablePPO
from hanoi import Hanoi, legal, after, GOAL, N
torch.set_num_threads(1)
MASK = np.array([legal(s) for s in range(N)]) == 1
# F[s]: fewest moves to the goal, by breadth-first search over MASK and after(), as leak.py does
def greedy_run(model, s, masked, cap=100):
    illegal = 0
    for t in range(cap):
        if s == GOAL:
            return t, illegal
        kw = {"action_masks": MASK[s]} if masked else {}
        a = int(model.predict(s, deterministic=True, **kw)[0])
        if MASK[s, a]:
            s = after(s, a)
        else:
            illegal += 1
    return cap, illegal
for cls, masked in [(PPO, False), (MaskablePPO, True)]:
    model = cls("MlpPolicy", TimeLimit(Hanoi(), max_episode_steps=100), gamma=0.9, seed=0)
    model.learn(50_000)
    # tally greedy_run(model, s, masked) over s in range(GOAL)
```

## Course record (not sources to cite)

From `./nb history --show` for both lessons. The indentation below comes from the published HTML
in the library checkout, because `--show` strips it; the text is otherwise the same as `--show`
prints.

### hanoi.py, from `action-masking-in-q-learning` (17 November)

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["gymnasium==1.4.0", "numpy"]
# ///
"""The Tower of Hanoi with four disks, as a Gymnasium environment whose
legal moves change with the state. A mask of the legal moves comes with
every observation, in info["action_mask"], and from action_masks().
"""
import gymnasium as gym
import numpy as np

DISKS = 4
N = 3**DISKS  # a state s: digit k of s in base 3 is the peg of disk k
GOAL = N - 1  # every disk on peg 2
MOVES = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]  # (from, to)


def tops(s):
    """The smallest disk on each peg, or DISKS for an empty peg."""
    top = [DISKS] * 3
    for k in reversed(range(DISKS)):  # largest first, so the smallest wins
        top[s // 3**k % 3] = k
    return top


def legal(s):
    """A new int8 array, 1 for each move that takes a disk from a nonempty
    peg to an empty peg or onto a larger disk, and 0 for the others."""
    top = tops(s)
    return np.array([top[a] < top[b] for a, b in MOVES], dtype=np.int8)


def after(s, m):
    """The state after legal move m: its peg's top disk changes peg."""
    a, b = MOVES[m]
    return s + (b - a) * 3 ** tops(s)[a]


class Hanoi(gym.Env):
    """An episode starts in a random state other than the goal, or in
    options["start"], and terminates when all four disks are on peg 2.
    Each move pays -1, and the move that completes the tower pays +10."""

    def __init__(self):
        self.observation_space = gym.spaces.Discrete(N)
        self.action_space = gym.spaces.Discrete(len(MOVES))

    def action_masks(self):
        """The same mask as booleans, under the name MaskablePPO calls."""
        return legal(self.s).astype(bool)

    def reset(self, *, seed=None, options=None):
        super().reset(seed=seed)
        start = (options or {}).get("start")
        self.s = int(self.np_random.integers(GOAL) if start is None else start)
        return self.s, {"action_mask": legal(self.s)}

    def step(self, action):
        if legal(self.s)[action]:
            self.s = after(self.s, action)
        # An illegal move leaves every disk where it is and pays -1.
        terminated = self.s == GOAL
        reward = 10.0 if terminated else -1.0
        return self.s, reward, terminated, False, {"action_mask": legal(self.s)}


if __name__ == "__main__":
    import re
    import warnings

    from gymnasium.utils.env_checker import check_env

    env = Hanoi()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        check_env(env)  # raises if any of its assertions fails
    print("check_env passed")
    for w in caught:
        print("  ", re.sub(r"\x1b\[\d+m", "", str(w.message))[:66] + "...")
    pairs = sum(legal(s).sum() for s in range(N))
    print(f"{N} states, {N * len(MOVES)} state-move pairs, {pairs} legal")
    s, info = env.reset(seed=0, options={"start": 0})
    print("reset:", s, info)
    print("action_masks():", env.action_masks())
    env.action_space.seed(0)
    mask = info["action_mask"]
    print("sample(mask=...):", [int(env.action_space.sample(mask=mask))
                                for _ in range(8)])
    print("step(4), illegal:", env.step(4))
    print("step(0), legal:  ", env.step(0))
```

Printed output of `uv run hanoi.py` on that page:

```text
check_env passed
   WARN: Not able to test alternative render modes due to the environ...
81 states, 486 state-move pairs, 240 legal
reset: 0 {'action_mask': array([1, 1, 0, 0, 0, 0], dtype=int8)}
action_masks(): [ True  True False False False False]
sample(mask=...): [1, 1, 1, 0, 0, 0, 0, 0]
step(4), illegal: (0, -1.0, False, False, {'action_mask': array([1, 1, 0, 0, 0, 0], dtype=int8)})
step(0), legal:   (1, -1.0, False, False, {'action_mask': array([0, 1, 1, 1, 0, 0], dtype=int8)})
```

API hanoi.py exposes:

```text
Dependency line   # dependencies = ["gymnasium==1.4.0", "numpy"]
Constants         DISKS = 4; N = 81 (3**DISKS); GOAL = 80 (N - 1); MOVES = [(0, 1), (0, 2), (1, 0),
                  (1, 2), (2, 0), (2, 1)], an action is an index into MOVES
Functions         tops(s) -> list of 3 ints; legal(s) -> new np.int8 array of 6, 1 = legal;
                  after(s, m) -> int, the state after legal move m (no legality check)
Class             Hanoi(gym.Env), no constructor arguments
                    observation_space Discrete(81); action_space Discrete(6)
                    action_masks() -> np.bool_ array of 6, from self.s (exists only after reset)
                    reset(*, seed=None, options=None) -> (s, {"action_mask": int8 array});
                      random start in 0..79 from np_random, or options={"start": s}
                    step(action) -> (s, reward, terminated, False, {"action_mask": int8 array});
                      illegal move = no-op paying -1; +10 on reaching GOAL, -1 otherwise;
                      never truncates (the lesson used TimeLimit(Hanoi(), max_episode_steps=100))
                  No render method; gymnasium's check_env passes with one render-mode warning.
Main block        only under __main__, so `from hanoi import ...` runs nothing.
```

Neighbouring files from the same lesson that the writer may import: masked_q.py defines
`GAMMA, EPS, ALPHA = 0.9, 0.2, 0.5` (line 13), `greedy(Q, s, mask)` and `q_learning(...)`.
leak.py defines `MASK`, `NEXT`, `REWARD`, `LIVE`, `resting_point`, `fewest_moves()` (breadth-first
fewest moves to the goal from every state) and `moves_from(Q, s, rng=None, cap=100)`; importing
leak.py runs `EXACT = resting_point()` (500 value-iteration sweeps) at module level.

### agent.py, from `training-an-off-the-shelf-agent` (8 November)

```python
# /// script
# requires-python = ">=3.10"
# dependencies = ["gymnasium==1.4.0", "stable-baselines3==2.9.2", "torch==2.14.1"]
#
# [[tool.uv.index]]
# name = "pytorch-cpu"
# url = "https://download.pytorch.org/whl/cpu"
# explicit = true
#
# [tool.uv.sources]
# torch = { index = "pytorch-cpu", marker = "sys_platform == 'linux'" }
# ///
"""Stable-Baselines3's PPO trained on SlipperyGrid, and the policy it ends
with, read off as a probability for each move in each cell."""

import gymnasium as gym
import numpy as np
import torch
from estimators import GAMMA
from grid_env import SlipperyGrid
from gridworld import N
from gymnasium.wrappers import TimeLimit
from stable_baselines3 import PPO

LIMIT, STEPS = 200, 50_000
torch.set_num_threads(1)  # so a seed's run does not depend on the core count


class Returns(gym.Wrapper):
    """Records the discounted return, at the course's GAMMA, of every
    episode the agent trains on. SB3's own log sums rewards undiscounted."""

    def __init__(self, env):
        super().__init__(env)
        self.G = []

    def reset(self, **kwargs):
        self.g, self.t = 0.0, 0
        return self.env.reset(**kwargs)

    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        self.g += GAMMA**self.t * reward
        self.t += 1
        if terminated or truncated:
            self.G.append(self.g)
        return obs, reward, terminated, truncated, info


def train(seed, steps=STEPS):
    """PPO with the course's discount and every other setting at SB3's
    default. Returns the model and the returns of its training episodes."""
    env = Returns(TimeLimit(SlipperyGrid(), max_episode_steps=LIMIT))
    model = PPO("MlpPolicy", env, gamma=GAMMA, seed=seed)
    model.learn(total_timesteps=steps)
    return model, np.array(env.G)


def move_probs(model):
    """probs[s, a], the probability the policy gives move a in cell s."""
    obs, _ = model.policy.obs_to_tensor(np.arange(N))
    with torch.no_grad():
        return model.policy.get_distribution(obs).distribution.probs.numpy()


def greedy_moves(model):
    """The frozen greedy policy as a table: the most probable move in each
    cell, the move model.predict returns with deterministic=True."""
    moves = move_probs(model).argmax(axis=1)
    for s in range(N):
        assert model.predict(s, deterministic=True)[0] == moves[s]
    return moves
```

API agent.py exposes, and what carries over to Hanoi:

```text
Dependency lines  gymnasium==1.4.0, stable-baselines3==2.9.2, torch==2.14.1, torch from the
                  explicit "pytorch-cpu" index on Linux only (marker sys_platform == 'linux');
                  elsewhere torch comes from PyPI. Adding "sb3-contrib==2.9.2" to this list
                  resolves (R0).
Constants         LIMIT, STEPS = 200, 50_000; module-level torch.set_num_threads(1)
Class             Returns(gym.Wrapper): records each training episode's return at GAMMA in .G
Functions         train(seed, steps=STEPS) -> (model, np.array of training returns), hard-wired
                  to SlipperyGrid and PPO; move_probs(model) and greedy_moves(model) read the
                  policy over np.arange(N) with N from gridworld (16 cells).
Imports           estimators (GAMMA = 0.9 per the 8 Nov page), grid_env (SlipperyGrid), gridworld
                  (N) at module level.
```

`from agent import ...` needs estimators.py, grid_env.py and gridworld.py in the same folder, and
train, move_probs and greedy_moves are SlipperyGrid-specific (16 cells, SlipperyGrid hard-coded).
Only Returns, the dependency block and the PPO(..., gamma=GAMMA, seed=seed) pattern carry over to
Hanoi. MaskablePPO's policy exposes the same obs_to_tensor and get_distribution, and
get_distribution also takes action_masks (sb3-contrib policies.py lines 355–368), so a Hanoi
version of move_probs is a two-line change. The 8 November lesson's baselines came from
baselines.py (`exact_value`, `returns`, `EXACT`), printed in an earlier lesson that is outside
this brief; seeds.py called `returns(eval_env, lambda obs, rng: int(moves[obs]), EPISODES,
1000 + seed)`.

## Contradictions

1. **The commission says the agent "needs no invented consequence (penalty, no-op)" for an illegal
   move. The environment still needs one.** sb3-contrib's docs say check_env steps with
   unmasked random actions (ppo_mask.md lines 92–96), and the plain-PPO baseline sends illegal
   actions to step (R12: 14,510 of 51,200). hanoi.py already defines the no-op at −1. The claim
   holds for MaskablePPO, which never sent an illegal action in training (R2) or in masked
   evaluation (R5, R10). It does not hold for the environment.

2. **The paper's penalty matched masking on its smallest map, and plain PPO learned Hanoi in one
   seed.** Table 2 (p. 5): on 4×4, r_invalid = −0.01 reached r_episode 40.00, equal to masking;
   masking reached 40 sooner (t_solve 8.67% vs 14.32%). The penalty's collapse begins at 10×10.
   Hanoi has 6 actions with 240 of 486 state-move pairs legal, about half. That is a far smaller
   invalid space than 4×4 µRTS, where a random Source Unit is valid with probability 0.125. In R11
   plain PPO under the no-op rule solved the start in the minimum 15 moves and took the fewest
   moves from 73 of 80 starts, against 77 for MaskablePPO. The difference that showed was in
   training (R12: 28% of steps illegal, falling from 0.510 to 0.009 by block) and in one start
   where plain PPO's greedy policy repeats an illegal no-op forever. A comparison built on the
   final greedy policy alone may show a small gap. One seed is not a result.

3. **"The trained agent picks illegal moves" without the mask: true on Hanoi, and harsher there
   than in the paper.** Masking removed in the paper still scored 17.32–33.53 against masking's
   40.00 (Table 2; pp. 5–6, "Masking removed still behaves to some extent"). On Hanoi a
   deterministic policy that picks an illegal no-op stays in the same state and picks it again, so
   one illegal argmax traps the episode until the time limit (R10: 35 of 100 episodes cut at 100
   with SB3's evaluate_policy; R5). The severity comes from hanoi.py's no-op rule combined with
   deterministic evaluation, not from masking alone.

4. **sb3-contrib docs vs source on unmasked environments.** The docs' code comment says
   "MaskablePPO behaves the same as SB3's PPO unless the env is wrapped with ActionMasker"
   (ppo_mask.md lines 117–120). The source raises ValueError when the env has no action_masks
   method and use_masking is left at its default True (ppo_mask.py lines 216–217); R6 confirmed.
   It behaves like PPO only with learn(..., use_masking=False).

5. **sb3-contrib docs vs source on ActionMasker with a method name.** The docs say ActionMasker can
   "specify the name" of a differently named mask method (ppo_mask.md lines 89–90), and the
   docstring accepts "the name of such a method" (action_masker.py lines 15–16). The code calls
   the bound method with the env as an extra argument (lines 23, 32), and R7 raised TypeError. The
   test (test_action_masker.py lines 43–52) never calls action_masks(). The callable form works.

6. **sb3-contrib docs vs a run on SubprocVecEnv.** The docs say ActionMasker cannot be used with
   SubprocVecEnv (ppo_mask.md lines 51–54). R9 trained with ActionMasker under SubprocVecEnv on
   Linux with the default forkserver start method. The warning may hold on other platforms or
   start methods; that was not tested.

7. **Inside the paper.** The prose says agents with r_invalid = −0.01 on 10×10 "spent 3.43% of the
   entire training time just discovering the first reward" (p. 5). Table 2 gives 3.43% for
   r_invalid = −1.00 on 10×10 and 1.57% for −0.01. The prose also cites "Figure 3" and "Figures
   3d" for KL and masking-removed results (p. 6), which are in the appendix figure on p. 9; the
   body figure is Figure 2 (p. 4). Cite Table 2's numbers, not the prose's.

8. **"Introduced" vs "analysed".** The brief names the paper as the one that "introduced or
   analysed" masking. The paper says masking was already common (Vinyals et al. 2017, Berner et
   al. 2019, Ye et al. 2020) and that it supplies the first detailed description and justification
   (pp. 1–2). sb3-contrib's docs link the technique to this paper (ppo_mask.md line 9;
   ppo_mask.py line 30). A Go-deeper line should say "analysed".

9. **The paper's "masking" was partial.** Its mask covered only the Source Unit and Attack Target
   Unit components, and "invalid actions still could be sampled" (p. 4, strategy 2). MaskablePPO
   on Hanoi masks every illegal action. The paper's masking rows are therefore not a full-mask
   result.

## Numbers

```text
Figure: sb3-contrib 2.9.2, files uploaded 2026-10-26T09:51:48Z
Owner:  PyPI JSON for sb3-contrib; GitHub release v2.9.2 (26 Oct)
Scope:  latest release as of 2026-11-18
```

```text
Figure: sb3-contrib 2.9.2 requires stable_baselines3 >=2.9.2,<3.0; Python >=3.10
Owner:  PyPI JSON info.requires_dist / requires_python
Scope:  release 2.9.2
```

```text
Figure: stable-baselines3 2.9.2 requires torch >=2.8,<3.0; gymnasium >=0.29.1,<2.0
Owner:  PyPI JSON for stable-baselines3 2.9.2
Scope:  release 2.9.2
```

```text
Figure: torch 2.14.1 uploaded 2026-09-30; torch 2.15.0 uploaded 2026-10-28 (latest)
Owner:  PyPI JSON for torch
Scope:  as of 2026-11-18
```

```text
Figure: masked logit value -1e8 (float, the logits' dtype)
Owner:  sb3-contrib distributions.py line 59
Scope:  every masked categorical outcome, Discrete/MultiDiscrete/MultiBinary
```

```text
Figure: MaskablePPO defaults n_steps 2048, batch_size 64, n_epochs 10, gamma 0.99
Owner:  sb3-contrib ppo_mask.py lines 81–84
Scope:  constructor defaults, same as SB3 PPO
```

```text
Figure: learn(50_000) runs 51,200 environment steps (25 rollouts of 2,048) with one env
Owner:  researcher run R12 (follows from n_steps 2048)
Scope:  PPO or MaskablePPO, n_envs = 1
```

```text
Figure: Hanoi: 81 states, 486 state-move pairs, 240 legal; 15 moves minimum from state 0
Owner:  course record (hanoi.py output; leak.py), 17 November lesson
Scope:  four-disk puzzle
```

```text
Figure: Paper Table 2, r_episode (average return over the last 10 episodes), 4 seeds, 500,000 steps
Owner:  Huang and Ontañón, arXiv v3 p. 5, Table 2
Scope:  µRTS harvesting, by map size; maximum shown 40 except naive masking on 4×4 (59.61)
        Map      Masking   Penalty -1   -0.1    -0.01   0      Masking removed   Naive masking
        4×4      40.00     0.00         30.00   40.00   30.25  33.53             59.61
        10×10    40.00     0.00         0.00    0.50    0.25   25.93             40.00
        16×16    40.00     0.25         0.75    1.00    1.00   17.32             40.00
        24×24    40.00     0.00         0.25    0.50    0.50   17.37             38.50
```

```text
Figure: Paper Table 2, t_solve (% of training steps until the 10-episode moving average exceeds 40)
        and t_first (% until the first positive reward)
Owner:  Huang and Ontañón, arXiv v3 p. 5, Table 2
Scope:  "-" = never reached
        Map      Masking t_solve / t_first   Penalty -0.01 t_solve / t_first   Penalty -1 t_first
        4×4      8.67% / 0.07%               14.32% / 0.51%                    0.53%
        10×10    11.13% / 0.05%              -      / 1.57%                    3.43%
        16×16    11.47% / 0.08%              -      / 0.44%                    0.44%
        24×24    18.38% / 0.07%              -      / 1.92%                    1.40%
```

```text
Figure: Paper Table 2, a_null (invalid Source Unit selections per episode, last 10 episodes),
        masking removed: 63.57 (4×4), 128.76 (10×10), 165.12 (16×16), 150.06 (24×24)
Owner:  Huang and Ontañón, arXiv v3 p. 5, Table 2
Scope:  agent trained with the mask, evaluated without it
```

```text
Figure: plain PPO illegal training steps, 14,510 of 51,200; by 10,240-step block
        0.510, 0.488, 0.344, 0.066, 0.009
Owner:  researcher run R12 (single seed 0; not for publication without a rerun)
Scope:  hanoi.py under TimeLimit 100, gamma 0.9, SB3 defaults otherwise
```

```text
Figure: MaskablePPO 50k steps, deterministic predict without masks illegal in 10 of 80 states;
        SB3 evaluate_policy mean return -33.22 (35/100 episodes cut at 100 moves) vs
        sb3-contrib evaluate_policy 1.09 (0/100 cut)
Owner:  researcher run R10 (single seed 0)
Scope:  100 deterministic episodes, separate evaluation env seeded 1000, undiscounted returns
```

```text
Figure: wall time for learn(50_000), one torch thread: 44 s (PPO), 48 s and 54 s (MaskablePPO,
        two separate runs)
Owner:  researcher runs R10, R11
Scope:  this container's CPU; a laptop will differ
```

## Limits

- The FLAIRS PDF galley (journals.flvc.org/FLAIRS/article/download/130584/133937) returned 403 and
  a browser-style retry was not permitted in this session, so page and figure locators are to
  arXiv v3, the authors' posted copy of the accepted paper. Whether FLAIRS paginates identically is
  not established.
- The paper does not say plainly whether "masking removed" was scored by separate evaluation runs
  during training or only at the end. Table 2 gives t_solve for it, which implies a curve over
  training, but the protocol is not spelled out (p. 4, strategy 4).
- No source tests masking against a penalty on an action space as small as Hanoi's. The paper's
  smallest map (4×4) is the nearest case, and there the penalty matched masking's final return.
- R0–R13 are the researcher's single-seed checks on Linux x86_64, CPU, one thread. SB3 does not
  promise identical results across PyTorch releases or platforms (cited in the 8 November lesson),
  so the writer's own runs will differ in detail. uv resolution was not tried on macOS or Windows,
  where agent.py's marker sends torch to PyPI.
- The SubprocVecEnv result (R9) covers Linux with forkserver only.
- baselines.py (the 8 November lesson's random and scripted baselines) was outside this brief's
  item 4, and its listing is not recorded here.
- Everything else the brief asked was established: the current release and its pins, uv
  resolution, each mask-handling question in item 2 with file and line, and the paper's
  masking-vs-penalty experiment with section, table and figure locators.

## Source assets

```text
Asset: Huang and Ontañón, Table 2 (arXiv v3 p. 5), the full-width results table
Shows: masking at r_episode 40.00 on every map beside the penalty rows falling to 0.00–1.00 from
       10×10 up, and masking-removed scores with their a_null counts
Crop:  keep the caption ("Results averaged over 4 random seeds") and the column header; keep the
       Invalid action penalty and Invalid action masking blocks; the Masking removed block is worth
       keeping if the page cites it; the Naive block can go. arXiv licence is the non-exclusive
       distribution licence; the FLAIRS version is CC BY-NC 4.0.
```

```text
Asset: Huang and Ontañón, Figure 2 (arXiv v3 p. 4), panels (a) 4×4 and (b) 10×10 episodic return
Shows: on 4×4 several strategies reach 40; on 10×10 the penalty curves stay near 0 while masking
       climbs early, over 5×10^5 steps
Crop:  keep panels (a) and (b) with their shared legend and axes; panels (c) and (d) (KL
       divergence) can go, since PPO's KL is stage 5 material
```

```text
Asset: sb3-contrib source and docs pages
Shows: None found that carries more than a quoted line would. The docs' MicroRTS result images
       (docs/images/4x4_*.png, 10x10_*.png) are dark TensorBoard screenshots of 3 unlabelled seeds,
       and the "combined" images the page references (4x4_combined.png, 10x10_combined.png) are
       absent from docs/images at tag v2.9.2.
Crop:  -
```

```text
Asset: PyPI pages, FLAIRS article page
Shows: None found.
Crop:  -
```

## Discarded

```text
https://journals.flvc.org/FLAIRS/article/download/130584/133937: 403 to a plain request; a
  browser-style retry was not permitted; arXiv v3 read instead.
https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/docs/images/10x10_no_mask.png
  (and its 4x4/10x10 siblings): looked at as an asset; TensorBoard screenshots with unlabelled
  seeds, rejected.
https://pypi.org/project/torch/2.15.0/: the newest torch, read in the PyPI JSON; rejected as a pin
  because the course pins 2.14.1 and sb3-contrib 2.9.2 does not require a change.
```
