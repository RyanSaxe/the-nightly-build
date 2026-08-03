# editor review-brief: expert-tools/serena (editor/01)

Inputs:
- editorial-direction.md (artifact root) — the standard to enforce
- writer/01/brief.md (the exact writer brief — for instruction-leakage detection)
- writing-coach/01/voice-guide.md — the voice, licenses, do-not-reuse list
- researcher/01/evidence.md — the evidence to open as an opponent
- writer/01/draft-handoff.md — open the original-work sentence only on the third read
- The article at `library/expert-tools/serena.html` (workspace root) and `.nb-context/` template context
Output: editor/01/editorial-review.md

Recent-pattern notes: recent expert-tools headlines follow "TOOL does X" and
open on an implementation detail; the "Behind the single command sits an
NNN-line script" opener is barred. Check headings for the comma-and cadence.

Round focus:
- Verify the honesty of the central adopt-or-skip judgment: the free default
  LSP backend is materially narrower than the "40+ languages / refactorings"
  banner (move/inline/propagate-deletions and type hierarchy are
  JetBrains-plugin-only/paid; LSP rename symbol-only). Confirm the article does
  not read as marketing and that each capability is stated with its limit.
- Confirm the MCP config is cited to official docs only and every citation's
  href resolves as printed (v1.6.1 cited to CHANGELOG, not the 403 releases tag).
- Confirm the headline and section titles name the tool and the work (series
  requirement) and the one concrete example proves value (not a tutorial).
- Audit data-nb-kind labels (8 primary + 1 secondary claimed) and the code
  listings/table for correctness. Make surgical cuts; route any redraft.
