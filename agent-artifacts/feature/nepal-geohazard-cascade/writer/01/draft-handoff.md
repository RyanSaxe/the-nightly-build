# Writer handoff: feature/nepal-geohazard-cascade

## Draft delivered

Completed the reported feature in:

`/workspace/scratch/53797a806fdc/nightly-build/.nb-work/feature/nepal-geohazard-cascade/library/feature/nepal-geohazard-cascade.html`

The article compares the optical Sentinel-2 precursor result with a separate Sentinel-1 backscatter preprint, then tests what those retrospective measurements establish about a warning that could reach people before the flood. It distinguishes the collapse, preconditioning and downstream cascade; dates the human toll to the Associated Press report of 25 September; and identifies the limits in climate attribution and the unreadable event-day DHM bulletin. The article links 12 distinct sources.

## Quotes checked

- Dave Petley, AGU Landslide Blog, 16 September 2026, paragraph 117: “does not mean that the event itself could have been reliably predicted nor that a warning system can be easily developed.” The article quotes this clause and attributes it to Petley’s commentary on the Wang et al. paper.
- Shristi, quoted in the IFRC response account, paragraph 153: “I was at school when the water came and destroyed my house.” The article attributes this testimony to IFRC and does not present it as an interview conducted for this article.
- World Weather Attribution report, main findings: “We have not assessed whether this specific rock-ice avalanche would have occurred in the absence of human-induced climate change.” The draft paraphrases the report’s counterfactual limit rather than claiming event-specific causation.

The quote locations and source classifications are recorded in `researcher/01/evidence.md`. I did not assert what the DHM 8 a.m. bulletin said because its contents were not readable in the available source record. The article says explicitly that its timestamp cannot establish an issued or received warning.

## Metadata and proof

Ran `./nb stamp .nb-work/feature/nepal-geohazard-cascade/library/feature/nepal-geohazard-cascade.html`; it computed 1,328 words, 6 reading minutes and 12 sources.

Ran the proof command exactly as supplied in the writer brief:

`/workspace/scratch/53797a806fdc/nightly-build/nb check /workspace/scratch/53797a806fdc/nightly-build/.nb-work/feature/nepal-geohazard-cascade/library/feature/nepal-geohazard-cascade.html --series feature --repo /workspace/scratch/53797a806fdc/nightly-build`

The first run found two blocking contract issues (series metadata mode and required `orientation` section) plus one citation-order warning. I corrected those in the article HTML. The final run returned:

`BLOCK: 0`
`WARN:  0`
`verdict: PUBLISHABLE`

## Runtime setting

Runtime model was inherited GPT-6. The requested writer effort is medium; per-role model and reasoning controls are not configurable in this runtime. This is the recorded deviation.
