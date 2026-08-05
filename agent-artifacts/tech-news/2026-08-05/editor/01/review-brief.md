# review-brief: tech-news/2026-08-05 (editor/01)

Inputs:
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/editorial-direction.md — governing standard, `brief` identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writer/02/brief.md — the exact writer brief (instruction-leakage checks; carries the authorized relaxed-window scope)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writing-coach/01/voice-guide.md — voice guide (read FIRST)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/researcher/04/evidence.md — THE current evidence record (round 04); earlier rounds superseded
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/writer/02/draft-handoff.md — handoff + original-work sentence + 2 open questions
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/library/tech-news/2026-08-05.html — the article to review (make direct cuts HERE)
- /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/tech-news/2026-08-05/agent-artifacts/tech-news/2026-08-05/editor/01/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort (REQUIRED stage).

Context you need: this was an unusually thin AI-news day. The week's biggest field items were already
published 08-01…08-04 (do not expect them here; re-filing any would be the error). The orchestrator
authorized a relaxed window (~Jul 15–Aug 5), so the four items carry DIFFERENT true dates — that is
intended, not a defect. Verify the framing states each date honestly and NOTHING implies all broke Aug 5.

Recent-pattern notes:
- Check the last couple of tech-news deks/leads (`nb history --structure tech-news/2026-08-04`) and confirm this brief breaks their shapes; watch the dek for banned molds and scaffolding subheads.

This round's focus:
- **The core risk is the vendor-only Qwen3.8-Max numbers.** Confirm EVERY Qwen score is attributed to Alibaba ("Alibaba reports…"), never printed as fact; the benchmark table (if kept) must be captioned vendor-only / unreproduced / mixed-harness, and the prose must note the weights are not yet public and no license as of Aug 5. RULE on the writer's open question 2: does the Qwen table amplify unreproduced numbers despite its caption? If yes, request it cut to prose (writer); if the caption honestly frames it as the very thing the item is about (an unverifiable vendor claim), it may stay. Also confirm GPT-5.6 Sol / Claude Fable 5 appear ONLY as Alibaba's comparison baselines, not re-filed as items.
- **Verify display text and load-bearing numbers** against the owning primary or, where the primary is gated (Cell 403; Nature auth-redirect; Light gated), the named independent secondary — and that the printed href is the source's OWN page (paywall = gated, not dead; open each). The contested QD temperature must read "about 12 kelvin" (not 12.4/12.5), attributed; the interference visibility 0.65 ± 0.14 must carry its interval (voice-guide license).
- **Audit data-nb-kind per item: exactly 1 primary + ≥1 INDEPENDENT secondary.** The writer marked the institutional PRs (Rockefeller, École Polytechnique) as `secondary` (a second `primary` would trip the source-kind rule) with independence resting on the true independent secondaries — confirm each item's independent secondary is genuinely independent authorship, not the institution that produced the result.
- **Non-overlap:** confirm no EU AI Act GPAI argument (→ opinion), no N-able CVE (→ current-events), no re-filed 08-01…08-04 item.
- Open question 1 (photonics adjacency of items 3 & 4): both are distinct results/groups and each clears sourcing; the band floor is 4 and no fifth in-window item exists, so both are needed. Accept unless one genuinely fails on its own merits — do not drop below 4.
- Second read (cut): enforce prose/punctuation; the leads should fuse development+significance per the voice guide; the verifiability through-line should be SHOWN in the ordering/leads, not asserted as a graded thesis. Third read: what does the brief give beyond the items (the original-work synthesis), closer to the voice-guide exemplars than a median summary? Reread the headline as the largest claim (it must be one the evidence supports — Qwen's is framed as "ships without the weights or the proof").
- After any direct cuts run `nb stamp`. Decision: approve or revise, naming each required item's owner (researcher for evidence; writer for prose/framing/table).
