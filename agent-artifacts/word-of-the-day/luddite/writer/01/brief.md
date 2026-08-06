# writer brief: word-of-the-day/luddite (01)

Inputs:
- .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/editorial-direction.md
- .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/commission.md  (the word, the history, the useful distinction)
- .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/writing-coach/01/voice-guide.md
- .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/researcher/01/evidence.md  (the only claim set available)
- .nb-work/word-of-the-day/luddite/library/word-of-the-day/luddite.html  (the initialized article to edit in place)
- .nb-work/word-of-the-day/luddite/.nb-context/  (effective template contract, furniture catalogs)

Output: .nb-work/word-of-the-day/luddite/agent-artifacts/word-of-the-day/luddite/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/word-of-the-day/luddite/library/word-of-the-day/luddite.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root /home/user/the-nightly-build; use --no-check-links while iterating, then links-included until BLOCK: 0)

Commission corrections resolved (the evidence record flagged these — apply exactly):
- CUT the Wellington/Peninsular-army troop comparison entirely; the evidence
  rejects it. State the deployment as ~12,000 troops (attributed as the record
  has it) with no Wellington gloss.
- York executions: state it precisely per the record — the January 1813 total
  of 17 (3 on 8 January for the murder of William Horsfall, 14 on 16 January),
  attributed to the owning source. Do not print the bare "14" without the
  breakdown if you cite an execution figure.
- Dictionary attestation: the OED entry could not be opened. Cite
  Merriam-Webster (opened in full) for the definition and the "First Known Use:
  1811". Do not attribute a first-use dating to the OED specifically; if you
  mention the Nottingham Review 1811 dating, mark it as attributed secondary,
  not verified fact.
- Present-sense anchor: use a source whose href a reader can actually open.
  Anchor the modern sense in the fully-openable TIME/Merchant piece ("The
  Luddites were not anti-machinery; many of them were machine experts"). You
  may reference the 2022 NYT "Luddite Club" instance only if its href resolves
  for a clicking reader; otherwise carry it through the openable secondary.
- Frame "what the Luddites actually opposed" as the better-supported
  historiographical reading (the E.P. Thompson line: opposition to the *use* of
  machinery to cut wages, deskill trades, and pass off inferior goods — not to
  machinery as such), not as a neutral given.

Form:
- Word template. Open with the `rs-word-card` alone (no heading), a cited
  one-sentence definition. Then 2-5 flex sections: origin -> development of
  sense -> present use, the last landing why the word still earns space.
  Word band ~550-800 (the proof reports the exact band).

Recent-pattern habits to break (do not inherit; full list in commission.md):
- Do not reuse the recent eponym-reveal opener shape ("X is named for the wrong
  Y"). Find Luddite's own concrete hook (e.g. the name honoring a man who may
  never have existed, or the scale of the state response).
- Vary section shapes; do not copy the recent definition -> one origin scene ->
  spread -> short "the layer that stayed" closer.
Required furniture (rs-word-card, Sources) is not a habit to avoid.
