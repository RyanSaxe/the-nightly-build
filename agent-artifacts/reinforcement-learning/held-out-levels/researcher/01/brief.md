# researcher brief: reinforcement-learning/held-out-levels (01)

Inputs:
- editorial-direction.md: the standards and the series prompt for this lesson
- commission.md: topic, the one idea, the case, boundaries
Output: researcher/01/evidence.md (beside this brief)

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

A lesson on a classic idea cites little, so find only what the page will use:
- Cobbe, Klimov, Hesse, Kim, Schulman 2019, "Quantifying Generalization in
  Reinforcement Learning" (ICML): the CoinRun training-level-count experiment
  (training vs test success against number of training levels), with exact
  figure/section locators and the numbers it reports (e.g. levels needed
  before the gap closes).
- Cobbe, Hesse, Hilton, Schulman 2020, "Leveraging Procedural Generation to
  Benchmark Reinforcement Learning" (Procgen): how levels are generated from a
  seed (the `num_levels` / `start_level` protocol, 200 training levels in the
  easy setting), exact locator. Do not install the package.
- Zhang, Vinyals, Munos, Bengio 2018, "A Study on Overfitting in Deep
  Reinforcement Learning": the passage showing agents fitting randomly
  generated / randomly rewarded levels (memorization), with locator.
- Optionally Kirk, Zhang, Grefenstette, Rocktäschel 2023 (JAIR) survey of
  zero-shot generalisation in deep RL: its definition of the train/test
  split over contexts, for Go deeper.
- Gymnasium's current documentation (November 2026, give version) for
  `Env.reset(seed=...)` and `self.np_random`: what seeding guarantees, that
  the seed is passed only on the first reset and later resets continue the
  generator, and how to reproduce a specific level. This decides how the
  lesson's generator keys levels; record the exact wording.
Record every URL as the document's own page (arXiv abs pages are fine).
