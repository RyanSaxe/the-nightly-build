# writer brief: paper-of-the-day/instructgpt (01)

Inputs:
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/editorial-direction.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/commission.md  (the reconstruction angle and the after-record weighing)
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writing-coach/01/voice-guide.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/01/evidence.md  (the only claim set available; equations set verbatim, headline conditions, named figures)
- .nb-work/paper-of-the-day/instructgpt/library/paper-of-the-day/instructgpt.html  (the initialized article to edit in place)
- .nb-work/paper-of-the-day/instructgpt/.nb-context/  (effective template contract, furniture catalogs, runtime assets)

Output: .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/instructgpt/library/paper-of-the-day/instructgpt.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then run it links-included until BLOCK: 0)

Commission decisions resolved (the evidence record flagged these as open):
- Source assets: bring exactly two — Figure 2 (the SFT→RM→PPO pipeline) and
  Figure 1 (win-rate-by-model-size, the headline result). Capture each with
  `nb asset` from the cited primary; spend what each shows in prose. Do NOT
  bring Figure 29 (alignment tax) or Gao's figure as assets; carry the
  alignment-tax point and the over-optimization curve in prose/inline-math
  only, so the piece stays inside the 1800-3400 band and reads as a
  reconstruction, not a figure tour.
- Keep DPO mathematical: set its reparameterization/closed form; do not add its
  empirical sentiment figure.

Precision the evidence record requires you to honor (do not smooth over):
- The headline reference point is not single. State it exactly: InstructGPT
  1.3B is preferred 85±3% vs a plain (un-prompted) 175B GPT-3 and 71±4% vs a
  few-shot-prompted 175B GPT-3; Figure 1's win-rate curve is measured against
  the 175B SFT model. Do not let the abstract's "175B GPT-3" stand unqualified.
- It is a human-preference result on OpenAI's own API prompt distribution,
  judged by ~40 labelers at ~72.6% agreement, aligned to "labelers and
  researchers, not any broader notion of human values" (§5.2), with a known
  length/verbosity confound. Frame the claim as that, not as capability or
  truthfulness.
- The β-KL term is load-bearing (Gao: the optimized proxy reward's gold value
  peaks then declines with KL). DPO reaches the same optimum without the RL
  loop (DPO Eq. 3 is InstructGPT Eq. 2 with γ=0). Record the after-record's own
  boundaries: Gao's setup is synthetic; DPO's evidence is off-task
  (sentiment/summarization/single-turn), not instruction-following at scale.

Recent-pattern habits to break (do not inherit; full list in commission.md):
- Do not open by naming a bare quantitative record in the first sentence (the
  recent diffusion/GANs opener shape). Find this piece's own way into the RLHF
  problem.
- Do not mirror the recent "before X people did Y → derivation → what the field
  kept" arc, and do not reuse a "what the field kept/inherited" closer.
Template furniture (abstract card, Sources, nb-math blocks) is required, not a
habit to avoid.
