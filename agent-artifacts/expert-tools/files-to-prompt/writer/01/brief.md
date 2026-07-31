# Writer brief — expert-tools/files-to-prompt (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft from the exact brief, voice guide,
and evidence record; carry it through the proof to BLOCK: 0.

## Begin with these exact inputs (under `.nb-work/expert-tools/files-to-prompt/`)
- `agent-artifacts/expert-tools/files-to-prompt/editorial-direction.md`
- `agent-artifacts/expert-tools/files-to-prompt/commission.md`
- `agent-artifacts/expert-tools/files-to-prompt/writing-coach/01/voice-guide.md`
- `agent-artifacts/expert-tools/files-to-prompt/researcher/01/evidence.md`
  (24 read sources; the tool was actually installed & run; real captured output;
  reproduced limitations; a maintenance/dormancy caveat)
- The initialized article: `library/expert-tools/files-to-prompt.html`
- Generated context: `.nb-context/` (contract, runtime-assets, furniture).

## What to write
`library/expert-tools/files-to-prompt.html`. Template `article`, **1200-3000
words**, flex sections 2-6 (last is the piece's own adopt-or-not conclusion).
Show the ONE part that changes the work — assembling the right slice of a codebase
into one LLM prompt — with a REAL demonstrated example, not an install tutorial.
- Open on the workflow problem (feeding a model precise context), not the tool's
  history. Name the tool and the work it changes in the headline and section
  titles (series requirement).
- Use the researcher's REAL captured commands and output as the demonstration.
  Render commands/output as `nb-code` listings (see `.nb-context` furniture). Do
  not invent output; use what was actually captured (default mode and `--cxml`).
- Explain where it enters a workflow (the assembly step / piping into `llm`), what
  it replaces (hand-copying, ad-hoc cat/find, over-broad repo dumps), the costs
  (learning flags, manual scoping, no semantic selection, the `-e` suffix-match
  footgun and the anchored-.gitignore leak the researcher reproduced), and — the
  series demands it — an HONEST maintenance verdict: last release/commit
  2025-02-19 (~17 months stale as of 2026-07-31), 13 open issues, but ~200
  installs/day and it works. Reach an adopt-or-not judgment that carries this
  caveat rather than burying it.

## Permitted changes / decisions you own
- Name the flex sections for THIS tool's argument (problem → the one leverage →
  demonstration → costs/maintenance → verdict), not Installation/Usage/Verdict.
- Headline/dek per `spec/headlines.md`: a specific declarative claim about what
  the tool concretely does; no colon machine-tell; dek adds a stance.
- Preserve fixed engine assets/classes/labels/required HTML. No added
  scripts/styles/iframes/forms/handlers/external images. Use `nb-code` for code.

## Metadata (`nb-meta`)
Real values: `series: "expert-tools"`, `slug: "files-to-prompt"`,
`template: "article"`, `mode: "open"`, `order: null`, `date: "2026-07-31"`,
honest `tags` (e.g. `["python","llm","cli"]`), measured counts, `dek`,
`harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
```
export PATH="$HOME/.local/bin:$PATH"
./nb check .nb-work/expert-tools/files-to-prompt/library/expert-tools/files-to-prompt.html \
  --series expert-tools --library /home/user/library
```

## Also write
`agent-artifacts/expert-tools/files-to-prompt/writer/01/draft-handoff.md`: the
visible act of original work (the real run on this repo's own tree and the
reproduced limitations, not a README paraphrase), final word/source counts,
unresolved WARNs.

## Request, don't guess
Missing evidence → `REQUEST researcher <need>`; missing voice → `REQUEST
writing-coach <need>`.

## Control signal
Return exactly one line (DONE only after BLOCK: 0):
`DONE writer agent-artifacts/expert-tools/files-to-prompt/writer/01/draft-handoff.md`
or `REQUEST <owner> <need>` / `BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web/shell tools for focused work; the evidence record is your source of
truth. You may re-run the tool only to re-confirm exact output you are about to show.
