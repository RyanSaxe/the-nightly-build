# Draft handoff: reinforcement-learning/sarsa-and-q-learning (writer 01)

## Main idea (28 words)

SARSA and Q-learning differ only in which next move's estimate enters the TD target, so SARSA learns its ε-greedy policy's action values and Q-learning learns q* while exploring.

## Original work

The lesson takes the expected value of each method's target to show that SARSA's fixed-ε resting point is exactly the best ε-soft policy's q̃ from `best_soft` (the step the commission left to the lesson), and that Q-learning's is q*. It then checks both, and what each agent actually earns, with paired runs that differ in one line of code and with exact solves on the course grid. No source does this.

## Proof

`nb check … --series reinforcement-learning --repo …` with links: **BLOCK 0, WARN 5, PUBLISHABLE.** All five warnings are left on purpose:

- W-SENTENCE-DENSITY ×2: false positives. The "sentences" are the TeX of the two display equations for the average targets (`\begin{aligned} \mathbb{E}…`). They are not prose.
- W-CITE-DENSITY on `orientation` (a worked case with stated numbers), `cell-9` (the runs) and `estimates-describe` (the runs plus exact solves). The series prompt says a section made of runs and derivations needs no citation.

Listings: `td_control.py` and `targets.py` were taken out of the built page, put in a fresh folder with the five earlier lessons' printed files, and run with `uv run targets.py` (1 min 55 s). The output matches the printed output line for line. Fig. 2 is seed 0 of the same code, drawn by `figures/figures.py`, which stays off the page.

Render: I built it with `nb preview` and captured it with Playwright at 390 px and 1280 px, in light and dark, with the details closed and then open. There is no horizontal page scroll. I split the display equations to fit phone width and set the figure legends in short rows. At phone width Table 1 scrolls sideways inside the runtime's table wrapper, as tables are meant to.

Length: by my count about 2,250 words of prose with headings and inline math included, or about 2,200 without the headings. I cut the cliff paragraph, a third problem (Exercise 6.12 on the order of the next-move choice) and a paragraph that repeated the card. The editor's count may land at the 2,200 line. If something has to go, the next whole cut I would make is the sentence in the off-policy section that explains why one-step Q-learning needs no importance sampling.

## Seed and cell checks (throwaway scripts in `.nb-work/…/sarsa-and-q-learning/scratch/`, which import `../code`)

1. **New seeds 20–39** (`reseed.py`, which runs `targets.main` on those seeds): SARSA ends on the best ε-soft arrows in 20 of 20 runs and Q-learning on the optimal arrows in 20 of 20. Mean errors are 0.08 against each method's own target. Cell 9 by the estimates: −7.10 and −0.98. Return from cell 9: −7.12 and −7.41. Exact value at cell 9: −7.10 and −7.29. With cell 9 turned left: −7.10 and −7.10. All conclusions hold. The return from cell 9 repeats only to about one decimal (−7.29 against −7.41 for Q-learning), so the page rounds it to −7.1 and −7.3 and leans on the exact solve for the gap.
2. **Q-learning in the book's order**, choosing the next move after the update (`checks.py after`, seeds 0–19): 19 of 20 runs reach the optimal arrows (seed 14 is wrong at cell 10), the error against q* is 0.080, and the return from cell 9 is −7.29. The conclusions are unchanged, so the page gives this one sentence, as the commission asked.
3. **Removal test, split by run** (`reseed.py`): for the 18 Q-learning runs with optimal arrows, turning cell 9 left gives exactly −7.097, which is SARSA's value. Runs 12 and 14 (cell 10 wrong) give −7.20 each. That is the 0.01 residual the page attributes to them.
4. **Constant α = 0.1** (`checks.py const`): only 2 of 20 SARSA runs end on the best ε-soft arrows, and the error against q̃ is 0.92. This is why the code keeps `td0`'s decaying N(s,a)^−0.7. It is not on the page.
5. **ε = 0.1** (`checks.py eps01`, `eps01.py`): at 100,000 episodes SARSA has the optimal arrows (which are also the best ε-soft ones) in 16 of 20 runs, but Q-learning has them in only 2 of 20. Its misses are at cells 5 and 10, where q* separates the top two moves by 0.35. By 400,000 episodes all 5 seeds I checked are right, so the cause is slower convergence with less exploration, not a different resting point. Because those wrong arrows would confound it, I did not use ε = 0.1 as the removal test for the gap in earnings. It is not on the page.
6. **Where the explanation fits worst**: every cell except 9 has the same best moves under q̃(0.5) and q*. Both methods' runs agree on those cells, apart from Q-learning's two misses at cell 10 (see 5). At ε ≤ 0.3 the exact gap in earnings is 0 (`exact.py`), as the explanation predicts.
7. **Exact size of the gap** (`exact.py`): at ε = 0.5, averaged over the 14 starts, the ε-greedy policy around π* earns −4.516 and the best ε-soft policy −4.484, a gap of 0.03. At cell 9 the gap is 0.19. The measured average over all starts (`checks.py base`) was −4.48 against −4.55 on seeds 0–19 and −4.50 against −4.54 on seeds 20–39. The page says "a few hundredths".
8. **Truncation**: no episode hit the 200-move cap in seeds 0–19 for either method. In seeds 20–39 SARSA hit it twice.

## Open questions

- The off-policy section cites Sutton and Barto, Section 5.5, p. 103 for "Many off-policy methods reweight … with importance sampling". The record places the start of importance sampling on that page, but it quotes no sentence saying most off-policy methods use it. Please check the wording against p. 103.
- Two facts carry no citation. The Why card's line that DQN keeps Q-learning's target with a network in place of the table sits in a bookend, which is exempt. The uniqueness arguments, that each backup shrinks gaps by γ, are the lesson's own derivations.
- The source title for Sutton and Barto reads "2nd edition, 2018", and the note gives the copyright line (2018, 2020). Lesson 5 called it the "second printing 2020", but the researcher found no such wording in the PDF.
- Voice: I raised no questions.
