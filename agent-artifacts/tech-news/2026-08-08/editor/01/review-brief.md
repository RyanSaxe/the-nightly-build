# review-brief: tech-news/2026-08-08 (editor/01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../writer/01/brief.md                  the exact writer brief (for prompt-leak detection)
  ../../writing-coach/01/voice-guide.md     brief craft standard and licenses (read first)
  ../../researcher/01/evidence.md           the evidence record (open as the skeptic requires)
  ../../writer/01/draft-handoff.md          original-work note (open on the third read)
  the article: .nb-work/tech-news/2026-08-08/library/tech-news/2026-08-08.html
  the .nb-context/ brief template contract + furniture catalogs

Recent-pattern notes (break formulas):
- Older tech briefs used date-label headlines; the template titles by date and the dekline
  carries the lead. Judge the dek as a claim and confirm item leads are significance-first
  with varied shapes; avoid the triad headline and comma-triad dek molds.

This round's focus (skeptic read, push hardest here — the danger is vendor claims stated as
verified fact):
- Item by item, confirm the prose separates a company's ANNOUNCEMENT from a verified
  result:
  * Terafab: confirm the >$16.8B is carried with the caveats — SpaceX's S-1 "general
    framework"/no binding commitments, Intel named-but-undisclosed manufacturer, and the
    figure down from a $25B March number.
  * AMD/Taalas: a definitive acquisition, terms undisclosed; the throughput and "73x an
    H200 at one-tenth the power" figures are Taalas's own unverified test-chip claims —
    confirm they are attributed as such, not stated as established.
  * Coding-agent security disclosure: verify the CVE numbers, CVSS scores, and fixed
    versions against the evidence, including the Claude Code severity discrepancy (Anthropic
    v4 6.0 vs NVD 9.1). Neutral, factual.
  * Kioxia/SanDisk NAND: confirm it is described as a demonstration, not shipping.
- Audit every `data-nb-kind`: one primary per item (a company post is primary for what was
  announced, not for whether the claim is true), at least one independent secondary.
- Four items meets the floor; do not push for a padded fifth. Palantir must not appear.
- Open every citation href as printed; it must land on the source's own page.

After any direct cuts, run `nb stamp` (the writer runs the full proof). Route new-prose or
new-evidence needs to the writer/researcher with the exact finding named.
