# Editorial review: reinforcement-learning/sarsa-and-q-learning (editor/01)

## Correct

Thesis, from the draft alone: SARSA and Q-learning apply the same TD update to action values, and they differ only in which estimate from the next cell enters the target. That one term decides what each learns. With ε fixed, SARSA's estimates can rest only at q̃, the action values of lesson 5's best ε-soft policy. Q-learning's can rest only at q*, whatever policy makes the moves.

Claims under it, and how each held:

1. The update rules differ in one term, and the code removes the other difference, the book's order of choosing the next move. Held. Equations (6.7) and (6.8) are on pp. 129 and 131, and the two boxes on pp. 130–131 choose the next move in different places. I opened the authors' PDF to check these. I reran the book-order check (`scratch/checks.py after`): 19 of 20 runs end optimal, the error against q* is 0.080 and the return from cell 9 is −7.29. These match the handoff, so the page's one sentence stands.
2. SARSA's average target has q̃ as its only fixed point. Held. I checked every step of the derivation. The ε-greedy average is non-expansive, so the contraction argument goes through. The identification with `best_soft` is the lesson's own step, as the commission asked. Singh et al. are cited for continuing discounted tasks only: Theorem 2 on p. 297, Theorem 3 on p. 299 and the setting on pp. 289–290, all checked in Szepesvári's copy. On seeds 0–19 and 20–39, all 20 SARSA runs end on the best ε-soft arrows.
3. Q-learning's only fixed point is q*, and the behavior policy decides only which pairs get updated. Held. Watkins and Dayan's theorem is on p. 282, and the clause about disconnected transitions is on p. 281, both checked in Dayan's copy. Eighteen of 20 runs on seeds 0–19 end optimal, and 20 of 20 on seeds 20–39. The two misses, seeds 12 and 14, are at cell 10, where q* separates the top two moves by 0.35. I reran those two seeds. Both have cell 10 right at 200,000 and at 400,000 episodes, so the misses are runs that had not finished converging, not a different resting point. The headline's "learns the optimal arrows" is therefore backed by the derivation, the theorem and 38 of 40 runs, with the other two settling when run longer. The page now says so in one clause, and the headline stays.
4. Q-learning's ε-greedy agent earns less from cell 9 because its arrow there points at a neighbour of the pit. Held. The exact solves give −7.10 and −7.30. Turning cell 9 left gives −7.11. Split by run, the 18 optimal runs give exactly −7.097, which is SARSA's value, and the two cell-10 runs give −7.201 each. That accounts for the remaining 0.01.

Reruns. I extracted every listing from the six built pages into a fresh folder and ran `uv run targets.py` (1 min 53 s). The output matches the printed output byte for byte. `figures.py`, pointed at those extracted listings, regenerates Fig. 1 and Fig. 2 byte-identical to the page. In Fig. 2, cell 9 points down for SARSA and right for Q-learning, and every other arrow is optimal. I reran the printed `targets.py` on seeds 20–39 and got the handoff's numbers.

Breaks and fixes:

- Problem 1's answer printed −1 + 0.9 × (−2.44) = −3.19. That product is −3.196, and with −3.19 the next sentence's "2.25 below −0.95" did not subtract. I changed it to −3.20, which makes the 2.25 correct. The exact unrounded values are −3.19 and 2.247. The page works from the values it displays, as the opening case also does.
- The importance-sampling sentence cited Sutton and Barto, Section 5.5, p. 103. I opened the PDF. Page 103 defines the target and behavior policies, and "Almost all off-policy methods utilize importance sampling" is on p. 104. I corrected the locator, then cut the paragraph for length (see Reads well), so the citation is gone.
- "Seeds 20 to 39 give the same split" was loose. Those seeds give 20 of 20 for Q-learning, not 18. I rewrote it as a conclusion without numbers.
- The sampled return from cell 9 under Q-learning does not repeat to one decimal: −7.29 on seeds 0–19 and −7.41 on seeds 20–39. The page now says "about −7.3". The gap in earnings rests on the exact solve, which repeats (−7.30 and −7.29).
- Left as is: the opening case's −2.44 and −1.00 follow from the rounded values the page prints. Unrounded q* gives −2.45 and −1.01. The case's point does not change.
- Left as is: a pair's first `td0` update has α = 1, and Watkins and Dayan state α < 1. The page claims only that N(s, a)^−0.7 meets the two sum conditions, which is true.

Labels in the headline, dek and headings: "half the time" is ε = 0.5. The cell numbers and ε values match the output.

Hrefs. All seven open on their sources: the Cambridge abstract page, which links the PDF; the Watkins thesis PDF; the Springer article pages for both DOIs; the AAAI PDF; and IEEE Xplore for the van Seijen DOI. The four Go-deeper links open their PDFs, and `#page=151` lands on Section 6.4. The exception is the MIT Press page for Sutton and Barto, which returned 403 to a scripted request. I could not load it in a browser from here. It is the href lessons 3, 4 and 5 already use. **For the orchestrator:** confirm it loads in a browser, or switch it to the authors' PDF that the note names.

`data-nb-kind`: all seven are primary, and each is the authors' own document for what it is cited for. The Expected SARSA attribution also cites John and van Seijen et al. directly, so it does not rest on the book's bibliographic remarks. Sutton and Barto's title, "2nd edition, 2018", is right even though lesson 5's differs: the front matter reads "© 2018, 2020" and does not print "second printing".

Proof WARNs: the two W-SENTENCE-DENSITY warnings are the TeX of the two average-target display equations. I confirmed this with the proof's own sentence splitter. The three W-CITE-DENSITY warnings are on sections made of a worked case, runs and exact solves, which the series prompt exempts. I accepted all five.

## Reads well

Cut:

- The off-policy section's importance-sampling paragraph. A reader can explain the main idea without it, the commission allows importance sampling at most a pointer, and it is the whole idea the writer named as the next cut. The cut was for length.
- The opening heading "Two targets from one move into cell 5". It repeated the recent record: lesson 5 opened on "Forty-two moves with no returns" and lesson 1 had "Two files that print the results". It now reads "The random move that only SARSA's target uses".
- "This grid ends its episodes, so here the runs below are the evidence." It repeated the course's "this grid" wording, and it overreached for Q-learning, whose episodic case Watkins and Dayan cover on p. 281. It now reads: "Episodes on the grid end at the goal or the pit, so for SARSA the runs below are the evidence."
- The takeaway's second sentence repeated the dek word for word. I rewrote both. The dek also used "estimate" and "next" three times each, and now reads: "Its update differs from SARSA's in one term: it takes the next cell's largest estimate, whatever move the agent makes there."

Lifted:

- The worked case used 0.9 without naming it, so I added "discounted by 0.9".
- "Aims toward cells 5 and 10" became "aims at cell 5 or cell 10". One arrow aims at one cell.

Checked and kept: the takeaway's "uses X, so its estimates rest at Y" follows the commission's clause order. Its words are the article's own ("estimates rest at", "the move its ε-greedy agent will make"), and that order is the derivation's, so it stays. No sentence borrows from the voice guide's quoted passages. The edges read clean apart from the items above. I kept "These are the two basic methods of TD control" because it introduces the term. The last sentence states the second result.

The draft runs plainer than the voice guide's register, with no personal remarks. Adding them would be polish, not something required.

## The experience

I built the page with `nb preview` and captured it with Playwright at 390 px and 1280 px, in light and dark, with the details closed and then open:

- Neither width scrolls sideways.
- Both figures are legible in both themes, and no label collides with an arrow.
- Inline math wraps on a phone. The KaTeX MathML layer extends past the viewport but is clipped.
- At 390 px, Table 1 scrolls inside the engine's table wrapper, because of the 14rem minimum on the label column. The Q-learning column is hidden until the reader scrolls. I left this as the engine designs it.
- I put a non-breaking space in "cell 9" so the cell-9 heading no longer leaves "9" alone on a line.

I considered adding a drawing of why cell 9 flips. Lesson 5's Fig. 3 already shows it, and the Background band links that lesson, so I added nothing.

Word count by the template's definition: 2,189. That covers the cards, captions, table cells, and problems with their answers, with each inline math span counted as one word. It is 2,223 with the title and dek, and 2,274 with the headings as well. Before my edits it was 2,202, 2,236 and 2,287.

The longest section is the derivation, at 594 words. Each paragraph in it is a step, so it stays. The body ends on the removal test and the problems.

What the piece gives beyond its sources: it gets both methods' resting points from the average of one target term, and it shows that SARSA's fixed-ε resting point is lesson 5's best ε-soft policy, which no source states. It then checks both results, and the cell-9 earnings gap, with paired runs that differ in one line and exact solves on the course grid. That matches the original-work sentence in `draft-handoff.md`.

## Edits

Edits were made in `scratch/article.src.html` and rebuilt with `scratch/build.py`, then `nb stamp` (words 4001, 17 min, 7 sources).
- Dek, in the header and in nb-meta: replaced it with "Its update differs from SARSA's in one term: it takes the next cell's largest estimate, whatever move the agent makes there."
- Orientation heading: "Two targets from one move into cell 5" became "The random move that only SARSA's target uses".
- Orientation, worked case: added "discounted by 0.9" before SARSA's target arithmetic.
- Target averages, Singh paragraph: "This grid ends its episodes, so here the runs below are the evidence." became "Episodes on the grid end at the goal or the pit, so for SARSA the runs below are the evidence."
- Off-policy: corrected the importance-sampling locator from p. 103 to p. 104, then cut that paragraph and its two Sutton and Barto citations (5.5 and 7.5).
- Cell-9 heading: put a non-breaking space in "cell 9".
- Cell-9 results paragraph: added ", and both turn it right when run for longer" to the cell-10 sentence.
- Cell-9 results paragraph: "Seeds 20 to 39 give the same split." became "On seeds 20 to 39 every SARSA run ends on the best ε-soft arrows and every Q-learning run on the optimal ones."
- Estimates section, first paragraph: "return −7.3" became "return about −7.3".
- Estimates section, second paragraph: "aims toward cells 5 and 10, which border the pit" became "aims at cell 5 or cell 10, both next to the pit".
- Problem 1 answer: changed "= −3.19" to "= −3.20".
- Takeaway: "They differ only in the next move whose estimate enters the target." became "The one difference is which estimate from the next cell enters the target."

Proof after the edits: BLOCK 0, WARN 5 (the same five as before), PUBLISHABLE. The listings and printed output are unchanged.

## Decision

approve: the argument holds, every number reruns, and the remaining fixes were made here. The template's reader check is still due before the lesson settles, and the MIT Press href needs a browser check.
