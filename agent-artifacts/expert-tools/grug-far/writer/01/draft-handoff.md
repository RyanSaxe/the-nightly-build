# Draft handoff: expert-tools/grug-far (01)

## Original work
The piece isolates the one boundary grug-far's own docs leave scattered — that
the edit-the-results-and-Sync move is a ripgrep-engine feature the ast-grep
engine simply drops — and stages a single worked buffer example at that pivot
(hand-edit some result lines, delete another to skip it, `<localleader>s` writes
exactly those lines back) so the reader watches the state change that separates
grug-far from `:s`, `:cdo`/`:cfdo`, quickfix replace, and a shell `rg | sed`
pipe.

## Proof
`./nb check ... --series expert-tools --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** Stamped: words 1326,
reading 6 min, sources 10 (all primary). Also builds cleanly under `nb preview`.

## Evidence corrections carried
- No sed engine. Default engine is ripgrep; Replace runs
  `rg --replace=... --passthrough`; engine menu is ripgrep / ast-grep /
  ast-grep-rules. The "why it is ripgrep, not sed" section states this against
  `replace.lua`.
- Sync (edit results, write back) is ripgrep-engine only, and disabled under
  `--multiline`/`--multiline-dot-all`. Drawn as the explicit boundary in the
  ast-grep and cost sections.
- Versioning cited from the tag stream (1.6.76, 2026-07-28), with the empty
  Releases tab noted as not-abandonment. Capture syntax cited as `$1`/`${1}`
  (ripgrep GUIDE), not sed's `\1`.

## Warnings left standing
None. Zero warnings.

## Open questions for the orchestrator
- Source asset not used. The evidence flagged the README's results-buffer
  screenshot/GIF as an available visual of the whole thesis, but the voice
  guide licenses the worked-example listing as the pivot form, and a hand-built
  listing is more honest than a cropped third-party screenshot with personal
  editor chrome. If the editor wants the buffer shown as an image, it needs an
  `nb asset` capture from the README and a second round; flagging the choice
  rather than assuming it.
- No open evidence or voice gaps blocked the draft; every display-text claim
  traces to a primary source in the record.
