# writer brief: daily-brief/2026-11-01 (01)

Inputs:
- `../../editorial-direction.md` — the standing editorial standard and the Daily Brief series direction.
- `../../commission.md` — the six-item slate and standing instructions.
- `../../writing-coach/01/voice-guide.md` — the register for news/tech items and the Word of the Day.
- `../../researcher/01/evidence.md` — the verified anchor fact, date, and source(s) for each item; cite from here.
- The article file to write into (already initialized, do not recreate its skeleton):
  `/home/user/the-nightly-build/.nb-work/daily-brief/2026-11-01/library/daily-brief/2026-11-01.html`
Output: `draft-handoff.md` (beside this brief) AND the finished article HTML at the path above.
Proof: `/home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/daily-brief/2026-11-01/library/daily-brief/2026-11-01.html --series daily-brief --repo /home/user/the-nightly-build`

Work from these inputs. Do not tour the repository or the archive. Where
something you need is missing, ask me (the orchestrator).

Fill the six items in the fixed order the skeleton already lays out: Word of the
Day, three news, two technology. Use the items and sources from `evidence.md`
(if the researcher substituted a backup, use the substitute). This is STRICT:
total body 300-700 words, exactly six items, one citation per item (the Word of
the Day takes two: a definition authority and a coinage history), min 6 sources.

- **Word of the Day** (bafflegab, unless `evidence.md` substituted grawlix):
  fill the `rs-word-card` with the word, part of speech, IPA, and a one-sentence
  definition cited to the dictionary authority; then three or four sentences of
  documented origin cited to the word-history source. Respect any hedge the
  evidence records (e.g. "possibly" the coiner, a disputed date) — attribute it.
- **Each news and tech item**: two or three sentences — what happened, who did
  it or claims it, what follows — present tense for events, the concrete
  development first, the figure or caveat the headline dropped. Attribute every
  contested or single-party claim to its source. Each item's `<h3>` headline
  obeys `spec/headlines.md` (subject-verb-surprise, no colon subtitle, a number
  only where it is the surprise, no question unless the item answers it).
- The two technology items touch Anthropic's models incidentally. Keep the
  framing strictly neutral and factual. The piece never refers to itself.

Fill the title and dek: the title is the single most important development of
the day stated as a headline (not a label), and the dek is one concrete sentence
that does not restate it and obeys the dek rules (no semicolon reversal, no
suspended question, no comma-triad). Keep the `nb-meta` JSON and the fixed chrome
(`<body class="nb-article">`, the `rs-word-card`, `<h2>Sources</h2>`) intact; set
date 2026-11-01. Do not stamp counts by hand.

Watch the length hard: 300-700 words total. If you run over, cut words inside
items, never drop an item or a citation. Run the proof yourself and fix what it
reports before handing off. In `draft-handoff.md` record the proof result and
the total word count. Meet `spec/slop.md`; test each item's first and last
sentence — a brief item must not close on a line that hands the point back.

## Researcher corrections (in evidence.md; honor these over any looser wording)

- The evidence record's quotes came through a summarizing fetch and are marked
  "extract". Prefer paraphrase-with-citation; print a quotation only if you can
  confirm it verbatim at the source. The one place a short quote matters is the
  bafflegab definition — confirm it against Merriam-Webster before quoting.
- **bafflegab:** Merriam-Webster carries NO "possibly" hedge and no etymology,
  so do not attribute a hedge to it. Green's dates it May 1952 while press
  coverage is January 1952, so do NOT print a month for the coinage — say 1952.
- **Alaska:** the state first moved to dismiss around 10/26-27; the 10/31 filing
  is a further motion. Do not write that the state "moved for the first time on
  10/31". DOJ's own filing says the only immediate relief it seeks is preserving
  and segregating ballots; the "sham candidate" framing is DOJ's allegation —
  attribute it. Source of record: DOJ ECF No. 67 in 3:26-cv-00376-SLG.
- **Arch:** the complaint could not be opened and no record confirms Judge
  Chutkan is assigned the DC/Virginia case. Write that DC and Virginia "asked
  Judge Chutkan" to halt it, not that she "is weighing" it. The 11/5 NCPC vote
  is sourced (Newsweek); the suit via WaPo/Spokesman-Review.
- **VOLTA:** Talos says the LLM ranks the victim's own stolen assets by
  monetization value — NOT victims against each other. State it that way.
- **Cursor:** its notice says removing the extension "may not be sufficient" (not
  "does not remove"); the ~11-hour window is the researcher's arithmetic (state
  it loosely, "about 11 hours", or give the two clock times); the notice gives no
  user count, so do not print any affected-user figure.
