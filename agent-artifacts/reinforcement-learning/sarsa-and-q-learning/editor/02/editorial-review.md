# Editorial review: reinforcement-learning/sarsa-and-q-learning (editor/02)

This review answers the reader check in `editor/02/reader-report.md`. It follows editor/01, which approved.

## Correct

The thesis and its claims are as editor/01 stated them, and none of my edits changes them.

The reader's restatement matches the main-idea sentence in `draft-handoff.md`. It names the shared TD update and the one term that differs. It says SARSA rests at the values of the ε-greedy policy it follows, which is the best ε-soft policy and not optimal at ε = 0.5, and that Q-learning rests at q* whatever the agent does. It adds two points the main-idea sentence leaves out, off-policy learning and the lower earnings of Q-learning's agent, and both are on the page. So the restatement shows no mismatch.

New checks:

- The claim that the two cell-10 runs settle when run longer. I reran seeds 12 and 14 of Q-learning (scratchpad `cell10.py`, which imports `code/`). At 100,000 episodes both have only cell 10 wrong, aiming down. At 200,000 episodes neither has a wrong arrow. The page now says "twice as many episodes", and the reader's complaint that "longer" was unquantified is answered.
- The new clause saying the agent keeps updating every pair. `td_control` starts each episode at a uniformly random cell in `LIVE`, and with ε = 0.5 every move has probability at least 0.125. So every pair is updated infinitely often with probability 1, which is the condition Watkins and Dayan need.
- The new sentence on Expected SARSA, "it moves each estimate the way SARSA moves it on average", rests on Sutton and Barto p. 133 in the evidence record: "Given the next state, S_{t+1}, this algorithm moves deterministically in the same direction as Sarsa moves in expectation." The citation keeps both of its locators.
- The new reason in the book-order paragraph, that Q-learning's target never uses the drawn move, can be read straight off equation (6.8). Van Seijen et al. §III, p. 2 makes the same point for Expected SARSA, but I did not add a citation.
- The non-expansion step. The ε-greedy average weights the maximum by 1 − ε and each of the four estimates by ε/4, and those weights add to 1. The maximum is a non-expansion, which is the argument lesson 2 made, and so is each single estimate. A weighted average of non-expansions with weights that add to 1 is also a non-expansion. The step holds.

Why the citation printed as "167": the Expected SARSA sentence ended in three `sup.nb-cite` elements, 1, 6 and 7, with nothing between them. On screen they are three small bordered chips that touch. In the page's text, which is what the reader agent got, the labels run together as "167". I gave each citation its own clause, so they now print as "…on average.1 George John introduced it in 1994,6 and van Seijen and colleagues named it in 2009.7". No other adjacent citations are left on the page. Outside this article, lesson 1 (`environments-and-the-rl-problem`) has two adjacent pairs that will read the same way in text.

MIT Press link: kept, as the orchestrator decided. The proof's link check passes.

## Reads well

How I handled each place in the reader report, in the report's order. For each one I asked first whether the passage could go.

1. **Book order of the next-move draw.** Not cut, because the commission asks the lesson to teach this difference. The reader could not tell why the order could matter. I replaced the middle sentence with the reason: Q-learning's target never uses that move, so the code can draw it before the update in both methods and b stays the only difference. The rerun sentence stays, shortened to "changed no conclusion below". The paragraph is still three sentences.
2. **Expected SARSA, named and dropped, and "167".** Not cut, because the commission asks for one sentence with John and van Seijen credited. The reader could not see why it sat in a section about resting points. The sentence now says what Expected SARSA does in that section's terms: it puts π's average in the target, so it moves each estimate the way SARSA does on average. Problem 1's answer already uses it. I split the attribution into its own sentence, which also fixed "167".
3. **The earnings paragraph's direct solve and "the rest".** Not cut, because the paragraph is the commission's second result and its removal test. I made the implied step explicit: the ε-greedy policy moves like its arrows on the modified grid, so "the direct solve on that grid therefore gives the policy's exact value." "Account for the rest" now reads "account for that last 0.01".
4. **The undefined error in Table 1.** The caption now defines it: "Errors are absolute differences from the exact action values, averaged over the 56 (cell, move) pairs and the 20 runs." This matches `np.abs(Q - q_soft)[LIVE].mean()` in `targets.py`. The prose already sets 0.08 beside 4.9, which gives the scale.
5. **"Both turn it right when run for longer."** Rewritten to remove both ambiguities: "have a wrong arrow at cell 10" and "Both have the optimal arrow there when run for twice as many episodes, so they had not finished converging." This also gives the meaning the reader asked for under results without meaning.
6. **The terse non-expansion step.** The main idea needs this step, so I added explanation. The clause became a sentence. It says the ε-greedy average weights the largest estimate and the four estimates by amounts that add to 1, and that, as in value iteration, none of these moves by more than the largest per-move gap. That is lesson 2's own wording for the argument.
7. **Whether the behavior policy updates every pair.** The main idea's "whatever the agent does, while it explores" depends on this, so I added one clause where the page says the policy decides only which pairs get updated: "and an ε-greedy agent that starts each episode in a random cell keeps updating all of them."
8. **"For a fixed π" read as circular.** Changed to "For each π". The next paragraph still makes π depend on Q.
9. **Headline against 18 of 20.** Kept. Item 5's sentence now says on the page that the two misses had not finished converging, and the derivation and theorem back the claim.

Skippable sections the reader named:

- The book-order paragraph and the Expected SARSA sentence stay, because the commission requires both. They are handled under 1 and 2.
- The history sentences (Rummery and Niranjan, Watkins 1989) stay. The series prompt asks the lesson to link the paper that introduced each method.
- The Singh et al. and Watkins–Dayan scope sentences stay. The commission requires the Singh scope sentence. The Watkins–Dayan sentence on separate stretches of experience is what lets the Singh paragraph say "for SARSA" the runs are the evidence.
- In the estimates section, I cut the sentence on the average over the 14 starting cells. It was a side result the main idea doesn't use, and the reader flagged it as reporting a result without its meaning. I narrowed the paragraph's first sentence to what remains: "From cell 9, Q-learning's agent also earns less than SARSA's." That matches the takeaway. I removed its row from `targets.py` so the script prints only numbers the page uses (see Edits). The cell-9 figures and their removal test stay.

Results reported without saying what they mean:

- Book order: answered by the new reason sentence (item 1).
- The 14-cell average: cut (above).
- Seeds 20 to 39: cut. The series prompt lets seed checks stay off the page. The two misses are now explained by the doubled run, and editor/01's rerun of seeds 20 to 39 (20 of 20 for each method) still stands in that review.
- "About −7.3": the paragraph now says what the number shows before giving it: "So only SARSA's estimates predict what its agent earns." I replaced "close to the −1.01 that…" with "which estimates what an agent earns by following the optimal arrows and never moving at random". That leaves one number fewer, and −0.98 now sits beside −7.3.
- Table 1's error rows: defined in the caption (item 4).

Edges: I read the first and last sentence of each changed paragraph on its own. The estimates section's second paragraph now ends on the 0.01 accounting, which is a plain factual close before the Problems note. No new sentence fails the placeholder test. None borrows from the briefing or from the voice guide's quoted passages.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 px and 1280 px, in light and dark, with the details closed and open. I also captured element shots of the four changed sections. Neither width scrolls sideways. The new sentences wrap cleanly. Table 1 still scrolls inside the engine's table wrapper at phone width, as editor/01 recorded. The new citation chips sit at clause ends without crowding. The figures are unchanged.

Word count by the template's definition: 2,208, against 2,177 for the page editor/01 approved, on the same counter. Editor/01's counter gave that page 2,189, so on its counting this page is about 2,220. The additions answer the reader check. I offset them by cutting two whole results, the 14-cell average and the seeds 20–39 sentence, and none of the explanation that stays was shortened.

What the piece gives beyond its sources is unchanged from editor/01. It derives both resting points from the average of one target term, identifies SARSA's fixed-ε resting point with lesson 5's best ε-soft policy, and checks both with paired runs and exact solves on the course grid.

Second reader check: my changes do not rewrite the central explanation or any whole section. The derivation's argument is unchanged. Two of its sentences were clarified ("For each π" and the non-expansion sentence), and one clause was added on every pair being updated. Every other change is to a sentence or a clause, or is a cut.

## Edits

Edits were made in `scratch/article.src.html` and `code/targets.py`, then rebuilt with `scratch/build.py` and run through `nb stamp` (words 4012, 17 min, 7 sources).
- Update rules, book-order paragraph: "The code below draws it before the update in both, so that b is the only difference. Rerunning Q-learning in the book's order changed none of the conclusions below." became "Q-learning's target never uses that move, so the code below can draw it before the update in both methods, which leaves b as the only difference. Rerunning Q-learning in the book's order changed no conclusion below."
- Target averages: "For a fixed π" became "For each π".
- Target averages, q̃ paragraph: the clause "since an ε-greedy average of four numbers moves by no more than the largest of them moves" became its own sentence: "Its ε-greedy average weights the largest estimate and the four estimates by amounts that add to 1, and as in value iteration none of these moves by more than the largest per-move gap."
- Target averages, Q-learning paragraph: added ", and an ε-greedy agent that starts each episode in a random cell keeps updating all of them" after "which pairs get updated and how often".
- Target averages, Expected SARSA: recast as "Expected SARSA puts π's average itself in the target, so it moves each estimate the way SARSA moves it on average.[1] George John introduced it in 1994,[6] and van Seijen and colleagues named it in 2009.[7]" The locators are unchanged, and the three citations no longer touch.
- Table 1 caption: "Errors are averaged over…" became "Errors are absolute differences from the exact action values, averaged over…".
- Cell-9 results paragraph: "The other two aim cell 10 wrong, where the best move beats the next by 0.35, and both turn it right when run for longer." became "The other two have a wrong arrow at cell 10, where the best move beats the next by 0.35. Both have the optimal arrow there when run for twice as many episodes, so they had not finished converging."
- Cell-9 results paragraph: cut "On seeds 20 to 39 every SARSA run ends on the best ε-soft arrows and every Q-learning run on the optimal ones."
- Estimates section, first paragraph: added "So only SARSA's estimates predict what its agent earns."
- Estimates section, first paragraph: "Q-learning's estimates put cell 9 at −0.98, the largest of its four, close to the −1.01 that an agent following the optimal arrows without random moves earns from there." became "Taking the largest of its four, Q-learning's estimates put cell 9 at −0.98, which estimates what an agent earns by following the optimal arrows and never moving at random."
- Estimates section, second paragraph: "Q-learning's agent also earns less than SARSA's." became "From cell 9, Q-learning's agent also earns less than SARSA's."
- Estimates section, second paragraph: "…with probability ε, so the direct solve gives its value exactly." became "…with probability ε. The direct solve on that grid therefore gives the policy's exact value."
- Estimates section, second paragraph: "…within 0.01 of SARSA's, and the two runs that aim cell 10 wrong account for the rest." became "…within 0.01 of SARSA's. The two runs with a wrong arrow at cell 10 account for that last 0.01."
- Estimates section, second paragraph: cut "Averaged over the 14 starting cells the gap shrinks to a few hundredths per episode, because cell 9 is the only cell where the two policies aim differently."
- `code/targets.py`: removed the `v[LIVE].mean()` column and its label "exact value averaged over the 14 starting cells". The script is now 98 lines. I extracted every listing from the six built pages into a fresh folder and ran `uv run targets.py` (114 s). The output is the old output with that one row gone, and every other number is identical. `scratch/targets_out.txt` now holds the new output, and the printed output on the page matches the run. Fig. 1 and Fig. 2 do not depend on `targets.py` and are unchanged.

Proof after the edits: BLOCK 0, WARN 5, PUBLISHABLE. These are the same five warnings editor/01 accepted. The two W-SENTENCE-DENSITY warnings are still the TeX of the two average-target equations, which I checked with the proof's sentence splitter. The three W-CITE-DENSITY warnings are on sections made of a worked case and runs.

## Decision

approve: every place in the reader report is cut or answered and the restatement matches the main idea. The proof is publishable, the listings rerun to the printed output, and no change rewrites the central explanation or a whole section.
