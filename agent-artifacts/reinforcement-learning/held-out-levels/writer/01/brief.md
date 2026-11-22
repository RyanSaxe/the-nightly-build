# writer brief: reinforcement-learning/held-out-levels (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: topic, the one idea, the case, boundaries, recent patterns,
  and "Decisions after research", which settles the open questions
- writing-coach/01/voice-guide.md: the series' pinned voice
- researcher/01/evidence.md: the citable claims
Output: writer/01/draft-handoff.md, and the article at
  /home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/library/reinforcement-learning/held-out-levels.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/library/reinforcement-learning/held-out-levels.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
Exception: you may read the published lessons the commission tells you to link
(under /home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/,
or via `nb history --show`) to reuse their code, pinned versions and
conventions and to match their numbers.

Keep your code and runs in a working directory under
/home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/work/
(not inside library/). Every listing on the page must run exactly as printed
with `uv run`, within a few minutes on a laptop CPU. Record each seed, cell and
removal check in draft-handoff.md so the editor can rerun it.

Environment: Playwright for previews is preinstalled. Use
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`; do not run
`playwright install`. Look at every SVG at phone and desktop width in both
themes. Run nb as /home/user/the-nightly-build/nb (export UV_SYSTEM_CERTS=1).
Do not commit or push.

Harness for nb-meta: Claude Code. Writer model: the orchestrator's model (inherit).
