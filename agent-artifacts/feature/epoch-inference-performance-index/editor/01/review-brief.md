# editor brief: feature/epoch-inference-performance-index (01)

Inputs:
- editorial-direction.md: standards, template contract, series prompt
- commission.md: story, boundaries, recent patterns to break (your recent-pattern
  notes), and decisions after drafting
- writer/01/brief.md: the exact writer brief
- writing-coach/01/voice-guide.md: how it sounds
- researcher/01/evidence.md and researcher/01/data/: open when a concern calls for it
- writer/01/draft-handoff.md: the writer's notes
- the article and its chart scripts: /home/user/the-nightly-build/.nb-work/feature/epoch-inference-performance-index/library/feature/
Output: editor/01/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/feature/epoch-inference-performance-index/library/feature/epoch-inference-performance-index.html --series feature --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.
You may use `nb history` to compare against the recent record.

Verify the writer's recomputed per-model ratios against Epoch's own score data.
The IPI is a modelled index with thin validation; check the article says so
where the argument leans on it. Look at both charts rendered (nb preview; use
`uv run --group figure-capture python` from /home/user/the-nightly-build with
`chromium.launch(executable_path='/opt/pw-browsers/chromium')`, never
`playwright install`). Word band 600–1200 is strict. Run nb as
/home/user/the-nightly-build/nb. Do not commit or push.
Editor model: the orchestrator's model (inherit), effort high.
