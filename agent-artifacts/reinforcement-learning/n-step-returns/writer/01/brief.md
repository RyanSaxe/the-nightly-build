# writer brief: reinforcement-learning/n-step-returns (01)

Inputs:
- ../../editorial-direction.md — standing directions (house, press, template identity and contract, series prompt)
- ../../commission.md — topic, idea, case, boundaries, decisions after research, recent-pattern notes
- ../../writing-coach/01/voice-guide.md — the pinned series voice
- ../../researcher/01/evidence.md — the claim set
Output: writer/01/draft-handoff.md (beside this brief); the article at
/home/user/the-nightly-build/.nb-work/reinforcement-learning/n-step-returns/library/reinforcement-learning/n-step-returns.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/n-step-returns/library/reinforcement-learning/n-step-returns.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Earlier lessons: read only the ones the page links, with
`/home/user/the-nightly-build/nb history --show reinforcement-learning/<slug>`.
Likely: learning-values-from-samples (TD(0), Monte Carlo, estimators.py, its
Fig. 2 about one cell per pass) and off-policy-importance-sampling (for the
one-sentence pointer). Read the first three lessons' instructions in the series
prompt about not copying their form.

Run environment: Python 3.11 and `uv` are installed; `uv run file.py` works.
Put the lesson's code files where the page's listings are printed from (the
contract says what a lesson may ship: images and chart files only; print every
needed file in full). Keep scratch and seed checks under
/tmp/claude-0/-home-user-the-nightly-build/f459be86-7567-53db-a107-d49609878cc2/scratchpad/rl-writer/.
Figure checks: `nb preview` plus Playwright (Chromium is preinstalled;
`require('playwright')` works; do not run `playwright install`). Look at every
figure at phone and desktop width in light and dark themes.

nb-meta: harness "Claude Code"; writer model: record the model you run as
(your system context names it). Dates: 2026-11-10.

Recent shapes to break are in the commission's recent-pattern notes. Do not
commit, push or run nb prepare-pr.
