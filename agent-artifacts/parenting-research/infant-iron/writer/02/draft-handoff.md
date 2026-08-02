# Draft handoff: parenting-research/infant-iron (writer/02) — targeted revision

Applied only the editor's three required items from `editor/01/editorial-review.md`.
No other prose was touched; no claims were added.

## Required items resolved

1. **Headline overclaim narrowed and synced.** Changed "no measured benefit to
   infant development" to "no measured cognitive benefit" in all three places:
   the `<h1>`, the `<title>` tag, and the nb-meta JSON `title` field. The dek
   ("...found no cognitive gain from giving it beforehand") was already
   narrower and consistent, and required no change — confirmed identical
   between nb-meta `dek` and the rendered `.nb-dekline` after the edit.
2. **Antithesis-close repetition thinned.** Recast three of the "X, not Y"
   paragraph endings the editor named, leaving the two load-bearing ones
   untouched:
   - Kept: "They are not the same question." (end of the treatment-vs-prevention
     opener) — the treatment-vs-prevention line.
   - Kept: "...treats dosing as a clinician's calculation, not a parent's
     estimate." (end of the Pemba/malaria paragraph) — the parent-vs-clinician
     boundary.
   - Recast: "...the AAP figure is a considered judgment under real
     uncertainty, not an uncontested global consensus." → split into two
     sentences ending "...is a considered judgment made under real
     uncertainty," dropping the antithesis tail (AAP/ESPGHAN section).
   - Recast: "...by the clinician managing that infant, not read off a
     general chart." → cut the trailing clause, ending "...by the clinician
     managing that infant." (preterm-dosing sentence, same section).
   - Recast: "Each belongs to a pediatrician's specific plan, not a
     household's general rule." → "Each is a pediatrician's specific call for
     that child." (home-and-clinician section).
   All three recasts are cuts/rewords of existing sentences; no new claims or
   citations were introduced.
3. **Proof re-run.** `nb stamp` run first (2,946 words, 16 sources, 13-minute
   read — within the 1200-3000 band), then the full `nb check` with links per
   the brief.

## Proof result

```
./nb check .nb-work/parenting-research/infant-iron/library/parenting-research/infant-iron.html \
  --series parenting-research \
  --library /tmp/claude-0/-home-user-the-nightly-build/e4c39d18-3bf5-5a96-80b8-fc87ffc0a494/scratchpad/library-checkout
```

Result: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`, first run after the
edits — no iteration needed. Link checking was included (not
`--no-check-links`).

No warnings intentionally left. No open evidence or voice questions.
