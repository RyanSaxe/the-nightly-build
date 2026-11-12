# Draft handoff: reinforcement-learning/the-deadly-triad (writer 01)

## Main idea (lesson identity, 27 words)

Semi-gradient TD with linear features can diverge when it bootstraps from off-policy updates; on Baird's counterexample, removing any one of the three keeps the weights bounded.

## Original work

The lesson reduces Baird's eight-weight expected update to a 2 × 2 map on two values, U for the upper states and H for state 7. That map shows why all three elements together diverge: the six upper updates raise their shared target H by 12 units for every 10 they raise U. The same map gives each removal's path in Fig. 4 and the discount threshold 15/17, and the lesson's own runs check all of it.

## Proof

`nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build` (links checked): BLOCK 0, WARN 3, verdict PUBLISHABLE.

Warnings left on purpose: all three are W-SENTENCE-DENSITY, and each one is a display TeX equation that the proof reads as a sentence. They are the TD update (eq. 11.1 to 11.3), the ratio expectation, and the U/H matrix. Each is already split into aligned lines so that it fits a 390 px phone. The prose around them has no flagged sentence.

## Length

Prose is about 2,390 words by my count: rendered body, captions, cards and problems, without code, output, TeX, drawing text, bands or sources. That is over the template's 2,200 line. I cut these whole ideas:

- which element to give up (pp. 264-265)
- the Gradient-TD and Emphatic-TD paragraph (both are now in Why and Go deeper only)
- the stage-4 DQN and van Hasselt sentence (now in Go deeper only)
- w7 turning negative later, matching Baird's hub weight going to minus infinity (checked below)
- the "favorable case" aside
- a separate section on the linear-features caveat (folded into one sentence after the quote)
- a w7 + w8 feature-variant problem

What remains is the derivation and the explanation of each removal. The editor may want one more cut. The next candidate is Problem 1 (on-policy w → 2w through the semi-gradient lesson's A), but that would leave one problem.

## Checks off the page (scripts in writer/01/scratch, run from writer/01/code)

- `uv run --with numpy python ../scratch/seeds.py`: TD diverges on seeds 1-30. After 1,000 steps, w8 is between 190 and 506 and every upper weight is above 47. All three removals stay at their starting maximum (10, 10, 12) on seeds 1-10, while the full triad passes 1e21.
- `uv run --with numpy python ../scratch/gamma.py`: the 2 × 2 eigenvalues equal the 8 × 8 matrix's negative ones at every γ tested. The threshold is 15/17. At 0.86 and 0.88 the smallest eigenvalue is positive, and at 0.885 it is negative. At 0.86 the upper updates already widen the gap (12γ > 10) but the system is stable. That is the worst case for the "12 against 10" explanation, so the prose and Problem 2 credit state 7's update for keeping up.
- `uv run --with numpy python ../scratch/eig.py`: the growth direction has a small negative w7 component. w7 is 6.85 at 1,000 sweeps, -36.25 at 2,000, and about -2.3e20 at 20,000, which agrees with Baird's PDF p. 3. This was cut from the page.
- `scratch/p1/baird.py` (state 7 = w7 + w8): no negative eigenvalue (0, 0.00494, 0.578). The cut problem used this.
- The DP row reproduces the researcher's 114.43 / 6.85 / 335.00.
- The listings, extracted from the built HTML into `scratch/verify/`, rerun with `uv run` and match the printed outputs byte for byte.

## Choices the editor should see

- The Monte Carlo removal uses the target ρG_t = 0. The task is continuing, so any Monte Carlo return has to be cut off, and with every reward 0 the return is 0 at any cutoff. The page says this. The expected matrix is (1/7)XᵀX. It has an eigenvalue of 0 for the null direction of X, so the page says the weights stop "away from 0" and are bounded, not converging to 0.
- The on-policy removal is degenerate as the researcher flagged: π updates only state 7. The page says the upper values stay wrong at U = -1.8.
- The task is treated as continuing, and the page says so (the commission decision).
- Baird's source href is the proceedings DOI (https) because leemon.com does not serve https. The locators and data-nb-url point at the author's July 1995 PDF, which is the copy the researcher read. The DOI landing page itself was not opened. The link check passed.
- The headline is not built as `<method> <verb> <environment> <comparison>`. The dek is one clause with no comma-and join.

## Open questions

None for evidence. The 2 × 2 reduction, the 15/17 threshold and all the removal eigenvalues are derivations and runs printed on the page, not cited claims.
