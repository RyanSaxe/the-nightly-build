# Evidence record: Epoch's Inference Performance Index (researcher 01)

Run date 2026-11-21. Every figure below was read in the document named; "my arithmetic" marks numbers I computed from them. All files named under `data/` are in `researcher/01/data/`.

**What the evidence supports, and where it is thin.** The headline survives its primary. Jason Li's Epoch AI report (9 Nov 2026) says GB300 provides "about 25×" an H100's inference capacity per chip on 8-bit FLOP/s that are 2.5× higher, and the 2.5× checks against Epoch's hardware database (5.0 vs 1.979 PFLOP/s dense FP8, ratio 2.53). The 4.6× vs 2.6× capacity series reproduces from the CSV (4.583 vs 2.594). The angle needs three corrections the primaries force. (1) The 25× is the arithmetic mean of four per-model ratios and is almost entirely one model: H100 scores 0.125 on Qwen3-Coder 480B and 0.005 to 0.023 on the other three, so 79% of its index is Qwen. Per model, GB300 is 8× to 200× an H100; a geometric mean gives 59×. (2) The FLOP/s-versus-capacity gap in the series is composition, not per-chip change: every Nvidia and TPU family's score per unit of FP8 compute is fixed across quarters, and about 95% of the rise in capacity per H100e is mix shift (Blackwell Ultra went from 4.5% to 30.6% of peak compute; Google TPU v7 from 0% to 9.0%), the rest drift inside the AMD, Trainium and other-chip families. TPU v7 is 17% of added capacity, nearly as much as Blackwell B200/GB200. (3) The index is a speed-of-light model with no software discount, validated against measurement only at five Kimi K3 points on GB300; no H100 comparison is validated. Independent benchmarks (SemiAnalysis InferenceX) put GB300/H100 between 12× and 36× on DeepSeek R1 depending on the interactivity target, and up to 65× to 100× at 116 tok/s/user, so Epoch's 25× is inside the range and the target decides where. Thin: no independent long-context (262k) H100 vs GB300 measurement exists in what I could open.

## Sources

URL:         https://epoch.ai/publications/inference-performance-index
Kind:        primary for the IPI definition, the 25×, the 2.5× and the scores. Author is the index's creator. Page title tag: "Changing how we measure AI chip inference performance | Epoch AI"; on-page title "Inference Performance Index: changing the way we measure inference capacity".
Establishes: firsthand: definition, the four-model basket, 50 to 400 tokens/s/req log-axis integral, the reference chip, the headline ratios and the limits notes.
Paraphrase:  Report, published 9 Nov 2026, "By Jason Li". Author line: "Jason Li is a researcher at Epoch AI, where he studies topics related to AI inference. Before Epoch, he worked at NVIDIA on LLM serving and inference optimization." Sole author; the commission's "authors" is singular. Estimates performance with Nvidia's AISimulate from per-chip dense FLOP/s by precision (BF16, FP8, FP4), HBM capacity, HBM bandwidth, one-way interconnect bandwidth per tier, and group size/latency. Estimates are "speed of light" (SOL), analytical optimum under modeled limits. Prefill and decode are modeled separately and enough prefill chips are provisioned to keep up; capacity is concurrent requests divided by all prefill plus decode chips. Workload: 262,144 cached tokens, 1,024 new tokens per prefill, about 1.51 new input tokens per output token, three accepted tokens per speculative decoding cycle. For each chip and model the highest concurrency at each required output speed from 50 to 400 tokens/s/req forms a curve; its area on a log speed axis (equal weight to 50-100, 100-200, 200-400) is divided by GB300's area for the same model; the IPI is the plain average of four ratios (GLM-5.2, Kimi K3, Qwen3-Coder-480B, an MAI-Base-2 proxy). Unit: GB300 equivalents (GB300e), GB300 NVL72 = 1. Scores given in text: GB300 NVL72 1; H200 HGX 0.12 ("roughly eightfold" lower); B300 HGX 0.54; GB300 NVL72 about 1.9× B300 HGX "highlighting the importance of its larger scale-up domain" (72 vs 8 GPUs); MI355X about 0.55; VR200 2.18. For Kimi K3 alone the model predicts "roughly a 46-fold GB300 advantage over H200, compared with eightfold across the full basket". Notes: scores are modeled potential, not software maturity; precision choices differ by accelerator and "We have not established that these choices preserve equivalent model quality"; acceptance length 3 is "a modeling assumption"; validation: GB300 Kimi K3 throughput "closely tracked predictions assuming 50% of modeled SOL performance, with an average absolute difference of about 12% across five frontier points". No table of scores; figures only.
Locators:    Opening paragraphs (25×, 2.5×, "a factor of ten"); "How we calculate the IPI"; "Combining the model comparisons" (formula, Figure 4); "Interpreting the IPI"; footnotes 1, 5, 6, 8, 9 under Notes.
Quote:       "We estimate that the Nvidia GB300 provides about 25× Nvidia H100's inference capacity per chip on the agentic inference workloads we model, with only 2.5× the 8-bit FLOP per second." / "Comparing FLOP/s alone would therefore underestimate GB300's inference capacity relative to H100 by a factor of ten." / footnote 8: "An arithmetic mean preserves a chip's contribution on models it serves well. A geometric mean penalizes uneven performance more strongly, substantially lowering Hopper's scores, but makes comparisons independent of the reference chip."

URL:         https://epoch.ai/data-insights/agentic-inference-capacity-growth
Kind:        primary (same author, Epoch AI) for the capacity series and its growth figures.
Establishes: firsthand: the 4.6× / 2.6× figures, 74% of added capacity, 73% of total, the assumptions behind chip-family mapping and the CSV.
Paraphrase:  Data Insight, 18 Nov 2026, "By Jason Li", title "Agentic inference capacity grew 4.6× in a year, versus 2.6× for compute capacity", CC BY. Capacity of chips sold to date, Q2 2025 to Q2 2026: inference 4.6×, peak 8-bit compute 2.6×. Method: cumulative chips sold in each category times its version 1 IPI score, summed across categories, divided by the Q2 2025 value; peak 8-bit compute computed for the same chips. Blackwell and Blackwell Ultra are 74% of added capacity and "roughly 73% of total agentic inference capacity, compared with 50% of total peak 8-bit computing power" by Q2 2026. Additions in Q2 2026 were 3.3× those in Q2 2025. Fitted growth of additions (log-linear regression): 3.2× inference and 2.1× compute per year over Q2 2025 to Q2 2026; 6.8× and 2.5× per year over Q1 2024 to Q2 2026 (doubling 4.3 and 9.2 months). 90% intervals 4.2 to 5.1× (inference) and 2.5 to 2.7× (compute); an earlier H200 transition lowers 4.6× to 4.5×. Intervals cover shipment and hardware-mix uncertainty only, not IPI model error (the page says "shipment and hardware-mix uncertainty"; it does not claim to cover model error). Assumptions: B200 shipments combined with GB200 and B300 with GB300; the GB share varied 30% to 90% (headline split 60% GB/NVL72, 40% HGX per the page's limits text); H100/H200 shipments split evenly from Q4 2024, earlier ones treated as H100; software efficiency not modeled. Inference capacity per unit of peak compute rose about 77%. Outlook: GB300 to VR200 is 2.2× per GPU against 8× from H200 to GB300.
Locators:    Opening paragraph; the data table and "Learn more about this graph"; sections Data, Analysis (Estimating capacity, Growth in additions, Uncertainty, Hardware-model co-design, Outlook).
Quote:       "On these workloads, inference capacity per unit of peak compute rose by about 77% over the year."

URL:         https://epoch.ai/data/charts/agentic-inference-capacity-growth/agentic_inference_capacity_by_chip_family_quarterly.csv
Kind:        primary: the dataset the Data Insight charts. Saved as `data/capacity.csv`.
Establishes: the full series (below under Numbers).
Paraphrase:  5 rows (Q2 2025 to Q2 2026), 35 columns. Column 0 `Quarter`. Columns 1 to 10: capacity by family as multiples of the Q2 2025 inference total (dimensionless). Column 11: total capacity, multiple of Q2 2025. Column 12: peak 8-bit compute, multiple of Q2 2025. Column 13: total capacity in GB300e. Column 14: total peak 8-bit compute in H100e. Columns 15 to 24: peak 8-bit compute by family in H100e. Columns 25 to 34: inference capacity by family in GB300e. The ten families, in file order: Nvidia Blackwell Ultra: B300 / GB300; Nvidia Blackwell: B200 / GB200; Nvidia Hopper: H100 / H200; Other Nvidia GPUs; Google TPU v8i; Google TPU v7; Earlier TPUs; AMD GPUs; Amazon Trainium; Other chips. Exact header strings are in `data/capacity.csv` line 1 (pattern `<family> (× Q2 2025 inference total)`, `<family> peak 8-bit compute (H100e)`, `<family> inference capacity (GB300e)`). Each quarter is a cumulative stock of chips sold to date, not a quarterly flow. Units: GB300e = GB300 NVL72 GPU equivalents under IPI v1; H100e = H100 equivalents of peak 8-bit FLOP/s (the page does not define the H100 value; my check below implies one H100e is one H100's dense FP8). Quarter-level sums of the family columns equal the total columns to 10 digits (my check). `data/capacity_by_family_long.csv` is the same data in long form (quarter, family, H100e, GB300e, GB300e per H100e) for `nb chart`.
Locators:    n/a (CSV). Downloaded 2026-11-21; HTTP 200, text/csv.

URL:         https://epoch.ai/data/ml_hardware.csv (Epoch Machine Learning Hardware database; documented at https://epoch.ai/data/machine-learning-hardware)
Kind:        primary for Epoch's recorded chip specifications and per-chip IPI; each row links the vendor datasheet it was taken from.
Establishes: dense FP8 FLOP/s, HBM capacity and bandwidth, intranode bandwidth and the IPI for 20 chips. Saved as `data/ml_hardware.csv` (183 rows, 39 columns, last column `Inference Performance Index (GB300e)`).
Paraphrase:  Rows I used (FP8 dense in FLOP/s, memory in bytes, bandwidth in byte/s; columns `FP8 performance (FLOP/s)`, `Memory (bytes)`, `Memory bandwidth (byte/s)`, `Intranode bandwidth (byte/s)`): H100 SXM5 80GB 1.979e15, 80e9, 3.35e12, 0.9e12, IPI 0.04. H200 SXM 1.979e15, 141e9, 4.8e12, 0.9e12, 0.123. B200 4.5e15, 180e9, 7.7e12, 1.8e12, 0.392. B300 4.5e15, 288e9, 7.75e12, 1.8e12, 0.541. GB200 5.0e15, 186e9, 8.0e12, 1.8e12, 0.9. GB300 5.0e15, 288e9, 8.0e12, 1.8e12, 1.0. MI355X 5.0332e15, 288e9, 8.0e12, 1.0752e12, 0.552. TPU v7 Ironwood 4.614e15, 192e9, 7.37e12, 1.2e12, 0.742. VR200 1.75e16, 288e9, 19.2e12, n/a, 2.177. 19 of the 20 scored chips have an FP8 value. `data/chip_fp8_vs_ipi.csv` joins FP8, HBM and IPI per chip (columns: hardware, fp8_dense_pflops, hbm_gb, hbm_bandwidth_tb_s, ipi_gb300e, ipi_per_fp8_pflops) for a scatter. Score precision here is three decimals.
Locators:    CSV columns as named; `Link to datasheet` column per row.

URL:         https://www.nvidia.com/en-us/data-center/h100/
Kind:        primary for H100's own specifications (Nvidia makes the chip, so it also has a stake in how it compares).
Establishes: H100 SXM FP8 Tensor Core "3,958 teraFLOPS" with the footnote "* With sparsity"; FP16 Tensor Core 1,979 teraFLOPS with sparsity; memory 80GB, 3.35TB/s; NVLink 900GB/s. Dense FP8 is therefore half of 3,958, 1,979 TFLOP/s, which matches Epoch's database.
Paraphrase:  Specification table, "H100 SXM" column.
Locators:    Specifications table and its "* With sparsity" footnote.

URL:         https://www.nvidia.com/en-us/data-center/gb300-nvl72/
Kind:        primary for GB300 NVL72's own specifications; vendor with a stake.
Establishes: system-level only (72 Blackwell Ultra GPUs, 36 Grace CPUs): FP8/FP6 Tensor Core "720 PFLOPS", FP16/BF16 "360 PFLOPS", FP4 "1440 | 1080" (second value footnoted "Without sparsity"), HBM about 20 TB, up to 576 TB/s, NVLink 130 TB/s. The page's footnote 1 reads "All Tensor Core specifications are with sparsity unless otherwise noted." Per GPU, FP8 sparse is 720/72 = 10 PFLOP/s, so dense 5 PFLOP/s, which matches Epoch's database (5.0e15). It also carries a vendor marketing claim: "up to a 50x overall increase in AI factory output performance compared to NVIDIA Hopper-based platforms", footnoted "DeepSeek-R1 ISL = 32K, OSL = 8K, GB300 NVL72 with FP4 Dynamo disaggregation. H100 with FP8 In-flight batching. Projected performance subject to change." The 50× is a product of 10× per-user responsiveness and 5× throughput per megawatt, not a per-chip ratio.
Locators:    Specifications table; footnotes 1 and 2; the "Performance Increase AI Factory Output Performance by 50x" caption.

URL:         https://github.com/jasonlizhengjian/inference-performance-index/blob/master/docs/METHODOLOGY.md (read as raw text, same path on raw.githubusercontent.com; the github.com HTML page returned 403 from my environment, the raw file is the same document)
Kind:        primary: the technical methodology behind the report, written by the index's author. The repository is under the author's personal GitHub account, not an Epoch organisation. Saved as `data/raw/..._METHODOLOGY.md`.
Establishes: exact equations, assumptions, the Rubin revision, and the four per-model ratios for VR200.
Paraphrase:  Snapshot "IPI v1 methodology, 20 October 2026 Rubin profile revision". Combined capacity B(s) = c / (1 + r·s·c/P), where c is decode requests per allocated chip, s required speed, P prefill throughput and r = 1.5133 new input tokens per output token. Area A = integral of B(s) ds/s over 50 to 400. IPI(h) = (1/4) Σ_m A(h,m)/A(GB300,m). For VR200 the four ratios are 1.224658, 2.476490, 2.354606, 2.653713; mean 2.177367. Catalog "requests fp8 for H100, H200 and TPU v7"; "Its other 20 profiles request nvfp4, sometimes as an FP4-equivalent modeling proxy". Assumed 3 accepted tokens per cycle; "The index applies no universal 50% achieved-performance discount." The trace behind the 1.51 ratio is 110,565 Claude warm-cache coding requests, "not redistributed". Evidence statement: reproduction shows consistency, "not physical accuracy"; the index has no confidence interval; scores need comparing within one snapshot.
Locators:    Sections 1 to 5, "Workload and model assumptions" table, "What the evidence supports".

URL:         https://github.com/jasonlizhengjian/inference-performance-index/blob/master/docs/research/methodology-sensitivity/README.md (and the CSVs beside it; read through raw.githubusercontent.com)
Kind:        primary: the author's own sensitivity study. Saved with `data/ipi_sens_score_matrix.csv`, `ipi_sens_per_model_sensitivity.csv`, `ipi_sens_scenario_results.csv`, `ipi_sens_robustness.csv`, `ipi_sens_family_robustness.csv`, `ipi_sens_provenance.json`.
Establishes: per-chip scores for 23 accelerators under 28 scenarios, including each model alone. Columns of `ipi_sens_score_matrix.csv`: `hardware`, `log_50_400` (headline IPI), other bands and weightings, `only_0` to `only_3` (one model alone: 0 GLM-5.2, 1 Kimi K3, 2 Qwen3-Coder 480B, 3 MAI proxy; confirmed because the mean of the four equals `log_50_400` for every chip, to 1e-9), `without_0` to `without_3`, `glm_kimi`, `proxy_*`, `decode_only`, `half_input`, `double_input`, `point_50/100/200/400`.
Paraphrase:  This is where the per-model component scores live. Same frozen 15 Oct release as the report plus the revised Rubin inputs, "re-integrates the same frozen 23-accelerator, four-model release". For VR200, log 50-400 gives 2.177, linear on the same band 2.425; GLM+Kimi basket 1.851; per-model range 1.225 to 2.654, which the study says is "why a basket score should not be presented as an architecture-independent hardware multiplier". Robustness ranges are "not confidence intervals or probabilities". Score table (their three-decimal table): H100 SXM FP8 0.040, H200 0.123, B200 0.392, B300 0.541, GB200 NVL72 0.900, GB300 NVL72 1.000, MI355X 0.552, TPU7x Ironwood FP8 0.742, VR200 2.177.
Locators:    "Linear versus logarithmic weighting" table; "Model-basket sensitivity" table; CSVs.

URL:         https://github.com/jasonlizhengjian/inference-performance-index/blob/master/docs/research/inferencex-validation/README.md (read through raw.githubusercontent.com)
Kind:        primary for what the author's validation did and did not show; the author tests his own model.
Establishes: the 12% figure is narrow.
Paraphrase:  Benchmark observations 19 Oct 2026. Kimi K3 on GB300: 11.6% mean absolute throughput difference at five frontier points in 50-400 tokens/s/user with decode and prefill at 50% of modeled SOL; "not a universal 12% error bar on the index". Same points with both phases at undiscounted SOL: 256.3%. All 11 frontier points over the full 31-680 range: 31.1%. Other hardware and model combinations in the same band and scenario: Kimi/GB200 202.5%, Kimi/B300 82.2%, Kimi/MI355X 40.0%, GLM/GB300 165.5%, GLM/MI355X 344.0%. The table lists no H100 or H200 row. "Neither comparison establishes an error bound on cross-hardware index ratios."
Locators:    "What the comparison establishes"; the five-point table; "How sensitive is this description of agreement?"; "Other hardware and model checks".

URL:         https://epoch.ai/data/machine-learning-hardware-documentation/methodology (Machine learning hardware documentation, "Inference Performance Index, Version 1")
Kind:        primary (Epoch's own documentation of the index).
Establishes: confirms that the published index uses "the arithmetic mean of the four ratios", equal weights, and states "The advantage varies by model and speed"; "We also report individual model scores"; "We apply no software-efficiency discount."
Paraphrase:  Summary page of the same method; says the 1.51 ratio comes from "about 111,000 selected requests from TraceLab's Claude Code subset"; "The range and weighting are benchmark choices."
Locators:    Section "Inference Performance Index" and "Key choices and why".

URL:         https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs (also at https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)
Kind:        primary for SemiAnalysis's own benchmark results (InferenceX v2, 16 Feb 2026, by Dylan Patel, Cam Quilici, Bryan Shan and 4 others; paid post, the part I read is the public excerpt). Independent of Epoch and of Nvidia, though Nvidia supplied hardware access (the post thanks Jensen Huang and Ian Buck). Secondary only for any claim about how the numbers were produced beyond what the page prints.
Establishes: measured ratios against an H100 baseline on large mixture-of-experts serving (DeepSeek R1 8k/1k in the sections I read).
Paraphrase:  GB300 NVL72 "achieves up to 100x on FP8 vs FP4 compared to even a strong H100 disagg+wideEP+MTP baseline and 65x on FP8 vs FP8. On H100 vs GB200 NVL72, we see up to 55x realized performance difference at 75 tok/s/user." Another passage: at 116 tokens/s/user, "up to 98x better perf on GB200 NVL72 FP4 and up to 100x better perf on GB300 NVL72 FP4" than "a strong H100 disagg+wideEP FP8 baseline"; tokens per dollar, 9.7× at 40 tok/s/user up to 65× at 116. The 100x vs 65x pair is a direct measure of the precision effect on the GB300 side (FP4 against FP8): about 1.5× of the ratio. It also says GB300 NVL72's 72-GPU NVLink domain gives "over 9x higher bandwidth" than multi-node B300 servers that fall back to 800 Gbit/s scale-out.
Locators:    Key Observations and Results; "Jensen Under Promising and Overdelivering"; B300 vs GB300 bandwidth paragraphs.

URL:         https://inferencex.semianalysis.com/compare/deepseek-r1-gb300-vs-h100
Kind:        primary for SemiAnalysis InferenceX results (their site); data interpolated from benchmark runs. Page schema says published 2026-02-03, modified 2026-06-17. Caveat: the page I fetched shows the banner "Unofficial deployment. This copy of InferenceX is not affiliated with or endorsed by SemiAnalysis. Its Data may be modified or out of date." The same banner appears on the Kimi K3 page that Epoch's report links to. I could not establish whether the banner reflects a mirror or a hostname check, so treat the numbers as indicative and prefer the newsletter above for anything quoted.
Establishes: GB300 NVL72 vs H100 on DeepSeek R1, 8k input / 1k output, FP8 for both, per-chip throughput at three interactivity targets.
Paraphrase:  45 tok/s/user: GB300 NVL72 8,703 vs H100 739 tok/s/chip (page text "12×"; my arithmetic 11.8×). 71 tok/s/user: 7,167 vs 281 (page "26×"; my arithmetic 25.5×). 97 tok/s/user: 5,528 vs 154 (page "36×"; my arithmetic 35.9×). Concurrency at those points: about 1,229 vs 132, 732 vs 41, 437 vs 17. Same site's Qwen 3.5 397B-A17B GB300 vs H100 page has no H100 data.
Locators:    Summary sentences at the top and the table "Throughput (tok/s/chip)".

URL:         https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0
Kind:        secondary for MLPerf (Nvidia reports its own submissions; the primary is MLCommons' results table, which I did not open). Vendor with a stake.
Establishes: short-context, fixed-latency ratios, H200 not H100: 8x B200 vs 8x H200 on Llama 2 70B, server 98,443 vs 33,072 tokens/s (3.0×), offline 98,858 vs 34,988 (2.8×); GB200 NVL72 vs H200 on Llama 3.1 405B "up to 3.4x higher per-GPU performance" (server), 2.8× offline. Per-GPU is "derived by dividing reported throughput by accelerator count", entries 5.0-0058 and 5.0-0060.
Paraphrase:  MLPerf Inference v5.0 (April 2025). No H100 comparison. Gives a contrast: ratios of about 3× per GPU at short context and a fixed latency target, against Epoch's modeled 8× (H200) at 262k context.
Locators:    Figure 1 caption, Table 1, footnotes.

## Contradictions

- Commission: "25 times on about 2.5 times its 8-bit FLOP/s". Confirmed by the primary, with one qualification: the 25× is an arithmetic mean. Per model, GB300/H100 is 43.5× (GLM-5.2), 166.7× (Kimi K3), 8.0× (Qwen3-Coder), 200× (MAI proxy) (my arithmetic from `only_0` to `only_3`: 0.02262, 0.00630, 0.12520, 0.00460). Geometric mean of H100's four scores is 0.0169, so 59.1×; H200: arithmetic 0.1228 (8.1×), geometric 0.0574 (17.4×). Epoch's footnote 8 concedes the geometric mean "substantially" lowers Hopper's scores. The commission's wording that the report "says an arithmetic mean flatters some chips relative to a geometric mean" is slightly off: the report says arithmetic preserves strength on models a chip serves well. Across the 23 chips the GM/AM ratio is 0.43 for H100, 0.47 for H200, 0.81 for B200, 0.90 for B300 and MI355X, 0.96 to 1.00 for most others (`data/ipi_arith_vs_geo.csv`). So the arithmetic mean favours chips with one strong model, which here is mostly Hopper and B200/B300 relative to GB300. Under the geometric mean the ordering of chips is unchanged where I checked; the ratios to H100 are what move.
- Sensitivity range of the headline: GB300/H100 across the author's 28 scenarios runs from 19.5× (without MAI proxy) to 270.9× (capacity at a single 400 tok/s/user point, where H100 scores 0.0037); excluding the single-point scenarios, 19.5× (proxy 0%/leave-out-MAI) to 89.5× (Qwen left out) (my arithmetic from `ipi_sens_score_matrix.csv`). The headline sits near the low end.
- The report's Figure 1 alt text says "up to 72×" for newer chips over H100. Text says 25× for GB300. 72× is consistent with MI455X (2.893 / 0.0397 = 72.9× in the database's rounding 2.893/0.040 = 72.3×), not with a GB300 claim. The frozen sensitivity release scores Meta MTIA 500 (512 GB) at 3.198, 80.6× an H100, and that chip is not in the public database. I could not open the figure's data to say which chips it includes.
- Data Insight: "74% of added capacity" and "roughly 73% of total" are two quantities, and both reproduce (74.4% of added GB300e between Q2 2025 and Q2 2026; 72.9% of the Q2 2026 stock). Not a contradiction. The Data Insight credits the Hopper-to-Blackwell transition; the CSV also shows Google TPU v7 at 17.4% of added capacity (904,954 of 5,210,967 GB300e), against Blackwell B200/GB200 at 17.8%.
- The Data Insight gives 3.2×/2.1× fitted growth over five quarters. The CSV starts at Q2 2025 and carries stocks only, so additions for Q2 2025 are not recoverable; a four-quarter fit of Q3 2025 to Q2 2026 additions gives 2.90× (inference) and 1.99× (compute); adding an implied Q2 2025 addition (1,858,660 / 3.3 = 563,230) gives 3.22×. Consistent with the 3.2×, but the 3.3× itself is not checkable from the files.
- Independent measurement vs Epoch's modeled ratio: InferenceX DeepSeek R1 8k/1k FP8 gives GB300/H100 of 11.8×, 25.5× and 35.9× at 45, 71 and 97 tok/s/user, and SemiAnalysis's newsletter gives up to 65× (FP8 vs FP8) and 100× (GB300 FP4 vs H100 FP8) at 116 tok/s/user. Epoch's 25× is within that range, but the benchmark is 8k/1k context, a different model basket, and a ratio that moves by 3× across interactivity targets. It neither confirms nor contradicts Epoch's number; it shows the interactivity target and precision choice move the ratio by more than the gap between 25× and 2.5×. MLPerf (Nvidia-reported) gives about 3× per GPU for B200 or GB200 over H200 at short context, against Epoch's 8× (GB300 over H200) at 262k; different regime.
- Nvidia's own "50x" for GB300 NVL72 over Hopper (DeepSeek-R1, 32K/8K, FP4 vs FP8) is output per megawatt and per user combined; it is not a per-chip ratio and does not compare with 25×.

## Numbers

Figure: GB300 NVL72 IPI relative to H100 SXM, 25.2× (IPI 0.0397 for H100; headline text rounds to 25×). Arithmetic: 1 / 0.039682 = 25.2.
Owner:  Epoch AI MLH database and the author's score matrix; the report's text gives 25×.
Scope:  IPI v1, four-model arithmetic mean, log speed axis 50 to 400 tokens/s/req, 262,144-token cached context, SOL with no software discount; per chip (GB300 NVL72, 72-GPU domain; H100 SXM 80GB in what the catalog calls an FP8, 400G scale-out profile).

Figure: GB300 FP8 dense FLOP/s over H100 SXM, 2.53×. Arithmetic: 5.0e15 / 1.979e15 = 2.5265. Vendor check: 720 PFLOP/s sparse / 72 GPUs = 10 PFLOP/s sparse = 5 PFLOP/s dense; H100 3,958 TFLOP/s sparse = 1,979 dense.
Owner:  Nvidia GB300 NVL72 and H100 product pages; Epoch database repeats both values.
Scope:  dense (no sparsity), 8-bit floating point, per GPU.

Figure: the report's "factor of ten": 25.2 / 2.53 = 9.97.
Owner:  Epoch report (derived by me from its own two numbers).
Scope:  as above.

Figure: other per-GPU ratios GB300 over H100 (Epoch database): HBM bandwidth 8.0 / 3.35 = 2.39×; HBM capacity 288 / 80 = 3.6×; NVLink per GPU 1.8 / 0.9 = 2.0×; BF16 dense same as FP8 ratio, 2.53×. H100 has no FP4. Every one of these is between 2× and 3.6×.
Owner:  Epoch MLH database, each row citing the vendor datasheet.
Scope:  per GPU, dense, H100 SXM5 80GB vs GB300.

Figure: two-step decomposition of 25.2× from Epoch's own scores (my arithmetic, not presented by Epoch). H100 to B300 HGX, an eight-GPU node: 0.5407 / 0.0397 = 13.6×, on FP8 2.27× (4.5/1.979), HBM bandwidth 2.31× (7.75/3.35) and HBM capacity 3.6×. B300 HGX to GB300 NVL72, same GPU, 72-GPU rather than 8-GPU domain: 1 / 0.5407 = 1.85× (Epoch text "about 1.9×"). 13.6 × 1.85 = 25.2. H100 to B200 HGX: 0.3919 / 0.0397 = 9.9×, on FP8 2.27×, bandwidth 2.30×, capacity 2.25×.
Owner:  `data/ipi_sens_score_matrix.csv` (author's scores) and `data/ml_hardware.csv`.
Scope:  IPI v1; the report does not attribute the 13.6× to causes. Part of it is the format modeled: H100 uses FP8 experts, the other 20 profiles use nvfp4 or an FP4 proxy, and SemiAnalysis measured about 1.5× of FP4 benefit on GB300 (100× vs 65×).

Figure: H100 and H200 component scores (GB300 = 1 under each model), model order GLM-5.2, Kimi K3, Qwen3-Coder 480B, MAI proxy: H100 0.02262, 0.00630, 0.12520, 0.00460 (mean 0.03968, geometric 0.01690); H200 0.08589, 0.02175, 0.36777, 0.01584 (mean 0.12281, geometric 0.05744). Qwen's share of the sum: H100 78.9% (0.12520 / 0.15872), H200 74.9%. Full table for 23 chips with arithmetic and geometric means and the GB300-over-chip ratios: `data/ipi_arith_vs_geo.csv` (columns: hardware, glm_5_2, kimi_k3, qwen3_coder_480b, mai_base_2_proxy, ipi_arithmetic_gb300e, geometric_mean_gb300e, gb300_over_chip_arithmetic, gb300_over_chip_geometric).
Owner:  author's repository, `docs/research/methodology-sensitivity/score_matrix.csv` (here `data/ipi_sens_score_matrix.csv`, columns `only_0` to `only_3`).
Scope:  frozen 15 Oct release with 29 Oct Rubin refresh; per-model area under the 50 to 400 tokens/s/req curve relative to GB300 NVL72 for that model.

Figure: other chips' scores (headline, then four components): B200 HGX 0.3919 (0.386, 0.194, 0.819, 0.169); B300 HGX 0.5407 (0.711, 0.371, 0.826, 0.255); GB200 NVL72 0.8996 (0.678, 0.972, 1.000, 0.950); TPU7x Ironwood 0.7415 (0.646, 0.771, 0.888, 0.661); MI355X 0.5525 (0.707, 0.382, 0.858, 0.263); VR200 2.1774 (1.225, 2.476, 2.355, 2.654). H100 GB300-relative single-speed scores at 50, 100, 200, 400 tokens/s/req: 0.048, 0.0396, 0.0457, 0.0037.
Owner:  as above.
Scope:  as above.

Figure: capacity series, Q2 2025 to Q2 2026 (chips sold to date). Total agentic inference capacity in GB300e: 1,454,225; 2,269,165; 3,416,362; 4,806,533; 6,665,192. Multiples of Q2 2025: 1.000; 1.560; 2.349; 3.305; 4.583. Total peak 8-bit compute in H100e: 12,203,971; 15,913,967; 20,331,360; 25,321,969; 31,654,723. Multiples: 1.000; 1.304; 1.666; 2.075; 2.594. Inference capacity per H100e of compute (GB300e / H100e): 0.1192; 0.1426; 0.1680; 0.1898; 0.2106.
Owner:  `capacity.csv`, Epoch AI chip-family series behind the Data Insight.
Scope:  cumulative chips sold to date at each quarter; IPI v1 scores held fixed across quarters; Epoch's AI Chip Sales shipment estimates with the B/GB and H100/H200 splits stated above.

Figure: growth recomputed. Inference 6,665,192 / 1,454,225 = 4.583×; compute 31,654,723 / 12,203,971 = 2.594×; the ratio of the two is 4.583 / 2.594 = 1.767, the Data Insight's "about 77%" (0.2106 / 0.1192 = 1.767).
Owner:  Epoch Data Insight; reproduced from the CSV.
Scope:  Q2 2025 to Q2 2026.

Figure: composition of the capacity series, Q2 2025 and Q2 2026 (my arithmetic). Blackwell Ultra B300/GB300 share of peak compute 4.46% then 30.55%; Blackwell B200/GB200 23.91% then 19.87%; Hopper 34.14% then 13.70%; Google TPU v7 0% then 8.99%; earlier TPUs 16.52% then 10.31%. Blackwell (both families) share of capacity: 67.4%, 73.3%, 75.0%, 75.2%, 72.9% across the five quarters; of peak compute: 28.4%, 35.8%, 42.5%, 47.5%, 50.4%.
Owner:  `capacity.csv`.
Scope:  shares of the cumulative stock.

Figure: scores per H100e of peak compute (capacity GB300e / compute H100e) by family, constant across all five quarters: Blackwell Ultra 0.3231, Blackwell 0.2757, TPU v7 0.3180, Other Nvidia 0.0397, earlier TPUs 0.0397. They vary only where the family mixes chips: Hopper 0.0520 to 0.0532, AMD 0.0397 to 0.0815, Trainium 0.1707 to 0.1917, TPU v8i 0.1787 at its one quarter. Consequence: per-chip scores are fixed, so the gap between 4.58× and 2.59× is composition.
Owner:  derived from `capacity.csv`, `data/capacity_by_family_long.csv` (column `gb300e_per_h100e`).
Scope:  family level.

Figure: decomposition of the rise in capacity per H100e, 0.11916 to 0.21056 (+0.09140), by midpoint split (change in compute share × mean family score, plus mean share × change in family score). A family absent in Q2 2025 (TPU v7, v8i) enters at its own score, so its effect counts as mix. Mix-shift part 0.08697 (95.1%); within-family score drift 0.00443 (4.9%). Mix terms by family: Blackwell Ultra +0.08431; TPU v7 +0.02859; TPU v8i +0.00074; Blackwell B200/GB200 −0.01114; Hopper −0.01075; earlier TPUs −0.00246; Other Nvidia −0.00135; AMD −0.00074; Trainium −0.00019. Score-drift terms: AMD +0.00254, Trainium +0.00103, other chips +0.00059, Hopper +0.00027. Counterfactual: hold every family at its Q2 2025 per-H100e score (new families at their own score), apply the Q2 2026 compute mix, and capacity growth is 4.495× instead of 4.583×.
Owner:  my arithmetic on `capacity.csv`; `data/recompute.py` reproduces it. The split depends on the midpoint convention but the sign and size do not: no choice makes within-family drift more than a few percent.
Scope:  Q2 2025 to Q2 2026 stocks.

Figure: added capacity by family over the year, 5,210,967 GB300e total: Blackwell Ultra 2,948,799 (56.6%); Blackwell 929,355 (17.8%); TPU v7 904,954 (17.4%); Trainium 190,586 (3.7%); AMD 108,745 (2.1%); earlier TPUs 49,561 (1.0%); other chips 41,654 (0.8%); TPU v8i 23,395 (0.4%); Hopper 13,816 (0.3%); Other Nvidia 102 (0.0%). Blackwell and Blackwell Ultra together 74.4%. Of added peak compute (19,450,753 H100e) they are 64.3%.
Owner:  `capacity.csv`.
Scope:  difference of the two cumulative stocks.

Figure: quarterly additions in GB300e: Q3 2025 814,939; Q4 2025 1,147,197; Q1 2026 1,390,171; Q2 2026 1,858,660. In H100e: 3,709,996; 4,417,393; 4,990,609; 6,332,754. Blackwell and Blackwell Ultra share of additions: 83.8%, 78.3%, 75.7%, 67.0%.
Owner:  `capacity.csv`.
Scope:  differences between consecutive quarters.

Figure: sensitivity to the averaging choice, applied to the series (my approximation, flagged). Scaling the Nvidia family scores to their geometric-mean values (Blackwell Ultra ×0.973 and Blackwell ×0.949 using the 60/40 GB/HGX mix, Hopper ×0.44 at an H200 share near 15%, TPU v7 ×0.99) and holding other families at the arithmetic scores moves capacity growth from 4.58× to about 4.99×. A geometric mean lowers Hopper's weight in the Q2 2025 base, so growth rises.
Owner:  my arithmetic; assumptions inferred from the CSV and the scores above, not Epoch's.
Scope:  indicative only. Epoch does not publish a geometric-mean series; family-to-chip mappings for AMD, Trainium and "other" are not public in what I read, so those are unchanged.

Figure: IPI against FP8 FLOP/s across Epoch's scored chips. 19 chips with both values; log-log Pearson correlation of IPI with FP8 dense FLOP/s is 0.79, with HBM bandwidth 0.89 (n = 18). IPI per PFLOP/s of FP8 runs from 0.020 (H100) to 0.380 across chips, a spread of 18.8×.
Owner:  my arithmetic on `data/chip_fp8_vs_ipi.csv` (script `data/recompute.py`).
Scope:  small sample, collinear specs, one index version; FLOP/s tracks the index across chips, so "FLOP/s is uncorrelated" would be wrong; the correct statement is that it fails to predict the ratio between generations.

Figure: independent benchmark ratios. InferenceX, DeepSeek R1, 8k input / 1k output, FP8 both sides, per chip: 8,703 / 739 = 11.8× at 45 tok/s/user; 7,167 / 281 = 25.5× at 71; 5,528 / 154 = 35.9× at 97. SemiAnalysis newsletter (16 Feb 2026): up to 55× GB200 NVL72 over H100 at 75 tok/s/user; up to 100× GB300 NVL72 (FP4) over H100 (FP8) and 65× FP8 vs FP8, at 116 tok/s/user. MLPerf v5.0 per Nvidia: B200 8-GPU over H200 8-GPU on Llama 2 70B 3.0× (server) and 2.8× (offline); GB200 NVL72 over H200 on Llama 3.1 405B 3.4× per GPU (server).
Owner:  SemiAnalysis for InferenceX; MLCommons results for MLPerf, reported by Nvidia.
Scope:  as stated in each; none uses a 262,144-token cached context. The "up to" language means the maximum over the benchmark's points, not a single operating point.

Figure: Epoch's validation. 11.6% mean absolute throughput difference, five Kimi K3 GB300 frontier points between 60.5 and 387.6 tok/s/user, both phases at 50% of SOL; 256.3% at undiscounted SOL; Kimi/GB200 202.5%, Kimi/B300 82.2%, GLM/GB300 165.5%.
Owner:  `docs/research/inferencex-validation/README.md` in the author's repository.
Scope:  one model on one chip is the only close agreement; no H100 or H200 row.

## Limits

- No independent measurement of H100 against GB300 at a 262,144-token cached context exists in what I could open. InferenceX's Qwen 3.5 page has no H100 data and the Kimi K3 page that Epoch links plots H200, not H100. The only H100 ratios I have are 8k/1k DeepSeek R1 (InferenceX) and Nvidia's.
- The IPI is a no-software-discount speed-of-light model. Its only measurement check is five Kimi K3 points on GB300; across other model and chip pairs the author's own table shows gaps from 40% to 344%. No evidence in what I read that the H100 ratio has been checked against any measurement. The score does not model software maturity; Epoch says InferenceX "attributes part of Hopper's weak Kimi K3 performance" to missing optimizations (the report text, linking SemiAnalysis's Kimi K3 AgentX post, which I did not open).
- The report has no per-chip score table. The per-model scores come from the author's repository (frozen release; the Rubin revision changes only VR200). Headline scores match the report's text to its displayed precision (H200 0.12, B300 0.54, MI355X about 0.55, VR200 2.18).
- The split of Blackwell shipments into 60% GB/NVL72 and 40% HGX and the H100/H200 split are the author's judgment. I recovered 60/40 independently only as a consistency check: with 60/40 weights both Blackwell families come to 2.527 H100e per chip (0.8164 / 0.3231 and 0.6968 / 0.2757), i.e. 5.0 PFLOP/s dense FP8 per chip. Epoch's database lists B200 and B300 at 4.5 PFLOP/s, so the series appears to treat HGX chips at 5.0, about 10% high for those chips. I infer this; Epoch does not state it. The effect on the 2.6× compute growth is not quantified.
- I did not open Epoch's AI Chip Sales dataset, so shipment counts are not independently checked. The Q2 2025 additions, the 3.3× additions figure and the 3.2× / 2.1× regression cannot be reproduced from the CSV (stocks only; no Q1 2025 row).
- The 90% intervals of 4.2 to 5.1× cover shipment and mix uncertainty only; the Data Insight lists no uncertainty for IPI error, and the methodology gives no confidence interval for scores.
- The report does not attribute the 25× to memory bandwidth, memory capacity, the 72-GPU domain or FP4. I can show the two-step split (13.6× chip generation in an 8-GPU node, 1.85× from the 72-GPU domain) and the SemiAnalysis FP4 effect (about 1.5×), and the per-GPU spec ratios (all 2× to 3.6×), but no ablation of bandwidth against capacity against format exists in what I read. The writer must not assign a share to bandwidth.
- Nvidia's GB300 NVL72 page labels FP4 "1440 | 1080²" without column headings; I used the Epoch database's 15 PFLOP/s per GPU (1.5e16) for FP4 dense and did not open the Blackwell Ultra datasheet. B200 and B300 dense FP8 (4.5 PFLOP/s) come from Epoch's database, whose rows cite the datasheets; I did not open those datasheets.
- The MLPerf figures are Nvidia's account of MLCommons entries; I did not open the MLCommons table. No MLPerf v6.x H100 comparison was found.
- The InferenceX compare page I fetched carries an "Unofficial deployment" banner (see source entry); its three ratios are indicative.
- The report says IPI v1 scores change if the basket changes, so any number in the article should say "IPI version 1".
- The headline ratio "about 25×" is reproduced; what I could not establish is a reason in the primaries why the model should be read as 25× rather than a range of 8× to 200×. Epoch says the advantage "varies by model and speed" and names the arithmetic mean's choice in footnote 8.

## Source assets

Asset: Figure 1 of the report, horizontal bar chart of IPI per chip normalised to GB300 = 1, `https://epoch.ai/assets/images/posts/2026/inference-performance-index/figure-1.png` (anchor `#figure-1` on the report page).
Shows: the ranking of chips by modeled capacity, with H100 and H200 at the bottom and "up to 72×" spread over H100.
Crop:  keep the full bar set with chip labels and the GB300 = 1 reference; omit the page chrome. The chart is on a linear axis, so small bars are unreadable; the writer may prefer `nb chart` from `data/chip_fp8_vs_ipi.csv`.

Asset: Figure 2, line chart of Kimi K3 decode on GB300, concurrency (requests per chip) falling against output speed on a log axis from 50 to 400 tokens/s/req, `.../figure-2.png` (`#figure-2`).
Shows: the concurrency against speed trade-off that the index integrates; the 2 vs 8 requests per chip example (about 210 vs 80 tokens/s/req, 420 vs 640 tokens/s/chip).
Crop:  keep both axes and the two annotated points; omit the caption text that restates the arithmetic.

Asset: Figure 3, line chart of GB300 and VR200 capacity curves on Kimi K3 over 50 to 400 tokens/s/req, with the area ratio equation (about 2.48) beneath it, `.../figure-3.png` (`#figure-3`).
Shows: that the index is an area ratio and that VR200's advantage varies by speed.
Crop:  keep both curves and the axis labels; the equation is HTML/MathJax text on the page, not part of the image.

Asset: Figure 4, bar chart of VR200 against GB300 for four models, about 1.2× to 2.65×, average 2.18, `.../figure-4.png` (`#figure-4`).
Shows: the averaging step and how far one model can sit from the mean. The score for H100 would show the same step more sharply (8× to 200× per model); that is a chart for `nb chart` from `data/ipi_arith_vs_geo.csv`.
Crop:  keep the four model labels and the average marker.

Asset: Figure 5 of the report, SemiAnalysis InferenceX Kimi K3 2.8T throughput per chip against P90 interactivity, Vera Rubin NVL72, GB300 NVL72, B300, MI355X, H200; credited "From SemiAnalysis", `.../figure-5-inferencex-kimi-k3.png` (`#figure-5`).
Shows: measured ordering with H200 far behind; useful as an independent measurement next to the model.
Crop:  keep the legend and the credit line; redistribution rests on SemiAnalysis and Epoch's permission, which I did not check.

Asset: Data Insight stacked bar chart of capacity by chip family with lines for total capacity and peak compute, `https://epoch.ai/assets/images/data-insights/agentic-inference-capacity-growth/agentic-inference-capacity-growth.png`.
Shows: the 4.6× and 2.6× lines against the family stacks.
Crop:  keep the two lines and the family legend. The series is in `data/capacity.csv`; a redrawn chart can add the compute-share composition that this image does not show.

Asset: the SemiAnalysis newsletter charts for the 98× to 100× result at 116 tok/s/user.
Shows: not captured; I read the text only.
Crop:  none; paid post.

## Discarded

https://userecurrence.ai/research/is-hosting-open-source-inference-profitable: seen as a search result only, not opened; a third party's H200 vs B300 vs GB300 economics piece, not a primary on any figure needed.
https://www.siliconreport.com/best-ai-chips-ranked-inference-2026-4cfa6181: seen as a search result only; aggregator whose 288-GPU GB300 totals (1.55, 2.49 and 2.5 million tokens/s) disagree with one another.
https://www.storagereview.com/news/nvidia-sets-mlperf-inference-v6-0-records-with-blackwell-ultra-platform: seen as a search result only; repeats Nvidia's GB300 per-GPU MLPerf v6.0 numbers (DeepSeek-R1 server 8,064 tokens/s/GPU) with no H100 or B200 baseline.
https://nebius.com/blog/posts/mlperf-inference-v6-0-results: seen as a search result only; vendor report of its own submissions, no H100 comparison.
https://inferencex.semianalysis.com/compare/qwen-3-5-gb300-vs-h100: read, rejected for the comparison: the page has GB300 NVL72 figures and no H100 data at any of its three operating points.
https://inferencex.semianalysis.com/inference/kimi-k3: read only to confirm it is an interactive dashboard with the "Unofficial deployment" banner; it gives no extractable H100 numbers.
https://inferencex.com/compare/deepseek-r1-gb300-vs-h100: returned 404.
https://api.github.com/repos/jasonlizhengjian/inference-performance-index/git/trees/master and https://github.com/jasonlizhengjian/inference-performance-index: refused in this environment (403, repository access not enabled for this session); the same files were read through raw.githubusercontent.com, so the article should link github.com paths as the Epoch report does.
