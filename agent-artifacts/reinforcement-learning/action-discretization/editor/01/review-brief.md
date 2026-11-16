# editor brief: reinforcement-learning/action-discretization (01)

Inputs:
- commission.md (assignment, boundaries, recent-pattern notes, decisions log)
- writer/01/brief.md (the exact writer brief)
- editorial-direction.md (includes the series prompt's lesson rules on code, runs, checks and problems)
- writing-coach/01/voice-guide.md (owner-pinned)
- researcher/01/evidence.md
- writer/01/draft-handoff.md
Output: editor/01/editorial-review.md (same artifact root); the article is library/reinforcement-learning/action-discretization.html in the workspace /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-discretization. Its code is in code/, printed output in runs/, throwaway checks in checks/. figures/build.py builds the article from figures/article.src.html and overwrites the HTML: edit the source and rebuild, or edit the HTML and do not rebuild.
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-discretization/library/reinforcement-learning/action-discretization.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

Recent-pattern notes are in the commission. Decisions the writer took without a ruling, which I now rule on:
- Near-upright starts via Pendulum-v1's reset options, on top of the raised torque cost: accepted, provided the page states both changes plainly and says why (the full swing-up is beyond a laptop-sized table).
- Torque cost 1.0: accepted.
- Result 2 read at three budgets counts as one result: accepted.
- Length: the prose runs about 2,450 words against the template's guide. Cut where the lesson drags; Fig. 3 or problem 2 is the writer's suggestion, the choice is yours.

This round's focus: rerun every listing exactly as printed (uv run) and check each printed number on the page and in each inline-SVG chart against the output; rerun the seed and removal checks listed in the handoff; check the bound 800C/(k−1)² derivation line by line; and confirm the lesson teaches only what lessons 1 to 18 taught. Look at every figure rendered (nb preview; Playwright is preinstalled: require('playwright'), chromium.launch() with no options) at phone and desktop width, light and dark. End with nb stamp and the proof at BLOCK: 0.
