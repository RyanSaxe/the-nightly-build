# writer brief: current-events/2026-08-11 (03)

Inputs:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/editor/01/editorial-review.md  — the routed fixes and the editor's own direct edits (already in the article)
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/researcher/03/evidence.md  — the resolved owning primaries and exact URLs
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writer/02/draft-handoff.md
  Article to edit: /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html

Output:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writer/03/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/42af37e2-ce88-5a16-a49b-bb7fb5609b03/scratchpad/library

Apply exactly two sourcing fixes from researcher/03; preserve the editor's direct
edits and all other settled prose.

Item 3 (National Guard): the old primary (Senate HSGAC report) is wrong — drop it.
Reframe the item to LEAD on the crime record with MPD as the single owning primary:
  https://mpdc.dc.gov/dailycrime  (District Crime Data at a Glance: violent crime
  +3%, 1,600->1,655; property crime -23%, 14,031->10,830, as of 10 Aug 2026),
independent secondary = Stars and Stripes (the existing s6). CRITICAL: this series
requires EXACTLY ONE primary per item. So MPD is the item's only data-nb-kind=
"primary". Keep any cost/projection detail only as brief context attributed to a
SECONDARY (Stars and Stripes for the ~$55M/month CBO figure; if you keep the
~$1.43B projection, cite Roll Call
https://rollcall.com/2026/08/04/pentagon-national-guard-in-dc-to-cost-another-1-43-billion/
as a secondary) — do NOT add CBO or the Niskanen study as a second primary. Given
researcher/03 flags a troop-count conflict (CBO ~2,400-2,950 vs the old "800->9,700"),
trim the troop-count sprawl or state only what an owner supports; do not leave an
unreconciled number. Keep the item tight.

Item 4 (HUD): repoint s7 (keep data-nb-kind primary) from the NY AG hosted copy to
the court's own RECAP copy:
  https://storage.courtlistener.com/recap/gov.uscourts.rid.62592/gov.uscourts.rid.62592.41.0.pdf
(confirmed HTTP 200, Document 41, D.R.I. 1:26-cv-00439/-00436).

Renumber sources only if the set changes; keep exactly one primary per item and each
data-nb-kind correct. Do not add claims beyond researcher/03's record. Redo the
display-text pass on the changed item, then nb stamp and run the FULL proof to
BLOCK: 0. One line per fix in the handoff; writer model = Claude Opus.
