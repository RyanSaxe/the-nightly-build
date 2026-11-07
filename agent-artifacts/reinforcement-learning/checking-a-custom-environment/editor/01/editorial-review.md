# Editorial review: reinforcement-learning/checking-a-custom-environment (editor/01)

## Correct

Thesis, from the draft alone: Gymnasium's `check_env` checks only the form of what `reset` and `step` return, so it passes copies of SlipperyGrid with wrong rules. A wrong rule shows when a baseline policy's average return misses the value solved from the rules, and each baseline is blind to some errors. The claims under it:

1. `check_env` compares a step only with a second seeded run of the same environment, and in `step` several faults only warn. This held. I read `check_env` (L406–508), `check_step_determinism` (L204–270), `check_returned_data_not_reused` (L273–307), `check_obs` (L131–176), `env_step_passive_checker` (L293–350) and `PassiveEnvChecker.step`/`reset` (common.py L287–326) in the 1.4.0 wheel. Every locator on the page matches. The 1.4.0 docs page carries the docstring's "with a variety of values" and its advice to call the checker after constructing an environment. checker.py, rerun, prints the same verdicts and the same count: 12 resets and 5 steps, from cells 0 and 8.
2. Random moves cannot see SlipBack, and the hand-drawn policy can. The derivation is right, but the heading and takeaway said "any slip rule". The sum assumes that every aim has the same p(k). Handoff check 4 shows what happens otherwise: when only aiming left slips back, the random value moves to −10.744. I narrowed the claim to what the derivation supports and stated the assumption in the prose and the legend. That is a narrowing of an overclaim. The reporting is not thin: the record and the runs cover the narrowed claim fully. My own exact solves reproduce every handoff value: −10.904 for random under all seven aim-independent changes, max |ΔP| = 0; hand-drawn 1.360, 2.284, 3.698, 1.145, 5.479, 5.900, −7.431; up_or_right −4.178 and −5.352; the blind-spot cases 1.360/−11.610 and 1.360/−11.005.
3. The removal test, `up_or_right`, is flagged on SlipBack. It held at seed 0 (z −6.5) and across seeds 1–9 (−5.6 to −9.2).
4. Play by hand shows SlipBack on its first backward slip, and the ranges catch NeverEnds. Both held. The play runs and the range table are byte-identical on rerun.

Each figure was checked against its denominator. The Fig. 3 offsets and ±3 SE bars recompute from the printed means and sds over √4000. The −T − 19 bound, −219 at T = 200, is right. The NeverEnds value iteration (problem 2) gives a goal cell where up and right tie at 85.04. That is consistent with the answer's "aiming up ... arrives in the goal again".

Breaks I fixed:
- "most faults only warn" overstated the passive checker. A non-tuple, a wrong length and a non-dict info all assert or raise. The commission asked for precise wording, so it now reads "several".
- "a reward that is not a number" read as NaN. A NaN reward warns in the passive check and then fails `check_step_determinism` (record, source 10). The phrase is now "a reward of a non-numeric type".
- Three phrases did not match the printed output. NeverEnds did not pass "silently", because it prints the render-mode warning. ArrayCell has two more warnings, not two. "Every copy" gets the render warning except NoSeed, which fails first.
- "on each copy with a rule error" left out the SlipperyGrid rows the run prints.
- "Each baseline is blind to the moves it never makes" was false for random moves, which make every move. It now names the hand-drawn policy.
- "only random moves ... can find it" ignored play by hand. It now says "of the two baselines".
- The problem 2 answer said nothing in training would show the task is wrong. The lesson's own checks would. It now says only a check against the rules shows it, for example returns past +10.

Headline, dek and subheads hold against the run and the source. "passes a grid with a backward slip" matches the checker.py output. The −10.90 in the dek is the exact value both rules give.

Links. Every external href was opened as printed. github.com refuses curl from here, so I opened those six through WebFetch: each lands on the file at its tag. The five Gymnasium files show 508, 457, 502, 582 and 662 lines, and preprocessing.py at v2.9.2 shows the one-hot line. The two Gymnasium docs anchors, both SB3 docs anchors and the PyPI page resolve, and every internal anchor exists in the published lessons. The Schulman link, per the commission's last decision, did not resolve. joschu.net resolves to an Amazon S3 website endpoint (`server: AmazonS3` over http), and those endpoints serve no https. `https://joschu.net/docs/nuts-and-bolts.pdf` resets through curl and returns 503 through WebFetch and through Chromium. web.archive.org is refused from this session, so I could not open an archived copy. UC Berkeley's CS 294 Deep RL, Spring 2017 site (Schulman is listed as an instructor) serves the file over https at `https://rll.berkeley.edu/deeprlcoursesp17/docs/nuts-and-bolts.pdf`. It is byte-identical to the http original: MD5 5d9a7116c2daefd8c3d9aeb16ff35f32, the same as joschu.net's S3 ETag. I substituted it in source 5 and in Go deeper (with `#page=6`) and rewrote the note to say so. I reread slides 5, 6, 7, 16 and 18 from that copy. Slide 6 lists the random policy, human control and the scale of observations and rewards, as the body says.

`data-nb-kind`: all ten are primary, and each is the owner's own document: Farama's source and docs, DLR-RM's source and docs, the maintainers' PyPI record, and Schulman's slides. No sentence claims an independent second source.

Code: the four course files are byte-identical to the published listings. All five listings on the page are identical to code/. From a fresh folder holding only those nine files, `uv run` of bugs.py and baselines.py exits cleanly, and checker.py, behaviour.py and both piped play.py runs print output identical to the page. Seeds 1–9 of behaviour.py reproduce handoff check 1 exactly: the correct copy is never flagged (max |z| 2.1), SlipBack random is never flagged (max |z| 2.4), SlipBack hand-drawn is flagged at 6.2–9.2, and NeverEnds is flagged at |z| ≥ 19.8. I changed no code.

## Reads well

What went:
- The Why card's first sentence, "An agent learns whatever rules its environment plays". It said nothing, and the next sentence says the same thing with the course's nouns.
- "The checker's source shows what a pass does mean". It was a signpost. The sentence before it already raises the question the next section answers.
- "needed hundreds of episodes". The page printed no figure for it, so it now gives the page's own figure, 4,000.
- "Each baseline is blind to the moves it never makes". It was built to be quoted and was wrong for one of the two baselines.

Nothing was lifted from the briefing. The commission's "tests the contract, not the task" and "the checks are complementary" do not appear in the article's wording. The voice guide's Olah move, telling the reader which line to read, appears once ("the second line is the one to read") in the article's own words. Against the recent record, the headline is a claim about the checker, not "X learns Y". The dek is a consequence sentence, not two clauses joined by "and". One heading cites a cell. The Why card's last sentence avoids the "you can write/derive/prove" ending of the last three. None of the listed house phrases occur. The shape (bug diagram, checker output, baseline table, a derivation with a removal test, play by hand, ranges) shares nothing with the last three lessons' heatmap triptych and error-vs-parameter chart.

Lifted: the derivation paragraph now states the one assumption the sum makes, and the takeaway carries the narrowed claim. The ranges heading is now a step of the argument ("The rules bound every number an agent will receive") where it had named a topic. The takeaway is cut from 124 to about 105 words, losing the restatement of what `step` warns about, which the body states precisely. The prose sits at the voice guide's register: short steps, the purpose before the step, one example carried through. I added no personal remark, because the guide allows one and does not ask for one.

## The experience

I read the rendered page at 390 px and 1,280 px in both themes. There is no horizontal scroll at either width. Figs. 1, 2 and 4 and the equation render cleanly, with no overlapping labels or arrows that stop short. In Fig. 1, the 0.1 label on the arrow into the pit sits inside the pit cell, which is legible in both themes.

The page gained colour consistency. Fig. 2 marks the hand-drawn row in orange and SlipBack's changes in blue, while Fig. 3 drew random in orange and hand-drawn in blue. Fig. 3 now draws random in grey and hand-drawn in orange, so blue means only "SlipBack's change" in the two figures that teach the bug. The equation legend's last entry no longer wraps a lone comma onto its own line at phone width.

Prose on the rendered page is about 2,200 words (2,205 by my extraction, counting the headline, dek, captions, legend, problems and the two cards, and excluding code, output, display and inline math, SVG text, the bands and the sources). Stamped words are 4,424. There are two experimental results, the checker verdicts and the baseline-against-exact table. `up_or_right` is the removal test on the page. Play by hand and the ranges table are the commissioned checks shown working, and they introduce no new causal claim.

What it gives beyond its sources: Gymnasium's and SB3's documentation tell you to run `check_env` and random actions. This page proves, and confirms with a run and a removal test, that random actions cannot see any slip rule that treats every aim alike or any relabelling of the aims. It also turns the course's exact solutions into a test that catches a one-character bug a passing checker and a passing random baseline both miss. That matches the handoff's original-work sentence. The headline, reread last, is narrower than the piece but true, and the dek carries the larger finding.

## Edits

- Why this matters: cut the opening sentence.
- Orientation: cut the closing signpost sentence.
- checker: "most faults only warn" → "several faults only warn".
- checker: "a reward that is not a number" → "a reward of a non-numeric type".
- checker: NeverEnds "passes silently" → "passes as SlipperyGrid does".
- checker: ArrayCell "passes with two warnings" → "two more warnings".
- checker: "The warning every copy gets" → "every passing copy".
- baselines: "on each copy with a rule error" → "on SlipperyGrid and on each copy with a rule error".
- baselines: "more episodes would not change the random row" → "would not flag the random row".
- uniform-aims heading: "average any slip rule away" → "average the slip rule away".
- uniform-aims: rewrote the p(k) sentence to state that both tables give every aim the same p(k), which is all the argument assumes.
- equation legend: p(k) entry adds "the same for every aim"; m(d) entry "otherwise 0" → "and 0 otherwise".
- uniform-aims: moved "(Fig. 3)" onto the up_or_right result it shows.
- uniform-aims: "The table also shows" → "Fig. 2 also shows".
- uniform-aims: "only random moves ... can find it" → "of the two baselines only random moves ...".
- by-hand: "seed 33, which shows the slip early" → "seed 33, chosen because it shows the slip early".
- by-hand: "needed hundreds of episodes" → "averaged 4,000 episodes".
- ranges heading: "The numbers an off-the-shelf agent will receive" → "The rules bound every number an agent will receive".
- ranges: "where check_env looked at five" → "five moves".
- Problem 2 answer: the last sentence is now two, ending on returns past +10, the most an episode on the real grid can pay.
- Takeaway: trimmed to about 105 words; narrowed "every slip rule" to "any slip rule that treats every aim alike"; the blind-spot sentence now names the hand-drawn policy.
- Source 5 and Go deeper 01: href → https://rll.berkeley.edu/deeprlcoursesp17/docs/nuts-and-bolts.pdf (Go deeper keeps #page=6); note rewritten.
- Fig. 3: random drawn in ink-soft, hand-drawn in chart-1, to match Fig. 2.
- `nb stamp`: words 4424, reading 19 min, sources 10.

Proof after the edits: `nb check ... --series reinforcement-learning --repo /home/user/the-nightly-build`, with links checked, gives BLOCK: 0, WARN: 3, PUBLISHABLE. W-SENTENCE-DENSITY is the TeX source of the display equation (confirmed with the engine's `sentence_density`). The two W-CITE-DENSITY warnings are on the derivation and run sections, which the series direction exempts.

## Questions for the orchestrator

None blocking. For the record: the commission suggested an archived copy for Schulman's slides, but web.archive.org is refused from this session, so I could not open one. I used the Berkeley course copy instead, which I opened and byte-compared with the author's file. If you would rather print the Wayback address (archive.org's API lists a 200 capture of the http original at 20260910095449), that is a one-href change in two places.

## Decision

approve. The argument is right and now claimed no wider than its derivation, every listing and figure reproduces, and no change remains for the writer.
