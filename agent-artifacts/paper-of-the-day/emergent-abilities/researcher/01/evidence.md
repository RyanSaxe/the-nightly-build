# Evidence — paper-of-the-day/emergent-abilities (01)

Both focal papers were read in full from their arXiv PDFs (text extracted directly, not
summarized secondhand), plus their abstract pages, the NeurIPS award record, one
author's own follow-up commentary, one outside theorist's response, two supporting
primaries (BIG-Bench, GSM8K), and two later arXiv follow-ons. Ten sources total, all
resolving, all read. The evidence is strong on: the exact wording of both abstracts and
definitions; the specific tasks, figures, and FLOPs/parameter thresholds Wei et al. report;
the exact metric taxonomy and the specific arithmetic demonstration Schaeffer et al. run;
and the NeurIPS Outstanding Paper award. It is thin on one thing worth flagging honestly:
Schaeffer et al.'s central arithmetic demonstration (Figure 3) is presented only as plots,
not as a data table — I could not extract exact per-model accuracy or token-edit-distance
values, only the qualitative shape and the metric/task identity. The worked example below
uses the real, named thresholds Wei et al. give (FLOPs, parameters) for the "before" state
and Schaeffer et al.'s described (not tabulated) curve shape for the "after" state. A
writer wanting exact digitized curve values would need to re-derive them from the
figure images themselves, which this record does not attempt.

## Sources

1. **Wei, Tay, Bommasani, Raffel, Zoph, Borgeaud, Yogatama, Bosma, Zhou, Metzler, Chi,
   Hashimoto, Vinyals, Liang, Dean, Fedus, "Emergent Abilities of Large Language Models,"
   arXiv:2206.07682 (v2, revised 26 Oct 2022), published in *Transactions on Machine
   Learning Research*, 08/2022.**
   URL: https://arxiv.org/abs/2206.07682 (abstract page, read) and
   https://arxiv.org/pdf/2206.07682 (full PDF, read in full — 30 pages, extracted with
   PyMuPDF for exact text).
   Kind: **Primary.** This is the paper whose claims the article reconstructs; it owns
   every number and definition attributed to it.
   Establishes: the definition of "emergent ability," the eight few-shot tasks in Figure 2,
   the four augmented-prompting cases in Figure 3, and its own discussion of the metric
   explanation (Section 5.1) — the paper anticipates and partially rebuts the argument
   Schaeffer et al. later make.
   Locators: Abstract (p.1); definition, Section 2 (p.2); Figure 2 and BIG-Bench
   discussion, Section 3 (pp.3–4); Figure 3 and augmented-prompting discussion, Section 4
   (pp.4–5); Table 1 (p.5); Section 5.1 "Potential explanations of emergence" (pp.6–7);
   Section 5.4 "Emergent risks" (p.8).

2. **Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a
   Mirage?", arXiv:2304.15004 (v2, revised 22 May 2023), NeurIPS 2023 (Outstanding Paper
   Award, "Outstanding Main Track Papers" category).**
   URL: https://arxiv.org/abs/2304.15004 (abstract page, read) and
   https://arxiv.org/pdf/2304.15004 (full PDF, read in full — 14 pages, extracted with
   PyMuPDF).
   Kind: **Primary.** Owns the mirage/metric-artifact claim and its own experiments.
   Establishes: the metric taxonomy (nonlinear/discontinuous vs. linear/continuous), the
   mathematical model, the InstructGPT/GPT-3 arithmetic demonstration, the BIG-Bench
   meta-analysis, and the vision-task demonstration. Its Discussion section explicitly
   limits its own claim.
   Locators: Abstract (p.1); metric definitions and Figure 2 (mathematical model), Section
   2 (pp.2–3); three predictions and GPT-3/InstructGPT arithmetic test, Section 3, Figure 3
   and Figure 4 (pp.4–6); BIG-Bench meta-analysis, Section 4, Figure 5 and Figure 6 (p.6);
   vision-task demonstration, Section 5 (pp.6–7); Discussion (p.9); reference list confirms
   citation to Wei et al. as reference [33] and to Anderson's "More Is Different" as [1].

3. **NeurIPS, "Announcing the NeurIPS 2023 Paper Awards" (blog post, 11 Dec 2023).**
   URL: https://blog.neurips.cc/2023/12/11/announcing-the-neurips-2023-paper-awards/
   (read).
   Kind: **Primary** for the award claim — NeurIPS is the awarding body, so this is the
   institution's own record, not a secondhand report of it.
   Establishes: "Are Emergent Abilities of Large Language Models a Mirage?" by Rylan
   Schaeffer, Brando Miranda, and Sanmi Koyejo is listed under the category "Outstanding
   Main Track Papers," published 11 Dec 2023.

4. **NeurIPS 2023 virtual program, poster page for paper 72117.**
   URL: https://neurips.cc/virtual/2023/poster/72117 (read).
   Kind: **Primary** — the conference's own program record, corroborating source 3.
   Establishes: same award ("Outstanding Paper"), authorship, and that the paper was
   presented as a 2023 oral/poster session. Used as a second, independent confirmation of
   the award from the awarding body's own infrastructure (not a second retelling of the
   same claim by an outside party).

5. **Jason Wei, "Common arguments regarding emergent abilities," personal blog, dated
   "May 3" (internal content — direct response to arguments raised after Schaeffer et
   al.'s April 2023 preprint — places it as 2023).**
   URL: https://www.jasonwei.net/blog/common-arguments-regarding-emergent-abilities
   (read).
   Kind: **Primary** for Wei's own position on the debate — he is the lead author of
   source 1, and this is his direct, first-person response to the metric-choice argument,
   not a third party's characterization of his view.
   Establishes: Wei's explicit acknowledgment of the metric argument ("if you plot ...
   log-probability of the target sequence, performance improves smoothly") and his
   rebuttal that the practically useful metric is the discontinuous one: "you want the
   answer to be 38, and nothing else. Maybe 37 is closer to 38 than -2.591, but assigning
   some partial credit to that answer seems unhelpful." He also states he has "not seen
   any substantial evidence that exact-match or multiple-choice performance can be
   predicted using smooth surrogate metrics," and that "there seems to be an overwhelming
   amount of evidence of emergent abilities that (for me) makes it a convincing
   phenomenon."
   Locator: main body of the post, the arithmetic-example paragraph and the closing
   assessment paragraph (post is short, unpaginated).

6. **Boaz Barak, "Emergent abilities and grokking: Fundamental, Mirage, or both?",
   Windows on Theory (blog), 22 Dec 2023.**
   URL: https://windowsontheory.org/2023/12/22/emergent-abilities-and-grokking-fundamental-mirage-or-both/
   (read).
   Kind: **Secondary** — Barak is an outside ML theorist (not an author of either focal
   paper) analyzing both from a distance.
   Establishes: a third position that changes the interpretation rather than repeating
   either paper's claim. Barak agrees the metric-swap argument is real ("If we use a
   different metric for the task performance, then instead of an abrupt and unpredictable
   'jump,' we could get a smooth and predictable improvement") but argues it does not
   fully dissolve emergence for tasks built from sequential sub-steps, because "even if we
   can precisely predict the loss of a model trained using N flops, we may not be able to
   predict which tasks it would solve beyond those solvable by an N/10 flop model" — a
   probability-of-all-substeps-succeeding argument independent of metric choice.

7. **Srivastava, Rastogi, Rao, et al. (450+ authors, ~132 institutions), "Beyond the
   Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models,"
   arXiv:2206.04615.**
   URL: https://arxiv.org/abs/2206.04615 (read).
   Kind: **Primary** for facts about BIG-Bench itself (the benchmark's own paper).
   Establishes: BIG-Bench comprises 204 tasks (Wei et al.'s "over 200 benchmarks" is
   consistent with this), drawing problems "from linguistics, childhood development, math,
   common-sense reasoning, biology, physics, social bias, software development, and
   beyond"; the paper's own finding that model performance is "poor in absolute terms" and
   that some tasks show sudden breakthroughs at scale while knowledge-heavy tasks improve
   gradually — this is the source BIG-Bench task performance data in both focal papers
   draws on.

8. **Cobbe, Kosaraju, Bavarian, Chen, Jun, Kaiser, Plappert, Tworek, Hilton, Nakano,
   Hesse, Schulman, "Training Verifiers to Solve Math Word Problems," arXiv:2110.14168.**
   URL: https://arxiv.org/abs/2110.14168 (read).
   Kind: **Primary** for facts about GSM8K itself.
   Establishes: GSM8K is "8.5K high quality linguistically diverse grade school math word
   problems"; the paper's own statement that "even the largest transformer models fail to
   achieve high test performance, despite the conceptual simplicity of this problem
   distribution" — this is the benchmark Wei et al.'s Figure 3A (chain-of-thought vs.
   standard prompting) is evaluated on.

9. **Snell, Wallace, Klein, Levine, "Predicting Emergent Capabilities by Finetuning,"
   arXiv:2411.16035 (submitted 25 Nov 2024).**
   URL: https://arxiv.org/abs/2411.16035 (read).
   Kind: **Secondary/follow-on** — a later, independent research group's work that treats
   emergence as a real, task-level phenomenon still worth predicting, rather than
   revisiting the metric question directly.
   Establishes: that "finetuning LLMs on a given task can shift the point in scaling at
   which emergence occurs towards less capable models," and that "emergence laws" fit to
   finetuning curves on MMLU, GSM8K, CommonsenseQA, and CoLA can forecast when a benchmark
   score will cross a threshold "up to 4x the FLOPs in advance" — evidence the field kept
   treating discontinuous-metric emergence as a real target to predict even after the
   mirage paper, rather than treating it as dissolved.

10. **Vladimír Havlík (Czech Academy of Sciences), "Why are LLMs' abilities emergent?",
    arXiv:2508.04401 (submitted 6 Aug 2025).**
    URL: https://arxiv.org/abs/2508.04401 (read).
    Kind: **Secondary** — a later philosophy-of-science analysis by a party outside both
    original research groups.
    Establishes: as of mid-2025 the debate has not settled by consensus. The paper argues
    "current debates over metrics, pre-training loss thresholds, and in-context learning
    miss the fundamental ontological nature of emergence in DNNs," proposing DNNs be read
    as complex dynamical systems with "genuine emergent properties analogous to those
    found in other complex natural phenomena." Useful as evidence the metric argument did
    not end discussion of whether emergence is "real" — it shifted the discussion's terms.

### Attempted, not used

The OpenReview page for Wei et al. (linked from the paper's own PDF header as
`https://openreview.net/forum?id=yzkSU5zdwD`) returned only a bot-verification
interstitial on fetch — gated, not read, so nothing from it is cited. The TMLR venue and
year are instead sourced directly from the published PDF's own running header ("Published
in Transactions on Machine Learning Research (08/2022)"), which is primary and sufficient.

## The abstract, verbatim

Paper: **Wei, Jason; Tay, Yi; Bommasani, Rishi; Raffel, Colin; Zoph, Barret; Borgeaud,
Sebastian; Yogatama, Dani; Bosma, Maarten; Zhou, Denny; Metzler, Donald; Chi, Ed H.;
Hashimoto, Tatsunori; Vinyals, Oriol; Liang, Percy; Dean, Jeff; Fedus, William.**
"**Emergent Abilities of Large Language Models.**" *Transactions on Machine Learning
Research*, 08/2022. arXiv:2206.07682.
Read the paper: https://arxiv.org/abs/2206.07682

> Scaling up language models has been shown to predictably improve performance and sample
> efficiency on a wide range of downstream tasks. This paper instead discusses an
> unpredictable phenomenon that we refer to as emergent abilities of large language
> models. We consider an ability to be emergent if it is not present in smaller models but
> is present in larger models. Thus, emergent abilities cannot be predicted simply by
> extrapolating the performance of smaller models. The existence of such emergence raises
> the question of whether additional scaling could potentially further expand the range of
> capabilities of language models.

Extracted character-for-character from the arXiv PDF (`arxiv.org/pdf/2206.07682`, page 1)
using direct text extraction, not a web summarizer. Note: an earlier, lower-fidelity
web-summary pass mis-rendered the final sentence as "...implies that additional scaling
could further expand the range of capabilities..." — the PDF's actual wording is "...raises
the question of whether additional scaling could potentially further expand the range of
capabilities...". Use the block above; the wording matters (it hedges, it doesn't assert).

## Verified facts, quotes, and locators

### Wei et al. — the emergence claim

- Working definition, given twice in near-identical form: "An ability is emergent if it is
  not present in smaller models but is present in larger models." (Section 2, p.2) The
  paper also opens with a broader borrowed definition: "Emergence is when quantitative
  changes in a system result in qualitative changes in behavior," attributed to
  "Steinhardt (2022) and rooted in a 1972 essay called 'More Is Different' by Nobel
  prize-winning physicist Philip Anderson." (Section 1, p.2)
- Scale is measured on the x-axis as training FLOPs, with parameter-count plots given as a
  secondary view in an appendix (Figure 11, Figure 12), because "most dense Transformer
  language model families have scaled training compute roughly proportionally with model
  parameters." (Section 2, p.2)
- The paper explicitly disclaims predicting *which* scale triggers emergence for a given
  ability: "Our goal in this paper is not to characterize or claim that a specific scale is
  required to observe emergent abilities, but rather, we aim to discuss examples of
  emergent behavior in prior work." (Section 2, p.3)
- Figure 2 shows "eight examples of emergence in the few-shot prompting setting," spanning
  five model families (GPT-3, LaMDA, Gopher, Chinchilla, PaLM): (A) modular/arithmetic
  (BIG-Bench 3-digit add/subtract, 2-digit multiply), (B) IPA transliteration, (C) word
  unscramble, (D) Persian question-answering — A–D all from BIG-Bench, 2-shot; (E)
  TruthfulQA; (F) grounded conceptual mappings; (G) MMLU; (H) Word in Context (WiC).
  (Section 3, pp.3–4)
- Figure 3 shows four "augmented prompting or finetuning" cases treated as emergent: (A)
  chain-of-thought prompting on GSM8K math word problems (source: Wei et al. 2022b, the
  separate CoT paper), (B) instruction-tuning on a 10-task NLU average, (C) a "scratchpad"
  technique on 8-digit addition, (D) a True/False self-evaluation calibration technique.
  (Section 4, pp.4–5)
- Section 5.1 anticipates the metric objection directly: "It is also important to consider
  the evaluation metrics used to measure emergent abilities... using exact string match as
  the evaluation metric for long-sequence targets may disguise compounding incremental
  improvements as emergence." But it argues this "is at best an incomplete explanation,
  because emergent abilities are still observed on many classification tasks (e.g., the
  tasks in Figure 2D–H)" — i.e., Wei et al. pre-empt the partial-credit argument for
  multi-step generation tasks, but assert it doesn't explain sharp jumps on tasks already
  scored by classification-style accuracy. (Section 5.1, p.6-7) This is the exact seam
  Schaeffer et al. later cut into, by showing that classification-style metrics
  (Multiple Choice Grade) are *themselves* discontinuous.
- Section 5.4 ("Emergent risks") notes societal risks (truthfulness, bias, toxicity) "do
  increase with model scale (see the Inverse Scaling Prize)" and that risk emergence is a
  distinct, non-capability concern from the paper's main claim. (p.8)

### Schaeffer et al. — the mirage claim

- The paper's own framing of what makes emergence "intriguing": "their sharpness,
  transitioning seemingly instantaneously from not present to present, and their
  unpredictability, appearing at seemingly unforeseeable model scales." (Abstract, p.1)
- Metric taxonomy, given as formal definitions: **Multiple Choice Grade** = 1 if the
  correct option has the highest probability mass, else 0 (discontinuous, step-function
  like); **Exact String Match** = 1 if the output string exactly matches the target
  string, else 0 (nonlinear in per-token error rate). Continuous/linear counterexamples
  used to "ablate" the emergent appearance: **Token Edit Distance** (counts wrong tokens,
  scales roughly linearly with per-token error) and **Brier Score** (mean-squared error
  between predicted probability and outcome, for classification tasks). (Section 1 and
  Section 2, pp.1–3)
- Central claim in the paper's own words: "for a particular task and model family, when
  analyzing fixed model outputs, emergent abilities appear due [to] the researcher's
  choice of metric rather than due to fundamental changes in model behavior with scale."
  (Abstract, p.1, and restated Section 1, p.2)
- Explicit self-limitation, in the Discussion: "We emphasize that nothing in this paper
  should be interpreted as claiming that large language models cannot display emergent
  abilities; rather, our message is that previously claimed emergent abilities in [Brown
  et al. 2020; Ganguli et al. 2022; BIG-Bench 2022; Wei et al. 2022] might likely be a
  mirage induced by researcher analyses." (Section 6/Discussion, p.9) This is the
  sentence that keeps the mirage paper from being an "emergence isn't real" claim — it is
  narrower than that.
- BIG-Bench meta-analysis: of "39 preferred metrics in BIG-Bench, at most 5 display
  emergence" by an automated emergence score; hand-annotation (citing the BIG-Bench
  authors' own annotation) narrows this to "4/39 metrics," and "2 metrics account for
  >92% of claimed emergent abilities": Multiple Choice Grade and Exact String Match.
  (Section 4, p.6, Figure 5A–C)
- Multiple-comparisons argument: "In BIG-Bench alone, there are ≥220 tasks, ∼40 metrics
  per task, ∼10 model families, for a total of ∼10^6 task-metric-model family triplets" —
  used to argue that some triplets showing an apparent jump "by random chance" is
  expected even absent any real effect. (Discussion, p.9)
- LaMDA demonstration: emergent abilities visible under the discontinuous Multiple Choice
  Grade on certain BIG-Bench tasks "disappeared when we changed the metric to the
  continuous Brier Score." (Section 4, Figure 6, p.6)
- InstructGPT/GPT-3 arithmetic demonstration (the article's best worked example
  candidate): tested on "2-shot multiplication between two 2-digit integers and 2-shot
  addition between two 4-digit integers." Under Accuracy, "the GPT family displays
  emergent abilities if the target has 4 or 5 digits"; switching to Token Edit Distance
  "while keeping the models' outputs fixed," the family's "performance smoothly,
  continuously and predictably improves with increasing scale." A second, independent
  test — collecting more test data to raise measurement resolution — found "all models in
  the InstructGPT/GPT-3 family achieve above-chance accuracy" even on the raw Accuracy
  metric, meaning small models were never truly at zero, just under-sampled. (Section 3,
  pp.4–5, Figure 3 and Figure 4) **Caveat:** these results are given as figures, not
  tables; no exact percentage-by-model values are stated in the running text.

### Points of agreement (both papers)

- Both cite the same intellectual lineage for "emergence": Philip Anderson's 1972 "More
  Is Different." Schaeffer et al. quote Wei et al.'s definition verbatim and attribute it
  correctly ("crisply defined as 'abilities that are not present in smaller-scale models
  but are present in large-scale models...'" — Schaeffer Section 1, p.1, quoting Wei
  Section 2 word for word).
- Both plot scale primarily as training FLOPs / parameter count on a log x-axis.
- Both treat BIG-Bench as the largest single evidence base for emergent-ability claims.
- Neither claims metric choice explains *why* a threshold falls where it does; Wei et al.
  say so explicitly (Section 5.1, "this analysis does not explain why downstream metrics
  are emergent or enable us to predict the scale at which emergence occurs"), and
  Schaeffer et al.'s own framework only explains the *shape* of the curve, not the
  location of the threshold in FLOPs.

## Contradictions

- **Direct tension, not a flat contradiction:** Wei et al. anticipate and reject the
  metric explanation as "at best an incomplete explanation" *because* it doesn't cover
  classification tasks like Figure 2D–H (Section 5.1). Schaeffer et al.'s central
  BIG-Bench result is built specifically from classification-style metrics (Multiple
  Choice Grade is a classification metric) and claims to explain >92% of BIG-Bench's
  claimed emergent cases with exactly two metrics, one of which is a classification
  metric — directly contradicting Wei et al.'s premise that classification tasks are
  metric-explanation-proof.
- **Barak vs. Schaeffer, unresolved:** Barak (source 6) accepts the metric-swap
  mechanism as real but argues it cannot be the whole story for tasks requiring several
  correct sub-steps in sequence, since the probability all sub-steps succeed can still
  produce a sharp aggregate curve even if each sub-step's probability rises smoothly.
  Schaeffer et al. do not address multi-step compounding directly; their mathematical
  model (Section 2) treats a single per-token error rate, not a chain of independent
  sub-task successes. This is a live gap, not something either focal paper resolves.
  Wei et al.'s own scratchpad/8-digit-addition example (Figure 3C) is exactly this kind
  of multi-step task, which neither paper's math fully covers.
  Wei et al.'s own CoT example (GSM8K, multi-step) is also this kind, unaddressed by
  Schaeffer's single-token-error model.
- **Jason Wei's post-hoc response (source 5) does not concede the practical point:** he
  argues the discontinuous metric (exact match) is the one that matters for real use ("you
  want the answer to be 38, and nothing else"), so demonstrating a smooth surrogate exists
  doesn't remove the practical unpredictability of *when the metric that matters* crosses
  a threshold. This is a values disagreement about which metric should count, layered on
  top of the empirical disagreement about whether emergence is a metric artifact.

## Numbers

| Number | Owning primary | Exact reading | Unit / denominator | Period / context |
|---|---|---|---|---|
| Emergent threshold, BIG-Bench 3-digit add/subtract & 2-digit multiply (GPT-3) | Wei et al., Fig. 2A, Table 1 | 2×10^22 (≈2.3×10^22 per Table 1) | training FLOPs | 13B parameters |
| Same task, LaMDA | Wei et al., Fig. 2A | ~1×10^23 | training FLOPs | 68B parameters |
| TruthfulQA jump | Wei et al., §3, Fig. 2E | 5×10^23 FLOPs, >20 percentage points above random | training FLOPs / accuracy pts | Gopher, 280B params |
| MMLU (57-topic avg) surpasses random | Wei et al., §3, Fig. 2G | 3–5×10^23 | training FLOPs | 70B–280B params, GPT-3/Gopher/Chinchilla |
| Word in Context (WiC) first above-random | Wei et al., §5, Fig. 2H | 2.5×10^24 | training FLOPs | PaLM, 540B params (GPT-3/Chinchilla failed at ~5×10^23) |
| CoT prompting surpasses standard prompting, GSM8K | Wei et al., §4, Fig. 3A | 10^23 | training FLOPs | ~100B params, LaMDA |
| Instruction-tuning helps (vs. hurts below) | Wei et al., §4, Fig. 3B | hurts ≤7×10^21 (8B params); helps at 10^23 (~100B params) | training FLOPs | LaMDA |
| Scratchpad helps, 8-digit addition | Wei et al., §4, Fig. 3C | ≥9×10^19 | training FLOPs | ~40M params |
| True/False calibration superiority | Wei et al., §4, Fig. 3D | ~3×10^23 | training FLOPs | 52B params, Anthropic model |
| BIG-Bench task count | Srivastava et al., Abstract | 204 (Wei et al. round to "over 200") | tasks | as of 2022 paper |
| GSM8K size | Cobbe et al., Abstract | 8.5K | grade-school math word problems | 2021 |
| BIG-Bench metrics showing any automated emergence | Schaeffer et al., §4, Fig. 5A | at most 5 of 39 | preferred metrics | BIG-Bench, hand-checked by emergence-score formula |
| BIG-Bench metrics showing hand-annotated emergence | Schaeffer et al., §4, Fig. 5B | 4 of 39 | preferred metrics | same dataset |
| Share of claimed emergent abilities under 2 metrics | Schaeffer et al., §4, Fig. 5C | >92% | share of hand-annotated emergent BIG-Bench cases | Multiple Choice Grade + Exact String Match combined |
| BIG-Bench task-metric-model triplets (multiple-comparisons argument) | Schaeffer et al., Discussion | ≥220 tasks × ~40 metrics × ~10 model families ≈ 10^6 | triplets | used to argue false positives are statistically expected |
| Emergence laws predict capability crossing | Snell et al. 2024, Abstract | "up to 4x the FLOPs in advance" | forecast horizon | MMLU, GSM8K, CommonsenseQA, CoLA finetuning curves |

Full curve series: neither focal paper publishes the underlying per-model numeric series
as a table; all of the above are threshold/summary statistics stated in running text or
figure captions. A chart reconstructing Wei et al. Figure 2A or Schaeffer et al. Figure 3
would need to be built from the described shape (near-zero/random performance for many
orders of magnitude, then a jump at the stated threshold under Accuracy; a smoothly rising
line under Token Edit Distance) rather than digitized point values, which this record does
not have.

## Concrete worked example (for the draft)

**Task:** integer arithmetic — BIG-Bench's 3-digit addition/subtraction and 2-digit
multiplication task (Wei et al., Fig. 2A) and the closely related 2-shot 2-digit
multiplication / 4-digit addition tasks Schaeffer et al. run directly on the
InstructGPT/GPT-3 family (Schaeffer et al., §3).

**Before (Wei et al., discontinuous metric — exact-match Accuracy):** GPT-3 sits at
"close-to-zero performance for several orders of magnitude of training compute," then
performance "jumps to sharply above random" at 2×10^22 training FLOPs, i.e., the 13B
parameter model (Wei et al., §3, Table 1). Read cold, this looks like the ability to do
3-digit arithmetic switches on at a threshold.

**After (Schaeffer et al., same task family, continuous metric — Token Edit Distance):**
holding the model outputs fixed and re-scoring the identical GPT-3/InstructGPT outputs
with Token Edit Distance instead of Accuracy, "the family's performance smoothly,
continuously and predictably improves with increasing scale" (Schaeffer et al., §3, p.5,
Fig. 3 bottom row). The same models, the same generated text, a different scoring rule —
and the cliff becomes a slope.

**Second confirmation (statistics, not metric):** re-running Accuracy itself with more
test examples (to raise measurement resolution) shows "all models in the
InstructGPT/GPT-3 family achieve above-chance accuracy" even under Accuracy — the small
models were never exactly zero, they were just under-sampled at the original BIG-Bench
test-set size (Schaeffer et al., §3, p.5, Fig. 4).

**What this shows and doesn't show:** it demonstrates the metric-swap and
statistics-resolution mechanisms concretely on a real task with real thresholds. It does
not, by itself, resolve whether a practitioner who only ever gets to use Accuracy (because
that's what the deployed product needs — an exact right answer) still faces a genuinely
unpredictable threshold in FLOPs for when accuracy becomes usable. That is exactly the
point Jason Wei's response (source 5) presses.

## Source assets

- **Wei et al. Figure 2** (BIG-Bench arithmetic, IPA transliteration, word unscramble,
  Persian QA, TruthfulQA, grounded mappings, MMLU, WiC — 8 panels): shows the sharp-curve
  shape across five model families on one page. Best single image for establishing "here
  is what an emergent curve looks like" before the metric argument is introduced. Location:
  arXiv:2206.07682, p.3–4 (Section 3). A crop must keep the axis labels (training FLOPs,
  log scale) and the "Random" baseline line — without them the near-flat-then-jump shape
  reads as decorative rather than as evidence of the threshold claim. Cannot be
  reproduced verbatim without republishing the original figure; a chart built from the
  described threshold values (per the Numbers table above) is the compliant substitute.
- **Schaeffer et al. Figure 3** (Accuracy vs. Token Edit Distance, same GPT-3/InstructGPT
  arithmetic outputs, top/bottom rows): the single figure that makes the mirage argument
  visually undeniable — same models, same outputs, two metrics, two very different
  curve shapes. Location: arXiv:2304.15004, p.5 (Section 3). A crop or redrawn version
  must keep both rows together (top = Accuracy, bottom = Token Edit Distance) and the
  shared x-axis (Model Parameters, log scale) — showing only one row loses the entire
  argument.
- **Schaeffer et al. Figure 6** (LaMDA, Multiple Choice Grade vs. Brier Score): a second,
  independent instance of the same metric-swap effect, on a different model family and a
  BIG-Bench-native metric pair rather than a hand-built one. Location: arXiv:2304.15004,
  p.6 (Section 4). Useful as a second confirming image if the arithmetic pair alone feels
  like a single cherry-picked case.
- Wei et al. Figure 3A (chain-of-thought on GSM8K) and Table 1 (full list of emergent
  abilities and their thresholds): Table 1 in particular is a strong candidate for a
  redrawn table or annotated excerpt, since it is the paper's own inventory of every
  threshold claim in one place. Location: arXiv:2206.07682, p.5.
- None found beyond the papers' own figures for the "afterlife" sources — Barak's post,
  Jason Wei's blog post, and the two 2024–2025 follow-ons are text-only with no
  chartable data of their own.

## Discarded

- An initial `WebFetch` pass on the Schaeffer et al. abstract page returned a paraphrase
  rather than the verbatim text (it introduced quotation marks around invented phrases).
  Rejected in favor of extracting the exact text from the arXiv PDF directly with PyMuPDF;
  the verbatim abstract quoted in this record is Wei et al.'s (the paper the article
  needs verbatim for its paper card), independently confirmed against the PDF text.
- The OpenReview forum page for Wei et al. (`openreview.net/forum?id=yzkSU5zdwD`) was
  attempted for independent venue/certification confirmation but returned only a
  bot-verification interstitial — gated, not read, not cited. The venue claim instead
  rests on the PDF's own running header, which is primary and unambiguous.
- Search results surfaced a CSET explainer, a Medium post ("Emergent Properties in Large
  Language Models"), and a "World Scholars Review" overview article on emergent
  abilities. None were opened past the search-result title/snippet, so none are cited or
  counted among the ten sources above — per the house rule against recording an unread
  URL.
