# Commission — paper-of-the-day/emergent-abilities

## Assignment
One Paper of the Day on **"Emergent Abilities of Large Language Models"** (Wei et
al., 2022; TMLR / arXiv:2206.07682), reconstructed and then weighed against its
most important post-publication record: **"Are Emergent Abilities of Large
Language Models a Mirage?"** (Schaeffer, Miranda, Koyejo; NeurIPS 2023 best
paper; arXiv:2304.15004), plus the follow-on discussion.

## Angle / required contribution
The Wei paper made "emergence" a load-bearing word in how the field talks about
scale: certain abilities are reported as absent in smaller models and appearing
sharply, unpredictably, once a model crosses a scale threshold. The Schaeffer
rebuttal argues those sharp curves are largely manufactured by the *metric*:
discontinuous, all-or-nothing scoring (exact-match, multiple-choice accuracy)
turns smooth, predictable per-token improvement into an apparent cliff, and
under continuous metrics (token edit distance, Brier score) the same tasks
improve smoothly.

The article's job is not to announce either paper. It is to rebuild the claim
carefully enough that the reader can see exactly where the two papers actually
disagree and where they do not — and to weigh it against what happened next.
The clarifying synthesis (hold it to the higher bar the house asks of a
crowd-pleasing read): "emergence" bundled a real thing (capability improves with
scale) with a measurement artifact (the choice of a discontinuous metric makes
the improvement look like a discontinuity). Name precisely what is artifact and
what survives — e.g. that practical *unpredictability* of when a given
benchmark's exact-match score crosses a usefulness threshold is not fully
dissolved by switching metrics, and that "emergence" as an existence claim about
model internals was never what Wei et al. measured. Rebuild at least one concrete
example (a specific BIG-Bench task or GSM8K few-shot) showing the metric effect
with real numbers.

## Reader
Paper's declared reader: math/CS background, ML-engineering career, well-read.
Assume they know what a language model, few-shot prompting, and a benchmark are.
Define BIG-Bench, the specific metrics, and any term the argument spends.

## Mode / template / paths
- Series `paper-of-the-day`, mode `open`, template `paper`.
- nb-meta: `mode: "open"`, `order: null`, `date: "2026-07-31"`.
- Article: `library/paper-of-the-day/emergent-abilities.html`. Words 1800-3400.
- Flex sections 2-8; last flex section lands the reconstruction's verdict.
- The `abstract` section carries the `nb-paper-card`: focal paper title as
  published, authors, venue/arXiv id, year, "Read the paper" link, and the
  abstract **verbatim** (cited).

## Source obligations
- Template floor: **min 8 sources**, all read and resolving.
- Primary sources own the claims: the two arXiv papers themselves (Wei et al.;
  Schaeffer et al.) are primary for their own claims. Secondary = analyses,
  blog treatments, later surveys, citation counts.
- The focal paper owns its claims; another source earns space only when it
  changes the interpretation. Do not let secondary coverage replace the papers
  or pad the list.
- Anchor the turning points with honest `data-nb-locator`/`data-nb-note` on the
  cites (section/figure/page), and quote an exact sentence only when it earns
  display space (`nb-excerpt`).

## Starting sources (verify each; do not cite unread)
- Wei et al., "Emergent Abilities of Large Language Models," arXiv:2206.07682
  (TMLR 2022). Abstract verbatim, the definition of emergence used, the figures.
- Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of LLMs a Mirage?",
  arXiv:2304.15004 (NeurIPS 2023). The metric argument, the specific
  continuous-vs-discontinuous demonstrations, the InstructGPT/GPT-3 tasks used.
- Follow-on that lets the article weigh the claim against what happened next:
  e.g. later commentary, the NeurIPS best-paper designation, any rebuttal or
  defense of the mirage paper, subsequent surveys on scaling/predictability.
- BIG-Bench (Srivastava et al.) and/or GSM8K (Cobbe et al.) for the concrete
  task example.

## Relevant prior coverage (do not repeat)
paper-of-the-day has covered: knowledge-distillation, lora, chain-of-thought
(7/28), attention, resnet, adam, batch-norm, lottery-ticket, chinchilla (7/22).
- Do NOT re-argue compute-optimal scaling (chinchilla's ground) or CoT prompting
  mechanics (chain-of-thought's ground). This piece is about the *shape* of the
  capability-vs-scale curve and whether "emergence" names a real discontinuity.
- The recent run leans on the "the paper's own table/figure already recorded the
  catch" reveal and "the field still has no agreed account" closers. Do not reuse
  those framings as a formula.

## Structures NOT to repeat
No "Background / Method / Results / Verdict" scaffold. Name flex sections for the
steps of *this* reconstruction. Vary the opener from the recent library (avoid
"N years later, follow-on work shows exactly where…" as a stock opening).

## Neighboring articles tonight
current-events, tech-news (AI news of the day), expert-tools (files-to-prompt),
investing (return on capital), unbiased, word-of-the-day (shibboleth). This is
the edition's deepest technical read; it should not duplicate tech-news's
day-of-the-week AI items. Keep it about the 2022 paper and its afterlife.

## Harness / model (balanced profile)
coach sonnet/low; researcher sonnet/high; writer sonnet/medium; editor
opus/high. nb-meta `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Publication bar
8+ real read sources; verbatim abstract with a resolving link; a faithful
reconstruction with at least one worked metric example; an honest verdict that
separates artifact from real phenomenon; 1800-3400 words; `nb check` BLOCK: 0;
editor DONE with no required change.
