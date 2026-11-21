# editor brief: reinforcement-learning/reward-scale (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: topic, one idea, case, boundaries, recent patterns to break
  (your recent-pattern notes), decisions after drafting
- writer/01/brief.md: the exact writer brief
- writing-coach/01/voice-guide.md: the series' pinned voice
- researcher/01/evidence.md: open when a concern calls for it
- writer/01/draft-handoff.md: the writer's checks, which you can rerun
- the writer's code: /home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/work/
- the article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/library/reinforcement-learning/reward-scale.html
Output: editor/01/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/reward-scale/library/reinforcement-learning/reward-scale.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
You may use `nb history` and read the published lessons the article links,
to compare against the recent record and the course's earlier code.

Rerun every listing exactly as printed (copy it out of the page into a fresh
directory outside library/ and agent-artifacts/, then `uv run`) and check each
printed number and figure against the output. Check that the Baselines issue
#538 paraphrase is faithful. Look at every figure rendered (nb preview; use
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`, never
`playwright install`). Keep any scratch files out of agent-artifacts/. Run nb
as /home/user/the-nightly-build/nb. Do not commit or push.
Editor model: the orchestrator's model (inherit), effort xhigh.
