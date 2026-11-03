# writer brief: reinforcement-learning/action-values-from-samples (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/agent-artifacts/reinforcement-learning/action-values-from-samples/editorial-direction.md — layered editorial direction, including the series prompt
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/agent-artifacts/reinforcement-learning/action-values-from-samples/commission.md — topic, one idea, case, boundaries, patterns to break, post-evidence decisions
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/agent-artifacts/reinforcement-learning/action-values-from-samples/writing-coach/01/voice-guide.md — the course's pinned voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/agent-artifacts/reinforcement-learning/action-values-from-samples/researcher/01/evidence.md — sources, locations, convergence status, practical notes
- Earlier lessons for code reuse and links: ./nb history --show reinforcement-learning/<slug>
  (environments-and-the-rl-problem, finding-optimal-policies, learning-values-from-samples), and
  their HTML under /home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/
  for exact gridworld.py / estimators.py listings.
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/agent-artifacts/reinforcement-learning/action-values-from-samples/writer/01/draft-handoff.md (the article is
/home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/library/reinforcement-learning/action-values-from-samples.html)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples/library/reinforcement-learning/action-values-from-samples.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Recent openers/conclusions/shapes are in the commission's "Recent patterns to break".
Run environment: run nb from /home/user/the-nightly-build as ./nb. Run lesson code in a scratch
dir with uv run (files with inline script metadata). For rendered checks, do not run the
playwright install in scripts/install-figure-capture.sh; `uv sync --group figure-capture` is
done, and Python Playwright must launch with executable_path="/opt/pw-browsers/chromium". Build a
preview with ./nb preview --preview /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-values-from-samples --out <scratch dir>.
Writer meta: harness Claude Code; record your model as given by your runtime.
