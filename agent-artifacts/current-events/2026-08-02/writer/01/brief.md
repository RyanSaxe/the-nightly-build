# Writer brief: current-events/2026-08-02 (01)

## Your job
Draft the US news `brief` for 2026-08-02 — the 4-item slate the evidence record
verified — then prove it to `BLOCK: 0`. Draft only from the evidence record and
voice guide. Each item is a judgment about why a development matters; no recap,
no reader-handoff closer.

## Begin with these exact inputs
- This brief; `../../commission.md`; `../../editorial-direction.md`.
- Voice guide: `../../writing-coach/01/voice-guide.md` (reread before drafting).
- Evidence record: `../../researcher/01/evidence.md` (your complete claim set and
  its caveats — obey every one).
- Initialized article:
  `/home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html`
  (edit; do not recreate the skeleton).
- Template context: `../../../../.nb-context/` (brief geometry: 4-6 items, 1
  primary + 1+ independent secondary each).

## The slate (lead order from the evidence record)
1. **Iran attack pause / Middle East travel warning (Aug 1, lead).** Primary:
   Trump's own Truth Social post (the party's statement — timestamp Aug 1 10:05
   PM; the pause "subject to being able to rapidly make a DEAL," terms = Hormuz
   reopening + end to the nuclear threat) and the U.S. Embassy Jerusalem security
   alert (Aug 1). Independent secondary: NBC (State Dept urges Americans in 10
   named countries to consider departing). THE JUDGMENT the wire can't file: the
   "deal" rests solely on Trump's unilateral, unconfirmed claim — no Iranian or
   Israeli confirmation in any independent account (NBC/Townhall/RawStory), and
   Trump has repeatedly claimed Hormuz was already open "despite evidence to the
   contrary." Report the pause as claimed; do not state the deal as fact.
2. **Somalia TPS court stay (Aug 1).** Primary: the DHS Federal Register notice
   terminating Somalia's TPS (Sec. Kristi Noem; 1,082 approved beneficiaries;
   original effective date Mar 17, 2026). Independent secondary: Fox News (Judge
   Allison D. Burroughs, D. Mass., issued a new administrative stay Aug 1 after
   plaintiffs refiled as a Fifth Amendment equal-protection claim following the
   Supreme Court's *Mullin v. Doe*). ATTRIBUTE the order to court reporting (the
   order text was not directly read; its existence/date are confirmed by two
   independent secondaries). Name the executive-vs-judiciary framing (DHS's
   Percival: "defiance, obstruction, and delay" vs the live constitutional
   claim) without adjudicating it.
3. **Measles elimination status at risk.** Primary: CDC data (as of Jul 30: 2,371
   confirmed cases, 37 outbreaks, 94% outbreak-associated; kindergarten MMR
   coverage 95.2% → 92.5%). CORRECT the misconception most coverage blurs (the
   record's real news): the Americas *region* lost elimination status in Nov 2025
   because of Canada; the *United States'* own national status is separately
   under review, decision due Nov 2026 (per PAHO, the body that actually
   certifies). The US has not lost its status; it is at risk. Independent
   secondary: KFF for the dual-verification structure/definition (not for the
   case count).
4. **Latino Civic Engagement Coalition (Jul 30, still live).** Primary: the
   UnidosUS joint press release (four orgs, exact names/titles: Janet Murguía,
   UnidosUS; Juan Proaño, LULAC Institute; Hector Sanchez Barba, Mi Familia en
   Acción; Katharine Pichardo, Latino Victory Foundation; goals: contact 5M+
   voters, register 250k, 3.5M door-knocks, ≥5% turnout lift; "for the first
   time" building civic infrastructure together). Independent secondary: CBS
   (target states; 36M Latinos eligible; Trump's 48% 2024 Latino share and the
   polling softening). Get every name and title exactly right.

Run these 4; do not pad. Do not re-report the discarded/prior threads (SCOTUS
mail-in voting, Blanche AG, tariffs, Cook, etc.).

## Coordination
The Iran thread advanced from the paper's 07-30 "direct strikes" coverage — say
what changed (a claimed pause), building on it, without re-explaining. Keep
tech-field items out (they belong to tonight's tech-news brief).

## Furniture
Items + sources. Reach for furniture only where evidence has a shape prose hides
and it is documented (e.g. a compact two-row region-vs-US timeline for measles,
if it earns its place). No chart unless from a verified series. No
article-authored scripts/styles/iframes/forms/external images.

## Universal rules
Per-item 1 primary + 1+ independent secondary; carry evidence-record kinds into
`data-nb-kind` (a party's own statement/official notice = primary; newsrooms =
secondary). Number sources in first-citation order; add
`data-nb-locator`/`data-nb-url` only where the evidence supplies it. Verify every
name, title, place, date, and number against the owning primary (a wrong title in
display text is the costliest error). Fill `nb-meta`: series current-events, slug
2026-08-02, template brief, mode rolling, order null, date 2026-08-02, tags
(accurate, e.g. ["foreign-policy","immigration","health","elections"]), measured
sources/words, a real dek (a stance, not a comma-triad), harness "claude-code",
model "claude-sonnet-5".

## Prove and hand off
Run to `BLOCK: 0`:
`/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/current-events/2026-08-02/library/current-events/2026-08-02.html --series current-events --library /home/user/library`
Treat warnings as revision notes. If a gated primary (travel.state.gov 403) is
needed, use the independent secondary the evidence record names instead; do not
cite a page the researcher could not read.

Write `draft-handoff.md` here: original-work sentence, paths changed, proof
result and warnings left, remaining questions. Return `DONE writer <path>` after
`BLOCK: 0`, or a REQUEST/BLOCKED line.
