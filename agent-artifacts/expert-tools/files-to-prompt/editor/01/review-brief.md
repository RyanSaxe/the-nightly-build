# Editor brief — expert-tools/files-to-prompt (01)

## Role
Load and follow `skills/editor/SKILL.md`. Fresh-eyes gate on an Expert Tools
article. Three ordered reads (skeptic, cut, reader). Direct cuts/small fixes in
the HTML; larger writing to the writer; evidence gaps to the researcher. Approve
only with `DONE` and no required change.

## Begin with these exact inputs (under `.nb-work/expert-tools/files-to-prompt/`)
- `agent-artifacts/expert-tools/files-to-prompt/editorial-direction.md`
- `agent-artifacts/expert-tools/files-to-prompt/writer/01/brief.md` (EXACT writer
  brief — check for instruction leakage)
- `agent-artifacts/expert-tools/files-to-prompt/writer/01/draft-handoff.md`
- `agent-artifacts/expert-tools/files-to-prompt/researcher/01/evidence.md` (the
  tool was installed and run; real captured output; reproduced footguns; a
  17-month dormancy caveat)
- `agent-artifacts/expert-tools/files-to-prompt/writing-coach/01/voice-guide.md`
- The article: `library/expert-tools/files-to-prompt.html`

## The three reads
1. **Skeptic.** Verify against the evidence record: the demonstrated commands and
   output are the researcher's REAL captured runs (not invented), including the
   `--cxml` tagging and default-mode binary exclusion; the two footguns (`-e`
   suffix-match bug; anchored-`.gitignore` leak) are described as reproduced and
   tied to the actual `should_ignore` source; the maintenance verdict carries the
   honest caveat (last release 2025-02-19 / ~17 months stale, 13 open issues,
   ~200 installs/day) rather than burying it. Audit every `data-nb-kind` and that
   the 20 citations trace to read/ran sources. The claim "niche + powerful +
   trustworthy-enough" must be earned, with the dormancy stated plainly.
2. **Cut.** Remove install-tutorial drift, hype adjectives, "here's the kicker"
   punchlines, signposts, scaffold headings (Installation/Usage/Verdict),
   instruction leakage. The example proves the value; it is not a walkthrough.
3. **Reader.** Does the piece show the ONE thing that changes the work (assembling
   the right codebase slice for an LLM) and reach a real adopt-or-not judgment?
   Is the tool + the work it changes named in the headline and section titles
   (series requirement)? Retest headline/dek vs `spec/headlines.md`. Judge voice.

## After edits
Re-run and confirm clean:
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/expert-tools/files-to-prompt/library/expert-tools/files-to-prompt.html \
  --series expert-tools --library /home/user/library
```
Must remain BLOCK: 0.

## Output
`agent-artifacts/expert-tools/files-to-prompt/editor/01/editorial-review.md`

## Control signal
Return exactly one line:
- `DONE editor agent-artifacts/expert-tools/files-to-prompt/editor/01/editorial-review.md`
  (approve, no required change, BLOCK: 0), or
- `REQUEST writer <one-sentence required change>` / `REQUEST researcher <need>` /
  `BLOCKED editor <reason>`.

## Scope discipline
`./nb` and web tools for focused verification only. Do not tour the repo/archive.
