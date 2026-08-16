# editor review-brief: tech-news/2026-08-16 (01)

Inputs (paths relative to the workspace root `.nb-work/tech-news/2026-08-16/`):
- `agent-artifacts/tech-news/2026-08-16/editorial-direction.md`
- `agent-artifacts/tech-news/2026-08-16/commission.md`
- `agent-artifacts/tech-news/2026-08-16/writer/01/brief.md` — the exact writer brief (check the draft against it for leakage)
- `agent-artifacts/tech-news/2026-08-16/writing-coach/01/voice-guide.md`
- `agent-artifacts/tech-news/2026-08-16/researcher/01/evidence.md`
- `agent-artifacts/tech-news/2026-08-16/writer/01/draft-handoff.md`
- `library/tech-news/2026-08-16.html` — the drafted brief (proof passes at BLOCK: 0, links included)
- `.nb-context/` — effective template contract and furniture catalogs

Output: `agent-artifacts/tech-news/2026-08-16/editor/01/editorial-review.md`

## Recent-pattern notes (tech-news desk, to catch formula)
- The "self-reported / not independently verified benchmark" framing is itself a recurring desk move (15 Aug: DeepSeek "with zero independently verified benchmark scores"; 11 Aug: "self-reports from the labs that produced them"). Marking a benchmark as a self-report is correct and required here, but the phrasing must not read like a stamped repeat of those recent deks and headlines. Check the headline, dek, and item kickers against that.
- Recent headlines lead with one specific result or number, not a topic triad. Confirm the Qwen lead does so.
- Recent deks have used the semicolon reversal and the "quiet week / the advances came from elsewhere" mold; check this dek is its own.

## This round's focus
- Every model capability or benchmark number must be labeled a lab self-report with the verification gap stated (Qwen, GLM-5.3). Verify the draft does this for each such number and that no self-report is presented as an established result.
- The single-GPU footprint (~24-28 GB at 8-bit) is a deployment estimate, not a measured benchmark; confirm it is framed as an estimate at reduced precision, not a hard figure.
- Per-item geometry: exactly one primary and at least one independent account per item; audit each `data-nb-kind` against the primary/secondary test (a company's own post is primary for its announcement, not independent verification).
- The Anthropic item must carry the company's own "involvement, not authorship" caveat.

Open every citation href as printed (including the x.com and Hugging Face links). Verify display text descriptor by descriptor. Edit directly what you own; route to the writer only reporting, evidence, or a redraft. You are the required fresh-eyes editor at high effort; make all three reads.
