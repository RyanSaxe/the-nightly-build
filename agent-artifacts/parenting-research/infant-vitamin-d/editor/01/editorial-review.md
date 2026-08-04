# Editorial review: parenting-research/infant-vitamin-d (editor/01)

## Skeptic

Thesis, stated from the draft alone: higher vitamin D doses raise a breastfed
infant's blood level but buy nothing above it, so once the standard 50 nmol/L
adequacy threshold is granted the entire higher-dose and broader-benefit case
collapses to the 400 IU result, leaving deficiency prevention as the drops'
only warrant. The headline and dek carry that claim without overreaching.

The load-bearing claims and how each held:

1. **Breastmilk is low in vitamin D; 400 IU holds 25(OH)D above 50 nmol/L, the
   IOM adequacy level.** Verified against AAP 2008 (under 25-78 IU/L; 200 IU
   held above 27.5 but not 50; 400 holds above 50) and IOM 2011 (20 ng/mL =
   50 nmol/L "for practically all individuals"). Conversions correct
   (27.5 nmol/L = 11 ng/mL). Holds.

2. **Higher doses give more 25(OH)D and no more of anything measured.** Tested
   each null at its own endpoint and population, and each is reported that way:
   Gallo age-3 (bone; healthy term), VIDI (bone strength pQCT + parent-reported
   infection; healthy, 95.7% sufficient at birth), Tuovinen (neurodevelopment;
   ASQ), Rueter (allergy; high-risk but sufficient at birth). The ASQ figures
   (1.17, 95% CI -0.06 to 2.38 at 12 mo; 0.48, -0.40 to 1.36 at 24 mo) match the
   Tuovinen primary exactly, opened firsthand. VIDI's ~12.5 ng/mL 24-month gap
   and "no additional benefit" match. Holds; no borrowed confidence between
   endpoints.

3. **The whole higher-dose case reduces to moving the target from 50 to 75
   nmol/L.** This is the spine, and it is the article's genuine synthesis, not
   infant-iron's "supplement-before-deficiency" shape or nirsevimab's
   relative-vs-absolute move. Confirmed the Gallo arms separate only against the
   75 line (400: 55%, 800: 81%, 1200: 92%, 1600: 97.5% at 75 nmol/L; all ~97% at
   50) and that 1600 IU exceeds the IOM 0-6 mo upper limit of 1,000 IU — stated
   in both the Fig. 1 caption and the threshold section. The 50-vs-75 spine
   holds and is load-bearing.

4. **The strong deficiency-prevention claim is honestly framed as resting on
   physiology + 25(OH)D surrogate + fifty-year cod-liver-oil experience, thin in
   RCT count because rickets is now rare.** Confirmed against Cochrane (19
   trials, 2,837 pairs; only 2 reported biochemical rickets; insufficient
   evidence on deficiency/bone health). The draft does not dress this as
   trial-proven; it says the strength is in the logic. The "uncommon" claim
   carries its denominator (2 of 19), so the voice guide's rate-for-adjective
   rule is met without importing an unverified rickets incidence figure (the
   writer's open question — no change needed; the current framing does not
   overstate).

**D-Wheeze scope wall:** verified it holds. Hibbs is 300 Black infants born
preterm (28-36 wks), sustained 400 IU vs a diet-limited strategy that withheld
once formula/fortifier supplied 200 IU; recurrent wheeze 31.1% vs 41.8%, RR 0.66
(0.47-0.94), all matching the primary opened firsthand. The labeled note walls it
to that population and reads it as support for the deficiency-prevention frame,
explicitly not as wheeze prevention for a healthy term breastfed infant and not
a case for a dose above 400 IU. No leak of the signal into the general claim.

**Display text:** headline is a defended finding (no colon subtitle, no adjective
triad). Dek adds the spine and the warrant without restating the headline and
without any banned mold (no comma triad, no semicolon reversal, no suspended
question); it makes a claim about the world, not a grade of the article's method.
Every subhead is an argument step in the piece's own nouns. Every number, dose,
threshold, study name, and date in the display text traces to its owning primary.

**data-nb-kind audit:** 9 primary / 2 secondary as claimed. Cochrane (s4) and
HealthyChildren (s11) are correctly secondary; the two guideline-owner documents
(AAP 2008, IOM), the two Gallo papers, VIDI results, Tuovinen, Rueter, Hibbs, and
Munns are the parties that own their claims and are correctly primary. No
mislabeled secondary hiding a missing independent source.

**Citation hrefs:** opened all 11. Nine resolve directly to the correct source
page and I confirmed title/authors/figures on each (Gallo 2013, Gallo 2016,
Tuovinen, Rueter, Hibbs, Cochrane, HealthyChildren, Munns/Karger, and the IOM
report-brief PDF, which downloads as the genuine National Academies document).
Two return HTTP 403 to the fetcher — s1 (publications.aap.org canonical article
page) and the s7 doi.org link, which correctly 302-redirects to the JAMA
Pediatrics article for that exact DOI. Both are the right addresses for their
sources, access-gated at the publisher, and the evidence record already documents
each as paywalled/mirror-read. Right address, not a broken link; no fix owed.

**Chart (Fig. 1):** inspected the committed `chart-1.py`. Plotted values
(reach_50 = 97/97/97/97; reach_75 = 55/81/92/97.5) match the evidence record and
the Gallo primary. Read as a reader: axes labeled, y-axis 0-100 and not truncated,
legend names both thresholds honestly, and the visual makes the point — every
dose clears 50, only 1600 clears 75 in nearly all. Honest.

**Strength table:** each study-type label is correct beside its endpoint —
25(OH)D status (RCTs of dose / Cochrane pooled), Rickets (physiology + consensus;
RCT base thin, 2 of 19), Later bone (RCT hard endpoint, Gallo age 3 / VIDI pQCT),
Respiratory infection (RCT, VIDI 1200 vs 400), Allergy (RCT vs placebo, Rueter),
Neurodevelopment (RCT, VIDI/Tuovinen). No study type overstated.

No claim broke. Nothing routed to the researcher.

## Cut

The worst tell was prompt leakage: the closing "The practical tail deserves the
same evidence-based calm as the main claim, not a softer register" is the voice
guide's Oster note ("the register does not change when the content turns
practical") written into the article as if it were reporting. It narrates the
piece's own register choice and adds no fact. Cut whole; the sentence before it
("a missed day is not a missed treatment of a disease, only a small gap in a
running average") already does the work and gives the paragraph a concrete close.

The other two cuts were method-narration/self-grading. "Here the honest grading
begins, because..." is a signpost describing where the piece is in its own
argument; removed, leaving the substantive claim ("The strong-sounding claim
rests on thinner trial evidence than its confidence suggests"). And the tail
"...and it is worth saying so plainly rather than dressing it as trial-proven"
grades the article's own candor on top of an already-made point; cut back to
"That is a case built on why rather than on a randomized count."

Sentence-density warnings: reviewed all three (the Gallo age-3 quote-plus-list,
the maternal 6,400 IU route, the four clinician-call situations). Each is a single
number- or quote-bearing sentence of the kind the voice guide licenses ("one
longer sentence that supplies the number"), each reads on first pass, and
splitting any would fragment its comparison or list. Kept all three.

Furniture reviewed and kept: the Fig. 1 chart earns its place (makes the 50-vs-75
separation visible in a way prose cannot), the strength table is analysis not
decoration, the D-Wheeze note is a necessary scope wall, and the Verdict block
earns emphasis by adding the falsification condition (a trial showing 75 buys a
hard outcome 50 does not) rather than merely restating the close. The two crisp
"not X, it is Y" openers ("not in the baby, it is in the milk"; "milk is not
defective") each correct a real, named misconception central to the piece and
carry the mechanism, so both clear the earned-contrast bar; left in place.

No repeated rhetorical shape across paragraph endings; headings do not fall into a
comma-and cadence. Punctuation clean (no em-dashes; the one semicolon in the
closing paragraph binds two genuinely tight clauses and is a legitimate rare use).

## Reader

Read straight through as a research-literate parent: what I have that the sources
alone would not give me is the reduction of a sprawling supplement debate to a
single contested blood threshold, and the demonstration — via the dose chart and
the endpoint table read together — that granting the standard 50 nmol/L line
retires every higher-dose and broader-benefit argument at once, so the drops are
warranted by deficiency prevention and nothing else. That matches the
original-work sentence in the handoff, and it survives the read. The prose sits
closer to the voice-guide exemplars (Carroll's arm-by-arm nulls, Oster's
mechanism-before-recommendation, Gid MK's population walls) than to a median
summary: evidence type and endpoint ride on each strength claim, and the nulls are
reported in bare figures. The headline, reread as the largest claim, is one the
body defends.

## Edits

- Cut method-signpost "Here the honest grading begins, because" opening the
  narrow-case caveat; sentence now begins "The strong-sounding claim rests on...".
- Cut self-grading tail "and it is worth saying so plainly rather than dressing it
  as trial-proven"; sentence ends at "a case built on why rather than on a
  randomized count."
- Cut prompt-leakage sentence "The practical tail deserves the same evidence-based
  calm as the main claim, not a softer register" from the closing section.
- Ran `nb stamp`: words 2310, reading_minutes 10, sources 11.

## Required work

None. No researcher, writer, or orchestrator item remains; the cuts were made
directly and the proof is the writer's to re-run.

## Decision

approve — every number, threshold, href, and data-nb-kind checks against its
owning primary, the 50-vs-75 spine and the D-Wheeze scope wall hold, and the only
defects (two self-grading signposts and one voice-guide leak) were surgically cut.
