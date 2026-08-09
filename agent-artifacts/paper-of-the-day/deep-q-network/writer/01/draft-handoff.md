# writer handoff: paper-of-the-day/deep-q-network (01)

## The one act of original work

The article separates DQN's two non-identical claims — the aggregate "human-level
control across 49 games" and the operational "at or above 75% of the human score
on 29 of 49" — and sorts each after-record study by which of the two it actually
touches, or by neither when it lands on the value estimates (Double DQN) or on
deep-RL fragility in general (Henderson). The evidence record supplies the studies
and their scopes; it does not perform this split. The synthesis is visible in the
"Where the later studies land" mapping table and lands in the verdict: the record
undercut the aggregate summary while leaving the operational 29-of-49 claim
standing.

## Proof

`nb check` (with links) returns `BLOCK: 0` — PUBLISHABLE. Stamped words=3016,
sources=8 (all primary; series floor 8), reading_minutes=13.

Two `W-SENTENCE-DENSITY` warnings left intentionally (one 41-word, one 42-word
sentence, both single-purpose and under control). They are the calm, carefully
punctuated long sentences the voice guide models on Weng, and fragmenting them
would flatten the register; recorded rather than split.

## Evidence handling worth flagging to the editor

- Every per-game percentage printed (Video Pinball 2,539%, Breakout 1,327%,
  Montezuma's Revenge ~0%) was read directly off the captured Figure 3, not from
  memory. The Extended Data Table 3 ablation grid (Breakout 316.8 → 3.2, etc.) was
  re-opened and read firsthand from the Nature PDF, per the brief's instruction to
  re-verify any Extended Data number before printing it.
- No after-record decimal is printed. The evidence flagged Machado's Brute/DQN
  scores, the Double DQN and Prioritized Replay medians, and Agarwal's run counts
  as fetch-read; those claims are kept directional and qualitative. The single
  after-record number in the piece, sticky-actions σ = 0.25, is firsthand per the
  evidence record.
- The after-record is aimed as the brief required: Machado reads as vindication of
  the operational claim against the determinism objection, not a rebuttal; Agarwal
  is pinned to the aggregate metric and the 100k regime, explicitly not a re-run of
  the 2015 agent; Henderson is marked MuJoCo-by-analogy, not a DQN re-test. No
  "DQN was debunked" framing.

## Open questions

- None blocking. One editorial note: the paper card reproduces the abstract
  verbatim as the template requires, with the paper's internal reference
  superscripts (its own bibliography pointers) dropped so the quoted prose reads
  clean. Flag if the house wants those handled differently.
