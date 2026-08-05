# Editorial review: expert-tools/visidata (editor/01)

## Skeptic

Thesis: the exploratory pass a pandas or SQL session spends in write-run-reread,
VisiData spends in cursor-and-keystroke on a sheet that is already loaded, and
the piece names precisely where that trade stops paying. It stands on six
load-bearing claims, and I tried to break each against source.

1. **The five transforms are single command-keys on the current column** (`=`
   addcol-expr, `+` aggregate-col, `F` freq-col, `W` pivot, `M` melt). I opened
   each cited source file as printed — `expr.py`, `aggregators.py`, `freqtbl.py`,
   `pivot.py`, `features/melt.py` — and every `addCommand` string matches the key,
   longname, and behavior the prose asserts. `gF` and `gM` exist as claimed. This
   is the core risk of the round and it holds firsthand, not from a remembered
   API.

2. **The demonstration's arithmetic reconciles.** Six rows: West totals
   12/18/16 = 46, East 9/20/18 = 47, matching the Fig. 1 frequency table. The
   pivot cells (West Widget 28, Gadget 18; East Widget 20, Gadget 27) are the
   same rows regrouped by Region×Product, and the melt is that pivot folded to
   tall. Every number in both transcripts is internally consistent.

3. **The async-loader caveat is stated exactly, not overstated.** The loaders
   docs and `sheets.py` confirm `reload` is `@asyncthread` and rows yield one at
   a time; the article claims immediate navigation/viewing but says a frequency
   count, sort, or aggregate is final only once loading finishes. That is the
   evidence's exact boundary. The `nb-note` fine-print does not inflate it.

4. **`max_rows` truncation** default 1,000,000,000 is confirmed verbatim in
   `sheets.py` and framed correctly as truncation, not mere slowness, past the
   cap.

5. **The notebook/SQL boundary** (reproducible pipelines, custom plotting,
   out-of-core joins; cmdlog narrows but does not close reproducibility) is
   supported by the community sources and stated as a real limit, not a defect.

6. **Maintenance facts** — v3.4 (2026-06-30), GPL-3.0, ~9,200 stars,
   single-primary-author (Pwanson; Kefala on docs/packaging), 2–3-quarter
   cadence — all verified against the repo header, home page, and CHANGELOG.

The writer's open question — the pivot walkthrough calls marking a key column
"one more keystroke" without naming the key, because `!` was not source-verified
— is resolved by accepting the honest unnamed phrasing. No unverified key is
printed on the page, so the walkthrough ships as written; full keystroke-for-
keystroke reproducibility of the key-mark step is not required and I am not
routing `!` to the researcher.

Display text, descriptor by descriptor: the headline names the tool and the work
it changes and is the exact claim the piece defends; the dek adds mechanism
("already loaded," "column under the cursor") and makes a claim about the world,
not a grade of the article's method; all six subheads are argument steps in the
piece's own nouns (no scaffolding slots). "Three keystrokes answer revenue by
region" is literally true (`=`, `+`, `F`). No place, date, name, or quantity in
display text is wrong.

`data-nb-kind` audit: 15 primary / 2 secondary, and each primary really is the
owner of its claim — VisiData's own home page, docs, source files, changelog,
repo, and the creator's own blog post. The two secondaries are Hacker News
threads used only for reported adoption-cost opinion, correctly labeled.

Every citation href was opened as printed. All twelve non-forum links resolve to
the source's own page and confirm the cited content. The two HN items are
canonical `news.ycombinator.com/item?id=` addresses; s14 resolved and confirmed
the vim-keybinding framing, and s15 returned only a transient HTTP 429 rate-limit
(same host and URL form as the s14 that resolved), which is infrastructure, not a
broken citation. No miscitation, no broken address, no primary/secondary
conflict.

## Cut

The demonstration proves the one changing move and stops. There is no `pip
install`, no setup steps, no full command tour — only `vd sales.csv` and the five
transforms the commission names, so the walkthrough stays inside the voice
guide's "prove and stop" bar and never drifts into an install tutorial.

Both `nb-code` listings earn their place: Fig. 1 carries the compute-aggregate-
group loop with the sheet shown before and after; Fig. 2 carries the reshape
half. The comparison table is not redundant with them — it names the exact pandas
idiom each keystroke displaces (`df.pivot_table(...)`, `df.melt(...)`), which is
the replacement argument the voice guide licenses from Evans, so it stays.

I ran the earns-its-place test sentence by sentence and made no cuts. The closest
tell is "That is the whole loop:" — structurally near the banned "X is the whole
Y" family — but the colon delivers concrete evidence the section just built ("no
dataframe named twice, no cell rerun, three keys after the file opened"), so it
argues rather than self-grades and clears the bar as a licensed punch; flattening
it would only regress the voice. No prompt leakage: the argument is rendered in
the article's own prose, and no planning label ("one changing move," "adoption
cost," "flex section") surfaces in the text. Grammar and punctuation are clean —
no em-dash chains, no comma splices, the one semicolon joins two tightly bound
independent clauses correctly. Paragraph endings vary in shape; no formula
repeats.

## Reader

Read straight through as a machine-learning practitioner who already owns a
pandas answer: the piece gives what no single doc page does. The docs tell you
`F`/`+`/`=`/`W`/`M` exist; the article stages them as one continuous session on
one CSV with numbers that reconcile, then locates exactly where the trade stops
paying (mid-load whole-column results, reproducibility, out-of-core) and prices
the single-author maintenance risk. That decision — when to reach for it and when
a notebook still wins — is the original work, and it matches the handoff's
original-work sentence. The prose sits closer to the voice-guide exemplars than a
median summary: the keystrokes are placed at the sentence making the claim, the
cost is named in the same flat register as the capability, and pandas is given
its real idiom before it is shown losing. The headline reread as the largest
claim is the thesis the whole piece defends, with the actor and the work named.

The recent-pattern check has no live prior: `nb history --series expert-tools`
reports no published coverage, so there is no back-catalog shape to inherit. The
outline is argument-shaped, not Overview/Usage/Verdict, and the closer lands on
the conclusion ("the keystrokes earn it"), not a reading list or a pointer away.

## Edits

None. No sentence failed earns-its-place badly enough to cut without risking a
rewrite, and no markup, sourcing, or accuracy defect was found. Because no direct
cuts were made, the stamped counts remain honest and `nb stamp` was not rerun.

## Required work

None.

## Decision

approve — every shown keybinding is source-verified as printed, the transcript
arithmetic reconciles, the async and truncation caveats are stated exactly to the
evidence, the unverified `!` key is honestly left unnamed, every citation resolves
to its own source page, and the demonstration proves the one changing move and
stops.
