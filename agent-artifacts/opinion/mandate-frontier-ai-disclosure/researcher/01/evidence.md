# Evidence record: opinion/mandate-frontier-ai-disclosure (01)

The evidence firmly supports the *occasion* and the *factual scaffolding* of the
commissioned thesis. The two live regimes are confirmed from their owning
instruments: on 2 August 2026 the European Commission's AI Office gained powers
to enforce the EU AI Act's general-purpose AI (GPAI) obligations (in force since
2 August 2025), and California's SB 53 — a developer-only transparency and
incident-reporting law, effective 1 January 2026 — is the only enforceable US
frontier-AI regime. Every threshold, deadline, and penalty in the commission is
verified against its primary. Named holders exist on both sides with real
standing and cited words: Senator Scott Wiener and Anthropic for a federal
transparency floor; Martin Casado, Matt Perault (both a16z), and Meta's Joel
Kaplan against disclosure mandates.

The evidence is **thin on the load-bearing causal claim** the thesis needs: I
found no source demonstrating that a transparency/disclosure floor actually
reduces catastrophic risk. Worse for the thesis, the best available natural
experiment cuts against it — leading developers largely *ignored* the EU's
training-data disclosure duty during the pre-enforcement window, suggesting
disclosure without teeth yields vague box-ticking. And the strongest pro-holder,
Dario Amodei, publicly declared in June 2026 that transparency alone is *no
longer enough* — complicating any thesis that a narrow disclosure-only floor is
the right national ceiling. These belong in Contradictions and the counter, and
the writer must not overstate efficacy.

## Sources

```text
URL:         https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53
Kind:        primary — the enacted California statute text; it owns every SB 53 threshold, deadline, and penalty.
Establishes: SB 53 (Transparency in Frontier Artificial Intelligence Act) definitions, disclosure duties, incident-reporting deadlines, penalty, enforcement authority.
Paraphrase:  "Frontier developer" = trained/initiated training of a frontier model using ≥10^26 computing operations (§22757.11(h),(i)). "Large frontier developer" = affiliates with annual gross revenues over $500,000,000 in the prior year (§22757.11(j)). Large developers must publish a frontier AI framework (§22757.12) and a transparency report before deployment (§22757.12(c)), transmit catastrophic-risk summaries to the Office of Emergency Services, report critical safety incidents within 15 days (§22757.13(c)(1)) or within 24 hours where there is imminent risk of death/serious physical injury (§22757.13(c)(2)), and honor whistleblower protections (§1107.1). Civil penalty up to $1,000,000 per violation, Attorney General enforced (§22757.15).
Locators:    §§22757.11–22757.15; §1107.1.
Quote:       Catastrophic risk (§22757.11(c)): "a foreseeable and material risk that a frontier developer's development, storage, use, or deployment of a frontier model will materially contribute to the death of, or serious injury to, more than 50 people or more than one billion dollars ($1,000,000,000) in damage to, or loss of, property arising from a single incident." Penalty (§22757.15): a civil penalty "does not exceed one million dollars ($1,000,000) per violation."
```

```text
URL:         https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
Kind:        primary — the European Commission's own statement of the AI Act timeline.
Establishes: The occasion date and applicability sequence from the enforcing authority.
Paraphrase:  The AI Act entered into force 1 August 2024; governance rules and GPAI obligations took effect August 2025; from 2 August 2026 the AI Office and Member-State authorities are responsible for implementing, supervising, and enforcing the Act.
Locators:    "Regulatory framework" timeline section.
Quote:       "The AI Act rules on GPAI became effective in August 2025." From 2 August 2026 "the AI Office and authorities of the Member States are responsible for implementing, supervising and enforcing the AI Act."
```

```text
URL:         https://artificialintelligenceact.eu/article/55/
Kind:        secondary compiler that reproduces the primary regulation text of Article 55 verbatim; treat the quoted article language as primary, the site as the transport.
Establishes: What GPAI-with-systemic-risk providers must do — the substance the AI Office now enforces.
Paraphrase:  Providers of GPAI models with systemic risk must perform state-of-the-art model evaluation including adversarial testing; assess and mitigate systemic risks at Union level; keep track of, document, and report serious incidents to the AI Office without undue delay; and ensure adequate cybersecurity for the model and its physical infrastructure. Approved codes of practice can demonstrate compliance until harmonized standards exist.
Locators:    Article 55(1)(a)–(d).
Quote:       Must "perform model evaluation … including conducting and documenting adversarial testing"; must "keep track of, document, and report, without undue delay, to the AI Office … relevant information about serious incidents."
```

```text
URL:         https://artificialintelligenceact.eu/article/51/
Kind:        secondary compiler reproducing Article 51 primary text; quoted language is primary.
Establishes: The EU systemic-risk compute threshold — the counterpart to SB 53's 10^26.
Paraphrase:  A GPAI model is presumed to have high-impact capabilities (systemic risk) when cumulative training compute exceeds 10^25 FLOP; the Commission may also designate by technical assessment or decision under Annex XIII.
Locators:    Article 51(1)–(2).
Quote:       Presumption applies where "the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25."
```

```text
URL:         https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/
Kind:        secondary — explainer summarizing the enforcement regime; useful for the fine figure and the enforcement-power inventory.
Establishes: What the AI Office can do from 2 August 2026 and the maximum fine.
Paraphrase:  From 2 August 2026 the Commission/AI Office may request documentation, run technical evaluations, demand compliance and risk-mitigation measures, restrict or withdraw a model from the EU market, and fine. Legacy models (pre-2 Aug 2025) have until 2 August 2027 to comply. Article 101 fines: up to 3% of worldwide annual turnover or €15,000,000, whichever is higher.
Locators:    "Enforcement powers"; "Fines" (Article 101).
Quote:       Article 101 fines up to "3 % of their annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is higher."
```

```text
URL:         https://www.anthropic.com/news/anthropic-is-endorsing-sb-53
Kind:        primary — Anthropic's own stated policy position. NOTE THE STAKE: Anthropic is a frontier developer that already publishes an RSP and system cards, so a mandate formalizes its existing practice while raising rivals' costs. Also the entity behind this paper. Record as a self-interested named holder.
Establishes: A named lab with standing backing SB 53's disclosure core AND a federal transparency floor.
Paraphrase:  Anthropic endorses SB 53 and states its preference for federal action over a state patchwork. It describes SB 53's duties as: publish safety frameworks covering how catastrophic risks are managed/assessed/mitigated; release public transparency reports summarizing catastrophic-risk assessments; report critical safety incidents to the state within 15 days; provide whistleblower protections; face monetary penalties for breaking framework commitments.
Locators:    Endorsement post body.
Quote:       "While we believe that frontier AI safety is best addressed at the federal level instead of a patchwork of state regulations, powerful AI advancements won't wait for consensus in Washington."
```

```text
URL:         https://darioamodei.com/post/policy-on-the-ai-exponential
Kind:        primary — Amodei's own June 2026 policy essay.
Establishes: The strongest pro-transparency holder now argues disclosure alone is insufficient — a crucial complication for a disclosure-only thesis.
Paraphrase:  Amodei says he supported transparency legislation (SB 53, NY RAISE, IL SB 315, and a federal standard) as an appropriate first step under uncertainty, to gain visibility into emerging risks. He now argues that with risks materializing, it is time to move beyond transparency to binding regulation: mandatory third-party evaluations across cybersecurity, biological weapons, loss of control, and automated R&D acceleration, plus government power to block or cancel deployment (an FAA-style model).
Locators:    Sections on transparency and on binding rules.
Quote:       "It is time to go beyond transparency to more serious and binding regulation of AI."
```

```text
URL:         https://missionlocal.org/2026/05/sf-congress-scott-wiener-tech-ai-safety-platform/
Kind:        secondary — reports Senator Wiener's federal AI-safety platform (his statements are the primary; this outlet carries them).
Establishes: A named lawmaker with standing (SB 53's author, now a congressional candidate) advocating a federal version of the disclosure regime.
Paraphrase:  Wiener's federal platform would require large developers to publish the safety measures they take, including model specs; have third parties verify compliance with minimum safety standards such as dangerous-capability testing; protect whistleblowers; and back it with large fines and injunctions. He frames uniform federal standards as the ideal, with California acting because Washington has not.
Locators:    Platform description; Wiener quotes.
Quote:       Wiener: "in an ideal world we would have … federal AI standards." He wants large developers to "make the safety measures they take public, including 'model specs.'"
```

```text
URL:         https://a16z.com/base-ai-policy-on-evidence-not-existential-angst/
Kind:        primary — a16z's own policy position, bylined Martin Casado, General Partner (Infrastructure), Andreessen Horowitz.
Establishes: The evidence/marginal-risk counter — regulate only once genuinely new risks are understood, not from speculation.
Paraphrase:  Casado argues AI marginal-risk claims remain "research questions and hypotheticals," that past alarms (GPT-2 "too dangerous to release") proved unfounded after years of deployment, and that expansive preemptive policy invites regulatory capture and harms US competitiveness. Policy should depart from existing regimes only after the marginal risk of AI over existing computer systems is understood.
Locators:    Body argument.
Quote:       "We should only depart from the existing regulatory regime, and carve new ground, once we understand the marginal risks of AI relative to existing computer systems."
```

```text
URL:         https://a16z.com/ai-model-facts-transparency-that-works-for-little-tech/
Kind:        primary — a16z position, bylined Matt Perault, Head of AI Policy, Andreessen Horowitz.
Establishes: The incumbent-entrenchment / Little Tech / patchwork counter — the strongest cited case against a heavy disclosure mandate.
Paraphrase:  Perault argues compliance is expensive and diverts startup resources; that mandates forcing developers to "express a view" on speculative, politically fraught safety questions are subjective; that a 50-state patchwork of transparency obligations overwhelms small teams; and that the long-term effect is greater market concentration favoring large platforms over Little Tech. He proposes a lightweight "AI Model Facts" sheet (knowledge cutoff, release date, language support, HQ location, ToS links, benchmark performance) as low-burden disclosure instead.
Locators:    Argument and proposal sections.
Quote:       "Compliance with a 50-state patchwork of state transparency obligations would present massive challenges for companies with small engineering, law, and policy teams." The mandates' "long-term effect will be to increase concentration in AI markets."
```

```text
URL:         https://iapp.org/news/a/ca-s-sb-53-eu-ai-act-are-both-governance-frameworks-but-the-similarities-end-there
Kind:        secondary — IAPP analysis by Haley Fine, CIPP/E.
Establishes: The two regimes diverge materially beyond surface similarity — needed so the piece does not equate them.
Paraphrase:  Fine argues the EU AI Act regulates the whole ecosystem (providers and deployers) while SB 53 reaches only frontier-model developers; SB 53 targets narrowly defined "catastrophic risk" while the EU imposes broader prescriptive risk management; only the EU requires a pre-market conformity assessment (SB 53 has no licensing). Incident-reporting triggers differ (SB 53's fixed 15-day/24-hour clock vs the EU's "as soon as the provider realizes").
Locators:    Scope, risk-definition, conformity-assessment, incident-reporting sections.
Quote:       Fine: organizations in scope of both "will need AI governance programs that integrate both frameworks"; on scope, "SB 53 is very unlikely to apply to organizations that would be" EU deployers.
```

```text
URL:         https://www.techpolicy.press/how-big-ai-developers-are-skirting-a-mandate-for-training-data-transparency/
Kind:        secondary — analysis by Dick Blankvoort, Harshvardhan Pandit, and Maximilian Gahntz.
Establishes: The strongest breaking evidence — a disclosure mandate the AI Office had not yet begun enforcing was largely ignored by the biggest labs.
Paraphrase:  The authors find that, despite the EU AI Act duty to publish training-data summaries, leading developers (OpenAI, Google, xAI) had not published usable summaries, exploiting the pre-enforcement gray area, while a smaller open-source developer (Hugging Face) complied substantively. This is direct evidence that disclosure without active enforcement produces minimal or absent compliance.
Locators:    Findings on published summaries and the enforcement gap.
Quote:       "there still aren't any published summaries to assess from leading AI developers"; the companies "have failed to do so."
```

```text
URL:         https://www.engadget.com/ai/meta-says-it-wont-sign-the-eus-ai-code-of-practice-190132690.html
Kind:        secondary — reports Joel Kaplan's primary statement (his LinkedIn post is the origin).
Establishes: A named large-developer / open-weight holder rejecting the EU disclosure-heavy model as overreach.
Paraphrase:  Joel Kaplan, Meta's Chief Global Affairs Officer, said Meta will not sign the GPAI Code of Practice, calling it legal uncertainty and overreach that goes beyond the AI Act and that Europe is on the wrong path. (Meta's refusal centers on the Code's copyright/transparency chapters; xAI signed only the safety chapter.)
Locators:    Kaplan quotes.
Quote:       Kaplan: the Code "introduces a number of legal uncertainties for model developers, as well as measures which go far beyond the scope of the AI Act"; "Europe is heading down the wrong path on AI"; "over-reach."
```

## Contradictions

- **The strongest pro-holder has moved past disclosure.** Amodei (darioamodei.com,
  June 2026) frames transparency as a first step now outgrown: "It is time to go
  beyond transparency to more serious and binding regulation." A thesis arguing a
  *narrow disclosure-only* federal floor must reckon with the fact that the lab
  that helped write SB 53 now calls disclosure insufficient. The honest framing:
  disclosure is a floor, not a solution, and the same holder wants a ceiling much
  higher than the thesis proposes.
- **Disclosure without enforcement was ignored.** The EU training-data-summary
  duty went largely unmet by OpenAI, Google, and xAI in the pre-enforcement window
  (TechPolicy.Press). This is the best available evidence on whether a paper
  transparency mandate changes behavior, and it says: not without teeth. It both
  strengthens the case for *enforceable* federal rules (vs voluntary) and
  undercuts any claim that disclosure alone reduces risk.
- **The two live regimes are not equivalent** (IAPP/Fine). The occasion invites an
  EU-vs-US contrast, but the EU regime is a whole-ecosystem, conformity-assessment
  structure while SB 53 is a narrow developer-only disclosure law. The piece must
  not smuggle the EU's structural apparatus into the "SB 53 raised to federal"
  proposal — the commission's own in/out list (disclosure yes; licensing,
  pre-release approval, full EU apparatus no) is right, and the divergence is the
  reason it must be stated precisely.
- **The counter's entrenchment argument partly rebounds on the pro side.** Perault
  (a16z) argues disclosure mandates raise concentration and favor incumbents. A
  federal floor endorsed by Anthropic — a compliant incumbent — is exactly the
  configuration that argument predicts. The writer should note this without
  ad hominem: it is a real structural critique, and Anthropic's endorsement carries
  obvious commercial stake (it already complies; a mandate raises rivals' costs).
  It also cuts the other way: a16z's *own* objection is the 50-state patchwork,
  which a single federal floor would cure.
- **The actual federal trajectory runs opposite to the thesis.** In 2026 the
  federal posture is preemption of state AI law, not a new federal mandate: an
  executive order (EO 14365) directs agencies to discourage/challenge state AI
  laws, and Congress considered (then stripped, 99-1) a state-law moratorium. A
  federal disclosure floor is politically upstream of where Washington is moving.
  (Sourced from search-result summaries of White & Case, Gibson Dunn, and
  StateScoop coverage; I did not open the underlying EO text — flagged as
  unverified below and to be confirmed if the writer relies on it.)

## Numbers

```text
Figure: 10^26 integer/floating-point operations — SB 53 frontier-model / frontier-developer threshold
Owner:  California SB 53 §22757.11(h),(i)
Scope:  Cumulative training compute including fine-tuning and modifications; defines who is in scope in California.
```

```text
Figure: $500,000,000 annual gross revenue — SB 53 "large frontier developer" threshold
Owner:  California SB 53 §22757.11(j)
Scope:  Affiliates' collective gross revenues in the preceding year; the disclosure duties attach to large developers.
```

```text
Figure: >50 people killed/seriously injured OR >$1,000,000,000 property damage — SB 53 "catastrophic risk"
Owner:  California SB 53 §22757.11(c)
Scope:  Foreseeable, material risk from a single incident; the harm class the framework must address.
```

```text
Figure: 15 days / 24 hours — SB 53 critical-safety-incident reporting deadlines
Owner:  California SB 53 §22757.13(c)(1) (15 days of discovery); §22757.13(c)(2) (24 hours where imminent risk of death or serious physical injury)
Scope:  Report to the California Office of Emergency Services.
```

```text
Figure: up to $1,000,000 per violation — SB 53 civil penalty
Owner:  California SB 53 §22757.15
Scope:  Attorney-General-enforced; per violation, not aggregate cap.
```

```text
Figure: 1 January 2026 — SB 53 effective date (signed 29 September 2025)
Owner:  California statute (standard effective date for a 2025-session bill without an urgency clause); confirmed as in force by January 2026 coverage.
Scope:  The commission's occasion date for the US regime.
```

```text
Figure: 10^25 FLOP — EU GPAI systemic-risk presumption threshold
Owner:  EU AI Act Article 51(2)
Scope:  Cumulative training compute; note this is an order of magnitude BELOW SB 53's 10^26 — the EU casts a wider net at the systemic-risk tier.
```

```text
Figure: 3% of worldwide annual turnover or €15,000,000, whichever is higher — EU GPAI fine
Owner:  EU AI Act Article 101
Scope:  Maximum Commission fine for GPAI-provider infringements.
```

```text
Figure: 2 Aug 2025 (GPAI obligations applicable) / 2 Aug 2026 (AI Office enforcement powers) / 2 Aug 2027 (legacy-model compliance)
Owner:  European Commission timeline (digital-strategy.ec.europa.eu); AI Act Article 113 application dates.
Scope:  The occasion: enforcement powers went live 2 Aug 2026.
```

## Source assets

```text
Asset: A side-by-side comparison of the EU AI Act and SB 53 (scope, compute threshold 10^25 vs 10^26, risk definition, conformity assessment, incident-reporting trigger, penalty), buildable from the IAPP/Fine analysis plus the two instruments.
Shows: That "SB 53 raised to a federal standard" is a far narrower proposition than the EU regime — the in/out line the thesis depends on.
Crop:  A table the writer composes from primaries; not lifted as an image. Keep the compute thresholds and the conformity-assessment row, since those carry the "disclosure floor, not EU apparatus" argument.
```

```text
Asset: SB 53's own tiered structure — frontier developer (10^26) vs large frontier developer ($500M revenue) and the duties that attach only to the latter (§§22757.11–22757.13).
Shows: The disclosure floor is scoped to the largest developers, blunting the "burdens startups" counter as applied to SB 53 specifically.
Crop:  Definitional subsections; retain the revenue gate that exempts small developers.
```

```text
Asset: None found for a chart — no clean time series here; the argument is legal/comparative, not trend data.
Shows: —
Crop:  —
```

## Discarded

```text
URL: https://news.stanford.edu/stories/2025/12/foundation-model-transparency-index-ai-companies-information — returned HTTP 403; could not confirm the 2025 FMTI decline (reported average ~40/100, Meta 60→31, Mistral 55→18) firsthand. Do not cite the FMTI numbers as read; they appear only in search snippets. The "voluntary transparency is declining" line, if used, needs a source the writer opens.
```

```text
URL: https://crfm.stanford.edu/fmti/paper.pdf — the primary FMTI paper; fetched as raw PDF stream that could not be parsed to text. Same caveat as above: unverified.
```

```text
URL: EO 14365 / state-AI-preemption coverage (White & Case, Gibson Dunn, StateScoop, per search snippets) — the federal-preemption trajectory is real and relevant to the counter/political-realism section, but I did not open the executive order or a full article. Flagged unverified; confirm before the piece rests weight on the 99-1 moratorium vote or the EO's specific directives.
```

```text
URL: PYMNTS / TechPolicy.Press coverage of California AB 2013 training-data disclosures being watered down — an adjacent California mandate (not SB 53). Overlaps the EU training-data finding I did verify; not separately opened. Note it is AB 2013, a different statute, if the writer reaches for it.
```
