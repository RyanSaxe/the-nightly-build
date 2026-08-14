# Writer handoff: tech-news/2026-08-14 (01)

## Original work

The article turns eight scattered source dossiers into a six-item ranked
brief that leads on governance rather than an exploit, states rather than
silently resolves the reasoning-trace paper's conflicting PII/credential
counts, builds a three-model cyber-benchmark table from Z.ai's own scattered
figures, and drops the probiotics candidate for a duplication the evidence
record itself did not catch: the same Nature paper (s41586-026-10909-6)
already ran as the lead health item in the library's 13 August edition, one
day before this brief.

## Evidence gap found during drafting

Checking the recent library (per the writer skill's instruction to read it
for content and context) turned up something the evidence record's own
"Where the evidence is thin" section didn't flag: the glucose-responsive
probiotics paper it proposed as a candidate item is not new to this paper.
`library/tech-news/2026-08-13.html` already ran it as "An engineered gut
probiotic switches on a diabetes drug only when blood sugar is high," citing
the same DOI, with a China Science Daily secondary source the evidence
record's own researcher could not find. I dropped the item entirely rather
than running it a second day running with the sourcing gap the brief
flagged (no confirmed independent, non-Nature secondary; paywalled headline
efficacy figures). This is worth surfacing to the researcher role: the
evidence record should check the recent library before naming a candidate,
not just the writer.

Also dropped, per the evidence record's own recommendation: the Gemini
1-billion-MAU item (stale, usage milestone not a technical result, no
verified primary) and the discarded Daybreak/GPT-5.6-Cyber item (already
excluded in evidence, duplicates GLM-5.3's cyber-benchmark ground).

## Items run (6)

1. Claude Code auto mode becomes the default (lead; non-incident, per the
   brief's steer away from a security lead)
2. GLM-5.3's coding and cyber-capability jump (Z.ai)
3. OpenAI's Ultrafast inference tier (GPT-5.6 Sol + Cerebras)
4. Gemini 3.7 Flash, read against Google's own mixed benchmark table
5. Reasoning-trace theft across Anthropic/OpenAI/Google APIs (arXiv,
   Panfilov et al.)
6. IonNet AI-screened solid-state battery electrolyte candidates (Science
   Advances), explicitly flagged in prose as published the week before this
   edition rather than on it

Composition note: two of the six items (GLM-5.3, reasoning-trace theft)
touch security, which the evidence's Contradictions section flagged as a
coherence risk given three straight prior security-led editions. Neither
leads the page; GLM-5.3 is framed on its coding-benchmark jump with the
cyber finding as a secondary, defensively-framed fact, and the
reasoning-trace item is framed as responsibly-disclosed, already-mitigated
research rather than a live exploit.

Self-reported lab figures (GLM-5.3's benchmarks, Claude Code auto mode's
safety study, OpenAI's Ultrafast speed figures, Google's Gemini 3.7 Flash
benchmark table) are attributed in the headline or opening sentence of each
item to the lab that reported them, not stated as settled fact. The
reasoning-trace item's PII/credential discrepancy between the arXiv
abstract and The Hacker News is stated as an unreconciled gap rather than
resolved by picking one number.

## Furniture

One `nb-table` inside the GLM-5.3 item, comparing GLM-5.3, GPT-5.6 Sol, and
Mythos 5 on CyberGym and ExploitBench, built from the evidence's own
benchmark-table asset description. No source-asset images were captured
(`nb asset`); the comparison reads more clearly as a table than as a cropped
screenshot, and no other item's evidence met the bar for a captured visual
the argument spends.

## Proof result

`nb stamp` then `nb check ... --series tech-news --library
/home/user/library-checkout` (links included): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. An intermediate `--no-check-links` pass surfaced 6
`W-SENTENCE-DENSITY` warnings (six long, clause-heavy sentences); all six
were split into shorter sentences rather than left standing, and the
warnings cleared. No warnings are intentionally left open.

## Open questions

None blocking. One minor, non-blocking note: two source-list entries
(arXiv 2608.09867 and The Hacker News' item) carry a writer-constructed
descriptive title rather than a literal page title, because the evidence
record did not capture the exact headline text for either page. The hrefs
and cited claims are exact; only the source-list display label is an
approximation. An editor who can open those two pages directly may want to
swap in their literal titles.
