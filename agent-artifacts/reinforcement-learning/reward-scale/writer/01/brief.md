# writer brief: reinforcement-learning/reward-scale (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: topic, the one idea, the courier case, boundaries, recent patterns
- writing-coach/01/voice-guide.md: the series' pinned voice
- researcher/01/evidence.md: the citable claims
Output: writer/01/draft-handoff.md, and the article at
  /home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/library/reinforcement-learning/reward-scale.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/library/reinforcement-learning/reward-scale.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
Exception: you may read the published lessons the commission tells you to link
(under /home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/,
or via `nb history --show`) to reuse their code and match their numbers.

The researcher found no source that works out the scale or shift results, so
the page's own derivations carry them; cite Sutton and Barto's exercises and
Ng, Harada and Russell's footnote as the places the questions are posed. The
scaling result holds for the expected-return objective only; one sentence can
say so with the SAC pointer from the record. DQN's Nature paper clips to
[−1, 1] while SB3's ClipRewardEnv takes the sign; if the page mentions either,
say which, since they differ on fractional rewards.

Keep your code and runs in a working directory under
/home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/work/
(not inside library/). Every listing on the page must run exactly as printed
with `uv run`. Record each seed and cell check in draft-handoff.md so the
editor can rerun it.

Environment: Playwright for previews is preinstalled. Use
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`; do not run
`playwright install`. Run nb as /home/user/the-nightly-build/nb. Do not commit
or push.

Harness for nb-meta: Claude Code. Writer model: the orchestrator's model (inherit).
