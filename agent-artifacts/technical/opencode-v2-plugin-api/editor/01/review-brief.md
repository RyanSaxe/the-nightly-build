# editor review-brief: technical/opencode-v2-plugin-api (01)

Inputs (read the voice guide first; open the evidence record when a concern calls):
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- commission.md (../../commission.md) — INCLUDING the "Orchestrator decision (after
  researcher/01)" section with the code-exact verified facts and corrections
- the exact writer brief (../../writer/01/brief.md)
- draft-handoff.md (../../writer/01/draft-handoff.md)
- recent-patterns.md (../../recent-patterns.md)
- evidence.md (../../researcher/01/evidence.md)
- The article: .nb-work/technical/opencode-v2-plugin-api/library/technical/opencode-v2-plugin-api.html

Output: ./editorial-review.md, decision approve | redraft.

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/technical/opencode-v2-plugin-api/library/technical/opencode-v2-plugin-api.html --series technical --repo /home/user/the-nightly-build

You decide whether this publishes. Correct, reads well, good reading experience.

Watch especially (from the research):
- Code correctness: every package name, version, import path and signature must match
  the verified record. The published import is "@opencode/plugin" (+ "/effect"); the
  repo-internal "@opencode-ai/plugin/v2/*" path must NOT appear in reader-facing code.
  `Plugin.define({ id, setup })` and `{ id, effect }` shapes exactly.
- No overclaiming: the piece must state that v2 has not displaced v1 (v1 ~25.7M vs v2
  ~174k weekly downloads, ~147:1) and that migration is real but early. "Published to
  npm 2026-09-11/12", not a vendor "GA".
- Documented-but-unverified details (several hook names, subdirectory autoload, the
  load-error string, "v1 silently skipped under v2") must be marked as documented/
  reported, not stated as verified fact.
- Illustrative code labeled illustrative; captions factual and cited.
- Headline/dek per spec/headlines.md; avoid the antithesis "X not Y" mold and the
  paired-heading rhythm flagged in recent-patterns.md.

Open every citation href as printed. Confirm BLOCK: 0 after edits; if you change the
dek keep nb-meta's dek identical to the dekline and rerun `nb stamp`. Report the review
path and decision.
