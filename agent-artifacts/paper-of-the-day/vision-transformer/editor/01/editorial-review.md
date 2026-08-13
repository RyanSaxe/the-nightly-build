# Editorial review: paper-of-the-day/vision-transformer (editor/01)

## Skeptic

The article states its thesis clearly from the draft alone. Dosovitskiy et
al.'s data-scale crossover is a real measurement: a pure transformer trails
convolutional baselines when trained on ImageNet-sized data and overtakes them
after pretraining on JFT-300M. The after-record then reassigns the cause. At
ViT-B parameter count, most of what looked like a data-scale requirement was a
training-recipe requirement (DeiT), and the residual, once recipe is fixed too,
is not architectural (ConvNeXt's isotropic tie). Raghu et al. supplies the
mechanism (scale teaches the largest models the local attention a convolution
gets for free) without disturbing any number. The flagship ViT-H/14 88.55%
stays untested at lower data, and the piece holds that bound rather than
writing past it.

The claims it rests on, each tested against the evidence record and reread in
the cited primary:

- **The crossover numbers are the paper's own and correct.** ViT-B/16
  77.91% (ImageNet-1k) to 84.15% (JFT-300M), a 6.24-point gain; ViT-L/16 85.30%
  (ImageNet-21k) to 87.76% (JFT-300M), 2.46; ViT-H/14 88.55% (JFT-300M). Every
  figure matches the Numbers section and the paper's Table 2 / Appendix Table 5,
  every subtraction recomputes, and every dataset size (1.3M / 14M / 303M)
  checks. Held.
- **DeiT beats ViT-B/16's JFT-300M number on ImageNet alone.** DeiT-B, identical
  ViT-B architecture, ImageNet-1k only, reaches 85.2% (distilled, 1000-epoch,
  384px), above ViT-B/16's JFT-300M 84.15%. This is DeiT's own claim, verbatim in
  the evidence quote. The comparison is B/16 to B/16. Held as a claim — but the
  headline's label failed (below).
- **ConvNeXt separates recipe from architecture.** Recipe alone lifts an
  unmodified ResNet-50 from 76.1% to 78.8% (+2.7); the isotropic ConvNeXt ties
  ViT within 0.2 points at S/B/L at matched params, FLOPs, and recipe. Verified
  against Tables 1, 2, 10. Held — but the body's summary conflated distillation
  into "recipe alone" (below).
- **The honest bound.** No after-record source retrains ViT-H/14, or anything
  near its 632M size, on ImageNet-1k alone. This is a claim of absence,
  consistent with the evidence record (DeiT never scales past 86M Base; ConvNeXt
  uses ImageNet-22K; Raghu retrains nothing new). Held, and load-bearing to the
  verdict.

Three breaks, all display-text or precision faults rather than broken reporting,
all fixed in place:

1. **Headline overclaim (the serious one).** The draft read "DeiT beat *Vision
   Transformer's* JFT-300M accuracy training on ImageNet alone." Unqualified,
   "Vision Transformer's JFT-300M accuracy" reads as the paper's flagship
   88.55% (ViT-H/14), which DeiT did **not** beat — DeiT-B's 85.2% beats
   ViT-B/16's 84.15%, a same-size comparison. The false label directly
   contradicts the article's own verdict, which spends a paragraph establishing
   that 88.55% is untouched. A reader who knows ViT's famous number and reads
   only the headline is told the opposite of the piece's finding. Fixed by naming
   the size: "DeiT beat ViT-B/16's JFT-300M accuracy training on ImageNet alone,"
   which is exactly the comparison the body defends and DeiT itself states.
2. **"Recipe alone ... 2.7 to 7.3."** The architecture-vs-recipe summary
   credited "recipe alone" with 2.7 to 7.3 points, but the article's own table
   directly above separates a "Recipe" row from a "Recipe + distillation" row,
   and the 7.3 sits in the distillation row. Recipe alone spans 2.7 (ResNet-50)
   to 3.9 (ViT-B, no distillation). Fixed to attribute 2.7-3.9 to recipe and the
   push to 7.3 to distillation, no number changed.
3. **DeiT dated "one month after the ViT preprint."** The ViT preprint is
   22 Oct 2020 and DeiT is 23 Dec 2020 (both confirmed on the cited arXiv abstract
   pages) — two months, not one. The interval was not in the evidence record and
   was wrong; cut the clause rather than assert a replacement figure, keeping the
   accurate "December 2020."

Sourcing audit. All four `data-nb-kind="primary"` labels are correct: each paper
is the document that owns the result cited to it (ViT for its architecture and
crossover; DeiT, ConvNeXt, and Raghu et al. each for their own numbers). No
secondary source is dressed as primary; no independent-source gap is hidden by a
wrong label. I opened all four source hrefs as printed — arXiv 2010.11929,
2012.12877, 2201.03545, 2108.08810 — and each lands on the paper itself with
title and authors matching the source entry. The one loose cite, ViT-B/16's
77.91% attributed to [2] at the DeiT section's opening, supports DeiT's
starting-point framing and the same figure is owned by and cited to [1] in the
crossover section; left as acceptable.

Both source assets check out. asset-1 is ViT Figure 3, honestly cropped: all
three pretraining datasets on the x-axis, every ViT variant, and the BiT ResNet
band all retained, and the crossover the argument spends (BiT above ViT at
ImageNet, the two largest ViT variants above the band at JFT-300M) is exactly
what the image shows. asset-2 is ViT Figure 5, both panels and all three series
(ViT / ResNet / hybrid) kept with the log-x compute axis, and the two things the
prose spends — ViT above the ResNet curve at matched compute, the hybrid's edge
vanishing at large compute — are both visible. Captions are factual and cited to
the correct original figure numbers via `data-nb-locator`, while the article
renumbers them as its own Fig. 1 / Fig. 2; the locators disambiguate, so this is
honest. The equation math is faithful: Equation 1's patch-embedding assembly,
the Eq. 2-3 encoder block, and Eq. 4's `y = LN(z_L^0)` all match the paper and
the legend labels each symbol correctly.

## Cut

The slop pass turned up one repeated pattern: self-narration of the article's
own structure. Three instances, all cut or rewritten:

- The orientation closed on a roadmap sentence beginning "What follows rebuilds
  the architecture ..." — a direct hit on the self-reference tell
  (`spec/slop.md` lists "what follows" by name). Cut; the section now ends on the
  substantive claim about when inductive bias stops paying, a stronger close.
- The after-record's opening paired "Everything above is the paper's own report"
  with a second "What follows." The turn from explaining the paper to examining
  it is one the voice guide explicitly wants signalled, so I kept the turn and
  the controlled-variable framing (three papers, two of three variables held
  fixed) but rewrote it without the self-reference: "That is the paper's own
  report. The after-record is three later papers ..."
- The synthesis table was introduced with "this section and the last one
  separate two variables ..." Rewrote to name the actual content — "The DeiT and
  ConvNeXt experiments separate two variables ..." — which drops the structural
  self-reference and reads more concretely.

The dek was rebuilt. The draft's dek ("changed only the training recipe ...
closes nearly all the rest of the gap") folded distillation into "recipe" — the
same conflation as the body break above, and misleading given that the
record-beating DeiT number needs a convolutional teacher — and closed on "the
rest of the gap," a dangling referent for anyone arriving from a link. The
replacement leads with what the headline leaves out (ConvNeXt's isotropic tie)
and states the stance positively, avoiding the negative-parallelism molds the
headline standard bars from deks.

Negative parallelism elsewhere was checked, not reflexively cut. "not whether
the crossover is real, but what it is made of" (Raghu section) and "a
transformer, rather than a training procedure, is what needed the data"
(synthesis) each correct a misconception the piece actually names and defends,
so both stay. Punctuation is clean: zero em-dashes in the body, en-dashes only
in numeric and page ranges, colons used to introduce their payoff. Headings
reconstruct the argument in the piece's own nouns and avoid the recent pieces'
problem-motivation opener and "what survives" holdsup closer; the verdict is
template-required and framed on the specific ViT-H/14 bound, not a generic
survival mold. No prompt leakage: the three-variable decomposition is the
article's own synthesis, not lifted from the commission.

## Reader

Read straight through as a machine-learning engineer who has read nothing else,
the piece gives one thing no single source gives: a controlled decomposition of
the ViT-versus-CNN gap into recipe (2.7-3.9 points), architecture (about zero),
and data (6.24 points), built by setting DeiT's ViT-B recipe ablation,
ConvNeXt's ResNet-50 recipe ablation, and the isotropic ConvNeXt/ViT tie beside
ViT's own data-only crossover in a single table — an accounting none of the four
papers assembles, then used to show the crossover is real as a measurement but
cannot by itself name the architecture as the variable that needed the data. The
original-work sentence in the draft handoff describes exactly this, and the
article delivers it. The prose sits closer to the voice-guide exemplars than a
median summary: it builds the notation one symbol at a time (patch, then token,
then Equation 1), and it names bounds in the register the guide asks for
(Raschka's habit of stating what a result does not cover, Weng's flat verdict on
a limitation), most visibly in keeping ViT-H/14's untested flagship in view
through to the closing question.

## Edits

- Rewrote the headline (all three copies: `<title>`, nb-meta, `<h1>`) from
  "Vision Transformer's JFT-300M accuracy" to "ViT-B/16's JFT-300M accuracy" to
  stop the flagship-88.55% misreading.
- Rewrote the dek (nb-meta and nb-dekline) to lead with the ConvNeXt tie, drop
  the distillation-as-recipe conflation and the dangling "rest of the gap," and
  clear a sentence-density warning.
- Cut the orientation's "What follows rebuilds ..." roadmap sentence.
- Rewrote the after-record opener from "Everything above ... What follows ..." to
  "That is the paper's own report. The after-record is three later papers ...",
  keeping the turn and the held-variable framing without self-reference.
- Cut ", one month after the ViT preprint" from the DeiT introduction (the gap is
  two months; verified against both arXiv pages).
- Rewrote "this section and the last one separate two variables" to "The DeiT and
  ConvNeXt experiments separate two variables."
- Split "Recipe alone ... is worth 2.7 to 7.3 points" into recipe alone (2.7 to
  3.9) plus distillation (to 7.3), and changed "those two numbers" to "those
  figures"; no number altered.
- Ran `nb check --no-check-links`: BLOCK 0, the two documented warnings remain
  (annotated-equation TeX density; sources floor).

## Required work

None blocking. Optional, non-blocking, for whoever picks it up:

- **researcher / writer:** I removed the incorrect "one month" gap. If a
  temporal anchor is wanted back, the verified interval is two months
  (ViT 22 Oct 2020, DeiT 23 Dec 2020); the evidence record does not currently log
  publication dates, so the researcher would add them before the writer restores
  the beat. Not needed for publication.
- **orchestrator:** re-stamp (words/dek/title changed) and run the final
  link-checked proof; the source-floor warning is accepted, not to be padded.

## Source floor

Approve with the warning accepted. The proof leaves W-SOURCES-MIN (4 versus the
non-strict series floor of 8). Judged on the argument: every load-bearing claim
rests on one of the four opened primaries, each of which owns its result. The
baselines the crossover is measured against (BiT ResNets, the JFT-300M and
ImageNet-21k datasets, the reused transformer encoder, and Swin) are cited as
reported inside the ViT and ConvNeXt comparison tables — the papers that own
those tabulations — so no load-bearing claim rests on an uncited primary. Opening
BiT, Swin, JFT, or Vaswani as separate entries would either cite documents the
researcher did not read or pad the list with sources the argument does not spend.
Four honest sources carry it; more would be padding. Not routed.

## Decision

approve — the crossover reconstruction and its three-variable synthesis are
sound and fully sourced; the headline's flagship overclaim, the recipe/
distillation conflation, the self-reference tells, and the wrong DeiT date were
all fixable in place, leaving no publication-blocking work.
