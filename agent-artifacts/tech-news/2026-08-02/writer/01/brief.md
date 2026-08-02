# writer brief: tech-news/2026-08-02 (01)

Inputs:
  ../../editorial-direction.md              house + headline standard, press voice, series prompt
  ../../commission.md                       angle, boundaries, neighbors, source policy
  ../../writing-coach/01/voice-guide.md     wire-terse item craft and licenses
  ../../researcher/01/evidence.md           the evidence record; the only claim set available
  the initialized article and its .nb-context (template contract + furniture catalogs)
Output: agent-artifacts/tech-news/2026-08-02/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout

Article to edit:
  .nb-work/tech-news/2026-08-02/library/tech-news/2026-08-02.html
Brief template: select 4-6 items; per item exactly one primary + at least one independent
secondary; min 5 sources overall. Iterate proof with --no-check-links, finish with links.

This round's focus:
- Select the strongest in-technology developments from the evidence (GPT-5.6 self-tuned
  inference kernels and the price passthrough; DeepSeek-V4-Flash release and pricing;
  RFC 10015 banning RSA/DHE in TLS 1.2; Gemini Robotics 2). Weaker candidates (Seedance
  2.5, Kimi-K3-on-MI355X, the Cisco CVE) are optional and carry the caveats the record
  flags — use only if they earn a slot, and never state a vendor's unverified throughput
  number as fact.
- BOUNDARY: do NOT cover the AI-*policy* items the record flagged as Current-Events
  territory — the EU AI Act Article 50 transparency rules and the federal ruling on the
  Pentagon's supply-chain designation of Anthropic. Those are routed to the same-day
  Current Events brief so the edition covers each once. Keep Tech News on developments
  *in* technology.
- Respect the record's sourcing caveats: section-level locators where noted; DeepSeek
  parameter count is inconsistently reported (284B vs 304B) — attribute or avoid the exact
  figure; the Opus 4.8 $25/M comparator could not be verified, so do not state it as fact.
- Do not re-lead on the crypto-flaw / AI-agent-CVE pattern of the last several briefs
  unless 08-02 genuinely advanced it (it did not, per the record). Vary dek/headings from
  the banned molds.
- Set nb-meta harness and writer model = sonnet.
