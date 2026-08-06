# Draft handoff: current-events/2026-08-06 (writer 01)

## Original work (one sentence)
This front page selects the five developments that actually changed something
on 2026-08-06 and, for each, states the single consequence its primary and
independent sources jointly force but neither states outright — most sharply
that Texas's pause is the state conceding its 474-gigawatt queue is mostly
speculative, and that Appalachian black lung will keep climbing from dust
already breathed no matter what any stalled rule does now.

## Proof result
`./nb check ... --series current-events` **with links included: BLOCK: 0, WARN: 0,
verdict PUBLISHABLE.** No warnings left standing. (One W-SENTENCE-DENSITY warning
on a 57-word black-lung sentence was fixed by splitting it into three sentences
and removing its two em-dashes.)

## Items selected (5 of the 6 candidates)
1. Oath Keepers / last Jan. 6 case dismissed (courts) — primary CourtListener docket + NPR + CNN. Carries `rs-docket`.
2. HHS $150M migrant-children legal contract to Burke Law Group (immigration) — primary Federal Register notice + NOTUS + NPR.
3. Abbott halts Texas data-center grid connections pending audit (energy) — primary Governor's directive + Houston Public Media + Texas Tribune.
4. El-Sayed upsets Stevens in Michigan's Democratic Senate primary (elections) — primary MI SOS portal + NBC (×2).
5. NIOSH black lung at highest rate since 1978 (public health) — primary AJRCCM research letter + NPR. Carries `nb-stat-strip`.

Dropped: **Somalia TPS / Ogles impeachment** (candidate 6). It was the weakest-sourced
swing (Fox News + The Blaze for the partisan strands), and a single member's
impeachment resolution against a judge that cannot advance sits closest to the
series prompt's explicit "routine political theater" exclusion. If the editor
wants a six-item brief, this is the item to restore; H.Res. 1472 (119th Cong.)
is the confirmed resolution number and USCIS's 2026-08-03 TPS update is its
clean owning primary.

## Link-integrity resolution of the three flagged primaries
- **NIOSH AJRCCM letter** — the evidence record supplied no URL. Confirmed via the
  cited NPR piece's own link: the letter moved to Oxford University Press (ATS→OUP,
  March 2026) and lives at
  `https://academic.oup.com/ajrccm/advance-article/doi/10.1093/ajrccm/aamag401/8750197`
  (Laney et al., "Coal Workers' Pneumoconiosis in the United States 1974–2025").
  Resolves; used as the item's owning primary.
- **HHS Federal Register notice** — the published-page URL
  (`/documents/2026/08/07/2026-16081/`) **404s** because publication is scheduled
  for 2026-08-07 (tomorrow). Switched to the live public-inspection PDF the evidence
  also supplied (`https://public-inspection.federalregister.gov/2026-16081.pdf`,
  HTTP 200). Editor publishing on/after Aug. 7 may prefer the permanent documents URL.
- **Ogles impeachment resolution** — confirmed as H.Res. 1472, but the item it
  belonged to was cut (see above), so no congress.gov href is in the article.
- Michigan SOS portal and other government/press primaries return 403 to the proof's
  probe; per `engine/nb/links.py` a 403 is "restricted, not dead" and never blocks.
  Only 404/410 or a non-resolving domain blocks, which is why the FR page had to move.

## Open questions for the editor
- **AJRCCM date discrepancy.** The OUP page shows the letter published Aug. 4, 2026;
  NPR and the evidence record say Aug. 5. I avoided pinning a hard date ("published
  this week") rather than assert one over the other.
- **HHS "almost no immigration lawyers"** in the headline compresses a real, sourced
  contradiction (NOTUS: no staff attorney lists immigration as a specialty; NPR: the
  firm has two). Both counts are attributed in the body; flag if you want the headline
  to name one figure instead of the summary.
