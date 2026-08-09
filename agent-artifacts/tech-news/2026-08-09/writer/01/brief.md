# writer brief: tech-news/2026-08-09 (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, brief template, series prompt
- ../../commission.md — the selection rule, source floor, and the Current Events boundary
- ../../writing-coach/01/voice-guide.md — how this brief should sound
- ../../researcher/01/evidence.md — the verified candidates, their independent-confirmation limits, and the lane flags
- article: .nb-work/tech-news/2026-08-09/library/tech-news/2026-08-09.html (initialized; edit it)
- template context: .nb-work/tech-news/2026-08-09/.nb-context/ (contract, runtime assets, furniture)

Output: draft-handoff.md (this directory)

Proof: ./nb check .nb-work/tech-news/2026-08-09/library/tech-news/2026-08-09.html --series tech-news --library /tmp/claude-0/-home-user-the-nightly-build/6bc74823-8205-56b3-a297-6e1aa55fabb3/scratchpad/library-checkout

This round's focus:
- Run four to six items; the evidence carries more candidates than you need. No first-party primary is dated 7-9 August, so this is a Sunday edition covering the week's developments (1-6 August window); that is appropriate, but do not imply a story broke today.
- Do not reflex into the AI-security beat as the lead. Lead with the more consequential development (the OpenAI "Astra" Lean-verified proofs, or the rhombohedral-graphene superconductivity result); hold the UK AISI rogue-agent report and the Langflow RCE off the lead if you run them at all.
- Two items are vendor claims about the vendor's own systems (OpenAI Astra; Alibaba Qwen3.8-Max). Treat each as primary only for what the vendor did, and say plainly where independent confirmation is partial: Astra's certificates are Lean-checkable but unrefereed, and Qwen's benchmarks are vendor-reported. Do not print a vendor benchmark as an established result.
- Lane separation with Current Events (runs tonight): keep the open-weights security-review exemption (policy) and the New Mexico Meta child-safety order (legal) out. The Terafab chip-fab story is available to you as a tech-industry item if you want it — Current Events is not covering it — but it is optional.
- Deks and headings: one lean dek that commits to the lead and names the actor; no three-clause comma-and-"and" dek; do not open the lead on the recent "...not the model" located-reversal mold. Verify every version, parameter count, and benchmark against the primary. Run the display-text pass, then `nb stamp` and the exact `nb check` (links included) until BLOCK: 0.
