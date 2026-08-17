# editor review-brief: paper-of-the-day/direct-preference-optimization (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md
- commission.md            ../../commission.md
- writer brief             ../writer/01/brief.md
- voice-guide.md           ../writing-coach/01/voice-guide.md
- evidence.md              ../researcher/01/evidence.md
- draft-handoff.md         ../writer/01/draft-handoff.md (original-work sentence; the writer's open questions on added sources and a caption)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/library/paper-of-the-day/direct-preference-optimization.html
- effective contract       /home/user/the-nightly-build/.nb-work/paper-of-the-day/direct-preference-optimization/.nb-context

Recent-pattern notes (compare dek, headings, edges against these for formula):
- The paper-of-the-day series spine ("the paper claimed X; the later record showed Y") is the mandate, not a formula to avoid. But the recent dek run leans on "a cause the paper floated and left open"; confirm this dek and headline commit the finding in DPO's own terms.

This round's focus:
- The load-bearing distinction: DPO's core theorem (objective-level equivalence to the RLHF objective) is undisputed and none of the follow-ups overturn it; what later work contests is what OFFLINE DPO reaches in PRACTICE. Verify the article holds these two visibly separate and does not present the practice critiques as refuting the theorem.
- Verify the internal tension is staged honestly: DPO's own Table 1 reports better out-of-distribution generalization than PPO (a small, preliminary transfer test the authors flag), while Xu et al. later argue DPO is more exposed to distribution shift. Both must appear side by side, each attributed to its owner.
- Audit the math against the paper: the KL-constrained objective, the optimal-policy closed form (Eq. 4), the reward reparameterization (Eq. 5), the Bradley-Terry substitution and partition-function cancellation (Eq. 6), the DPO loss (Eq. 7), and the gradient's per-example weight. Confirm each equation and its role are correct.
- Source audit (important): the writer reached the 8-source floor by adding three derivation primaries the researcher's evidence record did not carry — InstructGPT (arXiv 2203.02155), PPO (1707.06347), and Bradley-Terry (doi 10.2307/2334029) — each verified by focused fetch. Open each of these hrefs as printed, confirm it resolves and that the claim it is attached to is one that source actually owns. Audit every data-nb-kind. Attribute the later-record findings (Xu, Tang, Azar/IPO, Pal/DPOP) to their owning primaries.
- Inspect the four captured figures and Table 1 as evidence: the crop retains what the argument spends and omits clutter, captions are factual and cited, and prose carries the interpretation. Note the writer's caption judgment on the dialogue figure (Best-of-128 sits above 0.5 at the lowest temperature): verify the caption states what the figure shows and attributes the paper's stronger claim to the paper.
- Five proof warnings are intentional and non-editable: one W-SENTENCE-DENSITY on the template-required verbatim abstract sentence, and four on the required display equations (LaTeX token density read as long sentences). Treat these as engine false-positives, not prose to fix; every genuine prose density warning was already split.
