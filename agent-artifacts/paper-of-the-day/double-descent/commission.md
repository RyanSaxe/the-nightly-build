# Commission: paper-of-the-day/double-descent

## Assignment
- Series: paper-of-the-day (Paper of the Day). Template: `paper`. Mode: open.
- Slug: `double-descent`. Papers: **Belkin, Hsu, Ma & Mandal, "Reconciling
  modern machine-learning practice and the classical bias–variance trade-off"
  (PNAS 2019, arXiv:1812.11118)** as the primary claim, with **Nakkiran, Kaplan,
  Bansal, Yang, Barak & Sutskever, "Deep Double Descent" (2019,
  arXiv:1912.02292)** as the deep-network extension.
- Authorized by the 2026-08-03 `nb duty` result. One article only.
- Re-pick: the first choice (chinchilla) collided with an already-published
  slug. Confirmed NOT published: double-descent is absent from the library's
  paper-of-the-day slugs.

## Why these papers
They clarify an active problem — why massively over-parameterized models
generalize despite classical bias–variance intuition. Belkin et al. show the
test-risk "double descent" curve: risk rises to a peak at the interpolation
threshold, then falls again as capacity grows past it. Nakkiran et al.
generalize it to deep nets and along model size, epochs, and dataset size, and
tie it to an "effective model complexity." The public after-record is genuine
and contested: the effect's dependence on label noise, whether/when it appears
in practice, and later analyses of its mechanism. That record is what makes
this a reconstruction, not an announcement.

## Required contribution
Rebuild the central claim with the papers' own artifacts:
- Bring in the figures the claim turns on as SOURCE ASSETS (`nb asset` from the
  arXiv/PDF): the double-descent risk curve (Belkin Fig. 1/2) and Nakkiran's
  model-wise / epoch-wise / sample-wise curves, with captions and prose that
  say what each settles. Only use a figure whose argument the article spends.
- Set the math the reconstruction leans on (the interpolation threshold /
  parameters vs. samples, effective model complexity) with the equation
  furniture rather than paraphrase; at most one annotated equation.
- Weigh the claim against the after-record: the role of label noise, when the
  curve does and doesn't appear, and any serious critique or refinement.
  Steelman the effect and its skeptics; keep reported fact, estimate, and
  synthesis distinct.

## Sources
- min_sources: 8 (paper template floor). Primary: Belkin et al. and Nakkiran
  et al. (each owns its own claims/figures); include a serious critique or
  follow-on analysis as its own primary. Secondary reporting only for context.
  Cite figures with `data-nb-locator`/`data-nb-url` to the exact figure/page.
  Every URL must resolve.

## Neighbors in this edition
tech-news/2026-08-03 may touch AI releases; keep this piece about the 2018-2019
papers and their aftermath, not today's news. expert-tools/serena and the
briefs also touch AI — keep this a research reconstruction.

## Prior coverage — do not repeat, and break these shapes
Published papers include: adam-optimizer, attention-is-all-you-need,
batch-normalization, chain-of-thought-prompting, chinchilla, emergent-abilities,
grokking, knowledge-distillation, lora, lottery-ticket-hypothesis, resnet,
word2vec. The "follow-up work disagrees" catalog framing was used for grokking
and emergent-abilities; do not copy that device or its dek molds. Note that
grokking (a related over-fitting-then-generalizing phenomenon) is already
published — reference it only if the argument needs it, and do not retread it.
Vary heading shapes.

## Form
Paper template: abstract card + link up front, then 2-8 flexible sections
rebuilding and weighing the argument, ending on the reviewer's verdict. Word
band 1800-3400. Use figures (source assets) and at least one set equation. A
single nb-note-strong "Verdict" note is apt for the landing.

## Harness / model record
Harness: Claude Code (Agent SDK), scheduled publication run. Roles run as
isolated subagents on `claude-opus-4-8` (satisfies `capable`/`inherit`).
Per-role reasoning effort is not independently settable through the subagent
interface; each role runs at the session's effort, the closest available option
to the policy's guidance. Editor: model inherit -> `claude-opus-4-8`, effort
target high (ran at session effort). Recorded as a deviation on effort only.
