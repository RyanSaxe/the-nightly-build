# writer brief: current-events/2026-08-11 (02)

Inputs:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writer/01/draft-handoff.md  — your prior draft (3 items)
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/researcher/02/evidence.md  — the new verified 4th item (HUD NOFO vacatur) and the prior record it preserves
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/commission.md
  Article to edit: /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html

Output:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writer/02/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/42af37e2-ce88-5a16-a49b-bb7fb5609b03/scratchpad/library

Add one item to the existing three so the brief runs at four (within the 4-6 band):
the HUD FY2026 Continuum of Care NOFO struck down by the Aug 7 D.R.I. order (Judge
McElroy), using researcher/02's evidence. Preserve the existing three items and the
vaccine-EO lead; renumber sources in first-citation order across all four items with
correct data-nb-kind. Carry the evidence record's caveats into the prose exactly:
it is a vacatur (the NOFO set aside for skipping McKinney-Vento notice-and-comment),
NOT an injunction, and HUD may re-issue after proper process; the "97,000 people"
figure is the plaintiffs' allegation, not a court finding; the order is dated
Aug 7, reported into Aug 10. For the primary href, use the court order's own page /
the closest source's-own-page URL the evidence record records (note the verbatim
text was read via a hosted copy because the court docket was gated); a gated page
that still resolves is fine. Do not add any claim the evidence record does not
carry. Keep the display-text pass and spec/headlines + spec/slop compliance. Re-run
nb stamp and the full proof to BLOCK: 0. Update nb-meta tags if the added item
introduces a new topic; keep writer model = Claude Opus.
