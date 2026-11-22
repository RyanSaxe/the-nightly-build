# Evidence: reinforcement-learning/held-out-levels (researcher 01)

The sources support the lesson's protocol and its mention-only pointers firmly. Cobbe et al. 2019 state
that train and test levels come from one distribution so the train–test gap measures overfitting, and
they print the full train/test series against level count (Appendix E, Tables 1 and 3). Procgen's
paper, README and C++ source show exactly how a level seed is chosen from `[start_level,
start_level + num_levels)` and then seeds the level generator. Zhang et al. 2018 show agents reaching
optimal training reward on levels whose reward signs were randomized per level id, where good test
reward is impossible by design. Kirk et al. 2023 give the context/CMDP definitions and the
GenGap formula. Gymnasium 1.4.0's own docs and source settle what `reset(seed=...)` guarantees, and a
throwaway run confirmed it. Where it is thin or pushes back: no source measures the commission's own
case (a tabular learner, position-only vs local-view observations, a few hundred gridworld levels), so
every number on the page must come from the writer's runs. The level counts in the papers (thousands to
tens of thousands) do not transfer to a small grid. Four findings qualify the angle and are set out under
Contradictions. A gap can close because training return falls, so a small gap is not evidence of
learning. Architecture, regularization and exploration also move the gap, so observation and level count
are necessary conditions but do not decide the gap alone. "Cannot generalize whatever it trains on" holds
only for policies that act on the current observation, since a history-dependent agent that sees only its
position can detect walls from moves that fail. Perturbation checks on training levels miss memorization
in some agents.

## Sources

### 1. Cobbe, Klimov, Hesse, Kim, Schulman 2019, "Quantifying Generalization in Reinforcement Learning"

```text
URL:         https://arxiv.org/abs/1812.02341  (v3, 14 Jul 2019; ICML 2019, PMLR 97:1282–1289,
             proceedings page https://proceedings.mlr.press/v97/cobbe19a.html). Page numbers below are
             the arXiv v3 PDF (14 pages, includes appendices the PMLR main text omits).
Kind:        primary. The authors (all OpenAI, San Francisco, per the p. 1 affiliation line) built
             CoinRun and RandomMazes and ran every experiment they report.
Establishes: firsthand: the CoinRun and RandomMazes train/test success rates against the number of
             training levels; the protocol (levels from seeds, uniform sampling from a fixed training
             set, zero-shot test); that architecture and regularization change the gap at a fixed level
             count. Repeats (secondary within this paper): Zhang et al. 2018b's memorization finding
             (Section 2, p. 2).
Paraphrase:  Each CoinRun level is generated deterministically from a seed (§3.1, p. 2). They train 9
             PPO agents, each on a training set of a different size: 8 sets from 100 to 16,000 levels
             and one unbounded set where each level is seeded randomly from 2^32 seeds ("collisions are
             unlikely"); each episode samples uniformly from the agent's set; the whole experiment is
             repeated 5 times with training sets regenerated each time (§3.2, pp. 2–3; the LaTeX source
             confirms "$2^{32}$", which pdftotext flattens to "232"). Every agent trains 256M timesteps
             regardless of set size. Test performance is zero-shot, no fine-tuning (§3.2, p. 3). Each
             data point averages the final agent over 10,000 episodes (§3.2, p. 3). With Nature-CNN,
             "substantial overfitting occurs when there are less than 4,000 training levels. Even with
             16,000 training levels, overfitting is still noticeable" (§3.2, p. 3, Figure 2a). The
             IMPALA-CNN does better at test across all training sets (§4, p. 3, Figure 2b). L2, dropout,
             data augmentation, batch normalization and added stochasticity (epsilon-greedy, larger
             entropy bonus) each reduce the gap on a fixed set of 500 levels (§5, pp. 4–6, Figures 4–5).
             RandomMazes: square mazes of side uniform in 3–25 built with Kruskal's algorithm; the agent
             observes the 9×9 patch of cells around it; each cell is wall, empty, goal or agent; episode
             ends at the goal or after 500 timesteps; constant reward at the goal (§6.2, p. 7). They use
             an IMPALA-CNN followed by an LSTM "as memory is necessary for the agent to explore
             optimally" (§6, p. 6). RandomMazes shows "a sizeable generalization gap even when training
             on 20,000 levels" (§6.2, p. 7, Figure 8). In CoinRun-Platforms, training performance rises
             with the number of levels past a threshold, attributed to an implicit curriculum (§6.1,
             p. 7). Observations are 64×64×3 RGB in all three environments; CoinRun paints x and y
             velocity into the corner so the agent can act optimally without a frame stack (App. A.1,
             p. 9).
Locators:    §3.1 p. 2; §3.2 pp. 2–3; Figure 2 p. 3; §4 pp. 3–4; §5 pp. 4–6; §6 p. 6; §6.1 pp. 6–7; §6.2 p. 7;
             Figure 6 p. 6; Figure 8 p. 7; App. A p. 9; App. E Tables 1–3 p. 14.
Quote:       "Train and test levels are drawn from the same distribution, so the gap between train and
             test performance determines the extent of overfitting." (§3.2, p. 3). Kept because the
             lesson's claim that the gap is the measurement rests on exactly this wording.
```

### 2. Cobbe, Hesse, Hilton, Schulman 2020, "Leveraging Procedural Generation to Benchmark Reinforcement Learning"

```text
URL:         https://arxiv.org/abs/1912.01588  (v2, 26 Jul 2020; ICML 2020, PMLR 119:2048–2056,
             https://proceedings.mlr.press/v119/cobbe20a.html). Pages are the arXiv v2 PDF (19 pages).
Kind:        primary. The authors (OpenAI, San Francisco, p. 1) designed Procgen and ran its baselines.
Establishes: firsthand: the benchmark's train/test protocol (200 levels for easy, 500 for hard), the
             level-count experiment across 16 games, the deterministic-sequence ablation, the Maze
             generator, the masked-observation floor Rmin. It does not name the `num_levels` /
             `start_level` options; those are in the README and source (entry 3).
Paraphrase:  The state transition function is deterministic in all environments (§2, p. 2). Two
             difficulty settings, easy and hard, refer to the level distribution (§2.1, p. 2). Default
             training is PPO for 200M timesteps; easy environments are trained for 25M. "When evaluating
             generalization, we train on a finite set of levels and we test on the full distribution of
             levels"; the default training set is 500 levels, and "For easy difficulty environments, we
             recommend using training sets of 200 levels" (§2.2, pp. 2–3). Training sets from 100 to
             100,000 levels: "agents strongly overfit to small training sets in almost all cases. To
             close the generalization gap, agents need access to as many as 10,000 levels"; past a
             threshold, training performance improves as the training set grows, attributed to an
             implicit curriculum (§3.1, p. 4, Figure 2 p. 3). Training on a fixed sequence of levels
             (always starting at level 1) gives competent-looking training curves while test
             performance shows the agents "have in fact learned almost nothing about the underlying
             level distribution" (§3.2, p. 4, Figure 3). Maze: a mouse finds the sole piece of cheese;
             mazes from Kruskal's algorithm, size uniform from 3×3 to 25×25 (App. A.10, p. 11). By
             default the games need little or no memory; in the memory variant of Maze (and Dodgeball,
             Miner, Heist) observations are restricted to a small patch around the agent, after which
             "agents can reliably solve levels only by utilizing memory" (App. B.2, p. 13). Rmin, the
             normalization floor, "is computed by training a policy with masked out observations. This
             demonstrates what score is trivially achievable in each environment" (App. C, p. 13).
Locators:    §2 p. 2; §2.1 p. 2; §2.2 pp. 2–3; Figure 2 p. 3; §3.1–3.2 p. 4; §3.3 p. 5; App. A.10
             p. 11; App. B.2 and App. C (table of Rmin/Rmax) p. 13; App. I Figure 13 p. 19 ("trained on
             200 levels and evaluated on the full distribution of levels").
Quote:       "For easy difficulty environments, we recommend using training sets of 200 levels."
             (§2.2, p. 3). The brief asks for the 200-level locator; this is it.
```

### 3. Procgen README and C++ source (openai/procgen), with train-procgen's training script

```text
URL:         README, section "Environment Options": https://github.com/openai/procgen (master at
             commit 37b521dbb530f0734fd82f72d921f5e0e715c0d1).
             Source at that commit:
             https://github.com/openai/procgen/blob/37b521dbb530f0734fd82f72d921f5e0e715c0d1/procgen/src/vecgame.cpp
             https://github.com/openai/procgen/blob/37b521dbb530f0734fd82f72d921f5e0e715c0d1/procgen/src/game.cpp
             https://github.com/openai/procgen/blob/37b521dbb530f0734fd82f72d921f5e0e715c0d1/procgen/src/randgen.cpp
             https://github.com/openai/train-procgen/blob/1a2ae2194a61f76a733a39339530401c024c3ad8/train_procgen/train.py
             github.com HTML pages answered 403 from this session's egress proxy (gated, not dead). The
             same files were read from raw.githubusercontent.com at the pinned refs, and the commit
             SHAs were confirmed with git ls-remote. The blob URLs above are where the documents live.
Kind:        primary. Maintained by OpenAI, the benchmark's authors; the code is what executes the
             protocol the paper describes.
Establishes: firsthand: how `num_levels` and `start_level` define the level set, how a level seed is
             drawn on each reset, and that the paper's test workers use the unlimited set.
Paraphrase:  README: `num_levels=0` is "The number of unique levels that can be generated. Set to 0 to
             use unlimited levels"; `start_level=0` is "The lowest seed that will be used to generated
             levels. 'start_level' and 'num_levels' fully specify the set of possible levels";
             `distribution_mode` options include "easy" and "hard", default "hard". README also says the
             current CoinRun no longer paints velocity into observations, which "makes the environment
             significantly more difficult". vecgame.cpp lines 284–293: num_levels == 0 gives seeds in
             [0, INT32_MAX); num_levels > 0 gives [start_level, start_level + num_levels). Lines 302 and
             314–316: one generator seeded from `rand_seed` gives each game instance its own
             level-seed generator. game.cpp lines 93–117 (Game::reset): when a new level is needed,
             `current_level_seed = level_seed_rand_gen.randint(level_seed_low, level_seed_high)`, then
             `rand_gen.seed(current_level_seed)` and `game_reset()` builds the level from that seed.
             randgen.cpp lines 6–11: randint returns low + (x % (high − low)), so the upper bound is
             exclusive. So there are two generators: one picks which level, the other builds the level
             from its seed. train.py line 28: `num_levels = 0 if is_test_worker else num_levels`; the
             paper's test workers draw from all seeds, not from a disjoint held-out range.
Locators:    README "Environment Options"; vecgame.cpp L284–293, L302, L314–316; game.cpp L93–117;
             randgen.cpp L6–11; train.py L16–36.
Quote:       "'start_level' and 'num_levels' fully specify the set of possible levels." (README,
             Environment Options). Exact option names and semantics matter if the page names them.
```

### 4. Zhang, Vinyals, Munos, Bengio 2018, "A Study on Overfitting in Deep Reinforcement Learning"

```text
URL:         https://arxiv.org/abs/1804.06893  (v2, 20 Apr 2018; arXiv preprint, no journal reference
             on the abstract page). Pages are the arXiv v2 PDF (25 pages).
Kind:        primary. The four authors (addresses at google.com; the PDF prints no other affiliation
             line) built the maze environment and ran the A3C experiments.
Establishes: firsthand: memorization of up to 10,000 training mazes with random reward signs; optimal
             training reward with very different test reward depending on level count; the failure of
             sticky actions and random starts, applied to training levels, as detectors of overfitting.
Paraphrase:  Gridworld mazes BASIC (9×9 empty room), BLOCKS (13×13, 8 single-block obstacles), TUNNEL
             (13×13, generated internal walls); objects worth +1, +1, −1, −1 and a terminating key worth
             0.1; timeout −1 after 200 steps; −0.01 for walking into a wall; best possible episode
             reward 2.1 (App. A.1, p. 15). The observation is a multi-channel image with walls, each
             object's location and the agent's location in separate channels, i.e. the full map
             (App. A.1, p. 15). "The level id is a random seed that determines the initial state for
             the corresponding level"; training and test ids come from separate pools (§3, "Task Setup
             and Evaluation Protocol", p. 4; App. A.2, p. 15, "a test set of level ids that are disjoint
             from the training set"). With 10, 100, 1,000 and 10,000 training levels, training reward
             reaches optimal in all cases while test reward rises with level count; agents trained on
             10 levels "perform badly in all maze environments" (§3, "Training Optimality and
             Generalization", p. 4). Randomization test: on training levels each object's reward sign
             is flipped with probability p, fixed per level by using the level id as the seed; at
             p = 0.5 "good test performance is impossible (by design), and good training performance
             means serious overfitting"; small training sets still reach near-optimal training reward
             (§3, "Memorization Capacity of Deep RL Agents", pp. 5–6, Figure 2b; App. A.1 p. 15 calls
             this "Subsection 3.3"). Sticky actions and random starts applied to training levels at
             evaluation leave overfit agents' scores high (§4, pp. 6–8, Figures 3b and 4). In App. C,
             Agent-1 (10 TUNNEL training levels) is optimal on a training maze (Fig. 11), stuck near its
             start until timeout on a test maze (Fig. 10), robust to sticky actions even at 0.99
             (Figs. 12, 17), and trapped for the whole episode when started elsewhere on a training maze
             (Fig. 13) (C.2, pp. 20–21). Agent-3 (1,000 training levels, pure random rewards) cannot
             generalize by construction yet navigates training mazes well under random starts (C.3,
             p. 23). Conclusion of C.4: "In general, using held-out test sets is a more direct
             evaluation than applying those strategies to the training sets" (p. 24). Reported numbers
             are averages of the top 3 of 20 runs ranked by training reward (Table 2 caption p. 10;
             App. A.3 p. 16).
Locators:    §3 pp. 3–6 (subsection headings are unnumbered in the PDF; cite them by heading);
             Figure 2 p. 5; §4 pp. 6–8; §5 pp. 8–9; Table 2 p. 10; App. A.1–A.2 p. 15; App. C.2
             pp. 20–21, C.3 p. 23, C.4 pp. 23–24; Figures 10–13 pp. 19–22.
Quote:       "When p = 0.5, the sign of the reward of each object is positive or negative with equal
             probability. In this case, good test performance is impossible (by design), and good
             training performance means serious overfitting." (p. 5). Kept because the lesson's
             removal-test logic is the same construction.
```

### 5. Kirk, Zhang, Grefenstette, Rocktäschel 2023, "A Survey of Zero-shot Generalisation in Deep Reinforcement Learning"

```text
URL:         https://www.jair.org/index.php/jair/article/view/14174  (Journal of Artificial
             Intelligence Research 76 (2023) 201–264, DOI 10.1613/jair.1.14174, published 9 Jan 2023).
             arXiv copy: https://arxiv.org/abs/2111.09794 (v6, 19 Jan 2023), which carries the JAIR
             header and page numbers. Pages below are JAIR pages (PDF page n = journal page 200 + n).
Kind:        primary for its own formal definitions (CMDP as used here, ZSPT, GenGap) and its
             recommendations; secondary where it describes Procgen's protocol, which it reports from
             Cobbe et al. 2020. Authors as printed: Robert Kirk (University College London), Amy Zhang
             (University of California, Berkeley; Meta AI Research), Edward Grefenstette (University
             College London), Tim Rocktäschel (University College London).
Establishes: the train/test split as two context sets over one CMDP; GenGap; that the context must be
             observed for the CMDP to be an MDP; that a zero gap does not imply good performance.
Paraphrase:  A contextual MDP is a POMDP whose state is (underlying state, context); the context does
             not change within an episode and "takes the role of the seed, ID or parameter vector which
             determines the level" (§3.3, Definition 1, p. 208). Whether the context is observed is left
             open; "The context needs to be observed for the CMDP to be an MDP (and not a POMDP), but
             the opposite isn't true" (§3.3, p. 208). Restricting the context distribution to a subset
             gives a new CMDP (Definition 2, p. 209). Zero-shot policy transfer: pick training and
             testing context sets; learn by interacting with the training CMDP; the objective is
             expected return on the testing CMDP; the policy may be non-Markovian, a map from histories
             to actions (Definition 4, pp. 209–210; the printed text reads "Ctrain, Ctrain ⊆ C", a typo
             for Ctrain, Ctest). GenGap(π) := R(π, M|Ctrain) − R(π, M|Ctest) (Eq. 2, p. 210). "a gap of
             zero doesn't necessarily imply good performance (i.e. a random policy is likely to get a
             gap of 0)" (p. 211). The common IID assumption: training and testing contexts drawn from
             one distribution, as in Procgen, where the training set is 200 seeds and the full
             distribution is the test set (§3.6, p. 212). For PCG environments, protocol C holds out
             seeds from training and "does not test for zero-shot generalisation beyond avoiding
             memorising", and the authors recommend it as the standard RL evaluation protocol (§4.2,
             p. 220, Figure 2).
Locators:    §3.3 pp. 207–208; §3.4 pp. 209–211; §3.6 p. 212; §3.7 pp. 214–215; §4.2 pp. 219–220,
             Figure 2 p. 220; §4.3 "The Downsides of Procedural Content Generation" pp. 223–224.
Quote:       "The context needs to be observed for the CMDP to be an MDP (and not a POMDP), but the
             opposite isn't true" (p. 208). It is the formal statement nearest the lesson's
             observation argument.
```

### 6. Gymnasium 1.4.0 documentation and source (Farama Foundation)

```text
URL:         https://gymnasium.farama.org/v1.4.0/api/env/  (Env.reset, Env.np_random,
             Env.np_random_seed). The unversioned https://gymnasium.farama.org/api/env/ served text
             identical to v1.4.0 on 2026-11-22, and a nonexistent version path (/v9.9.9/) returns 404,
             so the versioned path is real.
             https://gymnasium.farama.org/v1.4.0/api/utils/  (gymnasium.utils.seeding.np_random)
             https://gymnasium.farama.org/v1.4.0/introduction/create_custom_env/  ("Reset function")
             https://gymnasium.farama.org/v1.4.0/introduction/basic_usage/
             Source at tag v1.4.0 (commit 8ba8c3a63bb4e000b7f33923f43d292acac07be1):
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/core.py
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/seeding.py
             https://github.com/Farama-Foundation/Gymnasium/blob/v1.4.0/gymnasium/utils/env_checker.py
             (github.com HTML answered 403 from this session's proxy; read via raw.githubusercontent.com
             at the tag.) Release: https://pypi.org/project/gymnasium/1.4.0/ , uploaded 2026-10-05, the
             latest on PyPI on 2026-11-22. Earlier lessons in the course pin gymnasium==1.4.0 (nb history).
Kind:        primary. The Farama Foundation maintains Gymnasium and owns the API contract.
Establishes: what reset(seed=...) does in 1.4.0, the recommended once-only seeding, and the
             seed-type check. It does not document any mechanism for keying levels to seeds or
             restricting an env to a set of levels.
Paraphrase:  reset's randomness "can be controlled with the seed parameter otherwise if the environment
             already has a random number generator and reset() is called with seed=None, the RNG is not
             reset". Passing an integer resets the generator even if it exists. The docs recommend
             seeding once, right after initialization. A custom env's first line in reset() should be
             super().reset(seed=seed). np_random is an np.random.Generator, created from entropy on
             first access if no seed was given. In core.py (L169–171) super().reset only does
             `if seed is not None: self._np_random, self._np_random_seed = seeding.np_random(seed)`.
             seeding.np_random (seeding.py) rejects anything that is not a non-negative Python int,
             then builds Generator(PCG64(SeedSequence(seed))). env_checker.check_reset_seed_determinism
             (L79–154) resets with seed=123, then with no seed, then repeats. It requires equal
             observations for each pair only when env.spec is set and not nondeterministic. It always
             requires the generator states to match for equal seeds and to differ for 123 vs 456.
             options is documented only as "Additional information to specify how the environment is
             reset (optional, depending on the specific environment)".
             Researcher's throwaway check (not a source; uv run --no-project --with gymnasium==1.4.0,
             numpy 2.4.6): an env whose reset returns self.np_random.integers(1000) gave
             [944, 625, 684, 897] for reset(seed=7) followed by three reset() calls, the identical list
             on a second pass, and [944, 944, 944, 944] when seed=7 was passed on every reset;
             reset(seed=np.int64(...)) raised "Seed must be a python integer, actual type:
             <class 'numpy.int64'>".
Locators:    api/env "Env.reset()" (Parameters: seed), "Env.np_random", "Env.np_random_seed";
             introduction/create_custom_env "Reset function" and "Common Debug Issues"; api/utils
             "Seeding"; core.py L124–171, L238–259; seeding.py np_random; env_checker.py L79–154.
Quote:       "Therefore, reset() should (in the typical use case) be called with a seed right after
             initialization and then never again." / "If you pass an integer, the PRNG will be reset
             even if it already exists. Usually, you want to pass an integer right after the
             environment has been initialized and then never again." / "However, if the environment
             already has a PRNG and seed=None is passed, the PRNG will not be reset and the env's
             np_random_seed will not be altered." (api/env, Env.reset). The brief asked for the exact
             wording.
```

### 7. Stable-Baselines3 2.9.2 vectorized environments (docs and DummyVecEnv source)

```text
URL:         https://stable-baselines3.readthedocs.io/en/v2.9.2/guide/vec_envs.html
             https://github.com/DLR-RM/stable-baselines3/blob/v2.9.2/stable_baselines3/common/vec_env/dummy_vec_env.py
             (read via raw.githubusercontent.com at tag v2.9.2; github.com HTML gated as above). 2.9.2 is
             the latest on PyPI on 2026-11-22 and the version earlier lessons pin.
Kind:        primary. SB3's maintainers document and implement this behaviour.
Establishes: that SB3 passes a seed to the env only on the first reset after vec_env.seed(), and
             auto-resets without a seed. This matters only if the writer trains with SB3 PPO.
Paraphrase:  The docs say VecEnv.reset() takes no parameters; to seed, call vec_env.seed(seed) then
             reset(), and "seed and options are discarded after each call to reset()". VecEnv.seed:
             "since gym 0.26, those seeds will only be passed to the environment at the next reset".
             DummyVecEnv.step_wait (L68–71) calls self.envs[i].reset() with no seed when an episode
             ends; DummyVecEnv.reset (L75–82) passes the stored seed and options once, then clears them.
Locators:    vec_envs guide, "VecEnv API vs Gym API" and VecEnv.seed; dummy_vec_env.py L68–82.
Quote:       none needed.
```

### 8. Jiang, Kolter, Raileanu 2023, "On the Importance of Exploration for Generalization in Reinforcement Learning"

```text
URL:         https://arxiv.org/abs/2306.05483  (v1, 8 Jun 2023; NeurIPS 2023,
             https://proceedings.neurips.cc/paper_files/paper/2023/hash/2a4310c4fd24bd336aa2f64f93cb5d39-Abstract-Conference.html).
             Pages are the arXiv v1 PDF.
Kind:        primary. The authors ran the tabular experiment. As printed: Yiding Jiang (Carnegie Mellon
             University; work done while interning at Meta AI Research), J. Zico Kolter (Carnegie Mellon
             University), Roberta Raileanu (Meta AI Research). Not named in the commission; recorded
             because it is the only source here with tabular Q-learning and it bears on what decides
             held-out return.
Establishes: firsthand: in a tabular gridworld, the exploration strategy during training changes test
             return while training return is optimal for both strategies.
Paraphrase:  A 5×5 deterministic grid; training episodes start at (0, 0), test episodes at (0, 4); goal
             (4, 0) pays 2, every other step −0.04; 250-step limit. Tabular Q-learning with
             epsilon-greedy and with a count-based UCB bonus both reach optimal training return, but
             epsilon-greedy generalizes worst with highest variance while UCB reliably finds the optimal
             test policy (§3 "Generalization in a Tabular CMDP", pp. 3–4, Figure 2, 100 runs per
             setting, 1000 episodes each). Footnote 2: "Without good training performance, the
             generalization gap is not a meaningful measure: a random policy would have no
             generalization gap at all." (p. 3).
Locators:    §3 pp. 3–4; Figure 2 p. 4; footnote 2 p. 3.
Quote:       footnote 2 as above; it independently restates Kirk's caution about the gap.
```

## Contradictions

1. **A closed gap is not a learned task.** Cobbe et al. §3.2 make the gap the measure of overfitting,
   which the commission adopts. But the Nature-CNN gap in their Table 1 shrinks from 32.66 points (100
   levels) to 0.83 (unbounded) partly because training success falls, from 99.45% to 90.87%. Test
   success only rises from 66.79% to 90.04%. Kirk et al. (p. 211) and Jiang et al. (footnote 2, p. 3)
   both state that a random policy has a gap of about zero. For the lesson, a position-only agent
   trained on many levels may show a small gap with both returns low, so the page must report both
   returns, as the commission already requires, and must not read a small gap as success.
2. **Observation and level count are necessary conditions, not the whole decision.** The commission says
   "Two things decide whether that gap can close". Cobbe et al. show other levers at a fixed level count.
   At 4,000 levels the gap is 11.83 points for Nature-CNN and 1.83 for IMPALA-CNN (Table 1). L2,
   dropout, augmentation, batch norm and stochasticity each narrow the gap on 500 levels (§5). Zhang et
   al. §6 attribute generalization differences to the match between architecture and task (ConvNets vs
   MLPs, Table 2). Jiang et al. §3 show, in a tabular grid with layout and training data fixed, that the
   exploration strategy changes test return. For a tabular local-view learner this means a held-out
   level can fail because its local views were never visited in training, even when the observation and
   level count suffice in principle.
3. **"Cannot generalize whatever it trains on" holds for memoryless policies only.** Kirk et al.
   Definition 4 lets a policy map histories to actions. A history-dependent agent that sees only its
   position can tell that a move failed when its position does not change, so in principle it can learn
   where walls are within an episode. The construction argument holds for a policy that is a function of
   the current observation, which describes the lesson's learners (a Q-table over the current
   observation, an SB3 MLP policy without a frame stack). Recurrent policies are outside this lesson,
   so the page should state the claim for policies that act on the current observation.
4. **A local view does not guarantee that a memoryless agent can solve held-out levels.** Cobbe et al.
   give their 9×9-view RandomMazes agent an LSTM "as memory is necessary for the agent to explore
   optimally" (§6, p. 6). Procgen's memory-mode Maze restricts observations to a small patch, after
   which "agents can reliably solve levels only by utilizing memory" (App. B.2, p. 13). A memoryless
   local-view agent in Kruskal-style mazes with dead ends may loop. Two layouts can show the same local
   view and goal direction yet need different moves. The writer's generator (sparse walls, or mazes
   without dead ends) decides how much of the held-out shortfall comes from this aliasing and how much
   from the number of training levels.
5. **Position-only held-out return need not be near chance.** A position-only policy follows one route
   on every level, so its held-out return is the share of held-out levels where that route is open. That
   share depends on how much the generated layouts have in common. Procgen's Rmin, trained with masked
   observations, is 4 of a maximum 10 in hard Maze and 5 of 10 in easy Maze (App. C table, p. 13). Small
   mazes are solvable blind. Candidate result 1's "near-chance held-out return" is a prediction for the
   writer's runs to test, not something any source establishes for this grid.
6. **Checks on perturbed training levels can miss memorization.** Zhang et al. §4 and App. C report that
   sticky actions, even at stickiness 0.99, left an overfit agent's training-level score high (Figs. 12,
   17, 18). Random starts exposed Agent-1, which was trapped on a training maze (Fig. 13), but not
   Agent-3, which had memorized random rewards on 1,000 levels and still navigated well (C.3, p. 23).
   Their conclusion is that held-out test sets are the more direct evaluation (C.4, p. 24). The
   commission's extra check (perturb one wall, or replay a training level's action sequence blind on
   another level) can support result 1 as a removal test. It should not be presented as a detector that
   works without the held-out split. No source tests those two specific checks.
7. **The papers' level counts are of a different scale.** Procgen: "as many as 10,000 levels" (§3.1,
   p. 4). CoinRun with Nature-CNN: overfitting still noticeable at 16,000. RandomMazes: gap 0.93 points
   at 64,000 levels and about zero at 128,000 (Table 3). The commission's sweep is 1 to 256 levels on a
   small grid with a tabular learner, so the papers' counts say nothing about where this lesson's gap
   closes.
8. **Training return need not stay flat as level count grows.** It falls for Nature-CNN (Table 1). It
   rises past a threshold in CoinRun-Platforms and many Procgen games, which the authors attribute to an
   implicit curriculum (Cobbe 2019 §6.1, p. 7; Cobbe 2020 §3.1, p. 4). Result 2's chart may show either
   pattern.
9. **"Held out" in Procgen means the full distribution.** The paper says both "measure performance on
   held out levels" (§3.1, p. 4) and "test on the full distribution of levels" (§2.2, p. 3).
   train-procgen's test worker sets num_levels = 0, drawing from all seeds in [0, 2,147,483,647), which
   include the training seeds. With 200 training seeds, a test episode hits a training level with
   probability 200 / 2,147,483,647 ≈ 9.3 × 10⁻⁸. Zhang et al. use disjoint pools (App. A.2), and Kirk's
   protocol C holds seeds out. A lesson that splits seeds explicitly should make the sets disjoint, as
   Zhang et al. do.
10. **Gymnasium allows per-episode seeding but advises against it, and SB3 never does it.** The 1.4.0
    docs say a passed integer "will be reset even if it already exists" and also advise seeding once,
    right after initialization. SB3 auto-resets without a seed. Keying a level by calling
    reset(seed=level_seed) every episode therefore works in a hand-written loop and fails under SB3,
    where only the first episode would get the seed. Procgen's design works under both: the env holds
    its level-seed set, draws a level seed from self.np_random on each reset, and builds the layout
    from a generator seeded with that level seed (entry 3). That design passes check_env's generator
    checks, because the layout sequence is a function of the reset seed. Passing the level through
    options is also documented as allowed. Earlier lessons in this course use options={"start": ...}
    for starts.
11. **Internal slips in the sources, for anyone quoting them.** Zhang et al. §4 cites "Subsection 3.2"
    for the random-reward results, while App. A.1 calls that part "Subsection 3.3"; cite it by heading.
    Procgen App. B.2 says "6 of the 16" environments have memory variants and then lists seven. Kirk
    Definition 4 prints "Ctrain, Ctrain ⊆ C" for Ctrain, Ctest. Cobbe 2019 §6.2's "20,000 levels"
    falls between the 16,000 and 32,000 rows of Table 3.

## Numbers

Cobbe et al. 2019, CoinRun, final success after 256M timesteps, mean ± sd across 5 seeds (training sets
regenerated per seed), each point 10,000 episodes. Owner: Cobbe et al. 2019, App. E Table 1, p. 14.
Gap = train − test, computed by the researcher from the table.

```text
# levels   Nature train   Nature test    gap     IMPALA train   IMPALA test    gap
   100     99.45 ± 0.09   66.79 ± 1.09   32.66   99.39 ± 0.08   66.58 ± 1.91   32.81
   500     97.85 ± 0.46   70.54 ± 0.62   27.31   99.16 ± 0.19   80.25 ± 1.07   18.91
  1000     95.7  ± 0.65   72.51 ± 0.68   23.19   97.71 ± 1.04   84.84 ± 2.24   12.87
  2000     92.65 ± 0.71   75.6  ± 0.28   17.05   97.82 ± 0.32   90.92 ± 0.45    6.90
  4000     90.18 ± 1.04   78.35 ± 1.47   11.83   97.7  ± 0.19   95.87 ± 0.62    1.83
  8000     88.94 ± 1.08   84.02 ± 0.96    4.92   98.13 ± 0.21   97.29 ± 1.04    0.84
 12000     89.11 ± 0.58   86.41 ± 0.46    2.70   98.14 ± 0.56   97.51 ± 0.46    0.63
 16000     89.24 ± 0.77   87.58 ± 0.79    1.66   98.04 ± 0.17   97.77 ± 0.68    0.27
 unbounded 90.87 ± 0.53   90.04 ± 0.9     0.83   98.11 ± 0.26   98.29 ± 0.16   −0.18
(unit: % of levels solved)
```

Cobbe et al. 2019, RandomMazes (IMPALA-CNN + LSTM, 9×9 local view), final success after 256M timesteps,
mean ± sd across 3 seeds. Owner: Cobbe et al. 2019, App. E Table 3, p. 14. Gap computed by the
researcher.

```text
# levels   train          test           gap
  1000     92.09 ± 0.35   68.13 ± 1.3    23.96
  2000     93.57 ± 2.06   74.08 ± 1.25   19.49
  4000     92.94 ± 1.47   77.79 ± 1.87   15.15
  8000     98.47 ± 0.4    83.33 ± 0.66   15.14
 16000     99.19 ± 0.19   87.49 ± 1.45   11.70
 32000     98.62 ± 0.37   93.07 ± 1.0     5.55
 64000     98.64 ± 0.14   97.71 ± 0.24    0.93
128000     99.06 ± 0.21   99.1  ± 0.34   −0.04
256000     98.97 ± 0.18   99.21 ± 0.11   −0.24
unbounded  98.83 ± 0.71   99.36 ± 0.16   −0.53
(unit: % of levels solved)
```

```text
Figure: 2^32 possible CoinRun level seeds; the unbounded agent meets about 2M unique levels
Owner:  Cobbe et al. 2019, §3.2, p. 3
Scope:  one 256M-timestep training run

Figure: 200 training levels (easy), 500 (hard, the default); 25M timesteps easy, 200M hard
Owner:  Cobbe et al. 2020, §2.2, pp. 2–3
Scope:  Procgen's recommended generalization protocol

Figure: "as many as 10,000 levels" to close the gap
Owner:  Cobbe et al. 2020, §3.1, p. 4
Scope:  16 Procgen games, training sets 100 to 100,000 levels, PPO 200M timesteps, hard mode

Figure: Maze Rmin 4, Rmax 10 (hard); Rmin 5, Rmax 10 (easy)
Owner:  Cobbe et al. 2020, App. C table, p. 13
Scope:  Rmin = score of a policy trained with masked observations; Rmax = level-completion reward

Figure: level-seed range [start_level, start_level + num_levels), upper bound exclusive; num_levels = 0
        gives [0, 2,147,483,647)
Owner:  procgen vecgame.cpp L284–293, randgen.cpp L6–11 (commit 37b521d)
Scope:  per reset, one seed drawn uniformly (by modulo) from the range

Figure: best possible episode reward 2.1; timeout −1 after 200 steps; −0.01 per wall bump
Owner:  Zhang et al. 2018, App. A.1, p. 15
Scope:  every maze variant; random-reward levels rescaled to keep the maximum at 2.1
```

Zhang et al. 2018, BASIC mazes, final episode reward, MLP / ConvNet, each the mean of the top 3 of 20 runs
ranked by training reward. Owner: Zhang et al. 2018, Table 2, p. 10. Maximum 2.1.

```text
# train levels   train p=0    test p=0      train p=0.5   test p=0.5
      10         2.1 / 2.1    −0.6 / −0.1   2.1 / 2.1     −0.4 / −0.6
     100         2.1 / 2.1     0.9 / 1.2    2.0 / 2.1     −0.4 / −0.6
    1000         2.1 / 2.1     1.6 / 2.0    2.0 / 2.0     −0.2 / −0.1
   10000         2.1 / 2.1     1.9 / 2.1    1.3 / 1.2     −0.1 / −0.1
(p = probability each object's reward sign is flipped on a training level; test levels unflipped)
```

```text
Figure: GenGap(π) = R(π, M|Ctrain) − R(π, M|Ctest)
Owner:  Kirk et al. 2023, Eq. 2, p. 210
Scope:  expected return under each context set's distribution

Figure: Gymnasium 1.4.0, released to PyPI 2026-10-05; Stable-Baselines3 2.9.2
Owner:  PyPI release records; Gymnasium docs v1.4.0
Scope:  latest releases on 2026-11-22, the versions earlier lessons pin

Figure: Jiang et al. tabular grid: 5×5, goal reward 2, step reward −0.04, 250-step limit, 100 runs ×
        1000 episodes per setting
Owner:  Jiang et al. 2023, §3, pp. 3–4
Scope:  train start (0,0), test start (0,4), same layout
```

## Limits

- No source measures the commission's case: tabular Q-learning (or SB3 PPO) on a seed-keyed gridworld
  with position-only vs local-view observations over 1–256 training levels. Every number for results 1
  and 2 must come from the writer's runs.
- No source states the position-only argument as such. The nearest primaries are Kirk's remark that an
  unobserved context makes the CMDP a POMDP (p. 208) and Zhang's random-reward levels, where the flipped
  signs are absent from the observation and good test performance is "impossible (by design)" (p. 5).
  The derivation is the writer's, and it holds only for policies of the current observation
  (Contradiction 3).
- No source tests the commission's specific memorization checks (perturbing one wall, or replaying a
  training level's action sequence on another level). Zhang tested only sticky actions and random starts.
- Gymnasium's docs do not describe how to key distinct levels to seeds or restrict an env to a level
  set. They document only one PRNG per env, `options` as env-specific, and `gymnasium.utils.seeding.
  np_random`. The two-generator design is Procgen's (entry 3), and the page's design is the writer's
  choice.
- Cobbe 2019 does not say how CoinRun's test seeds are kept apart from training seeds beyond "collisions
  are unlikely" with 2^32 seeds.
- The per-game numbers in Procgen Figure 2 (including Maze) exist only as plotted curves. No table gives
  them, so none are recorded.
- Domain randomization and sim-to-real were not researched, per the commission.

## Source assets

```text
Asset: Cobbe et al. 2019 Figure 2 (a) and (b), p. 3 of arXiv v3: % levels solved vs # training levels
       (log axis), train and test lines with shaded sd, dotted line for the unbounded agent's test score.
Shows: the gap closing as level count grows, and that it closes at a smaller count for IMPALA-CNN.
Crop:  keep both panels, axis labels, legend and the note (from the caption) that the dotted line is
       the unbounded agent; omit nothing from the axes.

Asset: Cobbe et al. 2019 Figure 6, right panel, p. 6: a RandomMazes level with the agent's observed
       9×9 patch shaded green.
Shows: what a local view of a generated maze covers, the commission's observation (b) in a source.
Crop:  right panel only; keep the green shading and enough caption to say what the shading is.

Asset: Cobbe et al. 2019 Figure 8, p. 7: RandomMazes train/test vs # training levels.
Shows: a local-view maze agent's gap persisting into tens of thousands of levels.
Crop:  keep axes and legend.

Asset: Cobbe et al. 2020 Figure 2, p. 3: 16 small multiples of train/test score vs number of levels.
Shows: the gap closing across games; the Maze panel is the relevant one.
Crop:  if cropped to Maze, keep that panel's axes, the shared "Number of Levels" label and the legend.

Asset: Zhang et al. 2018 Figure 2b, p. 5: training vs test bars against reward-flip probability, four
       training-set sizes per group.
Shows: near-optimal training reward on randomly rewarded levels with test reward at or below zero.
Crop:  keep the colour key from the caption (blue training, red test; dark to light = 10,000 to 10
       levels).

Asset: Zhang et al. 2018 Figures 11, 10 and 13, pp. 20, 19, 22: Agent-1 (10 training levels) optimal
       on a training maze, stuck near its start on a test maze, and trapped on the same training maze
       after a random start.
Shows: memorization drawn as paths, the closest source analogue to the lesson's path drawings.
Crop:  keep the frame-range and cumulative-reward labels above each tile; they carry the result.

Asset: Kirk et al. 2023 Figure 2, p. 220: evaluation protocols A, B, C for PCG environments as
       training and testing context sets.
Shows: the held-out-seed protocol (C) against Procgen's 200-seed protocol (B).
Crop:  keep all three panels and the caption's A/B/C key.

Asset: Jiang et al. 2023 Figure 2a, p. 4: 5×5 tabular CMDP with train start, test start and goal.
Shows: a tabular case where only the start differs between train and test.
Crop:  panel (a) only.

Gymnasium docs, Procgen README/source, SB3 docs: None found.
```

## Discarded

```text
https://gymnasium.farama.org/api/env/: unversioned copy, text identical to v1.4.0; recorded under the versioned URL instead.
https://gymnasium.farama.org/v1.4.0/introduction/train_agent/: no seeding text relevant to keying levels.
https://gymnasium.farama.org/v1.4.0/introduction/basic_usage/: one sentence pointing to reset's seed and options; adds nothing beyond api/env.
```
