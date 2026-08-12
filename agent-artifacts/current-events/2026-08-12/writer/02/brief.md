# writer brief: current-events/2026-08-12 (02)

Inputs:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/agent-artifacts/current-events/2026-08-12/researcher/02/evidence.md  — the corrected, current claim set (supersedes 01)
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/agent-artifacts/current-events/2026-08-12/editor/01/editorial-review.md  — the editor's routed findings (its 2 direct edits are already in the article; do not undo them)
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/agent-artifacts/current-events/2026-08-12/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/library/current-events/2026-08-12.html  — the article, edit it in place
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/.nb-context/  — template contract

Output:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-12/agent-artifacts/current-events/2026-08-12/writer/02/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/current-events/2026-08-12/library/current-events/2026-08-12.html --series current-events --library /home/user/library-checkout

Apply the editor's routed fixes from the corrected round-02 evidence. This is a
four-item, honestly dated edition: a 12 August publication covering the day's most
consequential recent US news. No reported development lands on the 12th; do not
claim any Tuesday event happened Wednesday.

1. Gilman: correct to the source. Robert Gilman was back in the United States
   Tuesday night (11 August); Trump announced it on Truth Social; he was expected
   to land at Andrews Air Force Base near Washington, D.C. Remove "arrived
   Wednesday" and the Texas military-hospital claim entirely (no source supports
   them). Release owns to the State Department (primary); return details to NBC
   (secondary). Detained since 2022; sentence raised from 3.5 to about 10 years; no
   prisoner exchange.
2. Preska / Epstein records: cite Preska's 11 August 2026 SDNY opinion (Giuffre v.
   Maxwell, 1:15-cv-07433, its CourtListener docket page) as the primary owning the
   holding, plus a wire secondary (Bloomberg/AP/PBS). The docket page is a
   human-clearable gate (403 to bots); record the source's own page. State the
   document scope only as far as the evidence supports (Giuffre-civil records; do
   not assert grand-jury materials if unresolved).
3. Talwani / mail voting: cite the 11 August 2026 D. Mass. preliminary-injunction
   order (League of Women Voters of Massachusetts v. Trump, its CourtListener
   docket page) as primary for the holding, plus Executive Order 14399 from the
   Federal Register (signed 31 March 2026; 91 FR 17125; Section 3(b): USPS shall not
   transmit mail-in or absentee ballots unless the individual is on a State-
   submitted eligible-voter list), plus a wire secondary. Fix any "federal
   eligibility list" shorthand to the accurate mechanism: state-submitted list,
   USPS-enforced. Frame the injunction as a new, distinct district-court action.
4. July CPI: reframe honestly. The July CPI release was scheduled for 12 August
   (8:30 a.m. ET, per the BLS release-schedule primary) but had not posted; there
   is NO July figure to print. Remove any claim that the release "happened this
   morning" and the internal contradiction. Give the verified June baseline (+3.5%
   YoY, -0.4% m/m, core +2.6%) and keep the Fed's hike posture as attributed
   secondary context.

The lead and dek must name the day's honest through-line without implying the
Tuesday developments occurred on Wednesday. Renumber sources in first-citation
order. Keep nb-meta harness "claude-code-routine", model "claude-opus-4-8", dek
identical to the rendered dekline. Run nb stamp, then the full proof (links
included) until BLOCK: 0.
