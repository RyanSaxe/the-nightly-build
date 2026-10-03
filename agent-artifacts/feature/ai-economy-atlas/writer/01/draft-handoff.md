# Draft handoff: feature/ai-economy-atlas (01)

## Original-work claim (one sentence)

This article pairs each ATLAS headline figure with the denominator its own data
dictionary assigns it and recomputes the released dataset to 20.06%, turning the
shares into a checkable statement: the 30% measures how heavily computer-and-
mathematical workers converse with Gemini about work, not how much of that work
AI does, and the 6.9 hours measures a surveyed belief about saved time, not
measured time.

That work is visible on the page in the denominator table (usage-pool section),
the 20.06%-vs-30% recomputation, the volume-vs-depth split carried through
Figure 1 (the saturation chart), and the closing section's two explicit
"establishes / does not establish" statements.

## Proof result

Exact brief command, links included:
`nb check .../ai-economy-atlas.html --series feature --repo /home/user/the-nightly-build`
→ **BLOCK: 0, WARN: 0, PUBLISHABLE.** `nb stamp`: words=1831, reading_minutes=8,
sources=9.

No warning left standing. Earlier iterations cleared four warnings
(sentence-density x3, one cite-order) by splitting long sentences and
renumbering sources into first-appearance order.

## Decisions and open questions for the orchestrator

1. **Chart scope (please confirm).** The brief asked for a chart "contrasting
   volume-share against saturation depth." The verified global series in the
   evidence Numbers section carries no major-group volume-share column, and the
   evidence confirms the public files withhold major-group volume shares (only
   US broad-group volumes, which sum to 20.06%, and per-country minor groups are
   released). So I built the chart strictly from the verified series as a
   saturation chart (any observed use vs intensive use) and carried the
   volume-vs-depth contrast in prose instead ("The 30% is a size; position is
   depth"). If a literal volume-vs-saturation chart is wanted, it needs a
   verified global major-group volume series the record does not currently hold.

2. **Chart coverage.** The evidence Numbers series lists 14 of the 22 major
   groups ("full 22-group series in file"); I charted only the 14 in the record,
   since I draw only from the record. If the full 22 are wanted, the researcher
   would need to add the remaining rows.

3. **One source URL changed within the evidence.** The dataset's top-level path
   (`/economy/atlas/data/atlas_v1_public_data.zip`) 404s and blocks the link
   proof; the evidence also names the served path
   (`/economy/atlas/embed-report-2026/data/atlas_v1_public_data.zip`), which
   resolves (200). Source 5 now uses that served path. No claim changed.

No open voice questions. The register follows the three-writer target
(name the target of inference, then the quantity the instrument produces).
