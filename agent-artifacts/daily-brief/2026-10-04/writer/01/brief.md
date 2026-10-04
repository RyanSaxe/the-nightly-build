# writer brief: daily-brief/2026-10-04 (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — the six-item structure and item decisions
- voice-guide.md (../../writing-coach/01/voice-guide.md)
- evidence.md (../../researcher/01/evidence.md) — the complete verified claim set per item
- recent-patterns.md (../../recent-patterns.md) — recent brief headline/dek habits to break
- Template contract + furniture: ../../../../.nb-context/template-contract.yaml and
  ../../../../.nb-context/furniture/press.md (rs-word-card) and engine.md

Output:
- The article HTML (edit in place):
  .nb-work/daily-brief/2026-10-04/library/daily-brief/2026-10-04.html
- ./draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-10-04/library/daily-brief/2026-10-04.html --series daily-brief --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the archive
for background. Where the evidence record does not carry a fact, ask me — do not
invent. Use the researcher's selected three news items; if the record flags an item's
primary as unresolved, ask me before dropping or swapping.

The piece: six items in the fixed order the skeleton already lays out — Word of the
Day (rs-word-card), three news items, two technology items (GPT-6.1 Sol; SynthID
Bio). Each item is a tight, self-contained paragraph: what happened and why it
matters, with claims attributed and evidentiary status explicit. Keep exactly six
items.

READ the "Orchestrator decision (after researcher/01)" section at the end of
commission.md FIRST — the items are decided and one premise changed materially:
- Word of the Day: "robot" (M-W respelling ˈrō-ˌbät, no IPA; note 1922 vs 1923
  first-use disagreement carefully).
- News 1 (LEAD): Pike FAILED execution — SCOTUS vacated the stay 6-3, Tennessee
  carried out the injection, Pike survived two doses of pentobarbital, Gov. Lee
  halted executions for 2026 and ordered a review, Commissioner Strada resigned
  Oct 3. Attribute the "unconscious on a ventilator" claim to Pike's attorneys.
  Drop the firing-squad request (or attribute narrowly). NOT a stay-only item.
- News 2: Hochul Executive Order 64 (AG James special prosecutor, Cornell case).
- News 3: Latitude air-ambulance Gulfstream G100 (C-GRJP), six aboard,
  Bermuda→Boston, Coast Guard debris field confirmed, people unaccounted for.
- Tech: GPT-6.1 Sol ($2/$10/$0.10 per M tokens; "near-Astra" is OpenAI's claim) and
  SynthID Bio (proof of concept; QUALITATIVE result only — no numeric hit rates).
- EXACTLY ONE data-nb-kind="primary" per item; tag any second owner-doc as secondary.
  The lead headline names the Pike outcome (not a stay, not a date prefix, not SCOTUS
  paperwork framing).

Specifics:
- Each item carries its primary (data-nb-kind="primary") and secondary per the record;
  number sources in first-citation order; 12+ sources. Prefer locators that land on
  the passage.
- Word card: term, part of speech, pronunciation, one-sentence cited definition, then
  the documented origin and a telling moment. Keep it lively and brief.
- News items: no date-prefixed headline, no SCOTUS-paperwork framing, no "N
  developments" roundup (see recent-patterns.md). Attribute anything unverified (e.g.
  the Christa Pike facts) to its source and state what is established vs. alleged.
- Tech items: attribute the GPT-6.1 Sol capability claim to OpenAI and give the exact
  prices from the record; give SynthID Bio's result as DeepMind reports it and note
  it is a proof of concept. Link the underlying record and independent reporting for
  each.
- Edition headline + dek (nb-meta title + dekline): name the day's lead story with a
  subject and verb (model: the "54 minutes" headline), not a roundup; dek is one lean
  sentence, no comma-triad/semicolon-reversal. nb-meta dek identical to the rendered
  dekline.
- Set nb-meta: series `daily-brief`, slug `2026-10-04`, mode `rolling`, date
  `2026-10-04`, template `brief`; fill harness/model; run `nb stamp`.
- Iterate with `nb check --no-check-links`, then full proof with links until BLOCK: 0.
  Write draft-handoff.md (the one-sentence original work this edition does with the
  day's events; proof result + any intentional warning; any open question).

Report the handoff path and any warning you left.
