# Evidence: feature/mlperf-grpo-post-training (researcher 01)

The commission asked whether rollout generation is inside the clock. It is. The
MLPerf rules and reference README put rollout generation, the sandboxed agent
episodes, the test-based reward, the policy update and the weight refit inside
the timed region. Initialization (up to 30 minutes), evaluation and the final
checkpoint write fall outside it. There are enough results to compare: the
official table holds 29 closed-division, Available-category entries from 7
submitters (87 scored runs). The angle needs one correction, and the article
should be built on it. The quality target never decided when a clock stopped.
The rules forbid evaluating any checkpoint before a fixed step,
`CEIL(2.5 + 3840 / GBS)`, which is step 10 at the batch size 28 of 29 entries
used. All 24 reference runs and all 87 scored submission runs passed at that
first eligible checkpoint, with 179 to 197 of 251 held-out tasks solved where
174 were needed. A "minute" on this benchmark is therefore the wall time to run
10 GRPO steps, 5,120 agent trajectories, over the first 320 training tasks in a
fixed order, with a pass/fail quality gate at the end. The official table shows
that buying speed with scale is expensive. On NVIDIA's GB300 vLLM series, 16
times the GPUs (64 to 1,024) cut the time 3.1 times (42.48 to 13.78 minutes),
and accelerator-minutes rose from 2,719 to 14,113. The record is thin in three
places. (1) Accelerator count leaves out the CPU sandbox fleet, although the
rules count dedicated sandbox CPUs toward submission scale. Google's TPU entry
ran its sandboxes on a separate shared CPU pool. (2) The lone non-NVIDIA entry
(Google TPU7x) ran a different workload: batch 1152, 6 steps, 6,912
trajectories. (3) Rollout staleness is a free, per-submitter knob, and the
staleness each entry used is not logged in MLLOG. AMD did not submit, so the
only cross-vendor comparison is one TPU entry against 28 NVIDIA-GPU entries.

## Sources

```text
URL:         https://github.com/mlcommons/training_policies/blob/master/training_rules.adoc
Kind:        primary. MLCommons Training working group's rules; it owns the benchmark definition, timing, run count and scoring.
Establishes: firsthand: model, dataset, closed target, hyperparameter constraints, timed region, offline-eval rule, minimum runs, olympic scoring, RCP rules, harness and sequence-processing rules.
Paraphrase:  The LLM post-training benchmark is qwen35_397b_grpo: Qwen3.5-397B-A17B trained by full-parameter GRPO on R2E-Gym-Subset (easy split), closed target 0.69 pass@4. The run result is wall-clock time for one contiguous period. It includes data use, training and evaluation "unless specified otherwise", and the clock may not pause. Before the clock starts, Closed may spend up to 30 minutes on model initialization (Open: 4 hours). For this benchmark, evaluation is offline. From step CEIL(2.5 + 3840/GBS), a checkpoint is saved every step, each carrying the timestamp of its latest weight update. Checkpoints are evaluated after the run, and run_stop takes the weight-update timestamp of the first passing checkpoint, so writing that checkpoint is excluded. Training must continue "at full capacity" up to the stopping step. Group size is fixed at 16 generations per prompt, and GBS = prompts × 16. LR and gradient clip are functions of GBS (reference points 256, 512, 1024). Fixed: training temperature 1.0 and top-p 1.0; validation temperature 0.1 and top-p 0.95; 30 agent turns; 1,800 s agent timeout; 60 s test timeout; 65,536-token context; no shuffle; no dynamic sampling; no LoRA; no speculative decoding; no partial rollouts. Free and not borrowable: max_trajectory_age_steps (staleness). In-flight weight updates are allowed. Sandboxes may run on CPUs of any architecture, but "any dedicated CPU capacity used for the sandbox counts against the overall submission scale". Every eligible generated sequence must go through the policy forward pass and loss, so zero-advantage groups cannot be filtered out. Minimum runs: 3 (other benchmarks: 3 or 10). Score: drop the fastest and slowest runs and average the rest, so with 3 runs the score is the median. Hyperparameter borrowing is not allowed for this benchmark. RCP generation is owned by "the reference owner (NVIDIA)".
Locators:    Commit 14bc89f (2026-09-30). "Benchmarks" table, line 85. "Closed Division" target table, line 150. Hyperparameters table rows qwen35_397b_grpo, lines 379–416 (sandbox-CPU clause in the agent_prompt_overrides row, line 411; staleness, line 408). "qwen35_397b_grpo hyperparameter constraints", lines 460–478. Borrowing exclusion, line 490. "Quality measure" eval-frequency row, line 510. "Run Results", lines 544–549. "Benchmark Results" minimum-runs table and footnote, lines 554–575. "Scoring", 577+. RCP rules for qwen35, lines 602 and 620. "Appendix: Benchmark Specific Rules", qwen35_397b_grpo, lines 676–687.
Quote:       "the LLM post training benchmark does late eval to hide variance and keep minimum number of submission runs low." (footnote to the minimum-runs table, line 575)
Quote:       "Filtering zero-advantage groups is specifically prohibited because their frequency is an artifact of the benchmark's fixed dataset and limited rollout count" (line 687)
```

```text
URL:         https://github.com/mlcommons/training/blob/master/llm_post_training/README.md
Kind:        primary. MLCommons reference implementation README (implementation provided by NVIDIA NeMo-RL); it owns the reference loop, data split, quality metric and reference runtime.
Establishes: firsthand: the loop as built, the dataset sizes, the reward, the quality metric, the reference hardware layout and the reference runtime.
Paraphrase:  RLVR with GRPO on Qwen3.5-397B-A17B (397B total, 17B active parameters, 512 routed experts with 10 active). Each task gives a repository and an issue. An OpenHands CodeActAgent edits the repo inside a per-task Apptainer container (R2E-Gym) through NeMo Gym. Reward is 1 if the patch passes the task's evaluation, else 0. Loss: token-level GRPO, binary reward, reward normalization, leave-one-out baseline, no KL penalty, PPO ratio clip 0.2/0.28, asynchronous collection. The reference RCPs used max trajectory age 1, and the README says "submissions may use any maximum trajectory-age setting." Training and generation run on separate GPU pools under Ray: Megatron trains, vLLM generates, and weights go to vLLM after every step. The dataset is a 700-task training set and a disjoint 251-task validation set, row order preserved. Quality is grouped pass@4 over the 251 validation tasks: 4 trajectories per task, so 1,004 agent trajectories per evaluation. The first passing score is 174/251 = 0.693. Reference hardware: 256 GB300 GPUs (64 four-GPU nodes): policy on 16 nodes, generation on 48. Reference RCPs used BF16. All 24 RCP runs (6 seeds × GBS 256/512/1024/1152) reached target at the first scheduled validation. The approximate runtime is about 140–160 minutes from run_start to run_stop.
Locators:    Commit e309244 (2026-10-28). "Plain-language summary" and "Technical summary", lines 1–58. "System requirements", 62–80. "Run and time the benchmark" GBS table, 379–410. "3. Dataset and environment", 484–563 (environment settings table, 539–553). "Model details", 578–604. "Benchmark runtime", 606–645. "Loss function", 654–686. "Quality metric", 718–731. "Quality target" RCP table, 733–761. "Evaluation schedule", 763–780. "Offline evaluation", 782–799. "6. Approximate runtime", 801–807.
Quote:       "All 24 runs reach the target at the first scheduled validation. This is stable observed convergence at the configured evaluation schedule; it does not imply zero latent crossing-step variance before the first observation." (Quality target)
```

```text
URL:         https://github.com/mlcommons/training/tree/master/llm_post_training/rcp_logs
Kind:        primary. Reference convergence-point run logs (GBS 256/512/1024 by NVIDIA, GBS 1152 by Google), MLLOG format.
Establishes: firsthand: timestamps, per-step time breakdown and pass@4 of every reference run.
Paraphrase:  My computation from MLLOG lines. Mean run_start→run_stop: GBS256 161.1 min, GBS512 139.6, GBS1024 150.4, GBS1152 150.1. These reference runs evaluated inline, so that span includes evaluation: about 18 to 20 min mean per GBS (eval_start→eval_stop). The training block (run_start→block_stop) averaged GBS256 143.1, GBS512 121.9, GBS1024 130.9, GBS1152 129.7 min. In the per-step tracked_stats, "exposed_generation_time" (time training waited on generation) made up 70% of summed logged step time at GBS256 (84.2 of 120.2 min) and 56% at GBS1152 (46.4 of 83.4). Policy training made up 19% and 32% respectively. Pass@4 at the crossing ranged 0.695–0.781.
Locators:    GBS256/, GBS512/, GBS1024/, GBS1152/ seed_1..6.out; keys run_start, block_stop, eval_start, eval_stop, run_stop, tracked_stats. The README table cites these as rcp_logs/256/ etc.; the directories are named GBS256 etc.
```

```text
URL:         https://github.com/mlcommons/logging/blob/master/mlperf_logging/rcp_checker/training_6.1.0/rcps_qwen35_397b_grpo.json
Kind:        primary. MLCommons logging repository; the reference convergence points the RCP checker enforces.
Establishes: firsthand: the convergence distribution submissions are tested against.
Paraphrase:  Six "Epochs to converge" values per GBS, all identical: 4608 ×6 (GBS256), 5120 ×6 (512), 7168 ×6 (1024), 6912 ×6 (1152). The 1152 points have Creator "Google", "Reference RCPs at BS=1152 on 64xGB200 using MLCommons reference code". The others have Creator "NVIDIA", "64 NVIDIA GB300 nodes". With zero spread and no evaluation allowed earlier, the RCP test and its normalization (RCP-mean / submission samples) cannot change a result.
Locators:    Keys qwen35_397b_grpo_ref_256/512/1024/1152; commit 53b389a (2026-10-27; 1152 entry merged via PR #485).
```

```text
URL:         https://github.com/mlcommons/logging/blob/master/mlperf_logging/compliance_checker/training_6.1.0/closed_qwen35_397b_grpo.yaml
Kind:        primary. MLCommons compliance checker for closed submissions.
Establishes: firsthand: which logged values a closed result must have.
Paraphrase:  validation_start_samples = GBS × ceil(2.5 + 3840/GBS). The first eval_accuracy must sit at exactly that samples_count, and later ones at +GBS each. Also checked: eval_samples = 251, max_sequence_length = 65536, num_generations_per_prompt = 16, GBS = prompts × 16, the LR formula, temperatures and top-p, target 0.69.
Locators:    BEGIN block; KEY global_batch_size POST; KEY eval_accuracy.
```

```text
URL:         https://github.com/mlcommons/training_results_v6.1
Kind:        primary. The official published results repository (MLCommons commit "Publishing Results", d5458b9, 2026-11-16); each submitter's own logs and system descriptions.
Establishes: firsthand: every scored run's MLLOG timestamps, eval accuracy, GBS and config; every system's accelerator type and count, division, availability, host CPUs and notes.
Paraphrase:  29 result directories <Submitter>/results/<system>/qwen35_397b_grpo/, each with 3 result files (87 runs). Every system JSON says division "closed", status "Available cloud" or "Available on-premise". Every run's run_stop status is success. Every GPU run stopped at samples_count 5120 (GBS 512) and the TPU run at 6912 (GBS 1152), i.e. at the first eligible checkpoint. Pass@4 of scored checkpoints: 0.7131–0.7849. Initialization (init_start→init_stop, off clock) took 9.7–23.4 minutes. Offline evaluation (off clock) took 2.4–20.4 minutes on GPU entries and 35.0–48.8 minutes on the TPU entry. Runs trained one step past the scored checkpoint (11 steps; TPU to step 10), and those steps are not scored. In Theia 64-GPU TRT-LLM result_0, step 1 finished 13.71 min after run_start with a step time of 3.34 min. About 10.4 minutes of the 35.84-minute score elapsed before the first policy step started. At 1,024 GB300 (vLLM, result_0) the same gap was about 4.0 of 12.93 minutes. The NVIDIA README attributes this to the training pool waiting while "the rollout buffer fills".
Locators:    e.g. NVIDIA/results/theia-jhb_ngpu1024_nemo_rl_vllm/qwen35_397b_grpo/result_0..2.txt; <Submitter>/systems/<system>.json. Note: many logs record submission_status "onprem" even where the system JSON says "Available cloud"; the explorer follows the system JSON.
```

```text
URL:         https://results.mlcommons.org/training
Kind:        primary. MLCommons' official results explorer (model filter "Qwen3.5 397B GRPO", v6.1); owns the published result IDs and minutes.
Establishes: firsthand: the 29 official rows with public IDs, minutes, accelerator count, division, availability, precision and parallelism.
Paraphrase:  29 rows for qwen35_397b_grpo in v6.1, all closed, all Available (cloud or on-premise), all precision "fp8". The minutes match the median-of-three I computed from the repository logs for every row. Full series under Numbers.
Locators:    Model select → Qwen3.5 397B GRPO; row data embedded in the page as objects {id:"6.1-NNNN:qwen35_397b_grpo", ...}. Fetched 2026-11-28.
```

```text
URL:         https://github.com/mlcommons/training_results_v6.1/blob/main/Google/systems/tpu7x-4x4x8-128x2x2x1.json
Kind:        primary for Google's own submission (submitter-authored system description in the official repo).
Establishes: firsthand: what Google's 640-chip count does and does not include.
Paraphrase:  160 hosts × 4 TPU7x = 640 chips. The trainer is 1 × 4x4x8 slice (128 chips); rollout is 128 × 2x2x1 single-host slices (512 chips) running vLLM on tpu-inference, with weights sent over DCN. Sandboxes ran on "GKE CPU node pools shared by the concurrent runs on the cluster": 508 sandbox nodes, 39,780 vCPUs total. Each run requested 6,160 vCPUs for 11,200 pre-warmed pods, and 1,681–1,734 vCPUs at 3,056–3,152 peak concurrent pods. Separate controller nodes are listed too. Scored checkpoints were "evaluated offline on 32 x tpu7x-2x2x4 slices (512 TPU7x chips)" ("not timed"). sw_notes: asynchronous, in-flight GRPO with max_staleness=2. Policy runs on MaxText/Pathways (FSDP 32, CP 4, EP 2).
Locators:    fields number_of_nodes, accelerators_per_node, accelerator_interconnect_topology, hw_notes, sw_notes.
```

```text
URL:         https://github.com/mlcommons/training_results_v6.1/blob/main/NVIDIA/benchmarks/qwen35_397b_grpo/implementations/theia-jhb_ngpu1024_nemo_rl_vllm/README.md
Kind:        primary for NVIDIA's own implementation (submitter-authored).
Establishes: firsthand: NVIDIA's config naming (train/generation node split), where sandboxes run, the evaluation procedure.
Paraphrase:  Every config splits nodes into a policy-training pool and a generation pool, named config_<SYSTEM>_<NODES>x<GPUS/NODE>_t<TRAIN>g<GEN>_... (TRAIN and GEN are node counts). The R2E-Gym sandboxes "run as Apptainer SIF images inside the training container" on the compute nodes. Asynchronous GRPO "leaves the training pool idle while the rollout buffer fills". After training, validation restores steps VAL_START_AT and VAL_START_AT+1.
Locators:    "1. Hardware Requirements"; section 4 run notes; "5. Quality → Evaluation frequency"; "6. Additional notes → Config naming convention". Same-directory config_GB300_256x4_t64g192_tp4pp2ep32gtp8_mxfp8.sh sets TRAIN_NODES=64, GEN_NODES=192, COLOCATED_GENERATION=0 and sources config_GBS512.sh (32 prompts × 16). config_common.sh sets MAX_TRAJECTORY_AGE_STEPS default 4. That default is not overridden in the 1024 config, but no MLLOG key records the value used.
```

```text
URL:         https://mlcommons.org/2026/11/mlperf-training-v6-1-results/
Kind:        primary for the round's announcement (MLCommons press release, 16 Nov 2026).
Establishes: firsthand: round date, 24 submitters, the benchmark's introduction; no per-benchmark numbers.
Paraphrase:  24 organizations; 153 systems; 250 results. The two new benchmarks are DLRMv4-HSTU and Qwen3.5-397B, the latter described as a first-of-its-kind large-scale GRPO post-training workload on software-engineering tasks. No timing definition or results for it.
Locators:    body paragraphs on new benchmarks and participation; quotes attributed to Pavan Yalamanchili and Shriya Rishab ("MLPerf Training working group co-chair") and David Kanter ("Head of MLPerf at MLCommons").
```

```text
URL:         https://mlcommons.org/benchmarks/training/
Kind:        primary. MLCommons benchmark catalog; owns division and availability definitions.
Establishes: firsthand: benchmark row (LLM post-training, R2E-Gym-Subset easy split, 0.69 pass@4, Qwen3.5-397B-A17B, v6.1); Closed/Open and Available/Preview/RDI definitions.
Paraphrase:  Closed requires the reference model, for "apples-to-apples" hardware/software comparison. Open allows a different model. Available means purchasable or rentable; Preview must become Available next round; RDI covers research/internal systems.
Locators:    benchmark table, first row; "Divisions"; "Availability".
```

```text
URL:         https://mlcommons.org/2026/11/mlperf-training-v6-1-insights/
Kind:        primary for MLCommons' own analysis of the round; authored by Shriya Rishab (NVIDIA, MLPerf Training Chair), Pavan Yalamanchili (Meta, MLPerf Training Chair), Alejandro Caruso (MLCommons) and David Kanter (MLCommons). The co-authors include an NVIDIA employee.
Establishes: firsthand: submitter/submission counts, sandbox concurrency range, train/generation split trend, FP8 use.
Paraphrase:  "Seven submitters ran it, with 29 submissions." Submissions ran "from about 500 to roughly 3,150 concurrent sandboxes per workload (with a 4,096 cap on a shared CPU pool)". As systems grow from 64 to 1,024 GPUs, "the split shifts toward generation, from 32 training and 32 generation GPUs to 256 and 768". "Every DeepSeek-V3 and Qwen3.5 GRPO result used FP8 in linear layers." Its ratios "are MLCommons-derived, not official MLPerf results." Published 17 Nov 2026.
Locators:    "Benchmark Updates"; "Multi-node systems are the norm → Host CPUs"; "The complexity of Large Scale Training → What strategies have been used?"; "Optimizations → Numerical precision".
```

```text
URL:         https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/
Kind:        primary for NVIDIA's own submissions and its claims about them (Farshad Ghodsian and Sukru Burc Eryilmaz, NVIDIA, 16 Nov 2026); secondary for any comparison involving others' entries (it uses Google's 6.1-0020 as its GB300 baseline).
Establishes: firsthand: NVIDIA's claims; the table checks them.
Paraphrase:  Vera Rubin NVL72 had "the fastest time ... 10.44 minutes at 1,024 GPUs (6.1-0117), compared with 13.78 minutes for GB300 NVL72 (6.1-0031) at the same scale". Two backends: TensorRT-LLM 10.44 and vLLM 10.94 (6.1-0118). Table 1 gives Qwen3.5 397B GRPO at 64 GPUs, "1.4x" Vera Rubin vs "optimized GB300 NVL72", IDs 6.1-0135 / 6.1-0020. It also claims the Vera CPU sustains "more than 22,500 concurrent RL environments across 256 CPUs in a single Vera CPU rack".
Locators:    section "Post-training arrives, and Vera Rubin leads it"; Table 1 and its footnote; Figure 1 caption.
```

```text
URL:         https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/
Kind:        primary for NVIDIA's corporate claim (Shruti Koparkar, 16 Nov 2026).
Establishes: only that NVIDIA claims a sweep and coverage that includes "reinforcement learning post-training"; no GRPO numbers.
Paraphrase:  General sweep claim; links the technical blog above for MLPerf Training detail.
Locators:    MLPerf Training section.
```

```text
URL:         https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/training-performance-benchmarks-tpus/
Kind:        primary for Google's claims about its own submissions (no byline; published 16 Nov 2026, updated 18 Nov 2026).
Establishes: firsthand: Google's claim; the table checks the minutes and chips.
Paraphrase:  "640 Ironwood TPUs reached the target model's coding benchmark target accuracy in 18.02 minutes (0.765 vs. the 0.69 goal), running code generation and learning simultaneously so training chips waited under 3% of the time." The footnote lists IDs 6.1-0017 to 6.1-0026, labelling 6.1-0017 "Ironwood 640-chip Qwen3.5-397B RL".
Locators:    "Agentic RL on Ironwood" paragraph; footnote 1.
```

```text
URL:         https://www.amd.com/en/blogs/2026/amd-advances-ai-training-across-more-workloads-in-mlperf-training.html
Kind:        primary for AMD's own submission scope (Jerry Zhang, AMD).
Establishes: firsthand: AMD submitted five benchmarks; GRPO is not among them (no mention of Qwen, GRPO, post-training or reinforcement learning).
Paraphrase:  AMD went from three to five benchmarks by adding GPT-OSS-20B and DLRMv4, and claims a ~16% average speedup vs v6.0 on Llama 2 70B LoRA and Llama 3.1 8B (not an official MLPerf score). The results repository has no AMD qwen35_397b_grpo directory.
Locators:    body paragraphs on benchmark coverage.
```

## Contradictions

- **The benchmark's name vs its behaviour.** MLPerf calls this time to train to a quality target. In this round the target never ended a run. Every scored run (87/87) and every reference run (24/24) passed at the first checkpoint the rules allow evaluating, with 179–197 tasks solved against the 174 needed. The rules' own footnote says the late first evaluation exists "to hide variance". The time therefore measures how fast a system executes a fixed number of GRPO steps. Convergence speed does not enter it. A writer should not say systems "reached quality faster".
- **NVIDIA's 1.4x vs its own 1,024-GPU figures.** 13.78 / 10.44 = 1.32x, not 1.4x. The 1.4x row is a different comparison: 64 GPUs, Nebius VR200 (6.1-0135, 24.82 min) vs Google A4X Max GB300 (6.1-0020, 34.17 min) = 1.38x. NVIDIA's comparison uses two other companies' entries. The table bears both numbers out as arithmetic. The 1,024-GPU headline does not hold the inference backend constant: 10.44 is TensorRT-LLM, and 13.78 is the only 1,024-GB300 entry, which ran vLLM. Same backend (vLLM vs vLLM, 10.94 vs 13.78) the ratio is 1.26x. NVIDIA's own same-backend 64-GPU pairs give 1.43x (TRT-LLM, 25.93 vs 36.99) and 1.32x (vLLM, 32.18 vs 42.48).
- **Google's footnote IDs vs the official table.** Google's blog labels 6.1-0017 "Ironwood 640-chip Qwen3.5-397B RL" and 6.1-0021–0025 as A4X RL entries. In the official explorer, 6.1-0017 is Google 14xGB200_NVL72 (Qwen, 43.30 min) and the TPU Qwen entry is 6.1-0023. Its labels for 6.1-0018 to 0026 do not match the explorer either: in the explorer, 6.1-0024 to 0026 are TPU DeepSeek-V3 entries and 6.1-0022 is GB300 DeepSeek-V3. NVIDIA's blog cites 6.1-0020 as Google's 64-GPU GB300 Qwen entry, which matches the explorer. Google's minutes (18.02), chip count (640) and accuracy (0.765, the pass@4 of the median-time run, result_1) match the table. Only the ID labels conflict.
- **Google's "training chips waited under 3% of the time".** Not checkable from the official record. Google's logged per-step stats are implementation-specific (their summed step times exceed the scored wall time, so they are not a breakdown of it). The claim also covers only the 128 trainer chips, while 512 of the 640 chips do rollout.
- **NVIDIA's "22,500 concurrent RL environments ... in a single Vera CPU rack"** vs MLCommons' "about 500 to roughly 3,150 concurrent sandboxes per workload (with a 4,096 cap on a shared CPU pool)". NVIDIA's figure describes capability. No submission in the table shows anything near it.
- **Accelerator count vs the rules' definition of scale.** The rules say dedicated sandbox CPU capacity "counts against the overall submission scale". The table's accelerator column counts only accelerators. Google's TPU entry ran up to ~3,150 concurrent sandbox pods on a separate, shared 39,780-vCPU GKE pool, plus controller nodes. NVIDIA-recipe entries ran sandboxes on the Grace/Vera host CPUs inside the same nodes. Accelerator-minutes therefore omit a resource the two architectures provision differently.
- **Reference runtime vs submission scores.** The reference README gives "approximately 140 to 160 minutes" from run_start to run_stop. Those reference runs evaluated inline, with about 18–20 minutes of evaluation inside that span. Submissions must evaluate offline, off the clock. The reference figure is not the same quantity as a score. Measured on the same work (10 steps at GBS 512, 256 GB300 GPUs), the reference training block averaged 121.9 minutes against NVIDIA's 20.11-minute submission (6.1-0040), about 6x. The reference was qualified for convergence, in BF16 with staleness 1. It was not tuned for speed.
- **GBS definition in the rules.** The hyperparameter table defines global_batch_size as "global batch size in problems (prompts) per training step". The same row, the compliance checker and every log count trajectories: GBS = prompts × 16, and 512 at GBS 512 means 32 prompts.
- **Commission premise "Vendor claims ... AMD".** AMD made no claim about this benchmark and submitted no result.

## Numbers

```text
Figure: 29 official results, 7 submitters, 87 scored runs; all Closed, all Available (18 cloud, 11 on-premise); 0 Open, 0 Preview, 0 RDI
Owner:  results.mlcommons.org/training (qwen35_397b_grpo, v6.1); training_results_v6.1 system JSONs; MLCommons insights ("Seven submitters ran it, with 29 submissions")
Scope:  MLPerf Training v6.1, published 16 Nov 2026
```

```text
Figure: 0.69 pass@4 target = at least 174 of 251 held-out tasks solved by one or more of 4 attempts; each evaluation runs 1,004 agent trajectories
Owner:  training_rules.adoc line 150, 396; reference README "Quality target"
Scope:  validation set of 251 R2E-Gym tasks, disjoint from the 700 training tasks
```

```text
Figure: first eligible evaluation at GBS × CEIL(2.5 + 3840/GBS) samples = step 18 (GBS 256), 10 (512), 7 (1024), 6 (1152); i.e. 4,608 / 5,120 / 7,168 / 6,912 trajectories
Owner:  training_rules.adoc line 510; compliance checker; RCP JSON
Scope:  a scored run cannot stop earlier than this
```

```text
Figure: 10 steps × 32 prompts = 320 of the 700 training tasks used before the scored checkpoint at GBS 512 (6 × 72 = 432 at GBS 1152); shuffle disabled, so the same tasks in the same order for every run
Owner:  derived from training_rules.adoc lines 380–381, 406 and the logged samples_count
Scope:  per scored run
```

```text
Figure: reference RCPs: 6 of 6 seeds at each of 4 GBS converge at the first eligible checkpoint; RCP spread = 0
Owner:  reference README "Quality target"; rcps_qwen35_397b_grpo.json
Scope:  24 reference runs (18 NVIDIA on 256 GB300; 6 Google on 256 GB200)
```

```text
Figure: scored-run pass@4 range 0.7131–0.7849 (179–197 of 251 tasks); every run stopped at the first eligible checkpoint
Owner:  training_results_v6.1 result_*.txt eval_accuracy and run_stop samples_count
Scope:  87 runs, 29 entries
```

```text
Figure: off-clock time per run: initialization 9.7–23.4 min (limit 30); offline evaluation 2.4–20.4 min on GPU entries, 35.0–48.8 min on the TPU entry (on 512 extra TPU7x chips per Google's system JSON)
Owner:  training_results_v6.1 result logs (init_start/init_stop, eval_start/eval_stop); Google system JSON hw_notes
Scope:  87 runs
```

```text
Figure: time before the first policy step completes (rollout buffer fill), result_0: Theia 64 GB300 TRT-LLM ~10.4 of 35.84 min; Google 16xGB300 ~11.5 of 37.39 min; Theia 1,024 GB300 vLLM ~4.0 of 12.93 min; Hecate 1,024 Rubin TRT-LLM ~3.0 of 10.89 min
Owner:  derived from training_results_v6.1 logs (end time of step-1 tracked_stats minus step-1 train_step_time)
Scope:  one run per entry shown; illustrative, not computed for all 87
```

```text
Figure: reference RCP per-step breakdown: exposed generation 70% of summed step time at GBS 256 (84.2 of 120.2 min), 56% at GBS 1152 (46.4 of 83.4); inline eval ~18–20 min per run
Owner:  training/llm_post_training/rcp_logs (tracked_stats; eval_start/eval_stop)
Scope:  6 seeds per GBS; summed over logged steps (the final step's stats precede eval and are partly missing)
```

Full official series. Train/gen GPU split is from config filenames using NVIDIA's naming convention. It is confirmed in config for NVIDIA 1,024 (64/192 nodes) and by Oracle's sw_notes for 56 (8/6 nodes), and MLCommons confirms the 32/32 and 256/768 splits. "n/r" means not recorded. Backend comes from the system JSON framework/sw_notes. Pass@4 is that of the median-time (scored) run. Accelerator-minutes = score × accelerator count (my derivation, not an official metric).

| ID | Submitter | System | Accelerator | Count | Train/Gen | Backend | GBS | 3 runs (min) | Score (min) | Accel-min | Availability | pass@4 |
|---|---|---|---|---:|---|---|---:|---|---:|---:|---|---:|
| 6.1-0117 | NVIDIA | Hecate (16x NVIDIA VR NVL72) | Rubin | 1024 | 256/768 | TRT-LLM | 512 | 10.89, 10.44, 10.14 | 10.44 | 10,696 | Available on-premise | 0.757 |
| 6.1-0118 | NVIDIA | Hecate (16x NVIDIA VR NVL72) | Rubin | 1024 | 256/768 | vLLM | 512 | 10.94, 11.18, 10.71 | 10.94 | 11,206 | Available on-premise | 0.741 |
| 6.1-0031 | NVIDIA | Theia-jhb (16x NVIDIA GB300 NVL72) | GB300 | 1024 | 256/768 | vLLM | 512 | 12.93, 13.78, 14.77 | 13.78 | 14,113 | Available cloud | 0.757 |
| 6.1-0131 | NVIDIA | Hecate (4x NVIDIA VR NVL72) | Rubin | 256 | 128/128 | vLLM | 512 | 13.96, 14.33, 15.27 | 14.33 | 3,669 | Available on-premise | 0.745 |
| 6.1-0043 | NVIDIA | Theia-jhb (8x NVIDIA GB300 NVL72) | GB300 | 512 | 256/256 | vLLM | 512 | 14.52, 14.28, 15.31 | 14.52 | 7,433 | Available cloud | 0.741 |
| 6.1-0023 | Google | tpu7x-4x4x8-128x2x2x1 | TPU7x (Ironwood) | 640 | 128/512 | vLLM (tpu-inference) | 1152 | 17.90, 18.02, 19.43 | 18.02 | 11,534 | Available cloud | 0.765 |
| 6.1-0056 | Oracle | BM.GPU.GB300.4 | GB300 | 256 | 128/128 | TRT-LLM | 512 | 20.11, 20.63, 19.12 | 20.11 | 5,149 | Available cloud | 0.721 |
| 6.1-0040 | NVIDIA | Theia-jhb (4x NVIDIA GB300 NVL72) | GB300 | 256 | 128/128 | vLLM | 512 | 20.11, 20.33, 19.99 | 20.11 | 5,149 | Available cloud | 0.741 |
| 6.1-0021 | Google | 64xGB200_NVL72 (A4X) | GB200 | 256 | 128/128 | TRT-LLM | 512 | 21.57, 20.44, 21.03 | 21.03 | 5,383 | Available cloud | 0.773 |
| 6.1-0047 | NVIDIA | Tyche-hsg (4x NVIDIA GB200 NVL72) | GB200 | 256 | 128/128 | vLLM | 512 | 21.60, 20.49, 22.68 | 21.60 | 5,530 | Available cloud | 0.773 |
| 6.1-0072 | CoreWeave | CoreWeave_GB200_64x4_ngc2608 | GB200 | 256 | 128/128 | TRT-LLM | 512 | 23.20, 22.78, 22.74 | 22.78 | 5,831 | Available on-premise | 0.721 |
| 6.1-0135 | Nebius | Nebius VR200 n16 (16x NVIDIA VR200 NVL4) | Rubin | 64 | 32/32 | TRT-LLM | 512 | 24.71, 24.82, 25.22 | 24.82 | 1,588 | Available on-premise | 0.749 |
| 6.1-0121 | NVIDIA | Hecate (1x NVIDIA VR NVL72) | Rubin | 64 | 32/32 | TRT-LLM | 512 | 25.93, 24.10, 26.81 | 25.93 | 1,659 | Available on-premise | 0.761 |
| 6.1-0119 | NVIDIA | Hecate (1x NVIDIA VR NVL72) | Rubin | 56 | 32/24 | TRT-LLM | 512 | 28.47, 29.21, 26.39 | 28.47 | 1,594 | Available on-premise | 0.769 |
| 6.1-0122 | NVIDIA | Hecate (1x NVIDIA VR NVL72) | Rubin | 64 | 32/32 | vLLM | 512 | 31.92, 34.42, 32.18 | 32.18 | 2,060 | Available on-premise | 0.777 |
| 6.1-0020 | Google | 16xGB300_NVL72 (A4X Max) | GB300 | 64 | 32/32 | TRT-LLM | 512 | 37.39, 34.17, 33.77 | 34.17 | 2,187 | Available cloud | 0.713 |
| 6.1-0052 | Oracle | BM.GPU.GB300.4 | GB300 | 64 | 32/32 | TRT-LLM | 512 | 35.07, 36.32, 34.99 | 35.07 | 2,244 | Available cloud | 0.749 |
| 6.1-0034 | NVIDIA | Theia-jhb (1x NVIDIA GB300 NVL72) | GB300 | 64 | 32/32 | TRT-LLM | 512 | 35.84, 39.05, 36.99 | 36.99 | 2,367 | Available cloud | 0.741 |
| 6.1-0049 | Nebius | Nebius GB300 n16 (16x NVIDIA GB300 NVL4) | GB300 | 64 | 32/32 | TRT-LLM | 512 | 37.61, 37.01, 35.16 | 37.01 | 2,369 | Available cloud | 0.733 |
| 6.1-0046 | NVIDIA | Tyche-hsg (1x NVIDIA GB200 NVL72) | GB200 | 64 | 32/32 | TRT-LLM | 512 | 41.88, 40.21, 39.86 | 40.21 | 2,573 | Available cloud | 0.741 |
| 6.1-0018 | Google | 14xGB300_NVL72 (A4X Max) | GB300 | 56 | 32/24 | TRT-LLM | 512 | 41.59, 40.57, 39.28 | 40.57 | 2,272 | Available cloud | 0.757 |
| 6.1-0032 | NVIDIA | Theia-jhb (1x NVIDIA GB300 NVL72) | GB300 | 56 | 32/24 | TRT-LLM | 512 | 41.44, 41.76, 40.87 | 41.44 | 2,321 | Available cloud | 0.749 |
| 6.1-0019 | Google | 16xGB200_NVL72 (A4X) | GB200 | 64 | 32/32 | TRT-LLM | 512 | 40.63, 42.97, 41.67 | 41.67 | 2,667 | Available cloud | 0.745 |
| 6.1-0035 | NVIDIA | Theia-jhb (1x NVIDIA GB300 NVL72) | GB300 | 64 | 32/32 | vLLM | 512 | 43.28, 41.76, 42.48 | 42.48 | 2,719 | Available cloud | 0.777 |
| 6.1-0051 | Oracle | BM.GPU.GB300.4 | GB300 | 56 | 32/24 | TRT-LLM | 512 | 41.33, 43.25, 46.71 | 43.25 | 2,422 | Available cloud | 0.717 |
| 6.1-0017 | Google | 14xGB200_NVL72 (A4X) | GB200 | 56 | 32/24 | TRT-LLM | 512 | 43.30, 43.05, 44.20 | 43.30 | 2,425 | Available cloud | 0.773 |
| 6.1-0148 | University of Florida | HiPerGator NVIDIA DGX B200 (32 nodes) | B200 | 256 | 128/128 | n/r | 512 | 44.55, 43.92, 42.83 | 43.92 | 11,243 | Available on-premise | 0.745 |
| 6.1-0146 | University of Florida | HiPerGator NVIDIA DGX B200 (16 nodes) | B200 | 128 | 64/64 | n/r | 512 | 61.14, 63.76, 65.82 | 63.76 | 8,161 | Available on-premise | 0.749 |
| 6.1-0069 | Cisco | Zeus_8xB300_SXM_288GB_multi_planar | B300 | 64 | n/r | TRT-LLM | 512 | 100.21, 102.99, 99.25 | 100.21 | 6,413 | Available on-premise | 0.753 |

Counts by scale: 56 GPUs ×5, 64 ×11, 128 ×1, 256 ×7, 512 ×1, 640 (TPU) ×1, 1,024 ×3. By accelerator: GB300 12, Rubin 7, GB200 6, B200 2, B300 1, TPU7x 1. NVIDIA submitted 14 of the 29. All 28 GPU entries list NVIDIA NeMo RL, NeMo/Megatron or NVIDIA's MLPerf containers in their framework or sw_notes fields.

Scaling series (same submitter, chip and backend; speedup and efficiency are my derivations from official minutes):

```text
Figure: Theia GB300 vLLM: 64 → 42.48 min (2,719 accel-min); 256 → 20.11 (5,149); 512 → 14.52 (7,433); 1,024 → 13.78 (14,113). 16x GPUs → 3.08x faster (19% scaling efficiency); 512→1,024 doubled GPUs for 5% less time
Owner:  results explorer IDs 6.1-0035, 0040, 0043, 0031
Scope:  GBS 512, 10 steps, closed
```

```text
Figure: Hecate Rubin vLLM: 64 → 32.18 (2,060); 256 → 14.33 (3,669); 1,024 → 10.94 (11,206); 16x GPUs → 2.94x faster
Owner:  IDs 6.1-0122, 0131, 0118
Scope:  GBS 512
```

```text
Figure: Hecate Rubin TRT-LLM: 56 → 28.47 (1,594); 64 → 25.93 (1,659); 1,024 → 10.44 (10,696). The fastest result in the table used 6.7x the accelerator-minutes of the 56-GPU run on the same chip and backend
Owner:  IDs 6.1-0119, 0121, 0117
Scope:  GBS 512
```

```text
Figure: other 64/56 → 256 pairs: Tyche GB200 40.21 → 21.60 (1.86x for 4x GPUs); Google GB200 41.67 (64) → 21.03 (256); Oracle GB300 35.07 (64) → 20.11 (256); University of Florida B200 63.76 (128) → 43.92 (256, 1.45x for 2x)
Owner:  IDs 6.1-0046/0047, 0019/0021, 0052/0056, 0146/0148
Scope:  GBS 512
```

```text
Figure: software/backend effect on identical hardware: Theia 64 GB300 TRT-LLM 36.99 vs vLLM 42.48 (vLLM 15% slower); Hecate 64 Rubin TRT-LLM 25.93 vs vLLM 32.18 (24% slower); at 1,024 Rubin TRT-LLM 10.44 vs vLLM 10.94 (5%)
Owner:  IDs 6.1-0034/0035, 0121/0122, 0117/0118
Scope:  GBS 512
```

```text
Figure: same accelerator, same 64-GPU scale, different submitters (GB300, TRT-LLM): Google 34.17, Oracle 35.07, NVIDIA 36.99, Nebius 37.01 min; Cisco B300 (8-GPU HGX nodes, not NVL72) 100.21
Owner:  IDs 6.1-0020, 0052, 0034, 0049, 0069
Scope:  GBS 512
```

```text
Figure: TPU entry: 640 chips (128 trainer + 512 rollout), 18.02 min, 11,534 chip-minutes, GBS 1152 → 6 steps, 6,912 trajectories (35% more trajectories and 40% fewer optimizer steps than every GPU entry)
Owner:  ID 6.1-0023; Google system JSON; compliance formula
Scope:  not the same work unit as the GPU entries
```

```text
Figure: run-to-run spread within an entry (max/min − 1): 1.7% to 14.2% (largest: Oracle 56 GB300, 41.33–46.71)
Owner:  training_results_v6.1 result logs
Scope:  3 runs per entry
```

```text
Figure: reference vs submission at the same scale and work: 256 GB300, GBS 512, 10 steps: reference training block mean 121.9 min (6 seeds) vs NVIDIA 6.1-0040 score 20.11 min (~6x)
Owner:  rcp_logs/GBS512; results explorer
Scope:  reference used BF16, staleness 1, inline eval; submission FP8 (MXFP8), async with NVIDIA default staleness 4 (config default, not logged)
```

## Limits

- No MLLOG key records each submission's max_trajectory_age_steps (staleness). I have Google's value (max_staleness=2, system JSON) and NVIDIA's config default (4). Whether every NVIDIA-recipe entry used 4 is not established.
- No submission reports its total CPU sandbox capacity in a comparable form. Only Google's TPU JSON quantifies it. Accelerator-minutes cannot be corrected for CPUs.
- The train/generation split for the Cisco entry is not recorded in its config name. University of Florida entries do not state their generation backend.
- The per-step "tracked_stats" breakdowns (policy training, exposed generation, weight sync) are implementation-logged and not required by MLPerf. Google's and Nebius VR200's summed step times exceed their scored wall times, so the stats cannot serve as a cross-submitter breakdown of the minute. Only the reference logs and the NVIDIA-recipe logs read cleanly.
- Why 28 of 29 entries chose GBS 512 is not stated in any document I read. Arithmetic is suggestive: GBS 512 needs 10 steps and 5,120 trajectories, GBS 256 needs 18 steps and 4,608, GBS 1024 needs 7 steps and 7,168. That is not evidence of the submitters' reasoning.
- Google's "training chips waited under 3% of the time" cannot be verified from the official record.
- There is no prior round to compare against. This is the benchmark's first round.
- The rules contain no explicit statement that the sandbox CPUs are inside or outside the clock. They run during the training block, which is timed, so their execution time is inside the measured minutes. What is undefined is how their capacity enters "scale".

## Source assets

```text
Asset: Results explorer chart "Time to train versus accelerator count", model filter Qwen3.5 397B GRPO, Closed, v6.1 (results.mlcommons.org/training)
Shows: all 29 points on minutes vs accelerators, coloured by submitter/accelerator family; the flattening from 256 to 1,024 GPUs is visible
Crop:  keep both axes with labels, the filter bar showing the model/division/version, and the legend; omit the site header and table below
```

```text
Asset: Reference README, "Quality target" table (six seeds per GBS, first observed crossing step, pass@4 range) — training/llm_post_training/README.md lines 747–756
Shows: every reference seed crossing at the first scheduled validation, the basis of the "gate never binds" finding
Crop:  keep the full table with header and the sentence after it ("All 24 runs reach the target at the first scheduled validation...")
```

```text
Asset: training_rules.adoc "qwen35_397b_grpo hyperparameter constraints" table (GBS 256/512/1024 with LR, clip, prompts, generations) and the minimum-runs table with its footnote
Shows: the fixed GBS-dependent schedule and the "late eval to hide variance" footnote
Crop:  keep the table header and all rows; keep the asterisked footnote with the minimum-runs table
```

```text
Asset: Google system JSON hw_notes for tpu7x-4x4x8-128x2x2x1 (GitHub file view)
Shows: the 128-trainer / 512-rollout split, the shared GKE CPU pool, and "[Offline evaluation, not timed] ... 512 TPU7x chips"
Crop:  keep the hw_notes line in full; the rest of the JSON can be omitted
```

```text
Asset: NVIDIA technical blog Table 1 row "Qwen3.5 397B GRPO (RL) | 64 | 1.4x | 6.1-0135 / 6.1-0020" and its footnote
Shows: which entries the 1.4x claim compares (Nebius VR200 vs Google GB300 at 64 GPUs)
Crop:  keep the column headers, the Qwen row, and the footnote's ID list
```

```text
Asset: Google blog, footnote 1 ID list
Shows: the ID labels that conflict with the official explorer
Crop:  keep the full ID list sentence
```

For the press release, benchmarks catalog, insights article, AMD blog, NVIDIA corporate blog, RCP JSON and compliance checker: None found. There are no visuals specific to this benchmark, or the text says it better.

## Discarded

```text
https://developers.googleblog.com/en/systems-engineering-playbook-optimizing-qwen-35-397b-moe-on-ironwood-tpu7x/: July 2026 inference-serving post; no MLPerf, GRPO or training content
https://mlcommons.org/working-groups/benchmarks/training/: working-group page; no v6.1 results table or GRPO rows
https://mlcommons.org/results-change-log/: no v6.1 entries (confirms no post-publication modification of these results as of 2026-11-28; nothing to cite beyond that)
https://github.com/mlcommons/training_results_v6.1/blob/main/.github/workflows/update_summary.yml: points to a results_branch summary CSV that does not exist on the remote; the explorer and logs were used instead
```
