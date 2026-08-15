# Editorial review: paper-of-the-day/variational-autoencoder (editor/02)

This is a confirmation re-review after the sources repair. In editor/01 I
completed the three reads and approved the reconstruction, the math (verified by
recomputation), and the throughline; the single open item was the source floor.
This round verifies only what changed — the three added sources, the new
diffusion verdict paragraph, the beta-VAE disposition, and the renumber — and
that nothing regressed.

## Skeptic

The thesis and its load-bearing claims are unchanged from editor/01 and were not
reopened. I checked each of the three new citations where it lands, opened the
three new hrefs, and read the new verdict paragraph against its source.

1. **Paisley, Blei, and Jordan 2012 (source 3), the high-variance claim.**
   Attached in the gradient-problem section to the sentence that the paper "sets
   aside" the score-function estimator because it "carries very high variance,"
   with the citation reporting the result rather than deriving it. That is
   exactly what source 3 owns: its Section 4 opening states the variance problem,
   gives the Cov(X)/S scaling, and reports the sample count can be "very large in
   practice." The article's locator (§4 'Searching with control variates,' p. 3,
   opening paragraph) matches the evidence locator. The href
   (arxiv.org/abs/1206.6430) resolves 200. `data-nb-kind="primary"` is honest —
   this is the authors' own paper, and it is cited for the claim the authors own.
   The claim lands.

   One break, fixed. The prose named these authors "Blei, Jordan, and Paisley"
   at this citation, but the source list, the new verdict paragraph, and the
   paper itself all give the true order "Paisley, Blei, Jordan" (confirmed
   against the arXiv record: John Paisley, David Blei, Michael Jordan). The
   round-02 diffusion paragraph, which names them correctly, turned a
   pre-existing wrong order into a live internal contradiction — the same three
   authors in two orders in one article. I corrected the gradient-section prose
   to "Paisley, Blei, and Jordan," matching the owning primary and the rest of
   the article. No number, quotation, or claim changed.

2. **Doersch 2016 (source 2), the reparameterization-validity claim.** Attached
   to the gradient-problem sentence that there is "no differentiable path through
   the random draw" — the wording I repaired in editor/01, which asserted the
   continuity requirement without a source that owns it. Source 2 is where that
   generalization is stated in general form: the noise must come from a fixed,
   unlearned distribution and the reparameterizing function must be continuous in
   x, "so that we can backprop through it," with the explicit consequence that a
   discrete latent breaks the trick. The locator (§2.2, p. 11, paragraph
   following Eq. (10)) matches the evidence. The href (arxiv.org/abs/1606.05908)
   resolves 200. On `data-nb-kind`: the tutorial as a whole is expository, but
   this specific necessary-conditions generalization is Doersch's own and appears
   in neither Kingma-Welling nor Rezende et al., so for the claim it is cited
   against he is the owning author. Primary is defensible and the researcher
   documented the reasoning. The claim lands.

3. **Ho, Jain, and Abbeel 2020 (source 8), the diffusion forward link.** New
   verdict paragraph. Its quote — "the usual variational bound on negative log
   likelihood" — is verbatim against the evidence and correctly attributed to Ho,
   Jain, and Abbeel, with the right locator (Eq. (3), §2, p. 2). The structural
   claim, that their KL-decomposed rewrite is "the same reconstruction-minus-KL
   shape as this paper's Eq. (3), stretched from one latent step to a chain of T
   timesteps," is supported by the evidence (Eq. (5)–(7), §2, p. 3) and does not
   overreach: the evidence establishes the diffusion objective is derived the
   same way, not merely analogous, and the paragraph claims exactly that. The
   recurring-variance sentence quotes "high variance Monte Carlo estimates"
   verbatim and ties it back to source 3 with the correct author order. The href
   (arxiv.org/abs/2006.11239) resolves 200. The paragraph is earned, correctly
   owned, and stops where the source stops.

**beta-VAE (source 7) stays honestly secondary.** `data-nb-kind="secondary"`,
href to the DBLP record, and a `data-nb-note` that states plainly it is cited to
the bibliographic index because every automated route into OpenReview returned a
bot-verification challenge, so "only the bibliographic record, not the
mechanism's own derivation, was directly read." The prose makes only the
general, corroborated disentanglement claim with no equation- or page-level
locator. It is not presented as read.

**Renumber.** First-citation order holds: s1 (abstract) → s2, s3 (gradient
problem) → s4 (reparameterization) → s5 (experiments) → s6, s7, s8 (verdict).
Every `#sN` href has a matching `<li id="sN">`, every visible superscript equals
its target number, and no dangling or stale-number reference survives. `nb-meta`
sources count is 8; the proof reports no W-CITE-ORDER and no W-SOURCES-MIN.

**No regression in math or numbers.** Both annotated equations, the SGVB
estimator, the IWAE bound, and every experiment number (500/200 hidden units,
minibatch 100, one sample, 100 units and 3 latent dimensions, Bowman's 99-vs-2)
are unchanged from editor/01. All editor/01 edits still stand: the merged
orientation signpost, the recast comma splice, the cut "identity does more than
name a bound," the "no differentiable path through the random draw" wording, the
cut self-grading and signpost sentences, the cut punchline, and the rewritten
beta-VAE paragraph.

## Cut

No fresh slop pass was owed and none of the added prose introduced any. The
diffusion paragraph carries facts and a reasoning step in every sentence; its
closer ("Diffusion training reappears from the same objective this paper
derives, stretched to a deeper chain of latents") states the conclusion the
paragraph builds rather than signposting it. The beta-VAE paragraph is the
already-approved editor/01 rewrite, unchanged. My one change this round is a
correctness repair, not a cut.

The proof reports BLOCK 0, WARN 3, PUBLISHABLE. The three W-SENTENCE-DENSITY
warnings are the accepted category: two are raw TeX inside the annotated ELBO and
SGVB-estimator equations (punctuation scores 61 and 66 from subscripts and
braces, transcribed verbatim), and the third is the Bowman verbatim quotation (46
words, reproduced exactly and unrepunctuable without ceasing to be a quote). The
new diffusion prose added no density warning — the writer split the one sentence
that had tripped it. The count and category match editor/01's concurrence.

## Reader

Unchanged from editor/01, and the additions strengthen it rather than shift it.
The piece still gives the reader the causal chain the sources hold only as
separate facts. The two new gradient-section citations now put a named owner
under two claims the argument leans on (the variance result and the
continuity/no-discrete-latents requirement), and the diffusion paragraph earns
the commission's forward link honestly: it shows the same bound generalizing
forward rather than asserting influence. The prose still sits closer to the
voice-guide exemplars than to a median summary. The headline reads true as the
largest claim.

## Edits

- Gradient-problem section: corrected the author order "Blei, Jordan, and
  Paisley" to "Paisley, Blei, and Jordan," matching the owning primary (source 3,
  confirmed against the arXiv record) and the article's own verdict paragraph and
  source list, removing an internal contradiction the new diffusion paragraph
  exposed.

## Required work

None. The source floor is met (8 sources, no W-SOURCES-MIN, no W-CITE-ORDER); the
three added citations land and own their claims with honest `data-nb-kind`; the
diffusion paragraph is earned and correctly attributed; beta-VAE remains a
declared secondary; the renumber is internally consistent; and no math, number,
or prior edit regressed.

## Decision

approve — the sources repair closes the only open item from editor/01: the piece
now stands at eight load-bearing sources, each new citation owns the claim it is
attached to, the diffusion forward link is earned and correctly sourced to Ho et
al., and the one inconsistency the round introduced (a split author order) is
fixed, with the proof clean at BLOCK 0 / PUBLISHABLE.
