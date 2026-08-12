# Commission: paper-of-the-day/mixture-of-experts

## Assignment

One paper reconstruction for the Paper of the Day desk. Template `paper` (min 8
sources; the abstract card anchors the top, then a reconstruction that sets the
math and brings the paper's own figures in as source assets, an evidence review,
and a verdict). Authorized scheduled work from `nb duty`: open slot, one article.
Do not repeat a published paper.

## The paper and why it qualifies

"Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
(Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton, Dean; ICLR 2017). Its central
claim is that conditional computation through a sparsely-gated mixture-of-experts
layer can raise a network's parameter count by roughly a thousandfold while adding
only minor computation per example, and that noisy top-k gating with an auxiliary
balancing loss makes such a layer trainable at scale. It qualifies for the desk on
every count the prompt asks: rebuilding the gating clarifies an active technical
problem (how today's frontier models route tokens to experts), and the paper has a
rich public record after publication — the Switch Transformer's simplification to
top-1 routing, GShard, expert-choice routing, and later auxiliary-loss-free load
balancing all let the article weigh the 2017 design against what the field kept and
what it discarded. It sits squarely in machine learning, the desk's center.

## What the reconstruction must do

Rebuild the argument with the paper's own artifacts, not a paraphrase of them. Set
the math the reconstruction leans on rather than describing it: the softmax gating
network, the noisy top-k gating that induces sparsity, and the two auxiliary losses
(importance and load) that keep experts balanced and the gate trainable. Explain
why sparsity is what makes the capacity nearly free, and where the real costs land
(the batch-shrinking problem the paper addresses, communication cost, and the
balancing the auxiliary losses exist to force). Bring in the figures the claim
turns on as source assets captured from the paper — the MoE layer schematic and the
language-modeling results showing capacity against perplexity or the computational
budget — with captions and prose that say what each one settles. Then review the
evidence and weigh the claim against the follow-on record: what the Switch
Transformer and later routing work confirmed, simplified, or overturned about the
2017 gating and its balancing losses. Close on an earned verdict about what the
paper got right and what the field had to change.

## Sources

`min_sources` 8. Anchor to: the paper itself (the arXiv/ICLR version, read into the
gating math and the appendices, not just the abstract); its key follow-on record
(Switch Transformer, Fedus et al.; GShard, Lepikhin et al.; expert-choice routing,
Zhou et al.; and a recent auxiliary-loss-free or production MoE reference such as a
DeepSeek MoE report); and the prior conditional-computation work the paper builds
on where a claim depends on it. Read the cited passages, not summaries. Verify
every figure (parameter counts, expert counts, perplexity or BLEU numbers, compute
ratios) against the primary that owns it, with its scope. Every URL resolves to the
source's own page.

## Required contribution

A reader who knows modern MoE only as "the thing frontier models use to scale"
finishes understanding the actual 2017 mechanism — noisy top-k gating and the
importance and load losses — well enough to see why later work kept the sparse
routing idea while replacing much of the balancing machinery, and with an earned
judgment of what the original design settled and what it did not. The article does
original work by reconstructing the gating and its balancing losses from the paper
and reading them against the follow-on record, not by announcing the result.

## Boundaries with the rest of tonight's edition

Tech News is instructed not to center an item on mixture-of-experts tonight, so
there is no overlap. Expert Tools covers a present-day structured-generation
library; this is a 2017 paper reconstruction and shares no subject with it.

## Habits not to inherit

- Recent paper reconstructions close under a distinctive mold naming a section or a
  cheaper alternative ("Reading Section 3.3 with the follow-on in hand", "A cheap
  way to get trust-region behavior"). Write this piece's close in its own nouns and
  do not stamp that shape.
- Recent section headings run "The X does Y" declaratives. Vary how the headings
  are built while keeping each a real step of the reconstruction in the paper's own
  nouns.
- Use figures as evidence the prose spends, not decoration. Bring in only the
  figures whose content the article actually reads.

## Production record

- Profile: balanced (`press/production.yaml`).
- writing-coach: capable tier realized as Claude Sonnet, effort low.
- researcher: capable tier realized as Claude Opus, effort high.
- writer: capable tier realized as Claude Opus, effort medium.
- editor: inherit (Claude Opus), effort high, required.
- Harness sets reasoning effort at the session level; per-role effort is the
  policy target on the closest available runtime setting. No `required` model or
  effort directive applies, so no deviation is owed.
