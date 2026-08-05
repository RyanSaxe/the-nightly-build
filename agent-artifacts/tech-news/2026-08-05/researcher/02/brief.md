# researcher brief: tech-news/2026-08-05 (02)

Inputs:
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/editorial-direction.md — citation standard, series territory, declared reader
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/commission.md — selection standard, sourcing, non-overlap boundaries
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/researcher/01/evidence.md — your prior evidence (preserve its still-valid work: Qwen3.8-Max is a keeper)

Output: /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/researcher/02/evidence.md
(Write a COMPLETE new evidence record that preserves still-valid entries and adds the new findings. Do not overwrite researcher/01.)

Run environment: harness = claude-code, model = capable, high effort. Web search and fetch available. Today is 2026-08-05.

Why a second pass: the writer found that TWO of the round-01 spine items — DeepSeek-V4-Flash-0731 and Inkling-Small — were ALREADY PUBLISHED as full items in `tech-news/2026-08-03`, so they cannot be re-filed as new. Only Qwen3.8-Max survives as genuinely new. The `brief` band requires 4-6 items, so we need at least 3 MORE genuinely-new, uncovered field developments.

Focus:
- FIRST, read what the recent editions already covered so you exclude them. Run `./nb history --structure tech-news/2026-08-03` and `./nb history --structure tech-news/2026-08-04` (and 08-02 if useful) and list the items/subjects already filed. Any candidate that duplicates one of those is out unless there is a genuinely new, sourced post-publication turn.
- Cast a WIDER net than round 01, for developments dated ~Aug 3-5, 2026, from PRIMARY records:
  - **arXiv** cs.LG / cs.AI / cs.CL new listings for the first days of August — a notable method/result/model paper that changes technical knowledge or practice (read the abstract + key result firsthand; verify the headline number in the paper).
  - **Science/health** results that change practice (Nature / Science / bioRxiv / a major lab or agency) — treat the research itself as the development.
  - **Systems / chips / infrastructure** with technical substance (a real launch or benchmark with an owning primary), not product promotion.
  - **Security research** with field consequence (a disclosed vulnerability class, a serious result).
- For each new candidate: an owning PRIMARY + at least one independent secondary; verify every number against the primary; distinguish vendor claim from independent verification; confirm each URL resolves to the source's own page. Aim to hand the writer a set from which a 4-6 item brief (including Qwen3.8-Max) can be built with DISJOINT subjects (not four model-release items of one shape).
- Keep the round-01 non-overlap flags (EU AI Act GPAI → opinion; Anthropic supply-chain ruling & CareCloud breach → current-events; no 2020-diffusion history → paper-of-the-day).
- If, after a genuinely wide search, fewer than 3 additional qualifying items exist, say so explicitly and list what you checked (arXiv, which venues, which dates) so the orchestrator can rule on scope — do not pad with promotion or re-filed items.
