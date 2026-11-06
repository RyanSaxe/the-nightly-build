# Editorial review: reinforcement-learning/termination-and-truncation (editor/01)

## Correct

Thesis, from the draft alone: Gymnasium's `step` returns terminated and truncated separately because they need different TD targets. Terminated means the next state has no future, so the target is the reward. Truncated means a limit outside the task cut the episode, so the cell keeps its value and the target bootstraps. The claims under it:

1. With the limit outside the task, a cut cell keeps its value (Pardo et al., Eq. 5). The Q-learning target is therefore R + γ(1 − terminated) max Q, and truncated never enters it, even when both flags are true.
2. Gymnasium 1.4.0's `Env`, `Discrete` and `TimeLimit` behave as described, and `grid_env.py` reproduces the two episodes of Fig. 1.
3. Treating the cut as terminal makes Q-learning rest at the optimal values of a grid that also ends with probability p(s, a) after each move. The runs land within 0.10 of that point at every limit, and the bootstrapping target stays near q*.
4. The course's 200-move cap cuts no episode at ε = 0.5. That is why it hid the mistake, and why the runs use a four-move limit.

How each held.

Reruns. I copied the three listings off the page into an empty scratch directory, along with `gridworld.py`, `control.py`, `estimators.py`, `mc_control.py` and `td_control.py` taken from the published lessons' listings, and ran `uv run grid_env.py` and `uv run limits.py` (2 min 39 s). Both outputs are byte-identical to the printed output. I checked every printed number in the prose and the flags in Fig. 1 against that output. I also checked all 42 cell values in Fig. 2, and recomputed Fig. 3's 14 plotted points and seven cut shares from its axis scale. All match.

Derived resting point (claim 3), tested five ways at limit 4:
- At 400,000 episodes, seeds 0 to 4, the distance to the derived point falls from 0.084 to 0.057 while the distance to q* stays at 1.13. The runs are converging on the derived point, so they don't sit near it by chance.
- Replacing each pair's p with the mean p raises the distance to 0.19 to 0.21, so the per-pair p in the equation is doing work.
- On fresh seeds 100 to 104 the runs end 0.104 from the derived point, and the bootstrapping target ends 0.136 from q*. "At least as closely" survives the new seeds.
- The derived point itself is below v* in every cell: by 0.13 at cells 2 and 7 and by 0.84 or more everywhere else. The two sentences about the third panel of Fig. 2 therefore follow from the equation, not from noise in five runs.
- `resting_point` and the measurement of p match the displayed equation. The independence step holds exactly, because `TimeLimit` sets truncated from the step count alone and the slip draw never sees it.

200-move cap (claim 4). In `limits.py` at limit 200, all five seeds, both versions: zero episodes cut, the longest 69 to 74 moves, and the two versions' Q tables bitwise identical. I also ran the last lesson's own runs, `td_control.py` with 20 seeds for each of SARSA and Q-learning, counting moves through a wrapper that leaves the random stream alone. No episode reached 200 moves, and the longest were 155 and 100. "The cap did not matter in the last lesson's runs" is now checked against those runs, not inferred from this lesson's.

Smaller checks: seed 29 gives the no-slip demo. The comment in `q_gym.py` holds, since `reset(seed=7)` hands the environment the same stream as `default_rng(7)`. At cells 5 and 10 the bootstrapping target's gaps shrink at 400,000 episodes (−0.12 and −0.25 become 0.14 and 0.11, against 0.06).

Sources. I opened every href as printed. The four Gymnasium 1.4.0 pages load with the cited anchors and passages, including "If true, the user needs to call reset()", the TimeLimit docstring and the tutorial's 1.4.0 compatibility line. In the PMLR PDF, "a common mistake" is on p. 4049, Eqs. (5) and (6) are on p. 4050 and Fig. 1 is on p. 4046. PyPI's release page served curl a browser challenge, and the index's JSON record confirms 1.4.0, uploaded 2026-10-05. MIT Press returned 403 to curl. All six earlier lessons cite Sutton and Barto at that same address, so I left the course's standing href, and the Go deeper link to the free PDF loads on printed p. 57. The internal anchors `#value`, `#update-rules`, `#target-averages`, `#every-episode` and `#noise-and-bias` all exist. The proof's link check passes.

`data-nb-kind`: all seven sources are primary. Each Gymnasium page is the maintainers' own reference or tutorial, PyPI is the index's own record, and Pardo et al. and Sutton and Barto are the authors' texts. The page never treats the tutorial and Pardo as independent of each other, which is right, because the tutorial cites Pardo. The Farama blog appears only in Go deeper.

Breaks and fixes:
- The caption under Q-learning's target said Pardo et al. "give this target as their Eq. (6)". Their Eq. (6) is the state-value target, r or r + γ v̂(s′). Narrowed to "give the rule for state values as their Eq. (6)". This narrowing is an edit to match the source, not a cover for thin reporting.
- "Neither flag stops the environment" was cited to `Env.step`'s Returns, which says only that the user must call reset after either flag. Rewritten to what the source says: the loop has to call `reset` before it steps again.
- Fig. 2's caption said the gaps at cells 5 and 10 "shrink with more episodes" and attributed the caption to `limits.py`, whose output does not show that. The claim holds (above), so I moved it into the prose.

Headline, dek and headings: cell 7 sits below the goal, the limit is four moves, 62% of episodes are cut (in the bootstrapping runs; the cut-as-terminal runs cut 64%), and the different grid ends at random. All hold against the output.

## Reads well

What went:
- "Pardo and colleagues and Gymnasium's tutorial both treat that case separately." It said nothing the sentence before it had not already said, and it existed to carry two citations. They now sit on the sentence they support.
- "The task is over there, no rewards follow, and the value of a terminal state is always 0." Three clauses for one fact, now one sentence.
- The example of a table that starts every estimate at 1, in the both-flags paragraph. The handoff named it as the next cut. The paragraph keeps the commission's point, that the target tests terminated alone, and now says the wrong target does no harm here only because the goal's estimate keeps its starting value.
- From the briefing: the takeaway opened on the commission's one-idea sentence with its clause order intact ("An episode can end for two reasons, and Gymnasium's step reports them separately"). The last sentence of Why this matters followed the required-contribution line ("give the target for any transition"). I rewrote both in the lesson's own terms. The takeaway now opens on the two flags needing different targets, and the card says what the reader can do with a step's five return values and with the resting-point equation.

Tightened as I went: I split the card's 36-word first sentence and the `td_control.py` cap sentence. I recast `grid_env.py`'s step sentence, whose trailing "with the environment's own generator" attached to the wrong verb. I broke three consecutive "At N moves" openers. "Gym" was never introduced, and is now "OpenAI Gym", as the Env docs name it. Two of four uses of "the course's grid" became "the grid" and "this grid". The cut-as-terminal paragraph now opens on p, which also removes an "Its" with no clear referent.

Added one sentence: "The same argument holds for action values." The derivation is written for v_π, and the next display is Q-learning's max target, so a reader needed that step.

The draft was not running flat. It already starts from a small case with numbers, gives each step's purpose before the step, and derives the result before running it, as the voice guide asks. Against the recent record, the headline keeps the claim form without the "still learns" mould, the dek does not explain a one-term difference, only one heading cites a cell number, and Why this matters avoids "You will derive" and "you will see".

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 and 1280 px in both themes. Nothing scrolls sideways. Fig. 1's panels stack on a phone, Fig. 2's values stay legible on the dark heatmap, Fig. 3's line labels clear both lines, and every arrow in Fig. 1 reaches its cell. I added and cut no component. Fig. 1 and the target equation already cover the four flag combinations, so a table of them would repeat both.

Prose length: 2,151 words in the body, cards, captions, problems and answers, and about 2,195 with the headline and dek. Counting headings and `details` summaries as well gives 2,316. Before the edits the counts were 2,175 and 2,340. That is under the template's 2,200, so no further idea comes out. Why this matters runs about 130 words and the takeaway about 105.

The piece drags nowhere worth moving. The Gymnasium section is the driest, and the next lessons need each of its paragraphs. The body ends on the reason for the four-move limit, and the takeaway restates the finding.

What it gives beyond its sources: on the course's own slippery grid, it derives where Q-learning's estimates rest when a time limit is read as terminal, namely at the optimal values of a grid that ends with a measured per-pair probability. It then checks that prediction at seven limits, using a Gymnasium version of the grid that runs. That matches the handoff's original-work sentence. Pardo et al. do the same calculation with a fixed 1/3 on a deterministic grid (Section 2.2, p. 4048), and the Go deeper row now points to it. The headline, the piece's largest claim, holds to within 0.08 at the limit it names.

## Edits

- Why this matters: split the first sentence in two.
- Why this matters: replaced the last sentence, which echoed the commission, with what the reader can do from a step's five return values and from one equation.
- Orientation: split the `CAP = 200` sentence and added that `td_control.py` kept the cap.
- Cut section: "The task is over there, no rewards follow, and..." became "No rewards follow a terminal state, so its value is always 0."
- Cut section: added "The same argument holds for action values."
- Target caption: "give this target as their Eq. (6)" became "give the rule for state values as their Eq. (6)", and the Gymnasium clause became its own sentence.
- Outside-the-task paragraph: cut "Pardo and colleagues and Gymnasium's tutorial both treat that case separately." and moved its two citations onto the preceding sentence. "On the course's grid" became "On this grid".
- Both-flags paragraph: replaced the last two sentences (the table starting at 1) with one sentence saying the goal's estimate keeps its starting value.
- Gymnasium section: "Neither flag stops the environment, and after either one the agent's loop calls reset" became "After either one, the loop has to call reset before it steps again."
- Gymnasium section: recast the `grid_env.py` step sentence so the generator attaches to the right verb.
- Gymnasium section: "Gym's step before version 0.26" became "In OpenAI Gym before version 0.26, step".
- Runs section: moved the cells 5 and 10 sentence from Fig. 2's caption into the prose.
- Runs section: reordered the cut-as-terminal paragraph to open on p, and "Its values are lower than the optimal ones" became "Its estimates are lower than the optimal values".
- Runs section: varied the three "At N moves" openers, and "the same estimates" became "identical estimates", which the bitwise check supports.
- Takeaway: replaced the first sentence, which was taken from the commission. "On the course's grid under a four-move limit" became "Under a four-move limit on the grid".
- Go deeper, Pardo row: added Section 2.2 (p. 4048), their resting-point calculation with a third of the targets stopping at the limit.
- Code, output, figures and the problems are unchanged. `nb stamp` gives words=4197, reading_minutes=18, sources=7. The proof with link checks gives BLOCK: 0, WARN: 1. The warning is W-CITE-DENSITY on the runs section, which holds only the lesson's own runs and which the series prompt exempts. The verdict is PUBLISHABLE.

## Decision

approve. The argument holds under every rerun and test I could build, and each problem I found was fixable by editing the page.
