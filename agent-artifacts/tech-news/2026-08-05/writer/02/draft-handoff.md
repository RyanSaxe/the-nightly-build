# Draft handoff: tech-news/2026-08-05 (writer 02) — first full draft

## Original work (one sentence)
The brief's organizing axis is not recency but verifiability: it leads with the week's loudest release, Qwen3.8-Max, precisely to mark it as the least checkable item on the page (vendor-only scores, no public weights), and ranks three quietly peer-reviewed results above it by what an outsider could actually reproduce — a judgment the evidence record supplies the parts for but never makes.

Where this is visible: the Qwen headline and table are captioned and worded as Alibaba's own unreproduced claims; the three peer-reviewed items carry their true earlier dates (Jul 15/29/30) and the "firmest results" framing in the dek; the through-line is that a thin AI week's real substance came from physics and immunology labs, not a model card.

## Proof result
`nb check … --series tech-news --library <checkout>` (links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.**
No warnings intentionally left. em-dash 0 (limit 4), "mechanism" 0 (press limit 1), "leverage" 0, "load-bearing" 0.

## How the four items are dated and framed
- **Qwen3.8-Max (Artificial Intelligence) — dated August 3, lead item.** Framed as a release, not a capability win. Every score is attributed to Alibaba ("Alibaba reports…", "Alibaba's own"); the table caption states the scores are on mixed harnesses of Alibaba's choosing and not independently reproduced; prose states the weights were not on Hugging Face/ModelScope and no license was named as of Aug 5. GPT-5.6 Sol (88.8) and Claude Fable 5 (84.6) appear only as Alibaba's own comparison baselines on Terminal-Bench 2.1 — not re-filed as items.
- **Arginine / MHC-I (Immunology) — dated July 30 (Cell).** Explicitly in mice; codon-specific effect (synonymous codons abolish it); read as a possible adjunct to immunotherapy, not a standalone treatment.
- **Photonic time crystal (Ultrafast Optics) — dated July 29 (Nature).** First all-optical realization; picosecond THz modulation ~1,000× faster than electronic; plasmonic loss cut by half.
- **Atom–quantum-dot interference (Quantum Networking) — dated July 15 (Light: Sci. Appl.).** Kept distinct from the photonic-time-crystal item (single-photon HOM interference between unlike emitters, for modular networks). Contested QD temperature printed as "about 12 kelvin" (not the 12.4/12.5 K figure), attributed to phys.org; visibility 0.65 ± 0.14 stated with its interval at first mention; overlap 0.88; ~917 nm.

Nothing implies all four broke on Aug 5; the dek gives the honest Jul 15–30 range for the three peer-reviewed papers, with Qwen (Aug 3) as the lead.

## Sourcing
13 sources, first-citation order. Each item carries exactly one primary + ≥1 independent secondary (per-item bands primary [1,1], secondary [1,∞]). Gated peer-reviewed primaries are cited at their own journal pages and confirmed resolving: Cell 403, Nature (×2) 303 auth-redirect, Light via nature.com 303 — gated, not dead; Qwen owner page 200. Institutional press releases (Rockefeller s6, École Polytechnique s10) are marked `secondary`, since the per-item contract admits only primary/secondary and a second `primary` would trip B-SOURCE-KIND; the independent secondaries (Science News, Technology Networks, phys.org ×2, SiliconANGLE, The Decoder, Implicator.ai) carry the independence requirement.

## Open questions for the orchestrator
- **Field adjacency (from researcher/04):** items 3 and 4 are both photonics/optics. They are distinct developments and each clears sourcing independently, so the set of four holds. No fifth qualifying item exists in-window without further relaxation, so dropping one returns the count to three (below the band floor of 4). Filed as four; flagging per the researcher's note.
- **Qwen benchmark table:** included as furniture because the article's argument spends exactly what it shows — "frontier parity" is a 2–4 point vendor-reported margin on a harness Alibaba chose. If the editor reads the table as amplifying unreproduced numbers despite the caption, it can be cut to prose without touching the sourcing.
