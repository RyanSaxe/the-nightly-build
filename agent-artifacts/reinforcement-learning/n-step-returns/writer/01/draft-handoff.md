# Draft handoff: reinforcement-learning/n-step-returns (writer 01)

## Main idea (30 words)

An n-step target adds n rewards to the estimate n moves later; n = 1 is TD(0), n beyond the
episode is Monte Carlo, and middle n can learn fastest.

## Original work

The lesson reproduces Figure 7.2's finding with its own code and supplies the mechanism Sutton and
Barto leave out: short targets carry the outcome back slowly, and long targets' noise forces a
small step. It tests that mechanism by removing target noise, which makes the longest target best.

## Proof

`nb check … --series reinforcement-learning --repo /home/user/the-nightly-build`, links included:
BLOCK 0, WARN 3. All three left on purpose.

- W-SENTENCE-DENSITY: the "sentence" is the TeX source of the aligned derivation in
  `first-n-td-errors`. No prose sentence is flagged.
- W-CITE-DENSITY on `first-n-td-errors` (a derivation) and on `information-and-noise` (the lesson's
  own runs, removal test and problems). The series prompt exempts both.

Prose by my count (cards, headings, captions, legend text, details summary, problems; no
equations, code, output, drawing text, bands or sources): about 2,170 words, counting "n = 4" as
three words. I cut a third problem, the n-step SARSA pointer sentence and the Exercise 7.1 citation
to get under 2,200.

## Code and checks

The listings print `nstep.py` and `sweep.py` from
`/tmp/claude-0/-home-user-the-nightly-build/f459be86-7567-53db-a107-d49609878cc2/scratchpad/rl-writer/code/`.
Their outputs are in `code/out/`. I extracted both listings from the built article into a fresh
folder and ran all five printed commands. Every output matched the page byte for byte. Checks run
from `code/` with `uv run --with numpy python checks/<file>`:

1. `pseudocode.py`: `nstep_td` against a literal transcription of the p. 144 box, for n in
   {1, 2, 3, 4, 7, 16, 64, 512}, three step sizes and 20 seeds. Largest difference 0.0. With n = inf
   it equals every-visit constant-step Monte Carlo exactly.
2. `seeds.py OFFSET [args]`: unused seeds (offsets 1000, 2000, 3000). n = 4 is lowest every time
   (0.257 to 0.263). n = 2 and n = 8 stay within 0.005 of each other. The page does not rank them.
   `--expected`, `--size 5` and `--episodes 100 --first 91` keep their conclusions at offset 1000.
   Under `--expected`, n = 256 and n = ∞ tie at three decimals there, so the page says "falls as n
   grows" and not "with every increase".
3. `integer_n.py`: n = 3, 4 and 5 tie (0.256 to 0.263 on two seed sets, finer α grid). The page
   says n = 3 and n = 5 do as well, so "four" in the headline is the tested power of two and not a
   unique optimum.
4. `by_state.py`: the worst case for the explanation is state 10, where TD(0) has the lowest error
   of any n (0.04 against 0.28 for n = 4). The true value there is the starting 0, so nothing has to
   travel, and the page says so in one clause. Near the ends TD(0) and n = 4 are about equal.
5. `zero_share.py`: only 1% to 5% of runs leave a TD(0) estimate exactly at 0 after 10 episodes. An
   early draft said the outcome "had not reached" those states in many runs. I replaced it with the
   share of the true value the mean has reached (half at state 6, a fifth at state 8, from the
   printed means).
6. `start_exact.py` (problem 2): with estimates starting at the true values, TD(0) has the lowest
   error at every step size and each n does best at the smallest step size.
7. Problem 1: `nstep_td` on that episode gives V(18) = 0.75 and V(19) = 0.85.

Figures are inline SVG drawn by `code/figures/make_figs.py` from `code/out/sweep.txt`, so Figs. 2 and
3 match the printed table. Fig. 1 matches the hand episode and the first three lines of
`nstep.py`'s output. I looked at all three figures and the four display equations at 390 px and
1280 px, in light and dark, using `nb preview` and Playwright. I split the equations onto two lines
because they overflowed at phone width.

## Decisions to know about

- The setup is Sutton's online.lisp, except that it uses Python's `random.Random(seed)` per run and
  every other point of his 51-point log α grid (26 values, 0.0067 to 1). The largest n is ∞ (true
  Monte Carlo) in place of 512. It matches 512 to the third decimal.
- The derivation is the recursive form, giving the n-step error as the first n TD errors. It ties
  the main idea to the earlier lesson's sum-of-TD-errors result. Eq. 7.3 appears only in the Watkins
  Go-deeper row, stated as a bound and not as an explanation.
- `nb-meta`: order 11 (the proof accepted it), harness "Claude Code", model "claude-opus-5-5".

## Open questions

- online.lisp href. The proof requires https, but https://incompleteideas.net serves a self-signed
  certificate from here, so curl fails TLS on it. The source href is the https URL, with a
  `data-nb-note` saying the http address serves the same file. The inline citation's `data-nb-url`
  is the working http URL. I assumed readers can get past a certificate warning. The alternative is
  to drop source 3 and present the centre start and α grid as the lesson's own choices.
- Scope flags. `--size 5` and `--episodes 100 --first 91` support the commission's required
  sentence that the best n depends on α, the chain and training length. I treated them as checks
  of the result 2 explanation (cases where little information is left to travel), not as a third
  result. If the editor counts them as results, the fallback is to keep the sentence and cite the
  flags in this file only.
