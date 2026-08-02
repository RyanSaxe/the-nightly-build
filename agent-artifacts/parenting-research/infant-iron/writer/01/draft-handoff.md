# Writer handoff: parenting-research/infant-iron (01)

## Original work

The evidence record states the Chilean trial's cognitive/visual-motor harm
signal (sources 6, 8), its social-emotional benefit signal (source 7), and
the guidance-body split (sources 1-2, 9-16) as separate entries. The
article's original work is threading those into one argument: that the
*sign* of iron-fortified formula's effect on a healthy six-month-old flips
with baseline hemoglobin status and with which outcome domain is measured,
not a single verdict of "helps" or "harms" — made visible by a purpose-built
chart isolating the three-subgroup sign flip, explicit weighing of the
cognitive-harm vs. adaptive-behavior finding against each other rather than
picking one (the "Verdict" note), and a closing distinction the evidence
itself supports but no single source states outright: what the Chilean
trial actually randomized was a measured formula dose, not food, so the
piece separates "offer iron-rich food" (broadly agreed across AAP, WHO,
CDC, USDA) from "add a supplement" (where guidance genuinely diverges)
instead of repeating any one guideline body's recommendation as the
takeaway.

## Paths changed

- Article: `/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html`
  (edited the initialized skeleton; skeleton chrome, required sections, and
  `nb-meta` shape preserved).
- Chart provenance:
  `/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron/chart-1.py`
  and its rendered
  `/home/user/the-nightly-build/.nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron/chart-1.png`
  — the Lozoff 2012 10-year subgroup sign-flip (whole sample, high-Hb
  iron-replete, low-Hb), built only from the evidence record's verified
  point-difference and effect-size ranges (source 6), all three subgroups
  kept together per the brief, colors assigned by direction (neutral for
  whole sample, the press theme's `--chart-4` red for the harm subgroup,
  `--chart-3` teal for the benefit subgroup) rather than default cycling,
  since direction is the chart's entire point. Inspected the rendered PNG
  and the built preview page before finalizing.
- `draft-handoff.md` (this file).

## Proof result

`nb check .../infant-iron.html --series parenting-research --library
/home/user/library` → **BLOCK: 0, WARN: 0**, verdict PUBLISHABLE. An
earlier pass surfaced 13 `W-SENTENCE-DENSITY` warnings; all were fixed by
splitting the flagged sentences (verified against the exact sentences the
prose checker flagged, not by guesswork) rather than left standing, since
short single-purpose sentences are both the house floor's rule and the
voice guide's explicit instruction to give each evidentiary claim its own
sentence. No warnings remain to record as intentionally kept.

Also inspected via `nb preview` + a full-page render: header, both flex
figures (chart and comparison table), the Verdict note, and the sources
list all render correctly in the site chrome; no layout issues.

15 sources cited (floor is 8), 14 primary / 1 secondary (the USDA Dietary
Guidelines committee's finding is cited via its PMC secondary explainer,
per the evidence record's own split classification of that entry — the
primary DGA PDF could not be read this session). 2,875 words (band
1200-3000).

## Evidence caveats honored

- The Chilean trial is reported as a mixed, domain-dependent,
  baseline-status-dependent pattern (harm on cognition/visual-motor in the
  iron-replete subgroup, benefit on adaptive behavior across the sample),
  never as unqualified "harm" — both findings get their own section and the
  Verdict note weighs them explicitly.
- No first-year-specific US prevalence number is stated; the orientation
  section uses the NHANES 1-2-year figures and says plainly that no dataset
  in the record specifies a rate under 12 months.
- AAP's 2026 report is attributed as read via secondary quotation (cited to
  Guideline Central, the resolving URL) rather than quoted as a primary
  passage.
- The unverified "18%" DGA figure and the un-located 2003 Chilean paper's
  own numbers are not used anywhere; source 6 (the 2012 follow-up) carries
  the original-trial-design and harm-signal citations instead, as directed.

## Deliberately omitted, not requested

The evidence record's discarded-but-verified FITS intake-adequacy figures
(age-banded, below-EAR percentages) were left out. They're flagged as
verified but lack a full citation entry (authors, journal, a numbered
Sources-list slot) in the evidence record, and inventing that detail to
seat a citation would have violated "never invent a locator." This isn't a
hole in the argument — the orientation section's prevalence-gap sentence
covers the same honesty requirement without them — so no researcher request
follows from it.

## Remaining questions

None. The evidence record settled every claim the argument needed; nothing
required a REQUEST.
