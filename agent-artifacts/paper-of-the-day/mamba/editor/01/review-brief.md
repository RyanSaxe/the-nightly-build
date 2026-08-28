# editor review-brief: paper-of-the-day/mamba (01)

Inputs (artifact root .nb-work/paper-of-the-day/mamba/agent-artifacts/paper-of-the-day/mamba/):
- editorial-direction.md, commission.md, writer/01/brief.md, writing-coach/01/voice-guide.md, researcher/01/evidence.md, writer/01/draft-handoff.md
- the article: .nb-work/paper-of-the-day/mamba/library/paper-of-the-day/mamba.html
- template context under .nb-work/paper-of-the-day/mamba/.nb-context/

## Recent-pattern notes (compare display text for formula/catchphrase)
Recent paper-of-the-day headlines/deks:
- "FlashAttention computes exact attention without building the full matrix" (08-21)
- "DPO makes the policy its own reward model and drops RLHF's RL loop" (08-17)
- "Goodfellow's linear explanation got the attack right and the cause wrong" (08-16)
- "The reparameterization trick pulled randomness out of the gradient's path" (08-15)
The claim-first headline (naming the finding) with authors named in the dek is the series shape. Fine in kind; flag a headline that copies a recent one's exact construction rather than finding Mamba's own.

## Round focus
This is a reconstruction, not a figure tour: verify the article DERIVES the mechanism (SSM recurrence/discretization, the selection making B/C/Δ input-dependent, why selectivity forecloses the convolution so the scan is what makes it practical) and WEIGHS the evidence, using the paper's figures as source assets rather than narrating them. Check the math against the evidence's exact equations; check each source asset's caption is factual and cited and that the crop retains the evidence the prose spends. Verify the verdict is earned and states where the claim stops (the recall/copying/in-context limits, Mamba-2/hybrids) — and specifically that the million-length induction-head win is NOT presented as general recall parity (the evidence flags this). Confirm flash-attention (covered 08-21) is not re-explained.
