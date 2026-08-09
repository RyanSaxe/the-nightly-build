# Editorial review: parenting-research/starting-daycare (editor/01)

## Skeptic

Thesis: the daycare research settles one thing that should change a household's
planning, the front-loaded run of respiratory and ear infections, and cannot
settle the two medium-term questions parents actually worry about, asthma and
development. The piece stands on four load-bearing claims: (1) early group care
raises respiratory and ear infections for the first two years and then reverses
below home care; (2) the gastrointestinal half of that near-term story is small
and nets to zero over six years; (3) the famous asthma protection does not
survive the larger cohorts and what replicates is a wheeze timing-shift, not a
durable asthma change; (4) the developmental effects are real, tiny, and
inseparable from family selection because no tier is randomized.

I recomputed every figure against its owning primary and opened all nine hrefs.

- Claim 1 holds. Côté respiratory 1.61 early / 0.79 later and ear 1.62 / 0.57
  match the primary exactly; the "sixteen infections for every ten" gloss is a
  correct read of 1.61, and "six ear infections for every ten" is a correct read
  of 0.57. The de Hoog table row (1.40 early, 0.85 at 5-6) matches. Verified on
  the live JAMA and de Hoog pages.
- Claim 2 holds and follows the evidence's correction. First-year AGE IRR 1.13
  and the six-year 12.2 vs 13.3 per 100 child-years both confirmed on the source
  page; Côté's null GI effect is stated. The older "threefold" review figure is
  named and set against the prospective cohort, then rejected. No large,
  near-certain GI claim survives. The de Hoog healthcare-use caveat (episodes
  offset at IRR 1.08 NS, but GP consultations 1.15, referral HR 1.43, 1.89 for
  6-12 month entrants) is carried accurately.
- Claim 3 holds. Ball RR 0.4 (CI touching 1.0), 0.8, 1.4, 0.8, 0.3 all match;
  the piece steelmans Tucson first, then weighs Caudri aOR 0.99 (with 0.86 and
  0.80) and Swartz (0.66 at 3-5, 0.98 NS at 6-18, 1.80/0.43 wheeze flip, 1.17
  any-care) over it. The "immune-training story is the part that did not hold"
  reading is correct and does not drift back to "maybe less later asthma."
- Claim 4 holds. d = .08 to .16 and the "point and a half on an IQ-type scale"
  gloss are correct (0.10 SD x 15 = 1.5 points). The correlational caveat is
  stated in prose and in the note.

Randomized-vs-observational line: marked three times (orientation, asthma
section close, and the dedicated note), plus the family-selection confounder in
each. Good.

Two breaks, both in the citation apparatus, found by opening every href against
its printed label. These are display-text/sourcing failures, the costliest kind,
and they route out because they live in the source markup and (for one) turn on
which primary is intended:

- **s2 journal wrong.** The href (PMC4098954) resolves to de Hoog et al.,
  *BMC Medicine* 2014 (the WHISTLER healthcare-use paper). The printed source
  reads "Pediatrics · ... (2014)" with `data-nb-locator="Pediatrics 2014"`. The
  study identity and all figures are right; the journal name is wrong. The
  evidence record carries the same "Pediatrics 2014" error.
- **s3 author and journal wrong.** The href (pubmed 27244798) resolves to
  **Hullegie et al., *Pediatrics* 2016;137(5)** ("First-year Daycare and
  Incidence of Acute Gastroenteritis"). The printed source reads "Pediatric
  Infectious Disease Journal · Enserink, de Hoog et al." The figures (IRR 1.13;
  12.2 vs 13.3; the "advances the timing... persists to age 6" quote) are all
  confirmed on that page, so the content is sound and the URL is right; the lead
  author and the journal are wrong. The evidence record carries the same error.
- **s8 links to the wrong paper, and the body inherits the error.** The href
  (PMC5115787) resolves to **Vandell et al., *Developmental Psychology* 2016**,
  "Early Child Care and Adolescent Functioning at the End of High School" (mean
  age 18.3, n=1,214), not the age-15 / *Child Development* 2010 paper the label
  names. The body's "At age 15 both threads persisted" is therefore attached to
  a source that measures the end of high school, not age 15. The cited figures
  (d = .08 to .16; the correlational caveat) do appear in the linked 2016 paper,
  so the numbers hold, but the citation is internally inconsistent: label, year,
  journal, and the body's stated age all disagree with the paper the link opens.

The remaining hrefs land on their sources: s1 (Côté, JAMA Peds 2010), s4 (Ball,
NEJM 2000 via the resolving PubMed abstract, used because NEJM itself 403s), s5
(Caudri, AJRCCM 2009), s7 (Belsky, Child Development 2007, gated but correct).
s6 (Swartz escholarship PDF) returns the document itself (binary, so I could not
read it as a reader, but the four pooled ORs match the record and the chart). s9
(AAP bronchiolitis CPG) 403s to an automated fetch but is the guideline's own
canonical publisher page and serves human readers; the researcher read the full
text from a mirror. I accept s9 as landing on the source, and note the 403 only
so a later check does not read it as a dead link.

`data-nb-kind` audit: all nine are labeled `primary`, and every kind is
defensible for how the claim is used (Côté/de Hoog/Hullegie own their cohort
ratios; Ball/Caudri own theirs; Swartz is primary for the pooled estimates it
computes; Belsky/Vandell own their longitudinal findings; the AAP is the
authoring body of its guideline). The failures above are in the human-readable
identity, not the kind flag.

One unsupported claim cut. The close carried "Group care raises exposure to
respiratory syncytial virus, which a healthy infant can now be protected against
with a single antibody dose" — an uncited medical claim absent from the evidence
record, wrapped in self-reference ("worth naming and not re-arguing here"). It
is nonessential and carries no citation, so I cut it (see Edits).

## Cut

Ran the slop pass over every sentence including display text and the caption,
note, and verdict furniture. The piece is disciplined: no vague attribution, no
puffery, no decorative-analysis trailing clauses, no empty conclusions. The
concretizations that could have gone generic instead commit ("a coin's worth of
difference from no effect," "a gap narrower than the wobble between two ordinary
years," "about a point and a half" on an IQ scale) and each is tied to this
subject, so they pass the slop test rather than fail it.

Negative parallelism is present but earned. The piece's whole argument is a set
of corrections, so the "wheeze changes in timing, not in total" and "not a
durable change in whether they end up with asthma" contrasts correct real, named
misconceptions and stay. "One caveat sharpens the reassurance rather than
dissolving it" is the one reflex contrast that leans on the voice guide's own
framing; it does orient a real caveat that the next two sentences pay off with
data, so I left it, but it is the closest call in the piece.

Self-reference: cut where it added nothing. "not re-arguing here" went with the
uncited RSV sentence. "What this piece will not do is issue a blanket
instruction..." was piece-self-narration; I recast the sentence to state the
fact directly ("No accessible pediatric guideline issues a blanket
instruction..."), which also keeps correction #3 intact. "this desk can supply"
I left: "the desk" is the series' established voice, and the recent-pattern note
directs keeping the clinician close.

Prompt-leakage check against the writer brief: the corrected findings the brief
specified appear as sourced conclusions, not as planning labels or "assignment
fulfilled" claims. "The honest near-term claim is..." echoes the brief's wording
but states the article's own synthesized verdict on the tier, so it reads as
conclusion, not instruction; left.

Reflex punctuation repaired. Three semicolons where a period does the job,
consistent with the editorial direction's punctuation standard: the GI-claim
sentence, the asthma "honest test" sentence, and the table caption. No em-dashes
in the body to repair. The two intentionally-retained density warnings (the
d = 0.10 IQ-scale comparison and the AAP hand-hygiene/breastfeeding
recommendation) each carry a single thought with a data appositive; splitting
either would break the comparison or the paired recommendation, so both hold
under the standard's allowance for a long sentence under control.

Headline, dek, and headings checked against the recent-pattern notes. The
opener does not use the "the dangerous part of X is Y" reversal mold. The dek is
two coordinated claims, not the banned three-clause comma-and-"and" triad, and
commits to the finding rather than grading the selection. The five headings are
concrete argument steps; one uses the comma-and-"and" join ("The developmental
effects are small, and the design cannot separate care from family"), but it is
a single instance among varied constructions and I have no recent-record
evidence it is a house formula, so I left it rather than introduce a late
standard.

Chart and furniture. The forest plot's committed provenance (chart-1.py, plotly,
Swartz Tables 3-4) matches the evidence record value-for-value: wheeze <2 1.80
(1.38-2.36), asthma 3-5 0.66 (0.50-0.87), asthma 6-18 0.98 (0.66-1.47), wheeze
6-18 0.43 (0.27-0.68). Read as a reader, the image is honest: log scale declared
in caption and alt text, a dotted 1.0 line, "fewer"/"more" placed correctly, and
whiskers that show asthma 3-5 entirely below 1, asthma 6-18 crossing 1, and the
wheeze rows on opposite sides. The alt text describes exactly what the plot
shows. The caption is a factual cited label with the interpretation kept honest
and the `data-nb-locator="Tables 3 and 4"` correct. The infection table's three
rows all match their primaries. No furniture reads as decoration or a stacked
block; the note and verdict each carry reasoning the prose needs.

## Reader

What the piece gives that the sources alone would not: a single decision axis,
"does this finding change whether or when to enroll?", laid across three tiers
of very different evidential weight, so that a quantitatively literate parent can
see that only the infection tier clears the bar and the choice returns to
logistics and room quality. That is the original-work sentence in the handoff,
and it survives the read: the piece does the ranking, not a restatement of nine
studies. The prose sits closer to the voice-guide exemplars than to a median
summary. It follows Carroll's discipline of attaching a concrete bound to each
number, Nuzzo's move of putting a real-but-small effect on a scale the reader
can picture, and Gawande's habit of doing the arithmetic before the verdict. The
headline reads as the largest claim the piece defends and delivers it.

## Edits

- Cut the uncited RSV-antibody sentence ("Group care raises exposure to
  respiratory syncytial virus, which a healthy infant can now be protected
  against with a single antibody dose, so the added exposure is worth naming and
  not re-arguing here.") from the closing section: an uncited medical claim plus
  self-reference.
- Recast the final close sentence from "What this piece will not do is issue a
  blanket instruction to keep high-risk infants out of daycare in RSV season: no
  accessible pediatric guideline states one, and..." to "No accessible pediatric
  guideline issues a blanket instruction to keep high-risk infants out of daycare
  during respiratory syncytial virus (RSV) season, and..." — removes the
  self-narration, keeps correction #3, and now defines RSV where it first appears
  (the definition had lived only in the sentence just cut).
- Changed a reflex semicolon to a period in the GI paragraph ("...narrowing
  later. The stomach bugs...").
- Changed a reflex semicolon to a period in the asthma paragraph ("...for almost
  any belief. The larger cohort...").
- Changed a reflex semicolon to a period in the infection-table caption
  ("...below 1.0 is fewer. Every ratio is adjusted.").
- Ran `nb stamp`: words 2341 -> 2302, sources 9, reading_minutes 10.

## Required work

- **researcher:** Reconcile three source-identity errors in the evidence record
  so the writer has correct metadata to print.
  - s2: the de Hoog WHISTLER healthcare-use paper at PMC4098954 is *BMC
    Medicine* 2014 (12:107), not *Pediatrics* 2014. Correct the journal.
  - s3: the paper at pubmed 27244798 is **Hullegie et al., *Pediatrics*
    2016;137(5)**, not "Enserink, de Hoog et al., *Pediatr Infect Dis J*."
    Correct the lead author and the journal. The URL and figures are right.
  - s8: PMC5115787 resolves to **Vandell et al., *Developmental Psychology*
    2016** (end of high school, mean age ~18.3), not the age-15 / *Child
    Development* 2010 paper the record names. Decide the owning primary: either
    (a) keep this URL and correct the label to the 2016 EOHS paper (and the body
    must stop saying "age 15"), or (b) supply the URL for the actual Vandell 2010
    *Child Development* age-15 paper if that is the intended source. Give the
    writer one correct URL + journal + year + the age the figures attach to.
- **writer:** After the evidence is corrected, update the printed source entries
  (anchor text and `data-nb-locator`) for s2, s3, and s8 to match, and fix the
  body sentence "At age 15 both threads persisted" to the age the corrected s8
  source actually reports. Re-run `nb stamp` and the exact `nb check` to BLOCK: 0.

## Decision

revise — the content, arithmetic, chart, and the three evidence corrections all
hold, but three cited sources print the wrong journal or author and one href
opens a different paper than its label (and the body's "age 15") names; those are
sourcing/display-text failures that route to the researcher and writer to fix.
