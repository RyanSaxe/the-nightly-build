# Commission: feature/mlperf-grpo-post-training

Run: scheduled, 2026-11-28, nb duty open section (no commissions). Template: article. Strict band 600–1200 words, 2–4 flex sections, at least 5 sources.
Production policy (balanced): coach capable/low; researcher capable/high; writer capable/high (series override); editor inherit/high. Recorded actual: all roles are subagents on the orchestrator's model at those efforts.

Topic selection: a scout subagent proposed three candidates (FAA 13 November ground stop; MLPerf Training v6.1 post-training benchmark; CDC stroke-mortality MMWR). Decided: MLPerf, because the FAA primaries could not be fetched and the paper ran an outage feature yesterday (Microsoft 365), and the ML-production audience is best served by the benchmark.

## Subject

MLCommons' MLPerf Training v6.1 results (released 16 November 2026) include the suite's first post-training benchmark: GRPO reinforcement learning on Qwen3.5-397B, scored on software-engineering repair tasks to a quality target (reported as 0.69 pass@4). Primary starting points the scout opened: https://mlcommons.org/2026/11/mlperf-training-v6-1-results/ and https://mlcommons.org/benchmarks/training/ ; vendor posts (NVIDIA, Google, AMD, others) are secondary for anything they claim about competitors and primary only for their own submission.

## Angle (to be tested, not assumed)

What does a time-to-quality benchmark for RL post-training actually time, and how do the submissions compare once the clock is set beside the accelerators used? The piece should let the reader draw the GRPO loop as the benchmark specifies it (rollout generation, reward from tests, policy update; what is inside and outside the timed region, the dataset, the reference convergence/variance rules and the number of runs required), then compare submissions on accelerator-minutes and on the scale each chose, from the official results table, not from vendor blogs.

The original work: reconcile the rules document with the results table so a reader can see what one "minute" on this benchmark contains and what a vendor's headline comparison does or does not hold constant. If the rules show rollout time is outside the clock, or results are too few to compare, the angle changes to whatever the material supports — report back.

## Boundaries

- Do not make this a per-watt or Endpoints piece; the paper ran an Epoch inference-index critique on 21 November and the per-watt Endpoints comparison is out of window.
- Do not reteach GRPO's derivation (the paper has a GRPO explainer from July and the RL course will teach it); one sentence and a drawing of the loop is enough.
- Figures from the official MLCommons results only; vendor numbers only where attributed.

## Neighbouring articles

The RL course lesson today is on time awareness in tabular RL; no overlap. The Daily Brief's technology items must not include this MLPerf round (orchestrator will tell its researcher if needed).

## Recent patterns to break (last 10 features)

- Headlines have repeatedly put a named organization + a reconciled number ("Epoch averages GB300 leads of 8× to 217× into 25×", "Glasswing's 2 November ledger reveals 235 of the 5,087"). Avoid the "X averages/reveals N of M" frame.
- Deks have often named the person or group behind the figure then a contrast clause ("Jason Li, who built Epoch's index, has matched it ... and published no such check..."). Build the dek another way.
- Several features have opened on the primary's own number then corrected it. Open on the finding instead.

## Decisions after researcher/01

- Angle, now settled: the evidence shows the quality target never stopped a clock. The earliest allowed evaluation (step CEIL(2.5 + 3840/GBS), step 10 at batch 512) is the one every reference and scored run passed at. So in v6.1 a "minute" on this benchmark is the wall time of a fixed amount of GRPO work (10 steps, 5,120 trajectories at batch 512) with a pass/fail gate, rollout and sandboxed episodes inside the clock. Lead with that, then show what scale and backend buy on that fixed work (accelerator-minutes vs minutes), and what headline comparisons hold constant or not.
- Do not write that any system "reached quality faster". Do not compare TPU and GPU on accelerator-minutes without stating that the TPU entry ran a different batch size (6 steps, 6,912 trajectories) and that sandbox CPU capacity and rollout staleness are uncounted.
- Vendor claims are reported attributed, set against the official table, with the same-backend correction where it applies. AMD made no claim; leave it out.
- Original-work target: reconcile the rules with all 87 runs to show the clock measures fixed work, and recompute the scale curve in accelerator-minutes.
