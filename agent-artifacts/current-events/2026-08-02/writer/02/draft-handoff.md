# Draft handoff: current-events/2026-08-02 (writer, invocation 02 — targeted repair)

## Fix applied (item 3 only)

The elimination-status determination (Americas region lost it Nov 2025; U.S.
national status separately under review, decision due Nov 2026) is PAHO's own
determination — its Regional Verification Commission is the body that
certifies elimination status; CDC does not. The item previously cited that
determination to CDC in the headline and tagged PAHO `data-nb-kind="secondary"`
solely to satisfy the template's one-primary-per-item cap. Fixed:

- **Headline href + citation** now point to PAHO (formerly CDC's page).
- **`data-nb-kind` swapped honestly:** PAHO is now `primary` (it owns the
  claim the headline and the item's central correction make); CDC is now
  `secondary`, cited for the case data it actually owns (2,371 cases, 37
  outbreaks, 94% outbreak-associated, 95.2%→92.5% MMR coverage). KFF stays
  `secondary`, unchanged, for the definitional/dual-verification structure.
- **Renumbering:** because PAHO now fires first in item 3 (the headline is
  its first appearance), source IDs `s9` and `s10` were swapped so numbering
  stays in first-citation order — PAHO is `s9`, CDC is `s10`. `s11` (KFF) is
  untouched. No other item's numbering changed.
- **Jan. 20, 2025 onset sentence:** added `s9` (PAHO) alongside the existing
  `s11` (KFF) citation, since the outbreak's analysis-period start date is a
  PAHO fact that was previously carrying only the KFF citation.
- The timeline furniture's two `<li>` citations were updated from `s10` to
  `s9` to match the renumbered PAHO source.

## Editor's other edits — preserved, untouched

Confirmed still in the file exactly as the editor left them:

- Item 2: the false "in an order a second outlet independently confirmed"
  clause remains cut; the Percival quote still carries both `s5` (Fox) and
  `s6` (yourNEWS).
- Item 3: the "; PAHO is now applying" → ". PAHO is now applying" punctuation
  fix remains (this repair only touched citation targets/kinds on that
  sentence, not its wording or the period the editor put in).
- Item 4: "Their chief executives lead the coalition" remains (not
  "presidents").

No changes were made to items 1, 2, or 4 beyond confirming the above held.

## Proof result

`nb check /home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html --series current-events --library /home/user/library`:

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

## Remaining questions

None.
