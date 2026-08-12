# researcher brief: paper-of-the-day/mixture-of-experts (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/commission.md  — the paper, the reconstruction, and source obligations

Establish, from the 2017 paper "Outrageously Large Neural Networks: The
Sparsely-Gated Mixture-of-Experts Layer" itself, the exact mechanism and figures
the reconstruction needs: the softmax gating network and its equation; the noisy
top-k gating that induces sparsity and how the noise and the top-k selection work;
the two auxiliary losses (importance and load) with their definitions and the
role each plays; the batch-shrinking problem and how the paper mitigates it; and
the headline results with their scope — the parameter and expert counts, the
language-modeling and translation numbers (perplexity, BLEU), and the compute
ratios behind the "thousandfold capacity at minor computational cost" claim. Read
the appendices where the loss definitions and experimental detail live, not just
the body. Identify the specific figures the claim turns on (the MoE layer
schematic; the results figures or tables showing capacity against perplexity or
compute) and record exactly where each lives in the paper and what it shows, so
the writer can capture it as a source asset.

Then establish the follow-on record from its owning papers: what the Switch
Transformer (Fedus et al.) changed by routing to a single expert and how it
treated the balancing loss; GShard (Lepikhin et al.); expert-choice routing (Zhou
et al.); and a recent production or auxiliary-loss-free MoE reference (e.g. a
DeepSeek MoE technical report). For each, record what it confirmed, simplified, or
overturned about the 2017 gating and its auxiliary losses. Verify every number
against the primary that owns it, with units and scope. Record contradictions and
any claim in the original that later work qualified. Classify each source primary
or secondary and why; at least 8 sources; confirm every URL resolves to the
source's own page.
