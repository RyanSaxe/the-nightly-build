# Draft handoff: expert-tools/serena (writer 01)

## Original work

The piece prices Serena's *actual* free-backend capability: it runs the
retrieve-trace-edit arc (`find_symbol` -> `find_referencing_symbols` ->
`replace_symbol_body`) as a single before/after against the grep-and-read path
it replaces, then reads the README's own capability tables back against its
"40 languages / refactoring" banner to show the free default is materially
narrower than it advertises. The evidence record lists those facts separately;
the article turns them into one adopt-or-skip judgment for putting an agent's
write path through the tool. The work is visible in the "free backend" section
(the capability table plus the paragraph that pins the demonstrated arc to the
free tier while the marquee refactorings stay paid) and in the Verdict note.

## Proof

`nb check` with links on (the exact brief command, `--library` pointed at the
checkout) reports **BLOCK: 0, WARN: 0, PUBLISHABLE**. `nb stamp` wrote
words=1685, reading_minutes=7, sources=9 (8 primary + 1 secondary; series floor
is 6).

Note on the stamp command: the brief lists `nb stamp <file> --series
expert-tools`, but `nb stamp` takes only the file argument and rejects
`--series`. Stamped with the file argument alone; the counts are correct and
`nb check` confirms them.

## Warnings intentionally left

None. Six `W-SENTENCE-DENSITY` warnings surfaced on the first proof and all
were resolved by splitting the dense sentences; the final proof is clean.

## Decisions worth flagging to the editor

- **Config cited to official docs only.** The install line and the
  `claude mcp add ...` one-liner come from the maintainers' README and Clients
  docs. The independent review's commands (`serena mcp start`, `~/.claude/mcp.json`)
  and marketplace forms were not used, per the README's own warning and the
  evidence Contradictions section; the drift is instead reported as a friction
  point in the register-server section.
- **v1.6.1 cited to the CHANGELOG, not the release page.** The evidence noted
  the `releases/tag/v1.6.1` page returns 403 to scripted requests. To keep every
  cited URL cleanly resolvable, the v1.6.1 / 2026-07-21 claim is carried by the
  CHANGELOG (s9), which establishes the same release; the release page is not
  cited.
- **Block-diagram source asset not captured.** The evidence offered the README's
  MCP topology SVG. The config listing plus prose already carry "where it
  enters," and the commission asked not to over-furnish, so the furniture set is
  two code listings (config, symbol arc) + one HTML capability table (the
  free-vs-paid contrast, the honest-cost section's core evidence) + one pull
  quote + one Verdict note. If the editor wants the topology shown, `nb asset`
  on that SVG is the intended path.
- **Reviewer gender not assumed.** The evidence names the reviewer only as
  "Andrew"; the draft refers to "the review"/"one reviewer" rather than a
  gendered pronoun.

## Open questions

None blocking. All claims trace to the evidence record; all nine cited URLs are
the resolvable primary/official pages the evidence identified.
