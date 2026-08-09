# Evidence: paper-of-the-day/deep-q-network (01)

The record supports the commission's reconstruction and its "what held, what was
an artifact" framing. The 2015 Nature claim, its exact scope, the Q-learning
objective, the two stability devices, and the two named figures are all recorded
firsthand from the Nature paper's full text including Methods, so the writer can
set the math and the figures exactly. The 2013 precursor is recorded firsthand,
and the precise delta the Nature paper added (a separately maintained target
network, reward and error clipping, a larger network, 49 games) is pinned to the
equations. The after-record is the honest part to read closely: it does not
overturn DQN. Machado's sticky-actions test shows DQN's result is robust to
added stochasticity while brittle memorization collapses, so the protocol
critique lands on the benchmark and on planning agents, not on DQN's headline.
Agarwal lands on the aggregate metric practice DQN's lineage used, but its deep
case study is the later Atari 100k regime, not the original 200M-frame agent.
Henderson is on MuJoCo continuous control, not Atari, so its bearing on the 2015
claim is by analogy about deep-RL fragility, not a re-test of DQN. Double
Q-learning is the one after-record study that critiques DQN's exact algorithm
(the max target overestimates in all 49 games) and it refines rather than
discards. Thin spots: the per-game score table (Extended Data Table 2) and the
component-ablation table (Extended Data Table 3) are image tables the text
extractor could not read, so their exact numbers are recorded as a gap; and the
after-record per-game numbers were read through the ar5iv HTML via a fetch
summarizer, flagged per entry for the editor to re-open.

## Sources

```text
URL:         https://www.nature.com/articles/nature14236
Kind:        primary. Mnih et al. own the DQN claim, the algorithm, and the figures.
Establishes: The central 2015 claim and its exact scope; the Q-learning objective,
             loss, gradient, target network and experience replay as the paper
             writes them; the two named figures.
Paraphrase:  A single deep convolutional network ("deep Q-network"), one algorithm,
             one architecture, and one hyperparameter set, receiving only the raw
             pixels (84x84x4 preprocessed) and the game score, was trained
             separately on each of 49 Atari 2600 games. It surpassed the best prior
             reinforcement-learning methods on 43 of the 49 games and reached a
             level comparable to a professional human games tester, where
             "comparable" is operationalized in the paper as 75% or more of the
             human score, met on 29 of the 49 games. Reinforcement learning with a
             nonlinear approximator is "known to be unstable or even to diverge";
             the paper's two fixes are experience replay (uniform random sampling
             from a 1-million-frame memory, breaking correlations between
             consecutive samples and smoothing the data distribution) and a
             separate target network cloned every C steps (an older parameter set
             for the target, adding a delay so an update to Q does not immediately
             move its own target, making "divergence or oscillations much more
             unlikely"). Read firsthand including full Methods and Algorithm 1.
Locators:    Abstract p.529; instability/two-ideas para p.529; loss equation p.529;
             results (43 of 49, 29 games, 75%) p.530-531; Methods "Algorithm"
             (Bellman, loss, gradient) and "Training algorithm for deep Q-networks"
             (replay, target network, error clipping), Algorithm 1 box.
Quote:       "achieve a level comparable to that of a professional human games
             tester across a set of 49 games, using the same algorithm, network
             architecture and hyperparameters" (abstract).
             "outperforms the best existing reinforcement learning methods on 43 of
             the games... achieving more than 75% of the human score on more than
             half of the games (29 games)" (p.530-531).
             "Reinforcement learning is known to be unstable or even to diverge when
             a nonlinear function approximator such as a neural network is used to
             represent the action-value (also known as Q) function" (p.529).
```

```text
URL:         https://arxiv.org/abs/1312.5602
Kind:        primary. Mnih et al. own the 2013 precursor result.
Establishes: What the precursor did first, and what the Nature paper had not yet
             added.
Paraphrase:  "The first deep learning model to successfully learn control policies
             directly from high-dimensional sensory input using reinforcement
             learning." A convolutional network trained with a Q-learning variant
             and experience replay (replay memory of one million frames, minibatch
             32) on seven Atari games: Beam Rider, Breakout, Enduro, Pong, Q*bert,
             Seaquest, Space Invaders. It outperformed all prior approaches on six
             of the seven and surpassed a human expert on three (Breakout, Enduro,
             Pong). The precursor's loss uses target y_i built from the previous
             iteration's weights theta_{i-1} held fixed within an iteration; it does
             NOT maintain a separately cloned target network updated every C steps.
             Its network is smaller than the Nature version: 16 filters 8x8 stride 4,
             then 32 filters 4x4 stride 2, then a 256-unit fully-connected layer.
             So the Nature paper's additions over 2013 are: the periodically-cloned
             target network, reward clipping to [-1,1], error clipping, a larger
             network (32/64/64 conv, 512 FC), and the jump from 7 to 49 games.
Locators:    Abstract; Section 4 (model architecture); Section 5 results / Table 1.
Quote:       "surpasses a human expert on three of them" and "outperforms all
             previous approaches on six of the games" (results).
Caveat:      Read via ar5iv HTML (arxiv.org/abs redirects to the abstract only). The
             seven-game names, the loss form, and the architecture dims are firsthand
             from the ar5iv full text; treat the specific per-game score table as
             read-through-fetch and re-open if quoted numerically.
```

```text
URL:         https://jair.org/index.php/jair/article/view/10819  (arXiv:1207.4708)
Kind:        primary. Bellemare et al. own the Arcade Learning Environment, the
             benchmark DQN is scored on (Nature reference 12).
Establishes: The benchmark and its evaluation methodology, including an early
             overfitting warning that predates DQN.
Paraphrase:  The ALE is a software framework over an emulator exposing hundreds of
             Atari 2600 titles, with an initial evaluation set of about 50 games. It
             proposed score normalization and aggregate reporting (average, median,
             score distributions). It warned explicitly that training and evaluating
             on the same games overestimates performance, and recommended tuning on
             a small set of training games before testing on unseen games (a
             train/test split). DQN did not adopt that split: it trained and
             reported on the same 49 games, tuning hyperparameters on five of them
             (Pong, Breakout, Seaquest, Space Invaders, Beam Rider). So the protocol
             weakness Machado later formalized was flagged by the benchmark's own
             authors before DQN.
Locators:    Framework description; normalization section; train/test methodology
             section.
Quote:       "it is considered poor experimental practice to both train and evaluate
             an algorithm on the same data set, as it can grossly over-estimate the
             algorithm's performance."
Caveat:      Read via ar5iv full text; game count "about 50" and the quotes are
             firsthand from that text.
```

```text
URL:         https://arxiv.org/abs/1509.06461
Kind:        primary. van Hasselt, Guez, Silver own the Double DQN result.
Establishes: The one after-record study that critiques DQN's exact algorithm: the
             max operator in the target systematically overestimates action values.
Paraphrase:  DQN's target uses one network both to select and to evaluate the
             next-state action through the single max, which biases the estimate
             upward ("more likely to select overestimated values"). The paper shows
             overestimation for DQN in all 49 tested games, in varying amounts, and
             on some games (Asterix, Wizard of Wor) the value estimates diverge
             visibly. Double DQN decouples selection from evaluation: the online
             network picks the argmax action, the target network scores it. This
             reduces overestimation and improves policies. It refines DQN's
             architecture rather than discarding it (same replay, same target
             network, one-line change to the target).
Locators:    Abstract; Background (Double Q-learning); Results on overoptimism
             (Figure 3); Table 1 (no-op starts) and Table 2 (human starts).
Quote:       "the max operator ... uses the same values both to select and to
             evaluate an action. This makes it more likely to select overestimated
             values, resulting in overoptimistic value estimates."
             "overestimations ... observed for DQN in all 49 tested Atari games,
             albeit in varying amounts."
Caveat:      Read via ar5iv full text. Equations firsthand; the score numbers in
             Numbers below were read through the fetch summarizer, re-open Table 1/2
             before printing them.
```

```text
URL:         https://arxiv.org/abs/1709.06560
Kind:        primary. Henderson et al. own this reproducibility study.
Establishes: How much deep-RL results move on seeds, hyperparameters, reward scale,
             and codebase. Scope: continuous-control policy-gradient methods on
             MuJoCo, NOT Atari or DQN.
Paraphrase:  Testing TRPO, DDPG, PPO, and ACKTR on MuJoCo tasks (HalfCheetah,
             Hopper, and others), the authors show that two groups of five random
             seeds, everything else identical, can produce significantly different
             score distributions (TRPO on HalfCheetah: t = -9.09, p = 0.0016).
             Network size and activation swing results (PPO on Hopper: 2790 +/- 62
             with a (64,64) tanh network vs 61 +/- 33 with (400,300) tanh); reward
             rescaling can break learning entirely; and three public implementations
             of the same algorithm (original, rllab, OpenAI Baselines) disagree
             substantially under identical hyperparameters (TRPO on Hopper ranging
             1183 to 3229). They recommend significance testing, more seeds, and
             power analysis. Because the subject is MuJoCo continuous control, this
             bears on the 2015 DQN claim only by analogy about deep-RL fragility; it
             is not a re-run of DQN.
Locators:    Figure 5 (seeds); Figure 2 / Tables 1-2 (architecture, activation);
             Figure 3 (reward scale); Figure 6 (codebases); Table 14 (bootstrap
             power).
Quote:       "even averaging several learning results together across totally
             different random seeds can lead to the reporting of misleading results."
Caveat:      Read via ar5iv full text; numbers read through the fetch summarizer.
```

```text
URL:         https://arxiv.org/abs/1709.06009
Kind:        primary. Machado et al. own the ALE evaluation re-examination.
Establishes: The protocol critique that lands directly on the Atari benchmark, and
             the test that shows DQN's result is robust to added stochasticity.
Paraphrase:  The original ALE is deterministic, so an agent can score well "by
             simply memorizing a good action sequence, rather than learning to make
             good decisions." The proposed fix is sticky actions: with probability
             sigma = 0.25 the environment repeats the agent's previous action
             instead of the chosen one, injecting stochasticity the agent cannot
             memorize around. No-op random starts do not fix this because the
             environment stays deterministic after the start. Under sticky actions,
             a pure memorizer (the Brute) collapses while learning agents barely
             move: this is the finding that matters for DQN, because it means DQN's
             scores are not a determinism artifact. Also recommends the game-over
             signal (not lives-lost) for episode termination, a train/test game
             split, and reporting the average of the last k episodes rather than the
             best policy.
Locators:    Section 5 (determinism, memorization); Section 5.2 (sticky actions
             formula, sigma = 0.25); Section 5.3 (no-ops insufficient); Section 3.1
             (termination, train/test split); Section 4.2 (last-k reporting);
             Tables 1-2 (Brute vs DQN, deterministic vs sticky).
Quote:       "it is possible to achieve high scores by learning an open-loop policy,
             i.e., by simply memorizing a good action sequence, rather than learning
             to make good decisions in a variety of game scenarios."
Caveat:      Read via ar5iv full text; sigma = 0.25 and the qualitative Brute-vs-DQN
             contrast are firsthand; the exact per-game numbers in Numbers below
             were read through the fetch summarizer, re-open Tables 1-2 to quote them.
```

```text
URL:         https://arxiv.org/abs/2108.13264
Kind:        primary. Agarwal et al. own the statistical re-analysis (NeurIPS 2021
             Outstanding Paper).
Establishes: Why the aggregate human-normalized scores DQN's lineage reports are
             fragile with few runs, and the metrics that replace them.
Paraphrase:  Deep-RL papers report point estimates (mean, median human-normalized
             score) from very few runs (commonly 3 to 10; on Atari 100k, mostly 3 or
             5). The median depends only on the ordering across tasks and, except at
             the middle task, ignores magnitude: "zero scores on nearly half of the
             tasks does not affect the median." The mean is dominated by a few
             high-scoring games. The fix is the interquartile mean (IQM): discard the
             top and bottom 25% of runs and average the middle 50%, reported with
             stratified-bootstrap confidence intervals, plus performance profiles,
             optimality gap, and probability of improvement. In the Atari 100k case
             study (26 games), point-estimate rankings reverse or fall inside
             overlapping confidence intervals once uncertainty is shown; on the ALE
             200M suite the algorithm ordering changes between median and IQM.
             The critique is of the metric practice, and its deep case study is the
             sample-efficient Atari 100k regime, not the original 200M-frame DQN.
Locators:    Section 3 (case study, run counts); Section 4.3 (median problem, IQM
             definition); Figures 2 and 6 (run counts vs CI width); Section 5 /
             Figure 9 (ALE 200M ordering changes, overlapping CIs).
Quote:       "median only depends on the performance ordering across tasks and not on
             the magnitude except at most 2 tasks. For example, zero scores on nearly
             half of the tasks does not affect the median."
Caveat:      Read via ar5iv full text; numbers read through the fetch summarizer.
```

```text
URL:         https://arxiv.org/abs/1511.05952
Kind:        primary. Schaul et al. own Prioritized Experience Replay.
Establishes: That DQN's uniform replay was a named limitation, realizing the
             "prioritized sweeping" improvement the Nature paper itself anticipated.
Paraphrase:  DQN samples the replay memory uniformly, replaying transitions at the
             frequency they were experienced "regardless of their significance."
             Prioritized replay samples in proportion to the magnitude of the
             temporal-difference error, so surprising transitions are replayed more.
             Added to DQN it improves 41 of 49 games and lifts the median normalized
             score from 48% to 106%; on a Double DQN baseline across 57 games the
             median rises from 111% to 128%. This is a direct refinement of the exact
             device the Nature paper flagged as replaceable ("A more sophisticated
             sampling strategy might emphasize transitions from which we can learn the
             most, similar to prioritized sweeping").
Locators:    Abstract; Section 3.2 (TD-error priority); Section 3.3 (proportional and
             rank-based variants); Table 1 / Section 4 (41 of 49; medians).
Quote:       "this approach simply replays transitions at the same frequency that they
             were originally experienced, regardless of their significance."
Caveat:      Read via ar5iv full text; the score numbers were read through the fetch
             summarizer, re-open Table 1 to quote them.
```

## Contradictions

- The commission's after-record framing risks reading as "later work undercut
  DQN." The record contradicts that on two of the three named studies. Machado's
  sticky-actions test shows DQN is essentially robust to added stochasticity; the
  study undercuts the deterministic benchmark and memorizing planners, and in
  doing so vindicates DQN's scores against the "it only worked because the game was
  deterministic" objection. So Machado is as much support as critique.
- Henderson is on MuJoCo continuous control (TRPO, DDPG, PPO, ACKTR), not Atari and
  not DQN. It does not re-run the 2015 agent. Its relevance is by analogy about
  deep-RL fragility, and the article must not imply it re-tested DQN and found the
  scores unstable.
- Agarwal critiques the aggregate-metric practice DQN's lineage uses, but its
  deep re-analysis is the Atari 100k sample-efficient regime and later algorithms
  (DER, OTR, DrQ, CURL, SPR), not the original 200M-frame DQN. Its bearing on the
  2015 headline is that "human-level, aggregated across 49 games" is a fragile way
  to summarize, not that DQN's 29-of-49 count is wrong.
- Internal to the 2015 claim: "human-level across 49 games" (abstract) versus
  "75% of human on 29 games" (results) are not the same statement. DQN was far
  below human on many games (Montezuma's Revenge near 0%). The headline aggregates
  a wide per-game spread, which is exactly what Agarwal's metric critique targets.
- Double DQN contradicts the reliability of DQN's own value estimates (overestimation
  in all 49 games) while agreeing that the architecture is sound enough to build on.
  It disagrees with the estimates, not the result.

What the after-record left standing: DQN's core result survives added stochasticity
(Machado), the two stability devices became the foundation the whole lineage builds
on (Double DQN, Prioritized Replay both extend them rather than replace them), and
the honestly-scoped claim (at or above 75% of human on 29 of 49 games) is unchallenged.
What it recast as artifact-prone: the aggregate "human-level" summary metric
(Agarwal), the deterministic evaluation protocol and best-policy reporting (Machado),
the reproducibility of deep-RL gains in general (Henderson), and the calibration of
DQN's value estimates (Double DQN).

## Numbers

```text
Figure: 49 Atari 2600 games
Owner:  Nature 2015, abstract and Methods "Training details"
Scope:  One network trained per game, same architecture/hyperparameters across all.
```
```text
Figure: 43 of 49 games — DQN beats best prior RL methods
Owner:  Nature 2015, p.530
Scope:  Comparison against best linear learner and Contingency/SARSA (Extended Data
        Table 2); prior methods used hand-designed features.
```
```text
Figure: 29 of 49 games at >= 75% of the professional human score
Owner:  Nature 2015, p.531 (the operational "human-level" claim)
Scope:  Human-normalized: 100 x (DQN - random) / (human - random); 75% is the
        paper's own threshold for "comparable to" the human tester.
```
```text
Figure: 30 evaluation episodes, up to 5 min each, epsilon = 0.05, no-op random starts
Owner:  Nature 2015, Methods "Evaluation procedure"
Scope:  The evaluation protocol Machado later argued stays deterministic after the
        start.
```
```text
Figure: Human tester baseline — ~20 episodes/game, up to 5 min, after ~2 h practice
Owner:  Nature 2015, Methods "Evaluation procedure"
Scope:  Defines the 100% level in Figure 3.
```
```text
Figure: gamma = 0.99; replay memory = 1,000,000 frames; minibatch = 32;
        total training = 50,000,000 frames (~38 days game time); frame-skip k = 4;
        epsilon annealed 1.0 -> 0.1 over first 1,000,000 frames, then 0.1;
        reward clipped to [-1, 1]; TD-error clipped to [-1, 1]; RMSProp
Owner:  Nature 2015, Methods "Training details" and Extended Data Table 1
Scope:  The single hyperparameter set used across all 49 games.
```
```text
Figure: Network — input 84x84x4; conv 32 filters 8x8 stride 4 (ReLU);
        conv 64 filters 4x4 stride 2 (ReLU); conv 64 filters 3x3 stride 1 (ReLU);
        FC 512 (ReLU); linear output, one unit per action (4 to 18 actions)
Owner:  Nature 2015, Methods "Model architecture"
Scope:  Larger than the 2013 net (16/32 conv, 256 FC).
```
```text
Figure: Target network cloned every C steps ("Every C steps reset Q_hat = Q")
Owner:  Nature 2015, Algorithm 1 and Methods "Training algorithm"
Scope:  The device absent from the 2013 precursor; C is a hyperparameter (Extended
        Data Table 1, target network update frequency).
```
```text
Figure: 7 games (2013) -> 6 of 7 beat prior methods, 3 of 7 beat a human expert
Owner:  Mnih et al. 2013, results
Scope:  Beam Rider, Breakout, Enduro, Pong, Q*bert, Seaquest, Space Invaders; human
        beaten on Breakout, Enduro, Pong.
```
```text
Figure: Sticky actions probability sigma = 0.25
Owner:  Machado et al. 2018, Section 5.2
Scope:  Per-timestep probability the environment repeats the previous action.
```
```text
Figure: The Brute (memorizer) collapses under sticky actions; DQN barely moves
Owner:  Machado et al. 2018, Tables 1-2
Scope:  Fetch-read table values (verify before printing): Brute Asterix ~6,909
        deterministic -> ~308 sticky (~95% drop); DQN Asterix ~3,501 -> ~3,123
        (~11%); DQN Beam Rider ~4,687 -> ~4,552 (~3%); DQN Freeway ~32.2 -> ~31.6.
        Load-bearing claim is the direction, not the decimals.
```
```text
Figure: DQN overestimates action values in all 49 games
Owner:  van Hasselt et al. 2016, Results on overoptimism
Scope:  Fetch-read aggregate scores (verify): DQN median normalized 93.5% -> Double
        DQN 114.7%; mean 241.1% -> 330.3% (no-op starts, Table 1); human-starts
        median 47.5% -> 116.7% (Table 2, tuned).
```
```text
Figure: Uniform replay is suboptimal; prioritized replay improves 41 of 49 games
Owner:  Schaul et al. 2016, Table 1
Scope:  Fetch-read (verify): median normalized 48% -> 106% on DQN; 111% -> 128% on
        Double DQN across 57 games.
```
```text
Figure: Aggregate metrics are fragile with few runs
Owner:  Agarwal et al. 2021, Sections 3-5
Scope:  Prior Atari 100k results from ~3-5 runs; median needs ~50-100 runs for a
        defensible CI, IQM ~10-20; median ignores magnitude on all but the middle
        task. Directional; exact run counts fetch-read, verify before quoting.
```

## Source assets

The two named figures are the priority; both are in the Nature paper.

```text
Asset: Figure 3, Nature 2015, p.531 — the per-game normalized-score bar chart.
Shows: All 49 games listed vertically from Video Pinball (top) down to Montezuma's
       Revenge (bottom), each a horizontal bar of DQN's human-normalized score with
       the best linear learner overlaid, on a scale where 0% = random and 100% =
       professional human, extending past 100% to 500% and (Video Pinball) ~4,500%.
       A marked line separates "At human-level or above" from "Below human-level."
       This is the figure the headline claim rests on: a reader sees at a glance
       that DQN clears human on the top ~29 games and falls far short on the bottom
       ones (Montezuma's Revenge ~0%), which is precisely the per-game spread the
       aggregate "human-level" phrase hides and Agarwal's critique targets.
Crop:  Keep the full vertical list of game names and the 0% / 100% / >100% axis with
       its "at or above human-level" divider; the whole point is the top-to-bottom
       spread, so do not crop to only the games DQN wins. Error bars are s.d. over
       the 30 evaluation episodes and can be retained or noted in the caption.
```
```text
Asset: Figure 4, Nature 2015, p.531 — 2-D t-SNE embedding of the last hidden layer,
       Space Invaders.
Shows: Each point is one game state, positioned by t-SNE on the 512-dim last-hidden-
       layer representation, colored by DQN's predicted state value V (dark red high,
       dark blue low), with screenshots pinned to selected points. It shows the
       network grouping perceptually different but similarly-valued states together
       (near-complete and full screens both high value), i.e. what the network
       learned to represent, not just how it scored. This is the figure that carries
       the "it learned a value-relevant representation" claim.
Crop:  Retain the color scale (V high-to-low) and at least the labeled screenshot
       pairs that the caption calls out (top-right full screens vs bottom partial
       screens, and the "perceptually dissimilar but nearby" cluster). The value
       coloring is the evidence; a grayscale crop loses the argument.
```

Additional Nature figures available if the reconstruction needs them:
```text
Asset: Figure 1, p.529 — schematic of the conv-net architecture (input 84x84x4,
       three conv layers, two FC layers, one output per action). Useful only if the
       architecture is being set; the Methods dims are the real source.
Asset: Figure 2, p.530 — training curves for Space Invaders and Seaquest (average
       score per episode; average predicted Q on a held-out state set). Shows stable
       learning, the visible evidence for the "trained in a stable manner" claim.
Asset: Extended Data Figure 2 — learned value function walked through Breakout (value
       climbs to ~21 then ~23 as the agent tunnels behind the wall) and Pong (the
       'up'/'down' action values split as the paddle tracks the ball). A strong
       teaching asset for what the value function encodes, tied to concrete moments.
```
After-record figures worth the space if the article weighs the critique visually:
```text
Asset: Machado et al., Tables 1-2 — Brute vs DQN, deterministic vs sticky actions.
       The single comparison that shows DQN robust where a memorizer collapses. A
       small two-row table (Brute drop ~95%, DQN drop ~11%) makes the point cleanly.
Asset: Agarwal et al., Figure 9 (ALE 200M) — algorithm ordering under median vs IQM
       with overlapping bootstrap CIs. Shows the ranking is metric-dependent. Use
       only if the metric critique gets its own beat; it is about the lineage, not
       the 2015 agent directly.
```

## Discarded

```text
URL: https://arxiv.org/abs/1312.5602 (arxiv abstract page) — abstract only; re-read
     via ar5iv full text for equations and results.
URL: https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf as fetched
     text — the fetch returned raw PDF bytes, not readable text; the PDF was instead
     extracted locally with pdfminer and read in full, so the source is kept, only
     the fetch route discarded.
```

## Open gaps for the editor

- Extended Data Table 2 (per-game DQN vs literature vs human scores) and Extended
  Data Table 3 (the component ablation isolating replay and target network) are
  image tables the text extractor could not read. The main-text qualitative claim
  that disabling replay, the target network, or the conv architecture has
  "detrimental effects" is firsthand (p.531). If the writer wants the ablation
  numbers themselves (the well-known replay-vs-target grid on Breakout, Enduro,
  River Raid, Seaquest, Space Invaders), they must be re-read from the Nature
  Extended Data, not from memory.
- Every after-record per-game and aggregate number in the Numbers section was read
  through the ar5iv HTML via a fetch summarizer. The directions are reliable and
  load-bearing; the exact decimals should be re-opened at the cited table before any
  are printed as quotations.
