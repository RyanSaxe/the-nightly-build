# Commission — expert-tools/files-to-prompt

## Assignment
One Expert Tools article on a niche, powerful tool that changes an expert
workflow. Primary pick: **`files-to-prompt`** (Simon Willison) — a CLI that
assembles a chosen slice of a codebase into one well-structured prompt for an
LLM, with precise inclusion control, .gitignore handling, and a Claude-optimized
XML output (`--cxml`) that improves long-context reference. This sits in the
**AI-harness extension** family, which is the rotation slot due after recent
Neovim (oil.nvim, 7/29) and Python-runtime (pydantic-monty, py-spy) picks.

## Researcher discovery authority (resolve BEFORE the writer starts)
The tool must genuinely qualify: niche (not a default/foundation), powerful
enough to alter a real workflow, and maintained well enough to trust. The
researcher must inspect the implementation, docs, commit history, release
cadence, and real usage — not just the README — and CONFIRM `files-to-prompt`
still qualifies as of 2026. If it has become a familiar default, is unmaintained,
or its only distinction is popularity, escalate `REQUEST correspondent` with the
finding and propose the fallback **`symbex`** (Simon Willison; extracts specific
Python symbols/signatures via AST to feed precise context to an LLM) or another
strong niche AI-harness tool the research surfaces. Do not silently swap; flag it.

## Angle / required contribution
Show the ONE part that changes the work, not an install tutorial. The workflow
problem: feeding an LLM the *right* slice of a large codebase — enough to reason,
not so much it drowns in irrelevant files or blows the context/token budget.
Demonstrate with a small, real shell command on a real repository subtree: how
`files-to-prompt` selects files (globs/paths, --extension, --ignore,
.gitignore honoring, binary skipping), and how its `--cxml` output structures the
files so a model can cite them precisely. Explain where it enters a workflow
(the assembly step before an LLM call, or piping into `llm`), what it replaces
(hand-copying files, ad-hoc cat/find pipelines, over-broad repo dumps), what
adopting it costs (learning the flags, remembering to scope tightly, no semantic
selection), and whether maintenance is trustworthy (releases, issues, author).
Name the tool and the work it changes in the headline and section titles.

## Reader
Math/CS background, ML-engineering career, works at the command line and with
LLM tooling daily. Assume fluency with shells, git, and calling models; do not
explain what an LLM or a token is. Teach the tool's specific leverage.

## Mode / template / paths
- Series `expert-tools`, mode `open`, template `article`.
- nb-meta: `mode: "open"`, `order: null`, `date: "2026-07-31"`.
- Article: `library/expert-tools/files-to-prompt.html`. Words 1200-3000.
- Flex sections 2-6; last is the piece's own conclusion (adopt-or-not judgment).
- If the researcher swaps the tool, the slug/workspace stays as commissioned only
  if the tool name still fits; otherwise escalate to the correspondent to
  re-init the workspace with the correct slug.

## Furniture guidance
A shell command or short code is a `nb-code` listing (the tool's example is the
proof, per the series prompt). Use a small table only if comparing outputs/flags
earns it. No decoration. The example proves value; it is not a walkthrough.

## Source obligations
- Template floor: **min 6 sources**, all read and resolving.
- Primary = the tool's own repository, source files, release notes, and the
  author's own writing about it; the actual output of running it. Secondary =
  independent write-ups/usage reports. Read past the README into the code.
- Every capability claim (gitignore honoring, cxml structure, binary skip, token
  behavior) must be verified against the source or a real run, not assumed.

## Starting sources (verify each)
- `github.com/simonw/files-to-prompt` (README, source, releases, issues, commit
  history).
- Simon Willison's blog posts / release notes announcing and updating it.
- The `llm` ecosystem context if the article shows piping into a model.
- At least one independent, real usage account.

## Relevant prior coverage (do not repeat)
expert-tools recent: oil.nvim (7/29, nvim), pydantic-monty (7/27, python
sandbox — already published, do not reuse), ast-grep (7/24, AST search/rewrite),
py-spy (7/22, profiling). Avoid the AST framing (ast-grep territory) if the
fallback `symbex` is used — differentiate on "assembling LLM context," not
"AST tooling." Vary structure from those pieces.

## Structures NOT to repeat
The recent expert-tools headlines are single declarative sentences naming the
tool and the concrete thing it did ("oil.nvim edits a remote server's files the
same way it edits a local directory"). Keep that quality of specificity but do
not copy a template. No "Installation / Usage / Verdict" scaffold; name sections
for this tool's argument.

## Neighboring articles tonight
paper-of-the-day (emergent abilities), tech-news, current-events, investing,
unbiased, word-of-the-day. This is the hands-on engineering read. Keep it
practical and demonstrated.

## Harness / model (balanced profile)
coach sonnet/low; researcher sonnet/high; writer sonnet/medium; editor opus/high.
nb-meta `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Publication bar
6+ real read sources including the tool's own source (not just README); a
working, real demonstrated example with actual output; honest costs and
maintenance judgment; an adopt-or-not conclusion; 1200-3000 words; `nb check`
BLOCK: 0; editor DONE.
