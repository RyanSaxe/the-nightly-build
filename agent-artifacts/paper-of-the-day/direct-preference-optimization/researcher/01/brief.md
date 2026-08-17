# researcher brief: paper-of-the-day/direct-preference-optimization (01)

Inputs:
- editorial-direction.md   /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/agent-artifacts/paper-of-the-day/direct-preference-optimization/editorial-direction.md (citation standard, series territory, reader)
- commission.md            /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/agent-artifacts/paper-of-the-day/direct-preference-optimization/commission.md (the paper, the reconstruction demands, boundaries)

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/agent-artifacts/paper-of-the-day/direct-preference-optimization/researcher/01/evidence.md

Notes:
- Read the DPO paper (Rafailov et al., 2023) in full including the appendix
  derivation: the KL-constrained objective, the optimal-policy closed form, the
  reward reparameterization, the cancellation of the partition function, the final
  DPO loss and its gradient, and the experiments (sentiment control, summarization,
  single-turn dialogue). Set the exact equations and the reported results.
- Identify the exact figures the claim turns on and where they live in the paper
  so the writer can capture them as source assets (the reward-vs-KL frontier; the
  win-rate comparisons against PPO/RLHF baselines). Say what each settles.
- Bring the after-the-fact record with primary sources: IPO (Azar et al.) on
  preference overfitting, KTO, and studies comparing DPO to on-policy PPO/RLHF and
  documenting DPO's off-distribution/likelihood-decrease behavior. Record where
  they agree and disagree with DPO's claim.
- Verify every headline number against the owning source; record contradictions
  between the original paper and the later critiques explicitly.
