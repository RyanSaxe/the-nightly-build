# writer brief: reinforcement-learning/domain-randomization (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/editorial-direction.md — layered direction, including the series prompt
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/commission.md — topic, idea, case, boundaries, and the decisions at its
  end, which govern
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/writing-coach/01/voice-guide.md — the series' pinned voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/researcher/01/evidence.md — the claim set, plus Gymnasium 1.4.0 notes
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/agent-artifacts/reinforcement-learning/domain-randomization/writer/01/draft-handoff.md
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/library/reinforcement-learning/domain-randomization.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

You may read published lessons only through
`/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>`
for what the course taught and for code to reuse: action-frequency (Dock's
rules and code), held-out-levels, frame-stacking-and-the-markov-property,
sarsa-and-q-learning. Recent shapes to break are in the commission's
recent-pattern notes. Work in a scratch directory under
/home/user/the-nightly-build/.nb-work/reinforcement-learning/domain-randomization/
for code; run every printed listing with `uv run` exactly as printed, and
do every seed, cell and removal check the series prompt requires, recording each
in the handoff. Look at each figure at phone and desktop width in light and dark
via nb preview; Python Playwright is available with `uv run --group
figure-capture` from /home/user/the-nightly-build, launching chromium with
executable_path='/opt/pw-browsers/chromium' (do not run playwright install).
Record the model you actually run on in nb-meta; the harness is Claude Code.
