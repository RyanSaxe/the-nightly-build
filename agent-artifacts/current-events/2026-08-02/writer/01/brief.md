# writer brief: current-events/2026-08-02 (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       angle, boundaries, neighbors, source policy
  ../../writing-coach/01/voice-guide.md     wire-terse consequence-item craft and licenses
  ../../researcher/02/evidence.md           the COMPLETE round-2 record; the only claim set available
  the initialized article and its .nb-context (brief template contract + furniture catalogs)
Output: agent-artifacts/current-events/2026-08-02/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Note: use the round-2 evidence record (researcher/02/evidence.md) — it preserves and
supersedes round 1. Article to edit:
  .nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html
Brief template: select 4-6 items; per item exactly one primary + at least one independent
secondary; min 5 sources overall. Iterate proof with --no-check-links, finish with links.

This round's focus (grounded in the round-2 record):
- Five fully-sourced candidates are available: (1) Iran strike cancellation with Iran's
  disputed denial; (2) MI/MN water-system cyberattacks, FBI investigating an Iran link;
  (3) Washington wildfire state of emergency / Spokane complex; (4) visa bond program made
  permanent (Federal Register final rule); (5) federal court blocks Minnesota's
  prediction-market ban. Select 4-6; Twin Falls is documented but recommended for DROP
  (no policy/institutional consequence — fails the "no routine tragedy" test); do not
  include it unless you can justify a genuine consequence, and if you do, attribute the
  5-vs-7 injured contradiction by outlet and timestamp.
- Sourcing caveats to honor precisely (these affect data-nb-kind and how you cite):
  * Iran item's primary is a third-party MIRROR of Trump's own post (trumpstruth.org), not
    Truth Social's page — the editor must judge this; cite transparently as a mirror of the
    primary post, and lean on the independent secondaries (NPR, AP, Times of Israel) for the
    reported facts and Iran's on-record denial.
  * Water-system PSA and the MN court order are corroborated only via direct secondary
    quotation (the federal PSA PDF and the court order were bot-gated). Prefer items whose
    primary you can actually stand behind; if you include these, be honest that the primary
    is quoted through the secondary, and set data-nb-kind accordingly.
  * The cleanest primaries are the Federal Register final rule (visa bonds) and the
    governor's proclamation + InciWeb (wildfire; its per-fire acreage sums to 5,390 —
    use InciWeb's figures, not KHQ's).
- BOUNDARY vs Tech News (same edition): the prediction-market ruling is a court/policy
  story and belongs HERE despite Kalshi/Polymarket being tech-adjacent. Tech News is
  covering in-technology developments; it is NOT covering the EU AI Act or the Anthropic
  supply-chain ruling — if you find either newsworthy as public policy, they are available
  to this brief, but only from a verified primary in the record (do not add un-sourced items).
- Do not re-lead on the standing macro/Fed spine of recent briefs; lead on what is new.
  Vary dek/headings from the banned molds.
- Set nb-meta harness and writer model = sonnet.
