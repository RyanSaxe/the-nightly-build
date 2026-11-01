# Editorial review: reinforcement-learning/finding-optimal-policies (editor 01)

## Verdict: SETTLED

Every change this piece needed was a direct cut, and I made them. No writer
round is owed. The article is left ready for the orchestrator to stamp and
prove. The only remaining proof warnings are non-blocking and expected:
`W-SELF-COUNT` (the stamp writes sources/words) and `W-LENGTH-HIGH`
(3974 words; see the length note below), plus four `W-SENTENCE-DENSITY` on the
derivations and the one aligned proof equation, which the template forbids
fragmenting. `nb check` returns BLOCK 0, verdict PUBLISHABLE.

## Direct cuts I made

1. **Decorative/mismatched citation removed (policy-iteration section).** The
   sentences "Howard developed the routine in 1960, after a roughly fifty-state
   catalogue-mailing problem for Sears. He had solved that one by a different
   method, and found its best policy was not the one that chased the largest
   immediate return." carried a citation to `s2` **ch. 7, pp. 83-84** (Howard
   1960). Those pages are the discounted policy-improvement routine; the Sears
   catalogue-mailing account is in Howard *2002* (Operations Research), p. 101,
   which the researcher read but which is **not** in the Sources list. The claim
   was therefore attributed to pages that do not contain it. I cut the two
   sentences rather than add a sixth source and open a writer round. Nothing
   load-bearing was lost: Howard's 1960 origin of the loop is still stated and
   correctly cited in the improvement section ("Howard, who first wrote down
   this loop in 1960, proved the same fact...", `s2` ch. 7 p. 87), and the
   section keeps its `s1`/`s2`/`s3` citations.

2. **Decorative citation removed (code subsection).** "...`uv run control.py`
   installs numpy from the inline metadata and finishes in about a second."
   carried a cite to `s1` **Section 4.1, p. 75** (S&B, Policy Evaluation). The
   sentence is the writer's own run detail and S&B says nothing about it; the
   cite matched no claim. Removed the `<sup>`; the sentence stands uncited, which
   is correct, and the value-iteration section it sits in is amply cited.

3. **Slop closer cut (pricing-moves section).** Deleted the paragraph's last
   sentence, "That is why a single pass is not the end of the story." It is a
   built-to-be-quoted closer leaning on a decorative "story" metaphor, and it
   reduces to a generic pattern under the slop test. The paragraph now ends on
   the concrete line it had already earned ("...the cells that do not flip are
   waiting on the ones that do.").

4. **Hypothetical-reader gesture cut (improvement section).** Deleted "A careful
   reader might expect the greedy step to be a gamble: by raising some cells it
   could drop others, the way tightening one part of a plan often loosens
   another. The theorem denies it, and so does the run." The body must speak to
   no one (`spec/slop.md` self-reference: no gesturing at a hypothetical reader).
   The surviving sentence still states and corrects the misconception in its own
   grammar ("...is not a trade that costs one cell to help another; it is a
   change that holds every cell at its old value or lifts it"), so the antithesis
   is licensed, and the concrete run result (bottom two rows lifted, top
   unchanged) is kept.

These four cuts also took ~100 words off the count, which helps the length
warning without touching any derivation, the runnable listing, or a worked
example.

## Required changes for the writer

None.

## Length

The proof reports `W-LENGTH-HIGH` (3974 words vs the 2000-3600 band). This
series is explicitly not strict, and the lesson carries a full runnable
`control.py` with its printed output and two multi-line derivations (the
telescoping improvement proof and the optimality backup). The template forbids
shrinking an idea's explanation to hit a band. Lesson 1 ran long for the same
reason. I cut the slop I would have cut regardless; what remains is tight, so I
left it long rather than amputate content. No action needed.

## Lesson-specific gates (all pass)

- **No "better at every cell" claim.** The piece states the inequality as `≥`
  throughout: "helps everywhere at once, or at worst changes nothing, and never
  costs a cell"; "holds every cell at its old value or lifts it"; "no cell
  anywhere left worse." The gains table omits the top two rows with gain 0.000
  and the prose says the top eight cells do not move. Correct.
- **Cell 14 is the move that beats the policy's choice.** The "Cell 14 would
  rather go right" section prices all four moves (−1.08, +0.32, −1.78, −2.55),
  right beats the hand-drawn up, and Fig. 1 draws the greedy backup at cell 14.
  Cell 13 is correctly shown as the cell whose hand-drawn action is already best,
  so it does not flip first. Matches the researcher's correction.
- **Tie rule stated.** The policy-iteration section states Howard's
  keep-the-old-action-on-a-tie rule (cited `s2` ch. 4 p. 39), names the ties at
  cells 9 and 12, and compares by action value rather than argmax. Problem 2
  states `v_*` is unique while the optimal policy is not. Correct.
- **AlphaGo Zero framed accurately.** The Why bookend: search sharpens the
  network's rule (improvement operator); self-play games scored by that search
  measure how good the sharper rule is (evaluation); the network is trained to
  match both. It does **not** say the network performs the evaluation. "Go
  deeper" says "search as the improvement step." Matches the researcher's
  correction and the manuscript passages.
- **Bellman 1957 not cited for discounted optimality.** The optimality equation
  is cited to `s1` S&B (3.19), p. 63. Bellman's 1957 journal paper is not in the
  Sources list at all. Correct.
- **Bookends uncited; every body section cited.** Why and The takeaway carry no
  citations. Orientation (`s1`), pricing-moves (`s1`), improvement
  (`s1`/`s2`/`s3`), policy-iteration (`s1`/`s2`/`s3`), value-iteration
  (`s1`/`s4`/`s5`) each carry citations. Correct.

## Correctness and citations

Every reported number was checked against the writer's console output (which is
printed in the article) and the researcher's independent cross-check, and they
agree: `v_π(13) = −2.01`; cell 14 action values −1.08/+0.32/−1.78/−2.55 and
cell 13 −2.01/−2.05/−2.71/−2.61; policy iteration converging in two improving
rounds plus a confirming third under the keep-old tie rule; the per-cell gains
table (cells 8-15); value iteration at 18 sweeps to 1e-4 (err 7.6e-5 < 8e-5) and
30 to 1e-8; the cell-13 trace falling for four sweeps and turning on the fifth
(shortest path to the goal is five moves); `v_*(13) = −0.71`, `v_*(14) = +0.61`.
The "beats up by 1.40" figure is the difference of the displayed two-decimal
values (0.32 − (−1.08)); consistent with what the page shows. All citations now
match their sources after the two removals above, including the Howard ch. 7
p. 87 linear-algebra improvement proof (correctly avoiding Howard's `γ`
symbol clash) and the Bertsekas / Van Roy contraction and max-non-expansion
anchors.

The piece does the original work its handoff claims: it runs policy iteration
and value iteration against lesson 1's hand-drawn policy on the unchanged grid
and shows the optimal policy is no worse anywhere and strictly better only on
the bottom two rows near the pit, reached in two improvements, with value
iteration folding one improvement into each of 18 sweeps to the same answer.

## Headlines

- **Headline** "Two improvements find the best policy": subject-verb-object with
  the number as the surprise, no colon subtitle, no unanswered question. Built
  differently from lesson 1's "noun is a X you can Y."
- **Dek**: one plain sentence with this lesson's own numbers, uses "while" not a
  semicolon reversal, suspended question, or comma triad. Adds the figures the
  headline omitted without restating it.
- **Section headings** ("What the hand-drawn arrows are worth", "Cell 14 would
  rather go right", "One greedy step is never a step down", "Evaluate, improve,
  repeat until the arrows stop", "A max in place of the average"): each a step of
  the argument in the piece's own nouns, built differently from each other, and
  none reproduces lesson 1's "X forces Y" / "Only X needs Y" shapes.

## Slop and banned terms

Edges tested hardest. After the four cuts, the first/last sentences of each
section and the article's last sentence ("...learned from sampled experience,
the subject of the next lesson") carry the subject's own nouns and pass the
placeholder test. The parallel four-move pricing sentences (Up/Right/Down/Left)
and the semicolon rules list in orientation are necessary enumerations, not
cadence or chained-semicolon slop, and read cleanly aloud. Counted bans all
pass: em-dash 0 (limit 4), "leverage" 0, "load-bearing" 0, "mechanism(s)" 0.
