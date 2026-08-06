# researcher brief: paper-of-the-day/instructgpt (02)

Purpose: the round-01 record delivered 5 opened primaries; the paper template's
source floor is 8 (see `nb source-policy --series paper-of-the-day`). Close the
gap honestly by opening the foundational works the reconstruction genuinely
leans on — not padding. These are primaries for their own claims and each
should support a claim the article already makes or should make.

Inputs:
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/editorial-direction.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/commission.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/01/evidence.md  (the prior record — PRESERVE all still-valid work; write a complete new evidence.md that keeps it and adds the new sources)

Output: .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/02/evidence.md

Open and record (read the cited passage; classify primary/secondary and say what
each establishes for the reconstruction). Target at least 3-4 of these so the
opened-source total reaches 8+:
- Christiano et al. 2017, "Deep reinforcement learning from human preferences"
  (arXiv:1706.03741) — the origin of the reward-model-from-preferences idea the
  InstructGPT pipeline inherits.
- Stiennon et al. 2020, "Learning to summarize from human feedback"
  (arXiv:2009.01325) — the immediate predecessor running the same SFT->RM->PPO
  pipeline; establishes the pipeline was not new to InstructGPT.
- Ziegler et al. 2019, "Fine-tuning language models from human preferences"
  (arXiv:1909.08593) — the KL-to-the-pretrained-policy penalty's earlier use.
- Schulman et al. 2017, "Proximal Policy Optimization Algorithms"
  (arXiv:1707.06347) — PPO, the exact RL algorithm the objective is optimized
  with; the article sets the PPO+KL objective and should cite PPO's owner.

For each, give the Numbers/Establishes/Paraphrase lines the writer needs, and in
Contradictions note anything that complicates "InstructGPT introduced RLHF"
(these sources show it assembled and scaled an existing lineage). Do not alter
the round-01 equations or headline verification; carry them forward intact.
Also resolve, if you can, the two lesser round-01 notes: the gated OpenAI-release
URL (record the document's own resolvable page) and any unconfirmed venue strings.
