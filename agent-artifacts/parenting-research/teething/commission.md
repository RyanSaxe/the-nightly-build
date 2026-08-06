# Commission: parenting-research/teething

## Authorized work
Scheduled duty for 2026-08-06 returned `parenting-research` as an open section:
choose a topic within the beat, do not repeat a published slug. This run
commissions exactly one parenting-research article.

## Subject and question
The desk follows a child born February 2026, so ~6 months old on 2026-08-06 —
the stage when the first teeth typically erupt and teething becomes a live
household concern. Topic: **infant teething — what the evidence shows it does
and does not cause, and the safety record of the relief measures parents reach
for.**

Two questions strong evidence can actually change a family decision on:
1. What symptoms are attributable to teething? High-quality prospective/cohort
   work (e.g. Macknin; the 2016 Pediatrics systematic review, Massignan et al.)
   ties teething to mild signs (drooling, gum irritation, low-grade temperature
   elevation) and specifically does NOT support blaming high fever, diarrhea,
   or serious illness on teething — a misattribution that can delay care.
2. What relief is safe? The documented safety record: the FDA's warnings and
   actions on benzocaine oral gels (methemoglobinemia; 2018 action) and on
   homeopathic teething tablets/gels containing belladonna (2016-2017 FDA
   warnings and Hyland's withdrawal). Contrast with low-risk measures
   (a chilled — not frozen — teether, gum massage, and evidence on weight-based
   acetaminophen only where a clinician indicates it).

The desk covers research, not generic advice: explain what the evidence
supports, how strongly, and what it cannot establish (study design, confounding
of a developmental stage with coincidental illness, normal variation). End with
what the evidence might change at home and where a symptom is a safety matter
requiring a pediatrician. The desk does not stand in for individual medical care.

## Template and geometry
Template `article` (longread). Series word band 1200-3000. Flex sections 2-6.
Cite rule per-section. Use furniture where evidence has a shape prose would hide
(e.g. a table separating teething-attributable from not-attributable symptoms,
or the regulatory timeline). Furniture carries evidence, not decoration.

## Sources
Source floor: min 8 (template article default). Primaries: the FDA safety
communications (fda.gov) on benzocaine and on belladonna teething products; the
peer-reviewed studies/systematic reviews on teething signs (Pediatrics; the
original Macknin cohort); AAP/authoritative clinical guidance for the home and
safety framing. Contested figures need the primary. Read the study, not the
press write-up, for what each design can and cannot establish.

## Production policy (resolved via `nb production-policy`)
- writing-coach: model capable, effort low
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model inherit, effort high, REQUIRED

Actual harness: roles run as isolated Claude subagents on model
`claude-opus-4-8` (capable tier; required editor "inherit" resolves to this
correspondent model). Deviation recorded: this runtime's subagent launcher does
not expose a per-invocation reasoning-effort control, so the required editor
"high effort" is approximated by the most capable available model at the harness
default effort. No model was traded down.

## Neighboring articles this run
company-analysis/eli-lilly, paper-of-the-day/instructgpt,
word-of-the-day/luddite, current-events/2026-08-06, tech-news/2026-08-06.
This is the edition's evidence-and-health longread for a lay-but-rigorous frame.

## Recent parenting-research coverage and habits not to inherit
Recent slugs: infant-vitamin-d, infant-iron, nirsevimab, sleep-training,
early-allergen-introduction, starting-solids (mostly nutrition and one shot).
Teething is a fresh domain (symptom attribution + drug/product safety).
Habits to break, not to copy:
- Recent openers state the trial's bottom line as the first sentence ("Iron
  reliably reverses developmental delay once anemic, but..."; "Higher vitamin D
  doses gave more in the blood and no more in the bone"). The headlines guide
  bans the hedged-contrast/"X not Y" dek mold and the comma-triad dek; recent
  deks lean on that "does one thing, not the other" shape — do not reuse it.
- Recent outlines end with a "Home choices / Back to the dropper" closer and a
  positions/guidelines-diverge section (nb-position). Use the safety+home
  framing the series requires, but do not copy the "where AAP and ESPGHAN part
  ways" section shape or the "back to the [object]" closer.
Required furniture and the Sources section are not habits to avoid.

## Original contribution expected
Separate, on the evidence, what teething actually causes from what gets blamed
on it, and turn the drug-safety record into a clear decision rule for a
6-month-old's household — including the symptoms that mean "not teething, call
the pediatrician." Not a listicle of remedies.
