# writer brief: tech-news/2026-08-04 (01)

Inputs:
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/editorial-direction.md — governing standard, `brief` template identity, series prompt, declared reader
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/commission.md — selection standard, sourcing, non-overlap boundaries
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writing-coach/01/voice-guide.md — craft standard and licenses (cap the one hedge-contrast; vary item syntax)
- .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/researcher/01/evidence.md — verified candidate items with primaries; cite only what it opened; use Numbers exactly
- .nb-work/tech-news/2026-08-04/library/tech-news/2026-08-04.html — the initialized brief to edit
- .nb-work/tech-news/2026-08-04/.nb-context/ — effective template contract and furniture catalogs

Output: .nb-work/tech-news/2026-08-04/agent-artifacts/tech-news/2026-08-04/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-04/library/tech-news/2026-08-04.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/2d5b8802-c025-5b79-bf1d-234ffd5a3463/scratchpad/library-checkout

Focus:
- Select the final 4-6 items (band 4-6; each exactly 1 owning primary + ≥1 independent secondary). Recommended spine from the researcher's candidates, varied by kind: (1 LEAD) OpenAI "Astra" Lean-verified proofs of 10 open math/TCS problems; (2) the AI-for-science coding-agents field report; (3) Feinstein Institutes human vagus-nerve atlas (non-AI variety, changes practice); (4) Cisco FMC zero-day; plus optionally (5) Epoch AI's ~9-month AI-supercomputer performance doubling. Drop Qwen 3.8 Max (no resolved primary). 
- MUST-OPEN gated primaries before publishing: several owner pages (openai.com index pages, science.org, feinstein.northwell.edu) returned 403 to the researcher's fetch tool. Open each owning primary yourself (browser-style) and confirm the specific claim before you cite it. Record the source's own canonical page as the href, not a fetch endpoint or a mirror, unless only a mirror resolves — then use the resolving independent account and mark kinds honestly.
- Number corrections the researcher caught, use exactly: the EXPLOITED Cisco CVE is CVE-2026-20316 (CVSS 5.3, chainable), NOT the CVSS-10 pair (20079/20131) — do not conflate them. The ~$200bn Google/Anthropic compute-financing figure is FT-owned reporting, not a company disclosure — so if you were to use it, it is secondary; but that story is current-events territory this edition, so leave it out to keep the briefs disjoint.
- Non-overlap: keep items disjoint from current-events (which covers policy/consequence stories) and from paper-of-the-day (the ResNet reconstruction). No item should be a foundational-paper explainer; these are current developments.
- For every research result, the primary is the paper/repo/dataset, not the press release — open it. Resolve arXiv/GitHub/dataset URLs to their own pages.
- Voice guide: open each item on the narrowest concrete fact (number/date/document) before any framing word; name the verifying check inside the same clause; cap the single earned hedge-contrast across the whole brief; vary syntax item to item (not five "Company released X, beating Y" lines). Avoid colon subtitles and the comma-triad dek; check recent tech-news deks (in commission).
- Name the piece's one act of original work (real synthesis across items, not mere selection) in draft-handoff.md.
