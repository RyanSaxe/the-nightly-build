# Commission — paper-of-the-day/knowledge-distillation

## Assignment
Report on **Hinton, Vinyals & Dean, "Distilling the Knowledge in a Neural
Network" (2015, arXiv:1503.02531)** on the `paper` template. Rebuild its central
claim, then weigh it against the public record that followed.

## The claim to reconstruct
A small "student" network can be trained to match a large "teacher" (or
ensemble) by learning from the teacher's *softened* output distribution — the
relative probabilities across wrong classes ("dark knowledge"), exposed by a
temperature-scaled softmax — rather than from hard labels alone. Rebuild the
temperature/softmax mechanics and the MNIST and speech results in the piece's
own words and math, for the house reader (comfortable with softmax, gradients,
logits). Show *why* soft targets could carry more information per example than
one-hot labels.

## Weigh against what happened next (the reason this paper, tonight)
The record complicates the intuition, and that tension is the article's job:
- **Stanton et al., "Does Knowledge Distillation Really Work?" (NeurIPS 2021)**:
  even with capacity to do so, students often fail to match the teacher's
  predictive distribution; fidelity and generalization come apart. This is the
  focal counter-evidence — read it in full.
- Successes that are real: DistilBERT (Sanh et al. 2019), "Born-Again Networks"
  (Furlanello et al. 2018, self-distillation exceeding the teacher), and the
  self-distillation / label-smoothing connections (e.g., Müller et al. 2019 on
  label smoothing and distillation interacting). Use these to bound the verdict.
Land a reviewer's verdict: where the mechanism is understood, where it is
folklore, and what a practitioner should actually expect.

## Reader / register
House reader; teach each term at first use only if the declared reader would not
hold it. Calm, first-principles, build concepts before the sentence needing them
(press voice; Olah/Weng patience where it teaches).

## Mode / template / geometry
- mode `open` · template `paper` · order null.
- words 1800–3400; flex_sections 2–8, each cited; anchors: abstract,
  orientation, sources. The abstract anchor puts the paper's link and its own
  words up front; flex sections carry the reconstruction and the verdict.

## Source obligations
- min_sources 8. Primary = the paper itself and each follow-on paper you weigh
  (read them, not summaries). Verify quoted numbers against the source that owns
  them. Record primary/secondary kind + locator per citation.

## Prevent repetition (recent paper-of-the-day)
Covered and off-limits as subjects: lora, chain-of-thought-prompting,
attention-is-all-you-need, resnet, adam-optimizer, batch-normalization,
lottery-ticket-hypothesis, chinchilla. Several of these use a "the paper's own
table/proof already recorded the limit" opener and a "weigh the claim against
the follow-on" spine — you share the spine (it is the series), so make the
*opener and section shapes* your own, not inherited. No colon-subtitle headline.

## Tonight's neighbors (avoid collision)
tech-news brief (AI news) covers *developments*, not foundational papers — no
overlap. Also: boeing, current-events, nirsevimab, bowdlerize.

## Output paths
- Article: `.nb-work/paper-of-the-day/knowledge-distillation/library/paper-of-the-day/knowledge-distillation.html`
- Artifacts: `.nb-work/paper-of-the-day/knowledge-distillation/agent-artifacts/paper-of-the-day/knowledge-distillation/`

## Runtime for nb-meta
harness `claude-code` · writer `claude-opus-4-8` (capable, high) · editor
inherited `claude-opus-4-8`, high, required.

## Required contribution
The reader leaves knowing when distillation transfers a distribution vs. merely
a smaller working model, and why the 2015 intuition and the 2021 measurement
disagree. An equation or a small comparison table (soft vs. hard targets;
teacher/student fidelity) is welcome where it carries the reasoning.
