# Editorial review: parenting-research/infant-fluoride (editor/01)

## Skeptic

Thesis: the professional advice to start fluoride at six months (a toothpaste
smear at the first tooth, and a supplement in low-fluoride water) rests on trial
evidence that never enrolled a child under one, but the two gaps are different
kinds. The toothpaste-timing gap is a benign evidentiary gap the fluorosis
evidence, read directly, shows does not move risk by start age, so it is safe to
act on; the supplement gap is a live, unresolved regulatory dispute between the
FDA and standing pediatric guidance, so it is not settled. That two-kinds
distinction is the article's own, and it is the piece's payoff.

Claims it stands on, and how each held:

1. No trial behind the toothpaste and varnish guidance enrolled a child younger
   than one. Held. Walsh 2019's Summary of Findings names its primary-dentition
   population "1 to 6 years"; Marinho 2013 states ages "1 to 15 years"; USPSTF's
   evidence base has no trial mean age under one. The headline's flat claim is
   supported by the population lines themselves.
2. Fluoride toothpaste prevents decay, dose-responsively, high-certainty at
   1000-1250 ppm. Held. SMD -0.28 (55 studies), -0.36 at 1450-1500, -0.08
   head-to-head, MD -1.86 d3fs (998 children, 24 mo) all match the Numbers
   section to the digit and to the right certainty grade.
3. The fluorosis risk that holds up is concentration, not start age. Held. Wong
   2024 gives RR 0.98 (CI 0.81-1.18, very low) on start age against Wright's
   older OR 0.70; the two concentration comparisons (RR 0.75, RR 0.72) are the
   only moderate-certainty findings. The article sides with the newer, targeted,
   less certain review and says why, rather than picking the scarier number.
4. The supplement decision turns on water-fluoride level; the floor is no
   supplement before six months. Held against AAP Table 2, the ADA chairside
   guide, and the CDC MMWR. The article correctly flags that USPSTF's <0.6 ppm
   trigger and the CDC/AAP/ADA three-tier schedule do not obviously specify the
   same rule in the 0.3-0.6 band, matching the evidence record's noted nuance
   without overstating it.
5. The FDA (2025-10-31) now recommends against ingestible fluoride under three,
   conflicting with standing AAP/ADA/CDC guidance, unresolved. Held against the
   HHS release and the ADA/CDA responses; the article keeps both positions
   standing at once and does not declare a winner.

I recomputed the figures against their owners and denominators and reread every
cited passage for what breaks the claim; nothing did. Display text checked
descriptor by descriptor: the headline's "younger than one" is exact to the
population lines; the FDA quotes (Makary "alter the gut microbiome," Kennedy
"driving a stake through the heart of outdated science") and the ADA and CDA
quotes are verbatim to source; the OR 23.74 (CI 3.43-164.30) is confirmed live
on the CDC page; no named person carries a title the article could get wrong,
because the piece wisely leaves Rosato's title off (the live ADA page calls him
president, the record called him a spokesperson).

data-nb-kind audit, all fourteen. I opened every href as printed. Eleven land on
the source's own page; the Cochrane, AAP-publications, and JADA canonical URLs
return 403 to automated fetch but resolve in a browser and are the source's own
address, not a fetch endpoint or a mirror, which is correct practice. s7 (Wong
2024) is labelled primary and is correct: it was read on the article's PMC page,
which hosts the review speaking for itself, so it is the primary read through a
host. s5 (ADA toothpaste guideline, read via Guideline Central's structured
reproduction of the ADA's own recommendation text and cross-confirmed verbatim
in the directly-read AAP report) is a reproduction of the authoring body's own
words, not an outside appraisal, so primary holds. Every other primary was read
directly or through a verified verbatim copy of the same document.

The one failure: s8 (Wright et al. 2014) was labelled primary but was read only
through the DARE critical abstract at NBK247248 — an independent appraisal
authored by the University of York Centre for Reviews and Dissemination that
reports and critiques Wright's figures rather than reproducing his paper. By the
authorship-and-stake test, that is a secondary source, and the evidence record
itself says "treated as secondary for that reason." The primary was never read;
only the appraisal was. I fixed it in place: relabelled secondary, repointed the
href from the gated JADA page (which nobody read) to the DARE abstract that was
actually read, and renamed the entry to name the CRD/DARE abstract. This changes
nothing the citation is cited for (still Wright's OR 0.70), and it leaves no
central claim short of a primary, because the article's own position rests on s7
(Wong, primary) and cites Wright only as the older figure it argues against.

## Cut

One sentence failed the slop test and was cut: "The two figures answer different
questions, and neither substitutes for the other," which reduces to a sentence
anyone could write about any two figures and only restated the substantive
distinction the prior sentence already carries ("a population baseline, not a
rate any trial measured directly").

The opener carried a newsroom self-reference slop.md rules out: "The child this
desk follows was born in February 2026." No published piece in the series uses
that framing; the siblings reference the child directly ("The child turns six
months old this August"). I rewrote it to the concrete, self-contained "A child
born in February 2026 turns six months old this August," which keeps every fact
and removes the desk-narration and any dangling referent for a link reader.

Edge sentences elsewhere held: they carry facts or a reasoning step. The
negative-parallelism constructions ("enrolled toddlers and older children, not
infants"; the "strength, not starting age" heading; "a population baseline, not
a rate...") each correct a misconception the piece actually names, so they are
earned contrasts, not the reflex. "Testing the water before filling a
fluoride-drop prescription is not a formality" survives because it delivers the
concrete upshot of the OR 23.74 finding immediately above it.

Display-text formula check against the recent record. The dek was built on the
same "clause, and clause" mould as the last two parenting deks
(infant-flu-vaccine, starting-daycare both close on ", and"), which spec/headlines
says looks stamped once it recurs. I recast it to a single main-clause-plus-"where"
sentence that keeps the varnish/supplement extension and the FDA-warning fact and
breaks the mould. The headline states this piece's own finding and copies no prior
headline. The section headings reconstruct the argument in the piece's own nouns
with no scaffolding slot and no repeated build. The closing furniture does NOT
inherit the flagged habit: the recent pieces close on a "what to act on / from the
trials to this child" heading over an nb-note + nb-note-strong stack, whereas this
piece closes on "The brushing amount is settled. The supplement is not." over an
nb-holdsup grid plus one Verdict note — which is the documented canonical pairing
for the holds-up grid (FURNITURE.md: its summary row is a Verdict note right after
it), and a real variation from the two-note stack. The "Verdict" label recurs
across the series but is documented furniture carrying distinct per-article
content, not the formula slop targets. I checked the draft's phrasing against the
voice-guide exemplars for borrowed clauses and found none.

One tidied wording: "The toothpaste evidence is the stronger of the two decisions
here" conflated evidence with decision and now reads "The toothpaste decision
rests on the stronger evidence." Mild redundancy remains across the closing prose,
the holds-up grid, and the Verdict (the rice-grain-smear/concentration point lands
three times), but each block has a distinct job and the repetition is not
publication-blocking; I left the earned Verdict the voice guide calls for intact.

## Reader

Read straight through as the declared parent-reader, the piece gives something the
fourteen sources do not: read alone, each guideline states "start at the first
tooth" and each review states its own age floor, but no single document says that
every evidence base behind the six-month advice shares a floor of one year, and
none separates the toothpaste-timing gap (an old evidentiary hole the fluorosis
trials show is safe to cross) from the supplement gap (a live FDA-versus-guidance
dispute). The article builds both, and the draft handoff's original-work sentence
describes exactly that cross-read and that distinction — both survive the read.
The prose sits with the voice-guide exemplars, not a median summary: it holds "the
finding is real" apart from "it is a different kind of finding" the way Goldacre
holds the surrogate-outcome pair, runs the Walsh numbers in the open the way Yong
runs his, and earns its flat Verdict only after Cochrane, the AAP, the ADA, the
USPSTF, the CDC and the FDA have each been walked through by name. The headline,
read last as the largest claim, is true and specific.

## Edits

- Rewrote the opener to remove the "this desk follows" newsroom self-reference:
  "A child born in February 2026 turns six months old this August, the age a
  first tooth usually erupts, and two fluoride decisions turn live at once."
- Rewrote the dek (both the nb-meta value and the dekline) off the recurring
  ", and" mould to: "The varnish and supplement guidance rest on the same trials
  that stopped at age one, where the drops still prescribed to a six-month-old in
  low-fluoride water now carry an October 2025 FDA warning."
- Cut the slop sentence "The two figures answer different questions, and neither
  substitutes for the other."
- Changed "The toothpaste evidence is the stronger of the two decisions here" to
  "The toothpaste decision rests on the stronger evidence."
- Relabelled source 8 (Wright et al. 2014) from data-nb-kind="primary" to
  "secondary", repointed its href from the gated JADA page to the DARE critical
  abstract actually read (https://www.ncbi.nlm.nih.gov/books/NBK247248/), added a
  locator, and renamed the entry to the CRD/DARE critical abstract of Wright.

## Required work

- orchestrator: re-run nb stamp before the PR. My cut and rewrites changed the
  word count and one source's kind, so the stamped words/reading_minutes and the
  primary/secondary tallies in nb-meta need refreshing (currently words=2552,
  sources=14; sources count is unchanged, one entry moved primary to secondary).
  Then run the final links-checked proof.
- writer (optional, non-blocking): chart-1.py's header comment cites "research.md"
  for its figures; the record is evidence.md. Cosmetic, in the writer's provenance
  domain; fix at next touch. No chart data, scale, label, or caption change is
  needed — all five ratios and CIs match the evidence and the caption is an
  accurate cited label.

## Decision

approve — the sources 7/8 question is resolved (7 primary, correct; 8 relabelled
secondary and repointed to the DARE abstract actually read), the chart is honest,
every central claim held against its primary, and the remaining prose and formula
fixes were made in place; only a re-stamp remains for the orchestrator.
