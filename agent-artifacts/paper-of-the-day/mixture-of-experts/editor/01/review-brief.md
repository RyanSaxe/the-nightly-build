# editor review-brief: paper-of-the-day/mixture-of-experts (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/commission.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/writer/01/brief.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/researcher/01/evidence.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/writer/01/draft-handoff.md
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/library/paper-of-the-day/mixture-of-experts.html  — the article to edit in place
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/.nb-context/  — effective template contract and furniture catalogs

Output:
  /home/user/the-nightly-build/.nb-work/paper-of-the-day/mixture-of-experts/agent-artifacts/paper-of-the-day/mixture-of-experts/editor/01/editorial-review.md

Recent-pattern notes (compare against these to catch formula the draft cannot show
alone): recent Paper of the Day reconstructions close on a distinctive mold naming a
section or a cheaper alternative ("Reading Section 3.3 with the follow-on in hand";
"A cheap way to get trust-region behavior"), and section headings run "The X does
Y" declaratives; deks state a corrective finding ("CLIP's robustness came from its
data, a cause the paper floated and left open"). Flag the close, a heading, or the
dek if stamped to those shapes; require this piece's own nouns.

This round's focus (verify against the evidence record and the paper's own text):
- The math: the softmax gate (Eq. 2), the noisy top-k gate (Eqs. 3-5), and the two
  balancing losses (importance Eqs. 6-7; load, Appendix A). Confirm each equation
  matches the paper and the prose reads it, not paraphrases it. Only one annotated
  equation per the furniture rule.
- The capacity claim is anchored to the controlled comparison (perplexity 34.7 to
  28.0 at ~6% added compute on the 1B-word benchmark), with the abstract's ">1000x"
  reframed as a capacity ceiling (~30x on that benchmark) and the 137B/131,072-
  expert model kept on its separate 100B-word corpus. Verify the numbers and their
  scope; a wrong denominator here is a sourcing failure.
- The follow-on verdict: Switch Transformer overturned the paper's k>1 premise with
  top-1 routing and collapsed the two losses to one; GShard; expert-choice routing
  and auxiliary-loss-free balancing discard the auxiliary loss. DeepSeek-V3 is used
  only to its abstract's claims (671B/37B; "auxiliary-loss-free"); confirm nothing
  is asserted beyond that, and that the expert-choice decoding limitation (flagged
  unverified) is not asserted.
- Inspect both captured source assets (Figure 1 schematic; Figure 2 perplexity
  plots): the crop retains the evidence the prose spends, log scaling and units are
  honest, and the caption is a factual cited label. Confirm citation order is
  first-appearance and audit every data-nb-kind.

Standard gate applies: only an editorial review with no required change settles the
article. Edit prose, structure, and documented furniture directly; route a broken
central claim, missing evidence, a chart/asset fix, or a redraft to the
writer/researcher.
