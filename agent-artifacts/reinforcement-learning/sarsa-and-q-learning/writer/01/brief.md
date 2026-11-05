# writer brief: reinforcement-learning/sarsa-and-q-learning (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/editorial-direction.md — standing directions, including the series prompt
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/commission.md — topic, one idea, case, post-research decisions (last section)
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/writing-coach/01/voice-guide.md — the pinned course voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/researcher/01/evidence.md — citable claims
- Earlier lessons, for what the course has taught and its code:
  `./nb history --show reinforcement-learning/<slug>` for environments-and-the-rl-problem,
  finding-optimal-policies, learning-values-from-samples, action-values-from-samples,
  epsilon-greedy-exploration; their HTML (with the printed listings) is under /home/user/the-nightly-build/.nb-work/library/library/reinforcement-learning/
Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/library/reinforcement-learning/sarsa-and-q-learning.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/agent-artifacts/reinforcement-learning/sarsa-and-q-learning/writer/01/draft-handoff.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/sarsa-and-q-learning/library/reinforcement-learning/sarsa-and-q-learning.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Recent shapes (lessons 1–5): every lesson opens with the "Why this matters" bookend
summarising the method, then a section built on a run count ("Forty-two moves with
no returns"); bodies close on a swept-parameter table before the Problems note;
the takeaway bookend restates the dek's two-clause shape. Deks are "X, and Y".
Recurring phrases to avoid: "the course's slippery grid", "on this grid". Break
these. Write and run every listing exactly as printed (uv run), put the list of
seed/cell checks in draft-handoff.md, and render the page (nb preview +
Playwright; scripts/install-figure-capture.sh) at phone and desktop width in both
themes before handing off.
