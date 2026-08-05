# writer brief: current-events/2026-08-05 (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/editorial-direction.md — governing standard, `brief` template identity, series prompt, declared reader
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/commission.md — selection standard, sourcing, non-overlap boundaries
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writing-coach/01/voice-guide.md — craft standard and licenses (clause-level compression: finding+stake in one main clause; folded attribution; load-bearing-word quote)
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/researcher/01/evidence.md — 7 verified candidates (+1 unverified international); cite only what it opened
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/library/current-events/2026-08-05.html — the initialized brief to edit
- /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/.nb-context/ — effective template contract and furniture catalogs

Output: /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/agent-artifacts/current-events/2026-08-05/writer/01/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/current-events/2026-08-05/library/current-events/2026-08-05.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Run environment: harness = claude-code, model = capable (Opus-class), medium effort.

Focus:
- Select the final 4-6 items (brief band 4-6; each item exactly 1 primary + ≥1 independent secondary). Favor law/policy/institutions/material-conditions consequence.
- **Critical shape caution from the researcher: four of the seven candidates are Democratic-state-vs-Trump legal actions all dated Monday Aug 3 (Section 301 tariff suit; voter-registration injunction; NY mask-law injunction; TANF-data suit) — distinct subjects but ONE shape. Selecting more than TWO makes the front page read as a single story.** Build a spine of DISJOINT shapes. A strong disjoint spine: (1) the record June trade deficit ($73.3B, BEA/Census, released Aug 4 — primary opened); (2) the deadly cyclosporiasis outbreak (CDC: first 2 deaths, 10,468 cases, 517 hospitalizations, 47 states, iceberg-lettuce/Taylor Farms recall — primary opened); (3) ONE tariff/court item (the 25-state Section 301 suit, NY AG filing opened); (4) the Spokane Old Trails Fire arson charge (Aaron Farinacci, 37; ~700 structures; ~65,000-67,000 evacuated) as an institutions/material item of a different shape. Add at most one MORE legal action only if you confirm its docket (see below), and only if it earns its place over the above.
- **Verification: three of the four legal candidates (voter-registration, NY masks, TANF data) were verified only through party statements and independent reporting — the courts' own orders/complaints were NOT opened.** If you file any of them, either open the docket/order yourself and cite it as the primary, or attribute the holding to the party/independent reporting and file the status as reported (do not assert a court holding you have not read). The voter-registration ruling DATE is itself contested (Aug 3 vs Aug 4) — state it honestly or omit the day.
- **Do NOT file the Iran/Hormuz international item** — the researcher could not verify it (CNN/Reuters geo-blocked). Omit it rather than print unverified international claims. (Series prompt: include international only when omitting it misleads; an unverifiable item does not qualify.)
- Verify every number/name/title/date against the owning primary (trade-deficit figure and revision; CDC case/death/hospitalization counts and state total; the exact filing court — Court of International Trade; the arson defendant's exact name/age/charge). A wrong title or number in display text is the costliest error. Confirm each source href resolves to the source's own page.
- Non-overlap: no AI/tech field development here (→ tech-news); no AI-governance argument (→ opinion). The researcher found no such items anyway.
- Headline/dek per the voice guide: fuse finding+stake into the lead's main clause; actors named; no colon subtitle, no comma-triad/semicolon-reversal/suspended-question dek, no scaffolding subheads. Use `nb history --structure current-events/2026-08-04` (and a prior day) to check recent deks/leads and break those shapes.
- Name the piece's one act of original work (a real synthesis across the items, not mere selection) in draft-handoff.md. Run `nb stamp` then the exact proof to BLOCK: 0, links included.
