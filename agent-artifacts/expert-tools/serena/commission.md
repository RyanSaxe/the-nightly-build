# Commission: expert-tools/serena

## Assignment
- Series: expert-tools (Expert Tools). Template: `article`. Mode: open.
- Slug: `serena`. Tool: **Serena** (oraios/serena) — an open-source MCP server
  / agent toolkit that gives coding agents semantic, LSP-backed code retrieval
  and editing tools (find_symbol, find_referencing_symbols, symbol-level
  edits) instead of raw file reads and text search.
- Authorized by the 2026-08-03 `nb duty` result. One article only.

## Why this tool, and the rotation
The series rotates roughly across Python packages, Neovim plugins, and
AI-harness extensions. The last five picks were files-to-prompt (Python CLI),
oil.nvim (Neovim), pydantic-monty (Python), ast-grep (CLI), py-spy (Python).
An AI-harness extension is the under-served family. Serena is a strong,
easy-to-miss find: it plugs into any MCP-speaking harness (Claude Code, Codex,
Cursor, etc.) and changes how an agent navigates a codebase — semantic symbol
operations over a language server rather than dumping whole files into context.
NOTE: `pydantic-monty` was already published 2026-07-27, so it is off the table.

## Required contribution
Read past the README. Inspect the implementation, the documented tool set, the
project history, and real usage:
- Name precisely what Serena changes in the workflow: token-efficient,
  symbol-level navigation and edits via the Language Server Protocol, versus an
  agent grepping and reading files. Show *where it enters* an agent workflow
  (configure it as an MCP server) and *what it replaces or enables*.
- Prove the value with ONE concrete example — a harness/MCP integration snippet
  and a symbol-level operation (e.g. `find_symbol` / `find_referencing_symbols`
  / a symbol replace) — not an installation tutorial. The example should show
  the part that changes the work.
- State adoption cost honestly (language-server availability per language,
  indexing/first-run cost, project setup, MCP client support) and whether it is
  maintained well enough to trust (release cadence, activity, backers).
- Name the tool and the work it changes in the headline and section titles
  (series requirement).

## Sources
- min_sources: 6 (article template floor). Primary: the Serena GitHub
  repository (README, source, docs, releases) — it owns claims about what the
  tool does; and the Model Context Protocol spec/docs for the MCP integration
  claims. Secondary: independent write-ups or comparisons for context and real
  usage. Cite implementation/doc claims to the repo at a resolvable URL (a
  specific file/section where possible). Every URL must resolve.

## Neighbors in this edition
paper-of-the-day/chinchilla and the tech-news brief also touch AI. Keep this a
practitioner tool piece, not an AI-industry story.

## Prior coverage — do not repeat, and break these shapes
Recent expert-tools headlines follow "TOOL does X to the work" and open on a
concrete implementation detail (line counts, defaults). That pattern is
series-appropriate; keep the concreteness but do not copy a specific opener
(e.g. "Behind the single command sits a NNN-line script"). Vary heading shapes
from the recent set.

## Form
Article template: `orientation` required section + 2-6 flexible sections +
Sources. Word band 1200-3000. A code listing is the natural furniture for the
MCP config and the symbol operation; use it where the code's behavior is the
evidence, escaped as HTML. Do not over-furnish.

## Harness / model record
Harness: Claude Code (Agent SDK), scheduled publication run. Roles run as
isolated subagents on `claude-opus-4-8` (satisfies `capable`/`inherit`).
Per-role reasoning effort is not independently settable through the subagent
interface; each role runs at the session's effort, the closest available option
to the policy's guidance. Editor: model inherit -> `claude-opus-4-8`, effort
target high (ran at session effort). Recorded as a deviation on effort only.
