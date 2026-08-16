# Editorial review: paper-of-the-day/adversarial-examples (editor/01)

## Skeptic

Thesis: Goodfellow, Shlens, and Szegedy's linear explanation of adversarial
examples produced a durable attack and a first defense, but its account of the
cause was superseded by the view that the vulnerability lives in the data's
non-robust-but-predictive features. The piece stands on four claims, each tested
below.

Claim 1, the linear-growth reconstruction. Verified the algebra against the
paper and the evidence record. The equation sets the constraint-saturating
perturbation as `eta = epsilon * sign(w)`, not the bare `sign(w)` the paper
prints in one place, so the epsilon is not dropped. `w^T eta = epsilon m n`
follows because `sign(w_i) w_i = |w_i|`, summed over `n` terms of average
magnitude `m`. The annotated equation names epsilon (the fixed bound), m
(average weight magnitude), and n (input dimension) exactly. This is the load-
bearing math and it is correct.

Claim 2, FGSM. `eta = epsilon * sign(grad_x J(theta, x, y))` matches the paper's
Sec. 4 form and the evidence record. The prose earns why the sign, not the
magnitude, is what a max-norm budget rewards: every component is already at the
boundary, so only its sign is free. Correct.

Claim 3, the harnessing claim and its own qualification. The reframing numbers
check out against the evidence record: clean MNIST error 0.94% to 0.84%
(1600-unit model 0.782%), FGSM adversarial error 89.4% to 17.9%, and misclassi-
fied adversarial examples still 81.4% average confidence. Directions are right
(error dropped; confidence stayed high). The generation-time figures (maxout
89.4% at 97.6% confidence, softmax 99.9%, CIFAR-10 87.15%) match. Madry >89%
MNIST / ~46% CIFAR-10, Ilyas 43.7-63.3% vs 10% chance, Athalye 7-of-9 and
6-complete-1-partial, Carlini-Wagner 95%-to-0.5%-then-100%, Wang 70.69% at
eps=8/255 all match their owning primaries.

Claim 4, the prior-view clash. Szegedy 2013 is represented in his own words
(the "low-probability pockets" quote in the note matches the evidence quote
verbatim), and the piece states plainly that the "nonlinearity" framing is
partly Goodfellow's own construction rather than asserting it as Szegedy's
position. The pockets-versus-contiguous-regions disagreement (Sec. 8, Fig. 4)
is presented as the real, load-bearing geometry clash the transfer argument
rests on. No strawman.

Display text, descriptor by descriptor. Opened all ten hrefs (nine source
entries, the paper card, and the Fig. 1 `data-nb-url`); every one resolves 200
to the document's own page. Verified each source's title, author list, and venue
against the live arXiv record: Goodfellow/Shlens/Szegedy, Szegedy et al.,
Ilyas et al. (NeurIPS 2019), Tsipras et al. (ICLR 2019), Madry et al. (ICLR
2018), Athalye/Carlini/Wagner (ICML 2018), Carlini/Wagner (IEEE S&P 2017),
Croce et al. (NeurIPS 2021), Wang et al. (ICML 2023) — all correct. The verbatim
abstract in the paper card matches the arXiv abstract word for word. Headline,
dek, and every subhead are written in the piece's own nouns and commit to
something the piece establishes.

`data-nb-kind` audit. Every source is cited only for its own claims and carries
`primary`. The one place a secondary label could hide a gap — Goodfellow
characterizing Szegedy's prior view — is handled correctly: the paper (#s1) is
cited only for its own text ("focused on nonlinearity and overfitting"), and
Szegedy's actual hypothesis is cited to Szegedy (#s2). No secondary
characterization is passed off as primary evidence.

Source asset. Inspected `asset-1.png` as a reader. It retains all three Figure 1
panels, the "+ .007 x" and "=" operators, the per-panel expressions, and every
confidence (panda 57.7%, nematode 8.2%, gibbon 99.3%) at epsilon=0.007. The
printed page caption is cropped out; the article's caption is a factual cited
label. No unrelated clutter. The middle panel is retained, so the reader can see
the perturbation is the gradient's sign, not random noise. Correct as is; no
recrop routed.

No break survived. Every claim held against its owning primary.

## Cut

Ran the slop pass sentence by sentence, then the edges alone, then the
dangling-referent read, then the delete test, then a leakage pass against the
commission and briefs.

Five sentences failed and were cut or repaired. Two were self-reference that
doubled as prompt leakage: "This piece rebuilds that argument and then weighs it
against the ten years that tested it" (the assignment, narrated) and "The scale
is the point of the reconstruction" (the article naming its own method). Two were
edge signposts that survived only on their neighbors: "That is worth checking
against the record, because the record is more specific than the summary" (a
method announcement; the contrast that follows carries it, so I joined the next
sentence with "But") and "The paper returns to settle that question later, and
where it lands is where its account of transfer stands or falls" (a forward
pointer plus an engineered "where it stands or falls" punchline; the later
section makes the point on its own). One was an unearned punchline: "The sign is
the whole point of the max-norm setting" ("the whole point" announces a stake
the next sentence actually builds, so the announcement was redundant).

Pattern: the failures clustered at section edges and all leaned on the
"whole/point" framing or on narrating the article's own plan. The middles report
cleanly.

Also changed one term for consistency ("the reconstruction holds" to "the linear
view holds," the name the piece uses everywhere else) and converted two reflex
semicolons to periods per the editorial direction's punctuation repairs. Left
one genuinely tight semicolon standing.

Checked the surviving negative-parallelism constructions against the "earned
contrast" test: "not about a straw man but about geometry" corrects a
misconception the section names (the nonlinearity strawman), and "not a
like-for-like ranking" corrects the real misreading of the stat strip. Both
stay. Compared distinctive phrasing against the voice-guide quotations; found no
borrowed clause. The register sits where the guide directs: Olah/Weng patience in
the reconstruction (intuition before the algebra, the figure read in plain
verbs), Huszar concession-before-critique in the weighing.

Furniture: one annotated equation, one `nb-note-strong` Verdict, no pull quote —
all within the catalog's per-article limits. The Verdict is the piece's own
weighing in fresh nouns, not a stamped "what the paper is right about" heading,
so it clears the recent-pattern caution.

## Reader

Read straight through as the declared ML practitioner. What the piece gives
beyond its sources: a single argument that re-sequences the paper's linear
explanation so the max-norm intuition precedes the algebra, then sets the
paper's own printed self-qualification (17.9% error but 81.4% confident when
wrong) against the pockets-versus-contiguous geometry and the Ilyas/Tsipras/Madry
record to reach a verdict on which half of "linearity explains adversarial
examples" the decade kept. No single source carries that weighing. The draft's
original-work sentence claims the same synthesis, and it survives. The prose sits
closer to the voice-guide exemplars than to a median summary: it concedes the
strong version of the linear view before faulting it, and builds each quantity
before spending it.

Headline as the largest claim: "got the attack right and the cause wrong"
commits harder than the commission's "incomplete," but the piece earns it (Ilyas
makes "regularize out the flaw" the wrong picture, not merely a partial one), and
the dek supplies the precision by naming where the cause was traced. It is not
the desk's "the proof leaves out its claim" mold, and the dek carries none of the
banned mold shapes.

## Edits

- Cut "This piece rebuilds that argument and then weighs it against the ten years that tested it." (orientation): self-reference and prompt leakage.
- Cut "That is worth checking against the record, because the record is more specific than the summary." (prior-view) and joined the next sentence with "But": method-announcing signpost.
- Cut "The paper returns to settle that question later, and where it lands is where its account of transfer stands or falls." (prior-view): forward-pointer signpost plus engineered punchline.
- Cut "The sign is the whole point of the max-norm setting." (fast-gradient-sign): unearned "whole point" punchline the next sentence already builds.
- Cut "The scale is the point of the reconstruction." (reframed): self-reference naming the article's own method.
- Changed "the reconstruction holds" to "the linear view holds" (contiguous-regions): consistent naming, removes mild self-reference.
- Converted the semicolon in "does not merely survive the change; it rises" to a period (fast-gradient-sign).
- Converted the semicolon in "the gradient an attacker needs; adapted attacks broke six" to a period (reframed).
- Added a disclosure to the stat-strip paragraph (reframed): the three eps=8/255 figures do not share an evaluation attack (Madry 45.8% under multi-step PGD [5], the other two under AutoAttack [8]), so the strip is a scale anchor, not a like-for-like ranking. Grounded in the evidence record; no number changed.

## Required work

None blocking. The math, the source asset, the numbers, the citations, and the
sourcing labels are all correct; every slop and disclosure issue was fixable in
prose and fixed directly.

- orchestrator: re-run `nb stamp` before the final `nb check`. Sentences were cut and added, so the stamped `words`/`reading_minutes` need refreshing; the rendered dekline and nb-meta `dek` were not touched and remain byte-identical.

## Decision

approve — every load-bearing claim held against its owning primary, the asset and
equations are correct, and the slop, self-reference, and stat-strip disclosure
issues were resolved with direct edits; the article is ready to stamp, prove, and
prepare for PR.
