# Researcher brief — expert-tools/files-to-prompt (01)

## Role
Load and follow `skills/researcher/SKILL.md`. High effort. Web access. You may
also install and RUN the tool for real to capture true output (you have a shell;
`uv`/`pip`/`pipx` available; the environment has network for package installs).

## Begin with these exact inputs
- `agent-artifacts/expert-tools/files-to-prompt/editorial-direction.md`
- `agent-artifacts/expert-tools/files-to-prompt/commission.md`

## First: confirm or challenge the pick
Inspect `github.com/simonw/files-to-prompt` past the README — the source code,
recent releases, commit history, open/closed issues, and real usage reports.
Decide whether it still qualifies as niche + powerful + trustworthy-maintained
as of 2026. If YES, proceed. If NO (now a default, unmaintained, or only-popular),
STOP and return `REQUEST correspondent <one-sentence finding + proposed fallback
(symbex or a better niche AI-harness tool)>` so the correspondent can redirect.

## Verify (open the source / run it)
1. **What it does mechanically.** Read the actual implementation: how it walks
   paths, honors/ignores `.gitignore`, the `--ignore`/`--extension`/include-hidden
   flags, binary detection, and the output formats (default, `--cxml` Claude XML,
   `-m`/markdown, line numbers). Confirm exact flag names and behavior against the
   source, not memory.
2. **A real run.** Install it and run it on a small real subtree (e.g. a few files
   from this repo's `engine/` or a scratch dir). Capture the ACTUAL command and a
   trimmed slice of the ACTUAL output for `--cxml` and default modes, so the
   writer can show a truthful example. Note token/size behavior if observable.
3. **Where it fits / what it replaces.** Confirm how it pipes into an LLM (e.g.
   `files-to-prompt ... | llm -m ...`), and the concrete pain it removes vs
   hand-assembled context.
4. **Maintenance & provenance.** Latest version + date, release cadence, author,
   license. Cite the release notes / changelog.
5. **Costs & limits.** No semantic selection, manual scoping, any gotchas from
   issues.

## Source floor & classification
Minimum 6 sources, read and resolving. Primary = the repo source/releases and
the author's own posts and your real run's output; secondary = independent
usage accounts. Classify each with a one-line reason. Never record an unread URL.

## Output (write only this)
`agent-artifacts/expert-tools/files-to-prompt/researcher/01/evidence.md`
Include: the confirmed pick decision; verified mechanics with source locators
(file/line or docs section); the real command(s) and captured output blocks
ready for the writer to quote as a listing; version/maintenance facts with
sources; costs/limits; candidate sources list classified; discarded sources.

## Control signal
Return exactly one line:
`DONE researcher agent-artifacts/expert-tools/files-to-prompt/researcher/01/evidence.md`
or `REQUEST correspondent <need>` / `BLOCKED researcher <reason>`.

## Scope discipline
`./nb` (after `export PATH="$HOME/.local/bin:$PATH"`) and web/shell tools for
focused work. Do not tour the repo or archive as background.
