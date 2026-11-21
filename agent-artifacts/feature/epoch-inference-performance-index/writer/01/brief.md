# writer brief: feature/epoch-inference-performance-index (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: the story, boundaries, and the recent patterns to break
- writing-coach/01/voice-guide.md: how it sounds
- researcher/01/evidence.md and researcher/01/data/: the claim set and series
Output: writer/01/draft-handoff.md, and the article at
  /home/user/the-nightly-build/.nb-work/feature/epoch-inference-performance-index/library/feature/epoch-inference-performance-index.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/epoch-inference-performance-index/library/feature/epoch-inference-performance-index.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

The researcher found the angle survives with corrections: the 25x per-chip
figure is an arithmetic mean that one model (Qwen) dominates for H100, the
per-model range is wide and a geometric mean gives a different number, and
the capacity-growth gap between IPI and FLOP/s units is mostly mix shift.
The IPI is a modelled index with thin measurement validation; say so where the
argument leans on it. Pick the finding the evidence best supports and lead
with it.

Environment: Playwright for previews is preinstalled. Use
`uv run --group figure-capture python` with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`; do not run
`playwright install`. Run nb as /home/user/the-nightly-build/nb. Do not commit
or push.

Recent feature openers state a count or share against a past baseline in the
first sentence ("Half the entries on the November 2026 TOP500 first appeared
..."). Recent closers end on a figure comparing two periods. Break both.
Harness for nb-meta: Claude Code. Writer model: claude-sonnet (capable tier).
