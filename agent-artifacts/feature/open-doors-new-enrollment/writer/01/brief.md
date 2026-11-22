# writer brief: feature/open-doors-new-enrollment (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: the story, boundaries, recent patterns to break, and
  "Decisions after research", which settles the angle
- writing-coach/01/voice-guide.md: how it sounds
- researcher/01/evidence.md (and any data beside it): the claim set and series
Output: writer/01/draft-handoff.md, and the article at
  /home/user/the-nightly-build/.nb-work/feature/open-doors-new-enrollment/library/feature/open-doors-new-enrollment.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/open-doors-new-enrollment/library/feature/open-doors-new-enrollment.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Lead with the finding: the total's small fall hides an 8.3% fall in enrolled
students offset by OPT, and the swap is almost entirely Indian graduate
students. Build each section around a visual (component series via `nb chart`
from the record's series; an inline-SVG flow drawing per press/editorial.md;
an origin comparison if it earns a place). Look at every visual at phone and
desktop width in both themes (nb preview; Playwright via
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`; never
`playwright install`).

Recent feature openers state a count or share against a past baseline in the
first sentence; recent closers end on a figure comparing two periods. Break
both. The strict 600–1200 word band is a hard limit. Run nb as
/home/user/the-nightly-build/nb (export UV_SYSTEM_CERTS=1). Keep scratch files
out of library/ and agent-artifacts/. Do not commit or push.
Harness for nb-meta: Claude Code. Writer model: claude-sonnet (capable tier).
