# Commission: expert-tools/grug-far

## Subject
**grug-far.nvim** — a Neovim plugin for project-wide search and replace whose
results open in a single editable buffer: you edit the matches as text and the
plugin writes those edits back across every file. Backed by ripgrep for search
and by an interchangeable replacement engine (sed by default, with ast-grep and
ripgrep's own `--replace` selectable), plus live preview and flag controls.

## Why this tool (fits the prompt)
- Niche and powerful: not a default; changes a real workflow (project-wide
  find-and-replace) by turning the result set into a text buffer you edit and
  sync, instead of a fire-and-forget `:s` or a shell one-liner you cannot
  review before it lands.
- Rotation: the recent run leaned Python/CLI/agent tools (visidata, serena,
  files-to-prompt); the last Neovim pick was oil.nvim (2026-07-29). This
  returns to Neovim. oil.nvim's idea (edit a filesystem listing as text) is a
  useful cousin to name in one sentence, not to repeat: grug-far edits search
  *results* as text.

## The part that changes the work (show it small)
Show the move that matters in a small, real Neovim example: open grug-far on a
pattern, see matches across files in one buffer, edit the Replace field (or the
result lines) with live preview, then sync to disk. Show one thing prose
cannot: e.g. using a capture-group replacement, or switching the engine to
ast-grep for a structural rewrite that skips look-alikes in strings/comments.
The example proves value; it is not an install tutorial.

## What the article must establish (per prompt)
Read past the README: inspect the implementation, docs, history, and real
usage. Say where it enters a workflow, what it replaces or enables (vs. `:s`,
`:cdo`, `:cfdo`, quickfix-based replace, or shelling out to sed/ast-grep), what
adopting it costs (dependencies: ripgrep required; ast-grep/sed optional;
learning the buffer model; failure modes on huge result sets or unsaved
buffers), and whether maintenance is healthy enough to trust (commit cadence,
maintainer, issue responsiveness, release history). Name the tool and the work
it changes in the headline and section titles.

## Honesty guardrail
The researcher must verify current behavior against the actual repository
(README, source, docs site, changelog, issues) rather than assume. If deep
inspection shows the tool is shallow, unmaintained, or materially overlaps a
recently covered tool (notably ast-grep, 2026-07-24) in a way that leaves
nothing distinct to teach, flag the orchestrator before drafting rather than
padding.

## Boundaries
- article template; band 1200-3000 words; min_sources 6. Sources are the repo,
  its docs/changelog/issues, the engines it drives (ripgrep, ast-grep, sed),
  and any substantive third-party writeups; prefer primary (the code and docs).
- A code listing of the Neovim config/keys and of a before/after replacement is
  the natural furniture. Keep listings minimal and real.

## Neighbors in this run
Six other articles; only this is a developer tool. Distinct from ast-grep by
angle: that piece was a standalone CLI AST rewriter; this is the in-editor,
edit-the-results surface (which can *drive* ast-grep). Draw the line explicitly
once.

## Habits not to inherit (recent expert-tools)
- Headlines are "Tool does concrete X" — good; find grug-far's own concrete
  surprise (editing search results as a buffer, or the sync step), not a copy.
- Deks that hedge with "though the free backend is narrower than..." recur.
  Write a dek that identifies this tool unmistakably.
