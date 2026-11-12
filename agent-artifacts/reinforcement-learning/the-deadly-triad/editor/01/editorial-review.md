# Editorial review: reinforcement-learning/the-deadly-triad (editor/01)

## Correct

Thesis, read from the draft alone: linear semi-gradient TD can diverge when it bootstraps from updates spread over a distribution other than the target policy's. On Baird's counterexample the weights grow, and taking away any one of the three elements keeps them bounded. The claims under it:

1. On the w → 2w fragment, each update multiplies w by 1 + α(2γ − 1), because nothing off-policy undoes it. This held. Sutton and Barto p. 260 has the derivation, and p. 261 has the on-policy "piper must be paid" argument the draft paraphrases. The worked numbers (10 → 10.98 → 12.06 at γ = 0.99, α = 0.1) recompute.
2. Baird's problem diverges under sampled TD and under DP sweeps, and the cause is that the upper states' updates raise H by 12γ for every 10 they raise U. This held. I checked the unit counts (5, 1, 2 per upper update and 1, 2 per state-7 update) and both lines of the 2 × 2 matrix by hand. Its eigenvalues −0.23925 and −0.02218 equal the 8 × 8 matrix's negative pair. The other six are 4/7 (five times) and 0. Problem 2's trace and determinant are right. A γ sweep shows the complex pair crossing zero between 0.882 and 0.8824, which matches 15/17.
3. Removing any one element leaves A with no negative eigenvalue and keeps the weights bounded. This is the claim the brief asked me to test, and two of its three removals did not test it.
   - The on-policy removal put every update on state 7, which is π's distribution. A was (1 − γ)x(7)x(7)ᵀ, and the six upper states never updated, so the mechanism had nothing to act on. That is Sutton and Barto's own removal (p. 262, "convergence is guaranteed"), but as a run it only showed that states nobody updates stay put. The page even reported that U stays wrong at −1.8. I replaced the run with a removal that is not degenerate: the agent evaluates b, the policy it follows. The MDP, features, sampling, start and α stay the same. Every ratio becomes 1, all seven states still update equally often, and each expected target becomes γ times the average of the seven values. Its A has eigenvalues 0 (the null direction of X), 0.01615, 0.32854 and 4/7. Sampled TD never exceeds the starting maximum of 10 on seeds 0 to 10, and the DP values go to 0.069 and 0.067 after 20,000 sweeps. The page now cites the book's state-7 version in one sentence and says why the run uses b instead.
   - The Monte Carlo removal has target 0 because every reward is 0. That does look trivial, but the stability verdict does not depend on it. The reward enters the expected update only through its constant term and never through A, and the Monte Carlo A, (1/7)ΣxxT, is positive semidefinite for any rewards. Its null direction is null(X), which the reward term cannot reach, so the weights cannot drift. I checked this off the page by putting a reward of 1 on every move. With all three elements the weights still grow (5.9e4 by 3,000 sweeps). The Monte Carlo, b-evaluation and tabular versions settle (values 100, about 96 and 100 at long horizons), and the old state-7 weighting leaves the upper values wrong at 38.2. So the narrow part was the explanation, not the experiment. The page now says in the expected-update section that rewards enter only that term, so a problem with every reward 0 tests stability as well as any. I added no reward row, which keeps the lesson to two results.
   - The tabular removal was never degenerate. Its smallest eigenvalue is 0.00143, and the page's account of it holds.

Classification: the off-policy change is a change to the experiment, rerun and printed. The Monte Carlo change narrows the explanation to what the derivation supports. Neither hides thin reporting.

Other breaks and fixes:
- The headline said TD's weights go to infinity. On-policy TD on this problem does not diverge, so I made it "off-policy TD's".
- Fig. 1 was captioned "redrawn from Sutton and Barto", but its dashed exit arrow is the draft's addition from p. 261. The caption now says the behavior policy's moves out were added.
- The draft gave its own gloss as Sutton and Barto's reason for calling the fragment "not completely convincing". The book's reason is that the fragment is only part of an MDP (p. 261), and the sentence now says that.
- "Runs with other seeds grow at the same pace" overstated the spread. On seeds 1 to 30, w8 after 1,000 steps falls between 190 and 506. It now reads "every other seed we tried also diverges".
- "A uniform sweep like DP's counts as off-policy" is false once the agent evaluates b, whose own distribution is uniform. That sentence now says DP's sweep is off-policy here because π's distribution sits on state 7 (p. 261).
- The tabular rate "(1 − γ)/7 = 0.00143" is an eigenvalue of A, not a per-sweep rate. It is now labeled as A's smallest eigenvalue.
- The Fig. 4 caption said the upper TD error is positive above U = γH. That holds only for π's targets, so the caption now says "under π".

Labels: I checked the headline, dek and subheads against pp. 260 to 264. Section 11.2, Figures 11.1 and 11.2, eq. 11.9 and p. 264 for the triad are all correct. Baird's "six-state star problem" checks against his PDF p. 2. Tsitsiklis and Van Roy's Section X, the three-state chain, is on PDF p. 14, which is journal p. 687.

Hrefs, each opened:
- Baird, https://doi.org/10.1016/B978-1-55860-377-6.50013-X: it resolves through Elsevier's linking hub to the ScienceDirect record for PII B978155860377650013X. Crossref and the linking hub both name it "Residual Algorithms: Reinforcement Learning with Function Approximation", Baird, Machine Learning Proceedings 1995, pp. 30-37, so it lands on the right paper. ScienceDirect itself refused this datacenter browser.
- Tsitsiklis and Van Roy, https://doi.org/10.1109/9.580874: it resolves to IEEE Xplore document 580874, and Crossref confirms the title, the journal, 42(5) and pp. 674-690. IEEE answered 202 to the scripted request.
- Go deeper, arXiv 1812.02648 and JMLR v17/14-488: both 200 with the right titles. The GTD PDF over http returns 200.
- Sutton and Barto: every https://incompleteideas.net address fails TLS. The host serves DreamHost's default self-signed certificate, issuer CN=sni.dreamhost.com, which I confirmed with openssl through the tunnel. A reader would get a certificate warning. Over http the PDF loads, and that is the address the book's own page links. I moved the Background and Go-deeper links and every cited-passage URL (data-nb-url) to http. The proof's B-SOURCES-FORM rule requires an https href in the Sources list, so that one href stays https, and its note now gives the working http address. This is an open question for the orchestrator. Should that href move to an https page that serves cleanly? The candidate is MIT Press's book page, https://mitpress.mit.edu/9780262039246/reinforcement-learning/, which returned 403 to every client here, so I could not confirm it lands. I did not make that swap.

data-nb-kind: all three sources are primary, written by the authors of the algorithms, examples and theorem they are cited for. That is correct.

## Reads well

What went:
- "that is enough to send the weights to infinity" (Why this matters). It said off-policy weighting alone is enough, which contradicts the triad stated two sentences later. Rewritten as "losing it sends linear TD's weights to infinity".
- "Gradient-TD and Emphatic-TD were built to keep all three stable". "Keep the elements stable" was the wrong object, so it now says "stay stable with all three present".
- "In Sutton and Barto's fragment": a definite reference to something the reader had not yet met. It now introduces the fragment as part of a larger MDP.
- "baird.py holds the problem and the update." Said nothing that the listing header doesn't. Cut.
- The paragraph "This is the fragment's w → 2w pattern spread over six states…". It went for length. The takeaway carries its point, and Problem 2 carries its threshold.
- The draft's gloss on why the fragment is incomplete. It was attributed to the book and is now cut (see Correct).
- "The cases behind that sentence use linear features". It gave a reading of the book as the book's statement. It now says the lesson reads the sentence for linear features, which the template allows.

Recent record: the headline does not use the method-verb-environment-comparison mold, and the dek does not open on a method name or join two clauses around a figure. Why this matters opens on the convergence condition, not on what a table does. Its reader sentence ("Given a linear problem…, you will be able to…") differs from the "You derive… then… and check" roadmap. "In the field's standard notation" and "slippery grid" are absent. The takeaway ends on the book's two-of-three statement, not on the dek's number. I found no sentence lifted from the voice guide's passages, and none from the commission's wording beyond the required statement of the triad.

What I lifted: the on-policy paragraph had been a bare account of where U stopped. It is now a mechanism. Under b, state 7's own moves count again, so its TD error is about −7.8 instead of −0.12, and it pulls H down. That is the book's "piper must be paid" from p. 261, made concrete on the same U and H that showed the divergence.

## The experience

The rendered page was checked at 390 px and 1280 px in light and dark. Fig. 4 is regenerated, with a blue on-policy (π = b) path that drops almost straight down to U and then follows the diagonal to the origin. No labels collide and nothing scrolls sideways (scrollWidth equals the viewport at both widths). I checked Fig. 3 and Fig. 4 against the printed outputs: 316.75, 335.00, 114.43, (564, 677), 9.018, and 0.069/0.067.

Both listings, extracted from the built HTML and run with `uv run`, match their printed outputs byte for byte. baird.py takes 0.4 s and triad.py about 2 s.

Prose count on the rendered page, by the writer's counter: 2,488 words. That covers the cards, captions, list, problems and body, and excludes code, output, TeX, drawing text, bands and sources. The draft had 2,391. The new removal and its explanation added about 180 words, and I cut about 100 (listed above). The page is still about 290 over the template's 2,200. Everything left is the derivation, the four removal explanations and two problems, and the template says not to thin an explanation. The series band of 2,500 to 6,000 including code is met, with the stamp at 4,093 words. The next whole cut, if the orchestrator wants one, is the Baird history sentence together with source 2. I would keep it.

What the page gives beyond its sources: it reduces Baird's eight weights to two values, U and H, and shows with one 2 × 2 matrix why the weights grow (12γ against 10). It then reads every removal, and the 15/17 threshold, from the same counts, and now tests the on-policy removal with all states updating. The writer's original-work sentence names the same reduction and the same threshold, so the two answers agree. Reread last, the headline's claim is that off-policy TD's weights go to infinity on an all-zero problem. The page shows that, and nothing in it is larger than what the page shows.

## Edits

- headline: "TD's weights" → "off-policy TD's weights"
- Why this matters: "that is enough to send the weights to infinity" → "losing it sends linear TD's weights to infinity"
- Why this matters: Gradient-TD and Emphatic-TD now "stay stable with all three present"
- Background 04, Go deeper 01, and every data-nb-url for source 1: https → http://incompleteideas.net/book/RLbook2020.pdf. The Sources href stays https for B-SOURCES-FORM, with a note added.
- orientation P1: the fragment is introduced as part of a larger MDP
- Fig. 1 caption: says the behavior policy's moves out were added to the redrawing
- orientation P4: the book's reason only ("only part of an MDP"); the gloss is cut
- baird: "holds the problem and the update" cut
- baird: "grow at the same pace" → "every other seed we tried also diverges"
- expected-update: added that rewards enter only the constant term and never A
- expected-update: cut the "fragment's pattern spread over six states" paragraph
- removals P1: the definition of off-policy training now ends at the quote, and a new sentence says why DP's sweep is off-policy here (p. 261)
- removals: the linear-features caveat is recast as the lesson's reading, in one sentence
- removals list: the off-policy removal now evaluates b
- removals: new paragraph on Sutton and Barto's state-7 removal (p. 262) and why the run uses b instead
- removals: the zero eigenvalue is explained once, after the output
- removals: new π = b paragraph replaces the −1.8 paragraph. The removal paragraphs are reordered to match the list (off-policy, Monte Carlo, table).
- removals: the tabular rate is labeled as A's smallest eigenvalue
- Fig. 4: on-policy path regenerated for π = b; label moved; alt text rewritten; caption qualified "under π"
- takeaway: the removals are named as evaluating the policy that generates the updates, the Monte Carlo target, and a table
- baird.py: td_step takes `target` (ratio target/b); expected_matrix takes `target` and uses b's uniform weighting. Printed output unchanged.
- triad.py: the off-policy row evaluates b; the ON_POLICY weighting and the `behavior`/`d` arguments are removed. Output row 3 is now `+0.00000 10 10 +0.06896 +0.06738`.
- Editor copies of the code, build and figure scripts, plus the checks (proto.py, seeds_editor.py, paths_dbg.py), are in editor/01/code and editor/01/scratch.

## Decision

approve. The argument stands, and the removal that did not test it is replaced with one that does. One question for the orchestrator does not block publication: whether to move the Sources href for Sutton and Barto off its failing https host.
