# Writer brief: tech-news/2026-08-02 (01)

## Your job
Draft the technology `brief` for 2026-08-02 — the 4-item slate the evidence
record verified — then prove it to `BLOCK: 0`. Draft only from the evidence
record and voice guide. Each item is a judgment about why a development matters,
not a recap; no reader-handoff closer.

## Begin with these exact inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set and
  its honest caveats — obey every one).
- Initialized article:
  `/home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html`
  (edit; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (brief geometry: 4-6 items, each
  cited with 1 primary + 1+ independent secondary).

## The slate (lead order from the evidence record)
1. **EU AI Act Article 50 transparency obligations take effect (2026-08-02).**
   Non-security lead, hard dateline. Primary: the regulation's Article 50 text
   and the European Commission FAQ (application date 2 Aug 2026 per Art. 113; the
   marking-obligation grace period to 2 Dec 2026; penalty ceiling €15M or 3% of
   worldwide turnover). Independent secondary: the K&L Gates/National Law Review
   analysis (scope beyond high-risk systems; "generic references hidden in terms
   and conditions... unlikely to be sufficient"). The judgment: what actually
   changes for builders as of today.
2. **OpenAI's field report: coding agents modernize scientific research software
   (2026-08-01).** Primary: OpenAI's report page. IMPORTANT sourcing constraint —
   the primary 403-blocked automated fetch for the researcher. First, TRY to open
   it yourself; if you can read it, cite the specifics you verify. If it stays
   inaccessible, cite it as the development's primary of record (it resolves for
   human readers) but state only figures a directly-read independent source
   confirms, and attribute the contested aligner-parity figure (99.8%) to The
   Decoder by name. Independent secondary: The Decoder (adds the METR ~50%-
   rejection finding and named-researcher critical quotes — Pedersen, Ewels). Use
   the verified speedups (RustQC 60x runtime / 25x disk I/O; FastQC-Rust 7x; Trim
   Galore 3x; HI.SIM 31% with byte-identical output; 8 case studies, 5 Codex-only
   / 3 with Claude Code). DO NOT use the "1,610→27 seconds" figure (unverified,
   likely hallucinated). The judgment lives in the caveat: agents went fast but
   "couldn't judge whether their own output was scientifically sound."
3. **US frontier-AI executive order (EO 14409) deadline lapses (2026-08-01).**
   Primary: the EO text (signed 2026-06-02; Section 3 sets a 60-day clock →
   2026-08-01). Independent secondary: Forkast/Yahoo Finance (no Federal Register
   notices, NIST/CISA publications, or OSTP statements as of 07-31). FRAME the
   "missed" claim honestly: "no public deliverable had appeared as of [date], per
   Forkast's reporting," not a flatly established government failure (only one
   independent account). Do NOT use the unverified Kush Desai "BREAKING" quote.
   The judgment: the contrast with Item 1 — one regulator hit its date, one
   didn't.
4. **DeepSeek-V4-Flash-0731 released (2026-07-31).** Primary: DeepSeek's own API
   changelog ("keeps the same model architecture and size... only
   re-post-trained"). Independent secondary: Artificial Analysis's own benchmark
   run (Intelligence Index 50 vs a 25 median for comparable open-weight models,
   #3/101; 284B total / 13B active MoE; input $0.14 / output $0.28 per 1M
   tokens). Note it is two days off the dateline — lead the item on the
   independent benchmark result, not the release-as-event. DO NOT assert
   "open-weight release" as settled unless you confirm the Hugging Face repo's
   files tab actually holds weight files (the record flags this as unresolved);
   treat vendor-stated agent benchmarks (Terminal Bench 82.7 etc.) as
   vendor-stated/unreproduced if used.

Run these 4; do not pad to 6 with the discarded candidates (AlphaFold-team,
IPMI/BMC, Meta pricing, BYD robot, Latigo, etc. — all rejected with reasons).

## Furniture
A brief is items + sources. Reach for furniture only where evidence has a shape
prose hides and it is documented — e.g. a compact table of Article 50's four
obligations by actor (provider vs deployer), if it earns its place. No chart
unless from verified series; no decoration. No article-authored scripts/styles/
iframes/forms/external images.

## Universal rules
Per-item: exactly 1 primary + 1+ independent secondary; carry evidence-record
kinds into `data-nb-kind`. Number sources in first-citation order; add
`data-nb-locator`/`data-nb-url` only where the evidence supplies it. When a story
advances one the paper covered, say so and build on it (none of these four is a
prior item). Fill `nb-meta`: series tech-news, slug 2026-08-02, template brief,
mode rolling, order null, date 2026-08-02, tags (choose accurate ones, e.g.
["ai","policy","open-source"]), measured sources/words, a real dek (a stance),
harness "claude-code", model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html --series tech-news --library /home/user/library`
If the OpenAI primary URL trips `B-SOURCE-DEAD`, handle it (confirm whether it's
a 403 vs a true 404; if genuinely unciteable, return
`REQUEST researcher <one-sentence>` rather than dropping below the 4-item floor).
Treat warnings as revision notes.

Write `draft-handoff.md` here: original-work sentence, paths changed, proof
result and warnings left, any remaining evidence questions. Return
`DONE writer <path>` after `BLOCK: 0`, or a REQUEST/BLOCKED line.
