# review brief: paper-of-the-day/deep-q-network (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, paper template, series prompt
- ../../writer/01/brief.md — the exact writer brief (check for instruction leakage)
- ../../writing-coach/01/voice-guide.md — how this reconstruction should sound
- ../../researcher/01/evidence.md — the verified record; open it as a map and reopen sources as an opponent
- ../../writer/01/draft-handoff.md — the original-work sentence (open on the third read)
- article: .nb-work/paper-of-the-day/deep-q-network/library/paper-of-the-day/deep-q-network.html
- template context: .nb-work/paper-of-the-day/deep-q-network/.nb-context/

Recent-pattern notes (compare the draft against these; break any that recur):
- The recent paper openers name a finding as a reversal or a "before it was asked to" turn ("Attention learned to align long before it was asked to explain", "word2vec's most famous demo predates word2vec"). The opener should not use that mold.
- The verdict section keeps landing under a "A reviewer's verdict" heading; the required verdict block should be named for this paper's own question.

Round focus (correctness watch-items from the evidence):
- Aim the after-record exactly where it lands. Henderson is MuJoCo continuous control (bears on DQN by analogy only); Agarwal's bite is on the aggregate "human-level" metric and the 100k regime, not a re-run of the 2015 agent; Machado's sticky-actions result largely vindicates DQN against the determinism objection. Reject any sentence implying these re-ran DQN and found its scores unstable, or a blanket "DQN was debunked."
- Any per-game number or replay/target-network ablation figure must trace to a re-verified Extended Data table; the firsthand scope numbers are 49 games, 43 of 49 beaten, 29 at >=75% human. Flag an unverified figure to the writer.
- Check the equations against the evidence (Q-learning objective, TD error, target network, experience replay). Inspect both source-asset figures: the crop retains the evidence the argument spends, the caption is a factual cited label. Audit every data-nb-kind.
