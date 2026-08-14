# Editorial review: unbiased/ai-training-copyright (editor/01)

## Skeptic

Thesis: the $1.5 billion Bartz settlement resolved only the piracy half of a
split ruling, training on lawfully acquired books was already held to be fair
use, and the genuinely contested question is whether the piracy-derived
per-work price should govern AI training generally. That thesis is sound and
the piece rests on four load-bearing claims, each tested against the primary it
cites.

1. The split itself, and the four-factor table. This is the article's spine and
a hard gate, so I opened Judge Alsup's order (the s2 href, which resolves in a
browser; my automated fetch drew a bot 403, not a dead link) and read the
factor analysis and the "Overall Analysis" section directly. Every cell holds.
Training copies: first factor "favors fair use" (p. 30, "exceedingly
transformative," verbatim at the order's fair-use conclusion), second factor
against ("points against fair use for all copies alike"), third "favors fair
use for the training copies," fourth "favors fair use for the training copies"
— i.e., fair use under all but the second factor, exactly as the table's
"the one factor training lost" cell states. Pirated-library copies: all four
"points against fair use," summarized as "Every factor points against fair use."
No writer-introduced holding, no cell the order does not itself supply. The
order's third, in-between category (destructive print-to-digital conversion,
where the order calls the fourth factor "neutral") is omitted from the two-column
table; that omission is defensible editorial scoping for the pricing question
and does not misstate the two categories shown, so I left it.

2. The settlement figures and release scope. I extracted the settlement order
(s1) and confirmed every number the piece spends: $1.5B non-reversionary fund,
482,460 works on the Works List, ~$3,000 estimated per-work payment described as
"four times the statutory minimum for ordinary infringement ... of $750" and
"fifteen times the statutory minimum for innocent infringement of $200,"
91.3% claims rate, and the release quote — class members give up claims
"broadly related to past AI inputs" but not "claims about past AI outputs, nor
claims of any kind about future conduct." All verbatim. The article's central
"does not touch the training ruling" claim is carried by this release scope plus
the Alsup split, and it holds.

3. The Copyright Office material. I extracted the Part 3 report (s6) and
confirmed the spectrum passage, the Brauneis "transcends the human limitations"
quote, the Samuelson/Sag "not just transformative, it is highly transformative"
quote, the a16z "far less competition, far less innovation" quote, and the
"recommends allowing the licensing market to continue to develop without
government intervention" line. The cover confirms "pre-publication version,"
"May 2025." The article presents the report as contested-standing analysis and
not binding law, as the brief requires.

4. The champions. Titles and quotes check against their owning sources: Mary
Rasenberger, CEO, The Authors Guild and the "excellent result ... robbing those
least able to afford it" quote (NPR, s8); Aparna Sridhar, Deputy General
Counsel, Anthropic and "Training AI on books is fair use under copyright law" /
"more than 91% ... claimed their share" (NPR, s11); Maria Pallante, President
and CEO, AAP and "abhorrent conduct that should never be normalized" / "an
important victory in the larger battle" (AAP release, s9, confirmed by direct
fetch after a bot 403). Lemley (Stanford) and Casey, Brauneis (GWU), Peterson
(Anthropic's economist), Malackowski (plaintiffs' economist), and a16z all sit
where the evidence places them. Every one of the 13 hrefs resolves as printed;
s12's ssrn.com issues a same-host 301 to www.ssrn.com and lands on the correct
"Fair Learning" abstract.

Three breaks, each addressed:

- The dek made a factual claim the record does not support. It said the $3
billion Concord II suit "is now pressing the settlement's roughly
$3,000-per-work piracy price as the rate the whole training-data economy should
pay." Concord II seeks more than $3 billion over roughly 21,000 works — on the
order of $143,000 per work, near the willful ceiling — and is itself a
torrenting/piracy suit whose training and torrenting claims Anthropic did not
even move to dismiss (confirmed via s5). It is not an effort to set $3,000 as an
industry rate; the dek inverted the figure and misassigned the purpose. Because
this is display text reaching every reader, I rewrote the dek (see Edits).

- The compensation side claimed the settlement order "names that exposure
directly: continued litigation carried 'the possibility of an adverse ruling'
on willfulness." Reading the order at page 12, that quote sits in the
final-approval fairness analysis as a generic litigation risk ("the possibility
of an adverse ruling, years of appeals, and changes in a defendant's financial
position"), framing the class's risk of pressing on — not the order naming
Anthropic's willful exposure. The evidence record carried the same "on
willfulness" gloss, but the source I opened does not bear it. The willful-exposure
point already stands on the prior sentence (17 U.S.C. § 504 plus Alsup's order
for a trial "including for willfulness"), so I cut the overstated sentence.

- The Lemley and Casey quotation was not verbatim. The article printed "license
all the underlying works for the new use" inside quotation marks; the original
(confirmed against the Stanford full text and the Copyright Office's own
quotation) reads "license all the underlying photographs or texts for the new
use." I bracketed the substituted word to "[works]," the standard fidelity
signal the evidence record itself used.

One sourcing gap I cannot close by editing: the orientation says the report
"was issued as a 'pre-publication version' in May 2025, within days of the
Register of Copyrights who signed it leaving the post," citing s6. The report
(s6) supports the pre-publication-May-2025 half but cannot establish the
Register's post-release removal, and no source documenting that removal appears
in the article's list. The removal is exactly the contested-standing context the
commission and brief want kept, so the fix is a source, not a cut. Routed to the
researcher.

## Cut

Two direct removals and one bracket (all logged under Edits). The slop pass ran
clean beyond those. I tested each edge sentence in isolation. The orientation
opener "The number is bigger than the question it answers" survives the
placeholder test — it carries the piece's actual claim, that the settlement's
size exceeds the legal scope it resolved. The section closers earn their place:
the orientation ends on the priced contested question in concrete figures, and
the body ends on the incumbency argument ("payable only by whoever already has
$1.5 billion to spend on one"), a conclusion the argument built rather than a
signpost. The one "not X, it is Y" construction in house voice — "not whether
training on lawfully acquired work is fair use ... It is whether the price ..."
— corrects a real, named misconception (the coverage that flattens this to
authors-versus-robots), so it is an earned contrast, not the reflex. The
"not just transformative, it is highly transformative" is a direct quotation and
exempt. No self-reference, no vague attribution, no decorative-copula tells, no
puffery beyond the court's own sourced "largest on record." Em-dash and lexical
counts were within the merged limit on the writer's proof and my edits add none.
No prompt leakage: the framing sentences restate the brief's live question in
the piece's own sourced terms, not its clause order.

## Reader

As the declared reader I finish with something no single source gives: the
factor-by-factor structure of one fight, assembled into a table and two
steelmanned positions around a sharpened pricing question. That is the draft's
stated original work — turning Alsup's split into the spine and organizing
scattered quotes into two camps — and it survives the read. The prose sits
closer to the voice-guide exemplars than to a median summary: named voices do
the arguing (Rasenberger, Sridhar, Brauneis, Lemley and Casey, Peterson), the
house voice hedges at the seam ("One judge has already answered that," not
"settled law"), and neither side's account is rounded up into a verdict. The
headline is the largest claim, and it states a sourced legal fact — the release
does not reach the training ruling — rather than grading the contested pricing
question; I scrutinized it for tilt and kept it.

## Edits

- Rewrote the dek (visible dekline and the nb-meta dek field, kept identical) to
  drop the inaccurate claim that Concord II is pressing the $3,000 piracy price
  as an industry rate, and to state the contested pricing question with both
  poles.
- Cut the compensation-side sentence "The settlement's own reasoning names that
  exposure directly: continued litigation carried 'the possibility of an adverse
  ruling' on willfulness." and its s1 pp. 11-12 citation; the source does not tie
  that quote to willful exposure, and the point is carried by the preceding
  sentence.
- Bracketed the Lemley and Casey quotation from "the underlying works" to "the
  underlying [works]" to match the original ("photographs or texts").

## Required work

- researcher: Supply one citable contemporaneous source establishing that
  Register of Copyrights Shira Perlmutter was removed from her post and its
  timing relative to the May 2025 release of the Part 3 report, so the
  orientation's removal-sequence clause rests on a source that can support it
  (it currently cites s6, the report, which cannot). Preserve the
  contested-standing context; do not cut it.
- writer: Attach the new removal source to the orientation clause (and tighten
  "within days" to "the next day" only if the source supports that timing), then
  re-run the proof with links included after this review's direct edits and the
  new citation. Minor, non-blocking: the Concord II motion was filed on or about
  August 3, 2026 per s5, while the piece says "On August 5-6, 2026, Anthropic
  moved to dismiss"; consider "in early August 2026" if you touch the sentence.

## Decision

revise — the article is accurate, neutral, and structurally sound after my
edits, but the orientation's Register-removal claim is cited to a source that
cannot establish it and needs a real citation the researcher must supply.
