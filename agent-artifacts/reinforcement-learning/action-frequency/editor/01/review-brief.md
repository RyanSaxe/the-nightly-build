# editor brief: reinforcement-learning/action-frequency (01)

Inputs:
- editorial-direction.md: the standing directions for this article, including the series prompt
- commission.md: the assignment and every decision, including those after writer round 01
- writer/01/brief.md: the exact writer brief
- writing-coach/01/voice-guide.md: the series' pinned voice guide
- researcher/01/evidence.md: the evidence record
- writer/01/draft-handoff.md: the writer's choices and the list of off-page checks
  (throwaway scripts in writer/01/checks/)
- Article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/library/reinforcement-learning/action-frequency.html
Output: editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/library/reinforcement-learning/action-frequency.html --series reinforcement-learning --repo /home/user/the-nightly-build

All input paths are relative to
/home/user/the-nightly-build/.nb-work/reinforcement-learning/action-frequency/agent-artifacts/reinforcement-learning/action-frequency/.

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me. You may read earlier
lessons with `nb history --show reinforcement-learning/<slug>` to check what the course taught.

Recent-pattern notes: deks open "On <environment>, ..." or "Over the first 10 episodes";
headlines use "<thing> keeps X from ..."; why-this-matters boxes end by naming a later algorithm;
takeaways open by restating the lesson's equation; recent section order runs problem figure,
code, math, code+figure result, caveat. Compare with `nb history --series reinforcement-learning
--limit 5` for formula.
Focus this round: rerun every listing as printed (uv run) and check each printed number and each
SVG chart against the output; verify the derivation step by step; confirm the causal claim about
run 2 is supported by the two removal flags at the stated seeds; the remaining W-CITE-DENSITY
warning is on a section of the lesson's own environment and run, which the series prompt exempts.
Run environment: `uv` available; Playwright and Chromium preinstalled (no `playwright install`).
