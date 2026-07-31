# Writer brief — word-of-the-day/shibboleth (01)

## Role
Load and follow `skills/writer/SKILL.md`. Draft the article from the exact brief,
voice guide, and evidence record, then carry it through the deterministic proof.

## Begin with these exact inputs
- `agent-artifacts/word-of-the-day/shibboleth/editorial-direction.md` (governing layers)
- `agent-artifacts/word-of-the-day/shibboleth/commission.md` (angle, reader, bar)
- `agent-artifacts/word-of-the-day/shibboleth/writing-coach/01/voice-guide.md`
- `agent-artifacts/word-of-the-day/shibboleth/researcher/01/evidence.md` (9 verified sources)
- The initialized article: `library/word-of-the-day/shibboleth.html` (skeleton copied here)
- Generated context: `.nb-context/` (template-contract.yaml, runtime-assets.yaml,
  furniture/{engine,press}.md). The `rs-word-card` markup is in
  `.nb-context/furniture/press.md`.

All paths are under the workspace `.nb-work/word-of-the-day/shibboleth/`.

## What to write
The article at `library/word-of-the-day/shibboleth.html`. Template `article`,
**550-800 words**, flex sections 2-6 (the last is the piece's own conclusion),
`orientation` + `sources` are fixed. Open with the `rs-word-card` (word,
part of speech, pronunciation, one cited definition), then tell the documented
origin (Judges 12 at the Jordan fords), trace the sense from spoken password to
the general in-group marker, and ground the present sense in the real modern use.

Follow the evidence record exactly. Key facts already verified for you:
- Definition authority: Merriam-Webster (sense 2a "a use of language regarded as
  distinctive of a particular group" is the cleanest card definition; sense 2b
  and 1a/1b carry the broader custom/belief sense for the body).
- Origin: Judges 12:5-6 (cite one named translation — JPS via Sefaria or NRSVUE
  via Bible Gateway). The Gileadites held the fords; the sh/s test; **42,000**
  Ephraimites fell (verified against the Masoretic Hebrew, not just English).
- The mechanism is the teaching payload: the give-away was involuntary — the
  Ephraimite dialect lacked the "sh" sound, so any sh-word would have served
  (Jewish Encyclopedia). The word's own meaning was not the point; the phoneme was.
- Hebrew literal meaning is DISPUTED ("ear of grain" vs "stream/flood"); state
  the ambiguity honestly, note context (a river ford) makes "stream" attractive
  to some scholars, do not pick a winner. Do not collapse the attestation dates
  ("late 14c." word in English vs "1630s/1638" figurative sense) into one "coined
  in YEAR" line.
- Modern use: the PLOS ONE 2023 paper "Shibboleth: An agent-based model of
  signalling mimicry" (source 9) — it quotes Judges 12 and generalizes, incl. the
  Ukrainian/Russian phonology example. This is your read, resolvable modern
  citation. Do NOT cite the NYT lines or the arXiv PDF (researcher could not read
  them; they are in Discarded).

## Pronunciation (correction — do not misattribute)
Merriam-Webster's `ˈshi-bə-ləth` is MW's own respelling, NOT IPA. In the word
card, either present a correct IPA pronunciation `/ˈʃɪbələθ/` (standard) or the
MW respelling labeled honestly. Do not print MW's respelling as if it were IPA.

## Permitted changes / decisions you own
- Name the 2-6 flex sections for THIS word's argument (scene → mechanism → sense
  development → modern use/close), not a Background/Origins/Today scaffold.
- Choose the headline and dek per `spec/headlines.md`. Do NOT open on a coiner
  (shibboleth has none — lean on that), do not reuse the "named for the wrong
  person" reveal (bowdlerize did it), and avoid the eponym framing (quisling did
  it). No hedged not-X-but-Y in the dek.
- You may render the Hebrew שִׁבֹּלֶת / סִבֹּלֶת inline as text beside its
  transliteration (evidence: no image asset warranted; no chart).
- Preserve the template's fixed engine assets, classes, labels, required HTML.
  Add no scripts/styles/iframes/forms/handlers/external images.

## Metadata (`nb-meta`)
Fill real values: `series: "word-of-the-day"`, `slug: "shibboleth"`,
`template: "article"`, `mode: "open"`, `order: null`, `date: "2026-07-31"`,
`tags: []` (or a couple honest tags like `language`, `etymology`),
`sources` = actual count, `words` = measured, `reading_minutes` = honest,
`dek` = your dek, `harness: "claude-code"`, `model: "claude-sonnet-5"`.

## Proof (run to BLOCK: 0)
From the checkout root (`export PATH="$HOME/.local/bin:$PATH"` first):
```
./nb check .nb-work/word-of-the-day/shibboleth/library/word-of-the-day/shibboleth.html \
  --series word-of-the-day --library /home/user/library
```
Drive it to **BLOCK: 0**. Treat every WARN as a revision note and clear what you
can honestly clear. You may `./nb preview` to eyeball the render if useful.

## Also write
`agent-artifacts/word-of-the-day/shibboleth/writer/01/draft-handoff.md`: record
the article's visible act of original work (what this piece gives beyond its
sources — here, the framing of the shibboleth as an *involuntary, identity-bound*
test and the clean separation of the phoneme-mechanism from the word's meaning,
plus the honest handling of the literal-meaning dispute), the final word count,
the source count, and any unresolved WARN with your reason.

## Request, don't guess
If evidence or voice guidance is missing, return `REQUEST researcher <need>` or
`REQUEST writing-coach <need>` rather than filling the gap yourself.

## Control signal
Return exactly one line:
`DONE writer agent-artifacts/word-of-the-day/shibboleth/writer/01/draft-handoff.md`
(only after `nb check` is BLOCK: 0) or `REQUEST <owner> <need>` /
`BLOCKED writer <reason>`.

## Scope discipline
`./nb` and web tools for focused work only. Do not tour the repo, git history, or
archive. The evidence record is your source of truth; re-open a source only to
confirm a specific wording you are about to quote.
