# writer brief: expert-tools/grug-far (01)

Inputs:
  ../../editorial-direction.md            — house/press/template/series standard
  ../../commission.md                     — subject, angle, boundaries
  ../../writing-coach/01/voice-guide.md   — the craft standard for this piece
  ../../researcher/01/evidence.md         — the complete claim set; cite only this
  ../../../../library/expert-tools/grug-far.html   — the initialized article to edit
  ../../../../.nb-context/                 — effective template contract + furniture catalogs
Output: writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/expert-tools/grug-far/library/expert-tools/grug-far.html --series expert-tools --library /home/user/library-checkout

Corrections the evidence record overrides the commission on (follow the evidence):
- There is NO sed engine. The default replacement engine is ripgrep
  (`rg --replace=… --passthrough`); the engine menu is ripgrep / ast-grep /
  ast-grep-rules. Do not describe a sed backend.
- Sync (editing result lines and writing them back to disk — the tool's
  signature move, Sync All) is supported by the ripgrep engine only; the
  ast-grep engine has no sync. Show the signature move on the ripgrep engine.
- Cite the tag stream (latest 1.6.76, 2026-07-28), not the empty Releases tab.
  Requires Neovim >= 0.11.0; ripgrep required, ast-grep optional. Capture-group
  syntax is `$1`/`${1}`.

Focus:
- One worked example placed at the pivot (results-as-editable-buffer → edit →
  Sync back), per the voice guide; cut setup lines so it proves the move, not
  an install. Draw the ast-grep line in one paragraph (grug-far can drive
  ast-grep as an engine; it is the in-editor edit-the-results surface).
- Name where it enters a workflow, what it replaces/enables vs `:s`,
  `:cdo`/`:cfdo`, quickfix replace, and shelling out; the honest cost
  (dependencies, the `maxSearchMatches` guard, sync limits); and maintenance
  health. Name the tool and the work it changes in headline and section titles.
Recent shapes to break (do not inherit): expert-tools headlines are "Tool does
concrete X"; find grug-far's own concrete surprise. Avoid the recurring
"though the free backend is narrower than…" dek hedge. Give code listings only
where a listing is the clearest form; keep them minimal and real.
