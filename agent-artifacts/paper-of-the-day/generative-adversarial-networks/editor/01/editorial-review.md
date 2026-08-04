# Editorial review: paper-of-the-day/generative-adversarial-networks (editor/01)

## Skeptic

Thesis: the GAN optimality result (unique optimum at p_g = p_data, criterion
value −log 4) is a true theorem about function-space minimax with the
discriminator solved to its inner optimum, but the loss Algorithm 1 actually
descends is a different object, and the after-record diagnoses the two losses
differently — the famous vanishing gradient indicts the abandoned minimax loss,
while the non-saturating loss GANs trained on is diagnosed as an unstable,
infinite-variance gradient. The paper declares both gaps itself.

Load-bearing claims and how each held:

1. **The value function (Eq. 1).** Printed as `min_G max_D V = E_{x~p_data}[log
   D(x)] + E_{z~p_z}[log(1 − D(G(z)))]`. Matches the paper's Eq. 1 and the
   evidence quote exactly. The cash-out lands in the next sentence (the inner
   max makes it more than a moving-target classifier). Holds.

2. **Optimal discriminator (Prop. 1).** `D*_G(x) = p_data/(p_data + p_g)`.
   Correct, and the pointwise argument (a·log y + b·log(1−y) maximized at
   y = a/(a+b)) is sound. Cashes out into what the generator now fights (a fixed
   function of the two densities). Holds.

3. **The reduction C(G) = −log 4 + 2·JSD (Thm. 1).** The annotated equation and
   its legend are honest: −log 4 is the floor and the optimum value, the factor
   2 makes the game track the divergence, JSD is symmetric and zero iff its
   arguments coincide. −log 4 ≈ −1.386 checks (log 4 = 1.3863). D* → 1/2 at the
   optimum checks. JSD pinned at max log 2 under disjoint support checks. Holds.

4. **The hinge — which theorem indicts which loss.** This is the spine and the
   piece's one act of original work, so I pushed hardest here. The article keeps
   the distinction clean across four paragraphs: the M·ε/(1−ε) bound that
   vanishes as ε → 0 is attributed to the *original minimax* loss
   (Thm. 2.4 / Cor. 2.1, §2.2.1); the `KL(p_g‖p_data) − 2·JSD` identity with
   centered-Cauchy, infinite-variance coordinates is attributed to the
   *non-saturating* loss the paper actually uses (Thms. 2.5–2.6, §2.2.2). The
   set equation `E_z[−∇_θ log D*(g_θ(z))] = ∇_θ[KL(p_{g_θ}‖p_data) −
   2·JSD(p_{g_θ}‖p_data)]` matches the evidence quote of Thm. 2.5 verbatim. The
   closer ("precise about a loss the paper set aside in Section 3") states the
   distinction without blurring it. Note: the article's "no finite mean and
   infinite variance" is more accurate than the evidence's "infinite mean" (a
   Cauchy mean is undefined), so the writer improved on the record rather than
   copying its slip. Holds, and it is stated correctly.

5. **Prop. 2 / Algorithm 1 gap.** The two Prop. 2 assumptions ("enough
   capacity", discriminator "is allowed to reach its optimum given G") are
   quoted correctly; k = 1 "the least expensive option" is quoted correctly;
   the Section 3 loss swap ("same fixed point", "much stronger gradients early
   in learning") uses genuine phrases from the paper's Section 3. The gap is
   framed as self-declared, matching the evidence. Holds.

6. **WGAN principled-but-contested.** Presented as a real fix (Earth-Mover
   continuous/differentiable a.e., weaker topology, dual over 1-Lipschitz
   critics) and then contested three ways, each attributed to its owner:
   Gulrajani (weight clipping "can lead to undesired behavior", gradient
   penalty), Mescheder (WGAN/WGAN-GP with finite critic steps "do not always
   converge to the equilibrium point"; the stabilizer is the penalty, not the
   Wasserstein distance), and Fedus (divergence-minimization "overly
   restrictive", Goodfellow a co-author). The verdict grades rather than
   splitting the difference ("they do not refute either one"). Holds; not
   symmetric-for-its-own-sake.

7. **Parzen-window named the weakest actual claim.** "The paper's soft spot is
   not its theory but its evaluation" — stated plainly, with the authors' own
   hedge quoted and the numbers (MNIST 225 ± 2, TFD 2057 ± 26) matching the
   evidence. Holds.

Display text: headline carries no colon subtitle and no eponym, present-tense
claim the piece defends, and reads as a gap ("leaves out"), not a debunking —
the recent-pattern trap is avoided. Dek is two clauses joined by "and", not a
comma triad, adds specifics the headline omits, and is byte-identical to the
nb-meta `dek`. Headings reconstruct the argument and use the piece's own nouns;
only one uses the comma-"and" cadence, so no formula. Every named
person/affiliation attribution (Gulrajani with Arjovsky; Mescheder, Geiger,
Nowozin; Fedus with Goodfellow; Radford, Metz, Chintala; Salimans) verified
against the owning arXiv page.

Sourcing: all 8 `data-nb-kind="primary"` labels are correct — each source is
cited only for a claim its own authoring party owns firsthand, and no secondary
reporting stands in for a primary. I opened all 8 source hrefs; every one
resolves to the correct source's own arXiv abstract page (1406.2661, 1701.04862,
1701.07875, 1704.00028, 1801.04406, 1710.08446, 1511.06434, 1606.03498). The
three figure `data-nb-url` provenance links point to the correct pages of the
focal PDF.

One item checked and left standing: the sentence ending the evaluation
paragraph credits the field with "abandoning it for the Inception score and its
successors within two years", carrying the s1 cite (which owns the Parzen
numbers). The Inception score is genuinely Salimans 2016 (s8, a cited primary),
2014→2016 is two years, and this is nonessential synthesis resting on cited
work, so it is not a break — a borderline citation-precision point, not
publication-blocking.

## Cut

Three surgical cuts, each removing a sentence that graded the piece or
signposted it instead of doing argument work:

1. "That quantity is what the next step names." — a forward signpost closing the
   optimal-discriminator section. The paragraph now ends on "...a quantity that
   depends on the two distributions and nothing else", a stronger landing, and
   the next section picks it up without the scaffolding.

2. "The distinction matters for reading the whole story." — a stakes-announcing
   opener on the vanishing-gradient closer. The distinction had just been drawn;
   the paragraph is sharper opening straight on "The famous one-line verdict...".

3. "That is the reason to weigh this paper rather than debunk it." — the worst
   tell: it both grades the article's own posture and leaks the briefing's
   weigh-vs-debunk framing into the prose. The surrounding argument (the method
   succeeded anyway, which is itself evidence the divergence account is not the
   whole story) carries the point without the label.

The four W-SENTENCE-DENSITY warnings (40–41-word sentences) were each judged
against the "long sentence in control is craft" allowance and kept: each is a
single controlled thought set against short sentences on either side (the loss
substitution, the Prop. 2 assumptions, the Earth-Mover topology claim, one
caption), and none loses its thread. No repeated rhetorical shape across
paragraph endings; the two earned hedged contrasts (the theory/practice pivot
and the "not its theory but its evaluation" verdict) sit within the ceiling and
the WGAN turn stays graded rather than spending a second one. Furniture (paper
card, four set equations with one annotated legend, three source figures, the
Example 1 table, the holds-up grid, the verdict block) each carries evidence or
the reviewer's verdict; none reads as a decorative block.

## Reader

What the piece gives beyond its sources: a reader finishes able to say which
after-record theorem indicts which GAN loss — that the celebrated vanishing
gradient is about a loss the paper set aside, while the loss the field trained
was diagnosed separately as an infinite-variance update on KL − 2·JSD — and to
tie both to the same disjoint-support fact the paper's own Prop. 2 and Section 3
already gesture at. No single cited source foregrounds that mapping; the piece
assembles it. That matches the original-work sentence in draft-handoff.md, and
it is visibly the hinge the headline, dek, and verdict all turn on. The prose
sits closer to the Weng/Olah/Nielsen exemplars than a median summary: every
equation cashes out in the next beat, the M·ε/(1−ε) bound and the Example 1
table are worked instances rather than restated trends, and the verdict grades
instead of shrugging.

## Edits

- Cut "That quantity is what the next step names." (optimal-discriminator section).
- Cut "The distinction matters for reading the whole story." (vanishing-gradient section).
- Cut "That is the reason to weigh this paper rather than debunk it." (what-training-did section).
- Ran `nb stamp`: words 3062 → 3034, reading_minutes 13, sources 8.

## Required work

None. The writer runs the proof (`nb check`) as the final gate; the cuts only
removed prose and introduce no new banned terms or blocks, and the four kept
density warnings are the same ones the draft handed off as intentional craft.

## Decision

approve — every load-bearing equation and the which-theorem-indicts-which-loss
hinge verify against the sources, all provenance and hrefs resolve, and the only
defects were three gradey/signpost sentences, now cut.
