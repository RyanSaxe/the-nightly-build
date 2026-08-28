# Writer draft handoff: tech-news/2026-08-28 (02)

## Editorial requests resolved

- **Date the OpenAI item and frame it as prior news, bringing the manuscript in
  as a cited primary** — done. The manuscript
  (`cdn.openai.com/pdf/ten-proofs-oai.pdf`, dated August 1, updated August 6) is
  now the item's cited primary (s5). The item opens "OpenAI posted the manuscript
  on August 1 and updated it on August 6, about four weeks ago," so a fresh
  reader sees prior work, not the day's development.

## Constraint hit, and how it was resolved

The deterministic proof enforces exactly one primary per item
(`B-SOURCE-KIND`: "item #3 cites 2 primary source(s); this series asks every
item for exactly 1"). Adding the manuscript alongside the openai/ten-proofs
repository (both OpenAI first-party primaries) blocked. The editor's and
coordinator's explicit instruction is to bring the manuscript in as the cited
primary, and the repository could not be relabeled secondary without falsifying
its source kind, so the manuscript **replaced** the repository as item #3's
single primary rather than joining it.

Consequence, flagged for the editor: the repository owned the "machine-checkable
Lean 4 certificates / Apache-2.0" claim and the "verification, not discoveries"
framing. With the repository no longer cited, those claims are gone — nothing in
the manuscript or The Decoder (the two remaining sources) supports the Lean
detail in the evidence record, so I did not carry it. The item now leans on the
manuscript's own richer result descriptions (the Cohn-Elkies asymptotic, the
Connes disproof, the R_k(3) lower bound) and closes on the still-open caveat
(unrefereed). If the desk wants the Lean-verification angle back, that requires
either citing the repository as the single primary and dating the item from The
Decoder's secondary dateline instead, or a series rule change permitting two
first-party primaries in one item.

Also changed the item's topic tag from "Formal mathematics" to "Mathematics" and
the meta tag "formal-math" to "mathematics," since the formal-verification
connotation is no longer sourced.

## Editor's direct edits

All four preserved unchanged: the trimmed AWS closer ("None of the two million
has been deployed yet."), the Broadcom no-comment period, the lead heading with
the date trimmed, and "raise" (not "megaraise") in the Broadcom heading. The
other three items were not otherwise touched.

## Proof

Final command (links included), run exactly as the brief specifies:
`./nb check ... --series tech-news --library /home/user/library-checkout`
Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warning left standing.
`nb stamp`: words 621, reading 3 min, sources 8. Display-text self-test redone
for the changed item: heading links to the manuscript primary, no disputed
figure or "Astra" appears in display text, and meta `dek` still matches the
rendered dekline.

## Open question

The item no longer states that the results are machine-verifiable (Lean/Apache-2.0
was repository-owned, and the one-primary rule forced the repository out). This is
a genuine loss of the item's strongest credibility signal; it is called out above
so the editor can decide whether the trade is acceptable or whether the series'
one-primary rule should bend for this item.
