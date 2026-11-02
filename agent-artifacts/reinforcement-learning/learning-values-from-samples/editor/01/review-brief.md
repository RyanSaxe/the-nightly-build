# editor review-brief: reinforcement-learning/learning-values-from-samples (01)

Inputs (all absolute):
- Editorial direction: .../agent-artifacts/reinforcement-learning/learning-values-from-samples/editorial-direction.md
- Commission (holds the recent-pattern notes to enforce): .../commission.md
- The exact writer brief: .../writer/01/brief.md
- Evidence: .../researcher/01/evidence.md
- Voice guide (read first): .../writing-coach/01/voice-guide.md
- Draft handoff: .../writer/01/draft-handoff.md
- Article to judge/edit: /home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/library/reinforcement-learning/learning-values-from-samples.html

Output: editorial-review.md in .../editor/01/

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/learning-values-from-samples/library/reinforcement-learning/learning-values-from-samples.html --series reinforcement-learning --repo /home/user/the-nightly-build

Decide whether this lesson publishes, and edit it until it can. Change anything except the facts; send back only if it needs a different argument.

Correct: state the thesis and claims from the draft alone. This is a teaching piece whose figures come from a code run — verify the numbers are internally consistent and match what the listings would produce (recompute a couple by hand from the stated setup, e.g. an MC/TD update step; the true v_pi(13) = -2.01 from lesson 1 is the yardstick). Confirm the estimators as shown use only sampled episodes and never read P/R/transitions, and that the exact solve is used only to score. Check every title, number and term in the headline, dek and subheads. Open every citation href. Audit data-nb-kind.

Reads well / slop: hold the whole piece to spec/slop.md, hardest at the edges. ENFORCE the recent-pattern notes in the commission against lessons 1 and 2: the "Why this matters" must NOT open on AlphaGo/AlphaZero; the dek must not use the "On the grid, X does Y to cell 13, while Z" mold; the body-closer must not end on "the next lesson"/"the subject of the next lesson"; the takeaway must not close on a reflective "remember the pair" line; headings must not echo L2's shapes. Compare the actual lesson 1/2 openers, deks, closers and headings (via `./nb history --show ...`) as the recent record.

Experience: read the rendered page from the top (nb preview). Check every figure/chart against the evidence and the run — overlapping labels, arrows short of their target, a heatmap or learning curve that does not show what the prose claims. Answer in one sentence what the lesson gives beyond its sources, then compare with the writer's original-work sentence in draft-handoff.

Write editorial-review.md in the skill's shape (Correct / Reads well / The experience / Edits / Decision). After direct cuts, if the proof needs only a restamp, I (orchestrator) will run nb stamp and nb check; return to the writer only where the proof fails on something needing new prose. Report the review path and the decision.
