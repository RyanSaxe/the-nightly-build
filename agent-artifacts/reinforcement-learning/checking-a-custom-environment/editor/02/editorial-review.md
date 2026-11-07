# Editorial review: reinforcement-learning/checking-a-custom-environment (editor/02)

This round answers reader check 1.

## Correct

The reader's restatement matches the handoff's main-idea sentence. It says `check_env` tests shape and seeding and compares the environment only with itself. It says a wrong rule shows when a fixed policy's average discounted return misses the value solved from the rules, that random moves cannot separate slip rules that give every aim the same turn probabilities, and that the hand-drawn policy cannot see errors in moves it never makes. No part of the main idea was missed or misread, so the central explanation did not need to change, and it has not.

New statements this round, and how each was checked:

- "none past the second move after a reset" (now in the ranges section, cited to `check_env` L477-482 and `check_returned_data_not_reused` L273-307). I reread both in the 1.4.0 wheel. The passive step and the two determinism steps each follow a reset. The data-reuse check resets and takes up to two steps. A throwaway probe that numbers each step within its episode, run three times, gave a deepest move of 2 every time, with every step starting in cell 0 or 8. The new wording of the checker's last check in the first paragraph ("resets, takes up to two steps and resets again") comes from L285-293.
- `PassiveEnvChecker` "a check of form on only the first reset and the first two steps": the claim is unchanged from the approved page (common.py L287-326), and only its wording changed.
- `NeverEnds`' large returns: its goal and pit end nothing (bugs.py, `==` for `in`), so their rewards repeat until the 200-move limit. This follows from the code and matches the problem 2 answer. The correct copy differs by that one character and stays inside the bounds, so the page already holds the comparison that removes the cause.
- "A step that swaps the aims up and down" as an example of relabelling: I reran editor 01's exact solve. Random's value is −10.904 under the swap, the same as under the rule, with max |ΔP| = 0, and hand-drawn's is −7.431.
- The hand-drawn blind spot now gives its reason from the rule: an up aim slips left or right, and a right aim slips up or down. `PI` aims up in 5, 9 and 13 and right in 10. The exact solves still give 1.360 for hand-drawn, against −11.610 and −11.005 for random, in the two blind-spot cases.
- Play by hand can show an error in `move` or `R`. This is a reasoned claim, not a run. The player judges each landing against the grid the first lesson drew, not against `gridworld.py`, which both baselines and their exact values import. The page already says play by hand is weakest against frequency errors, so the claim names only moves and rewards.
- Stable-Baselines3: "turns it into a one-hot vector of 16 floats before its network reads it" (preprocessing.py L122-124, docs note), and so every input is 0 or 1. That is arithmetic on the one-hot vector, not a new claim about the library.

One correction I made to my own draft this round: I had listed `SLIP` with `move` and `R` as shared by both sides. That is true, but problem 1 has a copy whose own `step` uses 0.02, and a reader would then take the answer to contradict the body. The sentence is back to `move` and `R`. The takeaway's "unless the environment and the solve share the error" covers the general case without naming it.

Every listing was rerun exactly as printed, from a fresh folder holding only the four course files and the five lesson files extracted from the page. bugs.py and baselines.py exit cleanly. checker.py, behaviour.py and both piped play.py runs print output byte-identical to the page. All five page listings are byte-identical to code/. Two listings changed: ArrayCell's docstring, and checker.py, which lost its call-counting class and the last line of its output. Neither change touches what the other outputs print. No href changed, and the proof's link check passes.

## Reads well

Each place the reader lists, and what I did with it:

1. Fig. 4 and the Stable-Baselines3 paragraph. I cut the figure. A one-hot vector needs no drawing for a reader with production ML experience, and the figure did not say why it was there. The pointer stays, because the commission asks what a neural agent receives from the observation. It is now two sentences that end on the consequence for this lesson's check: every input is 0 or 1, so the observation needs a range check and not a scale check. It calls the library "one library of off-the-shelf agents", which ties it to the agent that Why this matters promises.
2. The render-mode and PassiveEnvChecker paragraph. The commission requires `PassiveEnvChecker`, so I rewrote the paragraph rather than cutting it. Render modes are now defined as "the ways an environment can draw itself", and `gymnasium.make` as building an environment "from a registered name". The paragraph now ends on what the wrapper checks. I cut the sentence about "an episode's third move", which no bug on the page illustrated. The limit appears once, in the ranges section, as "no further than the second move after a reset". That is where the cells column, which sees every move, makes the contrast useful. The first paragraph now says that the data-reuse check takes up to two steps, so the limit follows from what the reader has already been told.
3. "The cells check_env started from." Cut. The count sat inside the shared-seed argument and suggested that more start cells would help, which the argument rules out. I moved it below the output first, but the lesson was then past its length (see The experience). I cut it as a whole result: the sentence, the `Counted` class in checker.py and the output's last line. The docs' "variety of values" quotation went with it.
4. "The second line is the one to read." Cut, along with the sentence before the display that restated the column-sum argument. The sentence now says what the sum computes, and the caption explains the change of variable, which the reader found clearer.
5. The heading. It now reads "One character sends a slip backward in every cell", and the body sentence says "in every cell". No heading on the page names a cell now.
6. "Fig. 2 also shows what the hand-drawn policy cannot see." The reference to Fig. 2 is gone. The paragraph now gives the reason from the rule: a policy that aims up never moves down, and one that aims right never moves left. The reader can check 5, 9, 13 and 10 against that reason without opening the earlier lesson.
7. Shared `move` and `R`. Kept, because without it the main claim overreaches. Its answer went to the play-by-hand section, which now says the player judges against the grid itself and so can see such an error. The takeaway now carries this blind spot alongside the others.
8. "a short sum" and "relabels the aims". The Why card's forward reference now says plainly that for random moves you can derive which errors they miss. The derivation itself stays in the body, and the dek already gives the case. The relabelling sentence gains the example of a `step` that swaps the aims up and down.

Minor terms: ArrayCell's docstring no longer says "Box space". `play` is now "Gymnasium's own `play` function", which needs "the pygame package and an environment that renders itself as images". Schulman is introduced as giving the checklist in a 2016 talk on deep RL research.

Results reported without saying what they mean:

1. NeverEnds' large returns: one clause says why, in the first place they appear.
2. and 3. The hand-drawn rise and the `up_or_right` fall: I added that a wrong rule can move a value either way and the test flags both. I did not explain the direction. That would be a claim about the cause of a run, and the series requires such a claim to carry its own removal test on the page. The main idea needs only the size of the gap. The code for `up_or_right`'s −4.18 was already printed. The sentence that introduces the policy now says `behaviour.py` adds it with its exact value.
4. The 12 resets and 5 steps: cut (place 3).
5. "more episodes would not flag the random row": cut. The next section proves it with the derivation, and nine more seeds still back the flags.

Sections the reader could skip. Play by hand and the ranges check are the commission's required checks and stay. Play by hand now has a role no baseline has, in item 7. The render and PassiveEnvChecker paragraph shrank to what the commission asks for, and the derivation display stays because the series requires the derivation in full.

Nothing in the new text came from the briefing or the voice guide. The new sentences use the article's nouns. I tested each new paragraph edge with the placeholder test. "A wrong rule can move a value either way, and the test flags both" survives, because it states the two-sided flag on |z| > 3.

## The experience

Prose on the rendered page, counted the same way before and after (my extraction: the headline, dek, headings, cards, captions, legend, problems and labels; not code, output, display or inline math, SVG text, the reading bands, sources, contents or navigation): 2,216 before this round and 2,272 now. Counting sentences only, leaving out headings and labels, it is 2,139 before and 2,193 after. Editor 01's 2,205 used a slightly different extraction. The reader's places needed about 120 words. Cutting Fig. 4 and its caption, the call count, the restated column-sum sentence, "more episodes would not flag the random row" and the takeaway's restatements recovered most of them, and the lesson sits at about 2,200. Stamped words are 4,366, down from 4,424, and the reading time is 19 minutes.

Visuals: Figs. 1 to 3 and the equation are unchanged. Fig. 4 is gone, and the ranges section now runs from its heading straight into text and the problems. I looked at the changed sections (orientation, checker with its shorter output, by-hand, ranges, takeaway) at 390 px and 1,280 px in light and dark. Nothing overlaps, no horizontal page scroll appears at either width, and the code blocks scroll inside their frames as before.

What the page gives beyond its sources has not changed since review 01: a proof, confirmed by a run and a removal test, that uniform random moves cannot see a slip rule that treats every aim alike or a relabelling of the aims, and a test from the course's exact solutions that catches a one-character bug that passes the checker. The page now also says which blind spot the exact-value test cannot cover, and which check covers it.

## Edits

- Why this matters: the last sentence now says random moves' blind spots can be derived before any episode runs ("a short sum" is gone).
- Orientation heading: "One character sends cell 10's slip backward" → "One character sends a slip backward in every cell"; body adds "in every cell".
- checker, first paragraph: the last check now reads "resets, takes up to two steps and resets again".
- checker, second paragraph: cut the docs quotation and the 12-resets-and-5-steps sentence; it ends "a backward slip happens in both and the two agree".
- checker, last paragraph: rewritten. Defines render modes, says `gymnasium.make` builds from a registered name and adds `PassiveEnvChecker`; the "third move" sentence is cut.
- bugs.py (page and code/): ArrayCell docstring → "step returns the cell inside a one-element array, not as an int."
- checker.py (page and code/): removed `Counted` and the count print; docstring is one line; output loses its last line.
- baselines: `up_or_right` sentence adds "which behaviour.py adds with its exact value".
- baselines results: NeverEnds clause on why its returns are large; "A wrong rule can move a value either way, and the test flags both."; cut "and more episodes would not flag the random row".
- uniform-aims: cut the column-sum sentence and "the second line is the one to read"; the sentence before the display now names what the sum computes.
- uniform-aims: relabelling example, "a `step` that swaps the aims up and down".
- uniform-aims: the blind-spot paragraph gives its reason from the rule's slips; the Fig. 2 reference is cut.
- by-hand: the first sentences now say the player checks against the grid itself and so can see a wrong `move` or `R`; Schulman is introduced by his 2016 talk; `play` needs "the pygame package and an environment that renders itself as images".
- ranges: Fig. 4 cut; the Stable-Baselines3 pointer is two sentences ending on range, not scale; the last sentence now contrasts with "no further than the second move after a reset", cited to source 2.
- Takeaway: adds "unless the environment and the solve share the error"; play by hand is "judged against the grid itself"; two clauses tightened.
- `nb stamp`: words 4366, reading 19 min, sources 10.

Proof: `nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`, links checked: BLOCK: 0, WARN: 3, PUBLISHABLE. The warnings are the same three as before: W-SENTENCE-DENSITY on the TeX source of the display equation (confirmed with the engine's `sentence_density`), and W-CITE-DENSITY on `baselines` and `uniform-aims`, which the series direction exempts.

Second reader check: these changes do not alter the lesson's central explanation, and they do not rewrite a whole section. The derivation, the baseline test, the removal test and every result the reader saw are unchanged. The largest changes are the checker section's last paragraph, the ranges section's first paragraph, the cut of Fig. 4 and the cut of the call count. Each section keeps its structure.

## Questions for the orchestrator

1. I cut a result the evidence record and the handoff both report: `check_env`'s 12 resets and 5 steps from cells 0 and 8 (handoff check 2). The page still states the limit that matters, no further than the second move after a reset, with source locators. If you would rather keep the count and accept a lesson of about 2,230 sentence words, restoring it is one sentence and the `Counted` lines in checker.py. I am going ahead on the assumption that the cut stands.
2. The new claim that play by hand can show an error in `move` or `R` is reasoned, not run. If you want a run behind it, the cheapest one is a piped play of a copy whose `move` misplaces one wall. I did not add it, because the lesson is at its result limit.

## Decision

approve. The reader restated the main idea correctly, every place it lists is now cut or answered, all listings reproduce byte for byte, and the proof has no blocking finding.
