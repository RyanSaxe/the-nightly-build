# Editorial review: reinforcement-learning/off-policy-importance-sampling (editor/01)

## Correct

Thesis, from the page alone: to value a target policy from episodes another policy played, multiply
each return by the product of π(a|s)/b(a|s) along its episode; under coverage the plain average of
these scaled returns is unbiased, and the ratio-weighted average is biased but bounded by the
returns. Three claims carry it.

1. The environment's probabilities cancel, so the ratio needs only the two policies and the aimed
   moves. Held. Equation 5.3 and the cancellation are on p. 104 of the authors' PDF (page=126), and
   Fig. 1's factors (1/0.625 = 1.6, 1.6³ = 4.10, 0 for episode B) match the printed episodes.
2. Under coverage, E_b[ρG | S₀ = s] = v_π(s), so first-visit ordinary IS is unbiased, and weighted IS
   is biased with a bias that fades. Held. The three-line derivation is correct, and coverage is
   stated on p. 103. The book gives (5.4) on p. 104 with no derivation, so "state this ... without
   deriving it" is accurate. The every-visit caveat is on p. 105. Table 1 and both outputs reproduce
   byte for byte. I reran `grid_seed3.py`: ordinary means 1.43, 1.43, 1.38 (standard errors near
   0.07), with weighted starting high. The handoff records the other seeds. `uncover_limit.py` gives
   0.65 for the arrows' probability of never acting in cell 7, which is the average ratio the
   coverage-removal sentence names.
3. On Example 5.5 the ordinary estimate's variance is infinite for every β ≤ 0.9 and equals 1 at
   β = 0.95; it still converges with probability 1. Held. The sum 0.1/β · Σ(0.9/β)ᵏ, its value
   0.1/(β − 0.9) above 0.9, and the β = 0.5 case (0.2 Σ 1.8ᵏ, p. 108) all check. I read Fig. 3's
   path coordinates at 10² to 10⁶ episodes, and all twenty curves agree with the printed tables to
   within 0.002. The loop's seed check (`loop_seed10.py`) reproduces the handoff's numbers, so the
   page is right not to claim that every run ends below 1.

One break. The page answered the Fig. 5.4 caption ("do not converge to this value") by saying it
"describes runs that had not converged after millions of episodes". That sentence put a reading in
the authors' mouths and stopped short of the conclusion the page had just shown. The book's own text
below the figure (p. 107) says the runs "fail to converge" even after millions of episodes. The
record (contradiction 1, and Precup, Sutton and Dasgupta's p. 7) supports calling the caption wrong
as a statement about the limit. I quoted the text and stated that verdict. This sharpens the claim
the page already made. It narrows nothing.

Labels: the headline, dek and four headings match the body and the printed output. The dek's "over
90%" follows from 0.9/β ≥ 1 for β ≤ 0.9. Every number on the page appears in printed output or
rounds a printed number. Timings hold (about 29 and 34 seconds for `grid_runs.py`, under 2.5 seconds
for `loop.py`).

Citations: every `data-nb-url` resolves to the authors' PDF and lands on the cited passage (PDF
pages 125, 126, 127, 128, 129, 130 and 171, each checked against its locator). The Go-deeper rows
were checked against PSS-00 p. 3 (Theorem 1, per-decision IS) and PSD-01 p. 7 (Theorem 7 and the
law-of-large-numbers remark). In-course anchors `#baselines`, `#off-policy`, `#monte-carlo` and
`#target-averages` exist in the published lessons, and every background title matches its
headline. Source 1's printed `href`, the MIT Press book page, returned an Akamai "Access Denied" 403
to this session, so I could not confirm that it lands. It is the URL the earlier lessons use for the
book, and the proof treats it as restricted rather than dead. Orchestrator: please confirm it opens
in a browser. If it doesn't, the authors' book page is http only and would fail B-SOURCES-FORM.

Kind: source 1 is the authors' own text for every definition, equation and example the page cites,
so `primary` is correct.

Warnings. The three W-SENTENCE-DENSITY warnings stand without action. Running the engine's own
sentence splitter shows that each one is the TeX source of a display equation (the ratio, the
unbiasedness derivation, the loop's mean square) and that no prose sentence trips it.
W-CITE-DENSITY on `grid-logs` stands as well. That section holds the lesson's own code, output and
Table 1, which the series prompt exempts, and the only outside claim in it links the termination
lesson.

## Reads well

Nothing was cut for saying nothing. The edges were clean: each paragraph opens on its point and
ends on a checkable statement, and the takeaway ends on its conclusion, not a figure. No sentence
borrows from the commission or from the voice guide's quoted passages. "Biased but bounded" comes
from the main-idea sentence and is the page's own claim.

One phrase came from the recent record. "By the end you can ..." in Why this matters repeats "By the
end you will" from two earlier openers and the course's "You will ..." habit. I rewrote that third
part around what this lesson lets the reader do: work out an episode's ratio from the two policies'
move probabilities, prove the plain average unbiased, and find the behaviors that give it infinite
variance on a loop. The old "tell from one number per step" also promised a general test that the
body only shows on the loop.

Lifted: the 38-word opening body sentence is now two sentences. The coverage-removal sentence had a
stacked appositive ("where the behavior never aims up, the arrow's move into the goal") and is now
split. The grid result closed on a tacked-on clause ("and it starts biased"), and it now ends on the
plain finding: on these logs the weighted estimate is biased and no more accurate. In the dek,
"variance stays infinite" became "is infinite". At phone width, line breaks were splitting
"π(a|s) > 0", "ρᵢ/Σⱼ ρⱼ" and "4.10 × −18.10 = −74.14" across lines, so those now carry non-breaking
spaces and word joiners.

The draft was nowhere thinner than the guide's register. Its sentences are short, each step says
what it is for, and the problems section works a case the body didn't (shifted returns).

I left the headline alone. It states the lesson's capability as a sentence claim. Unlike the recent
headlines, it isn't built on "the optimal arrows" or on a contrast, and the dek carries the
surprise.

## The experience

I looked at the rendered page (`nb preview`, Playwright) at 390 and 1280 px in light and dark. No
page-level horizontal scroll at either width. Fig. 1's labels clear their arrows in both themes,
and episode B's dashed aim runs a few units past the grid edge, which reads as an aim into the wall.
Fig. 2 matches the book's inset. Fig. 3's panels stack on a phone, and its axes, "true value 1"
label and cut-off note are legible in both themes. Table 1 fits a phone without scrolling. Every
visual plots something the prose relies on, and none is missing: the grid result is a 3 × 4
comparison that a table shows faster than a chart.

The page's weight sits in the right place. The worked episodes lead into the general ratio, then
the derivation, the run that checks it, and the loop where the method breaks. The densest stretch is
the four short paragraphs after the derivation (coverage, the two estimators, their bounds and
first-visit). Each one is used later, so none was cut.

Word count on the rendered page, counting prose only (cards, headings, captions, table cells,
problems): 2,245 with the headline and dek, or about 2,195 without them. That is at the template's
cut line. My edits added a net 22 words, almost all in the corrected caption passage.

What the piece gives beyond its sources: it proves the identity the textbook only states, measures
both estimators against exact values on the course grid with and without coverage, turns Example
5.5's one divergent sum into a threshold in β with runs on both sides of it, and shows from the
strong law that the book's "do not converge" caption is wrong as a limit statement. The writer's
original-work sentence covers the first three of these, and both statements survive.

## Edits

- Dek (visible and `nb-meta`): "its variance stays infinite" → "its variance is infinite".
- Why this matters: replaced "By the end you can compute ... tell from one number per step when its variance is infinite" with a lesson-specific sentence about working out the ratio, proving unbiasedness and finding the infinite-variance behaviors on a loop.
- Orientation, first paragraph: split the opening sentence into two; links kept.
- Orientation, last paragraph: "which the course's episodes record in every step" → "which every logged step records".
- Scaled returns: non-breaking spaces in "b(a|s) > 0 wherever π(a|s) > 0".
- Scaled returns: word joiners and a non-breaking space in "ρᵢ/Σⱼ ρⱼ"; non-breaking spaces in "4.10 × −18.10 = −74.14".
- Grid logs: last sentence of the Table 1 paragraph rewritten as two sentences ("On these logs the weighted estimate is biased and no more accurate.").
- Grid logs: coverage-removal sentence split ("The arrow there aims up into the goal, and the behavior in this run never aims up.").
- Loop: replaced "which describes runs that had not converged after millions of episodes" with the book's own "fail to converge" passage (new citation, Section 5.5, Example 5.5, text below Figure 5.4, p. 107, page=129) and the sentence "As a statement about the limit, the caption is wrong."
- Ran `nb stamp` (words 4,407, 19 minutes, 1 source).
- No code changed. All listings were rerun exactly as printed in a clean folder with the four imported files taken from the published lessons, and every output matched byte for byte.

## Decision

approve. The argument is correct and supported, and the changes it needed were a fair statement of
the caption disagreement, one repeated opener and some sentence-level fixes, all made here. The
proof is BLOCK 0, with four warnings that stand for the reasons above.
