# Editorial review: reinforcement-learning/action-masking-in-q-learning (editor/02)

Editor model: claude-opus-5-5 (Opus 5.5), harness Claude Code. This round answers the
reader check in `review-brief.md`. Scratch work is in
`/tmp/claude-0/-home-user-the-nightly-build/84eccc3f-e59d-500c-be1e-12104b5380af/scratchpad/rl-editor2/`.
The page as it stood before this round is saved there as `article-before-editor02.html`.

## Correct

The thesis is unchanged from editor/01. When legality depends on the state, Q-learning
has to mask the max in its target as well as its choice. A move it never makes keeps its
initial estimate, and a max over all six reads it. The claims under it:

1. Masking both places learns q* and solves the puzzle from every start. Masking only
   the choice leaves every legal estimate nine or more moves out at −1, and the greedy
   agent loops.
2. The choice-only agent can rest only at the solution of the optimality equation for a
   puzzle with an extra episode-ending move worth Q0. That solution has one value, and
   it matches v* out to eight moves and is −1 beyond.
3. Starting every estimate at −10 removes the effect without masking the target.

All three still hold. One reported figure behind them was wrong, and I missed it in
editor/01.

**The error columns graded the goal.** leak.py averaged |Q − x| over all 240 legal
pairs, and that count includes the goal's two legal moves. The goal ends the episode, so
the agent never acts there and those two estimates keep their initial value.
resting_point() bootstraps from the goal like any other state, so it gives each of them
−1 + 0.9 × 10 = 8, a value the puzzle has no use for. That added 2 × 8 / 240 = 0.067 to
every init-0 error and 2 × 18 / 240 = 0.15 to each init −10 error. I found it while
checking the reader's step-size question. Seed 5's masked-target error stopped at 0.067
from 10,000 to 20,000 episodes. The −10 agents stopped at exactly 0.150 at 20,000 and
40,000 episodes. In both cases the mean error over the other 238 pairs was below 0.001. I changed leak.py
to grade the 238 legal pairs outside the goal, printed the errors to three decimals, and
reran it.

| row | before | after |
| --- | --- | --- |
| masked target, error q* and rest | 0.08 | 0.009 |
| target over all six, error q* | 2.45 | 2.405 |
| target over all six, error rest | 0.07 | 0.002 |
| init −10, both rows | 0.47 | 0.325 |

The start, fewest and random columns and the resting-point table are unchanged. The prose
now says "within 0.01", "2.4", "0.002" and "0.33". Every conclusion is the same, and the
choice-only agent's match to the derived resting point is closer than the page said. This
is the only change to a printed number, and it comes from a rerun of the page's own
listing. Some draft-handoff figures for off-page checks share the same artifact: the
episode-ending check's "0.067" and probably the optimistic-start "0.017". Neither is on
the page.

Other checks this round:

- Listings. After every listing change I extracted hanoi.py, masked_q.py and leak.py
  from the page and ran them with `uv run`. Both outputs match the page byte for byte.
  leak.py takes about 41 s.
- The loop, traced from run 0 of the target over all six. Every legal estimate in
  states 0, 1, 7 and 6 is exactly −1.0. np.argmax takes 0 → 1 and then 0 → 2, which are
  both optimal. After that it takes 1 → 0 and 0 → 1, between states 7 and 6, which are
  13 moves out. The new trace sentence says exactly this.
- The −10 agents need more training, and nothing else is wrong with them. At 10,000
  episodes they take the fewest moves from 78.4 starts, and at 20,000 from all 80 in
  every run. Their tables stay identical to each other. The page says "with more
  episodes both reach all 80", without the throwaway numbers.
- Seed 5's one long start is also unfinished learning. At 5000 episodes state 52's best
  estimate is −6.45 against −5.43. At 10,000 episodes it takes the fewest moves from all
  80 starts.
- The constant step size. The new sentences say that the SARSA lesson's step sizes
  shrank to average out random slips, and that nothing here is random. Two facts back
  that up. The output's resting-point table matches v* at every distance. With a constant
  0.5, seed 5's mean error over the 238 pairs is 0.0002 at 10,000 episodes, and its
  largest single pair is 0.014 (`checks/perpair.py`).
- Go deeper 01's new reason. The printed release URL shows the update inside
  `if not (done or truncated)`, and the printed main URL shows
  `td_target = reward + discount_factor * (1 - terminated) * next_max`.
- The Taxi clause comes from taxi.py's class docstring at v1.4.0, lines 37–38: "navigating
  to passengers in a grid world, picking them up and dropping them off". I updated
  source 1's locator.
- Links. The proof ran with link checks on, and none blocked. No href is new this
  round. The PettingZoo page, both tutorial pages and both arXiv abstracts return 200.
  The GitHub addresses are the ones I opened in editor/01.
- data-nb-kind. All six remaining sources are primary: each is the owner's own code or
  docs. I removed four sources that nothing cites any more: Dietterich, PR #1812,
  OpenSpiel and the Hanabi Learning Environment.
- Headline, dek and headings are unchanged and still match the output: "more than eight
  moves", "stay at 0" and "−1".

No disagreement between the record and a source I opened.

## Reads well

**The reader check.** The reader's restatement gets the mechanism and the fix right, with
one mismatch. It lists "starting every estimate at or below −10" as a second fix equal to
masking the target, and its place 4 says it could not tell. The page now says the −10
start is a test of the explanation, and that masking the target remains the fix.

My action on each place, cutting first:

1. *Two Gymnasium Taxi documents.* Cut the docstring aside, meaning the index bug, PR
   #1812 and "though not the target". The only Gymnasium document left in the body is the
   tutorial. Go deeper 01 now says what is wrong with the 1.4.0 version: it skips the
   update on the step that ends an episode.
2. *Constant step size.* Added three short sentences. The reader has to accept that a
   constant step converges here, or the runs mean nothing.
3. *Fig. 1's "1 → 0".* Redrew it. The "max over all six" outline now encloses all four
   never-updated zeros, not the 1 → 0 column. The arrow carries "estimate −5.88", and
   the prose and caption name the estimate of the move just made.
4. *Pessimistic-start rows.* Kept, because they are the removal test for the causal claim
   and the series direction requires one on the page. The paragraph now says they test
   the explanation by changing only the initial estimates. It says masking stays the fix
   because a low enough start needs a lower bound in advance. It says the 70 of 80 is
   unfinished learning.
5. *The contraction step.* Rewrote it as an inequality, with a pointer to value
   iteration's non-expansion.
6. *Unintroduced terms.* Cut the Taxi no-op comparison, and cut OpenSpiel, Hanabi and
   Dopamine from the body and the Why card. Taxi and PettingZoo each get a few words.
   MaskablePPO is introduced as an off-the-shelf agent that a later lesson trains. "DQN"
   is gone from the page, Go deeper included.
7. *Two places, then three.* The tutorial sentence, the takeaway and Go deeper 01 all say
   two places now.
8. *The loop asserted.* Added the four-move trace.

Sections the reader could skip:

- The environment section. Cut the Taxi comparison and the int8/bool trap, in the prose,
  the four demo lines and the output line. The conventions are now one sentence, which
  the decisions log asks for. I kept the no-op rule and the check_env reason, because
  they are the commission's convention comparison.
- The Taxi docstring aside and the OpenSpiel/Hanabi citations: cut.
- The −10 paragraph: kept and reframed (place 4).

Results reported without meaning:

- "Ten more seeds…": cut. It was a seed check, which the series direction keeps off the
  page. The findings are recorded above.
- The init −10 rows are explained (place 4).
- The equal "error rest" and "error q*" columns: one sentence now says the masked
  target's resting point is q*.
- The `sample(mask=...)` output line: the demo paragraph now says that actions are
  positions in MOVES and that the draws fall only on actions 0 and 1.

What else went, and why:

- "DeepMind's OpenSpiel library masks both places in its PyTorch DQN." It came last in
  the Why card and used a term the course has not taught.
- "It moves the smallest disk to peg 1 and the next disk to peg 2. Then it moves…" This
  repeated the new trace a paragraph later. It is now one clause.

Lifted: the non-expansion step had been compressed past the point a reader could check,
and the step-size sentence asserted its fit without giving the reason. Both now give the
reason beside the claim. I held my own additions to the placeholder test. "Masking the
target remains the fix" depends on its nouns and answers the reader's question. Headings,
dek and the opening and closing sentences of both cards are unchanged from editor/01,
which checked them against the recent record.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 and 1280 px, in
light and dark. There is no horizontal scroll and the console shows no errors. In the
redrawn Fig. 1 the group outline, its label and "illegal: never updated" stay clear of
each other in all four views. "estimate −5.88" sits under the arrow, clear of both peg
rows. Fig. 2 is unchanged and still stacks on a phone.

Prose words on the rendered page come to 2,231, by the same script and rule as editor/01:
cards, captions, legends, problems and answers count, and code, output, equations, figure
text, bands, sources, headline and dek do not. My first answers to the reader brought the
page to 2,395. To get back to about 2,200 I cut the int8/bool trap as a whole idea, cut
the seed sentence, and merged the duplicate loop description. The other cuts are listed
above. The explanation the reader asked for stays whole.

What the page gives beyond its sources: it derives, and checks against its own runs,
that Q-learning masking only its choice solves the optimality equation of a puzzle where
every state offers an episode-ending move worth the untouched estimate. That says which
values break and where: nine or more moves out, at −1. The original-work sentence in the
handoff says the same, and the corrected 0.002 makes that check sharper. The headline's
claim still matches Fig. 2 and the output.

**Second check.** These changes do not alter the central explanation, and no section is
rewritten whole. The environment section lost three sentences and had one paragraph
recast, and the resting-point section gained sentences inside its existing argument.
Four printed error figures did change through the leak.py fix. They mean what they meant
before, but no reader has seen the new values.

## Edits

1. Why card: cut "DeepMind's OpenSpiel library masks both places in its PyTorch DQN."
2. Orientation: "raises the estimate from −5.88" → "raises the estimate of the move just made from −5.88".
3. Fig. 1: added "estimate −5.88" under "reward −1" at the arrow.
4. Fig. 1: the "max over all six" outline now encloses the four zeros. Its connector and label moved right, "illegal: never updated" was recentred, and the aria-label was updated.
5. Fig. 1 caption → "…to peg 0, a move whose estimate is −5.88. Each outline marks what one version of the target reads at the start."
6. Environment: "reaches every legal pair" → "every legal pair outside the goal".
7. Environment: the conventions paragraph was recast. Taxi now carries a clause describing it, and MaskablePPO is "an off-the-shelf agent a later lesson trains". The PettingZoo clause reads "PettingZoo's multi-agent games put the mask in the observation", and the last sentence reads "hanoi.py has that method too, and it returns the mask as booleans."
8. Environment: cut "Taxi treats a move into a wall the same way, and a pickup or drop-off in the wrong place as a no-op that pays −10." and its two citations.
9. Environment: the demo paragraph's int8 sentence was replaced by "An action is a move's position in MOVES, so the start's two legal moves are actions 0 and 1, and sample(mask=...) draws uniformly between them" (cited to discrete.py).
10. hanoi.py: removed the four lines that sampled with the boolean mask, reran it, and removed the matching output line.
11. Choice-only: cut "Gymnasium 1.4.0's Taxi documentation skips that step… The main branch has since fixed the index, though not the target." and its two citations.
12. Choice-only: "names the three places: the random choice, the greedy choice and the max in the update" → "masks the same two places".
13. Choice-only: cut "OpenSpiel's PyTorch DQN and the DQN in the Hanabi Learning Environment's fork of Dopamine also mask the target's max."
14. Choice-only: "The step size is a constant 0.5, which suits a puzzle with no chance…" → "Both agents use a constant step size of 0.5. The lesson on SARSA and Q-learning shrank its step sizes to average out the grid's random slips. No move or reward in this puzzle is random, so a constant step is enough."
15. leak.py: grades the 238 legal pairs outside the goal (LIVE, with a comment saying why), prints the errors to three decimals and rewords the legend. Reran it and replaced the output.
16. Results: "ends 0.08 from q* … over the 240 legal pairs" → "ends within 0.01 of q* … over the 238 legal pairs outside the goal".
17. Results: cut "Ten more seeds solve the start just as fast, though one of those runs takes a move too many from one other start."
18. Results: "2.45" → "2.4".
19. Results: the two sentences describing the loop → "After two moves it shuttles the smallest disk between pegs 0 and 1 for as long as it may move (Fig. 2)."
20. After Fig. 2: "From the start, that rule leads into the loop." → "…first legal move in MOVES. That is 0 → 1 at the start and 0 → 2 next, both best moves, and after that 1 → 0 and 0 → 1 over and over."
21. After Fig. 2: merged the two 29-of-80 sentences into one.
22. Resting point: ", and the puzzle has no chance, so no average is needed" → ", here with no average to take".
23. Resting point: "Taking the larger of Q0 and each of two numbers never moves them further apart." → "Q0 is the same in every table, so the max stays a non-expansion, as in value iteration: |max(Q0, x) − max(Q0, y)| is never more than |x − y|."
24. Resting point: "The five runs end 0.07 from this resting point on average." → "The five runs with the target over all six end 0.002 from this resting point on average. For the masked target the resting point is q* itself, so its rows give the same error twice."
25. Resting point: "The last rows of the output start there." → "The last rows of the output test this, changing only the initial estimates."
26. Resting point: "Both learn more slowly … for reasons this lesson doesn't take up." → "Masking the target remains the fix, since picking a low enough start needs a lower bound on every value in advance. After 5000 episodes both agents that start at −10 are also still 0.33 from q*, and they take the fewest moves from about 70 of the 80 starts. With more episodes both reach all 80."
27. Takeaway: "mask the random choice, the greedy choice and the max…" → "mask both places: the choice, random or greedy, and the max over the next state's moves."
28. Go deeper 01 → "both places masked in working code. Read the main-branch version, since the 1.4.0 version skips the update on the step that ends an episode."
29. Go deeper 02: "carries both into DQN" → "carries both into a neural-network Q-learner".
30. Sources: removed Dietterich, PR #1812, OpenSpiel and HLE. Renumbered discrete.py to 5 and the tutorial to 6. The Taxi locator is now "class docstring, lines 37–38; ## Information, lines 130–141; action_mask(), lines 417–436", and the discrete.py locator no longer cites the int8 assertion.
31. Ran `nb stamp`: words 4382, sources 6, 19 min.

Proof after the last edit, with links on: BLOCK 0, WARN 2. Both warnings are the
W-CITE-DENSITY warnings the orchestrator accepted, on `orientation` and `resting-point`.

## Decision

approve. The reader's restatement now matches the main idea. Every place it got lost is
cut or explained. The grading artifact is fixed by rerunning the page's own listing, and
every change was an edit I could make from the record and this checkout.
