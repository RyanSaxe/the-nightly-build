# researcher brief: paper-of-the-day/mamba (01)

Inputs:
- commission.md — the paper, the claim, what to examine and weigh
- editorial-direction.md — house standard, citation rules, press voice, series prompt

Output: .nb-work/paper-of-the-day/mamba/agent-artifacts/paper-of-the-day/mamba/researcher/01/evidence.md

Read the focal paper in full (arXiv:2312.00752), including the method section and
appendices. Establish, with exact locators:

- The SSM recurrence and its discretization as the paper states them, the
  selection mechanism (which parameters become input-dependent and how), and the
  hardware-aware selective scan (why selectivity forecloses the global
  convolution and how the scan restores efficiency). Preserve the exact
  equations and definitions the reconstruction will set.
- The empirical claims the argument turns on: the synthetic tasks (selective
  copying, induction heads), language-modeling scaling vs. Transformers/Transformer++,
  and throughput/inference-speed numbers, each with the figure/table it comes
  from.
- The public record after publication that changes the interpretation: Mamba-2
  and state-space duality, hybrid attention-SSM models (e.g. Jamba), and
  analyses of pure SSMs' limits on exact recall / copying / in-context retrieval.
  Record what each establishes and whether it confirms or qualifies Mamba's claim.

### Source assets

Identify the exact figures/tables to bring into the article as source assets (the
induction-heads or associative-recall result, the LM scaling curves, the
throughput figure), naming where each lives in the paper and what a reader learns
from it. Note what a crop must retain.

This round's focus: capture the math and the figure provenance precisely, and
find the strongest criticism as well as the confirming follow-ons, so the writer
can weigh the claim rather than announce it. Every URL must resolve to the
source's own page.
