# editor brief: feature/mlperf-grpo-post-training (01)

Inputs:
- agent-artifacts/feature/mlperf-grpo-post-training/editorial-direction.md
- agent-artifacts/feature/mlperf-grpo-post-training/commission.md (includes recent-pattern notes and decisions after research)
- agent-artifacts/feature/mlperf-grpo-post-training/writer/01/brief.md (the exact writer brief)
- agent-artifacts/feature/mlperf-grpo-post-training/writing-coach/01/voice-guide.md
- agent-artifacts/feature/mlperf-grpo-post-training/researcher/01/evidence.md
- agent-artifacts/feature/mlperf-grpo-post-training/writer/01/draft-handoff.md
- The article and its chart script: library/feature/mlperf-grpo-post-training.html and library/feature/mlperf-grpo-post-training/
Output: agent-artifacts/feature/mlperf-grpo-post-training/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/mlperf-grpo-post-training/library/feature/mlperf-grpo-post-training.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Strict band 600–1200 (stamped 1,193, sources count), so additions need cuts. Open items from the writer's handoff to settle: (1) accelerator-minute figures that do not equal score × count from rounded scores (e.g. 13.78 × 1,024 = 14,110.7 vs the record's 14,113). Recompute from the official per-run minutes in the record or the results logs; if a printed figure cannot be reproduced, change it to one a reader can reproduce and say so in the review. (2) Whether the reference README's "140 to 160 minutes" deserves a sentence. Recent feature headlines to compare: "Epoch averages GB300 leads of 8× to 217× over the H100 into 25×", "Glasswing's 2 November ledger reveals 235 of the 5,087 findings...", "Microsoft says its own traffic rerouting set off a latent July defect in every region". Recent deks often name a person then add a contrast clause. Look at the rendered page (nb preview + Playwright) at phone and desktop, light and dark, after any visual change.
