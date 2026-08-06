# Commission: paper-of-the-day/instructgpt

## Authorized work
Scheduled duty for 2026-08-06 returned `paper-of-the-day` as an open section:
choose a paper within the beat, do not repeat a published slug. This run
commissions exactly one paper article.

## Paper and angle
"Training language models to follow instructions with human feedback"
(Ouyang, Wu, Jiang, et al., OpenAI, 2022) — the InstructGPT paper, the
reference write-up of the three-stage RLHF pipeline (supervised fine-tuning →
reward model from human preference comparisons → PPO against the reward model
with a KL penalty to the SFT policy).

Chosen because rebuilding its central claim clarifies an active technical
problem — how a base language model is turned into one that follows
instructions and how "alignment" is actually optimized — and because it has a
strong public record after publication to weigh the claim against:
- The result: a 1.3B InstructGPT model's outputs were preferred to the 175B
  GPT-3's despite ~100x fewer parameters (the paper's headline figure).
- Reward-model over-optimization: Gao, Schulman, Hilton (2023), "Scaling Laws
  for Reward Model Overoptimization," shows the true objective degrades as the
  policy over-optimizes a proxy reward — a named limit the pipeline carries.
- DPO: Rafailov et al. (2023), "Direct Preference Optimization," derives a
  closed form for the same KL-regularized objective, removing the explicit
  reward model and the RL loop — evidence for how the field's practice moved on.

Rebuild the argument with the paper's own artifacts, not a paraphrase:
- Set the math the reconstruction leans on rather than describing it: the
  reward-model ranking loss, and the RL objective (expected reward minus a
  beta-weighted KL to the SFT policy). Where DPO is weighed, set its
  reparameterization so the reader sees why the same optimum has a closed form.
- Bring in the figures the claim turns on as source assets (see below), with
  captions and prose that say what each one settles.
Do not merely announce a famous result. The reconstruction is the article.

## Template and geometry
Template `paper` (longread). Word band 1800-3400, flex sections 2-8, cite rule
per-section. The template owns the abstract card (nb-paper-abstract /
nb-paper-card) and the Sources section. Use nb-math / nb-math-eq for set math,
nb-figure for source assets, nb-table/nb-holdsup where the evidence has that
shape — as evidence, not decoration.

## Sources
Source floor: min 8 (template paper default). Primary is the paper itself
(arXiv:2203.02155 and the OpenAI release); read the cited passages, appendices,
and figures, not the abstract. The after-record papers (Gao et al. 2023;
Rafailov et al. 2023) are primaries for their own claims. Verify every number
against the owning source.

## Source assets (figures to rebuild the claim)
The researcher must name the exact figures; candidates the claim turns on:
- InstructGPT vs GPT-3 human-preference win-rate by model size (the ~1.3B beats
  175B result).
- The RLHF pipeline diagram (SFT → RM → PPO).
- Any figure quantifying the "alignment tax" or preference-vs-scale tradeoff.
Bring only figures whose argument the article actually spends.

## Production policy (resolved via `nb production-policy`)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model inherit, effort high, REQUIRED

Actual harness: roles run as isolated Claude subagents on model
`claude-opus-4-8` (capable tier; required editor "inherit" resolves to this
correspondent model). Deviation recorded: this runtime's subagent launcher does
not expose a per-invocation reasoning-effort control, so the required editor
"high effort" is approximated by the most capable available model at the harness
default effort. No model was traded down.

## Neighboring articles this run
company-analysis/eli-lilly, parenting-research/teething,
word-of-the-day/luddite, current-events/2026-08-06, tech-news/2026-08-06.
This is the edition's ML/AI reconstruction and its only heavy-math longread.

## Recent paper-of-the-day coverage and habits not to inherit
Published slugs: adam-optimizer, attention-is-all-you-need, batch-normalization,
chain-of-thought-prompting, chinchilla, denoising-diffusion, double-descent,
generative-adversarial-networks, grokking, knowledge-distillation, lora,
lottery-ticket-hypothesis, resnet, word2vec. No RLHF/alignment-training or RL
paper is in the catalog; InstructGPT adds a genuinely new dimension.
Habits to break, not to copy:
- Recent papers open by naming a specific quantitative record in the first
  sentence (diffusion "FID of 3.17"; GANs "the loss Algorithm 1 descends").
  Find this piece's own opening onto the RLHF problem.
- Recent outlines run "before X, people did Y" → derivation section by section →
  "what training did / what the theorem is right about" closer (see GANs,
  diffusion). Outline the RLHF reconstruction on its own logic; do not mirror
  that arc or reuse a "what the field kept" closer.
Template furniture (abstract card, Sources, math blocks) is required, not a
habit to avoid.

## Original contribution expected
A reconstruction that makes the reader able to reason about RLHF: what the
KL-regularized objective actually optimizes, why a small aligned model beat a
large unaligned one, and what the after-record (over-optimization; DPO's
closed form) says about the claim's durability. Not a summary of a famous paper.
