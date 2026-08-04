# review-brief: tech-news/2026-08-04 (editor/01)

Inputs:
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/editorial-direction.md — governing standard, `brief` identity, series prompt, declared reader
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writer/01/brief.md — the exact writer brief (for instruction-leakage checks)
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writing-coach/01/voice-guide.md — voice guide (read first)
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/researcher/01/evidence.md — the evidence record
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writer/01/draft-handoff.md — the writer's handoff, original-work sentence, and the gated-primary caveat
- .nb-work/tech-news/2026-08-04/library/tech-news/2026-08-04.html — the article to review (make direct cuts here)
- .nb-work/tech-news/2026-08-04/.nb-context/ — effective template contract and furniture catalogs

Recent-pattern notes:
- Recent tech-news leaned on model-release and AI-security-CVE items. This brief varies kind (a formal-proof result, an AI-for-science tooling report, a neuroscience atlas, a CVE). Confirm no item reads as product promotion, and check the dek against banned molds (colon subtitle, comma-triad).

THE KEY DECISION this round (from the writer's handoff): Item 2 (OpenAI coding-agents-for-science field report) has an owning primary (openai.com field-report page + X post) that stayed gated (403/402) and could NOT be read firsthand; its canonical page is the primary href and resolves (403, so link-check passes), but every load-bearing figure and the "confidently wrong" caveat in that item are carried by The Decoder (secondary), which the writer did open. Decide:
  (a) keep the item — the canonical primary is the correct owning document and a read independent secondary carries the claims (gated ≠ dead) — but only if the item makes no claim not corroborated by the read secondary, and the data-nb-kind labels are honest; OR
  (b) if you judge citing an unread primary unacceptable here, the fix is the writer/researcher opening the primary via a working fetch path or swapping in an item whose primary was read. NOTE: dropping this item without replacement would leave 3 items, below the brief's 4-6 floor — so a drop requires a replacement, which is researcher+writer work. Name the owner precisely.

This round's focus (required editor stage, high effort):
- Skeptic: verify the four items' load-bearing numbers against the owning primaries in evidence. For Astra (lead): the results-to-Lean-file table — confirm each row against the repo/manuscript; the "zero unproven steps / no sorry" claim must be framed as the work's own, with no independent-endorsement (e.g., no Gowers) asserted. For Cisco: the EXPLOITED CVE is CVE-2026-20316 (CVSS 5.3), kept strictly distinct from the CVSS-10 20079 — confirm no conflation, and that the chaining/severity claim is honest. For the vagus atlas: the primary href is a resolving wire reproduction (feinstein.northwell.edu gated) — confirm the kind label is honest.
- Open every citation href as printed (each must resolve to the source's own page). Audit every data-nb-kind: one owning primary + at least one independent secondary per item; a different outlet is not automatically independent authorship.
- Cut/voice: cap the single earned hedge-contrast across the whole brief (voice guide); confirm item syntax varies (not four "Company released X" lines); each item opens on the narrowest concrete fact before any framing word.
- After any direct cuts, run `nb stamp`.

Output: .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/editor/01/editorial-review.md (skill's shape; end with Decision: approve | revise).
