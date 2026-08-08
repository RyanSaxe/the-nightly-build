# Draft handoff: tech-news/2026-08-08 (writer 02)

## Original work

Unchanged from writer/01 and still holds: the piece consolidates three
separately reported coding-agent disclosures into one comparison table that
makes the cross-vendor pattern legible in a single view none of the sources
provides — the exploitable layer is the harness, not the model, and the two
scorers even disagree on how bad the Claude Code bug is — and it orders the
whole slate by that same test of what a primary verifies against what a vendor
only announced, which is why the security disclosure leads over the far larger
Terafab dollar figure.

## Editorial request resolved (editor/01, Required work)

- Rewrote the false headline. Old title/h1/item-1 `<h3>` read "A single
  untrusted GitHub issue reached code execution in Claude Code, Gemini CLI, and
  Codex," which distributes "code execution" to all three named tools when the
  record (The Hacker News s3, corroborated by Novee s1) and the article's own
  table establish it only for Gemini CLI (OS command injection, CVE-2026-12537,
  CVSS 10.0); Claude Code's CVE-2026-54316 is credential (API-key) theft and
  Codex's flaw is instruction injection, not direct code execution. New line, in
  all three places (nb-meta `title`, `<h1 class="nb-title">`, and the identical
  item-1 `<h3>` anchor):
  **"One untrusted GitHub issue broke three coding agents at the harness, not
  the model."**
  This centers the harness-as-shared-attack-surface finding the table already
  draws, uses an aggregate verb ("broke") that names no per-tool outcome, and
  drops the triad-headline mold (no comma list of the three tool names). The
  claim is owned by Novee (s1), which the `<h3>` links.

## What changed and what did not

- Changed: nb-meta `title` (line 21), `<h1>` (line 39), item-1 `<h3>` text
  (line 51) — all three now carry the single corrected headline.
- Untouched: the dek (accurate per editor/01) and the nb-meta `dek`, which
  remain byte-identical to each other; the item-1 first paragraph (confirmed it
  still reads as an aggregate "reached remote code execution and credential
  theft," not a per-tool RCE claim); the CVE table; and items 2–4. Claim set not
  expanded.
- `nb stamp` rerun after the edit: words=890, reading_minutes=4, sources=9.
  nb-meta harness `claude-code-routine`, model `Opus 4.8` unchanged.

## Display-text self-test

Headline + subhead re-checked against the evidence record: "three coding
agents" = Anthropic/Google/OpenAI's agents (all sources); "harness, not the
model" owned by Novee s1; no distributed code-execution label; molds clear.

## Proof result

`./nb check … --series tech-news --library <scratchpad>/library`, links
included: **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing.

## Open questions

None blocking. Same standing note as writer/01: the slate is hardware- and
AI-infrastructure-heavy because no in-window (Aug 7–8) peer-reviewed
science/health result cleared the practice-changing bar with a clean primary.
