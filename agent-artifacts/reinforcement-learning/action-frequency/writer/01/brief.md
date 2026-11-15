# writer brief: reinforcement-learning/action-frequency (01)

Inputs:
- editorial-direction.md: the standing directions for this article, including the series prompt
- commission.md: the assignment and every decision, including the corrections made after research
- writing-coach/01/voice-guide.md: the series' pinned voice guide
- researcher/01/evidence.md: the complete set of claims available from sources
Output: writer/01/draft-handoff.md (and the article file and its scripts below)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/library/reinforcement-learning/action-frequency.html --series reinforcement-learning --repo /home/user/the-nightly-build

All input paths are relative to
/home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/agent-artifacts/reinforcement-learning/action-frequency/.
The article to edit: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/library/reinforcement-learning/action-frequency.html
The effective template contract and furniture catalogs are under
/home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/.nb-context/.

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me. To learn what earlier
lessons taught and what code can be reused, you may read the published lessons the commission
names with `nb history --show reinforcement-learning/<slug>` from /home/user/the-nightly-build.

Recent openers, closers and shapes to break:
- Deks open "On <environment>, ..." (12, 9, 1 Nov, 31 Oct) or "Over the first 10 episodes".
- Headlines use "<thing> keeps X from ...".
- Why-this-matters boxes end by naming a later algorithm ("DQN, later in the course, ...").
- Takeaways open by restating the lesson's equation in one sentence.
- Recent lessons' section order runs: problem figure, then a code section, then math, then a
  code+figure result, then an exploration/eval caveat. Outline from this lesson's reasoning.

Run environment: Python with `uv` is available (`uv run file.py`); Playwright and Chromium are
preinstalled (do not run `playwright install`). Scale every run to a few minutes on a CPU. Look at
every visual at phone and desktop width in both themes via `nb preview`.
