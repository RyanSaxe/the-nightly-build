# editor review-brief: expert-tools/atuin (01)

Inputs:
- `agent-artifacts/expert-tools/atuin/editorial-direction.md`
- `agent-artifacts/expert-tools/atuin/commission.md`
- `agent-artifacts/expert-tools/atuin/writer/01/brief.md`
- `agent-artifacts/expert-tools/atuin/writing-coach/01/voice-guide.md`
- `agent-artifacts/expert-tools/atuin/researcher/01/evidence.md`
- `agent-artifacts/expert-tools/atuin/writer/01/draft-handoff.md`
- `.nb-work/expert-tools/atuin/library/expert-tools/atuin.html`
- `.nb-work/expert-tools/atuin/.nb-context/`

Output: `agent-artifacts/expert-tools/atuin/editor/01/editorial-review.md`

Recent-pattern notes: recent expert-tools pieces headline with the tool name plus
a present-tense verb (acceptable, but flag if the rhythm is copied) and close on a
maintenance-and-trust section whose heading is built from a stat or the maintainer
count ("What it costs, and whether to trust it", "One maintainer ships every
release..."). Flag that closing mold and the install-count-in-headline device as
formula.

This round's focus: verify the two precisions the evidence record insists on — the
end-to-end encryption protects the sync payload only (the local SQLite store is
unencrypted at rest; the server sees envelope metadata), and any named sync
frequency uses the shipped source default (5m), not the docs' "hourly". Confirm
the shell example is correct and that it demonstrates a query a flat history
cannot answer. Confirm maintenance/trust is covered as the prompt requires.
