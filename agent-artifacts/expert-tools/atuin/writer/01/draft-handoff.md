# Draft handoff: expert-tools/atuin (01)

## Original work

The article resolves Atuin's "fully end-to-end encrypted" promise into a bounded
claim the evidence states only in scattered pieces (command text private in
sync, the local SQLite store plaintext at rest, envelope metadata visible to the
server) and ties that boundary, alongside a worked "which commands failed in
this directory" query bash cannot answer at all, to a single test for whether the
swap is worth it: whether the reader queries their history.

## Proof result

`./nb check .nb-work/expert-tools/atuin/library/expert-tools/atuin.html --series
expert-tools --library /home/user/library-checkout` (links included):
**BLOCK: 0, WARN: 0**. No warning left standing.

Stamp: words 1576, reading 7 min, sources 13. nb-meta records
`harness: claude-code-routine`, `model: Opus 4.8`.

## Honoring the researcher's two precisions

- End-to-end encryption is stated as covering the sync payload only. The
  encryption-boundary section and its table say plainly that the local SQLite
  database is unencrypted at rest and that the server sees envelope metadata
  (host id, per-host record counts, timestamps), never command content.
- The only sync frequency named is the shipped source default, five minutes
  (settings.rs), not the docs' "hourly." The unavoidable cost is stated as the
  SQLite database plus the shell hook; the background daemon is described as
  opt-in and default-off.

## Furniture

One `nb-code` shell listing (the bash-vs-Atuin before/after that carries the
value), one `nb-table` (the three-layer encryption boundary), one strong
`Verdict` note. No source asset was captured: the argument spends the recorded
context fields and the search query, not the README demo GIF's TUI view, and the
evidence record itself judges the live shell example the better vehicle for this
CLI tool.

## Open questions

None. The evidence record settled every claim the argument rests on, and no
voice-guide ambiguity surfaced against a concrete sentence.
