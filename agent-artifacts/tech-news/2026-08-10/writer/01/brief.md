# writer brief: tech-news/2026-08-10 (01)

Inputs:
- `agent-artifacts/tech-news/2026-08-10/editorial-direction.md` — house standard, press voice, series prompt, declared reader
- `agent-artifacts/tech-news/2026-08-10/writing-coach/01/voice-guide.md` — how the brief should sound
- `agent-artifacts/tech-news/2026-08-10/researcher/02/evidence.md` — the reinforced item set (round 02 supersedes 01); use this record
- `.nb-work/tech-news/2026-08-10/library/tech-news/2026-08-10.html` — the initialized brief to edit in place
- `.nb-work/tech-news/2026-08-10/.nb-context/` — effective template contract, runtime assets, furniture catalogs

Output: `agent-artifacts/tech-news/2026-08-10/writer/01/draft-handoff.md`
Proof: `./nb check .nb-work/tech-news/2026-08-10/library/tech-news/2026-08-10.html --series tech-news --library /home/user/library-checkout`

Focus this round: build one `nb-brief-item` per selected item from the evidence
record's grouped sources; the lead item sets the brief's headline and dek. Each
item carries exactly one primary record and at least one independent account, per
the source policy. Where an item is a model or benchmark claim, report the number
the vendor's own chart omits when the evidence supplies it. Use `nb-table` only
where an item's numbers are clearer shown than told.

Recent habits to break (see commission): keep the skepticism toward vendor claims
but write each headline and dek fresh against `spec/headlines.md`, avoiding the
negative-parallelism and comma-triad dek molds, and vary how item headings are
built.

Round-02 item set (all five firm): OpenAI's Lean-verified math results; EU AI Act
Article 50 transparency obligations; California AI Transparency Act; the Tesla/
SpaceX "Terafab" Texas fab; and the SK hynix/Sandisk High Bandwidth Flash standard.
Two risk notes to honor: (a) for the OpenAI item, the skeptical line is that the
Lean 4 certificates verify the *formalized* theorems while no named mathematician
had publicly worked through the arguments in-window — reaction, not verification —
and the manuscript says "an internal OpenAI model", so do not print the blog-only
"Astra" name or the "$2,000" figure as established. (b) Several items (OpenAI, both
transparency laws) are dated 1-2 Aug, just outside the tight window; Terafab (6 Aug)
and HBF (4 Aug) are inside it. Lead with an in-window item unless the OpenAI result
is clearly the most consequential, and do not imply every item broke on 2026-08-10.
