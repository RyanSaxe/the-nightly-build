# writer brief: current-events/2026-08-11 (01)

Inputs:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/editorial-direction.md
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/commission.md  — territory, edition boundaries, habits to break
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writing-coach/01/voice-guide.md
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/researcher/01/evidence.md  — verified candidate items; select 4-6 of the strongest
  Article to edit: /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html
  Template context: /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/.nb-context/  (template-contract.yaml, furniture/)

Output:
  /home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/writer/01/draft-handoff.md

Proof:
  cd /home/user/the-nightly-build && ./nb check .nb-work/current-events/2026-08-11/library/current-events/2026-08-11.html --series current-events --library /tmp/claude-0/-home-user-the-nightly-build/42af37e2-ce88-5a16-a49b-bb7fb5609b03/scratchpad/library

Select 4 to 6 items from the evidence record, leading with the childhood-vaccine
executive order (the day's strongest, best-sourced development). Run only items
whose primary and independent secondary both resolve; drop any candidate whose
sourcing the evidence record marks unverified (e.g. an unconfirmed election
result) rather than running it thin. Each item is one primary plus at least one
independent secondary, with data-nb-kind matching the evidence record. This is a
few-day news frame anchored to 10-11 August; that is normal for the brief, but
lead on genuine recent movement, not backfill. Set the nb-meta tags from the
items you actually run. Fill nb-meta harness and model (writer model: Claude
Opus). Honor the commission's edition boundaries and habits-not-to-inherit.
