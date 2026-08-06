# researcher brief: paper-of-the-day/instructgpt (01)

Inputs:
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/editorial-direction.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/commission.md  (the paper, the math to set, the figures to bring in, the after-record)

Output: .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/01/evidence.md

Read the primary sources, not summaries:
- InstructGPT: Ouyang et al. 2022, "Training language models to follow
  instructions with human feedback" (arXiv:2203.02155) and the OpenAI blog
  release. Read the method section, the RM ranking loss, the PPO+KL objective,
  the human-eval protocol, and the appendices behind the headline win-rate.
- Reward-model over-optimization: Gao, Schulman, Hilton 2023
  (arXiv:2210.10760). Read the functional form of the proxy-vs-gold gap.
- DPO: Rafailov et al. 2023 (arXiv:2305.18290). Read the derivation that maps
  the KL-regularized RLHF objective to a closed-form classification loss.

Record the exact equations the reconstruction needs (RM loss; RL objective with
the beta-KL term; DPO reparameterization) in the Numbers/record precisely
enough for the writer to set them faithfully. Verify the headline claim (a
~1.3B InstructGPT preferred over 175B GPT-3) and its evaluation conditions
against the paper. In Source assets, name the exact figures (win-rate-by-size,
the RLHF pipeline diagram, any alignment-tax figure) with what each shows and
what a crop must keep. In Contradictions, capture where the after-record
qualifies or complicates the paper's claim. Search for serious criticism of
the win-rate methodology (annotator agreement, prompt distribution) too.
