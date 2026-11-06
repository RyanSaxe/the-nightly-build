# Draft handoff: reinforcement-learning/termination-and-truncation (writer 01)

## Main idea (29 words)

Gymnasium's terminated flag means the next state's future is worth zero, so the TD target stops. Truncated means a time limit cut the episode, so the target still bootstraps.

## Original work

The lesson turns the time-limit mistake into a prediction. It derives that Q-learning which treats the cut as terminal rests at the optimal values of a grid that also ends with probability p(s, a) after each move. It measures p in the runs and checks the prediction on the course's grid at every limit from 2 to 200 moves: within 0.07 to 0.10, against an error of up to 1.29 from q*.

## Proof

Exact command from the brief, links included: `BLOCK: 0`, `WARN: 1`, verdict PUBLISHABLE. Stamped words=4204, sources=7.

- Warning left on purpose: `W-CITE-DENSITY section 'runs' has no inline citations`. That section holds only the lesson's own runs, which are their own evidence. The series prompt says this warning needs no action there.

Prose length: about 2,300 words by my count of the rendered text. That count includes headings and `details` summaries and leaves out code, output, equations, SVG text, reading bands and sources. It is a little over the 2,200 the template allows. I already cut a third problem, the `register`/`make` paragraph and its source, and most of the old-`done` paragraph. If the editor wants to get under 2,200, the next whole idea to cut is the "both flags are true" paragraph's last two sentences (the table that starts at 1). The commission requires the paragraph itself.

## Runs and checks (for the editor to rerun)

Files: the page prints `grid_env.py`, `q_gym.py` and `limits.py` in full. They need `gridworld.py`, `control.py`, `estimators.py`, `mc_control.py` and `td_control.py` from the earlier lessons, all in one folder. Python 3.11, gymnasium 1.4.0 and numpy 2.4.6 resolved under uv.

- `uv run grid_env.py`: the demo uses seed 29. I found it by searching seeds 0 to 49 for one where none of the eight scripted moves slips (29 and 39 both work). The printed output matches Fig. 1.
- `uv run limits.py` (2 min 37 s here): SEEDS = range(5). Each run seeds the environment with `reset(seed=seed)` and the agent with `default_rng((seed, 1))`. Every number on the page comes from this output. Fig. 2 and Fig. 3 were drawn from it, and I checked both against it.
- Clean-folder rerun: I copied the eight files into an empty folder and ran both listings. The output was byte-identical to the printed output.
- Fresh seeds: I set SEEDS = range(100, 105) and kept everything else. The conclusion is unchanged. Bootstraps: 0.08 to 0.14 at every limit. Cut is terminal: 1.25, 1.20, 1.14, 0.83, 0.42, 0.09 and 0.09 for limits of 2, 3, 4, 6, 10, 20 and 200. Distance to the resting point: 0.08 to 0.10. Episodes cut at limit 4: 0.62.
- Removal test for the causal claim, that dropping the bootstrap at the cut causes the error: this is the `cut_is_terminal` flag in `q_gym.py`. Its numbers are both columns of the printed table. Nothing else differs between the two versions.
- Worst-fit cases for the resting-point derivation:
  - Limit 2, where p is about 0.5: within 0.09.
  - Limit 200, where p is 0: within 0.09.
  - ε = 0.1 at limit 4, 5 seeds, prototype with the same algorithm and an agent seed of 1000 + seed. Here p is very uneven, down to 0.009 at cell 12. The prediction is still within 0.10 to 0.15. The cut-as-terminal error grows to about 1.37, and the bootstrapping error is 0.16 to 0.25. The page claims nothing from this run.
- Limit 200: no episode was cut in any of the five runs of either version, and the two versions' Q tables are bitwise identical. This supports the sentence "no episode was cut in any run, and the two versions learned the same estimates."
- Cells 5 and 10 (the caption of Fig. 2): with 400,000 episodes instead of 100,000 at limit 4, seeds 0 to 4, the bootstrapping target's mean largest estimates at cells 5 and 10 move from −0.12 and −0.25 to 0.14 and 0.11, against v* = 0.06. The overall error falls from 0.125 to 0.067. On the fresh seeds those two cells were already close at 100,000 episodes, so the caption says only that the gaps shrink with more episodes.
- Not on the page: at limit 2, the derived resting point itself has different arrows at cells 5 and 10 (left and down, away from the pit). At limit 4 its arrows are optimal, but the margins are 0.04 to 0.08, so the learned arrows at 5 and 10 flip from run to run in both versions. I made no arrow claim.
- The comment in `q_gym.py` says `reset(seed=s)` gives the environment the same stream as `default_rng(s)`. I checked this against `gymnasium.utils.seeding.np_random` in 1.4.0 (`PCG64(SeedSequence(seed))`) and compared the first draws.

## Decisions and open questions

- Commission correction applied: the orientation links the CAP passage (`action-values-from-samples.html#every-episode`). It says `td_control.py` already bootstrapped at the cap and recognized terminal cells through `TERMINAL`. It presents the new part as the two named endings under an interface where the agent does not see the rules.
- Limit choice: four moves. On the page: the main runs use four moves because the mistake disappears once the limit stops binding (Fig. 3: 4% of episodes cut at 20 moves, none at 200). The two Fig. 1 episodes also fit within four moves.
- Both qualifiers from the record are on the page: a limit that belongs to the task is a termination (Pardo case (i), Gymnasium tutorial), and both flags can be true, so the target tests terminated alone.
- Mention-only items kept to one sentence: the old `done` flag with its info entry, and Pardo et al. as the paper for the idea. I did not copy the Gymnasium tutorial's old-API one-liner (Contradictions 4) or the custom-env tutorial's stale wrapper output (Contradictions 6).
- I left Contradictions 10 (Sutton and Barto's "truncated return") off the page, because the page never uses that phrase.
- The Farama blog appears only in Go deeper and is not cited. The register/make docs were dropped with the paragraph I cut.
- No open evidence or voice question.
