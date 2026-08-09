# writer brief: paper-of-the-day/deep-q-network (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, paper template, series prompt
- ../../commission.md — the reconstruction, the figures, and the after-record to weigh
- ../../writing-coach/01/voice-guide.md — how this reconstruction should sound
- ../../researcher/01/evidence.md — the verified equations, figures, scope numbers, and after-record findings, with its caveats
- article: .nb-work/paper-of-the-day/deep-q-network/library/paper-of-the-day/deep-q-network.html (initialized; edit it)
- template context: .nb-work/paper-of-the-day/deep-q-network/.nb-context/ (contract, runtime assets, furniture)

Output: draft-handoff.md (this directory)

Proof: ./nb check .nb-work/paper-of-the-day/deep-q-network/library/paper-of-the-day/deep-q-network.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

This round's focus:
- Set the math the reconstruction leans on with the template's equation furniture: the Q-learning objective, the temporal-difference error, and why experience replay and the target network are there. Do not paraphrase where the equation is the thing.
- Capture the two figures as source assets with `nb asset` (per the skill, run it through `uv run --group figure-capture`): Figure 3 (per-game normalized scores against a human tester) and Figure 4 (the last-hidden-layer embedding). Caption each with what it settles, inspect the crop and the rendered page, and cite the paper.
- Aim the after-record precisely, per the evidence record's caveats: Henderson is MuJoCo continuous control and bears on DQN only by analogy; Agarwal's bite is on the aggregate "human-level" summary metric and the 100k regime, not a re-run of the 2015 agent; Machado's sticky-actions result largely vindicates DQN against the "it only worked because Atari was deterministic" objection. Do not imply any of these re-ran DQN and found its scores unstable, and do not write a blanket "DQN was debunked."
- Before printing any per-game number or the replay/target-network ablation figures, re-open Nature's Extended Data Tables 2 and 3, which the researcher flagged as image tables not machine-read. If you cannot re-verify a specific number, use the firsthand scope numbers (49 games, 43 of 49 beaten, 29 at ≥75% human) and the qualitative ablation claim instead of an unverified figure.
- Opener and verdict: do not open on the recent paper mold that frames a finding as a "before it was asked to" reversal. Keep the required verdict block, but name its heading for this paper's own question rather than the recurring "A reviewer's verdict".
- Name the article's one act of original work in draft-handoff.md and make it visible in the piece.
