# writer brief: paper-of-the-day/mixture-of-experts (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/commission.md  — subject, angle, boundaries, and the habits not to inherit
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/writing-coach/01/voice-guide.md  — how this piece should sound
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/researcher/01/evidence.md  — the complete claim set; treat as evidence, not prose
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/library/paper-of-the-day/mixture-of-experts.html  — the initialized article to edit in place
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/.nb-context/  — effective template contract, furniture catalogs, runtime assets

Output:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/paper-of-the-day/mixture-of-experts/library/paper-of-the-day/mixture-of-experts.html --series paper-of-the-day --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

nb-meta: set harness to "claude-code-routine" and model to "claude-opus-4-8"; fill
dates; nb stamp writes the counts.

This round's focus, from the evidence record:
- Set the math, do not paraphrase it: the softmax gate (Eq. 2), the noisy top-k
  gate (Eqs. 3-5), and the importance and load losses (Sec. 4 and Appendix A). Use
  the equation furniture; the reconstruction leans on these.
- Bring in only the figures the argument spends, captured as source assets with
  nb asset from the paper: the Figure 1 layer schematic and the Figure 2
  capacity/compute results (and Table 1 / Table 2 if the prose reads them).
- Anchor the capacity claim to the controlled comparison (perplexity 34.7 to 28.0
  at about 6 percent added compute on the 1B-word benchmark; 4.3B-param MoE there
  versus the 137B-param, 131,072-expert model), not the abstract's bare ">1000x".
- Weigh against the follow-on record honestly (this is the verdict's spine):
  Switch Transformer overturned the paper's own k>1 conjecture with top-1 routing
  and collapsed the two balancing losses to one; GShard; expert-choice routing and
  auxiliary-loss-free balancing discard the auxiliary loss entirely (Wang et al.
  argue it harms the model). DeepSeek-V3 is read only to its abstract's claims
  (671B/37B active; "auxiliary-loss-free"); do not assert beyond that. The
  expert-choice autoregressive-decoding limitation is unverified in the record;
  flag it as such or leave it out, do not assert it.
