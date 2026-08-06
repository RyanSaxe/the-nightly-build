# Draft handoff: tech-news/2026-08-06 (writer 02)

Revision applying editor/01's required writer items with researcher/02's
corrected sourcing. Not a rewrite; items 2–4 and the editor's two direct item-3
cuts are preserved.

## Changes made
1. **Item 1 sourcing gate (editor required).** Swapped the two non-independent
   legs for genuinely independent accounts, per researcher/02:
   - s2 is now GEN (Genetic Engineering & Biotechnology News), `data-nb-kind="secondary"`.
   - s3 is now NPR, `data-nb-kind="secondary"`.
   - Dropped Medical Xpress (a republished Boston Children's authoring-site
     release) and UT Dell Medical School (the study's own UT-led institution) as
     redundant; neither is independent, so keeping them would only clutter the
     list. Item 1 now has exactly one owning primary (Nature s1) plus two
     genuinely independent secondaries (GEN, NPR).
   - Source numbering is unchanged elsewhere (s4–s12 identical); total stays 12.

2. **Item 1 prose (editor required).** Removed the false "an independent
   science-news account" label (it pointed at the press release). The prose now
   names the independent outlets and scales each to what it actually carried:
   GEN reported the specific anellovirus/persistent-disability association
   independently of the authoring teams [2]; NPR, also an outside newsroom,
   confirmed the broader reactivation-linked-to-long-COVID finding the same day
   [3] (NPR does not name Anelloviridae, so it is attributed only to the broader
   finding). No new claims added.

3. **Dek recast (editor required).** Replaced the selection-grading dek and its
   banned "rather than an AI model" hedged contrast with a claim about the
   finding itself:
   "In 1,154 patients hospitalized with COVID and tracked for a year, the IMPACC
   study saw Epstein-Barr, cytomegalovirus, and anelloviruses reawaken during
   acute illness, a correlation its authors say does not yet prove cause."
   No self-reference, no hedged contrast. nb-meta `dek` and the `nb-dekline` are
   identical, and the `title`/`h1` are unchanged and consistent with it.

## Proof result
`./nb check ... --series tech-news --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings intentionally left.
`nb stamp`: words=833, reading_minutes=4, sources=12. GEN and NPR both probe
"ok" (openable) through the engine's link module.

## Notes for the editor
- The original-work sentence from writer/01 still holds and is still visible:
  provenance-ranked digest, self-reports tagged in-clause (SK hynix "it says";
  OpenAI's coordination narrative "not independently confirmed").
- No open questions. The item-1 independence gap and the selection-grading dek
  the round-01 review flagged are both closed.
