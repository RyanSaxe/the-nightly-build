# writer brief: reinforcement-learning/observation-scale (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editorial-direction.md: the standing directions, series prompt and lesson template
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/commission.md: topic, idea, case, boundaries, recent patterns, and the decisions at the end (they override earlier lines)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writing-coach/01/voice-guide.md: the pinned series voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/researcher/01/evidence.md: the evidence record
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/draft-handoff.md, and the article at
/home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

You may read the published lessons the commission names with
`/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>`
(semi-gradient-td, the-deadly-triad, training-an-off-the-shelf-agent) for what
they taught and what code they printed, not for form. Use
`--structure` for their outlines. Recent openers and closers to break are in
the commission's "Recent patterns" section.

Write and run every listing with `uv run` in a scratch directory under the
workspace (not on the page). Run the seed, cell and removal checks the series
prompt requires and list them in the handoff. Keep each experiment within a
few minutes on this CPU. Inspect every visual rendered at phone and desktop
width in light and dark themes (nb preview plus Playwright, set up by
/home/user/the-nightly-build/scripts/install-figure-capture.sh; Chromium is
preinstalled, do not run playwright install). Run `nb stamp` and the proof
until BLOCK: 0. Meta: harness "Claude Code"; writer model: the model this
session runs, effort xhigh.
