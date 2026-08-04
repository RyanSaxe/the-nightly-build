# writer brief: tech-news/2026-08-04 (02) — apply two editor-required fixes (writer-only)

Inputs:
- ../01/brief.md — original writer brief (scope, boundaries, voice)
- ../../writing-coach/01/voice-guide.md — voice guide (unchanged)
- ../../researcher/01/evidence.md — evidence (unchanged; no new research)
- ../../editor/01/editorial-review.md — the two required items
- article: .nb-work/tech-news/2026-08-04/library/tech-news/2026-08-04.html (edit in place; editor already made a direct cut + stamped)
Output: .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writer/02/draft-handoff.md
Proof: ./nb check .nb-work/tech-news/2026-08-04/library/tech-news/2026-08-04.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/2d5b8802-c025-5b79-bf1d-234ffd5a3463/scratchpad/library-checkout

Apply exactly these two fixes; change nothing else the editor left settled.

1. Item 1 (Astra) — headline + nb-meta title overclaim. The current display text asserts the ten problems are SETTLED as fact, but the body states no one outside OpenAI has confirmed the Lean-verified proofs. Reframe the headline AND the byte-identical nb-meta `title` (they must stay in sync) so they report what is true: the proofs were RELEASED / are machine-checkable (Lean-verified) but NOT yet independently confirmed. Keep it a real headline (subject-verb, concrete, no colon subtitle, no Betteridge question). Do not overstate; do not add an endorsement the sources don't carry. After editing, confirm nb-meta dek is still byte-identical to the rendered dekline and the h1 matches nb-meta title.

2. Item 3 (vagus atlas) — miscitation. The closing clause says GEN "underlined" the organ-targeting clinical use, but GEN (s6) carries only the atlas and figures (July 28), not that clinical use — which is owned by the primary (s5, the Feinstein release). Reword so the clinical-significance claim is cited to s5, and cite GEN (s6) only for what it actually corroborates (the atlas/figures). Preserve the item's one-primary + one-independent-secondary composition; do not leave s6 cited for a claim it doesn't make.

Then re-run the FULL proof WITH links until BLOCK: 0. Redo the display-text self-test on the changed headline/title and the vagus item (kinds, hrefs resolve, nb-meta dek == dekline, h1 == nb-meta title). Write draft-handoff.md with one line per editor item resolved and the final proof result. Do not push to git.
