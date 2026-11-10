# Commission: feature/andes-hantavirus-cruise-monitoring

Series: feature (Daily). Template: article. Mode: open. Authorized by
`nb duty` for 2026-11-10. Strict: 600–1,200 words, 2–4 flex sections, at least
5 sources. Five-minute read; each section built around a visual.

## Why now

CDC published its accounting of the US response in MMWR on 5 November 2026
(Vol. 75, No. 43, https://www.cdc.gov/mmwr/volumes/75/wr/mm7543a1.htm): seven
initial cases of severe respiratory illness, three deaths, among 147 people
aboard a cruise ship in the Atlantic, confirmed as Andes virus (ANDV), the only
hantavirus known to spread person to person. 88 US residents across 27
jurisdictions were monitored for 42 days; none was infected. About 653 exposed
people from 33 countries were monitored worldwide.

## The angle

How the response decided who to watch and for how long, and what a clean
result from it shows. The piece is about the mechanism of contact monitoring
for a pathogen with a long, variable incubation period:

1. Who was a contact: the funnel from the ship's 147 to the US 88 (passengers
   who left before confirmation, the repatriated group in Omaha, flight
   contacts), with CDC's risk categories as MMWR defines them.
2. Why 42 days: the incubation distribution the authorities used (WHO's and
   CDC's figures, and the Epuyén, Argentina, 2018–19 outbreak data that most
   ANDV person-to-person incubation estimates come from), and what share of
   infected contacts a 35- or 42-day window would still miss. Draw the
   distribution and the cutoff.
3. What zero of 88 does and does not show: a monitored group with no secondary
   infection bounds the secondary attack rate among those contacts (the writer
   may compute an exact binomial or rule-of-three bound and must label it as
   the paper's own arithmetic, not CDC's), set against the transmission that did
   happen aboard and in the Epuyén outbreak. Fair statement of why the
   response was still justified given a ~40% case-fatality rate.

The researcher should test this angle. If the record shows the 42-day window
was set by convention rather than an incubation estimate, say so and the piece
reports that instead. If case counts conflict across WHO, ECDC and CDC
(7 initial vs 13 total cases; 26 vs 28 US passengers), the record reconciles
them by date and definition.

## What it is not

Not a narrative of the voyage, not a retelling of the outbreak's spring news,
not a piece about cruise-industry safety. The ship's route can appear only if a
timeline figure needs it.

## Visuals to consider (the writer chooses)

- Contact funnel or flow diagram (inline SVG).
- Incubation distribution with the monitoring window marked (inline SVG or
  `nb chart` from a verified series or published parameters).
- A timeline of notification, repatriation, end of monitoring, WHO declaring
  the outbreak over (2 July per ECDC).
- A comparison of transmission settings (ship, flights, Epuyén) if the record
  supports one.

## Sources to start from (researcher confirms all)

- CDC MMWR, 5 Nov 2026 (above) — primary for US figures; read the full report,
  tables and figure.
- WHO Disease Outbreak News 2026-DON604 (28 May) and any later DON —
  https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON604
- ECDC outbreak page —
  https://www.ecdc.europa.eu/en/infectious-disease-topics/hantavirus-infection/surveillance-and-updates/andes-hantavirus-outbreak
- CDC qualitative risk assessment, 29 May —
  https://www.cdc.gov/cfa-qualitative-assessments/php/data-research/andesvirus2026-hantavirus.html
- Martínez et al., "Super-Spreaders" in Infectious Diseases (Epuyén), NEJM 2020
  — primary for the incubation distribution and serial interval.
- Any published incubation estimate for ANDV (e.g. Vial et al. 2006, Emerg
  Infect Dis) that sets the long tail.

## Production

Policy (balanced): writing coach low effort, researcher high, writer high
(series stage), editor inherited model at high effort (required).

## Neighbours in this edition

daily-brief/2026-11-10 (should not carry this story) and the RL lesson on
n-step returns.

## Recent-pattern notes

- Feature headlines this month: claim-led and specific, often with a number
  ("Four state redistricting votes in 2026 move no House district line";
  "Cutting Lp(a) as far as one genetic study required did not reduce
  cardiovascular events"; "Only the capability index measures what Anthropic's
  2x threshold counts"). Several build a "what X did not do" negative claim;
  two of the last four are null-result headlines. This one is also a null
  result in its data, so the headline must not use that frame again: lead with
  what the monitoring did or decided, not with "no" or "did not".
- Deks have repeatedly paired two figures with "and" or "so" ("…cut Lp(a) by
  … and the trial ruled out …"; "…each blocked a new map, so both states
  start…"). Build a different dek.
- Section headings in recent features: compact clauses, often a two-part
  contrast ("Two maps blocked, one rule loosened, one limit refused"). Avoid
  counted-parallel headings.
- The Lp(a) feature (2026-11-08) was also health science; keep the register
  on the response's mechanism, not the clinical biology.

## Decisions after research (researcher/01)

- The angle's second part changes, as the commission allowed. The record shows
  42 days was adopted first (WHO moved from 45 to 42 days by 8 May; CDC already
  used 4–42; ECDC adopted 42 on 9 May) and quantified later (WHO's 28 May
  estimate: mean 22 days, about 96% symptomatic by day 42, 91% by day 35,
  method unpublished). The number traces through a citation chain in which a
  2014 Chilean paper cites Vial 2006 as "7–42" while Vial 2006 reports 7–39;
  Epuyén's range is 9–40. The piece reports that order and that chain, as
  documented, without calling anyone careless: state what each document says.
- The central argument is now: the US monitoring was sized by a rule set before
  anyone estimated the distribution it was meant to cover; the later estimate
  says the rule catches about 96% of infections; and zero of 88 bounds the
  per-contact attack rate only to about 3.4% (the paper's own arithmetic),
  which does not separate this group from the household attack rate measured in
  Chile. Fair statement of why authorities used a long window for a virus with a
  CFR in the 20–50% range (cite the range by owner; this outbreak's 3 of 13).
- Visuals: prefer the published binned Epuyén series (UKHSA review) with the
  35- and 42-day cutoffs and WHO's 91%/96% points marked, over a fitted curve.
  If a fitted lognormal is drawn, the caption says it is the paper's own fit to
  WHO's two published points, not WHO's curve. A timeline of the window
  decisions (45 → 42, the dates above) and the 88-contact funnel are the other
  candidates; two or three visuals total for a five-minute read.
- Counts: use MMWR for US figures (28 passengers, 88 contacts, 40 high / 48
  low risk), WHO for global (13 cases, 3 deaths). Do not adjudicate the 3 vs
  6 April index-onset discrepancy in the body unless the piece uses the date;
  if it does, say the documents differ.
- NEJM Epuyén paper: cite only its abstract for what the abstract says;
  incubation figures come from the documents the record actually read.

## Decision during drafting (writer/01 query)

- WHO's "probability of safe release" may be read as the share of infected
  contacts symptomatic by that day, provided the article says WHO does not
  define the term. Decided by the orchestrator.
