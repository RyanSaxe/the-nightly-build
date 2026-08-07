# editor review-brief: expert-tools/grug-far (editor/01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../writer/01/brief.md                — the exact writer brief (leakage check)
  ../../writing-coach/01/voice-guide.md   — the craft standard
  ../../researcher/01/evidence.md         — the evidence record
  ../../writer/01/draft-handoff.md        — original-work sentence + open questions
  ../../../../library/expert-tools/grug-far.html   — the article to review
  ../../../../.nb-context/                 — effective template contract + furniture
Output: editor/01/editorial-review.md

Round focus:
- Technical correctness is the top risk. Verify every mechanism claim against
  the evidence record: NO sed engine (ripgrep default; menu ripgrep/ast-grep/
  ast-grep-rules); Sync is ripgrep-engine-only and disabled under multiline;
  capture syntax `$1`/`${1}` (not `\1`); version cited from the tag stream
  (1.6.76, 2026-07-28), not Releases; Neovim >= 0.11.0; ripgrep required,
  ast-grep optional; the `maxSearchMatches` guard. A wrong technical claim in
  display text or a listing is the costliest error — check the worked buffer
  listing and keybindings descriptor by descriptor.
- Confirm the worked example sits at the pivot (results buffer → edit → Sync)
  and proves the move rather than teaching installation; cut any setup line that
  does not.
- Confirm the ast-grep paragraph draws a clean boundary and does not re-tread
  the ast-grep piece (2026-07-24).
- Source-asset question (writer's open item): the writer used a hand-built
  listing instead of cropping a third-party README screenshot. Judge against the
  standard: request a source asset only if an exact visual lets the reader test
  a central argument better than prose; a hand-built listing is legitimate. Do
  not add decoration.
- Formula check: compare headline, dek, and section headings against recent
  expert-tools pieces (visidata, serena, files-to-prompt, oil-nvim, ast-grep,
  py-spy). Catch the "though the free backend is narrower than…" dek hedge and
  the "Tool does concrete X" headline mold if it reads stamped.
Make surgical cuts directly; run ./nb stamp after direct cuts. Route new prose,
markup, assets, or proof to the writer. Decide approve | revise.
