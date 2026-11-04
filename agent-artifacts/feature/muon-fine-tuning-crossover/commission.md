# Commission: feature/muon-fine-tuning-crossover

Series: Feature (open, strict, 600-1200 words, 2-4 flex sections, at least 5 sources).
Template: article. Date: 2026-11-04.

## The story

arXiv:2611.03633 (Li, Gai, Risteski, Springer, Raghunathan; CMU; submitted 2 November 2026)
reports about 600 pretraining runs and 29,000 fine-tuning runs of OLMo-style models from 30M to
600M parameters, pretrained on 150M to 154B DCLM tokens (token-to-parameter ratios of 5 to 2,560),
then fine-tuned on GSM8K, StackMathQA, Alpaca and MusicPile. Muon reaches lower pretraining loss at
every budget, yet past a crossover in token-to-parameter ratio an AdamW-pretrained model gives the
better trade between what fine-tuning teaches and what it makes the model forget. The crossover
ratio falls with model size (scouted as about 320 at 30M and about 10 at 600M on StackMathQA; the
researcher confirms every figure against the paper).

## The original work asked for

Lay the paper's crossover points against model size and show how fast the line falls, then place
the published token-to-parameter ratios of production models trained with Muon (Moonlight, Kimi
K2, and any other with a published count) beside it, computed by the paper from their own
technical reports. Those models sit outside the measured range by orders of magnitude in size.
The piece states that plainly: the overlay shows where they would fall if the trend held, and the
paper does not test that. Handle mixture-of-experts carefully: state whether active or total
parameters are used, and show both if the conclusion changes between them. If the paper's
crossover depends strongly on the fine-tuning set, the piece says so and does not pick the most
dramatic one.

## Required contribution and boundaries

- Explain the mechanism the paper gives (its margin-to-spread account and the linear-model proof)
  at the level of a reader who trains models, with a drawing if one teaches it.
- State the strongest objection fairly: tuning of the comparison, the 600M ceiling, a single v1
  preprint, other work finding Muon's speedup smaller (arXiv 2509.02046) or Muon fine-tuning results
  (arXiv 2605.10468). The researcher finds any author response or replication.
- Background: an earlier piece, the-paper/muon-optimizer (2026-07-17), explained how Muon works.
  Do not re-explain Muon's mechanics beyond one or two sentences; linking it is fine.
- Visuals: 2-4, each the spine of a section. Candidates: crossover ratio versus model size with the
  production overlay (built with nb chart from verified series only); the paper's learn-versus-forget
  figure captured with nb asset; a drawn diagram of the mechanism. The writer decides.

## Recent patterns to break (last five features)

- Headlines: four of five lead with a named entity plus a number or ratio ("Marvell's $115
  billion ... 23 times", "Swapping the model moves ... twice as far"). Prefer a headline whose
  surprise is a finding stated in words.
- Deks: two of the last four use a trailing "where ..." comparison clause ("..., where Bybit's 2025
  haul held no stablecoin", "..., where its sub-agent Asta Panda adds 25.3 points"). Do not use it.
- Deks have packed three or more figures; keep this dek to one detail.
- Section headings are all full declarative sentences; vary length and construction.

## Roles

Writing coach (low), researcher (high), writer (high, per series.yaml), editor (orchestrator model,
high, required).

## Decisions after researcher/01

- The original work changes. The researcher found that, converted to tokens, all 20 main-setting
  crossovers in Table 2 fall between 2.4B and 19.2B tokens, and the pooled log-log slope of
  crossover ratio against size is about -0.97, which a fixed token threshold would give. The paper
  does not make this point. That is the piece's own work: the crossover tracks how many tokens a
  model saw more than how many it saw per parameter, within 30M-600M dense models, to the factor-of-
  two precision the doubling grid allows. The chart shows it. State the precision and the absence
  of seeds and error bars.
- Production models: their token counts (trillions) sit two to three orders of magnitude past
  every measured crossover, whichever parameter count is used. The piece says that is an
  extrapolation the paper does not test, and does not use the extrapolated fit's numbers below the
  measured range (no "crossover below 0.2 at 1T").
- Moonlight's own ablation (Muon-pretrained, Muon-fine-tuned beats its AdamW twin on four
  benchmarks at 1.2T tokens) is the strongest contrary evidence and gets a fair statement in its
  own words, with its caveats (one run per arm, benchmark scores rather than forgetting, checkpoint
  before final decay). The piece weighs it; it does not dismiss it.
- Mechanism: one short treatment at most. The paper's theory compares Muon with gradient descent,
  not AdamW, and explains the reversal with budget, not the fall with size; say so if the mechanism
  appears.
- The fine-tuning-optimizer disagreement (Moonlight, Kimi K2, 2605.10468 favor Muon fine-tuning
  for Muon-pretrained models) and the weight-decay point are context; use them where they change
  the reading.
- Springer et al. 2025 shares authors and is not independent confirmation.
- "MNR" axis label versus "MSR" in the text: if a figure is captured, the caption follows the text
  and notes the label.
