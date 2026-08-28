# Evidence: tech-news/2026-08-28 (researcher 01)

The week's real technological weight sits in compute infrastructure and
autonomous-vehicle regulation, not in a model release. The single development
this record can anchor to a first-party primary and to the current date is the
AWS–NVIDIA agreement to deploy two million additional GPUs, published on AWS's
own newsroom (2026-08-26). The two flashiest aggregator leads in the commission
do not survive contact with a primary: the Nvidia–Hugging Face acquisition is
sourced only to The Information, is unsigned, and neither company has confirmed
it; Broadcom's reported $60–80B AI-debt raise rests entirely on anonymous
sources, and the one Broadcom SEC filing I could open does not contain it. The
Nevada robotaxi authorization is genuine but its headline number needs care: the
only permit document I could open caps Tesla at ten vehicles (interim order,
2026-07-27), while the widely reported 5,000-vehicle ceiling comes from the
2026-08-20 full-permit approval, for which I could not retrieve a primary order.
OpenAI's ten formally verified proofs are real and primary-sourced through the
manuscript and the Lean repository, but the work is dated 2026-08-01 (updated
2026-08-06), roughly four weeks stale for this edition. Where the record is
thin: I could not open the openai.com announcement page (HTTP 403), the primary
NTA order for the 5,000-vehicle approval, or any Broadcom/Anthropic primary for
the August raise; and `nb history` returned no published coverage in this
checkout, so the 2026-08-21 Hugging Face-intrusion continuity rests on the
commission's statement, not on a record I read.

## Sources

```text
URL:         https://www.aboutamazon.com/news/aws/aws-nvidia-2-million-gpus-ai
Kind:        primary — AWS's own newsroom, the authoring party to the commitment
Establishes: firsthand, that AWS commits to deploy 2 million additional NVIDIA
             GPUs and to build federal AI factories
Paraphrase:  AWS and NVIDIA announce an expansion under which AWS will deploy two
             million more NVIDIA GPUs across its global infrastructure in 2027
             and 2028, and will build AI factories for the U.S. government,
             including 100,000 GPUs on secure AWS infrastructure for federal and
             national-security workloads at Impact Level 6 (IL6) and above. The
             partnership extends beyond GPUs to CPUs, networking, memory, open
             models, data processing, and robotics.
Locators:    body; executive quote blocks
Quote:       Jensen Huang, Founder and CEO of NVIDIA: "For 16 years, we have
             scaled NVIDIA computing in the cloud together. Now we are expanding
             our partnership across the full stack." Matt Garman, CEO of AWS:
             "Customers want the freedom to choose the best tools for their AI
             workloads, and they want confidence that everything works
             seamlessly together."
```

```text
URL:         https://aibusiness.com/data-centers/aws-nvidia-expand-partnership-2-million-more-gpus
Kind:        secondary — AI Business (Informa TechTarget) reporting on the joint
             announcement from outside the two companies
Establishes: independent confirmation of the two-million-GPU figure; adds the
             NVIDIA platform names and the running total the primary omitted
Paraphrase:  Independent coverage dates the announcement to 2026-08-27 and states
             the two million GPUs span NVIDIA's Blackwell Ultra, Rubin, and Rubin
             Ultra platforms for 2027–2028, on top of the more-than-one-million
             GPUs AWS committed earlier in 2026 at GTC, bringing capacity
             introduced this year to more than three million. Repeats the 100,000
             government-GPU figure.
Locators:    body; contextual paragraphs
Quote:       —
```

```text
URL:         https://nta.nv.gov/uploadedFiles/ntanvgov/content/Carriers/Certificates/T_to_Z/Tesla_Robotaxi_LLC_AVNC_002-cert_ADA.pdf
Kind:        primary — the Nevada Transportation Authority's own signed Interim
             Order and Permit (the artifact), read firsthand
Establishes: firsthand, the terms of Tesla's interim robotaxi authorization: a
             ten-vehicle cap, Strip-corridor geofence, and a 45 mph ceiling
Paraphrase:  The Nevada Transportation Authority grants Tesla Robotaxi, LLC
             Autonomous Vehicle Network Company (AVNC) Permit 002 under Docket
             26-05015. Service is limited to fully autonomous passenger transport
             within an approved Operational Design Domain, originating and
             terminating in Clark County and confined to the Las Vegas Strip
             corridor. Operations are capped at a maximum fleet of ten (10)
             vehicles; passenger transport is prohibited on roadways posted above
             45 mph; pickups are barred within a quarter mile of Harry Reid
             International Airport absent airport authorization. Signed by Vaughn
             Hartung, Chairman; attested by Travece LeTourneau, Applications
             Manager. Incorporates the Authority's Compliance Order of 2026-06-25.
Locators:    p. 1; SERVICE and RESTRICTIONS paragraphs; signature block
Quote:       "Operations are limited to a maximum fleet of ten (10) fully
             autonomous vehicles"; "Dated: July 27, 2026"
```

```text
URL:         https://techcrunch.com/2026/08/20/tesla-uber-and-waymo-all-get-the-ok-to-operate-thousands-of-robotaxis-in-nevada/
Kind:        secondary — TechCrunch reporting on the 2026-08-20 NTA meeting from
             outside the Authority
Establishes: that on 2026-08-20 the NTA approved full commercial permits raising
             the caps well above the July interim order; reports the 5,000/1,000/
             1,000 ceilings I could not confirm against a primary order
Paraphrase:  On 2026-08-20 the NTA unanimously approved three permits letting
             Tesla, Uber, and Waymo run paid robotaxi service in Clark County,
             with ceilings of up to 5,000 Tesla vehicles and up to 1,000 each for
             Waymo and Uber over twelve months. Tesla's Cybercab chief engineer
             frames 5,000 as a ceiling, not a plan.
Locators:    body; caps paragraph and Tesla quote
Quote:       Eric Early, Tesla Cybercab chief engineer: "The 5,000 has always been
             a ceiling for us. I don't think we'll be in a position by this time
             next year to deploy 5,000 vehicles" (realistic target "2,500, maybe a
             bit higher").
```

```text
URL:         https://cdn.openai.com/pdf/ten-proofs-oai.pdf
Kind:        primary — OpenAI's own manuscript, "Ten Advances in Mathematics and
             Theoretical Computer Science," read firsthand (text extracted)
Establishes: firsthand, the exact ten results claimed and that they were produced
             by an internal OpenAI model; the document's own date
Paraphrase:  OpenAI presents ten results across mathematics and theoretical
             computer science obtained by "an internal OpenAI model": the exact
             asymptotic strength of the Cohn–Elkies linear program for
             high-dimensional sphere packing; exponential improvements to binary
             and spherical code bounds; an explicit construction of a nonsofic
             group (answering whether every countable group is sofic); a disproof
             of Connes's rigidity conjecture; arithmetic-circuit lower bounds for
             the permanent; exponential quantum parallel repetition; hardness of
             the closest-vector problem via a 3SAT reduction; Ehrhart's volume
             conjecture in every dimension for the stated bodies; a superexponential
             lower bound on multicolor Ramsey numbers R_k(3); and bipartite
             constructions disproving the Erdős–Simonovits compactness conjecture
             and an Erdős degeneracy conjecture. The abstract attributes the work
             to "an internal OpenAI model," not to a named model.
Locators:    title page; Abstract items 1–10; footnote 1
Quote:       "We present a collection of results obtained by an internal OpenAI
             model, spanning mathematics and theoretical computer science";
             "Updated August 6, 2026. The original version can be found at
             https://cdn.openai.com/pdf/ten-proofs-oai-original.pdf."
```

```text
URL:         https://github.com/openai/ten-proofs
Kind:        primary — OpenAI's own repository, the verification artifact itself
Establishes: firsthand, that machine-checkable Lean 4 certificates for the ten
             results are published under an open license
Paraphrase:  The repository holds Lean 4 formalizations of the ten results in the
             manuscript, released under Apache-2.0, listing the same ten topics
             (sphere packing, binary/spherical codes, nonsofic groups, Connes's
             rigidity, arithmetic circuit complexity, quantum parallel repetition,
             closest vector problem, Ehrhart's volume conjecture, multicolor
             Ramsey numbers, extremal-number conjectures). The page frames the
             contents as Lean certificates accompanying the paper, not as new
             discoveries in themselves.
Locators:    repository README and file listing
Quote:       —
```

```text
URL:         https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/
Kind:        secondary — The Decoder reporting on OpenAI's announcement from
             outside OpenAI
Establishes: the "Astra" name and the reported ~$2,000 compute claim, which do
             not appear in the manuscript pages I read; an independent
             mathematician's reaction
Paraphrase:  Reports that OpenAI attributes the ten results to an internal version
             of its next major model, "Astra," and that OpenAI says the tokens to
             generate all ten solutions would have cost about $2,000 at its API
             rates. Notes the results are not peer reviewed. Quotes an outside
             mathematician assessing the constructions as significant.
Locators:    body; cost paragraph; reaction quote
Quote:       Thomas Bloom (University of Manchester, erdosproblems.com): the
             results are "big news ... in terms of constructions, this is big."
```

```text
URL:         https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/
Kind:        secondary — TechCrunch relaying The Information's report; not a party
             to the deal
Establishes: that the Nvidia–Hugging Face acquisition is reported but unconfirmed
             and unsigned; the reported price and prior valuation
Paraphrase:  The Information first reported, citing a source familiar with the
             matter, that Nvidia agreed to buy Hugging Face for about $12.9B
             (reported by others as more than $13B), against Hugging Face's $4.5B
             2023 Series D valuation and roughly $150M annual revenue. Neither
             Nvidia nor Hugging Face responded to requests for comment; Business
             Insider reported the talks had not produced a signed agreement and
             could still collapse. Dated 2026-08-26.
Locators:    body; sourcing and comment paragraphs
Quote:       Business Insider, as relayed: talks "had not yet produced a signed
             agreement and could still atomize."
```

```text
URL:         https://finance.yahoo.com/technology/ai/articles/broadcom-seeks-80-billion-debt-171925920.html
Kind:        secondary — Yahoo Finance relaying CNBC/Bloomberg/Reuters reporting;
             not a party to the financing
Establishes: that Broadcom's reported AI-debt raise rests on anonymous sources
             with no company confirmation, and its reported structure
Paraphrase:  Broadcom is reported (CNBC/Bloomberg via Reuters, ~2026-08-20/21) to
             be seeking $70–80B in debt (a figure some sources push toward $100B)
             tied to AI customers including Anthropic, structured through a
             special-purpose vehicle that mirrors an earlier $35B June arrangement
             with Apollo and Blackstone toward expanding Anthropic's compute.
             Blackstone declined to comment; Broadcom and Apollo did not respond.
             The reporting attributes the figures to anonymous sources, not a
             filing.
Locators:    body; structure and comment paragraphs
Quote:       —
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000054/avgo-20260503.htm
Kind:        primary — Broadcom's own Form 10-Q (fiscal Q2 2026, quarter ended
             2026-05-03), read firsthand
Establishes: firsthand, that this filing does NOT contain the Anthropic backstop
             or AI-rack financing an aggregator attributed to it
Paraphrase:  A review of this 10-Q found no reference to Anthropic, to an investor-
             partner backstop, to AI-rack purchase or lease obligations, or to the
             reported compute-financing arrangement. The quarter it covers ended
             2026-05-03, before the June arrangement the reporting describes, so
             any such disclosure would fall in a later filing, not this one. An
             aggregator claim that this 10-Q disclosed a "$29B maximum exposure"
             backstop is not supported by the document read.
Locators:    full filing; debt and commitments disclosures
Quote:       —
```

```text
URL:         https://www.thomsonreuters.com/en/press-releases/2026/august/thomson-reuters-leverages-its-world-class-data-assets-to-launch-its-own-frontier-model
Kind:        primary — Thomson Reuters's own press release, read firsthand
Establishes: firsthand, the launch of an in-house model and the company's own
             framing and figures
Paraphrase:  On 2026-08-24 Thomson Reuters announces "Thomson," its first
             proprietary large language model, built from a strong open-source
             foundation (unnamed) with a stated $40M training investment. The
             company calls it a "frontier model" while emphasizing efficiency over
             scale, claims early evaluations "on par with the latest frontier
             models" on a range of tasks, and positions it for deployment inside
             CoCounsel legal and tax products, with a small version on Hugging Face
             for academic evaluation. This is a product launch with in-house-model
             framing, not an independent research result.
Locators:    press release body; benchmark and deployment paragraphs
Quote:       Title: "Thomson Reuters Leverages its World-Class Data Assets to
             Launch Its Own Frontier Model."
```

```text
URL:         https://techstartups.com/2026/08/27/top-tech-news-today-august-27-2026-amazon-apple-google-meta-nvidia-openai-salesforce-more/
Kind:        secondary — a same-day aggregated roundup, used only to enumerate
             candidate leads for later verification, not as proof of any claim
Establishes: the existence of same-day claims (Nvidia earnings, an Anthropic–
             Nscale compute deal, a Hugging Face/Pollen "Microduck" robot, a
             reported Nvidia–Groq acquisition, others); none confirmed here
Paraphrase:  Lists August-27 items including Nvidia's quarterly results, a
             reported Anthropic–Nscale compute agreement ($45B over six years, 460
             MW), a Hugging Face/Pollen Robotics "Microduck" $399 biped, a claimed
             Nvidia acquisition of Groq, a Google speech model, a Salesforce–
             Anthropic integration, and Kioxia/Sandisk memory investment. Each is a
             claim to confirm against a primary; several are dubious (see
             Discarded).
Locators:    roundup list
Quote:       —
```

## Contradictions

- **Robotaxi fleet size: ten vs. thousands.** The only permit document I could
  open (NTA AVNC Permit 002, Docket 26-05015, dated 2026-07-27) caps Tesla at ten
  vehicles on the Strip corridor. The widely reported 5,000-vehicle Tesla ceiling
  (and the 8,000 combined) comes from the 2026-08-20 full-permit approval, for
  which I could not retrieve a primary NTA order. The two are a chronology, not a
  conflict: the July order was interim, the August approval superseded it. But the
  writer must not present 5,000 as a first-party-confirmed figure. Firsthand
  primary supports ten; 5,000/8,000 rest on secondary reporting (TechCrunch,
  Engadget, Electrek). Tesla's own engineer calls 5,000 a ceiling and ~2,500 the
  realistic near-term number.

- **Nvidia–Hugging Face: reported, not confirmed.** Every account traces to a
  single origin (The Information) citing one source. Neither company has confirmed
  or commented; the agreement is unsigned and, per Business Insider, could still
  collapse. There is no primary. The $12.9–13B price is a reported figure, not an
  owned one. Under the commission's floor this item has one secondary origin (many
  retellings of it) and zero primary.

- **Broadcom debt raise: no primary, and one aggregator claim is false.** The
  $60–80B raise is anonymous-sourced with no company confirmation. An aggregator
  claim that Broadcom's Q2 FY2026 10-Q disclosed a "$29B maximum exposure"
  backstop is not supported by the filing I read; that quarter closed before the
  June arrangement the reporting describes.

- **"Astra" is a press label, not the manuscript's term.** OpenAI's manuscript
  credits "an internal OpenAI model." The name "Astra," and the ~$2,000 compute
  claim, appear in OpenAI's announcement page (which I could not open, HTTP 403)
  and in secondary reporting, not in the manuscript pages I read. Attribute the
  name and the cost figure to the announcement/secondary layer, not to the paper.

- **The math results are real but off-date and unrefereed.** The manuscript is
  dated 2026-08-01, updated 2026-08-06 — about four weeks before this edition. The
  results are Lean-verified (the GitHub certificates are the check) but have not
  been through journal peer review. Any use in a 2026-08-28 brief must treat this
  as prior news being built on, not as the day's development.

- **Boundary tension on two on-date items.** Nvidia's quarterly earnings
  (2026-08-27) and, arguably, the Nevada robotaxi approval are public-consequence
  and markets-adjacent. The commission routes markets and macro to the
  current-events brief. I flag both rather than decide; the robotaxi item is
  defensible here as a technology-deployment milestone, the earnings item much less
  so.

## Numbers

```text
Figure: 2,000,000 additional NVIDIA GPUs
Owner:  AWS newsroom (aboutamazon.com), the authoring party
Scope:  deployed across AWS global infrastructure in 2027–2028; on top of >1M
        committed earlier in 2026 (per secondary), total introduced this year
        reported as >3M
```

```text
Figure: 100,000 NVIDIA GPUs for U.S. government AI factories
Owner:  AWS newsroom (aboutamazon.com)
Scope:  on secure AWS infrastructure at Impact Level 6 (IL6) and above
```

```text
Figure: 10 (ten) vehicles — Tesla interim fleet cap
Owner:  NTA AVNC Permit 002, Docket 26-05015 (primary, firsthand)
Scope:  Clark County, Las Vegas Strip corridor; interim order dated 2026-07-27
```

```text
Figure: up to 5,000 Tesla / 1,000 Waymo / 1,000 Uber (≈8,000 combined) vehicles
Owner:  reported from the 2026-08-20 NTA approval; NO primary order opened
Scope:  Clark County, over 12 months; ceilings, not deployment plans (Tesla's
        engineer: ~2,500 realistic)
```

```text
Figure: ~$12.9B–$13B (Nvidia–Hugging Face)
Owner:  UNVERIFIED — reported by The Information; no company confirmation, unsigned
Scope:  against Hugging Face's $4.5B 2023 valuation and ~$150M annual revenue
        (both also reported, not primary-confirmed here)
```

```text
Figure: $70–80B (up to ~$100B in some accounts) — Broadcom AI-debt raise
Owner:  UNVERIFIED — anonymous sources via CNBC/Bloomberg/Reuters; no filing
Scope:  reported SPV structure extending a $35B June Apollo/Blackstone/Anthropic
        arrangement; Broadcom and Apollo did not comment
```

```text
Figure: ~$2,000 compute cost for all ten proofs
Owner:  OpenAI, as reported by secondary (the-decoder); not found in the
        manuscript pages read, and the announcement page was inaccessible (403)
Scope:  OpenAI's stated token cost at its own API rates; a claim, not an
        independently checkable figure
```

```text
Figure: $40M training investment — Thomson Reuters "Thomson" model
Owner:  Thomson Reuters press release (primary)
Scope:  in-house model built on an unnamed open-source foundation; "on par with
        latest frontier models" is the company's own early-evaluation claim
```

## Source assets

```text
Asset: NTA AVNC Permit 002 — the RESTRICTIONS paragraph and signature/seal block
       (nta.nv.gov PDF, p. 1)
Shows: the ten-vehicle cap, Strip-corridor geofence, 45 mph limit, and airport
       exclusion in the Authority's own words, with the state seal and signatures
       that make it the authentic order rather than a paraphrase
Crop:  must retain the "maximum fleet of ten (10)" clause and the "Dated: July 27,
       2026" line; omit nothing that changes the cap or the date
```

```text
Asset: OpenAI manuscript — the Abstract's numbered list of the ten results
       (cdn.openai.com PDF, title/abstract page)
Shows: the exact scope and phrasing of each claimed advance in the authors' own
       words, including that the work is credited to "an internal OpenAI model"
Crop:  keep the "internal OpenAI model" attribution if the list is shown; do not
       crop in a way that implies a named, released model produced it
```

```text
Asset: openai/ten-proofs repository — the file listing and Apache-2.0 license
Shows: that machine-checkable Lean 4 certificates, not just prose, back the claim
Crop:  n/a (structural evidence, best cited than imaged)
```

```text
Asset: AWS–NVIDIA expansion — None found. The primary is text; no first-party
       chart or figure carries the two-million-GPU claim better than the sentence.
```

## Discarded

```text
URL: https://www.cnbc.com/2026/08/27/nvidia-hugging-face-acquisition.html — HTTP 403; could not open, so not cited. TechCrunch used for the same claim.
URL: https://www.forbes.com/sites/siladityaray/2026/08/27/... — HTTP 403; not opened.
URL: https://openai.com/index/ten-advances-in-mathematics/ — HTTP 403; the announcement's own page could not be opened. Manuscript and GitHub used instead; "Astra" name and $2,000 figure attributed to secondary.
URL: Nvidia quarterly earnings (2026-08-27, NVIDIA release / Form 10-Q nvda-20260726) — real and primary-available, but routed to current-events by the markets/macro boundary; primary NOT opened, so no figure asserted here. Flagged as a lead only.
URL: Anthropic–Nscale compute deal ($45B/460MW, 2026-08-27, Bloomberg per roundup) — plausible infrastructure lead; no primary or independent secondary opened; UNVERIFIED. Offered to the writer only if they want a second infra item and can verify it.
URL: Hugging Face/Pollen Robotics "Microduck" $399 biped (2026-08-27) — product promotion; does not qualify on its own under the series prompt.
URL: Reported "Nvidia acquires Groq for $20B" (aggregator roundup) — highly dubious (Groq is a competing inference vendor); no primary; treat as likely erroneous unless a filing appears.
URL: Thomson Reuters "Thomson" model (2026-08-24, primary opened) — kept as a documented candidate but flagged as a product launch with in-house-model framing; likely fails the "product promotion does not qualify on its own" bar.
URL: Google speech model / Salesforce–Anthropic integration / Kioxia–Sandisk memory (aggregator roundup) — unverified same-day claims; no primary opened; not qualifying without verification.
URL: Materials/photonics science items (Caltech low-loss waveguides ~2026-08-17; femtosecond hidden-state observation ~2026-08-21; DNA–semiconductor memory ~2026-08-17) — mid-August and off-peak for this edition; primaries not opened; not pursued given the week's clearer infrastructure weight.
```
