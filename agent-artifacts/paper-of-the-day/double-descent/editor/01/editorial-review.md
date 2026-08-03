# Editorial review: paper-of-the-day/double-descent (editor/01)

## Skeptic

Thesis: double descent is a real, widely reproduced effect, but its strongest
original framing — a law in parameter count that extends the classical U-curve
across all model families — is contingent on how complexity is measured, on
label noise, and on regularization. The piece stands on four load-bearing
claims, and I tried to retire each against the cited primaries.

1. **The second descent exists and the interpolation threshold sits at capacity
   = n (n·K for K-class).** Held. Belkin Fig. 1 (asset-1) shows the schematic
   with training risk dashed to zero at and past the threshold; Belkin Fig. 2
   (asset-2) shows the RFF/MNIST curves peaking at N = n = 10^4. The equation
   furniture (N = n; N = nK) matches the evidence record (Fig. 4 net threshold
   at n·K = 40,000). Spigler's independent jamming cusp corroborates. No
   retiring sentence found.

2. **The mechanism is min-norm / smoothness inductive bias.** Held. The article
   ties the coefficient-norm peak to the risk peak in Fig. 2, both visible in
   asset-2 (norm peaks at N = 10^4, then falls toward the min-norm kernel
   reference line, which sits below every finite-N point). Hastie's closed-form
   recovery backs it. Direction checked against the image: correct.

3. **EMC unifies the model-size, epoch, and sample axes; more data can hurt.**
   Held. Nakkiran Def. 1 is set verbatim with a correct five-term legend
   (EMC, T, n, Error_S(T(S)), ε = 0.1). The sample-wise "more data hurts" case
   is stated as 4k → 18k = 4.5×, correctly using the Fig. 3 figure rather than
   the abstract's "quadrupling"/4× — the documented numbering/figure trap was
   handled honestly.

4. **The after-record narrows the "law in parameter count" reading without
   refuting the effect.** Held, and scoped correctly. Curth's x-axis critique is
   confined to non-deep methods in the article's own words ("do not touch
   Nakkiran's ResNet, CNN, and Transformer results ... leaves model-wise and
   epoch-wise double descent in deep networks standing"). Label-noise dependence
   is shown both ways with Nakkiran Fig. 4 (asset-4: CIFAR-100 peak at 0% noise;
   CIFAR-10 plateau that noise deepens). Regularization removal is proved
   (isotropic ridge) and shown (asset-6). The Nakkiran-vs-Mei/Montanari
   misspecification tension is left open, not settled.

Display text audited descriptor by descriptor. Headline states a claim the
piece defends, present tense, no colon tell. Dek makes a claim about the world
(not a grade of the article's method) and identifies the piece; it is a single
from→to sentence, not the barred subsequent-work catalog mold or a comma triad.
Authors, venue (PNAS 116(32), 2019), and year on the abstract card match the
evidence. Byline stamped reading time verified (see Cut — I had to re-sync it
after my cuts).

Every citation href opened as printed. All eight source-list arXiv abstract
pages resolve to the correct papers; all figure `data-nb-url` PDF pages point to
the exact document and figure claimed, and the locators are consistent with the
linked arXiv versions (only Belkin Fig. 1/Fig. 2 are used, both stable across
arXiv/PNAS, so the numbering trap is avoided). The abstract card correctly uses
the arXiv title and arXiv link (the PNAS DOI 403s the checker) with the PNAS
venue recorded in the meta line. `data-nb-kind` audit: all eight are defensibly
`primary` — each is cited only for the claim it owns, so no secondary is
missing and no independent-source gap is hidden.

One genuine defect surfaced: the source-list title for Spigler et al. (#s4) reads
"...affects generalization in deep learning," but the linked arXiv page
(1810.09665) titles it "...affects loss landscape and generalization." The URL
resolves to the right paper; the printed title is inaccurate. Routed to the
writer (the title sits inside citation markup). Curth's title (#s6) differs from
the current arXiv title but matches the NeurIPS 2023 proceedings title the entry
labels it with, so that one is correct as printed.

## Cut

The prose is disciplined and mostly earns its place sentence by sentence; the
builder/reviewer register turns are real (the "Does the curve survive its own
x-axis?" gate marks the pivot into weighing). Two direct fixes:

- A semicolon chain in the opening ("...underfits; too much and it fits the
  noise; between them sits a sweet spot") — the banned run-on-wearing-punctuation
  pattern. Broken into three plain declaratives, which also suits the licensed
  Olah short-declarative cadence.
- "That coincidence is the point," a mild self-grading punchline of the
  "that's the point" family. The surrounding sentences already make the
  norm-peak/risk-peak coincidence salient and then explain it, so the label was
  grading rather than arguing. Cut; the passage reads tighter.

No prompt leakage: "after-record," "reconstruction," and "rebuilt" read as
authored analytical language, not copied instruction labels; no planning labels,
selection rules, or assignment-fulfilled claims. No self-reference. Heading
cadence varies and reconstructs the argument; the one hedged-contrast heading
("A real effect, not a universal law") corrects a misconception the piece
actually disproves, so it is earned. Furniture is all load-bearing: every figure
has a sentence naming what it settles, and the single nb-note-strong Verdict is
apt.

Worst tell was the semicolon chain; no repeated formula across paragraph endings
or headings.

## Reader

What the piece gives beyond its sources: a judged reconstruction that reads five
papers as one argument about a question none of them poses in one place —
whether double descent is a law in parameter count — and walks it figure by
figure to a calibrated verdict (real effect, contingent framing). That matches
the original-work sentence in the draft handoff, and the article delivers it. The
prose sits closer to the voice-guide exemplars than a median summary: it points
at named features on each figure, restates the strong claim before pressing it,
and states a falsification condition in the verdict rather than a hedge.

## Edits

- Broke the opening semicolon chain into three declarative sentences (orientation).
- Cut "That coincidence is the point." (smoother-interpolants section).
- Updated the byline from "11 min read" to "10 min read" to match the re-stamped
  reading_minutes after the cuts.
- Ran `./nb stamp` after the cuts: words=2412 (band 1800-3400), reading_minutes=10,
  sources=8 (floor 8). Byline and nb-meta now agree.

## Required work

- **writer** — Correct the Spigler et al. source-list title (#s4) to the linked
  arXiv title, "A jamming transition from under- to over-parametrization affects
  loss landscape and generalization." Minor, and the only outstanding item; the
  link resolves correctly, so this is a label-accuracy fix inside citation markup.

## Decision

revise — the article is substantively sound and my cuts resolved the prose tells,
but a printed citation title is inaccurate and must be corrected before publication;
it is a one-line writer fix.
