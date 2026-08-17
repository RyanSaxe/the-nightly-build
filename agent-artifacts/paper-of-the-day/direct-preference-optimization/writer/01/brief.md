# writer brief: paper-of-the-day/direct-preference-optimization (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md (house standard, press voice, series prompt, paper-template identity)
- commission.md            ../../commission.md (assignment, reconstruction demands, boundaries)
- voice-guide.md           ../writing-coach/01/voice-guide.md (how this piece should sound; exemplar passages)
- evidence.md              ../researcher/01/evidence.md (complete claim set; read Numbers, Contradictions, Source assets closely)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/library/paper-of-the-day/direct-preference-optimization.html
- effective contract       /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/.nb-context

Output: /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/agent-artifacts/paper-of-the-day/direct-preference-optimization/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/paper-of-the-day/direct-preference-optimization/library/paper-of-the-day/direct-preference-optimization.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/b3d5d9d7-6994-5933-851f-0ef1bb302a4b/scratchpad/library-checkout

Reconstruction demands (this is a reconstruction, not a summary):
- Set the math the argument leans on, using the paper's own equations: the KL-constrained objective (Eq. 3), its optimal policy (Eq. 4), the reward reparameterization (Eq. 5), the Bradley-Terry substitution that cancels the partition function (Eq. 6), the DPO loss (Eq. 7), and the gradient with its per-example weight. The reward-equivalence-class argument in the appendix is what the title ("your language model is secretly a reward model") actually means; make it land.
- Bring the figures the claim turns on into the article as captured source assets via `nb asset` from the paper's arXiv record (the sentiment reward-vs-KL frontier where DPO dominates PPO; the summarization/dialogue win-rate results). Captions factual and cited; prose says what each settles. Inspect each captured asset and the rendered page.

This round's focus (handle the complication precisely — it is the load-bearing finding):
- Keep two things distinct: DPO's core theorem (objective-level equivalence to the RLHF objective) is undisputed and none of the follow-ups overturn it; what later work contests is what OFFLINE DPO reaches in PRACTICE. Frame the "later record" on the practice claims, not as a refutation of the theorem.
- The sharpest tension is internal and must be shown honestly: DPO's own Table 1 reports DPO generalizing better out-of-distribution than PPO (0.36/0.31 vs 0.26/0.23), a result the authors themselves flag as a small, preliminary transfer test, while Xu et al. later argue DPO is more exposed to distribution shift. Present the paper's own result and the later counter-evidence side by side.
- Carry the after-record with its primary sources: Azar/IPO (KL regularization can hollow out on near-deterministic preferences), Xu et al. (tuned on-policy PPO beats DPO; DPO can reach exploitative out-of-distribution policies), Tang et al. (a persistent online-vs-offline gap), and Pal et al./DPOP (DPO can drive down the likelihood of the very responses it prefers). Attribute each finding to its owning source.
- Venue caveat: KTO and Xu et al. (ICML 2024) are confirmed in-text; IPO (AISTATS 2024), Smaug/DPOP, and Tang et al. are recorded by arXiv identifier with venue labeled only where the researcher was confident. Cite each to its resolving arXiv page and do not state a venue the evidence did not confirm.

Form and floor: paper template (abstract card, reconstruction, evidence review, verdict). Reader is an ML engineer: assume transformers and the RLHF/InstructGPT baseline; teach the DPO derivation. Source floor is at least 8 sources and it is an evidence requirement, not a label: the DPO paper and its four/five follow-ups plus the derivation's own primaries (the RLHF/InstructGPT baseline, the Bradley-Terry model, the PPO baseline) reach 8 legitimately. If your honest citations do not reach 8 opened sources, return a precise researcher request rather than padding. Vary dek/headline from the recent "a cause the paper floated and left open" mold. Fill nb-meta harness and writer-model fields; nb stamp writes counts.
