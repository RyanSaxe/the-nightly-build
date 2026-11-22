# editor brief: reinforcement-learning/held-out-levels (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: topic, one idea, case, boundaries, recent patterns to break
  (your recent-pattern notes), decisions after research
- writer/01/brief.md: the exact writer brief
- writing-coach/01/voice-guide.md: the series' pinned voice
- researcher/01/evidence.md: open when a concern calls for it
- writer/01/draft-handoff.md: the writer's checks, which you can rerun
- the writer's code: /home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/work/
- the article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/library/reinforcement-learning/held-out-levels.html
Output: editor/01/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/held-out-levels/library/reinforcement-learning/held-out-levels.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
You may use `nb history` and read the published lessons the article links,
to compare against the recent record and the course's earlier code.

Rerun every listing exactly as printed (copy it out of the page into a fresh
directory outside library/ and agent-artifacts/, then `uv run`) and check each
printed number and figure against the output. Points the writer raised:
prose length (~2,200 words against the template's aim); the derivation uses
the discounted optimum while the printed score is goal-reached-within-40;
a few unstable runs at 16 and 64 levels that fail their own training levels,
untraced (judge whether the page states that honestly enough); the removal
test via a fixed hand-written fallback rule (does it test the cause the page
claims?). Also judge whether the headline repeats the recent record's single
agent/single environment narrative form. The two warnings left
(W-SENTENCE-DENSITY on TeX, W-CITE-DENSITY on the lesson's own runs) are the
writer's stated choices; confirm or fix.

Look at every figure rendered (nb preview; `uv run --group figure-capture
python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`, never
`playwright install`), at phone and desktop width, both themes. Keep scratch
files out of agent-artifacts/ and library/. Run nb as
/home/user/the-nightly-build/nb (export UV_SYSTEM_CERTS=1). After edits run
`nb stamp` and the proof until BLOCK 0. Do not commit or push.
Editor model: the orchestrator's model (inherit), effort xhigh.
