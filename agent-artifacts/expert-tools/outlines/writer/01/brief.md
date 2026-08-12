# writer brief: expert-tools/outlines (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/commission.md  — subject, angle, boundaries, and the habits not to inherit
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/writing-coach/01/voice-guide.md  — how this piece should sound
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/researcher/01/evidence.md  — the complete claim set; treat as evidence, not prose
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/library/expert-tools/outlines.html  — the initialized article to edit in place
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/.nb-context/  — effective template contract, furniture catalogs, runtime assets

Output:
  /home/user/the-nightly-build/.nb-work/expert-tools/outlines/agent-artifacts/expert-tools/outlines/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/expert-tools/outlines/library/expert-tools/outlines.html --series expert-tools --library /home/user/library-checkout
  (use --no-check-links while iterating; run the full command, links included, until BLOCK: 0)

nb-meta: set harness to "claude-code-routine" and model to "claude-opus-4-8"; fill
dates; nb stamp writes the counts.

This round's focus, from the evidence record's refinements:
- Frame Outlines against the retry-and-parse path it actually replaces, not as
  today's fastest constraint engine; XGrammar and llguidance now claim to beat it
  and criticize its precomputed-index design. Say that honestly where the piece
  weighs speed.
- "Valid by construction" is backend-dependent: the FSM-over-vocabulary masking
  runs on local/open-weight backends; on hosted APIs Outlines delegates to the
  provider's feature, and inside vLLM/SGLang the default engine is often XGrammar.
  The example and the guarantee must not overclaim across backends.
- Whether constraining decoding hurts reasoning accuracy is genuinely contested
  ("Let Me Speak Freely?" versus dottxt's rebuttal); the structural guarantee is
  not. Keep the two separate.
- Attribution: the 2023 paper's byline is Normal Computing; the library is now
  dottxt-ai. Both are correct for their moment; do not conflate them.
