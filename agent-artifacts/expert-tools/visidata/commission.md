# Commission: expert-tools/visidata

## Authorized work
Scheduled duty for UTC 2026-08-05 returned `expert-tools` (open section,
`article` template) with no fixed commission. Publish exactly one article this
run. Slug: `visidata`.

## The tool
**VisiData** (`vd`), Saul Pwanson's terminal multitool for tabular data: open
almost any tabular or semi-structured source (CSV, TSV, JSON, JSONL, SQLite,
xlsx, Parquet, HTTP, and more) in one interactive TUI, then explore it —
frequency tables, pivots, aggregations, computed columns from Python
expressions, sorting/filtering, joins — without leaving the terminal or writing a
throwaway script. It fits the series: a command-line tool that is easy to miss,
powerful enough to change a real workflow, and not chosen for popularity.

Rotation note: the last two expert-tools picks were a Python package (pydantic-
monty) and an AI-harness tool (serena); a command-line tool balances the
rotation. VisiData is distinct from every published pick (ast-grep, files-to-
prompt, oil-nvim, py-spy, pydantic-monty, serena).

## Required contribution (from the series prompt + article template)
- Read PAST the README: inspect the implementation, docs, history, and real
  usage. Find the ONE thing that changes the work and show it in a small, real
  example (a shell session / a few keystrokes / a short expression column), not
  an installation tutorial. Candidate "changing move" to evaluate and, if it
  holds up, build the piece around: exploratory analysis as *interactive
  keystrokes over a loaded sheet* (e.g. `F` for a frequency table, `+` to add an
  aggregator, a Python-expression computed column, the pivot/melt commands)
  replacing the write-run-tweak loop of a pandas/one-off-script session — and its
  async/incremental loader that lets you start exploring a large file before it
  finishes loading. Verify the actual keybindings/commands and behavior against
  current docs/source; do not ship a remembered API.
- `article` template = original analysis: outline the reasoning first, name flex
  sections for THIS argument (not a standard "Overview/Usage/Verdict" outline),
  and remove any section whose deletion leaves the reasoning unchanged. Do NOT
  close on a reading list or a pointer away.
- Cover honestly: where it enters a workflow, what it replaces or enables, what
  adopting it costs (learning the modal keystrokes, edge cases, when a notebook
  is still better), and whether it is maintained well enough to trust (release
  history, maintainer, activity). Name the tool and the work it changes in the
  headline and section titles.

## Sourcing
`min_sources: 6`; word band 1200-3000. Primaries: the VisiData source repo,
official documentation (visidata.org), the author's own writing/talks, release
history/changelog. Verify version numbers, command/keybinding names, and
maintenance status against the current primary record. A remembered keybinding is
a citation error waiting to happen — confirm each shown command in the docs or
source. Confirm every URL resolves to the source's own page.

## Boundaries — do not repeat
- Published expert-tools slugs: ast-grep, files-to-prompt, oil-nvim, py-spy,
  pydantic-monty, serena. Use `nb history --structure expert-tools/<a-recent-
  slug>` for shape/continuity only and break its section shapes; do not inherit
  the prior article's outline.
- Non-overlap: none of the other edition pieces cover developer tooling; keep the
  example concrete to VisiData.

## Template and policy
- Template: `article` (fixed).
- Production policy (balanced): editor required at high effort, model inherit.
  Researcher/writer models = capable. If a shell transcript is shown, it is
  authored text in the article's own code furniture (not an external asset);
  charts/source assets only if the evidence supplies a real verified visual.

## Neighbors this edition
Full edition: current-events, tech-news, expert-tools (this),
investing/free-cash-flow, opinion/mandate-frontier-ai-disclosure,
paper-of-the-day/denoising-diffusion, word-of-the-day/ultracrepidarian.
