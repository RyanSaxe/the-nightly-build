# researcher brief: expert-tools/grug-far (01)

Inputs:
  ../../editorial-direction.md
  ../../commission.md
Output: researcher/01/evidence.md

Research questions (primary = the repository and its docs; read past the README):
- grug-far.nvim: what it is and the exact mechanism — search results open in one
  editable buffer; editing the Replace field / result lines with live preview;
  syncing edits back to files. Verify from source/docs, not assumption:
  required dependencies (ripgrep) and optional engines (sed default; ast-grep;
  ripgrep --replace), how the engine is selected, and known limits/failure
  modes (huge result sets, unsaved buffers, undo, binary files). Capture the
  actual keybindings/commands and a minimal real config.
- Maintenance health: maintainer, commit cadence, recent releases/changelog,
  open-issue responsiveness, Neovim version requirements. Give concrete, dated
  evidence (latest release/tag, recent commit dates).
- Positioning: what it replaces or enables vs Neovim-native options (`:s`,
  `:cdo`/`:cfdo` over the quickfix list, buffer-based approaches) and vs
  shelling out to sed / ast-grep. Where exactly it enters a workflow. Draw the
  line to ast-grep (covered 2026-07-24): grug-far can *drive* ast-grep as an
  engine; it is the in-editor edit-the-results surface, not a standalone
  matcher.
- A concrete "part that changes the work" the writer can show small: e.g. a
  capture-group replacement across files, or switching to the ast-grep engine
  for a structural rewrite. Provide the exact commands/keys and expected
  behavior.
min_sources 6, prefer primary (code, docs, changelog, issues). Contradictions:
note any gap between the README's claims and actual behavior/limits. Resolve
URLs to the project's own pages (GitHub repo, docs site). If inspection shows
the tool is shallow or unmaintained, say so in your report to the orchestrator.
