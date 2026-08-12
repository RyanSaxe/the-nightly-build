# Evidence: tech-news/2026-08-12 (03)

This final pass settles the item pool at three, each with a primary and an
independent secondary. The 12 August total solar eclipse and its coronal-science
campaigns carry a NASA primary and an independent AFP/phys.org secondary. Dyna-1,
the model that reads protein millisecond motion from the peaks missing in NMR
spectra (Nature, 10 August), carries a Nature primary and two independent
secondaries, with the standing caveat that both predate the Nature publication
because the result circulated as a March 2025 preprint. Added this round under the
orchestrator's boundary override: Anthropic now marks Claude's text output (about
11 August), sourced to Anthropic's own support documentation plus an independent
TechCrunch account, and recorded with the honest caveat that Anthropic did not
disclose how the text watermark works. The phosphine-mediated azine C–H coupling
paper (Nature, 11 August) is dropped: after a final search of C&EN, Chemistry
World, phys.org, EurekAlert and Colorado State's own chemistry news page, no
independent secondary exists, and the only non-Nature page carrying it is an
abstract-republishing aggregator that the brief rules out. The pool therefore
reaches three qualifying items, not four. Three is the acceptable floor with a
length warning; the edition should run short rather than pad. Round-02's verified
work is preserved; additions and the drop are marked [03].

## Sources

```text
URL:         https://science.nasa.gov/eclipses/future-eclipses/total-solar-eclipse-on-august-12-2026/
Kind:        primary — NASA's own eclipse page; NASA owns the event parameters and the US science plan.
Establishes: The 12 August 2026 total solar eclipse date, path, and duration of totality, firsthand.
Paraphrase:  A total solar eclipse on 12 August 2026 sweeps across Greenland, Iceland, northern Russia,
             the Atlantic, Spain and a small corner of Portugal. Totality lasts under two minutes for
             most observers and a little under two and a half minutes near the path center. Western
             European and African observers see the Sun set while still partially eclipsed.
Locators:    Page body, "Where and When" and duration sections.
Quote:       "still less than two and a half minutes"
```

```text
URL:         https://science.nasa.gov/science-research/heliophysics/nasa-science-soars-during-august-total-solar-eclipse/
Kind:        primary — NASA heliophysics account of its own funded campaign (a plan, dated 30 July 2026, not results).
Establishes: The instruments and questions NASA is flying against the eclipse; firsthand for the plan.
Paraphrase:  NASA-funded teams chase the Moon's shadow with the WB-57 high-altitude jet carrying the
             SCIFLI Multispectral Airborne Imager (four cameras), flying at 50,000 feet and about 460
             mph, capturing at least 20 corona images per second and extending totality to nearly three
             minutes versus 2 minutes 18 seconds on the ground. Iceland teams fly 80 balloons, Spain
             teams six with 360-degree cameras, from 18 hours before to 8 hours after totality. Targets:
             the corona-heating problem, prominence formation, the atmospheric boundary layer, ozone,
             and the corona-to-solar-wind link.
Locators:    Instruments and "Balloons"/"Science" sections; page last updated 30 July 2026.
Quote:       "at least 20 images per second"
```

```text
URL:         https://phys.org/news/2026-08-total-eclipse-scientists-chance-probe.html
Kind:        secondary — AFP wire report carried by phys.org; a newsroom independent of NASA and ESA,
             though it quotes both agencies. Independent author, not a campaign owner.
Establishes: Independent confirmation that the 12 August eclipse is a coordinated coronal-science event,
             and that European teams (France's CEA, ESA's Solar Orbiter and Proba-3) are observing.
Paraphrase:  AFP reports that scientists will use the eclipse to study the corona and chromosphere, the
             Sun's magnetic field and the origins of the solar wind, naming France's CEA, ESA's Solar
             Orbiter, and the Proba-3 formation-flying mission, with a future MESOM concept to place a
             craft in the Moon's shadow. Dated 5 August 2026.
Locators:    Body; dateline 5 August 2026 (AFP).
Quote:       "Next week, CEA scientists will focus on the sun's corona, the outermost layer of its atmosphere."
```

```text
URL:         https://www.nature.com/articles/s41586-026-10989-4
Kind:        primary — the Nature research paper; the authoring group owns the model and the claim.
Establishes: Dyna-1, a deep-learning model that predicts microsecond-to-millisecond protein dynamics
             from missing NMR chemical-shift assignments. Published 10 August 2026.
Paraphrase:  Wayment-Steele, El Nesr, Hettiarachchi, Ojoawo, Kariyawasam, Ovchinnikov and Kern assume
             that residues left unassigned in NMR chemical-shift data are exchange-broadened by µs–ms
             motion, and train models on that signal drawn from roughly 10,000 proteins in the
             Biological Magnetic Resonance Data Bank. After curating more than 100 NMR relaxation
             datasets (they call the set RelaxDB, 133 proteins), they show the model also predicts
             exchange measured by independent NMR relaxation experiments, including motion tied to
             enzyme catalysis and ligand binding. The best model uses an intermediate layer of the ESM
             protein language model.
Locators:    Abstract; author list; "Published: 10 August 2026" on the article page.
Quote:       (dataset) "~10,000 proteins deposited in the Biological Magnetic Resonance Data Bank (BMRB)"
```

```text
URL:         https://cbirt.net/dyna-1-unraveling-protein-dynamics-with-deep-learning-and-nmr-data/
Kind:        secondary — independent coverage by CBIRT (Centre of Bioinformatics Research & Technology),
             author Deotima Chakraborty, not a paper author.
Establishes: An independent account of the Dyna-1 result. Dated 5 April 2025 — it covers the bioRxiv
             preprint, so it establishes the result was reported and independently written up well
             before the Nature publication, not that the Nature paper was covered on 10 August.
Paraphrase:  CBIRT describes Dyna-1 as a deep-learning model trained on NMR data that predicts µs–ms
             protein motion by treating NMR signals broadened beyond detection as labels, using an ESM
             intermediate layer.
Locators:    "About Deep Learning Model Dyna-1" section; dated 5 April 2025.
Quote:       "Dyna-1 ... can predict physiologically relevant µs-ms motions based on measurements of
             µs-ms motion collected by numerous separate labs on proteins ... described using various
             types of studies."
```

```text
URL:         https://newsletter.kiin.bio/p/dyna-1-learning-protein-dynamics
Kind:        secondary — independent coverage by Kiin Bio Weekly (Substack), authors Kiin Bio and
             Natasha Kilroy, not paper authors.
Establishes: A second independent account of the Dyna-1 result. Dated 6 November 2025 — again a
             preprint-era write-up, not coverage of the 10 August Nature publication.
Paraphrase:  Describes Dyna-1 as learning µs–ms dynamics from missing NMR amide-backbone assignments,
             using ESM embeddings, trained on roughly 9,400 curated proteins, predictive of
             functionally important motions.
Locators:    Body; dated 6 November 2025.
Quote:       "Dyna-1 learns something remarkable about proteins not from what is present in NMR data,
             but from what is missing."
```

```text
URL:         https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content   [added 03]
Kind:        primary — Anthropic's own support documentation; Anthropic owns what it will do to Claude output.
Establishes: That Claude embeds an imperceptible watermark in generated text and attaches C2PA
             provenance metadata to generated files; models launched on or after 2 August 2026 mark at
             launch, with older models being retrofitted. Page updated 11 August 2026.
Paraphrase:  Anthropic states Claude weaves an imperceptible watermark into generated text that survives
             copy-paste and "may persist through some editing," and attaches signed C2PA provenance
             metadata to SVG, PNG and JPG files. Models launched 2 August 2026 or later mark at launch;
             older models are being retrofitted. A detected mark means content "may have been processed
             by Claude" and is not conclusive, since Claude may only have edited existing material.
             Disclosed: that text is marked, that the mark survives copy-paste, the file formats, the
             C2PA standard, model coverage, and the non-conclusiveness of a hit. NOT disclosed: how the
             text watermark is constructed, and how much editing removes it.
Locators:    Sections on text marking, file metadata, model coverage, and the limitation note; page
             states it was updated 11 August 2026.
Quote:       "it weaves an imperceptible watermark directly into the text itself"
```

```text
URL:         https://techcrunch.com/2026/08/11/anthropic-says-it-will-watermark-text-generated-by-its-ai-models/   [added 03]
Kind:        secondary — independent US newsroom (TechCrunch) reporting on the Anthropic announcement.
Establishes: Independent confirmation of the 11 August 2026 announcement, of the EU-AI-Act framing, and
             that the text-watermark mechanism and its removability are undisclosed. It establishes that
             the claim was made and independently reported, not how the watermark works.
Paraphrase:  TechCrunch reports Anthropic will watermark Claude text and use C2PA for files to meet EU
             AI Act transparency rules effective 2 August 2026, links Anthropic's support page, and notes
             it is unclear how much editing removes the text watermark; Anthropic had not answered its
             request for detail by publication.
Locators:    Body; dated 11 August 2026.
Quote:       "It's not clear how much editing users need to do to remove the watermark."
```

## Contradictions

- The 4-item floor versus what 12 August produced. Honest verification yields three
  qualifying items (eclipse; Dyna-1; Anthropic text-marking), not four. The azine
  C–H coupling paper is a verified primary with no independent secondary anywhere I
  could reach, so it is dropped rather than propped up with an aggregator. The gap
  is a real property of the day, confirmed against Nature's full 10–12 August
  research list, the AI-release trackers, and the science wires.
- Wire dates versus primary dates. Science-news aggregators repeatedly restamp
  older results: the "11 August 2026" ScienceDaily super-steel item traces to a
  2023 Materials Today / Science Advances result; its "11 August" MIT
  language-versus-reasoning item is a July 2026 PNAS paper. The centromere and
  Raygun papers (both Nature, 29 July) and the magnetar vacuum-birefringence paper
  (~6 August) were similarly miscredited to mid-August. Every date here is from the
  owning primary.
- Dyna-1's news event versus its independent coverage. The news is the 10 August
  Nature publication, but the independent secondaries (CBIRT, 5 April 2025; Kiin
  Bio, 6 November 2025) cover the March 2025 preprint. They are genuine independent
  accounts of the same result; none reports the Nature publication itself. The
  editor should decide whether preprint-era secondaries satisfy the template.
- The eclipse is an observing campaign, not a same-day laboratory result. It is the
  one development genuinely dated 12 August, so it anchors the edition, but it
  should be written as a campaign whose payoff follows the data, not as a result.
- The Anthropic item's technical content is thin by the lab's own choice. The
  development is real and in scope as a change to how a widely used model behaves,
  but the only verifiable technical facts are the C2PA file standard, the model
  coverage cutoff, and that text is marked at all. The mechanism and robustness are
  undisclosed, and a detected mark is explicitly non-conclusive. The item must be
  written with that caveat, not as a solved provenance guarantee.

## Numbers

```text
Figure: totality lasts under 2 min 30 s at maximum; ~2 min 18 s from the ground
Owner:  NASA (science.nasa.gov eclipse pages)
Scope:  12 August 2026 eclipse; duration at path center vs. a fixed ground site
```

```text
Figure: WB-57 jet at 50,000 ft, ~460 mph, ≥20 corona images/second, ~3 min observation window
Owner:  NASA heliophysics ("NASA Science Soars...")
Scope:  Single instrumented aircraft flight on eclipse day
```

```text
Figure: 80 scientific balloons (Iceland) and 6 balloons (Spain, 360-degree cameras)
Owner:  NASA heliophysics
Scope:  Campaign counts, launch window 18 h before to 8 h after totality
```

```text
Figure: training signal from ~10,000 proteins (BMRB); RelaxDB of 133 proteins with relaxation data
Owner:  Nature s41586-026-10989-4 (Dyna-1)
Scope:  Model training/validation corpus; µs–ms exchange prediction
```

```text
Figure: text marking applies to Claude models launched on/after 2 August 2026; C2PA metadata for SVG/PNG/JPG
Owner:  Anthropic support article 16266773
Scope:  Model coverage and file formats; text-watermark robustness not quantified by Anthropic
```

## Source assets

```text
Asset: Eclipse path-of-totality map on the NASA science.nasa.gov eclipse page
Shows: Where totality falls (Greenland, Iceland, Spain, Portugal) and the partial-eclipse footprint
Crop:  Must retain the country labels and the path centerline; omit the surrounding site chrome
```

```text
Asset: WB-57 / SAMI corona-imaging description on the NASA "Soars" page
Shows: How the airborne campaign extends totality and what the corona instruments capture
Crop:  Keep the altitude/speed/frame-rate figures legible if a figure is used; no decorative shots
```

```text
Asset: Dyna-1 schematic in Nature s41586-026-10989-4 (missing-assignment signal to predicted dynamics)
Shows: The core idea — absence in an NMR spectrum used as a label for µs–ms motion
Crop:  Must retain the "missing assignment -> exchange" mapping; omit unrelated benchmark panels
```

```text
Asset: The Anthropic support article itself (support.claude.com 16266773)
Shows: In the lab's own words, what is marked, the C2PA standard, and the non-conclusive-detection caveat
Crop:  If quoted as an image, keep the limitation sentence intact so the caveat travels with the claim
```

## Discarded

```text
URL: https://www.nature.com/articles/s41586-026-10991-w — phosphine-mediated azine C–H coupling; verified Nature primary (11 Aug), but DROPPED for want of any independent secondary. Final search of C&EN, Chemistry World, phys.org, EurekAlert and Colorado State's own chemistry news page found none; the CSU/EurekAlert hits cover a different May 2024 McNally paper. The only non-Nature page is csnsf.org, an abstract-republishing aggregator, which the brief rules out.
URL: https://csnsf.org/phosphine-mediated-azine-c-h-couplings-with-water-and-ammonia/ — auto-aggregator republishing the Nature azine abstract; not independent reporting, explicitly not to be attached.
URL: https://www.sciencedaily.com/releases/2026/08/260811052717.htm — "super steel" (SS-H2, HKU); a 2023 Materials Today / Science Advances result reposted, not a 10–12 Aug development.
URL: https://www.sciencedaily.com/releases/2026/08/260811011140.htm — MIT logic-vs-language brain systems; the underlying PNAS paper and MIT News are dated early July 2026, not 11 Aug.
URL: https://www.nature.com/articles/s41586-026-10841-9 — human-centromere paper; Published 29 July 2026, not a 12 Aug development.
URL: https://www.nature.com/articles/s41586-026-10842-8 — Raygun protein resizing; Published 29 July 2026, not 12 Aug.
URL: https://www.nature.com/articles/s41586-026-10859-z — magnetar vacuum birefringence; ~6 Aug 2026 and contested by an April 2026 reanalysis.
URL: https://thinkingmachines.ai/news/introducing-inkling/ — Inkling open-weights model; dated 15 July 2026 and a mixture-of-experts model, which the commission bars centering an item on.
URL: https://nvidianews.nvidia.com/news/nvidia-releases-new-physical-ai-models-as-global-partners-unveil-next-generation-robots — Cosmos/Isaac physical-AI models; dated 5 January 2026, stale.
URL: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/ — WeatherNext cyclones; 6 Aug 2026, not 12 Aug.
URL: techstartups / CNBC (Nvidia $500bn financing, Intel $20bn raise, Sony-TSMC $4.7bn JV, Unitree IPO, Meta Muse Glimmer, GPT-5.6-Cyber) — markets/business, product releases, or the already-covered AI-security thread; out of scope for this brief.
URL: Google "Made by Google" / Pixel 11 event (12 Aug 2026) — genuinely dated 12 Aug but product promotion, screened out by the series brief.
URL: llm-stats.com/ai-news, llmgateway.io/timeline, digitalapplied.com tracker — aggregators; no model releases dated 11–13 Aug, confirming the AI-release lull.
URL: space.com and smithsonianmag.com eclipse features, skyandtelescope.org campaign piece, esa.int virtual-totality page — independent eclipse coverage that exists and would serve as extra secondaries, but each returned HTTP 403 or a gated/truncated body, so no passage could be read to cite; the AFP/phys.org secondary is used instead.
```

## Closing note to the orchestrator

Final honest pool: three items, each with a primary and an independent secondary.
(1) The 12 August total solar eclipse coronal-science campaign — NASA primary,
AFP/phys.org secondary; an event, not a result. (2) Dyna-1 — Nature primary, two
independent secondaries, both preprint-era. (3) Anthropic marks Claude's text
output — Anthropic support-page primary, TechCrunch secondary, mechanism
undisclosed. The azine C–H coupling paper is dropped for lack of any independent
secondary. Four items each with primary plus independent secondary is not
achievable honestly for this date; three is the pool, which is acceptable with a
length warning. I recommend running the three and letting the edition be short
rather than padding with the misdated wire items, the product/markets stories, or
the aggregator.
