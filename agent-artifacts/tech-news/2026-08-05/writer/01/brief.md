# writer brief: tech-news/2026-08-05 (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/editorial-direction.md — governing standard, `brief` template identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/commission.md — selection standard, sourcing, non-overlap boundaries
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writing-coach/01/voice-guide.md — craft standard and licenses (interval-anchored figure, magnitude conversion, marked inference)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/researcher/01/evidence.md — verified candidates; cite only what it opened
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/library/tech-news/2026-08-05.html — the initialized brief to edit
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/library/tech-news/2026-08-05.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

Focus:
- Select the final 4-6 items (brief band 4-6; each item exactly 1 primary + ≥1 independent secondary). The evidence's strongest field-level spine is the open-weight model surge: Qwen3.8-Max, Thinking Machines' Inkling-Small, DeepSeek-V4-Flash-0731. That is only 3 model items — do NOT pad to 6 with weak releases. If you cannot reach 4 items that each clear the significance bar as *field developments*, file the strong 4 (add a genuinely consequential systems/science item only if the evidence supports one that owns its claim). Product promotion and unreproduced hype do not qualify on their own.
- **This is the critical risk for this brief, per the researcher: nearly every headline benchmark is vendor-published and not independently reproduced.** Do not print a vendor's benchmark number as fact. Attribute it to the vendor in the prose ("Alibaba's own table reports…"), and where an independent signal exists (e.g. Artificial Analysis' index for DeepSeek), give it as the independent line. Use the voice guide's "marked inference" and "interval-anchored figure" licenses. An item whose only support is the vendor's own claim, with no independent account, does not meet the per-item source rule — either find the independent secondary in the evidence or drop the item.
- **URL discipline:** every citation href must land on the source's own page. The researcher flagged that qwen.ai/blog is a JS app that fetch tools read as bare text; the page still resolves in a browser, so the model card / blog's own URL is the correct primary address — but confirm each printed href resolves and is the owner's page, not a fetch endpoint or an aggregator standing in for a primary. Carry the evidence record's data-nb-kind (primary/secondary) exactly; a different outlet is not automatically independent authorship.
- Honor the flagged Contradictions: Inkling-Small's release date (July family page vs. ~Aug 2 full-weights) and Qwen3.8-Max's preview-vs-release status — state what is actually known, do not assert a clean date the sources dispute.
- Non-overlap: defer EU AI Act GPAI (→ opinion), the Anthropic supply-chain court ruling and CareCloud breach (→ current-events). Keep this brief to field developments.
- Headline/dek per voice guide: pick the one development that matters most (the open-weight frontier surge is a candidate through-line, but show it in the leads, do not assert it as a graded thesis); actors named; no triad headline, no colon subtitle, no banned dek molds, no scaffolding subheads. Check recent tech-news deks (use `nb history --structure tech-news/2026-08-04`) before settling.
- Name the piece's one act of original work (the synthesis across items, not mere selection) in draft-handoff.md. Run `nb stamp` then the exact proof to BLOCK: 0, links included.
