# Writer draft handoff: tech-news/2026-08-28 (03)

## Editorial requests resolved

- **Restore the OpenAI item's verification substance under the one-primary rule**
  — done via the alternative flagged in round 02. The openai/ten-proofs
  repository is again the item's one primary (s5), owning the machine-checkable
  Lean 4 certificates, the Apache-2.0 license, and the "verification for an
  accompanying manuscript rather than discoveries in their own right" framing.
- **Cite an independent secondary and take the date from it** — The Decoder (s6)
  is the secondary; the item now opens "The Decoder reported the ten results
  about four weeks ago, on August 1," sourcing the staleness to its dateline
  (which the evidence record confirms coincides with the manuscript's). The item
  reads as prior work now public, not the day's development.
- **Keep the "not peer-reviewed" close** — kept as the item's final sentence.
- **Retag to the formal-verification substance** — visible tag back to "Formal
  mathematics" and meta tag back to "formal-math," now that the Lean certificates
  are sourced again.

The manuscript (round-02's primary) is no longer cited, so its manuscript-owned
result characterizations (the Cohn-Elkies asymptotic, the Connes disproof, the
R_k(3) lower bound) are replaced with the topic-level scope the repository
supports (sphere-packing bounds, Connes's rigidity conjecture, quantum parallel
repetition, multicolor Ramsey numbers). The "Astra" name and the ~$2,000 cost
stay confined to the announcement-and-secondary layer, now contrasted against the
repository rather than the manuscript.

## Preserved

Items 1 (AWS), 2 (robotaxi), and 4 (Broadcom) are untouched, including all four
editor direct edits (trimmed AWS closer, Broadcom no-comment period, date trimmed
from the lead heading, "raise" not "megaraise"). Source numbering was unaffected
outside item 3: the repository takes s5 and The Decoder s6, exactly as before the
round-02 swap, so Broadcom's s7/s8 did not move.

## Proof

Final command (links included), run exactly as the brief specifies:
`./nb check ... --series tech-news --library /home/user/library-checkout`
Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warning left standing.
`nb stamp`: words 614, reading 3 min, sources 8. Display-text self-test redone
for the changed item: heading links to the repository primary and its claim is
repository-owned; the date is carried by the secondary that owns the dateline; no
disputed figure or "Astra" appears in display text; meta `dek` still matches the
rendered dekline.

## Open question

None outstanding. The round-02 concern (verification angle lost) is resolved. The
item now carries exactly one primary and one independent secondary, so it no
longer strains the series' one-primary-per-item rule.
