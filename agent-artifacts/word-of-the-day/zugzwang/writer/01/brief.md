# Writer brief — word-of-the-day/zugzwang (01)

## Your job
Draft the article from the commission, voice guide, and evidence record, then
carry it through the deterministic proof to BLOCK: 0.

## Exact inputs (start here; do not go fill gaps yourself)
- `agent-artifacts/word-of-the-day/zugzwang/commission.md`
- `agent-artifacts/word-of-the-day/zugzwang/editorial-direction.md`
- `agent-artifacts/word-of-the-day/zugzwang/writing-coach/01/voice-guide.md`
- `agent-artifacts/word-of-the-day/zugzwang/researcher/01/evidence.md`
- Initialized article: `library/word-of-the-day/zugzwang.html`
- Template context under `.nb-context/` (template-contract, runtime-assets, furniture)

## Write
1. The article at `library/word-of-the-day/zugzwang.html`. Constraints:
   - `article` template geometry: `orientation` anchor + 2–6 flex sections you
     name for this piece + `Sources`. Words **550–800** (measured). Every section
     cited.
   - The **`rs-word-card` comes first** (inside/opening the orientation section):
     term, part of speech, IPA pronunciation, one-sentence standalone definition,
     cited. Match the sample markup in `.nb-context` furniture.
   - Tell the documented origin (verified dates only — 1858 print, 1905 first
     English, 1604 concept if used), trace the meaning's development, ground the
     present sense in a real cited use, and land the transfer beyond chess. Keep
     etymology and present-meaning distinct.
   - Fill `nb-meta` with ACTUAL values: title, dek (one concrete sentence, not a
     restatement of the definition), date `2026-08-01`, mode `open`, order null,
     tags e.g. `["language","etymology"]`, sources (measured count), words
     (measured), reading_minutes, harness `claude-code`, model `claude-sonnet-5`.
   - Number source entries in first-citation order; carry honest `data-nb-kind`
     (primary/secondary) from the evidence record. Only cite sources the evidence
     record verified; every URL must resolve.
2. `agent-artifacts/word-of-the-day/zugzwang/writer/01/draft-handoff.md`: state
   the article's visible act of original work (the distinction it teaches and the
   transfer it makes that the sources alone do not), any warnings you resolved,
   and anything unresolved for the editor.

## Prove it
Run: `/home/user/the-nightly-build/nb check library/word-of-the-day/zugzwang.html --series word-of-the-day --repo /home/user/the-nightly-build`
Drive it to **BLOCK: 0**. Treat warnings as revision notes and fix what you can;
note any you deliberately keep and why in draft-handoff.md. You may also
`nb preview` to eyeball rendering.

## Rules
- Author against documented furniture only; no extra scripts/styles/iframes/
  forms/handlers/external images. Preserve fixed engine assets/classes/labels.
- Begin with the named inputs. If evidence is missing or a claim is unsupported,
  reply `REQUEST researcher <need>` (evidence) or `REQUEST writing-coach <need>`
  (voice) — do not invent facts or citations.

## Report
End with one line: `DONE writer library/word-of-the-day/zugzwang.html`
(or a REQUEST/BLOCKED line if you cannot reach BLOCK: 0).
