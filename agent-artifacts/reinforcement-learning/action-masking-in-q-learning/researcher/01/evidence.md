# Evidence: reinforcement-learning/action-masking-in-q-learning (researcher 01)

The two-place rule is well supported as practice. Gymnasium's own tutorial, "Action Masking in the Taxi Environment", lists three places to mask: random choice, greedy choice, and the max in the Q-learning update. It does that in the release docs and on main. Several value-method sources take the max over the next state's legal actions only: OpenSpiel's tabular Q-learner and DQN, the Dopamine fork in DeepMind's Hanabi Learning Environment, Zahavy et al.'s "Action Elimination Q-learning" (NeurIPS 2018, Definition 3), and He et al.'s DRRN (ACL 2016, Algorithm 1). Sutton and Barto write the action set as A(s) and initialize Q only for a in A(s), so their max ranges over legal actions without saying so. The evidence is thin in one place: no source I found isolates "mask the choice, not the target" in Q-learning and measures what it costs. The pitfall shows up in four places. Gymnasium 1.4.0's Taxi docstring gives a Q-value snippet that masks only the choice, and it returns the wrong action (fixed on main after the release). John Rothman's 2021 blog post says his team made the mistake. Tianshou 2.0.1's non-double DQN target reads unmasked outputs (my reading of the code, with no report from the maintainers). Gymnasium 1.4.0's own tutorial had a different target bug, which was also fixed after the release. The lesson's run will be the first measurement on the page. Two of the commission's premises are wrong. MaskablePPO does not read `info`: it calls an `action_masks()` method. Taxi's "masked" actions are not forbidden: they are legal no-ops that cost −1 or −10. Nothing here was executed. Package installs were refused in this session and the system Python has no numpy, so every API statement comes from reading the Gymnasium 1.4.0 and sb3-contrib 2.9.2 source and docs.

## Sources

### 1. Gymnasium 1.4.0, Taxi environment (docs page and source)

```text
URL:         https://gymnasium.farama.org/environments/toy_text/taxi/
             source: https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/envs/toy_text/taxi.py
Kind:        primary. Gymnasium's maintainers (Farama Foundation) document and implement their own environment.
Establishes: firsthand, what Taxi puts in info, the mask's dtype and meaning, and what a masked action does.
Paraphrase:  reset() and step() both return info with keys "prob" and "action_mask". action_mask() builds a fresh
             np.zeros(6, dtype=np.int8) and sets 1 for each action that will change the state: a move not blocked by
             the grid edge or a wall, pickup only at the passenger's location, dropoff only with the passenger aboard
             at one of the four designated locations. A masked action is still accepted by step(). A move into a
             wall leaves the state unchanged and costs the usual −1; an illegal pickup or dropoff leaves the state
             unchanged and costs −10. Only Taxi-v4 is registered in 1.4.0 (max_episode_steps=200). Among Gymnasium
             1.4.0's built-in environments, Taxi is the only one that emits action_mask (grep of the gymnasium/
             package at tag v1.4.0: only taxi.py and the Discrete/MultiDiscrete spaces mention it).
Locators:    taxi.py at v1.4.0: docstring "## Rewards" (lines 113–119), "## Information" (lines 130–141);
             _pickup/_dropoff (lines 185–211); action_mask() (lines 417–436); step() return (line 467);
             reset() return (line 485). Registration: gymnasium/envs/__init__.py lines 167–172.
Quote:       "“action_mask”: if actions will cause a transition to a new state. This was added in v0.25.0"
             "An action that results a noop, like moving into a wall, will incur the time step penalty. Noops can be
             avoided by sampling the `action_mask` returned in `info`."
             "Or with a Q-value based algorithm ``action = np.argmax(q_values[obs, np.where(info["action_mask"] == 1)[0]])``."
```

The last quote is itself evidence. `np.argmax` over the legal subset returns a position in that subset, not an action number. With legal actions [1, 3], it returns 0 or 1. The snippet also masks only the choice and says nothing about the target. I worked this out by reading the code, not by running it. The maintainers' later fix (source 2) confirms it.

### 2. Gymnasium main after 1.4.0: Taxi docstring fix (PR #1812)

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/pull/1812
             commit: https://github.com/Farama-Foundation/Gymnasium/commit/8d92e8fa44bfd54ded9bb15b053fbdb11fb9f5a5
             rendered: https://gymnasium.farama.org/main/environments/toy_text/taxi/
Kind:        primary. The maintainers' own change to their docstring.
Establishes: the 1.4.0 snippet was wrong. It is fixed on main and not yet in a release.
Paraphrase:  "Docs: fix the environment docstrings and pages", by pseudo-rnd-thoughts, merged 2026-10-23. In taxi.py
             it replaces the snippet with valid = np.where(info["action_mask"] == 1)[0] and then
             action = valid[np.argmax(q_values[obs, valid])], and writes sample(mask=...) with the keyword. It also adds
             a paragraph: pickup is illegal unless the taxi is at the passenger, dropoff is illegal unless the passenger
             is aboard at a designated location, and dropping at a designated location other than the destination is
             legal (−1, passenger left there). PyPI's latest Gymnasium on 2026-11-17 is 1.4.0 (uploaded 2026-10-05), so
             the release docs page at gymnasium.farama.org still shows the old snippet.
Locators:    git diff v1.4.0..main of gymnasium/envs/toy_text/taxi.py, docstring "## Information" and "## Rewards".
Quote:       "``action = valid[np.argmax(q_values[obs, valid])]``."
```

### 3. Gymnasium 1.4.0, `Discrete.sample(mask=...)`

```text
URL:         https://gymnasium.farama.org/api/spaces/fundamental/#gymnasium.spaces.Discrete.sample
             source: https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/spaces/discrete.py
Kind:        primary. The API reference and its implementation.
Establishes: the exact signature and how a mask is checked and used.
Paraphrase:  sample(mask=None, probability=None); passing both raises ValueError. The mask must be an np.ndarray of
             dtype np.int8 and shape (n,), holding only 0s and 1s. Each condition is an assert, so a bool array fails
             with "The expected dtype of the sample mask is np.int8". The sample is uniform over the positions where
             mask == 1, drawn with the space's own generator (self.np_random, seeded by action_space.seed()). If every
             entry is 0, it returns space.start, which is action 0 for Discrete(n). It does not raise. probability= takes a
             float64 distribution that must sum to 1. The file is unchanged between v1.4.0 and main.
Locators:    discrete.py lines 127–196 (sample); docstring lines 134–141; the int8 assert at lines 154–156; the
             all-zero branch at lines 166–171. Base signature: gymnasium/spaces/space.py lines 96–110.
Quote:       "Expected `np.ndarray` of shape ``(n,)`` and dtype ``np.int8`` where ``1`` represents valid actions and ``0``
             invalid / infeasible actions. If there are no possible actions (i.e. ``np.all(mask == 0)``) then
             ``space.start`` will be returned."
```

### 4. Gymnasium tutorial, "Action Masking in the Taxi Environment"

```text
URL:         release (1.4.0): https://gymnasium.farama.org/tutorials/training_agents/action_masking_taxi/
             main: https://gymnasium.farama.org/main/tutorials/training_agents/action_masking_taxi/
             added by PR #1345 (dantp-ai, merged 2025-07-02): https://github.com/Farama-Foundation/Gymnasium/pull/1345
             fixed by PR #1811 (merged 2026-10-23): https://github.com/Farama-Foundation/Gymnasium/pull/1811
Kind:        primary for what Gymnasium documents as the masking procedure for Q-learning.
Establishes: Gymnasium itself states that the max in the update runs over the next state's legal actions only.
Paraphrase:  The intro lists three places to mask: exploration (random choice from legal actions), exploitation
             (argmax over legal Q-values), and the update (max over the next state's legal actions, read from the next
             step's info["action_mask"], with 0 if none are legal). The experiment compares masking in all three
             places with no masking at all, using 12 seeds, 5000 episodes, α=0.1, γ=0.95, ε=0.1 on Taxi-v4. It never
             masks the choice alone, so it does not isolate the target. The 1.4.0 code skips the update whenever
             terminated or truncated is true. PR #1811 says this meant "the +20 drop-off reward was never learned and
             truncation never bootstrapped". On main the update runs on every step with
             td_target = reward + γ(1 − terminated)·next_max, and random choice uses env.action_space.sample(mask=...).
             The release page still shows the 1.4.0 code.
Locators:    docs/tutorials/training_agents/action_masking_taxi.py at v1.4.0: intro "How Action Masking Works"
             (lines 26–35), train_q_learning (lines 50–137), the update (lines 110–127), "Results Analysis"
             (lines 273–295). Main's version: same sections, update at main lines 106–127.
Quote:       "3. During Q-learning updates: We compute the maximum future Q-value only over valid actions in the next state"
```

### 5. Gymnasium 1.4.0, environment checker

```text
URL:         https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/env_checker.py
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/passive_env_checker.py
Kind:        primary. Implementation of check_env, which the course taught in checking-a-custom-environment.
Establishes: two constraints on a masked environment's design.
Paraphrase:  (a) check_env steps with env.action_space.sample() and no mask (check_step_determinism, line 218;
             check_returned_data_not_reused, line 287; the passive step check, line 478). So a masked environment must
             still give every action in Discrete(n) a defined outcome. That rules out raising on an illegal action and
             means picking a convention such as a no-op or ending the episode. (b) check_returned_data_not_reused
             (lines 273–303, called at line 482) fails if two reset/step calls return info entries that share memory,
             tested with np.shares_memory (passive_env_checker.py lines 206–214). An environment that returns a row of
             a precomputed mask table without .copy() fails with "The infos returned by ... share an object". Taxi
             passes because it builds a new array on every call.
Locators:    env_checker.py lines 204–235, 273–303, 406–482; passive_env_checker.py lines 179–218.
```

### 6. sb3-contrib 2.9.2, MaskablePPO

```text
URL:         https://sb3-contrib.readthedocs.io/en/v2.9.2/modules/ppo_mask.html
             source: https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/maskable/utils.py
                     https://github.com/Stable-Baselines-Team/stable-baselines3-contrib/blob/v2.9.2/sb3_contrib/common/wrappers/action_masker.py
Kind:        primary. The library's docs and code.
Establishes: MaskablePPO gets masks by calling a method on the environment. It does not read info.
Paraphrase:  get_action_masks(env) calls env.get_wrapper_attr("action_masks")() (or env_method on a VecEnv);
             EXPECTED_METHOD_NAME = "action_masks". An environment either defines action_masks() itself or is wrapped
             with ActionMasker(env, action_mask_fn), where action_mask_fn takes the env and returns the mask. The docs'
             example environment returns True for valid actions. The distribution converts any mask to torch.bool and
             replaces invalid logits with −1e8. The docs warn that MaskableEvalCallback and the maskable evaluate_policy
             must replace SB3's versions, that SubprocVecEnv needs action_masks() on the environment itself (ActionMasker
             cannot be used), and that check_env samples actions without the mask. MaskablePPO is the only masked
             algorithm in sb3-contrib 2.9.2. QR-DQN has no mask support. The docs cite Huang and Ontañón (arXiv 2006.14171).
             The course pins stable-baselines3==2.9.2, which matches this sb3-contrib release (2026-10-26).
Locators:    docs page "Notes", "Example", the two Warnings; utils.py lines 5–19; action_masker.py lines 44–69;
             sb3_contrib/common/maskable/distributions.py lines 46–70.
Quote:       "InvalidActionEnvDiscrete has a action_masks method that returns the invalid action mask (True if the action
             is valid, False otherwise)."
```

### 7. Huang and Ontañón, "A Closer Look at Invalid Action Masking in Policy Gradient Algorithms"

```text
URL:         https://arxiv.org/abs/2006.14171 (v3, 31 May 2022; v1 25 June 2020)
             published: FLAIRS-35 (2022), https://doi.org/10.32473/flairs.v35i.130584
Kind:        primary for its own proof and experiments. Secondary for the history: it says other work used masking first.
Establishes: what the paper usually cited for masking actually shows. It covers policy gradients only. It does not
             claim to have introduced masking, and it says nothing about value methods or Q-learning targets.
Paraphrase:  Authors: Shengyi Huang and Santiago Ontañón, College of Computing & Informatics, Drexel University
             (Ontañón marked "Currently at Google"). The paper says masking was already used by Vinyals et al. 2017
             (StarCraft II), Berner et al. 2019 (Dota 2) and Ye et al. 2020 (MOBA), and that those papers describe it only
             briefly. Masking replaces invalid logits with M = −1×10^8 before the softmax. Proposition 1 proves that the
             resulting gradient is the policy gradient of the masked policy π′θ, treating the mask as a state-dependent
             differentiable function. The experiments run PPO with 4 seeds on a µRTS resource-harvesting task over
             4×4, 10×10, 16×16 and 24×24 maps. They compare an invalid-action penalty (r_invalid ∈ {0, −0.01, −0.1, −1},
             described as standard since Dietterich 2000), masking, "naive" masking (sample from the masked distribution
             but take the gradient through the unmasked one), and masking removed at evaluation. Masking solved every
             map. The penalty did not scale past 4×4. Naive masking reached high return but its KL divergence between
             PPO updates was much higher, and its time to solve varied more with map size.
Locators:    Introduction and "Invalid Action Masking" (pp. 1–2); "Masking Still Produces a Valid Policy Gradient",
             Proposition 1 (p. 3); "Strategies to Handle Invalid Actions" (p. 4); Table 2 (p. 5); "Evaluation Results"
             (pp. 5–6); "Related Work", "Conclusions" (p. 6). Page numbers are arXiv v3.
Quote:       "Existing work (Vinyals et al. 2017; Berner et al. 2019) seems to treat invalid action masking as an
             auxiliary detail, usually describing it using only a few sentences."
```

### 8. Vinyals et al., "StarCraft II: A New Challenge for Reinforcement Learning" (2017)

```text
URL:         https://arxiv.org/abs/1708.04782
Kind:        primary.
Establishes: an early documented use of masking, in a policy-gradient agent (A3C) and in supervised learning from
             replays. Nothing on value targets.
Paraphrase:  The agents never choose unavailable actions: the policy masks the function-identifier choice a0 and
             renormalizes the distribution over it. In supervised learning from replays, the mask is the union of the
             actions available over the past 8 frames, and it sets the probability of the others to near zero.
Locators:    Section 4.2 "Policy Representation" (arXiv p. 9); Section 5.2 "Policy Predictions" (arXiv p. 16).
Quote:       "we mask out the function identifier choice a0 such that only the available subset can be sampled. We
             implement this by masking out actions and renormalising the probability distribution over a0."
```

### 9. He et al., "Deep Reinforcement Learning with a Natural Language Action Space" (DRRN, ACL 2016)

```text
URL:         https://aclanthology.org/P16-1153/ (arXiv 1511.04636)
Kind:        primary.
Establishes: an early value-method algorithm whose action set depends on the state in both the choice and the target.
             It predates Huang and Ontañón and the 2017 StarCraft paper.
Paraphrase:  Authors from the University of Washington and Microsoft Research. Text games give a list of feasible
             actions A_t in each state. Exploration is a softmax over A_t (Eq. 2). Each replay transition stores the next
             state's action set, and the target is y_k = r_k + γ max over a′ ∈ A_{k+1} of Q(s_{k+1}, a′). The network
             scores only the listed actions, so it has no masked column to leak.
Locators:    Section 2.1, Eq. (2) (arXiv p. 2); Algorithm 1, lines 11–14 (arXiv p. 5).
```

### 10. Zahavy, Haroush, Merlis, Mankowitz and Mannor, "Learn What Not to Learn: Action Elimination with Deep Reinforcement Learning" (NeurIPS 2018)

```text
URL:         https://arxiv.org/abs/1809.02121
Kind:        primary.
Establishes: a value-method paper that states both places as a definition. Its actions are eliminated by a learned
             signal, not forbidden by rules.
Paraphrase:  Authors at the Technion, Google Research and DeepMind. Definition 3 defines Action Elimination Q-learning
             as updating only admissible pairs and choosing the best next-state action among admissible ones.
             Proposition 1 gives convergence to the optimal Q-function on valid pairs, under its elimination assumptions.
             In AE-DQN, ACT() is ε-greedy over the admissible set, and Targets() takes the max over admissible actions
             only. The authors say this reduces function approximation errors, but they do not measure that part on
             its own.
Locators:    Section 3.3, Definition 3 and Proposition 1 (arXiv p. 6); Section 4 "Method" (p. 6); Algorithm 1 (p. 7).
Quote:       "Action Elimination Q-learning is a Q-learning algorithm which updates only admissible state-action pairs
             and chooses the best action in the next state from its admissible actions."
```

### 11. OpenSpiel (Google DeepMind), tabular Q-learner and PyTorch DQN

```text
URL:         https://github.com/google-deepmind/open_spiel/blob/4956843d7375e29a4c986425c66f897d7ac15340/open_spiel/python/algorithms/tabular_qlearner.py
             https://github.com/google-deepmind/open_spiel/blob/4956843d7375e29a4c986425c66f897d7ac15340/open_spiel/python/pytorch/dqn.py
Kind:        primary. The code is the behaviour.
Establishes: a maintained library masks both places, in a tabular learner and in DQN with replay.
Paraphrase:  Tabular QLearner: _epsilon_greedy gives ε/len(legal_actions) to each legal action and splits 1 − ε among the
             legal greedy ones, which is Sutton and Barto's ε-greedy over A(s). The update's target is
             reward + γ·max over the legal actions of the new state (zero at a terminal step). DQN: each replay transition
             stores legal_actions_mask, built from the next time step's legal actions. The target sets illegal entries to
             torch.finfo(torch.float).min before the max. Exploration draws from legal_actions, and the greedy choice
             takes the argmax of q_values[legal_actions] and maps it back to the action.
Locators:    tabular_qlearner.py lines 66–87 (_epsilon_greedy), 105–158 (step), target at lines 138–141;
             pytorch/dqn.py lines 31, 36–42 (Transition), 444–459, 480–495, 541–545.
```

### 12. Hanabi Learning Environment (Google DeepMind), Rainbow/DQN agents, a fork of Dopamine

```text
URL:         https://github.com/google-deepmind/hanabi-learning-environment/blob/54e79594f4b6fb40ebb3004289c6db0e34a8b5fb/hanabi_learning_environment/agents/rainbow/dqn_agent.py
             .../agents/rainbow/rainbow_agent.py (same commit)
Kind:        primary.
Establishes: Dopamine-based DQN code that adds the mask in the target. This is the Dopamine instance the brief asked
             about. I did not check Dopamine's own repository for a legal-action input.
Paraphrase:  The header says the file "is a fork of the original Dopamine code incorporating changes for the multiplayer
             setting and the Hanabi Learning Environment". Legal actions arrive as an additive vector: 0 for legal, −inf
             for illegal. Exploration chooses at random among the zeros. The greedy action is argmax(Q + legal). The
             target is reduce_max(next_qt + next_legal_actions). The Rainbow agent's next-state argmax adds the same
             vector.
Locators:    dqn_agent.py lines 18–19 (fork note), 186–198, 230–238, 335–355, 385–417; rainbow_agent.py lines 171–172, 205–206.
```

### 13. Tianshou 2.0.1, DQN

```text
URL:         https://github.com/thu-ml/tianshou/blob/v2.0.1/tianshou/algorithm/modelfree/dqn.py
Kind:        primary for the code. The reading below is mine, and no maintainer has confirmed it.
Establishes: in at least one maintained library, one configuration masks the choice but not the target max.
Paraphrase:  forward() masks with obs.mask when choosing the action, but returns the raw network output as logits.
             _target_q() uses those logits. With is_double=True (the default), it indexes them at the action chosen
             under the mask, so the target stays legal. With is_double=False ("Nature DQN"), it returns
             target_q.max(dim=1)[0] over the unmasked logits. A GitHub issue search for "mask target" and
             "mask is_double" in thu-ml/tianshou found no report of this. The v2.0.1 file matches master
             (f2402056) byte for byte.
Locators:    forward lines 101–143; compute_q_value lines 145–151; add_exploration_noise lines 153–175; _target_q lines
             365–379.
```

### 14. John Rothman, "Valid actions in the context of RL learning" (blog, 24 Oct 2021)

```text
URL:         https://johnrothman.wordpress.com/2021/10/24/valid-actions-in-the-context-of-rl-learning/
Kind:        primary only for a first-person report that his team made this mistake. A practitioner blog with no
             stated affiliation, so it carries little weight on anything else.
Establishes: someone reported making exactly this mistake. It gives no measurement.
Paraphrase:  Masking the argmax is obvious, but the loss can be overlooked, and the max in the target must run over
             feasible actions. His team's mistake "went unnoticed for a while". His fix code is itself defective.
             It calls next_q_values.masked_fill(...) without assigning the result (masked_fill is not in place), and
             it fills with −1, which is only safe if every legal value exceeds −1. The TensorFlow variant multiplies
             by the mask after taking the max.
Locators:    paragraphs 4–6 and the two code blocks.
Quote:       "It would be obvious that when selecting the max action to make sure to remove infeasible actions, but the
             loss calculation can be overlooked. This was a mistake my team made that went unnoticed for a while."
```

### 15. PettingZoo 1.27.0, AEC API, "Action Masking"

```text
URL:         https://pettingzoo.farama.org/api/aec/
Kind:        primary.
Establishes: putting the mask in info is one convention among several, even within Farama.
Paraphrase:  Masking is optional and can go in the observation or in info. PettingZoo Classic environments use
             observation["action_mask"]. Shimmy's OpenSpiel environments use info["action_mask"]. Sampling is
             env.action_space(agent).sample(mask).
Locators:    section "Action Masking".
Quote:       "action masking is optional, and can be implemented using either `observation` or `info`."
```

### 16. RLlib (Ray 2.60.0), action-masking example

```text
URL:         https://github.com/ray-project/ray/blob/ray-2.60.0/rllib/examples/rl_modules/action_masking_rl_module.py
Kind:        primary.
Establishes: RLlib's shipped masking example puts the mask in a Dict observation and supports PPO only.
Paraphrase:  The example's RLModule reads "action_mask" from a gymnasium.spaces.Dict observation, derives from
             PPOTorchRLModule, and raises ValueError("This example only supports PPO...") for any other algorithm.
Locators:    module docstring lines 1–20; lines 88–109.
```

### 17. Sutton and Barto, Reinforcement Learning: An Introduction, 2nd ed. (MIT Press 2018; authors' PDF dated 2020)

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf (book page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary.
Establishes: the definitions the lesson leans on, with printed page numbers.
Paraphrase:  A(s) is "set of all actions available in state s". The agent selects A_t ∈ A(s), and footnote 3 says the
             book sometimes assumes the same set in every state and writes A. The derivation of the Bellman optimality
             equation (3.19) opens with v*(s) = max over a ∈ A(s) of q_π*(s, a). Later lines and (3.20) for q* write max_a. An ε-greedy policy gives each
             nongreedy action ε/|A(s)| and the greedy action 1 − ε + ε/|A(s)|, and ε-soft means π(a|s) ≥ ε/|A(s)|. The
             Q-learning update (6.8) writes its max as max_a Q(S_{t+1}, a) with no set named. The boxed algorithm
             initializes Q(s, a) "for all s ∈ S+, a ∈ A(s)", so Q exists only on legal pairs and the max can only range
             over A(S_{t+1}). That last step is my inference from the box. The book does not say it about masking.
             Section 14.3 says choosing the sets A(s) "can radically simplify learning".
Locators:    Summary of Notation, p. xx; Section 3.1, p. 48 and footnote 3; Section 3.6, pp. 63–64, eqs (3.19)–(3.20);
             Section 5.4, p. 100; Section 6.5, p. 131, eq (6.8) and the boxed algorithm; Section 14.3, p. 359.
Quote:       "To simplify notation, we sometimes assume the special case in which the action set is the same in all
             states and write it simply as A." (p. 48, footnote 3)
             "Initialize Q(s, a), for all s ∈ S+, a ∈ A(s), arbitrarily except that Q(terminal, ·) = 0" (p. 131)
```

### 18. Dietterich, "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition" (JAIR 13:227–303, 2000)

```text
URL:         https://www.jair.org/index.php/jair/article/view/10266 (arXiv cs/9905014)
Kind:        primary. Taxi's original definition.
Establishes: where Taxi's "no-op with a penalty" convention comes from.
Paraphrase:  Six deterministic primitive actions. The reward is −1 per action, +20 for delivering the passenger, and
             −10 for attempting Pickup or Putdown illegally. A navigation action into a wall is a no-op with the
             usual −1.
Locators:    Section 3.1 "A Motivating Example" (arXiv p. 9), Figure 1.
Quote:       "There is a reward of −10 if the taxi attempts to execute the Putdown or Pickup actions illegally. If a
             navigation action would cause the taxi to hit a wall, the action is a no-op, and there is only the usual
             reward of −1."
```

## Contradictions

1. **MaskablePPO does not use `info`.** The commission calls exposing the mask through `info` "the convention MaskablePPO and Gymnasium's own environments such as Taxi use". Only the Taxi half is true. MaskablePPO calls `env.action_masks()`, directly or through `ActionMasker(env, fn)` (source 6). The conventions differ in more than the channel. Gymnasium's `Discrete.sample` asserts dtype `np.int8` with 1 for legal. Taxi returns int8. sb3-contrib's example returns booleans, and its code converts any mask to bool. PettingZoo Classic and RLlib's example put the mask in the observation dict instead (sources 15, 16). An environment that serves both Gymnasium-style loops and MaskablePPO needs `info["action_mask"]` and an `action_masks()` method, or an `ActionMasker` function that rebuilds the mask from the state.

2. **Taxi's masked actions are not forbidden.** The commission's topic is "removal of actions that the environment forbids", and it cites Taxi as the model. Taxi's mask marks actions "that will cause a transition to a new state" (source 1). Every masked action is still executable: a wall move is a −1 no-op and an illegal pickup or dropoff is a −10 no-op. Dietterich's original Taxi has the same rewards (source 18). So Taxi is the "no-op with a penalty" convention with an advisory mask on top. Under that convention the masked pairs are real pairs of the MDP with well-defined values. The lesson's new environment, where illegal actions are meant to have no defined outcome, is a different design from Taxi. It still has to give every action some outcome to pass `check_env` (source 5).

3. **Gymnasium's own Taxi docstring masks only the choice, and with a wrong index, in the current release.** In 1.4.0 the Q-value snippet masks only the greedy choice and returns a position within the legal subset (source 1). Main fixed the index on 2026-10-23 (source 2), but the fixed docstring still says nothing about the target. Meanwhile the tutorial on the same site states the target rule (source 4). If the lesson says "Gymnasium documents the two-place rule", that holds for the tutorial and not for the Taxi page.

4. **Gymnasium 1.4.0's tutorial contradicts the course's termination-and-truncation lesson.** It skips the update on terminated or truncated steps. The +20 reward was never learned and truncation never bootstrapped (PR #1811's own words, source 4). The release docs page still shows that code. Do not copy the 1.4.0 listing. Main's version uses R + γ(1 − terminated)·max over legal actions, which matches the course's target.

5. **The tutorial's experiment does not test the target.** It compares masking in all three places with masking nowhere (source 4). Its listed benefits ("Faster convergence", "Better performance") come from that comparison. They do not show what masking the target adds on top of masking the choice.

6. **Huang and Ontañón's text and Table 2 disagree.** The text says masking's t_solve "is roughly 12% and very similar across different map sizes", but Table 2 gives 8.67%, 11.13%, 11.47% and 18.38%. The text attributes 3.43% of training spent finding the first reward to r_invalid = −0.01 on 10×10. Table 2 gives 3.43% to r_invalid = −1.00 there and 1.57% to −0.01. Cite Table 2, not the prose.

7. **In policy gradients, "masked in one place only" is not uniformly worse on return.** Huang and Ontañón's naive masking samples from the masked policy but takes the gradient through the unmasked one. It had the highest r_episode on 4×4 (59.61 against masking's 40.00), tied on 10×10 and 16×16, and was slightly lower on 24×24 (38.50). Its cost showed as larger KL between updates and a t_solve that grew with map size (49.14% on 24×24). The paper covers policy gradients only. A sentence that compares it with the Q-learning bug is an analogy and has to say so.

8. **When the leak vanishes or flips.** This is my reasoning from the update rule. No source states it, and the writer should test it. Under "mask the choice only", an illegal pair is never taken, so its estimate stays at its initial value. In a table that value is fixed, and it enters the target only when it exceeds the largest legal estimate in the next state. With zero initialization and rewards that are mostly negative (Taxi's −1 per step), the frozen zeros sit above every legal estimate. Every state with an illegal action then gets the target r + γ·0, which is the leak at its worst. With zero initialization and positive values, the frozen zeros eventually fall below the legal maximum and the leak fades. Initializing illegal entries to −∞ masks the target with no explicit mask, as long as no illegal action is ever taken. If one is taken, the update computes −∞ + α(target + ∞), which is NaN. That is one more reason to mask exploration. The commission's "case the explanation fits worst" is the sign of the rewards relative to the initial value.

9. **Sutton and Barto never write A(S_{t+1}) under the max in (6.8).** Their restriction comes from the domain of Q, which the box initializes only on legal pairs (source 17). "The book's rule already masks the target" is an inference from that domain. The book does not state it.

10. **Two Gymnasium edge cases that fail silently or loudly.** `Discrete.sample` with an all-zero mask returns action 0 and does not raise. A bool mask raises an AssertionError (source 3). Taking the max over an empty legal set (a terminal next state whose mask is all zeros) raises in numpy. Main's tutorial guards it with `next_max = 0` and also multiplies by (1 − terminated).

I looked for a source that says masking the target is unnecessary in Q-learning and found none.

## Numbers

```text
Figure: Taxi mask, np.int8 array of shape (6,), 1 = action changes the state
Owner:  Gymnasium 1.4.0 taxi.py action_mask(), lines 417–436
Scope:  every reset() and step() info, Taxi-v4
```

```text
Figure: Taxi rewards, −1 per step, +20 for delivery, −10 for illegal pickup or dropoff, wall move a −1 no-op
Owner:  Gymnasium 1.4.0 taxi.py docstring lines 113–119; Dietterich 2000 Section 3.1
Scope:  per step, Taxi-v4 (max_episode_steps = 200)
```

```text
Figure: Discrete.sample mask, dtype np.int8, shape (n,), values 0/1; all-zero mask returns space.start
Owner:  Gymnasium 1.4.0 discrete.py lines 134–171
Scope:  Gymnasium 1.4.0, unchanged on main as of 2026-11-17
```

```text
Figure: Gymnasium tutorial setup, 12 seeds × 5000 episodes, α = 0.1, γ = 0.95, ε = 0.1
Owner:  action_masking_taxi.py (v1.4.0 lines 154–159; same on main)
Scope:  Taxi-v4, masked everywhere vs masked nowhere. The page reports results only as a plot.
```

```text
Figure: masked logit values: −1×10^8 (Huang and Ontañón; sb3-contrib HUGE_NEG); torch.finfo(float).min (OpenSpiel DQN);
        −inf (HLE); logits.min() − logits.max() − 1 (Tianshou)
Owner:  sources 7, 6, 11, 12, 13
Scope:  implementation constants, for the writer's choice of fill value
```

Huang and Ontañón, Table 2 (PPO, 4 seeds, µRTS harvest). This is the full series, in case a chart is wanted. The lesson is about Q-learning, so it probably is not.

```text
Figure: probability a random Source Unit choice is valid, 2/16 = 0.125 (4×4) and 2/576 = 0.0034 (24×24)
Owner:  Huang and Ontañón, "Evaluation Environment" (p. 4)
Scope:  per action, µRTS maps of those sizes
```

```text
Figure: r_episode (average return, last 10 episodes), maps 4×4 / 10×10 / 16×16 / 24×24
        masking                         40.00 / 40.00 / 40.00 / 40.00
        penalty r_invalid = 0           30.25 /  0.25 /  1.00 /  0.50
        penalty r_invalid = −0.01       40.00 /  0.50 /  1.00 /  0.50
        penalty r_invalid = −0.1        30.00 /  0.00 /  0.75 /  0.25
        penalty r_invalid = −1           0.00 /  0.00 /  0.25 /  0.00
        naive masking                   59.61 / 40.00 / 40.00 / 38.50
        masking removed (eval)          33.53 / 25.93 / 17.32 / 17.37
Owner:  Huang and Ontañón, Table 2 (p. 5)
Scope:  last 10 episodes of training, 4 seeds
```

```text
Figure: t_solve (% of training steps until the moving average of return exceeds 40)
        masking 8.67% / 11.13% / 11.47% / 18.38%; naive masking 11.74% / 13.97% / 30.59% / 49.14%
Owner:  Huang and Ontañón, Table 2 (p. 5)
Scope:  same runs
```

## Limits

- No source isolates "mask the choice, not the target" for Q-learning and measures its effect. Any number the lesson prints for that comparison is new. The pitfall is "known" only in a weak sense: one first-person blog, one wrong docstring in Gymnasium's current release, one configuration of Tianshou (my code reading), and a tutorial that states the rule without testing it.
- I found no source that says one paper introduced invalid-action masking. Huang and Ontañón say it was already in use and was treated as a detail. The earliest instances I opened are DRRN (2016, value method, a state-dependent set in the target) and the StarCraft II environment paper (2017, policy gradients). I did not search the pre-2016 game-playing or tabular literature.
- Nothing was executed. Installing gymnasium==1.4.0 and sb3-contrib in a scratch venv was refused by this session's permission check, and the system Python has no numpy. The API behaviour above comes from reading tagged source and the rendered docs. The writer's runs will be the first check that the names work as stated. The asserts and return values are simple enough that I expect them to hold.
- No source measures whether the leak is worse under function approximation. Zahavy et al. assert that masking the target reduces approximation error but do not isolate it. A sentence on generalization has to be marked as not run, or the writer has to run it.
- I read the Hanabi agents' code, not the Hanabi challenge paper (Bard et al. 2020), so the code is the only citation for Dopamine-style masking.
- I checked only RLlib's shipped example (PPO only). I did not check RLlib 2.60's documentation for DQN masking, or the forum advice to set "hiddens": [] and "dueling": False for masked DQN.
- I did not establish when the main-branch fixes (sources 2 and 4) will reach a release. If a Gymnasium 1.4.1 or later ships before publication, the release docs will change.

## Source assets

```text
Asset: none found that should carry the argument. The Gymnasium Taxi page, Discrete.sample, the tutorial, MaskablePPO,
       OpenSpiel, HLE and Tianshou are text and code. A listing quoted in a figure caption does better than a screenshot.
```

```text
Asset: Sutton and Barto p. 131, the boxed "Q-learning (off-policy TD control)" algorithm (Section 6.5)
Shows: Q initialized only "for all s ∈ S+, a ∈ A(s)" while the update writes max_a, which is the gap a fixed-width
       table opens
Crop:  keep the Initialize line and the update line together, with the box title. Omit the exercises above it. The
       box is easy to retype as an equation instead.
```

```text
Asset: Huang and Ontañón, Figure 2 (a)–(b) (p. 4), episodic return over training steps on 4×4 and 10×10 for masking, the
       four penalties, naive masking and masking removed
Shows: in PPO, the penalty convention stops learning as the invalid share grows, and masking does not
Crop:  keep panels (a) and (b) with the shared legend. Omit the KL panels (c)–(d) unless the naive-masking analogy is
       used. The figure is policy gradients, which the commission limits to one sentence, so this is optional.
```

```text
Asset: Dietterich 2000, Figure 1 (Taxi domain grid)
Shows: the original Taxi layout
Crop:  not needed, since the lesson builds its own environment. Listed only for completeness.
```

```text
Asset: Gymnasium tutorial plot "taxi_v3_action_masking_comparison.png" on the release page
Shows: masked-everywhere vs unmasked learning curves on Taxi-v4
Crop:  do not use. It comes from the 1.4.0 code with the terminal-step bug, and it does not test the target.
```

## Discarded

```text
https://arxiv.org/abs/2004.00980 (Kanervisto, Scheller and Hautamäki, "Action Space Shaping in Deep Reinforcement Learning", 2020): masking only in policy-gradient agents on StarCraft II minigames; nothing on value targets.
https://gist.github.com/vwxyzjn/83b765decf4654fa7ad6094c4ec98af2 (action_masking_dqn.py, 2021): an uncommented gradient demo that masks both places; a gist is not a document of record and adds nothing beyond sources 11–12.
https://github.com/ray-project/ray/issues/47537: a user reports masked DQN training failing under Ray 2.34; no diagnosis and no replies.
https://github.com/DLR-RM/stable-baselines3/issues/1876 and /issues/580: users asking how to mask DQN or use a dynamic A(s); no analysis of the target.
https://github.com/tensorflow/agents/issues/255 and /issues/727: usage questions about observation_and_action_constraint_splitter; nothing on the target.
https://github.com/JuliaPOMDP/DeepQLearning.jl/issues/68 and /issues/77: feature requests for masking; no analysis.
https://github.com/thu-ml/tianshou/issues (searched "mask target", "mask is_double"): no issue about the unmasked non-double target.
https://github.com/Farama-Foundation/Gymnasium/pull/1804: the umbrella documentation PR, closed unmerged; its changes landed in #1811 and #1812, which are cited instead.
```
