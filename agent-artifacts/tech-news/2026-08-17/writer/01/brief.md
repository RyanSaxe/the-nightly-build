# writer brief: tech-news/2026-08-17 (01)

Inputs:
- editorial-direction.md   ../../editorial-direction.md (house standard, press voice, series prompt, brief-template identity)
- commission.md            ../../commission.md (selection standard, coordination, recent-pattern habits)
- voice-guide.md           ../writing-coach/01/voice-guide.md (how this brief should sound; exemplar passages)
- evidence.md              ../researcher/01/evidence.md (candidate items with verified sources; read Numbers and Contradictions closely)
- article (edit in place)  /home/user/the-nightly-build/.nb-work/tech-news/2026-08-17/library/tech-news/2026-08-17.html
- effective contract       /home/user/the-nightly-build/.nb-work/tech-news/2026-08-17/.nb-context

Output: /home/user/the-nightly-build/.nb-work/tech-news/2026-08-17/agent-artifacts/tech-news/2026-08-17/writer/01/draft-handoff.md

Proof (run from /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/tech-news/2026-08-17/library/tech-news/2026-08-17.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/b3d5d9d7-6994-5933-851f-0ef1bb302a4b/scratchpad/library-checkout

This round's focus (decisions the evidence carries and must not be lost):
- Select 4-6 items by consequence from the evidence record. Aug 17 itself was quiet; the strongest items sit Aug 10-14, which is fine for a brief that adds what the headline dropped.
- The defensible lead is the cyber vulnerability-finding model cluster: OpenAI's gated, guardrail-reduced GPT-5.6-Cyber against Z.ai's open-weights GLM-5.3, on the capability-vs-governance divergence. Do NOT lead on "another Chinese open model with self-reported benchmarks" — that shape has led the last two briefs and GLM-5.3's numbers are all vendor self-report.
- Every capability figure in both cyber items is vendor-measured and independently unverified (GLM CyberGym 77.2->84.5, the 2,400-vuln claim; OpenAI's 95.0% completion). Say who measured each number; never present a vendor benchmark as neutral fact. Record the parameter-count discrepancy (743B vs 753B) and the one-day launch-date discrepancy honestly or omit the contested figure.
- The two Nature science candidates are login-gated; do not state their figures unless the primary passage is confirmed. If unverifiable, leave them out rather than cite unread numbers.

Coordination: this brief owns developments in the field. Public-consequence items the evidence flags for Current Events (Microsoft Patch Tuesday zero-days, semiconductor capex/financing, the DeepMind leadership change, the HIV therapy result) stay OUT of this brief. Do not duplicate the same-day Current Events lead.

Form: brief template, 4-6 items, per-item at least one primary that owns the development and one independent account; at least 5 sources total; every href resolves to the source's own page. Carry each source's primary/secondary kind into data-nb-kind. Vary the lead construction from the recent "model ships with self-reported benchmarks" headline mold. Fill nb-meta harness and writer-model fields; nb stamp writes counts.
