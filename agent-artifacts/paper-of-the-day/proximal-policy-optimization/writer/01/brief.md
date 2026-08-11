# writer brief: paper-of-the-day/proximal-policy-optimization (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/agent-artifacts/paper-of-the-day/proximal-policy-optimization/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/agent-artifacts/paper-of-the-day/proximal-policy-optimization/commission.md  — paper, angle, reconstruction obligations, habits to break
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/agent-artifacts/paper-of-the-day/proximal-policy-optimization/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/agent-artifacts/paper-of-the-day/proximal-policy-optimization/researcher/01/evidence.md
  Article to edit: /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/library/paper-of-the-day/proximal-policy-optimization.html
  Template context: /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/.nb-context/  (paper template: abstract card + link, reconstruction sections, per-section citations)

Output:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/proximal-policy-optimization/agent-artifacts/paper-of-the-day/proximal-policy-optimization/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/paper-of-the-day/proximal-policy-optimization/library/paper-of-the-day/proximal-policy-optimization.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/42af37e2-ce88-5a16-a49b-bb7fb5609b03/scratchpad/library

Longread (1800-3400 words). Rebuild PPO from the paper's own artifacts: set the
math with the equation furniture (the ratio r_t, L^CPI, the clipped L^CLIP with
epsilon=0.2 and why the min() is a pessimistic bound, the combined actor-critic
loss with the c1/c2 terms, truncated GAE, the multi-epoch minibatch loop). Do not
paraphrase the equations the reconstruction leans on; set them. Then weigh the
paper's advertised mechanism (the clipped objective as the trust-region enforcer)
against Engstrom et al.'s reexamination, steelmanning PPO's own ablation (Table 1,
clipping at 0.2 best) and Andrychowicz first.

Respect these corrections from the evidence record exactly:
- The angle is advertised-vs-operative mechanism, NOT "PPO debunked"; PPO's
  practical dominance is undisputed. Say so.
- Engstrom's trust-region result is about the probability RATIO (PPO's max ratio
  exceeds 1+epsilon) — its MEAN KL stays under TRPO's 0.07 bound in the same
  experiment. Do not write the flattened "PPO leaves its trust region" claim.
- Code-level optimizations outweigh the PPO-vs-TRPO step choice (Engstrom Table 2);
  PPO-NoClip beats PPO-Minimal (Table 3); Engstrom concedes PPO strictly contains
  PPO-NoClip since epsilon is a free parameter.

Bring in the figures the claim turns on as source assets via `nb asset`, only for
exact visuals from the cited papers whose argument the prose spends (candidates:
the PPO clipping-illustration figure; an Engstrom ablation or the trust-region
figure). Inspect each captured asset and the rendered page. If a chart would carry
a comparison better than a source figure, build it only from the evidence record's
verified numbers with `nb chart` and commit its provenance. Use per-section
citations with correct data-nb-kind (6 primary, 2 secondary in the record). Fill
nb-meta (title, dek matching rendered dekline, tags, harness, writer model = Claude
Opus). Record the original-work sentence in the handoff.
