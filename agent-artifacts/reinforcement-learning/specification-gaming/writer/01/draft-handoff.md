# Draft handoff: reinforcement-learning/specification-gaming (writer 01)

## Main idea (30 words)

Value iteration and Q-learning maximize the return of the reward as written, so a reward paid for a repeatable sign of progress can make looping, not finishing, the optimal policy.

## Original work

The published cases (CoastRunners, the bicycle) report scores and no optimum. The lesson builds an eight-cell race, derives in closed form the discount window (0.514 to 0.937) inside which finishing beats a repeatable checkpoint, and confirms that window exactly with value iteration. It then shows Q-learning reaching the same loop, with maximal return and no finishes.

## Proof

`nb stamp` then `nb check …/specification-gaming.html --series reinforcement-learning --repo /home/user/the-nightly-build` (links on): BLOCK 0, WARN 1. No link notes.

- W-CITE-DENSITY on `discount-window`. Left on purpose. The section is a derivation plus the lesson's own runs, which the series direction exempts.

Stamp: words=4358 (code and output included), reading_minutes=19, sources=7. Prose comes to about 2,190 words by my count (cards, captions, legend and problems included; title, dek, code, output, equations, SVG text, reading bands and sources excluded). That is at the template's ceiling, after cutting a Lego paragraph and a pure-application problem.

## Code and runs

The code lives in the article workspace at `/home/user/the-nightly-build/.nb-work/reinforcement-learning/specification-gaming/code/`. The page prints `race.py`, `window.py` and `learn.py` in full. `*.out.txt` holds each listing's output. `figs.py` (off the page) draws both inline SVGs from `race.py` and `window.py`, and `figs.html` is its output.

- **Listings as printed.** I extracted the three listings and their printed outputs from the article HTML into a fresh folder and ran `uv run race.py`, `uv run window.py` and `uv run learn.py`. All three outputs match the page byte for byte. Times: under 1 s, about 1 s, about 4–5 s.
- **Seeds and cells.** Run `cd code && uv run checks/check_runs.py`; its output is in `checks/check_runs.out.txt`. The page uses seeds 0–4. Seeds 5–14 give the same conclusions in all three rows: same moves as q* in every state in 10 of 10 runs, the same finish counts, 7 or 100 moves, and scores of 11 or 50. Every state is graded on the page, so no conclusion rests on one cell.
- **Removal test (on the page).** `learn.py`'s third row, `Race(once=True)`, pays the checkpoint on the first crossing only. At γ = 0.99, value iteration and all 5 Q-learning runs then finish in 7 moves with a score of 11.
- **Worst-fit cases** (`check_runs.py`):
  - γ = 0.93 is inside the window with a gap of 0.08 at cell 2; all runs finish.
  - γ = 0.95 is just above it; all runs loop.
  - γ = 0.5 is below it, where the cause is myopia and not a large γ; value iteration and all runs loop, as the formula predicts.
  - Time limits of 10, 20 and 1000 at γ = 0.99 give the same moves, which supports "neither value contains the time limit".
- **Step size.** With the course's decaying step N(s,a)^−0.7, γ = 0.99 had not settled after 2000 episodes: mean |Q − q*| was 21 for the repeat row and 1.0 for the once row, and the once row had wrong moves in its unpaid states past the checkpoint. That is why `learn.py` uses a constant 0.1. The page justifies this from determinism and lets the printed |Q − q*| column show that the estimates settle.
- **Environment checker.** check_env passes `Race()` and `Race(once=True)` with only the render-modes warning. This is not on the page.
- **Problem answers.** Run `cd code && uv run checks/check_problems.py`; its output is in `checks/check_problems.out.txt`.
  - The per-move-payment answer: finishing switches between γ 0.974 and 0.976, with no lower end down to γ = 0.1.
  - The finite-horizon answer: backward induction at H = 100 finishes on move 99 after 47 crossings, lapping when 7 or more moves remain.
  - The cut problem's bound (F > 51.8 at 0.99, F > 7.22 at 0.9) was also checked by value iteration, in case it is reinstated.

The visuals were checked through `nb preview` and Playwright (`/opt/node-tools` playwright, browsers in `/opt/pw-browsers`) at 390 and 1280 px, light and dark. There is no horizontal overflow and no KaTeX errors. Earlier label collisions in both figures are fixed.

## Evidence handling, and open questions

- **OpenAI post (S1).** It was never read at openai.com. The page describes it in its own words, cites it at its own URL with a `data-nb-note`, gives "2016" as the date, and gives the byline as "Amodei and Clark", the surnames only, as DeepMind cites them. The "three targets" detail comes from the AIID reproduction. If the orchestrator can open the live page, the 2016 date and the byline order are the two things to confirm.
- **Contradiction 4.** DeepMind's "changed the optimal policy" is set against OpenAI's scores-only claim in the CoastRunners paragraph.
- **Contradiction 6.** DeepMind's weaker-algorithm point is answered by checking every run against the exact solve.
- **Contradiction 7.** Turner gets one sentence, and his convergence conditions are said to hold on the race. The takeaway says "value iteration and Q-learning maximize", not "an agent maximizes".
- **Bicycle (contradictions 1 and 2).** It is described from Randløv and Alstrøm: around the start, with physical stability as a second cause. The list's description is not used.
- **Lego.** Only the not-stacking failure is used, in Problem 1, not the flip.
- **Contradictions 8 and 9.** Sutton and Barto's qualification in Section 17.4 is not material to the case and appears as a Go deeper row only. The spectrum point is left off the page.
- **Randløv and Alstrøm source link.** It points to the gwern.net copy the researcher read. The note gives the ICML pages and the mlanthology record. Ng et al.'s title is given as the evidence records it.
- **Inline math.** It uses `span.nb-math-in`, which nb.js typesets, as earlier lessons do. The furniture catalog documents only block `nb-math`, so the editor may want to confirm this markup is allowed.
