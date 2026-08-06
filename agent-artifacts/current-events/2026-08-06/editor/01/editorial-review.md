# Editorial review: current-events/2026-08-06 (editor/01)

## Skeptic

The brief carries five items, each a full-sentence claim with a compressed
verdict. The front-page thesis, as the dek states it, is that the day's official
decisions "kept sorting who is held to account and who is spared." The load-
bearing claims are: (1) a judge dismissed the last January 6 prosecution under
protest; (2) HHS is moving a $150M migrant-children legal contract to a firm with
almost no immigration lawyers; (3) Texas paused new data-center grid hookups
pending an audit of a 474 GW queue; (4) El-Sayed won Michigan's Democratic Senate
primary despite a ~9:1 advertising disadvantage; (5) central-Appalachian black
lung reached 32.5%, its worst rate since 1978.

I opened every printed href as the article renders it and tested each figure and
label against the owning primary.

- **Item 1 (Oath Keepers).** Primary CourtListener docket resolves (200 to a
  browser; the 403 is bot-blocking, not a dead link) and lands on
  *United States v. Rhodes III*, 1:22-cr-00015 (D.D.C.). NPR and CNN corroborate
  the "final Jan. 6 case" framing (CNN returned 451 from this egress region but
  resolves 200 to a browser). Rhodes's 18-year sentence, the January 2025
  commutation, the "epilogue" quote, and the Aug. 4 dismissal all check against
  the primary and NPR. The writer correctly declines to state a defendant count
  the order's own list would settle (secondary tallies disagree, six vs. nine).
  Held.
- **Item 2 (HHS/Burke).** Primary is the Federal Register public-inspection PDF
  (`2026-16081.pdf`); it downloads as a valid 3-page HHS/ORR notice — the
  deliberate artifact the commission authorized because the published-page URL
  404s until Aug. 7. The $150M figure, Marcella Burke as former Trump-era EPA
  deputy general counsel, and the Acacia 20,000-children comparison all check
  against NOTUS and NPR. The immigration-expertise contradiction is handled
  correctly: NOTUS ("no staff attorney lists immigration") and NPR ("two of 24")
  are each attributed, not merged. Held.
- **Item 3 (Abbott).** Primary gov.texas.gov resolves and confirms the audit, the
  pause, the disclosure requirements, 474 GW, ~5x record peak, and ~90% data
  centers. Houston Public Media and Texas Tribune resolve (200 to a browser).
  Held.
- **Item 4 (Michigan).** Break. The printed primary href,
  `https://mvic.sos.state.mi.us/`, is the Michigan **Voter Information Center** — a
  voter-lookup tool for registration and sample ballots — not an election-results
  page. Its bare root does not land on, and never displays, the canvassed or
  unofficial Senate-primary result the item cites it for; it also returns 403 to a
  direct browser visit, not merely to the proof's probe. The writer kept it on the
  strength of `engine/nb/links.py` treating a 403 as "restricted, not dead," but
  that only clears the proof; it does not satisfy the requirement that the href
  land on the source that owns the claim. The result itself is sound — El-Sayed
  48.5 / Stevens 47.5 / McMorrow 4.0 at ~98.8% reported, the ~$65M outside money,
  >$30M AIPAC-affiliated, ~9:1 ad advantage, Peters vacating, Rogers unopposed all
  verify against NBC (s11, s12). But the item has no valid owning primary. Fails
  the per-item sourcing gate.
- **Item 5 (black lung).** Primary AJRCCM letter resolves (via headless fetch):
  Laney et al., NIOSH/CDC, "Coal Workers' Pneumoconiosis in the United States
  1974–2025." 32.5% (91/280), up from 20.6% in 2018, highest since 1978, and
  >1,700 deaths 2020–2023 all check against the primary and NPR. Arithmetic
  (91/280 = 32.5%) is correct. Held.

Date precision (AJRCCM): the primary (OUP) shows publication Aug. 4; NPR and the
evidence record say Aug. 5. The primary governs, so I fixed the writer's cautious
"published this week" to "published August 4" directly.

`data-nb-kind` audit: all fourteen labels are correct in kind — five primaries
(court docket, Federal Register notice, governor's directive, state elections
authority, peer-reviewed letter) and nine independent secondaries, one owning
primary and at least one independent account per item. The only sourcing defect
is the *address* of the item-4 primary, not its label.

## Cut

The prose is tight; there was little to remove. I made two punctuation fixes in
item 2, converting reflex semicolons to periods: one separating Burke's identity
from the immigration-expertise finding, one separating HHS's account from the
"practical result" verdict. The second also cleanly splits report from read, the
separation the voice guide's Semafor lesson asks for.

Two prose problems need the writer, not a cut:

- **The dek grades the selection and overclaims the theme.** "…leading a front
  page where official decisions kept sorting who is held to account and who is
  spared" narrates the artifact ("a front page") and asserts a front-page-wide
  pattern that the energy (item 3) and elections (item 4) items do not fit. A dek
  must commit to something the piece establishes and must not grade its own
  selection. The lead clause ("A judge ends the last January 6 prosecution under
  protest") is a real, committed claim; the thematic tail is the problem.
- **The item-4 verdict asserts an unsupported causal magnitude.** "A near-total
  advertising advantage moved the result by roughly a point, which is close to no
  result at all." No counterfactual is cited, so "moved the result by roughly a
  point" is a causal claim the two sources cannot reconstruct, and its direction
  is ambiguous (Stevens outspent and *lost*). The supportable read is that a ~9:1
  advantage failed to prevent a ~1-point loss — it bought almost nothing.

No prompt leakage in the item prose. Verdict cadence varies enough (two "so"
constructions, one earned "not…but" in item 1, which stays within the one-or-two
contrast ceiling). No comma-triad dek, no "from X to Y" span, no colon-subtitle
headlines — the recent-pattern habits are not reintroduced. rs-docket and
nb-stat-strip each carry evidence with a genuine shape and earn their place.

## Reader

Read straight through as the paper's declared reader, the brief delivers what the
wire would not: the Jan. 6 case ended on an executive choice rather than the
evidence; representation for children who cannot represent themselves now rests
with a firm that has barely done the work; Texas is conceding it cannot yet tell
real load from a placeholder; black lung will keep climbing from dust already
breathed no matter what any stalled rule does now. Those are real synthesized
reads, and they match the original-work sentence in the handoff. The prose sits
closer to the voice-guide exemplars (compressed verdict, load-bearing particular)
than to a median summary. The one soft spot is the item-4 verdict, which reaches
past its sources rather than landing inside them.

## Edits

- Item 5: "published this week" → "published August 4" (date precision; the AJRCCM primary shows Aug. 4, and the primary governs the NPR/evidence Aug. 5).
- Item 2: reflex semicolon → period after "…EPA deputy general counsel".
- Item 2: reflex semicolon → period after "…new terms it refused" (also separates report from verdict).
- Ran `nb stamp`: words=948, reading_minutes=4, sources=14 (unchanged).

## Required work

**researcher** — Supply the correct owning primary for the Michigan Senate
primary: a Michigan Secretary of State / Bureau of Elections results page that
resolves and lands on this specific race (unofficial results pending canvass).
`mvic.sos.state.mi.us` is the Voter Information Center, not a results portal, and
does not own the vote count. Name the exact resolving URL so the item has one
owning primary that a clicking reader reaches.

**writer** — (1) Replace the item-4 primary href (both the headline `<a>` and
source entry s10) with the researcher's supplied results URL; keep the
`data-nb-kind="primary"` label. (2) Recast the dek (both the `nb-meta` "dek" field
and the `nb-dekline`) to a claim the selection establishes, dropping the self-
referential "front page" framing and the theme the energy and elections items do
not support. (3) Recast the item-4 verdict so it does not assert an unsupported
causal magnitude — state the supportable read (a ~9:1 ad advantage failed to
prevent a ~1-point loss). (4) Re-run the proof with links included after these
changes.

Note for the orchestrator (not blocking): NPR's own text may not carry HHS's
"offered Acacia new terms it refused" account that the evidence record attributes
to it; the researcher documented it, so I did not block, but the writer/
researcher can confirm on the next pass.

## Decision

revise — item 4 has no valid owning primary (the printed MVIC href is a voter-
lookup tool, not the results source that owns the El-Sayed win), and the dek and
item-4 verdict reach past what the sources establish.
