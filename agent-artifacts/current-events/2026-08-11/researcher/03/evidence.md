# Evidence record: current-events/2026-08-11 (03)

This third pass closes the two sourcing gaps the editor routed (editor/01,
"Required work"). It does not re-open the settled items; pass 01 and pass 02
stand except where corrected below.

**Item 4 (HUD) is fully resolved.** The court's own Memorandum and Order now has
a neutral, court-adjacent home I opened and read as text: the CourtListener/RECAP
copy of Document 41 on the D.R.I. docket. It is the same ten-page order pass 02
read via the New York Attorney General's copy, byte-for-byte the court's
document, hosted by the free-law RECAP archive rather than by a plaintiff. The
writer can repoint s7 to it and keep `data-nb-kind` primary.

**Item 3 (National Guard) is resolved by supplying the owning primaries, and by
retiring the mislabeled one.** The cited s5 — the Senate HSGAC report PDF — is a
**scanned image** (JPEG-encoded pages), so it cannot be read as text by any fetch
tool; more important, it is the **Peters–Kim report of 5 February 2026**, which
owns *seven-month* figures ($330M to date, ~$1.65M/day, ~$602M/yr, ~2,500 troops
as of early January, "no measurable impact on public safety"), **not** the
one-year-mark figures the item leads on. It should be dropped as the item's
primary. In its place I opened and verified the actual owners of the item's
figures: **MPD's own crime page owns the crime numbers firsthand** (violent +3%,
property −23%, as of 10 August 2026); **CBO's 28 January 2026 letter owns the
~$55M/month cost** ("$55 million a month for 2,950 personnel in Washington,
D.C."); the **Niskanen Center study owns the causal read** (~24% cut in
opportunistic property crime, no measurable violent-crime effect); and the
**~$1.43B projection is the Pentagon comptroller nominee's**, carried by Roll
Call. Recommendation to the writer below: **lead the item on the MPD crime record**
— it gives the cleanest one-owning-primary-plus-independent-secondary basis, with
every figure openable.

Thin spots, stated honestly: cbo.gov itself returns 403 to every automated
request I made (browser-UA curl and fetch alike) — its content is confirmed by a
verbatim Senate-hosted copy I read in full and by two secondaries, but a reader's
link should point at cbo.gov and be eyeballed in a real browser. The cumulative
"9,700+ rotated / ~2,000 armed" troop figures have no single primary page; they
live in the Joint Task Force / National Guard Bureau deployment record and are
carried by the secondary. Keep those off the lead.

## Preserved from passes 01 and 02

Incorporated by reference, unchanged:
`/home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/researcher/01/evidence.md`
and
`/home/user/the-nightly-build/.nb-work/current-events/2026-08-11/agent-artifacts/current-events/2026-08-11/researcher/02/evidence.md`.
Those hold: the childhood-vaccine executive order (two White House primaries plus
NPR); the D.C. Circuit ballroom ruling (CBS plus the CADC opinion's own page);
the Lisa Cook removal notice (SCOTUSblog, still secondary-only, unchanged); and
the full substance of the HUD order and its independent secondaries (Rhode Island
Current, Davis Vanguard) and the HUD release (hud-no-26-038). The only changes
here are (a) the HUD **primary link** moves to the court's neutral copy, and (b)
the National Guard **primary** is replaced with the owning sources below.

## Sources

### Item 4 (HUD) — new owning primary link

```text
URL:         https://storage.courtlistener.com/recap/gov.uscourts.rid.62592/gov.uscourts.rid.62592.41.0.pdf
Kind:        primary — the court's own Memorandum and Order (Document 41), the
             identical ten-page order pass 02 read, hosted on the free-law RECAP
             archive (a neutral repository of PACER filings), not by any party. I
             downloaded it and extracted all ten pages of text; it is a text PDF,
             not a scan.
Establishes: the holding, legal basis, and remedy, firsthand — same document as
             pass 02, now on a neutral host
Paraphrase:  Header reads "Case 1:26-cv-00439-MSM-AEM  Document 41  Filed 08/07/26
             Page 1 of 10." The caption consolidates the two challenges the order
             decides together — STATE OF WASHINGTON, et al. v. HUD, et al., and
             NATIONAL ALLIANCE TO END HOMELESSNESS, et al. v. HUD, et al. (i.e. the
             26-cv-00439 and 26-cv-00436 matters). Body matches pass 02 verbatim:
             HUD violated the APA (5 U.S.C. 706(2)(D)) by issuing the 2026 NOFO's
             $1.3B set-aside without McKinney-Vento notice-and-comment; the court
             "sets aside HUD's issuance of the 2026 NOFO in its entirety" and
             "denies Plaintiffs' request for a permanent injunction."
Locators:    p.1 caption and case-number header; holding pp.5, 7; injunction
             denial p.9; conclusion/signature p.10 (McElroy, 8/7/2026)
Quote:       "The Court therefore sets aside HUD's issuance of the 2026 NOFO in its
             entirety as violative of the APA. The Court, however, denies
             Plaintiffs' request for a permanent injunction."
```

```text
URL:         https://www.courtlistener.com/docket/73584661/state-of-washington-v-united-states-department-of-housing-and-urban/
Kind:        primary/neutral docket — CourtListener's page for the D.R.I. docket
             (1:26-cv-00439-MSM-AEM), the browsable neutral home of the case. I
             fetched it (HTTP 200) and read the entry list.
Establishes: that Document 41 is the Memorandum and Order of 7 August 2026, and
             the docket's identity, firsthand
Paraphrase:  Docket entry 41, dated "Aug 7, 2026," reads: "MEMORANDUM AND ORDER
             GRANTING IN PART AND DENYING IN PART [34] Plaintiffs' Motion for
             Summary Judgment and DENYING IN PART AND GRANTING IN PART [37]
             Defendants' Cross-Motion... sets aside HUD's issuance of the 2026 NOFO
             in its entirety as violative of the APA... denies Plaintiffs' request
             for a permanent injunction... So Ordered by District Judge Mary S.
             McElroy on 8/7/2026." Presiding: District Judge Mary S. McElroy,
             Magistrate Judge Amy E. Moses; related case 1:25-cv-626-MSM-AEM. The
             entry links the same RECAP PDF above and a PACER purchase link
             (ecf.rid.uscourts.gov/doc1/16102540710?caseid=62592).
Locators:    docket entry #41; entry #42 is the accompanying Judgment
Quote:       docket text as above
```

```text
URL:         https://ag.ny.gov/sites/default/files/decisions/washington-et-al-v-department-of-housing-and-urban-development-et-al-decision-2026.pdf
Kind:        secondary host of a primary document — the NY Attorney General's
             (a plaintiff's) verbatim copy of the same order. RETAINED only as a
             readable fallback; superseded as the citation target by the neutral
             RECAP copy above. Same text pass 02 read in full.
Establishes: nothing new; identical order text
Paraphrase:  see pass 02
Locators:    see pass 02
Quote:       see pass 02
```

### Item 3 (National Guard) — owning primaries

```text
URL:         https://mpdc.dc.gov/dailycrime
Kind:        primary — the Metropolitan Police Department's own "District Crime
             Data at a Glance" page; MPD owns and publishes the counts. Opened and
             confirmed (renders as MPD's live data page).
Establishes: the item's crime figures, firsthand, from the agency that owns them
Paraphrase:  Citywide year-to-date comparison as of 10 August 2026: violent crime
             1,600 (2025) -> 1,655 (2026), "3%" increase; property crime 14,031
             (2025) -> 10,830 (2026), "-23%"; all crime 15,631 -> 12,485, "-20%."
             The page states figures reflect "data entered into MPD's records
             management system" and are preliminary pending classification
             amendments and unfounded determinations.
Locators:    the at-a-glance comparison table; violent-crime and property-crime rows
Quote:       "3%" (violent, YoY); "-23%" (property, YoY), as of 10 Aug 2026
```

```text
URL:         https://www.cbo.gov/publication/61943
Kind:        primary — the Congressional Budget Office's cost letter; CBO owns the
             estimate. NOTE: cbo.gov returns 403 to every automated request I made
             (browser-UA curl and fetch); it is a live public CBO publication that
             gates scrapers, not a dead link. I read the document's FULL TEXT via a
             verbatim Senate-hosted copy (Sen. Warren / Sen. Duckworth office
             download of the identical CBO letter) and the figures are also
             confirmed by the secondary below. The direct-PDF form of the same page
             is https://www.cbo.gov/system/files/2026-01/61943-Troop-Deployments.pdf
Establishes: the ~$55M/month D.C. cost and the per-day cost, firsthand (CBO's own
             estimate)
Paraphrase:  Letter dated 28 January 2026 from CBO Director Phillip L. Swagel to
             the Honorable Jeff Merkley, Ranking Member, Senate Budget Committee;
             Re: "Estimating the Costs of Troop Deployments to U.S. Cities" (CBO
             pub. 61943). CBO estimates the monthly cost of continuing the ongoing
             deployments at their then-current size ranges up to "$55 million a
             month for 2,950 personnel in Washington, D.C." A CBO table of "Dollars
             per day" per service member gives Washington, D.C. a range of $522 to
             $607. The letter also recounts that the 11 August 2025 presidential
             memorandum led to "[a]pproximately 2,400 National Guard personnel...
             activated and deployed to Washington," with an additional ~500-560
             after the 26 November 2025 shooting of two West Virginia guardsmen.
Locators:    letterhead and salutation (date, addressee, Re line); "Monthly Cost of
             Future Deployments" section ("$55 million a month for 2,950 personnel
             in Washington, D.C."); the "Dollars per day" table (Washington, D.C.
             $522-$607); background paragraph (Aug 11 memorandum; ~2,400 activated)
Quote:       "$55 million a month for 2,950 personnel in Washington, D.C."
```

```text
URL:         https://www.niskanencenter.org/washington-dc-crime-decline-and-its-lessons-for-american-policing/
Kind:        primary (for its own analysis) — the Niskanen Center study; it owns
             the causal estimate and the cost-effectiveness comparison. Opened and
             read.
Establishes: the deployment's measured effect on crime, and the per-officer cost
             comparison — the analytical spine of the item's "the troops can't
             claim the drop" point
Paraphrase:  "Washington, D.C.'s crime decline and its lessons for American
             policing," by Erich Battistin, Richard Hahn, Samantha Perez-Davila,
             and Borui Sun, published 28 May 2026. Using an event-study design on
             MPD data, it finds the Guard deployment produced roughly a 24 percent
             reduction in opportunistic property crime in the first six months and
             "no measurable effect on violent crime" (robberies were already
             trending down before August 2025, with no break at deployment). It
             puts the daily cost at $607 per Guard member (citing the CBO 2026
             figure) versus about $384 per MPD officer, and argues an equivalent
             investment in targeted MPD deployment could yield far larger benefit.
Locators:    "What kind of crime fell -- and why" section and Figure 7; the
             cost-comparison section
Quote:       "a 24 percent reduction in opportunistic property crime in the first
             six months, with no measurable effect on violent crime"
```

```text
URL:         https://www.hsgac.senate.gov/media/dems/peters-and-kim-report-finds-trump-administrations-national-guard-deployment-in-d-c-costs-taxpayers-more-than/
Kind:        primary (for the report's findings) — the readable committee/senators'
             announcement of the Peters-Kim HSGAC report. This REPLACES the
             unreadable scanned s5 PDF as the record's home for the report's
             figures. The identical release is also at kim.senate.gov and
             peters.senate.gov (I opened the kim.senate.gov copy and confirmed the
             text).
Establishes: what the HSGAC report actually owns — and that it is a February 2026,
             seven-month document, NOT the one-year figures
Paraphrase:  Released 5 February 2026. Ranking Members Gary Peters (D-MI) and Andy
             Kim (D-NJ) report the D.C. deployment had cost more than $330 million
             -- "nearly $1.65 million each day" -- in the seven months since
             activation, is "on track to spend more than $602 million per year"
             (against MPD's ~$599M FY2026 operating budget), involved ~2,500 service
             members from D.C. and nine states as of early January, and produced
             "no measurable impact on public safety," "no clear strategy, no
             evidence of effectiveness." It does NOT contain the one-year figures
             (9,700 rotated, $55M/month CBO, $1.43B comptroller, property -24% /
             violent +3%).
Locators:    release headline and body; cost paragraph; MPD-budget comparison;
             public-safety-impact paragraph
Quote:       "more than $330 million -- nearly $1.65 million each day"; "no
             measurable impact on public safety"
```

```text
URL:         https://rollcall.com/2026/08/04/pentagon-national-guard-in-dc-to-cost-another-1-43-billion/
Kind:        secondary — CQ Roll Call, 4 August 2026; independent reporting that
             attributes the ~$1.43B projection to its owner. Opened and confirmed.
Establishes: the owner, period, and provenance of the $1.43B figure
Paraphrase:  Reports that the estimate that the D.C. Guard deployment will cost
             "another $1.43 billion" from 1 October 2026 through January 2029 came
             from Jules "Jay" W. Hurst III, the nominee for Pentagon comptroller, in
             a written response to a question for the record from Sen. Elizabeth
             Warren (Senate Armed Services Committee); first reported by The
             Washington Post. The underlying document is a QFR response to the SASC;
             I found no standalone public page hosting it, so this figure remains
             carried by the secondary, not by an openable owning-primary page.
Locators:    lede and attribution paragraph
Quote:       the estimate "was contained in a written response by Jules 'Jay' W.
             Hurst III, the nominee for Pentagon comptroller, to a question for the
             record from Sen. Elizabeth Warren"
```

The independent secondary for the one-year item — Stars and Stripes, 10 August
2026 (s6, pass 01: https://www.stripes.com/theaters/us/2026-08-10/national-guard-dc-one-year-deployment-22510103.html)
— stands as read; it is the item's independent secondary and attributes each
figure to the owners above. The Stars and Stripes report of 28 January 2026
(https://www.stripes.com/theaters/us/2026-01-28/cbo-estimate-national-guard-deployments-20555864.html,
opened here) independently confirms the CBO "$55 million per month... $660 million
for the year" for "more than 2,690 troops" and the "$522 to $607 per service
member per day" range.

## Contradictions

- **The labeled primary (s5) is the wrong document for this item.** The HSGAC PDF
  is the Peters-Kim report of 5 February 2026; its numbers are seven-month figures
  ($330M, $1.65M/day, $602M/yr, ~2,500 troops as of early January). The item leads
  on one-year figures those do not include. Do not cite the HSGAC report for the
  one-year troop, cost, or crime numbers.
- **Initial troop count: 800 vs ~2,400.** The item (via Stars and Stripes) says 800
  were ordered on 11 August 2025; CBO's letter says "[a]pproximately 2,400 National
  Guard personnel... were activated and deployed to Washington" following the
  Aug 11 memorandum. The 800 is the first D.C.-only tranche; the ~2,400 reflects
  the D.C. plus state guards activated shortly after. If the item uses "800
  initial," it should mark it as the first order, not the deployment's activated
  strength.
- **Property crime: "nearly a quarter" vs MPD's -23%.** MPD's own page shows
  property crime -23% year-to-date (as of 10 Aug 2026), not -24%/-25%. The ~24%
  figure is Niskanen's *causal* estimate of the Guard's marginal effect over the
  first six months, a different quantity from MPD's raw citywide YoY change. Keep
  the two distinct: MPD owns "-23% citywide"; Niskanen owns "~24% of property crime
  attributable to the deployment."
- **Violent crime "+3%" is a within-2026 rise on a longer decline.** MPD shows
  violent crime +3% YoY (1,600 -> 1,655), while the pre-deployment period saw a
  steep drop (a 30-year low in 2024, per the U.S. Attorney's Office, carried by the
  secondary). The mixed record survives, as the editor kept it.
- **CBO cost is monthly-at-size; the $1.43B is a forward projection.** CBO's
  ~$55M/month is the cost of the deployment at its then-current size (2,950 in
  D.C.); the comptroller's ~$1.43B covers 1 Oct 2026-Jan 2029. They are not the
  same measure and should not be summed or conflated.
- **Lisa Cook (unchanged):** still the 5 August "considering removal" notice with a
  window to 26 August; nothing moved on 10-11 August; no openable owning primary
  (the letter). Not added.

## Numbers

```text
Figure: violent crime +3% (1,600 -> 1,655); property crime -23% (14,031 -> 10,830), YTD
Owner:  MPD, "District Crime Data at a Glance" (mpdc.dc.gov/dailycrime), as of 10 Aug 2026
Scope:  Washington, D.C. citywide, 2026 year-to-date vs same period 2025; preliminary
```

```text
Figure: ~$55 million per month for 2,950 personnel in Washington, D.C.
Owner:  CBO letter, pub. 61943, 28 Jan 2026 (Director Swagel to Sen. Merkley)
Scope:  cost of the ongoing D.C. deployment at its then-current size
```

```text
Figure: $522-$607 per service member per day (Washington, D.C.)
Owner:  CBO letter, pub. 61943 ("Dollars per day" table)
Scope:  per-person daily cost of the D.C. deployment; the $607 high end is the
        number Niskanen and the secondary quote
```

```text
Figure: ~24% reduction in opportunistic property crime; no measurable violent-crime effect
Owner:  Niskanen Center study, 28 May 2026 (Battistin, Hahn, Perez-Davila, Sun)
Scope:  causal estimate of the Guard deployment's marginal effect, first six months
```

```text
Figure: ~$1.43 billion, 1 Oct 2026 through Jan 2029
Owner:  Pentagon comptroller nominee Jules "Jay" W. Hurst III (written QFR response
        to Sen. Warren, SASC), reported by Roll Call 4 Aug 2026; no public standalone
        page for the QFR document itself
Scope:  projected forward cost of continuing the D.C. deployment
```

```text
Figure: HSGAC report — $330M over ~7 months, ~$1.65M/day, ~$602M/yr, ~2,500 troops (early Jan)
Owner:  Peters-Kim HSGAC report, 5 Feb 2026 (announced at hsgac.senate.gov/media/dems and kim.senate.gov)
Scope:  seven-month accounting through early 2026 — NOT the one-year figures; use only if the item cites the report as such
```

```text
Figure: 2026 NOFO set aside "in its entirety"; permanent injunction denied (HUD)
Owner:  McElroy Memorandum and Order, D.R.I. 1:26-cv-00439 & -00436, Doc. 41, 7 Aug 2026
Scope:  unchanged from pass 02; primary link now the neutral RECAP copy
```

## Source assets

```text
Asset: MPD "District Crime Data at a Glance" table (violent +3%, property -23%), mpdc.dc.gov/dailycrime
Shows: the mixed crime record in the owning agency's own numbers, side by side
Crop:  keep both the violent-crime and property-crime rows together; cropping to
       property alone would drop the violent-crime rise the item's balance rests on
```

```text
Asset: CBO "Dollars per day" table row for Washington, D.C. ($522-$607), CBO pub. 61943
Shows: the per-Guard-member daily cost the cost-effectiveness argument turns on
Crop:  retain the D.C. row and the column header; label the source and date (Jan 2026)
```

```text
Asset: Niskanen event-study figure (Figure 7) of crime deviations by type
Shows: property crime breaking downward at deployment while violent crime does not
Crop:  keep both crime-type panels; the contrast is the point
```

```text
Asset: CourtListener docket entry #41 (the order's neutral docket line), courtlistener.com/docket/73584661/
Shows: the order's provenance on the court's own docket, independent of any party
Crop:  the entry text and the case number 1:26-cv-00439-MSM-AEM
```

## Discarded / gated

```text
URL: https://www.hsgac.senate.gov/wp-content/uploads/NationalGuardReportExecutiveSummary.pdf — resolves, but the PDF is a SCANNED IMAGE (JPEG-encoded pages), unreadable as text by any fetch tool; and it is the Feb 2026 Peters-Kim report, not the one-year figures. Replaced by the readable senators' release as the owner of the report's findings.
URL: https://www.cbo.gov/publication/61943 and https://www.cbo.gov/system/files/2026-01/61943-Troop-Deployments.pdf — both return 403 to all automated requests (browser-UA curl and fetch). Live public CBO pages that gate scrapers, not dead. Full text read via a verbatim Senate-hosted copy and confirmed by Stars and Stripes; recorded as the owner's own page with the gate flagged for the writer to eyeball in a browser.
URL: https://www.warren.senate.gov/imo/media/doc/cbo_estimate_on_the_cost_of_domestic_troop_deployments.pdf and https://www.duckworth.senate.gov/download/cbo-cost-estimates-on-domestic-deployments — the identical CBO letter, senator-hosted transports; the Duckworth copy is the one I extracted the text from. Not recorded as the citation target (transport, not CBO's own page), used only to read CBO's words.
URL: https://dockets.justia.com/docket/rhode-island/ridce/1:2026cv00439/62592 — 403 to fetch; used only to confirm the D.R.I. case id (62592) that keyed the CourtListener docket.
URL: https://www.courtlistener.com/docket/72351074/... — this is the appeal (No. 26-1217), not the district-court order; not the target.
```

## What the writer must change

- **Item 3 (National Guard) — replace the primary.** Drop s5 (the HSGAC scanned
  PDF) as the item's primary; it owns none of the one-year figures. **Lead the item
  on the crime record with MPD as the owning primary:** cite
  `https://mpdc.dc.gov/dailycrime` (`data-nb-kind` primary) for "property crime
  down about 23% while violent crime rose 3%" (MPD, as of 10 Aug 2026), with Stars
  and Stripes (s6) as the independent secondary. That is the clean
  one-owning-primary-plus-secondary basis. Then cite each remaining figure on its
  owner: the ~$55M/month cost to CBO (`https://www.cbo.gov/publication/61943`; note
  the site gates bots -- confirm it renders in a browser), the causal "~24%
  property / no violent effect" read to the Niskanen study
  (`https://www.niskanencenter.org/washington-dc-crime-decline-and-its-lessons-for-american-policing/`),
  and the ~$1.43B projection to the Pentagon comptroller nominee via Roll Call
  (`https://rollcall.com/2026/08/04/pentagon-national-guard-in-dc-to-cost-another-1-43-billion/`).
  If the item keeps the "$602M/yr, no measurable impact" HSGAC line, cite the
  readable senators' release
  (`https://www.hsgac.senate.gov/media/dems/peters-and-kim-report-finds-trump-administrations-national-guard-deployment-in-d-c-costs-taxpayers-more-than/`),
  and mark that figure as a February 2026 seven-month figure, not a one-year one.

- **Item 4 (HUD) — repoint s7.** Change the s7 href from the NY Attorney General's
  copy to the court's neutral RECAP copy of the order,
  `https://storage.courtlistener.com/recap/gov.uscourts.rid.62592/gov.uscourts.rid.62592.41.0.pdf`
  (keep `data-nb-kind` primary). It is the identical ten-page Document 41 on a
  neutral free-law host and it resolves (HTTP 200, text PDF). If a browsable docket
  page is preferred over a direct PDF, use the docket home
  `https://www.courtlistener.com/docket/73584661/state-of-washington-v-united-states-department-of-housing-and-urban/`
  (entry #41). Correct docket: 1:26-cv-00439-MSM-AEM (consolidated with
  -00436-MSM-AEM), not the related 25-cv-626/636 line.
