# Evidence: reinforcement-learning/time-awareness (researcher 01)

The commission's one idea comes from Pardo, Tavakoli, Levdik and Kormushev
(ICML 2018). In Section 2 they say that when a time limit is part of the task,
the remaining time belongs in the state, and a state without it breaks the
Markov property. Their TD target, Eq. (4), stops at every termination,
including the time limit. Harada (AAAI 1997), the precedent Pardo et al.
credit, gives the simplest case where the optimal action changes with the
remaining time. A risky move pays off only on the last step. Harada also argues
that running standard Q-learning on (state, time) works but wastes data when the
dynamics do not depend on time. Gymnasium 1.4.0 (5 October 2026) is still the
current release. Gymnasium's own docs say that a time limit built into the task
ends the episode with terminated and that the remaining time must be observed.
Gymnasium's tools do not do either of these things. `TimeAwareObservation` adds
the number of steps taken so far, not the steps remaining, although its own
parameter description says "remaining". `TimeLimit` always reports the limit as
truncated. No 1.4.0 wrapper reports a step count as terminated. The record is
thin in three places. I could not run the wrapper, because this session blocked
code execution, so its behaviour on the grid's `Discrete(16)` observations comes
from reading the 1.4.0 source. No primary measures whether a time feature hurts
generalisation. The commission's description of "Pardo et al.'s second failure"
does not match how the paper frames it (see Contradictions).

## Sources

### Core (the page will likely use these)

```text
URL:         https://proceedings.mlr.press/v80/pardo18a.html
             (PDF: https://proceedings.mlr.press/v80/pardo18a/pardo18a.pdf)
Kind:        primary. The authors propose time-awareness and own its definition,
             equations and experiments.
Establishes: firsthand: the time-limited objective, the claim that the remaining
             time is part of the state, the time-indexed value and TD target, and
             the Last Moment, Two-Goal Gridworld, Queue of Cars and MuJoCo
             experiments.
Paraphrase:  Fabio Pardo, Arash Tavakoli, Vitaly Levdik and Petar Kormushev
             (Robot Intelligence Lab, Imperial College London; footnote, p. 4045),
             "Time Limits in Reinforcement Learning", Proceedings of the 35th ICML,
             PMLR 80:4045-4054, 2018. The paper separates two cases. In (i) the
             task is to maximise return over a fixed period. In (ii) the limit
             only diversifies training. In case (i) "the terminations due to time
             limits are in fact part of the environment", so a notion of the
             remaining time must be part of the agent's input "to avoid violation
             of the Markov property" (Abstract, p. 4045).
             The Introduction (p. 4045) says the remaining time "is an inherent
             part of the environment's state and is essential to its Markov
             property", and names the approach time-awareness (TA). Section 2
             (p. 4047) treats reaching the limit as "transitioning to a terminal
             state". The environment's states therefore "contain a notion of the
             remaining time used by its transition function". The time-dependent
             MDP is "a stack of T time-independent MDPs followed by one that only
             transitions to a terminal state". A time-unaware agent acts in a POMDP
             "where states that only differ by their remaining time appear
             identical", which they call state-aliasing. A time-unaware agent
             also sees termination as random, with a probability that depends on
             its behaviour policy. Staying in the start state for a whole episode
             makes termination from it look like probability 1/T, and always
             moving away makes it look like 0. The fix is to include "the
             remaining time T − t in the agent's representation of the
             environment's state or by providing a way to infer it" (p. 4047).
             Eq. (3), p. 4047: v_π(s, T − t) = E_π[G_{t:T} | S_t = s].
             Eq. (4), p. 4047: y = r "at all terminations", and
             y = r + γ v̂_π(s′, T − t − 1) "otherwise". The limit is one of
             the terminations.
             p. 4047, right column: without the remaining time, the agent's
             updates for the same state sometimes bootstrap and sometimes do not,
             depending on whether the limit was hit. "These conflicting updates
             ... result in an inaccurate average." With a fixed limit, "the
             inclusion of the elapsed time t would be sufficient". They "chose to
             always represent the remaining time" for generality.
             Section 2.1, Last Moment (p. 4047): two states, A and B. "Stay" in A
             pays 0. "Jump" moves to B and pays 1. B is a trap that pays −1 per
             step. The best play is to jump on the last step. "For a
             time-unaware agent, the task is impossible to master for T > 1 and
             the best feasible policy would be to stay in place". A time-aware
             agent stays for T − 1 steps and then jumps.
             Section 2.2, Two-Goal Gridworld (pp. 4047-4048): deterministic grid
             with goals worth 50 (top right) and 20 (bottom left). There are 5
             actions (4 moves and stay). A move costs −1 and staying costs 0.
             Episodes end after 3 steps or at a goal. Start cells are random and
             exclude the goals. Tabular Q-learning uses random actions, a decaying
             learning rate and γ = 0.99. "The time-aware agent has a state-action
             value table for each time step" and learns to head for the nearest
             goal when there is time and to stay otherwise. The time-unaware agent
             treats the limit as terminal. Its greedy values next to the goals
             converge to 49 and 19. Elsewhere,
             v(s) = 2/3(−1 + γ max_{s′∈N(s)} v(s′)) + 1/3(−1), because 2/3 of its
             moves bootstrap. That agent tries for the nearest goal even when the
             goal is out of reach. They call this a "leakage of the values to
             states that are out of reach" (p. 4048). Monte Carlo methods avoid
             the leakage but still cannot solve cases like the Last Moment
             without the remaining time (p. 4048).
             Section 2.3, Queue of Cars (p. 4048): exit 9 slots ahead. The "safe"
             action advances with 50% probability. The "dangerous" action
             advances with 80% probability and has a 10% chance of a collision
             that ends the episode. Reward 1 at the exit. A time-unaware agent
             "can only learn a fixed combination of dangerous and safe actions
             based on the position". Time-aware PPO adapts to the remaining time
             (Fig. 2).
             Section 2.4 (pp. 4048-4050): PPO with and without the remaining
             time on 19 MuJoCo Gym tasks (Fig. 3). With γ = 1, time-unaware PPO
             "often diverges drastically" (Fig. 3b). On InvertedPendulum-v1,
             time-aware PPO learns how the value decays with time, and standard
             PPO "only learns a constant estimate" (Fig. 4, p. 4050). Time-aware
             Hopper learns a "photo finish" jump before the limit (Fig. 5).
             Time-aware PPO "concatenates the observations provided by the
             environment and the remaining time represented by a scalar
             (normalized from −1 to 1)" (Introduction, p. 4046).
             Section 3.1 (p. 4050): the same grid and the same Q-learning, but
             now the agent bootstraps at the limit (partial-episode
             bootstrapping). It learns "the time-unlimited optimal policy of
             always going for the most rewarding goal" (Fig. 1c).
             Discussion (p. 4052): time-unaware agents often still do well. The
             reasons given are limits so long that timeouts are rare, cues in the
             observation that correlate with time, states rarely seen at
             different remaining times, and a small discount factor. Frame stacks
             or RNNs may help "to an extent", but "including this information is
             much simpler". Time-awareness can let an agent learn open-loop
             (state-independent) policies. With a fixed start state and no
             stochastic transitions, an optimal policy "can rely only on the
             time".
Locators:    PMLR pagination 4045-4054. Abstract and Introduction p. 4045. Fig. 1
             and the PPO time-input detail p. 4046. Section 2, Eqs. (3)-(4), 2.1,
             and the start of 2.2 p. 4047. End of 2.2, Fig. 2, 2.3 and 2.4
             p. 4048. Fig. 3 and the end of Section 2 p. 4049. Figs. 4-5,
             Eqs. (5)-(6) and 3.1 p. 4050. Discussion p. 4052. The arXiv v4 PDF
             has the same page breaks: arXiv page n = PMLR page 4044 + n.
Quote:       "a notion of the remaining time should be included as part of the
             agent's input to avoid violation of the Markov property" (Abstract,
             p. 4045). The exact wording is the claim the lesson builds on.
Quote:       "This time-wise termination can be seen as transitioning to a
             terminal state whenever the time limit is reached." (Section 2,
             p. 4047)
```

```text
URL:         https://arxiv.org/abs/1712.00378v4
Kind:        primary. The same authors' revised preprint (v4, 27 Jan 2022). It
             is the version Gymnasium's tutorial links (as abs/1712.00378).
Establishes: firsthand: corrections the authors made after publication.
Paraphrase:  Same structure, equation numbers and page breaks as the PMLR
             version. Differences I checked:
             (1) Section 2.1 (p. 3) replaces "the best feasible policy would be
             to stay in place" with "The optimal stochastic strategy being to jump
             50% of the time when T = 2 and to never jump when T > 2".
             (2) Fig. 1 (p. 2) gains a panel "(a) Gridworld" that marks the goals
             50 and 20. Standard, time-awareness and PEB become (b), (c) and (d),
             and the caption adds "with T = 3 and −1 penalties for movements".
             (3) Section 2.2 (p. 4) writes v(s) = max_a q(s, a), where PMLR has
             arg max_a q(s, a).
             (4) The Fig. 4 caption (p. 6) says the time-aware agent learns "a
             function that accurately takes into account the remaining time".
             (5) The Fig. 7 caption (p. 8) says γ = 1, where PMLR says γ = 0.99.
Locators:    pp. 2, 3, 4, 6, 8 of the v4 PDF (https://arxiv.org/pdf/1712.00378v4).
Quote:       none needed.
```

```text
URL:         https://pypi.org/project/gymnasium/1.4.0/
Kind:        primary. The Farama Foundation's own release record on PyPI.
Establishes: firsthand: the current version and its date.
Paraphrase:  gymnasium 1.4.0 was uploaded 2026-10-05 (wheel at 11:02:14 UTC).
             As of 2026-11-28 it is the latest version on PyPI, and nothing has
             been released after it. Requires Python >=3.10. The previous
             release was 1.3.0 (2026-04-22).
Locators:    the release page header, and the PyPI JSON API
             (https://pypi.org/pypi/gymnasium/json, `info.version` and
             `releases`), read 2026-11-28.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/gymnasium_release_notes/#release-v1-4-0
Kind:        primary. Gymnasium's maintainers' release notes.
Establishes: firsthand: the 1.4.0 date and the changes in that release.
Paraphrase:  "v1.4.0 Released on 2026-10-05". The release adds a keyword-only
             `sort_keys` argument to `Dict` spaces (default True). Neither
             `TimeAwareObservation` nor `TimeLimit` is listed among its changes.
             `TimeAwareObservation` last changed in 1.1.0, which added "support
             for environments without a spec" (#1289).
Locators:    section "v1.4.0" (anchor #release-v1-4-0). The 1.1.0 entry is under
             #release-v1-1-0.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/observation_wrappers/#gymnasium.wrappers.TimeAwareObservation
Kind:        primary. Gymnasium's versioned API reference.
Establishes: firsthand: the signature, documented behaviour and examples of
             TimeAwareObservation in 1.4.0.
Paraphrase:  Signature: `TimeAwareObservation(env, flatten=True,
             normalize_time=False, *, dict_time_key='time')`. Summary line:
             "Augment the observation with the number of time steps taken within
             an episode." With `normalize_time=True`, time is "a normalized value
             between [0,1]", and otherwise "the current timestep is an integer".
             Time goes under the "time" key for Dict observation spaces and as
             the last element for Tuple spaces. Any other space becomes
             `Dict(obs=..., time=...)`. `flatten` applies
             `gymnasium.spaces.utils.flatten`. "No vector version of the wrapper
             exists." Change log: added in v0.18.0. v1.0.0 removed vector support
             and added `flatten` and `normalize_time`.
             The CartPole-v1 examples (limit 500) show elapsed time. The default
             call gives a 5-element Box whose last bound is 500, time 0 at reset
             and 1. after one step. `normalize_time=True` gives 0. at reset and
             0.002 after one step. `flatten=False` gives
             `'time': Box(0, 500, (1,), int32)`, with 0 at reset and 1 after one
             step.
             The Parameters list contradicts all of this: "normalize_time – if
             True return time in the range [0,1] otherwise return time as
             remaining timesteps before truncation" (see Contradictions).
Locators:    anchor #gymnasium.wrappers.TimeAwareObservation. The page is
             byte-identical to the unversioned /api/wrappers/observation_wrappers/
             (checked 2026-11-28). The /v1.4.0/ path is a real versioned build:
             /v9.9.9/ returns 404, and /v1.3.0/ differs.
Quote:       "otherwise return time as remaining timesteps before truncation"
             is quoted only because the wording is itself the error.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/_modules/gymnasium/wrappers/stateful_observation/
             (same file at the tag: https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/wrappers/stateful_observation.py)
Kind:        primary. The 1.4.0 source code.
Establishes: firsthand: what the wrapper actually computes.
Paraphrase:  `self.timesteps` is set to 0 in `reset` and incremented in `step`
             before the inner step runs, so the k-th step's observation carries
             k. Raw time is `np.array([time], dtype=np.int32)` in
             `Box(0, self.max_timesteps, dtype=np.int32)`. Normalised time is
             `time / self.max_timesteps` as float32 in `Box(0.0, 1.0)`. Both are
             elapsed steps. The limit is read from `env.spec.max_episode_steps`,
             or else from a `TimeLimit` found by walking inward through the
             wrappers. Without either, the constructor raises ValueError: "The
             environment must be wrapped by a TimeLimit wrapper or the spec
             specify a `max_episode_steps`." The order is therefore
             `TimeAwareObservation(TimeLimit(env, n))`. A `TimeLimit` placed
             outside cannot be found. For a non-Dict, non-Tuple base space the
             unflattened space is `Dict(obs=..., time=...)`, whose keys sort as
             "obs", "time". With `flatten=True` the observation is
             `spaces.flatten` of that Dict. The wrapper is an ObservationWrapper,
             and `ObservationWrapper.step` (core.py lines 571-576) passes reward,
             terminated, truncated and info through unchanged.
             My reading, not executed: in 1.4.0's spaces/utils.py, `flatten`
             turns `Discrete(n)` into a one-hot vector (lines 232-236) and
             concatenates Dict entries in key order (lines 263-269). So
             `TimeAwareObservation(TimeLimit(SlipperyGrid(), max_episode_steps=4))`
             should return a 17-element vector: 16 one-hot cell entries, then
             the elapsed step count 0-4. The dtype should be int64 for raw time
             and float64 if normalised, because Discrete's default dtype is
             int64. A tabular learner would have to turn that vector back into a
             (cell, steps) index.
Locators:    stateful_observation.py at v1.4.0. Class at line 106, docstring
             110-167, __init__ 171-256 (`normalize_time` parameter text 184-185,
             limit lookup 199-214, time space 219-226, Dict building 229-244,
             flatten 247-256), observation 258-271, step 273-286, reset 288-302.
             The docs-hosted copy matches the PyPI wheel (sha256
             1cb947c5...4fdf0e). The raw GitHub file at tag v1.4.0 is
             byte-identical to the wheel's. github.com blob pages returned 403
             through this session's proxy, which means gated, not dead.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/wrappers/misc_wrappers/#gymnasium.wrappers.TimeLimit
             (source: https://gymnasium.farama.org/v1.4.0/_modules/gymnasium/wrappers/common/)
Kind:        primary. Gymnasium's versioned API reference and source.
Establishes: firsthand: TimeLimit signals the limit only through truncated.
Paraphrase:  `TimeLimit(env, max_episode_steps)` "Limits the number of steps for
             an environment through truncating the environment if a maximum
             number of timesteps is exceeded. If a truncation is not defined
             inside the environment itself, this is the only place that the
             truncation signal is issued. Critically, this is different from the
             terminated signal that originates from the underlying environment as
             part of the MDP." In code, step increments `_elapsed_steps` and sets
             `truncated = True` when `_elapsed_steps >= _max_episode_steps`.
             `terminated` passes through unchanged. reset sets the count to 0.
             There is no option to report the limit as terminated. A search of
             the 1.4.0 gymnasium/wrappers/ directory for `terminated = True`
             finds only AtariPreprocessing's `terminal_on_life_loss`, so no
             wrapper turns a step count into termination.
Locators:    anchor #gymnasium.wrappers.TimeLimit. common.py at v1.4.0: class at
             line 43, docstring 46-88, __init__ 90-115, step 117-136
             (truncation at 133-134), reset 138-151.
```

```text
URL:         https://gymnasium.farama.org/v1.4.0/tutorials/gymnasium_basics/handling_time_limits/#termination
Kind:        primary for Gymnasium's definition of its own flags. Secondary for
             the Markov-property claim, which it takes from Pardo et al. (its
             "(Reference)" link goes to https://arxiv.org/abs/1712.00378).
Establishes: firsthand: Gymnasium classifies a limit built into the task as a
             termination. It only repeats the claim that the remaining time must
             be observed.
Paraphrase:  The page notes that it "is compatible with Gymnasium version 1.4.0".
             Under Termination, ending at a terminal state "also includes
             episodes ending in finite-horizon environments due to a time-limit
             inherent to the environment. Note that to preserve Markov property,
             a representation of the remaining time must be present in the
             agent's observation in finite-horizon environments." Under
             Truncation, a limit on an infinite-horizon task "is also different
             from time-limits in finite horizon environments as the agent in this
             case has no idea about this time-limit."
Locators:    sections "Termination" (#termination) and "Truncation" (#truncation).
```

### Optional (useful if the page takes the matching turn)

```text
URL:         https://cdn.aaai.org/AAAI/1997/AAAI97-090.pdf
             (bibliographic record: https://mlanthology.org/aaai/1997/harada1997aaai-reinforcement/)
Kind:        primary. Harada's own paper introducing QT-learning. Pardo et al.
             (p. 4047) say time was "first demonstrated" to matter in
             time-limited RL by this paper.
Establishes: firsthand: a finite-horizon game whose optimal action depends on
             the time left, and the efficiency argument for sharing each
             experience across all time indices.
Paraphrase:  Daishi Harada (Dept. EECS, Computer Science Division, University of
             California, Berkeley), "Reinforcement Learning with Time", AAAI-97,
             pp. 577-582. Abstract (p. 577): a finite-horizon problem can be
             solved "by recasting the problem as an infinite horizon problem over
             a state space extended to include time", but doing so "does not
             make use of what is known about the environment structure, and is
             therefore inefficient". Introduction (p. 577): the
             extended state-time environment "retains the Markov property".
             Risk vs. no-risk game (pp. 577-578, Fig. 1 on p. 578): from InPlay,
             "risky" wins with probability p and loses otherwise. "No-risk" wins
             with probability q and otherwise lets the player try again. With a
             horizon T and no action durations, the optimal non-stationary policy
             makes the risky move only if p > q and t = T − 1, "only make the
             risky move at the last possible moment" (p. 578). With random
             action durations, p = 0.8, q = 0.5 and T = 5, dynamic programming
             gives a table of optimal moves by time (p. 578, see Numbers).
             Section "Finite-horizon" (p. 579): standard Q-learning on X × T
             works. But because transition probabilities and rewards "do not
             depend on time", each experience (x, t) → (y, t + 1) can update
             Q((x, τ), u) for every τ. That is QT-learning. Simulation (pp.
             579-580, Figs. 2-3): on the risk vs. no-risk game without durations,
             QT-learning beats standard Q-learning even when measured per
             parameter updated.
Locators:    pp. 577 (abstract, introduction), 578 (Fig. 1, policies, table),
             579 (Eqs. 1-4, QT-learning update, simulation setup), 580 (Figs. 2-3).
             The PDF is a scan with OCR. The text layer garbles symbols (for
             example "t +-I" for "t = T − 1"), so read the page image.
Quote:       "only make the risky move at the last possible moment, when
             t = T − 1" (p. 578). This is the earliest primary statement of the
             lesson's pattern.
```

```text
URL:         http://incompleteideas.net/book/RLbook2020.pdf
             (book page: http://incompleteideas.net/book/the-book-2nd.html)
Kind:        primary. The authors' own text of Reinforcement Learning: An
             Introduction, 2nd edition (MIT Press, 2018; this PDF is © 2018, 2020).
Establishes: firsthand: the course text's definition of the Markov property.
Paraphrase:  Section 3.1, p. 49: in an MDP the probability of each S_t, R_t
             depends only on S_{t−1}, A_{t−1}. "This is best viewed as a
             restriction not on the decision process, but on the state. The state
             must include information about all aspects of the past
             agent–environment interaction that make a difference for the future.
             If it does, then the state is said to have the Markov property."
             Section 17.3, pp. 465-466: the formal version for histories. A
             state function f is Markov if any two histories it maps to the same
             state give every future test the same probability (Eq. 17.6).
             Chapter 3 Bibliographical and Historical Remarks, entry "3.3–4",
             p. 70: the MDP literature separates finite-horizon tasks, which end
             "after a particular fixed number of time steps", from
             indefinite-horizon and infinite-horizon tasks. The book's episodic
             tasks correspond to indefinite-horizon tasks.
Locators:    Section 3.1, p. 49, paragraph after Eq. (3.3). Section 17.3,
             pp. 465-466, Eqs. (17.5)-(17.6). Chapter 3 remarks, p. 70.
Quote:       "The state must include information about all aspects of the past
             agent–environment interaction that make a difference for the future.
             If it does, then the state is said to have the Markov property."
             (p. 49). The lesson can quote this wording.
```

```text
URL:         https://farama.org/Gymnasium-Terminated-Truncated-Step-API
Kind:        primary for the Farama Foundation's own design rationale. The
             Markov claim in it is a retelling of the same origin as the tutorial.
Establishes: firsthand: Gymnasium's maintainers say a task's own time limit is a
             termination and point to TimeAwareObservation for it.
Paraphrase:  "Deep Dive: Gymnasium Terminated - Truncated Step API", Farama
             Foundation, 27 October 2023, no named author. Section "Related
             Reinforcement Learning Theory": "while finite horizon tasks end due
             to a time limit, this would be considered a termination since the
             time limit is built into the task. For these tasks, to preserve the
             Markov property, it is essential to add information about 'time
             remaining' in the state. For this reason, Gym includes a
             TimeAwareObservation wrapper for users who wish to include the
             current time step in the agent's observation."
Locators:    final section, "Related Reinforcement Learning Theory", last
             paragraph.
```

```text
URL:         https://sb3-contrib.readthedocs.io/en/v2.9.2/common/wrappers.html
             (source: sb3_contrib/common/wrappers/time_feature.py in sb3-contrib 2.9.2, PyPI 2026-10-26)
Kind:        primary for the Stable-Baselines team's own wrapper and its stated
             concern. A retelling for the time-awareness idea, which it credits
             to Pardo et al.
Establishes: firsthand: a widely used library appends remaining (not elapsed)
             normalised time, and ships a mode for checking whether an agent
             overfits the time feature.
Paraphrase:  `TimeFeatureWrapper(env, max_steps=1000, test_mode=False)`: "Add
             remaining, normalized time to observation space for fixed length
             episodes." The code computes `time_feature = 1 - (self._current_step
             / self._max_steps)`, commented "Remaining time is more general". It
             supports only 1-D Box observations or a Dict with an "observation"
             Box, so it cannot wrap the grid's `Discrete(16)`. `test_mode`: "In
             test mode, the time feature is constant, equal to zero. This allow
             to check that the agent did not overfit this feature, learning a
             deterministic pre-defined sequence of actions." The code sets
             `time_feature = 1.0` in test mode, which contradicts the docstring.
Locators:    time_feature.py (2.9.2): docstring lines 12-27, __init__ 29-71,
             `_get_obs` 83-101 (time feature 92-95). The docs page section is
             "TimeFeatureWrapper". The raw GitHub file at tag v2.9.2 is
             byte-identical to the wheel.
```

## Contradictions

1. **Elapsed or remaining time, inside Gymnasium's own docs.**
   `TimeAwareObservation`'s summary line ("the number of time steps taken"), its
   code (`self.timesteps` counts up from 0) and its doctest outputs (1 and 0.002
   after one CartPole step) all give elapsed steps. Its own `normalize_time`
   parameter text says the raw value is "remaining timesteps before truncation"
   (stateful_observation.py lines 184-185, echoed on the docs page). The Farama
   blog asks for "'time remaining' in the state" and then offers this wrapper
   "to include the current time step". Pardo et al. (p. 4047) settle what
   matters here. Elapsed time is enough when the limit never varies, and they
   chose remaining time for generality. Under a fixed four-move limit with every
   episode starting at move 0, elapsed k and remaining 4 − k carry the same
   information. A page that describes the wrapper must say "elapsed", or a
   reader who checks the output will catch the page being wrong.

2. **Gymnasium's definitions do not match Gymnasium's wrappers.** Gymnasium's
   tutorial and blog both say a limit built into the task ends the episode with
   terminated, and that the remaining time must be observed. Its tools do not do
   that. `TimeLimit` always reports the limit as `truncated=True` and never
   touches terminated (common.py 133-134). `TimeAwareObservation` passes both
   flags through unchanged. No 1.4.0 wrapper turns a step count into
   termination. So `TimeAwareObservation(TimeLimit(env, 4))` gives an agent the
   time, but still calls the fourth move a truncation. For the commission's idea
   to show up in the flags, the environment itself has to count moves and return
   terminated. `TimeAwareObservation` then still needs a `TimeLimit` (or a spec
   with `max_episode_steps`) just to build, or it raises ValueError (lines
   199-214). In that stack both flags come back True on the fourth move. That
   repeats termination-and-truncation's case where the goal is reached on the
   limit's last move, and a target that tests terminated alone handles it.
   Inference, not stated by any source: a tabular learner that sees the time and
   bootstraps on truncated reads Q at (cell, 4 elapsed). No update ever starts
   from that entry, so it keeps its starting value. With a zero start the result
   matches termination by accident. With any other start, or with function
   approximation, it does not.

3. **The commission's "Pardo et al.'s second failure" is not Pardo's framing.**
   The commission describes it as "a time-unaware agent bootstrapping through
   the limit". In Pardo et al., the time-unaware agent of Section 2.2 / Fig. 1a
   does not bootstrap at the limit. It treats the limit as terminal. Its failure
   is leakage: it bootstraps from neighbours' values 2/3 of the time, values
   that are out of reach in the time it has left (p. 4048). The agent that
   bootstraps at the limit is the partial-episode-bootstrapping agent of
   Section 3.1 / Fig. 1c (p. 4050). The paper presents it as correct for a
   time-unlimited task, and it learns to head for the 50 goal whatever the time
   left. Run on the time-limited task, that agent ignores the limit. The writer
   can show either failure, but should attribute each to the right section.
   "Bootstrapping through the limit" is Section 3.1's method used on the wrong
   objective. Pardo et al. never call it a failure.

4. **Pardo's gridworld does not need a time-dependent policy.** Pardo et al.
   write of the Two-Goal Gridworld: "While the final optimal policy does not
   actually require time information" (p. 4048). Starts are at full time and
   moves are deterministic, so "go if the nearest goal is within 3 moves,
   otherwise stay" depends only on the cell. The time-unaware failure there
   comes from learning (leakage), not from a policy it cannot represent. The
   commission asks for a cell whose optimal action differs between one move
   left and several. Pardo's gridworld does not supply that. Pardo's Last
   Moment (p. 4047), Queue of Cars (p. 4048) and Harada's risk vs. no-risk game
   (p. 578) do. On the slippery grid, slips let one cell be reached with
   different numbers of moves left, which is what the commission needs. The
   writer's backward induction will confirm whether it happens.

5. **Adding time to the state is valid but wasteful (Harada).** Harada says
   Q-learning on (state, time) is correct and keeps the Markov property, but
   "does not make use of what is known about the environment structure, and is
   therefore inefficient" (p. 577). When dynamics and rewards do not depend on
   time, one experience can update every time index (QT-learning, p. 579).
   Pardo et al. (p. 4047) answer that their setting allows rewards and
   transitions that depend on time, "preventing the possibility to consider
   multiple time instances at once". The slippery grid's slip rule and
   rewards do not depend on time, so Harada's trick applies to it. A cell plus
   moves-left Q-learner that updates one entry per move learns more slowly than
   necessary. This matters only if the page compares learning speed.

6. **Time-unaware agents often do fine (scope of the problem).** Pardo et al.'s
   Discussion (p. 4052) lists the conditions: timeouts are rare when limits are
   long (ALE's 5 minutes), the observation carries cues correlated with time,
   the same state is rarely seen at different remaining times, or the discount
   factor is small. On the four-move grid none of these holds, which suits the
   lesson. A general claim that time-unaware agents fail would go beyond the
   source.

7. **Time features and generalisation: a concern, not a measured harm.** Pardo
   et al. give one primary case of a time-aware policy failing outside its
   horizon. The Hopper policy that maximises return over 300 steps "generally
   results in a photo finish which would lead to a fall ... if the simulation
   was to be extended" (p. 4049). They present open-loop, time-only policies as
   a possible benefit (p. 4052). The Stable-Baselines team ship `test_mode` in
   `TimeFeatureWrapper` precisely to check that an agent "did not overfit this
   feature, learning a deterministic pre-defined sequence of actions". That is
   a maintainers' stated concern without data. I found no primary that measures
   a time feature hurting generalisation (see Limits).

8. **Encoding conventions differ, and no primary compares them.** Pardo et
   al.'s tabular agents keep one table per time step (p. 4047). Their PPO gets
   remaining time scaled to [−1, 1] (p. 4046). Gymnasium gives elapsed steps as
   a raw int32 or scaled to [0, 1]. sb3-contrib gives remaining time scaled from
   1 down to 0. For a tabular learner the encoding is just an index. Scaling
   matters only under function approximation, and that is my judgement, not a
   finding from any source.

9. **The two versions of Pardo et al. differ.** In the Last Moment, the
   published PMLR text says the best feasible time-unaware policy is to "stay in
   place". arXiv v4 corrects this to jumping 50% of the time when T = 2 and
   never jumping when T > 2. My check with γ = 1: the expected return
   p(1 − p), against 0 for always staying, peaks at p = 0.5. The panel letters
   of Fig. 1 and the γ in the Fig. 7 caption also differ. termination-and-truncation
   cited PMLR pages. If this lesson cites the Last Moment's time-unaware policy,
   it should use the v4 wording and say so, or avoid the detail.

10. **sb3-contrib's docstring and code disagree.** The docstring says the
    test-mode constant is zero, and the code sets 1.0. This matters only if the
    page mentions `test_mode`.

## Numbers

```text
Figure: Gymnasium 1.4.0, released 2026-10-05 (PyPI wheel 11:02:14 UTC)
Owner:  PyPI release page; Gymnasium release notes #release-v1-4-0
Scope:  latest release on PyPI as of 2026-11-28; previous release 1.3.0 on 2026-04-22
```

```text
Figure: TimeAwareObservation defaults flatten=True, normalize_time=False, dict_time_key="time" (keyword-only)
Owner:  stateful_observation.py v1.4.0, lines 171-178; docs anchor #gymnasium.wrappers.TimeAwareObservation
Scope:  Gymnasium 1.4.0
```

```text
Figure: raw time = elapsed steps, int32, Box(0, max_timesteps); 0 at reset, k after the k-th step
Owner:  stateful_observation.py v1.4.0, lines 219-226, 273-302; docs doctest (CartPole-v1: 0 then 1)
Scope:  per episode; max_timesteps from env.spec.max_episode_steps or the inner TimeLimit
```

```text
Figure: normalised time = elapsed / max_timesteps, float32, Box(0.0, 1.0); CartPole-v1 after one step: 0.002
Owner:  stateful_observation.py v1.4.0, lines 219-223; docs doctest
Scope:  CartPole-v1 limit 500 steps
```

```text
Figure: TimeLimit sets truncated=True when elapsed >= max_episode_steps; terminated untouched
Owner:  common.py v1.4.0, lines 130-136; docs anchor #gymnasium.wrappers.TimeLimit
Scope:  per episode, counter reset to 0 in reset
```

```text
Figure: Two-Goal Gridworld: goals 50 (top right) and 20 (bottom left); move −1, stay 0; 5 actions; T = 3; γ = 0.99
Owner:  Pardo et al., PMLR p. 4047, Section 2.2
Scope:  deterministic grid, random start excluding goals, tabular Q-learning with random actions
```

```text
Figure: time-unaware greedy values next to the goals converge to 49 and 19
Owner:  Pardo et al., PMLR p. 4048, Section 2.2
Scope:  same setup; the limit treated as terminal
```

```text
Figure: share of a time-unaware move that bootstraps = 2/3; v(s) = 2/3(−1 + γ max v(s′)) + 1/3(−1)
Owner:  Pardo et al., PMLR p. 4048, Section 2.2
Scope:  cells not adjacent to a goal, T = 3
```

```text
Figure: perceived termination probability 1/T for an agent that stays in its start state, 0 for one that always leaves it
Owner:  Pardo et al., PMLR p. 4047, Section 2
Scope:  time-unaware agent, limit T
```

```text
Figure: Queue of Cars: exit 9 slots away; safe action advances 50%; dangerous action advances 80%, collides 10%; reward 1 at the exit
Owner:  Pardo et al., PMLR p. 4048, Section 2.3
Scope:  the time limit for this task is not stated in the text
```

```text
Figure: time-aware PPO input: remaining time as one scalar normalised to [−1, 1]
Owner:  Pardo et al., PMLR p. 4046
Scope:  all PPO experiments in Section 2
```

```text
Figure: MuJoCo limits T = 1000 (Reacher-v1 T = 50); 19 tasks; seeds 0, 1000, ..., 9000; Hopper photo finish at T = 300
Owner:  Pardo et al., PMLR pp. 4046, 4048-4050 (Fig. 3 caption, Fig. 5 caption)
Scope:  Section 2.4
```

```text
Figure: Harada risk vs. no-risk game, no durations: risky move only at t = T − 1, and only if p > q
Owner:  Harada 1997, p. 578
Scope:  InPlay state, horizon T, 0 ≤ t < T
```

```text
Figure: Harada, with durations, p = 0.8, q = 0.5, T = 5; duration probabilities for t = 1, 2, 3:
        risky 0.3, 0.7, 0.0; no-risk 0.6, 0.1, 0.3.
        Optimal move and value of InPlay by time:
        t=0 no-risk 0.9075; t=1 no-risk 0.825; t=2 risky 0.8; t=3 risky 0.8; t=4 no-risk 0.3; t=5 end
Owner:  Harada 1997, p. 578 (table)
Scope:  computed by dynamic programming with known parameters; full series kept for a possible table
```

```text
Figure: Harada simulation: initial Q uniform in [0.0, 0.1]; exploration 0.05-0.25; step size 0.005-0.1; 4 runs per setting, 100 runs per algorithm
Owner:  Harada 1997, p. 579
Scope:  risk vs. no-risk game without durations, T = 5, p = 0.8, q = 0.5
```

```text
Figure: sb3-contrib time feature = 1 − step / max_steps (default max_steps 1000); test_mode constant 1.0 in code
Owner:  sb3-contrib 2.9.2, time_feature.py lines 29, 92-95
Scope:  per episode; max_steps from env.spec.max_episode_steps when present
```

## Limits

- I could not run `TimeAwareObservation` on a `Discrete(16)` environment. This
  session's permission classifier blocked running the 1.4.0 package. The
  17-element one-hot-plus-time output and its int64/float64 dtypes are read
  from the 1.4.0 source, not observed. The writer's run settles it.
- No primary measures that a time feature hurts generalisation. The record has
  only sb3-contrib's stated concern (`test_mode`) and Pardo's Hopper horizon
  example.
- No primary compares raw, elapsed, remaining or normalised time encodings
  experimentally. Contradiction 8 is judgement.
- No primary shows the commission's grid case (one cell whose optimal action
  differs between one move left and several). The writer's backward induction
  has to show it. The sources supply only analogous cases (Harada's game,
  Pardo's Last Moment and Queue of Cars).
- Pardo et al. do not state the Queue of Cars time limit in the text, or which
  time step Fig. 1(b)'s time-aware panel shows.
- I did not check whether frame-stacking-and-the-markov-property already quotes
  Sutton and Barto, p. 49. The brief limited history lookups to
  termination-and-truncation.
- Everything else the brief asked for is established above.

## Source assets

**Pardo et al., PMLR**

```text
Asset: Fig. 1, p. 4046 (arXiv v4: p. 2): three heat maps of the Two-Goal Gridworld
       with greedy arrows. (a) Standard, (b) Time-awareness, (c) Partial-episode
       bootstrapping.
Shows: three different policies from one grid. The standard agent heads for
       the nearest goal everywhere. The time-aware agent stays in cells where
       no goal is reachable. The PEB agent heads for the 50 goal everywhere.
Crop:  keep all three panels and their letter labels together. The PMLR
       version does not mark which goal is 50 and which 20, and has no colour
       scale. The arXiv v4 Fig. 1 adds panel "(a) Gridworld" with 50 and 20
       marked, so it reads better on its own. If v4 is used, the caption must
       use v4's letters (b)-(d). Neither version says which time step the
       time-aware panel shows.
```

```text
Asset: Fig. 2, p. 4048, top right: heat maps of the probability of the
       "dangerous" action in the Queue of Cars. Left: time-aware PPO, rows =
       episode steps 0, 3, 6, 9, 14. Right: time-unaware PPO, rows = seeds 0-4.
Shows: the time-aware agent's choice in each slot changes with the remaining
       time. The time-unaware agent's choice is fixed per seed and differs
       between seeds.
Crop:  keep both y-axis labels ("episode steps", "seeds"). The two panels have
       different row meanings, and without the labels they look comparable.
       Keep the caption's key that 0 is black and 1 is white.
```

```text
Asset: Fig. 4, p. 4050, top left: 3-D surfaces of learned state value against
       episode time step and training steps, InvertedPendulum-v1, T = 1000, for
       γ = 0.99 and γ = 1.
Shows: the time-aware agent's value falls as the episode nears its limit. The
       standard agent's value is flat in time, an average over remaining times.
Crop:  keep both γ panels, the axis labels and the TA-PPO/PPO colour legend.
       The legend sits at the right edge of the figure block in the PMLR
       layout, near Fig. 5.
```

```text
Asset: inline diagram in Section 2.1, p. 4047, right column: the Last Moment
       MDP (states A and B, "stay" 0 and −1, "jump" 1).
Shows: the smallest MDP whose optimal action depends only on the time left.
Crop:  small and low resolution. Redrawing it as inline SVG would read better
       than a capture.
```

**Harada 1997**

```text
Asset: Fig. 1 and the table "Time / Optimal Move / Value", p. 578.
Shows: the game's three states, and an optimal move that switches with time.
Crop:  the page is a 1997 scan. The table is plain text and better retyped
       (values in Numbers) than captured. Fig. 1 is legible in the page image.
```

**Gymnasium docs and source, Farama blog, sb3-contrib, Sutton and Barto**

None found. These are code and prose.

## Discarded

```text
https://github.com/aravindr93/mjrl/issues/13: cited by sb3-contrib's docstring, but it is about a time-based feature in mjrl's value baseline, not about observation design. Off the lesson.
https://arxiv.org/abs/2010.04304: Reda, Tao and van de Panne, "Learning to Locomote". It covers bootstrapping at time-limit terminations (partial-episode bootstrapping, which termination-and-truncation owns) and has no discussion of time features.
https://arxiv.org/abs/2006.05990: Andrychowicz et al., "What Matters in On-Policy RL". It covers only timeout handling for bootstrapping under 1000-step limits, nothing on time in the observation.
https://gymnasium.farama.org/v1.4.0/api/env/#gymnasium.Env.step: read and consistent with the TimeLimit and tutorial entries (terminated = terminal state "as defined under the MDP of the task"; truncated = "condition outside the scope of the MDP. Typically, this is a timelimit"). termination-and-truncation already cites this page, and nothing here needs it again.
```
