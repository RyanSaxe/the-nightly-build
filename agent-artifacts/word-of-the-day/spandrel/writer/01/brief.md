# writer brief: word-of-the-day/spandrel (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, word template, series prompt
- ../../commission.md — the word, its origin, and the dispute to hold
- ../../writing-coach/01/voice-guide.md — how this short read should sound
- ../../researcher/01/evidence.md — the verified definitions, the 1979 passage, the objection, and its cautions
- article: .nb-work/word-of-the-day/spandrel/library/word-of-the-day/spandrel.html (initialized; edit it)
- template context: .nb-work/word-of-the-day/spandrel/.nb-context/ (contract, runtime assets, furniture)

Output: draft-handoff.md (this directory)

Proof: ./nb check .nb-work/word-of-the-day/spandrel/library/word-of-the-day/spandrel.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

This round's focus:
- 550 to 800 words, 2 to 5 sections beyond the required `rs-word-card` definition. Keep it the paper's smallest read; do not expand into a survey of adaptationism.
- Hold the two distinctions the evidence flags, do not smooth them: spandrel (the flat space beside an arch) versus pendentive (the curved segment carrying a dome), and spandrel (the byproduct itself) versus exaptation (the byproduct later co-opted into a use). If you describe a trait that "came along for free and later found a use," that later use is exaptation and should be named as the separate term it is.
- Gould conceded in 1997 that the San Marco structures are pendentives and answered the objection by broadening the word, not by denying the point; that concession is the honest spine of the origin story. If you use Robert Mark's structural objection, attribute it to Steadman's account, which is the only source that carries it here.
- Opener: do not open on the recent word-of-the-day copular frame that names the distinction in the abstract before any story lands ("X marks the difference between..."). Open on a documented particular.
- Do not invent a locator; use only the locators the evidence record supplies. Run the display-text pass, then `nb stamp` and the exact `nb check` (links included) until BLOCK: 0. Name the piece's one act of original work in the handoff.
