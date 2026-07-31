# Writing-coach brief — expert-tools/files-to-prompt (01)

## Role
Load and follow `skills/writing-coach/SKILL.md`. Transferable voice guide for
THIS article. No named persona, no reusable lines.

## Begin with these exact inputs
- `agent-artifacts/expert-tools/files-to-prompt/editorial-direction.md`
- `agent-artifacts/expert-tools/files-to-prompt/commission.md`

## The commission in one line
A 1200-3000 word Expert Tools piece on `files-to-prompt` (an AI-harness CLI that
assembles a precise codebase slice into one LLM prompt): show the one part that
changes the work with a real command and output, name where it enters a
workflow, its costs, and whether it's trustworthy — an adopt-or-not judgment,
not an install tutorial.

## What to study (at least three respected writers)
Study the best practitioner tool-writing: how strong engineering writers (e.g.
Simon Willison's own tool announcements, Julia Evans' explainers, Dan Luu's
grounded technical prose) introduce a small tool by showing it working on a real
case, argue adoption honestly (costs and limits included), and avoid tutorial
sprawl. Extract how they open on the workflow problem (not the tool's history),
weave a single demonstrated example, and close on a real judgment. Anchor to the
best, not the average dev-tool blog post.

## Output (write only this)
`agent-artifacts/expert-tools/files-to-prompt/writing-coach/01/voice-guide.md`
Cover: register for an expert reader who lives at the CLI; how to present a
command-line example so the demonstration carries the argument (and when a code
listing vs prose is right); how to make the "right slice of context" idea
concrete; honest adoption-cost writing; and tells to avoid (install-tutorial
drift, hype adjectives, "here's the kicker" punchlines, scaffold headings like
Installation/Usage/Verdict). Tie each move to a reason.

## Control signal
Return exactly one line:
`DONE writing-coach agent-artifacts/expert-tools/files-to-prompt/writing-coach/01/voice-guide.md`
or `REQUEST <owner> <need>` / `BLOCKED writing-coach <reason>`.

## Scope discipline
`./nb` and web tools for focused questions only. Do not tour the repo or archive.
