# writer brief: feature/binance-hack-freeze (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/feature/binance-hack-freeze/editorial-direction.md
- Commission: .../commission.md (the story, the freeze-ceiling angle, what the piece must establish)
- Evidence: .../researcher/01/evidence.md (the complete set of claims available to you; do not invent beyond it)
- Voice guide: .../writing-coach/01/voice-guide.md
- Article to edit: /home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/library/feature/binance-hack-freeze.html
- Markup contract + furniture: .nb-context/template-contract.yaml and .nb-context/furniture/{engine,press}.md under /home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/

Output:
- The article HTML above, edited in place.
- draft-handoff.md in .../writer/01/
- Any chart script `chart-N.py` and rendered `chart-N.png` committed beside the article (nb chart provenance).

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/library/feature/binance-hack-freeze.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive for background. Where the evidence cannot supply a fact you need, ask me (the orchestrator) — do not invent and do not expand the claim set yourself.

This round's focus:
- READ the commission's "Query decisions (orchestrator, after research 01)" section and follow it exactly — research refined the angle. In short: the freeze ceiling is set by how much of the haul sits in issuer/administrator-controlled tokens (overwhelmingly stablecoins, ~$3.46B of ~$6.43B; ~44% frozen, 94% of that stablecoin; ~$3.25B beyond reach). The attacker raced to swap ~$786M of stablecoins into ETH/TRX before freezes landed, so ~77% of stolen stablecoin was frozen — speed, not only the asset model, set the gap. Note administrator exceptions (Arbitrum/Optimism/WBETH) as small-dollar caveats; do NOT claim "native assets cannot be frozen." Capability is not action (Circle freezes only when legally compelled; its $1.1B claim is unreconciled). Drop BNB. Chain totals are not asset totals. Always "frozen/seized," never "recovered." Totals as a range. Breach path is an initial finding Binance itself walked back. Attribution is multiple analysts' assessments + an FBI attribution via a secondary; Binance has not attributed; NK denies. The Bybit 2025 all-native haul (~3% frozen) vs Binance's stablecoin-heavy haul (44% frozen) is the sharpest contrast and the piece's original work.
- Template `article`: word band 600-1200 (hard, strict mode), flex sections 2-4, min 5 sources, cite per section. Open with the finding in two or three sentences, then build each section around a visual with short prose saying how to read it and what follows. Cut whatever is not needed to follow the visuals and the conclusion. Five-minute read.
- The finding is the freeze and its ceiling: the frozen recovery is concentrated in issued stablecoins because only an issuer can freeze an address, while the native-asset share (BTC/ETH/SOL/BNB) has no freeze switch and sets the ceiling on what any freeze could recover. Make that comparison visible: a stolen-vs-frozen-by-asset-type table or a computed `nb chart`, built only from the evidence record's verified series.
- Draw the mechanism this press expects: an inline-SVG of the two paths — the breach path (compromised laptop -> service container -> unauthorized withdrawals) and/or the freeze path (flagged address -> issuer blocklist on issued tokens; native assets unaffected). Look at every rendered visual (nb preview) before handing off.
- Separate established from judged. Binance's breach finding is an initial finding attributed to Binance. The North Korea attribution is TRM Labs' high-confidence assessment stated in TRM's words, not a settled fact — present it fairly, in the holder's words, and say it is an assessment. Give figures as the ranges their owners state; say plainly what is unsettled (figures are days old). Recompute any derived figure against its denominator.
- Numbers: use the evidence record's Numbers section exactly. Do not invent precision the sources do not give.

Avoid these recent-feature shapes (the editor compares against them):
- No colon-subtitle headline and no question-mark (Betteridge) headline. State the finding about the freeze and name who it is about.
- Recent deks drop one hard figure into a subordinate clause; a number in the dek is fine but do not copy that exact cadence, and do not use the banned negative-parallelism dek molds (semicolon reversal, suspended question, comma triad). Check recent feature deks.
- Vary section headings; each is a step of this argument in its own nouns, not a stock label.

Do original work: state in one sentence (in draft-handoff.md) what the piece does to the evidence that the evidence does not do itself (e.g. putting the Binance and Bybit hauls side by side to show that how much a freeze can ever reach is decided by the share of the haul in issuer-administered tokens and by how fast the thief swaps out of them), and make it visible on the page (the stolen-vs-frozen-by-asset comparison and the Bybit contrast). Fill nb-meta dates/harness/model (writer model: Claude Sonnet via Claude Code; harness: Claude Code). Number sources in first-citation order, carry each source's kind into data-nb-kind (a different website is not an independent author), add data-nb-locator/url where the record gives it, and land each citation on the passage, not a homepage. Run `nb stamp` then the full `nb check` (links included) until BLOCK: 0. Report the handoff path and any warning left on purpose.
