# Draft handoff: opinion/vaccine-schedule-order (writer 02)

Round 02 applied the two routed sourcing fixes only. The editor's nine direct
edits were preserved unchanged (verified: reworded dek, "governed by the Federal
Advisory Committee Act," the 1964 timeline dot without the FACA clause, the two
deleted slop sentences, the Racine-to-NBC recite, the Verdict "advances the
causal reason its signers gave" wording, and the Hviid identity anchor on the
epidemiologist sentence).

## Original-work sentence (unchanged, still holds)

The article turns the evidence record's separate facts into an argument the
record does not make: that the order's own operative instructions (splitting
MMR, reviewing adjuvants, spacing shots across visits) are what tie the
off-the-page autism remarks to the written policy, so both the autism ground
and the conceded peer-nation point reduce to a single procedural defect whose
remedy is an ACIP evidence review and vote, not a better-drafted order.

## Routed items resolved

- Item 1 (Wakefield descriptor). "A case series of twelve children" is now cited
  to the source that owns it: the 1998 Lancet paper (new primary, s15,
  thelancet.com PIIS0140673697110960, showing the RETRACTED banner). Quackwatch
  (now s16, secondary) is kept only for the verbatim retraction and the GMC
  dishonesty finding, which sit in the same sentence after the descriptor. The
  Lancet page returns 403 to automated fetch (bot wall, gated-not-dead, same as
  the retained acpjournals Hviid primary); it resolves for a reader and the
  proof's link checker treats 403 as "ok."
- Item 2 (CRS reclassification). CRS (now s5) is relabeled
  data-nb-kind="secondary". The statutory claims it carried now cite the U.S.
  Code sections directly as primaries: 42 U.S.C. 217a for ACIP's Section 222
  establishment (s4), 42 U.S.C. 300gg-13 for the ACA §2713 coverage mandate
  (s6), and 42 U.S.C. 1396s for the VFC §1928 linkage (s7), all hosted on
  Cornell LII and confirmed to return HTTP 200. CRS is retained as the secondary
  account for the CDC-adoption and MMWR process description; KFF (s8) still
  corroborates the coverage linkage.

Sources renumbered in first-citation order (15 to 19 entries): the three
statutory primaries enter in the "who sets it" section and the Lancet paper in
the autism note, shifting every downstream number. Composition is now 10 primary
and 9 secondary, all cited, min_sources 8 satisfied.

## Final proof result

`./nb check ... --series opinion --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0 — PUBLISHABLE.**

Stamped: words=1932, reading_minutes=8, sources=19. nb-meta harness
"claude-code-routine", model "claude-opus-4-8", dek identical to the rendered
dekline.

## Warnings intentionally left

None.

## Open question

None. Both fixes are pure sourcing changes; the argument, both grounds, and the
steelman are untouched.
