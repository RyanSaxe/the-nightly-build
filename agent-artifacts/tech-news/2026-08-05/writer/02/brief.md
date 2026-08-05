# writer brief: tech-news/2026-08-05 (02) — first full draft

(writer/01 returned blocked without drafting: its spine items were already published on 08-03.
This is the first real draft, built on the round-04 evidence and an authorized relaxed window.)

Inputs:
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/editorial-direction.md — governing standard, `brief` template identity, series prompt, declared reader (ML-engineering background)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/commission.md — selection standard, sourcing, non-overlap boundaries
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writing-coach/01/voice-guide.md — craft standard and licenses (interval-anchored figure; magnitude conversion; marked inference)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/researcher/04/evidence.md — THE evidence to use (round 04 is the complete, current record); cite only what it opened
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/library/tech-news/2026-08-05.html — the initialized brief to edit (still the untouched skeleton)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writer/02/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/library/tech-news/2026-08-05.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

## Authorized scope (state the timeframe honestly)
This was an unusually thin AI-news day: the week's biggest field items (HAWK-256/Claude, GPT-5.6,
DeepSeek-V4-Flash-0731, Inkling-Small, OpenAI Astra) were ALREADY published on tech-news 08-01…08-04
and must not be re-filed. The orchestrator relaxed the window to recently-consequential, not-yet-covered
developments (~Jul 15–Aug 5). **Each item must carry its TRUE date; do NOT imply everything broke on
Aug 5.** Frame the brief as the week's most consequential technology developments, honestly dated.

## The 4 items (from researcher/04 — a clean disjoint set)
File all four; the band floor is 4.
1. **Qwen3.8-Max** (Alibaba, Aug 3) — AI model release. Benchmarks are VENDOR-ONLY and unreproduced, and the weights are not yet public — attribute every score to Alibaba's own table ("Alibaba reports…"), do not print as fact, and do not give it a confident capability headline the evidence can't support. Use the voice guide's marked-inference license.
2. **Arginine / MHC-I codon-dependent translation** (*Cell*, Jul 30) — immunology result that changes practice. Peer-reviewed primary (gated) + Rockefeller press release + independent secondaries.
3. **Atom–quantum-dot two-photon interference** (*Light: Sci. Appl.*, Jul 15) — quantum-networking result. NOTE the flagged number discrepancy: the QD temperature reads 12.4 K vs 12.5 K across secondaries — do NOT print the exact figure unless you can attribute it cleanly; prefer the value the primary supports or omit the decimal precision and attribute to the secondary.
4. **Plasmonic metamaterial photonic time crystal** (*Nature*, Jul 29) — first all-optical photonic time crystal; halves plasmonic loss in the THz band. Primary (gated) + phys.org + École Polytechnique release corroborating date/authors.

Items 3 and 4 are both photonics (distinct groups/results) — acceptable; both are needed to hold the count at 4. Keep them clearly distinct in framing.

## Requirements
- Each item exactly 1 primary + ≥1 INDEPENDENT secondary; carry the evidence's data-nb-kind exactly. Where a peer-reviewed primary is gated (Cell/Nature/Light behind a paywall), the DOI/journal page is still the source's own page and the correct primary address — confirm each printed href resolves (a paywall is gated, not dead), and pair it with the resolving independent secondary.
- Verify every load-bearing number against the owning primary or, where gated, attribute to the named secondary and mark it. Distinguish vendor claim (Qwen) from independent verification.
- Non-overlap: no EU AI Act GPAI argument (→ opinion); no N-able/CISA CVE (→ current-events); the semiconductor business/policy items are out of scope (no field-result primary).
- Headline/dek per the voice guide: pick the ONE development that matters most and say what happened to it — but note Qwen's headline claim can only be "Alibaba reports…", so choose a lead you can stand behind; the dek supplies the brief's honest range and timeframe. No triad headline, no colon subtitle, no banned dek molds, no scaffolding subheads. (No back-catalog dek/heading formula to break beyond the recent briefs.)
- Name the piece's one act of original work (the synthesis across items, not selection) in draft-handoff.md. Run `nb stamp` then the exact proof to BLOCK: 0, links included.
