# editor brief: reinforcement-learning/semi-gradient-td (01)

Inputs:
- ../../editorial-direction.md — standing directions, template identity, series prompt
- ../../commission.md — topic, boundaries, decisions after research and on writer queries, recent-pattern notes
- ../../writer/01/brief.md — the exact writer brief
- ../../writing-coach/01/voice-guide.md — the pinned voice guide
- ../../researcher/01/evidence.md — the claim set
- ../../writer/01/draft-handoff.md — the writer's handoff, with the checks to rerun
- the article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/semi-gradient-td/library/reinforcement-learning/semi-gradient-td.html
- the writer's scripts: /home/user/the-nightly-build/.nb-work/reinforcement-learning/semi-gradient-td/scratch/
Output: editor/01/editorial-review.md (beside this brief)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/semi-gradient-td/library/reinforcement-learning/semi-gradient-td.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background (`nb history` for the recent lessons' patterns and
the linked n-step-returns lesson is fine). Where something you need is
missing, ask me.

This round's focus: (1) the start-state claim (the TD fixed point gives the
start state its exact value) is the lesson's original result and is
unsourced; check its derivation on the page and rerun `--start 250` and at
least one other start. (2) Rerun every printed listing with `uv run` and
confirm the output blocks match byte for byte, and that every number in the
prose and figures appears in or rounds from that output. (3) The series limits:
at most two experimental results outside a project lesson, a removal test on
the page for each causal claim. (4) The headline "TD(0) no longer converges to
the best fit once states share weights" against spec/headlines.md and the
commission's recent-pattern notes. Make direct cuts and code changes yourself,
then nb stamp and the proof. Check any figure you change with nb preview and
Playwright (Chromium preinstalled). Use /home/user/the-nightly-build/nb. Do not
commit or push.
