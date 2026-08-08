# writer brief: tech-news/2026-08-08 (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       the day, the selection standard, boundaries
  ../../writing-coach/01/voice-guide.md     craft standard and licenses for this brief
  ../../researcher/01/evidence.md           the verified slate and the only claim set available
  the initialized article and its .nb-context (brief template contract + furniture catalogs)
Output: agent-artifacts/tech-news/2026-08-08/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/5348099f-bd2a-54d6-a1ef-dbfbbb236392/scratchpad/library

The article file to edit is at:
  .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html
Run the proof with --no-check-links while iterating, then with links included until BLOCK: 0.

This round's focus (4-6 items; each item exactly one primary + at least one independent
secondary, per the brief template contract):
- Use the researcher's verified slate (4 solid field items; a Cloudflare-OS fifth is
  optional). Four strong items meets the floor — do not pad with a weak item. The
  in-window science/health result the commission preferred was not found; that is fine.
- Obey the evidence's separation of announcement from commitment, item by item:
  * Terafab: report >$16.8B first-phase, but the prose must carry the caveats — SpaceX's
    S-1 calls it a "general framework" with no binding commitments, Intel is the
    named-but-undisclosed manufacturer, and $16.8B is down from a $25B March figure.
  * AMD/Taalas: a definitive acquisition agreement, terms undisclosed; the throughput and
    "73x an H200 at one-tenth the power" numbers are Taalas's own unverified test-chip
    claims — attribute them as such, do not state them as established.
  * The coding-agent security disclosure (Novee, Black Hat): report the CVEs precisely and
    neutrally, including the Claude Code severity discrepancy (Anthropic v4 6.0 vs NVD 9.1)
    and the fixed versions. Just the facts from the record.
  * Kioxia/SanDisk 332-layer NAND: a demonstration, not shipping — say so.
- Each item opens on why it matters to technical knowledge or practice. Carry data-nb-kind
  labels from the evidence (a company post is primary for what was announced, not for
  whether a claim is true). Do NOT include Palantir earnings.
- Headline names the day's single most consequential development as a claim. Avoid the
  triad headline and comma-triad dek molds.
- Set nb-meta harness = "claude-code-routine" and model = "Opus 4.8".
