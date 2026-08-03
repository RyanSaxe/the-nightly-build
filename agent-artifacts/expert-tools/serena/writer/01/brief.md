# writer brief: expert-tools/serena (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, headline standard, press voice, `article` template identity, series prompt
- commission.md (artifact root) — the tool, what it changes, and shapes to break
- writing-coach/01/voice-guide.md — the voice, licenses, and do-not-reuse list for this piece
- researcher/01/evidence.md — the ONLY claim set available to you; use its Sources/Numbers/Contradictions exactly, including the verbatim config and the symbol-operation arc
- The initialized article at `library/expert-tools/serena.html` (workspace root) and `.nb-context/` (effective template contract + furniture catalogs)
Output: writer/01/draft-handoff.md
Proof (run from repo root, links included):
  `./nb stamp .nb-work/expert-tools/serena/library/expert-tools/serena.html --series expert-tools`
  `./nb check .nb-work/expert-tools/serena/library/expert-tools/serena.html --series expert-tools --library /tmp/claude-0/-home-user-the-nightly-build/d8b08235-82ac-5f6a-8e20-e2e2f6109b0c/scratchpad/library-checkout`
  Iterate with `--no-check-links` while drafting; run the command above (links on) until `BLOCK: 0`.

This round's focus:
- Headline and section titles must name the tool (Serena) and the work it
  changes (series requirement).
- Prove value with ONE concrete example, not an install tutorial: the MCP
  server config (cite to the OFFICIAL docs only — third-party command forms
  drift and the README warns they are outdated) and the symbol-operation arc
  from the source (find_symbol -> find_referencing_symbols ->
  replace_symbol_body). A code listing is the right furniture; escape as HTML.
- State the honest limit in the same breath as the capability (voice guide's
  descending-honesty rule): the free default LSP backend is materially less
  capable than the "40+ languages / refactorings" banner implies — move/inline/
  propagate-deletions, type hierarchy, and interactive debug are
  JetBrains-plugin-only (paid); LSP rename is symbol-only; the language list is
  tiered/experimental; there is a one-time indexing cost. Do not let the piece
  read as marketing.
- Report every number with its source/limit; maintenance signals (stars,
  commits, v1.6.1 2026-07-21) belong where they support the trust judgment.
- Article template: `orientation` required + 2-6 flexible sections + Sources.
  Word band 1200-3000. min 6 sources.
