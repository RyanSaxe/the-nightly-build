# writer brief: reinforcement-learning/action-masking-in-maskable-ppo (01)

Inputs:
- editorial-direction.md
- commission.md (read the "Decisions during production" section: it adjusts the angle)
- writing-coach/01/voice-guide.md (pinned by the series)
- researcher/01/evidence.md (includes the exact hanoi.py and agent.py listings)
Output: writer/01/draft-handoff.md (and the article at
  /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-maskable-ppo/library/reinforcement-learning/action-masking-in-maskable-ppo.html)
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-maskable-ppo/library/reinforcement-learning/action-masking-in-maskable-ppo.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background.
Where something you need is missing, ask me. You may read the two lessons the commission links
(`./nb history --show reinforcement-learning/action-masking-in-q-learning` and
`.../training-an-off-the-shelf-agent`, and their HTML in the local library checkout under
/home/user/the-nightly-build/.nb-work/library/) to see what the course has taught.

The researcher's runs are single-seed guides, not numbers to print. Run every listing yourself with
`uv run` in a scratch folder under
/tmp/claude-0/-home-user-the-nightly-build/efbdeaae-8835-5515-95b0-8d4030ac57a4/scratchpad/rl-writer/,
follow the series prompt's result checks (new seeds, removal test on the page, worst case), and list
each check in draft-handoff.md. Keep each experiment within a few minutes on CPU.

Recent openers, closers and outlines to break are in the commission's "Recent patterns" section.
The previous lesson's sections ran: problem-number heading, env listing, failure-with-masked-choice,
mechanism, then the note. Build a different outline.

Harness: Claude Code. Writer model: claude-opus-5-5 (xhigh effort, as the series requires).
