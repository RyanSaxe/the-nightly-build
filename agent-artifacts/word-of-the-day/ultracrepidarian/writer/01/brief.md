# writer brief: word-of-the-day/ultracrepidarian (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editorial-direction.md — governing standard, `word` template identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/commission.md — the word, the two-layer origin, the distinction to preserve
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writing-coach/01/voice-guide.md — craft standard and licenses (two scenes + one pivot; let each quoted primary line stand; retire the eponym-opener)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/researcher/01/evidence.md — verified definition, Pliny locator/Latin, Hazlitt evidence, modern usage; cite only what it opened
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html — the initialized article to edit
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

Focus:
- `word` template: the definition card is anchored first (precise definition, part of speech), then 2-5 flexible story sections, then Sources. **Word band 550-800 — tight;** cut to the two scenes plus the distinction, no lexical-essay bloat. Per the voice guide: two short scenes (the corrected cobbler's proverb; Hazlitt's jab at Gifford) joined by one visible pivot marking the centuries/language crossed; let each quoted primary line stand; do NOT open on the eponym ("here is the person behind the word").
- **Accuracy traps from the evidence — honor them exactly:**
  - **Do not say "Hazlitt coined it."** The evidence shows Hazlitt wrote "well *called* an Ultra-Crepidarian critic" (presenting it as already applied) and that Charles Lamb may have coined it. Say **first recorded use** (Hazlitt, *A Letter to William Gifford*, 1819), or state the coinage is unsettled. Etymology is history, not proof of the present meaning.
  - **Pliny's Latin is *supra crepidam* ("above the sandal"), not *ultra*.** The *ultra-* is the later proverb's cast; the sense is Pliny's, the prefix is the proverb's. Get this right in any Latin you print (NH 35.85: "ne supra crepidam sutor iudicaret, quod et ipsum in proverbium abiit").
  - Gifford, the target, had been apprenticed to a shoemaker — the cobbler proverb lands because of it. Use it.
  - **Do not cite Merriam-Webster** (it does not carry the word; the URL 404s). Cite an authoritative dictionary whose page resolves — Dictionary.com for the definition; OED may be named for the 1819 first-evidence dating (its page is login-gated but is the source's own page). Pliny via LacusCurtius/attalus; Hazlitt via the reprinted letter. min_sources 4.
  - The Baptist News modern-usage quote 403s to fetch tools — either reconfirm it resolves in a browser or use the Salon (2023-12-01) usage instead; do not print a source whose href does not resolve.
- Ground the present sense in a real modern use (Salon quote is confirmed). Preserve the distinction the word names (opining beyond one's competence) vs. near-neighbors.
- Headline/dek per `word` identity and the headline standard: no colon subtitle, no banned dek molds. Name the piece's one act of original work in draft-handoff.md. Run `nb stamp` then the exact proof to BLOCK: 0, links included.
