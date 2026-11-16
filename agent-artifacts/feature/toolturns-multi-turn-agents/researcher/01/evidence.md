# Evidence: ToolTurns (arXiv 2611.14925v1)

The paper's Tables 3, 4 and 11 report, for all nine agents, the three per-position success rates (opening, follow-up 1, follow-up 2), the pooled per-request rate, the all-three-pass dialogue rate, five rubric aspects and a weighted rubric score. That is enough to compare, per model, the observed dialogue completion with what independent turns would predict, and to line up rubric rank against task-success rank. The comparison has one limit the writer must carry: the tables give marginal rates only, never joint outcomes, so they show that failures cluster (observed completion beats the independent prediction by 5.8 to 8.4 points for every model) and cannot say why. The paper itself already makes the independence calculation for the best model (0.696^3 = 34% against 39.8%, section 4.1.3), so the per-model version extends the paper and does not originate the idea. The finding also cuts against a "failures compound" framing: most of the 69.6% to 39.8% drop is plain arithmetic (three required passes), and the clustering makes completion higher than independent turns would give. The numbers rest on one run per agent, LLM judges, an LLM-simulated tool layer and an LLM-simulated user, with no confidence intervals on Tables 3 and 4. The rubric-versus-success disagreement (Spearman 0.23) is driven largely by one model (GPT-5.4-mini); without it the correlation is 0.64 (my computation). Two outside sources (tau-bench, Laban et al.) are recorded with exact passages. Neither measures per-turn decay inside a dialogue, so both are context and not confirmation.

Artifact root for relative paths: `.nb-work/feature/toolturns-multi-turn-agents/agent-artifacts/feature/toolturns-multi-turn-agents/`.

## Sources

URL:         https://arxiv.org/html/2611.14925v1 (PDF: https://arxiv.org/pdf/2611.14925v1; abstract: https://arxiv.org/abs/2611.14925)
Kind:        primary for every ToolTurns figure and design detail (the authors own the benchmark and the runs). The authors designed the benchmark and the evaluators, so every claim of validity is a claim by the party with the stake. A single preprint (cs.CL, submitted 11 Nov 2026, v1, CC BY 4.0). No venue or peer review is stated.
Establishes: firsthand: all of Tables 2 to 11 below, the construction details, the limitations. Merely repeats: nothing used from other work except descriptions of tau-bench, ToolSandbox and others in Table 1.
Paraphrase:  Authors: Milad Gholami, Brendan King, Jeffrey Flanigan, University of California, Santa Cruz. 2,620 problems, each producing exactly one dialogue of three requests (opening plus two follow-ups), 7,860 scored subtasks per agent. Nine agents evaluated with the user simulator, tool layer and judges held fixed. Pooled per-request success tops out at 69.6% (Claude Opus 4.8), all-three-pass at 39.8% (same model). Every model scores lower on both follow-ups than on the opening request. Rubric-aspect scores and task success rank models very differently (Spearman 0.23).
Locators:    Abstract; section 1 (Introduction); section 3.1 to 3.4 (design); section 4.1.1 to 4.1.3 (setup, models, results, Tables 3 and 4); section 4.2.1 (judge validation); section 6 (Limitations); Appendix B.2.3 to B.4 (simulator checks); Appendix C (budgets); Appendix F.1 to F.4 (worked examples, Tables 9 to 11); Appendix G.4 (task-success judge prompt). The paper contains no figures, only tables and transcripts.
Quote:       "If subtask outcomes within a dialogue were independent, a 69.6% subtask rate would imply a 0.696^3≈34% all-pass rate; the observed 39.8% is higher, so successes and failures are positively correlated within a dialogue." (section 4.1.3, paragraph after Table 3). Also: "This pattern does not isolate a cost of conversational dependence: the judge omits prior-subtask tool evidence, which can hide the provenance of reused information (§ F.3). The effect of that omission on follow-up declines and model comparisons has not been established." (section 4.1.3, after Table 4).

URL:         https://arxiv.org/abs/2406.12045 (HTML: https://arxiv.org/html/2406.12045v1)
Kind:        primary for tau-bench's own pass^k results (the authors ran and own them). Not a ToolTurns source: outside context. Authors: Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan, Sierra (Yao's work done during an internship, per the paper's footnote). Submitted 17 Jun 2024.
Establishes: firsthand: gpt-4o function-calling agent pass^1 about 61% on tau-retail and about 35% on tau-airline; pass^8 below 25% on retail; the definition of pass^k. This is repeated trials of the same task, not successive turns, so it measures consistency and not turn-to-turn decay.
Paraphrase:  pass^k is "the chance that all k i.i.d. task trials are successful, averaged across tasks". Best agent (gpt-4o, function calling) falls from above 60% at k=1 to below 25% at k=8 in retail. Independent trials at a flat 61% would give 0.61^8 = 1.9% at k=8 (my arithmetic, not in the paper), so the observed 25% means success is heavily task-dependent: some tasks are solved nearly every time and others rarely. The same structure as ToolTurns's clustering: a score on single attempts overstates what "every attempt must pass" will deliver, and the effect is smaller than independence predicts because difficulty is shared across attempts.
Locators:    Abstract; section 1 (Introduction, paragraph beginning "Our experiments reveal"); section 5.1 "Agent consistency via pass^k" and Figure 4 (pass^k and pass@k curves in tau-retail; the per-k values exist only in the figure, which I did not read pixel by pixel); section 5.2 "Failure 3: Partial resolution of compound requests" (19% of failures).
Quote:       "Even for the best-performing gpt-4o function calling agent which has a >60% average task success, pass^8 drops to <25%." (section 5.1). Also: "Upon analyzing the failure cases, we find that current agents struggle with complex reasoning over databases, understanding and following ad-hoc policies, and handling compound (more than one) requests." (section 1)

URL:         https://arxiv.org/abs/2505.06120 (HTML: https://arxiv.org/html/2505.06120v1)
Kind:        primary for its own simulation results. Authors: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville (Microsoft Research and Salesforce Research; the HTML header scrambles which author goes with which affiliation, so cite the affiliations jointly). "LLMs Get Lost In Multi-Turn Conversation", submitted 9 May 2025. Single-turn text tasks (code, database, actions, math, data-to-text, summary), not a tool-use benchmark except the Actions task.
Establishes: firsthand: across 15 LLMs and more than 200,000 simulated conversations, an average 39% drop from fully specified single-turn to sharded multi-turn; decomposed into a 16% average aptitude loss and a 112% average increase in unreliability. A control (Concat: all the sharded information given in one turn) averages 95.1% of the single-turn score, so lost information does not explain the drop.
Paraphrase:  Agrees with ToolTurns on direction (later turns, worse outcomes) and supplies the control ToolTurns lacks: Laban et al. hold the information constant and change only whether it arrives over several turns. It also supplies a mechanism for clustering: early wrong assumptions and premature answers that later turns rely on. It does not support per-turn decay inside a fixed-length dialogue; it compares single-turn to multi-turn and does not tabulate success by turn position.
Locators:    Abstract; section 6.1 "Average Performance Findings" (the -39% and the Concat control); section 6.2 "Aptitude vs. Reliability Analysis" (16% and 112%; "performance degrading 50 percent points on average between the best and worst simulated run"); section 6.3 gradual sharding experiment (GPT-4o and GPT-4o-mini only); Appendix F (root causes).
Quote:       "when LLMs take a wrong turn in a conversation, they get lost and do not recover" (abstract). Also: "every model sees its performance degrade on every task when comparing Full and Sharded performance, with an average degradation of -39%." (section 6.1). Caveat the authors state themselves: the sharded setup, with the user revealing at most one shard per turn, "can seem unrealistic and adversarial" (section 6.3).

URL:         https://arxiv.org/abs/2501.17399
Kind:        primary for MultiChallenge's own figures. First author Ved Sirdeshmukh, nine co-authors; affiliation not checked. Submitted 29 Jan 2025.
Establishes: its abstract states that "all frontier models have less than 50% accuracy on MultiChallenge, with the top-performing Claude 3.5 Sonnet (June 2024) achieving just a 41.4% average accuracy." That is a low absolute level on multi-turn conversation challenges, not a per-turn or per-dialogue comparison.
Paraphrase:  Read abstract only, not the body. Recorded as a possible but weak third reference; I recommend not using it, since it offers no per-turn structure.
Locators:    Abstract only.

## Contradictions

1. The commissioned angle says the per-request to per-dialogue gap "can be shown" to reflect how failures in one turn relate to the next. The paper's tables support one specific, modest reading: the observed all-three-pass rate beats the independence prediction in all nine models, by 5.8 to 8.4 percentage points. Most of the headline gap is compounding. For Opus 4.8, 69.6% falls to 39.8%, and independence alone would already give about 33.5% to 33.7%. Failures cluster. They do not cascade in a way that makes dialogues worse than independent turns would predict.
2. Opening-request rate cubed is a different baseline, and it does not show a consistent shortfall. A buyer who evaluates on opening requests only and cubes the result would predict 41.7% for Opus 4.8 against 39.8% observed. That is 1.9 points high. Across the nine models the cubed opening rate is above the observed dialogue rate for six models (by 1.6 to 3.3 points) and below it for three (GPT-4.1-mini by 2.9, GPT-5.4-mini by 6.9, Qwen3.6-27B by 0.5). The follow-up decline and the clustering partly cancel (my arithmetic from Tables 3 and 4, see Numbers). So "single-request evaluation overstates dialogue completion" is not shown uniformly. What it overstates is the success of follow-ups, which is a separate claim (Table 4).
3. Paper on the decline itself: "This pattern does not isolate a cost of conversational dependence" (section 4.1.3). The paper concedes the follow-up decline may partly be a judging artifact, because the task-success judge sees only the current subtask's slice (Appendix F.3, with a worked case: problem 1515, Gemma 4, where figures retrieved one subtask earlier were scored as fabricated). The follow-up drop cannot be presented as a measured cost of context carry-over.
4. GPT-OSS-120B's decline and its position at the bottom are partly protocol artifacts. In 56.1% of its dialogues it returns a plain-text answer instead of calling finish, which leaves the subtask open, so the next user turns attach to the wrong slice (Appendix F.4, Table 11; the transcript in F.1). The paper says part of its 16.2-point decline "reflects non-compliance with the tool-calling protocol rather than failures of reasoning or tool use". GPT-OSS is also the judge model (Table 3 footnote ‡). Treat its row (largest decline, lowest per-request rate, largest ratio of observed to independent) as unreliable for any claim about conversation itself.
5. GPT-5.4-mini flatness. It has the flattest profile (57.6, 55.9, 55.5) and the lowest opening score, yet the paper says "this smaller measured decline does not establish stronger multi-turn ability" (section 4.1.3). 28.3% of its opening queries make no API call (Table 11), and it succeeds on only 44.3% of those (Appendix F.4). It also gives the largest rubric-versus-success disagreement.
6. Opus 4.8 and Qwen3.6-27B recover on follow-up 2 (+3.2 and +2.9 points over follow-up 1), so the decline is not monotone for every model (paper, section 4.1.3). The paper says the larger share of every model's loss comes at follow-up 1, then it is "roughly flat".
7. The rubric-versus-success disagreement is concentrated. Spearman between weighted rubric and task success is 0.23 (paper; I reproduce 0.233 from Table 3). Dropping GPT-5.4-mini only gives 0.64 (n=8), and dropping it and GPT-4o-mini gives 0.57 (n=7) (my computation). With nine models a rank correlation of 0.23 is not distinguishable from zero: the exact two-sided permutation p-value is 0.55 (my computation). So "ranks models very differently" is a statement about these nine, driven by a few models, and not an established property of rubric scoring. The paper's own explanation is specific and checkable: GPT-5.4-mini makes the fewest API calls (3.6 per dialogue), so it leads on efficiency and consistency and trails on task success (Appendix F.2, F.4).
8. Rubric reliability against humans is moderate (quadratic weighted kappa 0.53 on the five aspects, section 4.2.1) while task-success judging is substantial (kappa 0.68). The paper does not give the number of dialogues in that human check or whether it covered all nine agents. That is a gap in the trust case for the rubric half of the comparison, and a weaker one for task success.
9. On the user simulator, the paper's own evidence is mixed. Dialogue-level scores are nearly identical across user-simulator conditions (overall 0.858, 0.862, 0.871 in Table 5), which the authors call "insensitive" to the intervention. The checker-fixer works at the turn level: on 536 rewritten turns detected defects fall from 335 to 197 (41.2%), and 76 of 120 blind human pairs prefer the revision (63.3%, p=0.005). Those turns come from a separate 322-dialogue single-call condition, and "the 2,620-problem ToolTurns set" was not what was tested (section 4.2). The paper does not test whether the checker-fixer changes agent scores. It does state: "The turn-level design also cannot speak to whether repairing individual turns compounds into better dialogues" (Appendix B.3.2, limitations paragraph).

## Numbers

### Source tables (transcribed, as printed)

Table 3 (section 4.1.3; 2,620 dialogues per agent; "dialogues and subtasks for which the judge returned an error are excluded"; GPT-OSS is also the judge). Task success = pooled subtask pass rate. "all three pass" = share of dialogues in which all three subtasks pass.

| Metric | 4o-mini | 4.1-mini | 5.4-mini | Opus 4.8 | Qwen3.5-397B | Qwen3.6-27B | Gemma 4-31B | GPT-OSS-120B | GLM-5.2-744B |
|---|---|---|---|---|---|---|---|---|---|
| Overall (weighted rubric) | 0.646 | 0.740 | 0.817 | 0.809 | 0.683 | 0.709 | 0.759 | 0.693 | 0.685 |
| Task success | 57.0% | 64.5% | 56.3% | 69.6% | 60.9% | 61.0% | 67.5% | 55.2% | 67.9% |
| all three pass | 25.1% | 33.9% | 26.0% | 39.8% | 29.3% | 29.0% | 36.4% | 24.9% | 37.7% |
| Consistency | 0.839 | 0.866 | 0.924 | 0.898 | 0.837 | 0.858 | 0.899 | 0.873 | 0.836 |
| Relevance | 0.581 | 0.713 | 0.771 | 0.788 | 0.646 | 0.717 | 0.696 | 0.695 | 0.662 |
| Efficiency | 0.433 | 0.573 | 0.696 | 0.604 | 0.444 | 0.520 | 0.529 | 0.494 | 0.439 |
| Correctness | 0.722 | 0.798 | 0.861 | 0.866 | 0.766 | 0.732 | 0.862 | 0.708 | 0.752 |
| Adaptability | 0.569 | 0.693 | 0.802 | 0.908 | 0.685 | 0.707 | 0.754 | 0.680 | 0.716 |

Rubric weights (section 3.4.1): correctness 0.30; consistency, relevance, efficiency 0.20 each; adaptability 0.10. Each aspect is scored on five levels (0, 0.25, 0.5, 0.75, 1.0). The paper says it does not read second-decimal gaps as meaningful. Opus 4.8 is "Claude Opus 4.8" (section 4.1.2). Open-weight models: Qwen3.5-397B-A17B, Qwen3.6-27B, Gemma 4-31B-IT, GPT-OSS-120B, GLM-5.2-744B.

Table 4 (section 4.1.3; subtask success rate, %, by position; delta = follow-up 2 minus initial, as printed):

| Model | Initial | FU 1 | FU 2 | Delta |
|---|---|---|---|---|
| GPT-4o-mini | 65.2 | 55.7 | 50.3 | -14.9 |
| GPT-4.1-mini | 67.7 | 63.9 | 62.0 | -5.7 |
| GPT-5.4-mini | 57.6 | 55.9 | 55.5 | -2.1 |
| Opus 4.8 | 74.7 | 65.4 | 68.6 | -6.1 |
| Qwen3.5-397B | 67.6 | 57.8 | 57.5 | -10.1 |
| Qwen3.6-27B | 65.8 | 57.2 | 60.1 | -5.7 |
| Gemma 4-31B | 73.5 | 65.5 | 63.5 | -10.0 |
| GPT-OSS-120B | 65.2 | 51.5 | 49.0 | -16.2 |
| GLM-5.2-744B | 74.1 | 64.8 | 64.8 | -9.3 |

Consistency checks I ran: the mean of each Table 4 row equals the Table 3 task-success figure to within 0.1 (for example Opus (74.7+65.4+68.6)/3 = 69.57 against 69.6). The 7,860 subtasks per agent equal 2,620 x 3, and the gate paragraph counts 70,740 subtasks across nine agents (9 x 7,860), so the per-position rates and Table 3 appear to share a denominator. The paper does not state how many dialogues the "judge error" exclusion removed, so that is an assumption. The printed deltas in Table 4 match my subtraction (final minus initial) for all nine rows.

Table 11 (Appendix F.4; behaviours over all 2,620 dialogues per agent):

| Behaviour | 4o-mini | 4.1-mini | 5.4-mini | Opus 4.8 | Qwen3.5 | Qwen3.6 | Gemma 4 | GPT-OSS | GLM-5.2 |
|---|---|---|---|---|---|---|---|---|---|
| finish calls that give up (%) | 7.1 | 1.6 | 6.9 | 0.1 | 7.9 | 6.1 | 1.1 | 12.4 | 0.6 |
| Initial queries with no API call (%) | 1.7 | 4.0 | 28.3 | 3.3 | 2.3 | 2.2 | 4.1 | 9.2 | 1.1 |
| API calls per dialogue | 15.6 | 8.3 | 3.6 | 7.2 | 14.0 | 10.3 | 10.6 | 10.7 | 17.4 |
| message_user calls per dialogue | 3.05 | 1.99 | 0.73 | 0.86 | 1.38 | 1.78 | 0.92 | 1.36 | 1.29 |
| Dialogues with an answer outside finish (%) | 0.3 | 0.0 | 0.5 | <0.1 | <0.1 | 0.3 | <0.1 | 56.1 | <0.1 |

Paper-reported rank statistics (section 4.1.3, Appendix F.4):
- Spearman 0.97 between the two task-success definitions (pooled subtask rate and all-three-pass), "differing only in two swaps of adjacent pairs". I confirm: Qwen3.5 and Qwen3.6 swap (6th and 5th by pooled; 5th and 6th by all-three-pass), and GPT-4o-mini and GPT-5.4-mini swap (7th and 8th; 8th and 7th).
- Spearman 0.23 between rubric weighted aggregate and task success. I reproduce 0.233 from Table 3.
- Give-up rate versus task success: Spearman -0.93 (Appendix F.4).
- Consistency spans 0.836 to 0.924 (0.09); efficiency 0.433 to 0.696 (0.26); adaptability 0.569 to 0.908 (0.34, at weight 0.10).

### Derived figures (computed by the researcher from Tables 3 and 4; not printed in the paper)

Figure: independent-turn prediction = initial x FU1 x FU2 (Table 4 rates multiplied), against the observed all-three-pass rate (Table 3). Rounding error from one-decimal inputs is under 0.3 points.
Owner:  inputs from Tables 3 and 4 (ToolTurns paper); the arithmetic is mine.
Scope:  2,620 dialogues per agent; one run per agent; assumes the per-position rates and the all-three-pass rate share one denominator (not stated).

| Model | Product of Table 4 rates | Pooled rate cubed (paper's method) | Observed all-three-pass | Observed minus product (points) | Observed / product | Perfect-overlap ceiling (lowest of the three rates) |
|---|---|---|---|---|---|---|
| GPT-4o-mini | 18.3 | 18.5 | 25.1 | +6.8 | 1.37 | 50.3 |
| GPT-4.1-mini | 26.8 | 26.8 | 33.9 | +7.1 | 1.26 | 62.0 |
| GPT-5.4-mini | 17.9 | 17.8 | 26.0 | +8.1 | 1.45 | 55.5 |
| Opus 4.8 | 33.5 | 33.7 | 39.8 | +6.3 | 1.19 | 65.4 |
| Qwen3.5-397B | 22.5 | 22.6 | 29.3 | +6.8 | 1.30 | 57.5 |
| Qwen3.6-27B | 22.6 | 22.7 | 29.0 | +6.4 | 1.28 | 57.2 |
| Gemma 4-31B | 30.6 | 30.8 | 36.4 | +5.8 | 1.19 | 63.5 |
| GPT-OSS-120B | 16.5 | 16.8 | 24.9 | +8.4 | 1.51 | 49.0 |
| GLM-5.2-744B | 31.1 | 31.3 | 37.7 | +6.6 | 1.21 | 64.8 |

Reading: every model sits above independence and far below perfect overlap, so the three outcomes are positively related and nowhere near identical. The excess is 5.8 to 8.4 points in absolute terms for all nine models, so the ratio is larger for weaker models (1.51 for GPT-OSS, 1.19 for Opus and Gemma 4) mostly because their products are smaller. Opus 4.8's pooled-cubed figure (33.7%) matches the paper's "≈34%". The ceiling column is the highest all-three-pass rate any joint distribution could give, the minimum of the three rates. The Frechet floor on the rate is zero for six models and 2.5 to 8.7 points for Gemma 4, GLM-5.2 and Opus 4.8, so the observed rates are not informative about the lower bound.

Figure: share of dialogues that complete all three requests, among dialogues whose opening request succeeded = all-three-pass / initial rate. This is exact, not an approximation, because every all-pass dialogue has a passing opening request. Same inputs and denominator caveat as above.
Owner:  inputs from Tables 3 and 4; the division is mine.
Scope:  2,620 dialogues per agent.

| Model | Completes all three given opening passed | Independent FU1 x FU2 (for contrast) |
|---|---|---|
| GPT-4o-mini | 38.5% | 28.0% |
| GPT-4.1-mini | 50.1% | 39.6% |
| GPT-5.4-mini | 45.1% | 31.0% |
| Opus 4.8 | 53.3% | 44.9% |
| Qwen3.5-397B | 43.3% | 33.2% |
| Qwen3.6-27B | 44.1% | 34.4% |
| Gemma 4-31B | 49.5% | 41.6% |
| GPT-OSS-120B | 38.2% | 25.2% |
| GLM-5.2-744B | 50.9% | 42.0% |

Reading: even when the opening request succeeds, between 47% (Opus 4.8) and 62% (GPT-OSS-120B) of dialogues still fail at least one follow-up. The "independent FU1 x FU2" column uses unconditional follow-up rates, a baseline and not a measurement of conditional rates.

Figure: opening rate cubed, as a stand-in for what an opening-request evaluation would extrapolate to, against observed all-three-pass.
Owner:  inputs from Tables 3 and 4; arithmetic mine.
Scope:  as above.

| Model | Initial cubed | Observed | Observed minus cubed |
|---|---|---|---|
| GPT-4o-mini | 27.7 | 25.1 | -2.6 |
| GPT-4.1-mini | 31.0 | 33.9 | +2.9 |
| GPT-5.4-mini | 19.1 | 26.0 | +6.9 |
| Opus 4.8 | 41.7 | 39.8 | -1.9 |
| Qwen3.5-397B | 30.9 | 29.3 | -1.6 |
| Qwen3.6-27B | 28.5 | 29.0 | +0.5 |
| Gemma 4-31B | 39.7 | 36.4 | -3.3 |
| GPT-OSS-120B | 27.7 | 24.9 | -2.8 |
| GLM-5.2-744B | 40.7 | 37.7 | -3.0 |

Figure: ranks (1 = best) of the nine models under three orderings, from Table 3 (no ties in any column).
Owner:  Table 3 values; ranks mine. The Spearman figures marked "paper" are the paper's; the others are mine.
Scope:  nine models; one run each.

| Model | Rubric weighted | Task success (pooled) | All-three-pass | Rubric minus task-success rank |
|---|---|---|---|---|
| GPT-4o-mini | 9 | 7 | 8 | +2 |
| GPT-4.1-mini | 4 | 4 | 4 | 0 |
| GPT-5.4-mini | 1 | 8 | 7 | -7 |
| Opus 4.8 | 2 | 1 | 1 | +1 |
| Qwen3.5-397B | 8 | 6 | 5 | +2 |
| Qwen3.6-27B | 5 | 5 | 6 | 0 |
| Gemma 4-31B | 3 | 3 | 3 | 0 |
| GPT-OSS-120B | 6 | 9 | 9 | -3 |
| GLM-5.2-744B | 7 | 2 | 2 | +5 |

Rubric against pooled task success: Spearman 0.23 (paper, reproduced). Rubric against all-three-pass: 0.32 (mine). Pooled against all-three-pass: 0.97 (paper, reproduced). Rubric against task success without GPT-5.4-mini: 0.64, n=8 (mine). Rubric against task success without GPT-OSS-120B, the judge: 0.19, n=8 (mine). Exact two-sided permutation p-value for 0.23 at n=9: 0.55 (mine). Rank of the opening-request rate also tracks all-three-pass closely (Spearman 0.95, mine).

Figure: rubric versus task success for the two models the paper singles out.
Owner:  Table 3 and Appendix F.2 of the paper.
Scope:  GPT-5.4-mini: weighted rubric 0.817 (rank 1), task success 56.3% (rank 8 of 9). Opus 4.8: 0.809 (rank 2), 69.6% (rank 1). GLM-5.2: 0.685 (rank 7), 67.9% (rank 2). Paper: the rubric "places GPT-5.4-mini ahead of Opus 4.8 despite a 13.3-point deficit in task success". The 13.3-point gap is correct (69.6 - 56.3). Problem 140 (Appendix F.2, Table 10): GPT-5.4-mini rubric 0.925 and 0/3 success; Opus 4.8 rubric 0.600 and 3/3 success. In 63 dialogues GPT-5.4-mini scores at least 0.9 on the rubric and fails all three subtasks. Problem 140's environment returns a brand list truncated alphabetically at Lenovo, so Samsung never appears. Opus 4.8 passed by answering from its own knowledge after saying the tool was unreliable, which the paper describes as "a property of the two metrics, not a verdict on which agent behaved correctly".

Figure: one worked series for a single problem (Table 9, problem 2610; follow-ups differ per agent). Initial / FU 1 / FU 2: GPT-4o-mini fail, fail, pass; GPT-4.1-mini fail, pass, pass; GPT-5.4-mini fail, pass, pass; Opus 4.8 fail, pass, fail; Qwen3.5 fail, fail, pass; Qwen3.6 pass, pass, pass; Gemma 4 pass, pass, pass; GPT-OSS fail, fail, fail; GLM-5.2 fail, pass, pass. Rubric overall: 0.55, 0.75, 0.68, 0.80, 0.53, 0.85, 0.80, 0.43, 0.70 in the same model order. The paper's caption: "Follow-up queries differ across agents because each is generated from that agent's own dialogue." Note that failing the opening request does not prevent passing a later one in this problem (seven of nine models), which is the within-dialogue structure the aggregate tables hide, from one problem only.

### Construction details that bear on trust (all ToolTurns paper)

- Problems: 2,620; 1,827 distinct tools; 11,004 distinct endpoints; 47 RapidAPI categories; 1,032 single-tool (39.4%) and 1,588 multi-tool (60.6%, of which 1,023 cross-category); mean 3.4 tools and 26.5 endpoints per problem (medians 3.0 and 15.0) (Table 2). Tools come from ToolBench's RapidAPI collection. Each problem yields exactly one dialogue (section 3.2).
- Opening queries and withheld context were generated by GPT-4o-mini under a template that asks for a deliberately vague request with 2 to 4 concrete withheld keywords (section 3.1). Not written by people (section 6).
- Tool responses come from StableToolBench's cache where available and from an LLM simulation otherwise (sections 3.2 and 6, Appendix F intro: "All tool observations come from StableToolBench's cache or its LLM simulator"). The simulator model for missing responses is Qwen3-32B-AWQ (section 4.1.1: "The same model supplies API responses missing from the StableToolBench cache"). Task success "is defined against that record" (section 6). The paper does not report the share of observations that were cached versus simulated. It reports that placeholder prose appears in only 154 of 70,740 subtasks (0.2%), and a deterministic gate fails 20 (0.03%) (section 3.4.2).
- User simulator: Qwen3-32B-AWQ served through vLLM (section 3.3), with the checker-fixer enabled, answering clarification questions from the withheld context and generating follow-ups. It never sees tool calls or tool responses (Appendix C). Temperatures: 0.7 for follow-up queries, 0.8 for clarification responses. Follow-ups must be "solvable by exactly one operation from api_list" (section 3.3). The checker flags eleven violation types (Table 8).
- Dialogue shape: one opening request and exactly two follow-ups; each main query capped at 10 user-visible messages; agent search loop capped at 15 messages, then one forced synthesis call (Appendix C; section 3.2).
- Judges: all rubric and task-success calls use "gpt-oss at temperature 0.2" (section 4.1.1). The size of that model is not stated, and the Table 3 footnote says GPT-OSS is also the judge model, so one agent is judged by its own family. The task-success judge returns a boolean per subtask, "strict on wrong or missing answers", and sees only that subtask's slice (Appendix G.4: "{query}, {dialogue}, {tool_calls}, and {final_answer} are that subtask's slice only"). Judging prompts are in Appendix G.
- Human validation of the agent judges: Cohen's kappa 0.68 for binary task success ("substantial") and quadratic weighted kappa 0.53 for the five rubric aspects ("moderate") (section 4.2.1). The number of items, annotators and models covered is not stated.
- Human validation of the user simulator: 120 blind pairs of original versus revised turns, revision preferred in 76 (63.3%, 95% CI [54.2, 71.7], two-sided sign test p=4.5e-3), no position bias (Appendix B.3.2). The detector the paper uses for its automatic measure agrees with humans on 68.1% of the 47 pairs where it has a preference (kappa 0.23) and is silent on 73 of 120 (Appendix B.3.3). The paper says its labels "calibrate the automatic measure rather than serve as ground truth" (B.3.1).
- Simulator against human-written dialogues: compared on API-Bank's 622 human-written dialogues using the same LLM judge (GPT-4o-mini) (Appendix B.4, Table 7). Simulated users score 0.851 against 0.772 for the filtered human set. The authors attribute part of the gap to turn count and to a differing assistant and environment, and say the gap is "not as proof that synthetic users are uniformly 'more human'".
- Checker-fixer effect on dialogue-level scores is tiny: user-simulator quality 0.862 without it versus 0.871 with it (Table 5, 322 dialogues). The authors "deliberately do not read the +0.009 margin ... as evidence that the pipeline works" (B.2.2).
- Judge-side defects recorded by the paper: omitted provenance across subtasks (problem 1515, Gemma 4, Appendix F.3), a wrong tool observation (problem 589, Opus 4.8: the tool applied a standard-time offset in late September, the agent corrected it, and the judge failed the subtask against the tool output). The paper keeps "the original success labels" in the reported scores and says the effect on the follow-up declines and the model rankings "remains unquantified" (section 6).
- Statistical reporting: Tables 3 and 4 give no confidence intervals, no seeds and no repeated runs. At n=2,620, a proportion near 40% has a binomial standard error of about 0.96 points, and near 25% about 0.85 points (my arithmetic; the paper does not give it). Adjacent models in all-three-pass (GLM-5.2 at 37.7 and Gemma 4 at 36.4; Qwen3.5 at 29.3 and Qwen3.6 at 29.0) are within what sampling alone could move, although the same problems are used for every agent.

### External figures

Figure: gpt-4o function-calling agent on tau-retail: pass^1 about 61% (abstract and section 1), and a 115-trajectory sample at 65.2% in the failure analysis (section 5.2); pass^8 below 25% (section 5.1, abstract). On tau-airline pass^1 about 35%.
Owner:  tau-bench paper (arXiv 2406.12045).
Scope:  tau-retail, 115 tasks; pass^k is the chance that all k i.i.d. trials of the same task pass. Not turns within a dialogue.

Figure: average performance drop of 39% from single-turn fully-specified to sharded multi-turn across six tasks; mean aptitude loss 16%; mean unreliability increase 112%; Concat control averages 95.1% of the single-turn score.
Owner:  Laban et al. (arXiv 2505.06120), sections 6.1 and 6.2.
Scope:  15 LLMs, six generation tasks, more than 200,000 simulated conversations, 10 simulations per model and instruction, temperature 1.

## Limits

- The joint distribution of the three outcomes is not reported. Table 3 and Table 4 give only marginals, so conditional rates such as the chance of passing follow-up 1 given a failed opening cannot be computed except the one exact quantity above (all-three-pass given opening passed). The paper's repository ("sanitized saved scores", release v1.0.0, https://github.com/milad621/ToolTurns, per the Reproducibility statement) may hold per-dialogue outcomes. I could not open it: this session returned 403 and has no GitHub access to that repository. Treat the address as stated by the paper and not confirmed by me.
- Whether the clustering reflects problem difficulty (a broken tool or a badly specified withheld context affects all three turns, as in problem 140) or an agent-side carry-over of an early failure cannot be separated from the tables. The paper offers both explanations without testing either: "Either some problems are simply harder, or an agent that establishes the right tool and context early tends to keep succeeding" (section 4.1.3).
- No fully specified single-turn control. The paper never runs the same follow-up requests as stand-alone first requests, so the follow-up decline is not shown to come from conversational dependence (the paper says so in section 4.1.3). Laban et al. supply that control in a different setting (Concat versus Sharded).
- Per-position rates can differ in difficulty: follow-ups are generated from each agent's own dialogue (Table 9 caption) and are required to be answerable by one operation, so a follow-up is easier or harder in a way that varies by agent. No per-position difficulty-matched comparison is possible.
- No intervals or repeated runs for any Table 3 or Table 4 value. A test of "observed above independent" needs the per-dialogue data; the 5.8 to 8.4 point gaps are many times the 0.2 to 0.3 point rounding error and roughly six to ten binomial standard errors of the observed rate, but the standard errors of the product and the observed rate are correlated, so I do not offer a significance claim.
- The denominator exclusions ("dialogues and subtasks for which the judge returned an error are excluded", Table 3 note) are not counted in the paper. The arithmetic consistency of Tables 3 and 4 suggests few or none.
- The identity and size of the judge model "gpt-oss" are not stated beyond the footnote that GPT-OSS is also the judge model; whether it is the 120B checkpoint is unknown.
- The human check of the agent judges (kappa 0.68 and 0.53) has no stated sample size.
- Share of tool observations that came from cache versus LLM simulation is not reported.
- Model names and versions (Claude Opus 4.8, GPT-5.4-mini, Qwen3.6-27B, GLM-5.2) are as the paper prints them. I did not verify them elsewhere, and the paper gives no dates, endpoints or API snapshots for the proprietary models.
- tau-bench and Laban et al. do not give per-turn decay inside a fixed-length dialogue, so neither confirms the turn-by-turn pattern. I found no outside benchmark with matched per-turn and per-dialogue tables. I did not read the BFCL multi-turn results or MultiChallenge's body.

## Source assets

Asset: The paper contains no figures or charts, only tables (Tables 1 to 11) and transcripts. The nearest visual-ready material is Table 4 (per-position success, section 4.1.3) and Table 3 (rubric and task success rows, section 4.1.3). Both are numbers to be redrawn from the printed values, not images to crop.
Shows: Table 4: the opening-to-follow-up decline per model; Table 3: the rank disagreement between the rubric aggregate and task success.
Crop:  Not for image reuse. If a table is excerpted, keep the model order, the column headers (Initial, FU 1, FU 2, Delta) and the caption's definition of Delta. Rebuild as a chart from the transcribed values above, citing section 4.1.3.

Asset: Table 9 (Appendix F.1), a nine-agent pass/fail grid for problem 2610, with the rubric score beneath each agent.
Shows: how one dialogue resolves differently per agent, including a model that fails the opening request and passes both follow-ups, and a rubric score that does not track the grid.
Crop:  Keep all nine columns, the three outcome rows and the rubric row, and the caption's note that follow-ups differ by agent. Omit the surrounding transcripts.

Asset: Table 10 (Appendix F.2), five rubric aspects and task success for two agents on problem 140.
Shows: the clearest single case of rubric score and task success pointing in opposite directions (0.925 and 0/3 against 0.600 and 3/3).
Crop:  Keep both rows and all columns; add the explanation that the environment's brand list is truncated at Lenovo.

Asset: tau-bench Figure 4 (pass^k and pass@k curves, tau-retail, section 5.1).
Shows: the drop of success as all k trials must pass, from above 60% at k=1 to below 25% at k=8, against pass@k rising.
Crop:  Cannot be reproduced from the text alone; I did not read values off the figure, so a writer who wants to chart it needs the figure itself or the repository data.

## Discarded

https://github.com/milad621/ToolTurns: could not be opened (403 in this session, not necessarily dead). Address is the paper's own; unverified by me.
https://arxiv.org/abs/2501.17399 (MultiChallenge, Sirdeshmukh et al.): read abstract only; offers a low absolute accuracy (below 50%, best 41.4%) and no per-turn or per-dialogue structure, so it adds nothing to either strand.

## Questions for the orchestrator

1. The paper's repository (release v1.0.0) says it holds "sanitized saved scores". If it has per-dialogue outcomes, it would let the writer report the real joint pass patterns (for example, the share of dialogues in which a failed opening was followed by a pass), which the tables cannot give. The commission says not to reconstruct numbers the paper does not give, so I did not attach it. Do you want me to try, or leave it?
2. The commission calls the per-model independence comparison a computation the paper does not present. The paper does it once, for Opus 4.8 (section 4.1.3). The per-model version and the exact quantity "completes all three, given the opening passed" are mine; the writer should credit the paper for the Opus case. I decided to record both.
3. I treated the commissioned angle ("failures in one turn relate to failures in the next") as supported only in the narrow form above: positive clustering, no direction or mechanism. If the writer is expected to say failures "carry forward", the evidence does not support that.
