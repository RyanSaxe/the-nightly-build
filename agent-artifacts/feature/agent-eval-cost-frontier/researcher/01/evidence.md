# Evidence record: feature/agent-eval-cost-frontier (researcher 01)

Retrieved 2026-10-31. Every figure below was read in the document named as its owner on that date.

The evidence supports a real chart. Ai2 publishes a per-agent overall score and an overall cost per problem in USD for 24 test-set agents on the AstaBench leaderboard (23 of them with full 4/4 category coverage), and the same leaderboard marks an 11-agent Pareto frontier that I reproduced independently from its own numbers. I also rebuilt the score and cost for 10 of the 24 rows from Ai2's raw per-run result files, and they match to the displayed precision. The accuracy ranking and the score-per-dollar ranking are very different orderings of those 23 agents (the top agent by accuracy is 21st of 23 by score per dollar). The evidence is thin or works against the commission in five places. (1) Cost is logged model token usage multiplied by prices from a frozen snapshot of a community price table. Tool calls are not priced, and the costs are not billed amounts, so two sentences in the commission and the required diagram need rewording. (2) Every costed row was submitted by Ai2, and 10 of the 11 frontier points are one Ai2 baseline scaffold (ReAct) with the language model swapped, so the frontier is a model-choice frontier. (3) The agent at the top of the accuracy column is itself on the frontier, as it must be, so "often not the one you would deploy" is a budget judgment the data cannot make for a reader. (4) The paper's Table 4 and the live leaderboard give different numbers for the same named agents. (5) The leaderboard's overall chart shows no error bars, and the score differences between the top agents are about the size of a 95% interval. The AstaBrief post gives latency and no dollar cost.

## Sources

URL:         https://arxiv.org/abs/2510.21652 (PDF read: https://arxiv.org/pdf/2510.21652, version v2, 21 Apr 2026)
Kind:        primary. Authored by the Ai2 Asta team (Bragg, D'Arcy et al., 39 authors, Allen Institute for AI and co-affiliations). It owns the benchmark design, the cost method and the paper-era results. Published at ICLR 2026.
Establishes: firsthand: what AstaBench contains, the tool environment, how cost is computed, the 57-agent evaluation, Tables 4 and 11 with per-agent overall score and cost, Figure 2 with the Pareto frontier.
Paraphrase:  AstaBench is 11 benchmarks in four categories (Literature Understanding, Code & Execution, Data Analysis, End-to-End Discovery), 2,404 problems by the Table 2 counts (1,918 test, 486 validation), run inside the Asta Environment. The environment supplies the same tools to every agent: the Asta Scientific Corpus (literature search served over MCP, restricted to papers before a per-task date cutoff so new papers cannot leak in) and a stateful Jupyter Computational Notebook sandbox. Inspect logs which models each agent called and how many tokens they used. The agent-eval toolkit turns those logged usages into dollars using a frozen snapshot of the litellm community cost map, with cache discounts applied and with no service-tier or batching discounts. Open-weight models served by Together AI are priced from Together's size-based pricing. The paper evaluated 57 agents of 22 classes and reports the score and cost of each, with a Pareto frontier in Appendix D. Its stated reason for reporting cost: simple strategies such as repeated runs with majority vote raise accuracy by spending more.
Locators:    Abstract; Section 1 (p. 2, bullets and footnote 4); Figure 1 (p. 3); Table 2 (p. 6); Section 4.1 (pp. 5-6); Section 4.2 "Time-invariant cost calculation" (pp. 6-7) with footnotes 9 and 10; Section 5 (pp. 7-9); Figure 2 (p. 8); Appendix A principle 3 (p. 16); Appendix B (p. 17); Table 4 (p. 18); Tables 5-10 (pp. 18-20); Table 11 (p. 21); Appendix D statistical methodology (p. 21); Table 22 (p. 54).
Quote:       Section 4.2, p. 6: "Inspect logs only model usages (not normalized dollar amounts)". Same section: "For mapping model usages to prices, we use a frozen snapshot of the litellm cost map, which is community-sourced for broad model coverage." p. 7: "it does not factor in any latency-related discounts (e.g., service tier or batching). Using a frozen snapshot allows a fair comparison of evaluation costs even if API prices change between evaluations." Footnote 10, p. 7: "The cost map snapshot used for the leaderboard may be periodically updated, but we will always re-calculate all costs based on the current snapshot to ensure fair comparison." Section 5, p. 9: "The best economical model is ReAct with gpt-5-mini, scoring 32%—within 21% (absolute) of the best performing models—while costing over an order of magnitude less at $0.04 per problem." Section 5, p. 7: Asta v0 "scores ∼9% higher than the next best agent, ReAct with gpt-5 (53.0% vs. 44.0%). However, this comes with the trade-off of significantly higher development (engineering) cost, and (for some tasks, specifically in end-to-end-discovery) higher inference cost." Section 5, p. 9: "Powering a general agent with an expensive model can lower the overall cost. Though the per-token cost is 3 to 25 times lower for gemini-flash and llama-scout compared to o3 or sonnet, the weaker models often take more steps or get stuck in loops, causing a ReAct agent to end up being twice as expensive in addition to lower-performing."

URL:         https://allenai.org/asta/leaderboard (public address; a 302 redirect sends it to https://allenai-asta-bench-leaderboard.hf.space/home, the Hugging Face Space allenai/asta-bench-leaderboard at https://huggingface.co/spaces/allenai/asta-bench-leaderboard). Retrieved 2026-10-31.
Kind:        primary. Ai2 runs the leaderboard and owns every row on it. The paper cites this address as the leaderboard (footnotes 4 and 11). The hf.space host is recorded because that is where the app renders; it is the same app the allenai.org address redirects to.
Establishes: firsthand: the live overall leaderboard for the test split (87 rows) and the validation split (14 rows), each with Overall Score, Overall Cost, per-category score and cost, categories attempted, run date, openness and tooling class. I read the tables from the data embedded in the page, which carries each value at full precision in a hover tooltip. The page also carries the "Efficiency Frontier" line and a Pareto icon on each frontier row.
Paraphrase:  Overall score is a macro-average of the four category averages, each category weighted equally. Overall cost is, on the home page, "A macro-average of the agent's cost per problem across all categories, in USD. Each category contributes equally." Costed rows number 24 of 87 on the test split; the other 63 show "Missing". The 24 costed rows are all submitted by Ai2 (15 ReAct, 8 Smolagents Coder, 1 Asta v0). Commercial and third-party agents (Elicit, SciSpace Deep Review, FutureHouse Crow and Falcon, OpenAI Deep Research, Perplexity Sonar Deep Research, You.com APIs, RoboPhD, EvoScientist, Button, Qiushi Engine) cover 1 of 4 categories and show no overall cost. The chart axes are "Average (mean) cost per problem (USD)" and "Average (mean) score". The overall chart's error bars are set invisible in the embedded figure, so no interval is shown. The most recent run on the test split is dated 2026-10-25.
Locators:    Home page, "AstaBench Overall Leaderboard (Aggregate)" table under the Test Set tab; the intro text block above it; the note "Agents without cost data are displayed to the right of the vertical divider line"; the Validation Set tab below. The Space's commit list (https://huggingface.co/spaces/allenai/asta-bench-leaderboard/commits/main) includes "Fix Pareto frontier strict-domination semantics (#122)", "Bump scorer deps: agent-eval 0.1.53, inspect_ai 0.3.203, litellm 1.88.1 (#123)" (both 2026-08-05) and "Improve leaderboard cost precision and uncertainty UX (#124)" (2026-08-11).
Quote:       none needed beyond the paraphrase.

URL:         https://allenai-asta-bench-leaderboard.hf.space/about (the About page of the same app)
Kind:        primary. Ai2's own statement of how the leaderboard aggregates scores and cost.
Establishes: firsthand: the leaderboard's definitions and its own caveat about cost.
Paraphrase:  The About page defines Overall cost as the average cost per task "aggregated only across benchmarks with reported cost", reports costs in USD per task, excludes benchmarks without cost data from cost averages, and plots agents without cost at the far right.
Locators:    "Understanding the Leaderboards" and "Scoring & Aggregation" blocks.
Quote:       "Note: Cost values reflect pricing and infrastructure conditions at a fixed point in time. We recognize that compute costs may change over time and vary by provider, and are actively working on methods to keep costs up-to-date and normalized for fair comparisons."

URL:         https://huggingface.co/datasets/allenai/asta-bench-results (files under 1.0.0/test/, for example 1.0.0/test/miked-ai_ReAct-GPT-5_2025-08-11T16-34-47.json)
Kind:        primary. Ai2's repository of the per-run result files the leaderboard is built from.
Establishes: firsthand: what is recorded per run, and that the leaderboard figures can be rebuilt. Each file holds the suite configuration (primary metric and macro-average weights per task), the metrics with standard errors, and for each task a model_usages record per problem (input tokens, output tokens, cache-read and cache-write tokens, reasoning tokens, total_cost) plus a model_costs list with one dollar figure per problem (100 entries for ScholarQA-CS2, 40 for each E2E benchmark). The dataset was last modified 2026-10-27 and holds 87 test files.
Paraphrase:  Cost per problem is the mean of the per-problem model_costs for a benchmark. I averaged benchmarks to category means (LitQA2 tasks at weight 0.5), then averaged the four categories. That reproduced the leaderboard for ReAct gpt-5 (0.4332, $0.309), ReAct gpt-5-mini (0.3136, $0.0366) and Asta v0 (0.5090, $3.395), and the six Ai2_ReAct files from 2026-04 and the ReAct o3 file matched the displayed score and cost.
Locators:    Dataset card feature schema (results, model_usages, model_costs fields); the files named above.
Quote:       none.

URL:         https://github.com/allenai/agent-eval
Kind:        primary. The toolkit the paper and leaderboard use for cost.
Establishes: firsthand: one line of mechanism.
Paraphrase:  The README lists the toolkit's second function as extracting "the token usage of the agent from log files, and computes cost using `litellm`". I did not read the source code of the cost routine.
Locators:    README, opening list.
Quote:       "Extracts the token usage of the agent from log files, and computes cost using `litellm`."

URL:         https://allenai.org/blog/astabench
Kind:        primary. Ai2's own post, dated 2025-08-26, with an update dated 10/27 (2025).
Establishes: firsthand: Ai2's summary of the original results and the cost framing; repeats the paper's design. It reports the original August numbers and says they remain unchanged in the post.
Paraphrase:  Scale given as over 2,400 problems, 57 agents, 22 classes; the overall leaderboard in the post shows 18 agent instances that could do every category. The post reports Asta v0 at 53.0% and ReAct gpt-5 at 43.3%, ReAct claude-3-5-haiku at 20% for "$0.03 per problem", ReAct gpt-5-mini at 31% for "$0.04", and says a gemini-powered ReAct agent "cost 4x more per problem while achieving half the score". The 10/27 update says a change to the paper-search task instructions "approximately doubles costs for both" Paper Finder and LitQA2-FullText-Search and "does not change our main conclusions". It also says reasoning effort is fixed at "medium" for general solvers and "Work is underway to add reasoning effort to the leaderboard".
Locators:    "Update 10/27" box at the top; paragraph beginning "The best economical model is ReAct powered by claude-3-5-haiku"; paragraph beginning "Language model performance can be unintuitive"; footnote marked ** ("reasoning effort"); section "Time-invariant cost reporting"; section "Accounting for submissions with less controlled measurement or lower transparency".
Quote:       "Our displayed costs are time-invariant; model usage details logged (locally) by Inspect enable our package to calculate monetary costs across all submissions using consistent pricing even as provider costs change over time." Also: "warns about results that may not be comparable due to use of external tools, closed-source or model weights, or missing logs or cost information."

URL:         https://allenai.org/blog/astabrief
Kind:        primary. Ai2's post "Open-sourcing AstaBrief, the fast report-generation model in Asta", dated October 2, 2026.
Establishes: firsthand: AstaBrief 8B's purpose and Ai2's latency claim. It is not an AstaBench entry and the post gives no dollar cost.
Paraphrase:  AstaBrief 8B (start: Qwen3-8B; supervised fine-tuning then direct preference optimization) turns a research question and retrieved excerpts into a cited report in one pass. Across the full Asta pipeline, Fast mode averages 51.1 seconds per report against 178.5 seconds for the Claude-powered Thinking mode, "about 3.5× faster". The same paragraph says "nearly an order-of-magnitude reduction in report generation time compared to the proprietary models we tracked". The post says it wanted to reduce "generation time and serving costs" and calls the pipeline "substantially faster and cheaper", and gives no dollar figure for either. Ai2 states that most training and evaluation was completed in 2025 and "We haven't rerun the full evaluation against today's frontier models". Usage: 374 Asta users tried Fast mode; positive feedback 84.2% for Fast and 85.2% for Thinking.
Locators:    Paragraph beginning "Developing AstaBrief required tens of thousands of real research queries" (the 51.1 and 178.5 figures); paragraph beginning "We wanted to help scientists generate cited reports faster"; section "Validating the approach".
Quote:       "across the full Asta pipeline, Fast mode averages 51.1 seconds per report compared with 178.5 seconds for Thinking mode, about 3.5× faster."

URL:         https://huggingface.co/allenai/AstaBrief_8B
Kind:        primary. The model card, last modified 2026-10-03.
Establishes: firsthand: quality numbers on AstaBench's ScholarQA-CS2 test set. It carries no latency figure and no cost figure.
Paraphrase:  On the 100-question ScholarQA-CS2 test set: Qwen3-8B average 77.3, AstaBrief-8B-SFT 83.7, AstaBrief-8B 87 (citation precision 90.5, citation recall 78.2). A second table lists SQA-CS2 test: Asta ScholarQA 86.2, DR-Tulu-8B 88.8, AstaBrief-8B 87.0.
Locators:    "Evaluation Results" section, the two tables.
Quote:       none.

## Contradictions

1. The commission says the diagram should show that "every model call and tool call is metered" and that cost figures "are the agents' measured inference cost ... not retail API prices". The sources support neither sentence as worded. Section 4.2 (p. 6) and the agent-eval README say cost is computed from logged model token usage multiplied by per-token prices from a frozen snapshot of the litellm community cost map, plus Together AI size-based pricing for open-weight models (footnote 9). The prices are a published price table applied to measured tokens, not amounts billed. I found no passage in the paper, the blog, the About page or the README that puts a dollar price on a tool call (corpus search or notebook execution). The tools are standardized so that every agent sees the same information, and their output enters the cost only as tokens the model reads. The paper does not say whether the LLM-judge calls that score rubric-based tasks (gemini-2.5-flash is the official ScholarQA-CS2 judge, Appendix E) are in the agent's cost. The result files hold the agent's model usages. I did not verify this.
2. "Time-invariant" versus "fixed point in time". The paper and blog call costs time-invariant because prices come from one frozen snapshot. The leaderboard About page says costs "reflect pricing and infrastructure conditions at a fixed point in time" and that they "may change over time and vary by provider". Paper footnote 10 says the snapshot may be updated and all costs recalculated. The reconciliation is that costs are comparable within one snapshot and can shift when Ai2 updates it. The Space's commit "Bump scorer deps: ... litellm 1.88.1" (2026-08-05) shows the scoring dependency moved. I did not establish whether the price snapshot moved with it.
3. The paper's tables and the live leaderboard disagree for the same named agents. Paper Table 4 (p. 18): Asta v0 53.0 at $3.40, ReAct gpt-5 44.0 at $0.31, ReAct o3 39.4 at $0.16, ReAct gpt-5-mini 31.6 at $0.04, ReAct claude-3-5-haiku 21.9 at $0.04. Live leaderboard: Asta v0 0.5090 at $3.3950, ReAct GPT-5 0.4332 at $0.3090, ReAct o3 0.3783 at $0.1635, ReAct GPT-5 Mini 0.3136 at $0.0366, ReAct Claude 3.5 Haiku 0.2140 at $0.0359. The Ai2 blog (original numbers) gives Asta v0 53.0, ReAct gpt-5 43.3, Haiku 20% at $0.03, gpt-5-mini 31% at $0.04. The blog's 10/27 update says astabench 0.3.1 changed the paper-search tasks and that the arXiv paper holds the updated results, so paper and leaderboard come from different task versions. That does not explain every gap. The Asta v0 gap (53.0 versus 50.9) is in End-to-End Discovery, where the paper's Table 10 averages 70.4 and 67.3 and the result file gives a category score of 0.600. I could not find the cause. The chart should use one source only. I recommend the live leaderboard (it holds the 2026 runs and the frontier flags) and the paper for mechanism.
4. Two Ai2 pages define Overall cost differently. The home page says "A macro-average of the agent's cost per problem across all categories". The About page says "aggregated only across benchmarks with reported cost". For the 24 costed rows the two readings should coincide; I did not test the case of a partly costed agent.
5. Paper versus blog on why weaker models cost more. The paper says per-token cost is "3 to 25 times lower for gemini-flash and llama-scout compared to o3 or sonnet" and the ReAct agent ends up "twice as expensive". The blog says o3 per-token is "6-10x higher than that of gemini-flash" and a gemini ReAct agent costs "4x more per problem while achieving half the score". The live board gives ReAct Gemini 2.5 Flash at $0.7107 and 0.1524 against ReAct o3 at $0.1635 and 0.3783, which is 4.3 times the cost for 0.40 of the score. The difference is the comparator (Sonnet 4 at $0.3965 gives 1.8 times).
6. AstaBrief: the post gives two speed figures. "Nearly an order-of-magnitude reduction in report generation time" and "about 3.5×" (51.1 s versus 178.5 s) appear in one paragraph. The 3.5 times figure is labeled as the full Asta pipeline. The order-of-magnitude figure has no stated basis in the post. Use only the 51.1 and 178.5 figures, and only as latency.
7. The angle against the sources. (a) The top-accuracy agent is always on a Pareto frontier. The leaderboard's top agent by score, ReAct claude-opus-4-7, is the right end of the frontier. The data show what each step up costs. They do not show that the top agent "is often not the one you would deploy". That is a statement about a budget the reader sets. (b) "No single best science agent" is carried by model swaps inside one scaffold. 10 of the 11 frontier points are Ai2's ReAct baseline with different language models and one is Smolagents Coder with GPT-5. Ai2's specialized agent (Asta v0, 0.5090 at $3.3950) is off the frontier, because ReAct with gpt-5.5 scores 0.5287 at $1.6104. (c) The frontier mixes model generations. Five frontier points are August 2025 runs and six are April 2026 runs, all priced under one cost snapshot.

## Numbers

Figure: 2,404 problems in 11 benchmarks (test 1,918; validation 486); 4 categories; 57 agents of 22 classes in the paper; abstract says "2400+ problems"
Owner:  arXiv 2510.21652, abstract and Table 2 (the sums are mine from the Table 2 rows)
Scope:  paper-era evaluation, Aug 2025 snapshot; DS-1000 alone is 900 of the 1,918 test problems

Figure: Test-split leaderboard, 87 rows, 24 with an overall cost, 23 of those with 4/4 categories (the 24th, Smolagents Coder with Llama 4 Scout, has 3/4)
Owner:  https://allenai.org/asta/leaderboard
Scope:  test split, retrieved 2026-10-31; latest run date on the board 2026-10-25

Figure: Full series for the chart, all 24 costed test-split rows. Score is the leaderboard's Overall Score on a 0 to 1 scale (macro-average of four category averages). Cost is the leaderboard's Overall Cost in USD per problem (macro-average of four category averages of per-problem cost). Values are the full-precision tooltip values rounded to 4 decimals. All submitted by Ai2. Openness is "Open source & closed weights" for every row except the two Llama 4 Scout rows ("Open source & open weights"). Tooling is Standard for ReAct, Custom interface for Smolagents Coder, Fully custom for Asta v0.
Owner:  https://allenai.org/asta/leaderboard (rebuilt from raw files for rows 1, 2, 3, 4, 5, 6, 7, 8, 9, 13)
Scope:  test split, retrieved 2026-10-31

| # | Agent | LLM as displayed | Overall score (0-1) | Overall cost (USD per problem) | Categories | Run date | On leaderboard frontier |
|---|---|---|---|---|---|---|---|
| 1 | ReAct | claude-opus-4-7 | 0.5804 | 3.5422 | 4/4 | 2026-04-21 | yes |
| 2 | ReAct | claude-opus-4-6 | 0.5533 | 2.1851 | 4/4 | 2026-04-21 | yes |
| 3 | ReAct | claude-sonnet-4-6 | 0.5447 | 2.0755 | 4/4 | 2026-04-21 | yes |
| 4 | ReAct | gpt-5.5-2026-04-23 | 0.5287 | 1.6104 | 4/4 | 2026-04-27 | yes |
| 5 | Asta v0 | Claude Sonnet 4 (2025-05), plus 6 other models | 0.5090 | 3.3950 | 4/4 | 2025-08-13 | no |
| 6 | ReAct | gemini-3.1-pro-preview | 0.4958 | 1.2551 | 4/4 | 2026-04-21 | yes |
| 7 | ReAct | gpt-5.4-2026-03-05 | 0.4648 | 0.7006 | 4/4 | 2026-04-21 | yes |
| 8 | ReAct | GPT-5 (2025-08) | 0.4332 | 0.3090 | 4/4 | 2025-08-11 | yes |
| 9 | ReAct | o3 (2025-04) | 0.3783 | 0.1635 | 4/4 | 2025-08-08 | yes |
| 10 | ReAct | Claude Sonnet 4 (2025-05) | 0.3746 | 0.3965 | 4/4 | 2025-08-08 | no |
| 11 | Smolagents Coder | GPT-5 (2025-08) | 0.3535 | 0.1265 | 4/4 | 2025-08-14 | yes |
| 12 | Smolagents Coder | Claude Sonnet 4 (2025-05) | 0.3494 | 1.0239 | 4/4 | 2025-08-08 | no |
| 13 | ReAct | GPT-5 Mini (2025-08) | 0.3136 | 0.0366 | 4/4 | 2025-08-11 | yes |
| 14 | ReAct | GPT-4.1 (2025-04) | 0.3040 | 0.1985 | 4/4 | 2025-08-08 | no |
| 15 | Smolagents Coder | GPT-4.1 (2025-04) | 0.2998 | 0.3212 | 4/4 | 2025-08-08 | no |
| 16 | Smolagents Coder | GPT-5 Mini (2025-08) | 0.2704 | 0.0648 | 4/4 | 2025-08-14 | no |
| 17 | Smolagents Coder | Gemini 2.5 Flash (2024-05) | 0.2450 | 0.7088 | 4/4 | 2025-08-08 | no |
| 18 | ReAct | Claude 3.5 Haiku (2024-10) | 0.2140 | 0.0359 | 4/4 | 2025-08-08 | yes |
| 19 | ReAct | GPT-4o (2024-08) | 0.1617 | 0.1223 | 4/4 | 2025-08-08 | no |
| 20 | ReAct | Gemini 2.5 Flash (2024-05) | 0.1524 | 0.7107 | 4/4 | 2025-08-08 | no |
| 21 | Smolagents Coder | GPT-4o (2024-08) | 0.1311 | 0.3588 | 4/4 | 2025-08-08 | no |
| 22 | Smolagents Coder | Claude 3.5 Haiku (2024-10) | 0.1214 | 0.2974 | 4/4 | 2025-08-08 | no |
| 23 | Smolagents Coder | Llama 4 Scout 17B (unpinned) | 0.1090 | 0.1081 | 3/4 | 2025-08-08 | no |
| 24 | ReAct | Llama 4 Scout 17B (unpinned) | 0.0774 | 0.6784 | 4/4 | 2025-08-08 | no |

Figure: Frontier on the leaderboard: 11 agents, flagged with the Pareto icon. In order of rising cost: rows 18, 13, 11, 9, 8, 7, 6, 4, 3, 2, 1 of the table above. I recomputed the non-dominated set from the 24 rows (an agent is dominated if another has at least its score at no more cost and is strictly better on one) and got the same 11 agents. The cost spread across the frontier is $0.0359 to $3.5422, a factor of 98.7, so a log x-axis is warranted. The paper's Figure 2 also uses a log axis.
Owner:  https://allenai.org/asta/leaderboard (flags); recomputation is mine
Scope:  test split, 24 costed rows, retrieved 2026-10-31

Figure: Ranking by accuracy versus by score per dollar (overall score divided by overall cost), over the 23 agents with 4/4 coverage. Derived by me. Accuracy rank / score-per-dollar rank: ReAct claude-opus-4-7 1 / 21 (0.16 per dollar); claude-opus-4-6 2 / 19; claude-sonnet-4-6 3 / 18; gpt-5.5 4 / 17; Asta v0 5 / 22 (0.15); gemini-3.1-pro 6 / 13; gpt-5.4 7 / 11; ReAct GPT-5 8 / 7 (1.40); ReAct o3 9 / 5 (2.31); Smolagents GPT-5 11 / 4 (2.79); ReAct GPT-5 Mini 13 / 1 (8.56); Smolagents GPT-5 Mini 16 / 3 (4.17); ReAct Claude 3.5 Haiku 18 / 2 (5.95); ReAct Llama 4 Scout 23 / 23 (0.11). Score per dollar favors the cheapest agents by construction and rewards a dominated agent: Smolagents GPT-5 Mini is third by this measure and is dominated by ReAct GPT-5 Mini (0.3136 at $0.0366 against 0.2704 at $0.0648).
Owner:  derived from the leaderboard rows above
Scope:  23 agents with 4/4 coverage and cost

Figure: Cheaper agents within a few points of the most accurate agent (ReAct claude-opus-4-7, 0.5804 at $3.5422). Derived by me.
  ReAct claude-opus-4-6: 2.7 points lower (0.5533), $2.1851, 61.7% of the cost.
  ReAct claude-sonnet-4-6: 3.6 points lower (0.5447), $2.0755, 58.6% of the cost, $1.47 per problem cheaper.
  ReAct gpt-5.5: 5.2 points lower (0.5287), $1.6104, 45.5% of the cost (2.2 times cheaper).
  ReAct gemini-3.1-pro: 8.5 points lower (0.4958), $1.2551, 35.4% of the cost.
  ReAct gpt-5.4: 11.6 points lower (0.4648), $0.7006, 19.8% of the cost (5.1 times cheaper).
  ReAct GPT-5: 14.7 points lower (0.4332), $0.3090, 8.7% of the cost (11.5 times cheaper).
  ReAct GPT-5 Mini: 26.7 points lower (0.3136), $0.0366, 1.03% of the cost (96.8 times cheaper), keeping 54% of the top score.
Owner:  derived from the leaderboard rows above
Scope:  23 agents with 4/4 coverage and cost; one run per agent

Figure: Where paying more buys accuracy, as steps along the frontier (extra points, extra dollars per problem, cost multiple). Derived by me.
  ReAct Claude 3.5 Haiku to ReAct GPT-5 Mini: +10.0 points for +$0.0007 (Haiku is on the frontier only because it is $0.0007 cheaper).
  GPT-5 Mini to Smolagents Coder GPT-5: +4.0 points for +$0.0899 (3.5 times).
  Smolagents Coder GPT-5 to ReAct o3: +2.5 points for +$0.0370 (1.3 times).
  ReAct o3 to ReAct GPT-5: +5.5 points for +$0.1455 (1.9 times).
  ReAct GPT-5 to ReAct gpt-5.4: +3.2 points for +$0.3916 (2.3 times).
  ReAct gpt-5.4 to ReAct gemini-3.1-pro: +3.1 points for +$0.5545 (1.8 times).
  ReAct gemini-3.1-pro to ReAct gpt-5.5: +3.3 points for +$0.3553 (1.3 times).
  ReAct gpt-5.5 to ReAct claude-sonnet-4-6: +1.6 points for +$0.4651 (1.3 times).
  ReAct claude-sonnet-4-6 to ReAct claude-opus-4-6: +0.9 points for +$0.1096 (1.1 times).
  ReAct claude-opus-4-6 to ReAct claude-opus-4-7: +2.7 points for +$1.3571 (1.6 times).
  Spans: GPT-5 Mini ($0.0366) to ReAct GPT-5 ($0.3090) buys +12.0 points for 8.4 times the cost. GPT-5.5 ($1.6104) to claude-opus-4-7 ($3.5422) buys +5.2 points for 2.2 times the cost.
Owner:  derived from the leaderboard rows above
Scope:  the 11 frontier agents

Figure: Agents that spend more and score lower (dominated rows). Derived by me.
  Asta v0 (0.5090, $3.3950) against ReAct gpt-5.5 (0.5287, $1.6104): gpt-5.5 scores 2.0 points higher at 47.4% of the cost. Asta v0 is Ai2's own specialized agent; the paper says its higher development (engineering) cost is not in the figure.
  ReAct Claude Sonnet 4 (0.3746, $0.3965) against ReAct o3 (0.3783, $0.1635): o3 scores 0.4 points higher at 41.2% of the cost.
  ReAct Llama 4 Scout (0.0774, $0.6784) against ReAct GPT-5 Mini (0.3136, $0.0366): 18.5 times the cost for a quarter of the score. The open-weight model is priced from Together AI size-based pricing (paper footnote 9).
  ReAct Gemini 2.5 Flash (0.1524, $0.7107) against ReAct o3 (0.3783, $0.1635): 4.3 times the cost for 40% of the score.
Owner:  derived from the leaderboard rows above
Scope:  23 agents with 4/4 coverage and cost

Figure: What drives the overall cost. For ReAct claude-opus-4-7 the category costs are Literature Understanding $1.803, Code & Execution $2.101, Data Analysis $0.439, End-to-End Discovery $9.826 (the overall $3.542 is their mean), so End-to-End Discovery is 69% of the four-category sum. Its End-to-End scores come from 80 problems (40 in each of E2E-Bench and E2E-Bench-Hard). For Asta v0 the paper's Table 4 gives End-to-End Discovery $12.57 against $0.19 for Code & Execution and $0.25 for Data Analysis.
Owner:  https://allenai.org/asta/leaderboard (row 1 category columns); paper Table 4 (Asta v0)
Scope:  category-level means of per-problem cost, test split

Figure: 95% confidence intervals for the overall score, computed by me from the raw result files by the method in the paper's Appendix D (standard error per benchmark, weighted propagation to category, root-sum-square of the four category standard errors divided by 4, times 1.96). The same method gives ReAct gpt-5 ±2.9 against the paper's ±3.0. claude-opus-4-7 58.0 ±2.7; claude-opus-4-6 55.3 ±2.4; claude-sonnet-4-6 54.5 ±2.7; gpt-5.5 52.9 ±3.0; gemini-3.1-pro 49.6 ±2.5; gpt-5.4 46.5 ±2.5; ReAct GPT-5 43.3 ±2.9; ReAct o3 37.8 ±2.5; ReAct GPT-5 Mini 31.4 ±2.6; Asta v0 50.9 ±2.5 (score points). The interval for claude-opus-4-7 overlaps those of claude-opus-4-6, claude-sonnet-4-6 and gpt-5.5, and does not overlap gemini-3.1-pro's. These intervals reflect sampling over problems in one run per agent; no repeated-run variance is published. No cost interval is published for the overall figure.
Owner:  computed by the researcher from https://huggingface.co/datasets/allenai/asta-bench-results; the paper's Table 11 publishes intervals for its own runs (for example ReAct gpt-5 44.0 ±3.0, o3 39.4 ±2.6, gpt-5-mini 31.6 ±2.7, claude-sonnet-4 40.1 ±2.4, Asta v0 53.0 ±2.4)
Scope:  test split overall score

Figure: Paper-era series (Table 4, p. 18; Table 11, p. 21). Score in percent, cost in USD per problem. Asta v0 mixture 53.0, 3.40. ReAct gpt-5 44.0, 0.31. ReAct o3 39.4, 0.16. Smolagents Coder claude-sonnet-4 38.1, 1.02. Smolagents Coder gpt-5 37.5, 0.13. ReAct gpt-5-mini 31.6, 0.04. ReAct claude-3-5-haiku 21.9, 0.04. Smolagents Coder llama-4-scout 11.1, 0.11. Table 11 extends this to 18 agents (for example ReAct claude-sonnet-4 40.1, 0.40; ReAct gpt-4.1 31.6, 0.20; ReAct gemini-2.5-flash 15.3, 0.71; ReAct llama-4-scout 7.9, 0.68; Smolagents Coder gemini-2.5-flash 26.4, 0.71). Cost columns are rounded to two decimals in the paper.
Owner:  arXiv 2510.21652, Tables 4 and 11
Scope:  the 18 agents that attempt all four categories, paper v2 task versions (astabench 0.3.1)

Figure: AstaBrief 8B Fast mode averages 51.1 seconds per report; Thinking mode (Claude-powered) averages 178.5 seconds; Ai2 calls the ratio "about 3.5×".
Owner:  https://allenai.org/blog/astabrief
Scope:  full Asta pipeline; the post does not give a sample size, a date range or the hardware for these averages

## Limits

1. Per-agent cost IS published. The leaderboard gives overall cost per problem in USD for 24 test-split agents, the paper gives it for 8 agents in Table 4 and 18 in Table 11, and the raw per-problem costs are in Ai2's results dataset. A real chart can be built from the table in Numbers. Nothing here forces a conceptual chart.
2. The commission's sentence that "every model call and tool call is metered" cannot be sourced. Model calls are metered and priced. Tool calls are standardized and not priced. The drawn diagram should show metered model calls (tokens in, tokens out, cache reads, reasoning tokens) priced from a fixed table, with the search and notebook tools drawn as the controlled environment.
3. The commission's sentence that cost is "not retail API prices" cannot be sourced. Cost is logged tokens times prices from a frozen litellm snapshot (community-sourced) with cache discounts and no batching or service-tier discounts. It is a price-table cost of the measured token usage, not a billed amount. The paper does not say which snapshot date applies, and I did not find it.
4. Every costed row was submitted by Ai2 and is one of its three baselines (ReAct, Smolagents Coder, Asta v0). No external or commercial agent has an overall cost. Elicit, SciSpace, FutureHouse, OpenAI Deep Research, Perplexity and You.com cover one category and show "Missing". The paper's Table 6 gives dollar costs for some commercial agents on ScholarQA-CS2 alone (OpenAI Deep Research $1.803, FutureHouse Falcon $0.403, Perplexity Sonar Deep Research $0.416), and I did not find how those costs were obtained. The leaderboard's category pages may show more; I read only the overall page.
5. The frontier is mostly one scaffold. 10 of 11 frontier points are ReAct and one is Smolagents Coder, so the article can say "which language model to put in the same agent" and cannot say "which kind of agent", except for the one comparison with Asta v0. Five frontier points are runs from August 2025 and six from April 2026.
6. One run per agent. The intervals I computed cover sampling over problems only. Several adjacent frontier steps (claude-opus-4-6 to claude-opus-4-7, claude-sonnet-4-6 to claude-opus-4-6) are inside one another's intervals. The leaderboard's overall chart has no error bars and the paper publishes none for the live runs.
7. Overall cost is a macro-average of four category means of per-problem cost. It is not the mean cost over the 1,918 test problems. The End-to-End Discovery category (80 problems) supplies most of the cost for the expensive agents (69% of the category-cost sum for claude-opus-4-7).
8. Cost excludes engineering cost (paper, Section 5, p. 7, for Asta v0). Reasoning effort is fixed at "medium" for general solvers and is not on the leaderboard (blog footnote). The paper does not say whether LLM-judge calls enter the cost.
9. The paper's numbers and the leaderboard's differ for the same agents (Contradiction 3). The cause of the Asta v0 gap is unexplained. The two sources must not be mixed on one chart.
10. No document I read cautions against reading the frontier as a deployment guide. The paper's stated caution is about capability: "AI remains far from solving the challenge of science research assistance" (abstract). I searched the paper text for deployment, cost-accounting and exclusion language and found only the passages cited above. The leaderboard flags results "that may not be comparable due to use of external tools, closed-source or model weights, or missing logs or cost information" (blog), and the About page warns that costs vary with provider and time.
11. AstaBrief 8B has no AstaBench leaderboard row and no dollar cost in Ai2's post or model card. Only latency (51.1 s against 178.5 s) is given, the sample behind it is not described, and Ai2 says the evaluation was not rerun against current frontier models. It cannot be placed on the cost frontier. The model card's ScholarQA-CS2 test score (87.0) is a single-benchmark figure.
12. I did not open the OpenReview version (https://openreview.net/forum?id=M7TNf5J26u, linked from the About page) and did not render the leaderboard chart. I read its data.

## Source assets

Asset: Figure 2, p. 8 of arXiv 2510.21652, panel "Overall" (top left of six panels). Score against cost per answer in USD on a log x-axis, one marker per agent configuration, dotted line joining the Pareto-frontier agents, legend entries under "Efficiency Frontier".
Shows:  the frontier for the paper-era agents (the numbers of Tables 4 and 11, not the live board). Shows that the cost axis spans two decades and that the frontier bends flat at the high-cost end.
Crop:   keep the axis labels, the log tick labels, the dotted frontier line and the legend. The other panels (Literature Understanding, Code & Execution, Data Analysis, End-to-End Discovery) may be omitted. The caption note "the x-axis (cost per answer in dollars) uses a log scale" must travel with it. Its numbers differ from the live leaderboard's.

Asset: Figure 1, p. 3 of arXiv 2510.21652. A schematic: Agent and LLM, Task, Standard Tools, Rubric & LLM Judge feeding Accuracy, and Compute Cost.
Shows:  the paper's own picture of where accuracy and cost come from in one evaluation. Its caption: "AstaBench leaderboards record not just agents accuracy but also how much computation is required to achieve that performance."
Crop:   the whole figure. The drawn diagram in the article can refine it with the token-usage and price-table step from Section 4.2.

Asset: Table 4, p. 18 of arXiv 2510.21652 (and Table 11, p. 21). Per-agent overall score and cost with per-category columns; the caption says bold marks agents on the Pareto-optimal frontier for that column pair. I read the table as extracted text and did not check the bold in the rendered PDF.
Shows:  the category cost spread behind each overall cost, for example Asta v0 End-to-End Discovery $12.57 against $0.19 for Code & Execution.
Crop:   keep the header rows (Overall, then the four categories, each with Score and Cost) and the "O" and "T" columns.

Asset: The interactive scatter on https://allenai.org/asta/leaderboard, "AstaBench Overall Leaderboard (Aggregate)", Test Set tab. X-axis "Average (mean) cost per problem (USD)", y-axis "Average (mean) score", a dashed green "Efficiency Frontier" line, different markers by openness class, hover text with score, cost, openness, tooling and models. Agents without cost sit right of a divider.
Shows:  the live frontier of 11 agents and the unplotted commercial agents.
Crop:   keep both axis titles, the frontier line, and the divider with its "Missing cost" side. The writer plots the table in Numbers with `nb chart`; the page's figure data had no error bars and I did not verify its axis scale because I did not render it.

## Discarded

https://www.google.com/url?q=https://aclanthology.org/2025.acl-demo.49.pdf: linked from the model card as the ScholarQA system paper; not opened, not needed for any figure.
https://diyai.io/news/ai2-astabrief-open-research-report-model/ and four other third-party AstaBrief write-ups (zipmex.com, fourweekmba.com, nocode.mba, orcarouter.ai): seen only as search-result snippets, not opened. They restate Ai2's 51.1 and 178.5 second figures, which I read in Ai2's own post, so they add nothing and are not sources for any number.
https://huggingface.co/spaces/OpenHands/openhands-index: a fork of the AstaBench leaderboard code by another team, seen only as a search snippet and not opened. It is not AstaBench's own leaderboard.
https://www.flowhunt.io/glossary/benchmarking and https://oumi.ai/docs/en/latest/user_guides/evaluate/leaderboards.html: general benchmarking pages that came up in search, not opened, no AstaBench figures.
