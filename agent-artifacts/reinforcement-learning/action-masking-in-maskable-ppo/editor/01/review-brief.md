# editor brief: reinforcement-learning/action-masking-in-maskable-ppo (01)

Inputs:
- the article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-maskable-ppo/library/reinforcement-learning/action-masking-in-maskable-ppo.html
- editorial-direction.md
- commission.md (including "Decisions during production")
- writing-coach/01/voice-guide.md (pinned by the series)
- researcher/01/evidence.md
- writer/01/brief.md (the exact writer brief)
- writer/01/draft-handoff.md (lists every result check with scripts to rerun)
Output: editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/action-masking-in-maskable-ppo/library/reinforcement-learning/action-masking-in-maskable-ppo.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive for background.
Where something you need is missing, ask me. You may read the linked earlier lessons
(`./nb history --show reinforcement-learning/<slug>`) to check what the course has taught.

The writer's run copies, check scripts and page code are in
/tmp/claude-0/-home-user-the-nightly-build/efbdeaae-8835-5515-95b0-8d4030ac57a4/scratchpad/rl-writer/.
Rerun the printed listings exactly as printed (`uv run`) and compare every number on the page and in
every figure against the output. A rerun's number counts as evidence.

Recent-pattern notes (last five lessons, 13–17 November):
- Headlines: one declarative finding naming an environment or a number, often "X does Y on Z".
- Deks: five in a row explained a mechanism with "since", "because" or "so".
- Openings: one surprising number, then a listing of the environment.
- The 17 November lesson's outline: problem heading, env listing, failure, mechanism, note.

Orchestrator's concerns:
1. The headline "MaskablePPO's network never learns which moves are illegal": check it against what
   the code and runs show (masked logits receive no gradient through the masked softmax? the network's
   illegal probability stays at 0.30–0.35). "Never" must hold across seeds and training length, and
   the lesson must not explain why the gradient stays valid (stage 6) beyond a pointer.
2. The lesson must not teach PPO's algorithm (stage 5). Check it uses PPO only as a library.
3. The word band counts code and output: 3,660 of 2,500–6,000. Fine; prose ~2,030.
4. The off-page 150k-step seed 0 collapse: confirm the page claims nothing it would contradict.

Run `./nb preview` from /home/user/the-nightly-build and look at every figure and table at phone and
desktop widths in both themes. Delete the generated /home/user/the-nightly-build/site/ directory when done.
