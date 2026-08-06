# editor review-brief: paper-of-the-day/instructgpt (01)

Inputs (read in the order your skill names):
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/editorial-direction.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writing-coach/01/voice-guide.md
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writer/02/brief.md  (the exact current writer brief) and writer/01/brief.md (round-01 direction) — for instruction-leakage checks
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/02/evidence.md  (CURRENT complete claim set, 9 opened sources; supersedes 01)
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writer/02/draft-handoff.md  (original-work sentence — open only on the third read; writer/01 handoff also present)
- .nb-work/paper-of-the-day/instructgpt/library/paper-of-the-day/instructgpt.html  (the article; two source-asset figures, displayed math)
- .nb-work/paper-of-the-day/instructgpt/.nb-context/  (template contract, furniture)

Output: .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/editor/01/editorial-review.md

This is the first editorial read on the article. After any direct prose cuts run
`nb stamp`. The writer owns proof, markup, math, and assets; route those back.

Recent-pattern notes (verify the writer broke these, don't reintroduce):
Recent paper pieces opened by naming a bare quantitative record in sentence one
and ran a "before X people did Y -> derivation -> what the field kept" arc with a
"what the field kept/inherited" closer. Template furniture (abstract card,
Sources, math blocks) is required, not a habit.

This round's focus (a heavy-math reconstruction — precision is the gate):
- HEADLINE REFERENCE POINT: verify the claim is stated exactly, not as the bare
  abstract "1.3B beats 175B GPT-3": InstructGPT 1.3B preferred 85±3% vs a plain
  175B GPT-3 and 71±4% vs a few-shot 175B GPT-3, and Figure 1's win-rate curve
  is measured against the 175B SFT model. It is a human-preference result on
  OpenAI's own API prompt distribution (~40 labelers, ~72.6% agreement, aligned
  to "labelers and researchers," known length/verbosity confound) — framed as
  preference, not capability/truthfulness.
- MATH: check the set equations against the evidence record — the RM ranking
  loss, the PPO+KL (β) objective, and the DPO reparameterization/closed form
  (DPO Eq. 3 = InstructGPT Eq. 2 with γ=0). The three W-SENTENCE-DENSITY
  warnings are on displayed equations/one inline-math derivation; confirm they
  are equations tripping the heuristic, not genuine run-ons.
- AFTER-RECORD: the durability read must be earned — Gao's over-optimization
  makes the KL term load-bearing; DPO shows the RL loop is removable; both carry
  their own scope limits (Gao synthetic; DPO off-task). Confirm it's cited/
  reasoned, not asserted.
- LINEAGE CITATIONS (added round 02): Christiano 2017, Ziegler 2019, Stiennon
  2020, PPO/Schulman 2017 must each genuinely support the "InstructGPT assembled
  and scaled an existing method" claim, not pad the count. Audit every
  data-nb-kind; open every href (the OpenAI-release page is 403-gated to bots
  but must be the resolvable openai.com/index/instruction-following/ page).
- SOURCE ASSETS: inspect both figures (the SFT->RM->PPO pipeline and the
  win-rate-by-size) as evidence — the crop retains what the argument spends, the
  caption is a factual cited label, and the prose spends what each shows.
- Third read: does the reader get a way to reason about RLHF beyond the papers?
  Compare against the original-work sentence.
