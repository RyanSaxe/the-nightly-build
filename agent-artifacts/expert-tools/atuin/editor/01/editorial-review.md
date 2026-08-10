# Editorial review: expert-tools/atuin (editor/01)

## Skeptic

Thesis: Atuin turns a flat shell history into a queryable SQLite table with
per-command context, which lets a terminal-native engineer ask questions
`.bash_history` cannot answer at all; the tool earns its shell hook and database
for someone who queries their history, and its "end-to-end encrypted" sync
covers less than the phrase implies.

The claims it stands on, and how each held:

1. **Bash keeps only the command text; Atuin records context columns (cwd, exit,
   duration, session, hostname) in SQLite.** Held. Confirmed against history.rs
   (the `History` struct) and the create_history.sql migration. The columns the
   orientation names are exactly the ones the schema declares.

2. **The recorded context answers a question a flat history cannot: which
   commands failed in this directory, via `atuin search --exclude-exit 0 --cwd
   .`** Held, and this is the article's load-bearing example. Verified against
   the search reference (s3): `--exclude-exit` drops commands that exited with
   the given value, so `--exclude-exit 0` keeps failures, and `--cwd .` restricts
   to the current directory. Because `.bash_history` records neither exit code
   nor directory, the query is genuinely unanswerable there rather than merely
   harder. The bash half of the listing (`history | grep make`) is honest about
   what a text-only history can do. The example proves value and is not an
   install walkthrough.

3. **The cost is the hook on every prompt, a growing plaintext database, and the
   up-arrow/Ctrl-R rebinding; the daemon is opt-in, and sync runs in-shell on a
   5m default.** Held. preexec/precmd behavior matches the shell-integration
   docs (s5). The daemon-off and 5m facts I verified directly at settings.rs:
   `sync_frequency` "5m", `auto_sync` true, `daemon.enabled` false,
   `daemon.autostart` false. The article correctly uses the shipped 5m source
   default, not the sync guide's "hourly" prose, which was this round's explicit
   trap.

4. **Actively maintained: ~1-2 week release cadence since 2021, MIT, Rust,
   18.19.0 on 2026-08-03 with a beta line open past it.** Held against the
   releases feed and LICENSE (s8, s9). Numbers and dates match the record; no
   figure altered.

5. **"End-to-end encrypted" protects the sync payload only; the local store is
   plaintext and the server sees envelope metadata.** This is the piece's
   sharpest claim and the round's focus, so I checked it at the source rather
   than trusting the record. history.rs carries the comment verbatim ("Client
   stores data unencrypted, and only encrypts it before sending to the server").
   record.rs confirms only `data` is encrypted while id, idx, host, tag, version,
   and timestamp travel in the clear, and that idx is unique per (host, tag), so
   "per-host record counts" and "how much you run and when" are a fair reading of
   what the server sees. paseto_v4.rs confirms the per-record random 32-byte CEK
   wrapped under a master key that is 32 bytes, generated locally, and never
   serialized. Every encryption sentence and the three-layer table are accurate.

No central claim broke. No arithmetic to recompute beyond the field counts, and
the one field-count sentence I corrected (see Edits) was a wording slip, not a
sourcing gap. Every `data-nb-kind` is right: twelve primary sources that own
their claims, and the one secondary (the SANS forensic write-up) is correctly
labeled and used only for the outside-confirmation point, not for any capability
claim. Citation hrefs point at the sources themselves. I resolved the four
load-bearing source files (history.rs, settings.rs, record.rs, paseto_v4.rs)
directly.

I considered the README demo GIF the record offers as an optional asset and agree
with the writer's decision to omit it: the argument spends the recorded context
fields and the failed-here query, both of which the live `nb-code` listing
carries better than a TUI screenshot, and the record itself judges the shell
example the stronger vehicle for a CLI tool.

## Cut

Eight sentences failed the slop or punctuation test and were trimmed or cut in
place; none needed reporting.

- One reader-gesture that also echoed the brief's characterization of the
  audience ("The reader who lives in a terminal already has a history and already
  knows what it cannot do") went as prompt-adjacent framing whose content the
  piece assumes and demonstrates anyway.
- A lecture-style opener ("Start with a real friction") went so the paragraph now
  leads with the concrete failed build, which is the Willison/Evans move the
  voice guide asks for.
- Two self-grading signposts went: "That bound is worth stating plainly, because
  it is the same honesty the query buys you" (kept the plain limit-statement
  after it) and "What it does not reach is worth stating exactly, because" ahead
  of the two qualifying facts.
- One negative-parallelism-plus-decoration tag ("a useful reminder that the
  exposure is ordinary rather than exotic") became a plain appositive stating the
  outside confirmation.
- One stock flourish ("the answer is in your hands:") and one low-content tag
  ("and easy to act on") went from otherwise concrete sentences.

Punctuation: one semicolon that joined a claim to its source attestation became a
period, per the house default. The remaining semicolon (the Fig. 1 caption)
carries a genuine bash-vs-Atuin parallel and stays. No em-dashes in the piece.

The earned contrasts survive on purpose: "Encryption protects the payload, not
the envelope" corrects a misconception the piece names (the "fully encrypted"
marketing), stated in the section's own nouns, and "the local database, not the
sync server, as the file worth protecting" is the verdict the argument built.

Formula check against the recent-pattern notes: the flagged closing mold is
broken. Maintenance sits as a middle section, not the closer, and the piece ends
on the verdict ("When the swap pays off"). No install count appears in the
headline. The headline leads with the tool name and a present-tense verb like the
recent three, which the notes call acceptable, but the causative-plus-comparative
construction ("makes your shell history answer questions bash can't") varies the
rhythm rather than copying it, so I kept it. Headings are built differently from
one another and reconstruct the argument on a skim.

## Reader

Read straight through as the paper's declared engineer, the piece gives something
no single source does: it reconciles a "fully end-to-end encrypted" promise, a
docs-versus-source frequency contradiction, and a plaintext-local fact that live
only in scattered files, into one bounded reading, then ties that boundary to a
single decision test (do you query your history) and a concrete verdict (guard
the local database, not the sync server). The draft-handoff's original-work
sentence claims exactly this reconciliation, and it survives the read. So does
the sources-alone test: to get here from the sources you would have to read the
README, the sync guide, history.rs, record.rs, and settings.rs and notice the
contradiction yourself. After the trims the prose sits closer to the voice-guide
exemplars than to a median summary: plain declaratives, a named concrete
friction, tool limits stated at the same resolution as results, and a calibrated
Dan-Luu-style weighing of the swap. The headline is the largest claim and the
piece defends it.

## Edits

- Cut the reader-gesture sentence opening the orientation's second paragraph.
- Cut the "Start with a real friction" opener so the failed-here paragraph leads
  with the concrete scenario.
- Replaced "That bound is worth stating plainly, because it is the same honesty
  the query buys you: the database answers for what it saw, and says nothing
  about the rest" with "The database answers for what it saw and says nothing
  about the rest."
- Corrected "more than the five context fields this query uses" to "more than the
  two fields this query uses" (the query filters on exit and cwd; five was the
  wrong count for what the query touches).
- Replaced "What it does not reach is worth stating exactly, because two facts
  from the source qualify the promise" with "Two facts from the source qualify
  the promise."
- Changed the semicolon after "before sending to the server" to a period.
- Replaced "which is a useful reminder that the exposure is ordinary rather than
  exotic" with "independent confirmation that the exposure is real."
- Removed the "the answer is in your hands:" flourish from the self-hosting
  sentence.
- Removed "and easy to act on" from the sync verdict's topic sentence.

## Required work

- **orchestrator (non-blocking).** My trims shortened the article by roughly
  three dozen words. If the re-run proof validates nb-meta `words` /
  `reading_minutes` against the body, recompute them (currently 1576 / 7) before
  stamping. The writer runs the proof; no content change is needed from the
  writer.

No work for the researcher (evidence settled every claim) or the writer (no
reporting, redraft, asset, or chart provenance outstanding).

## Decision

approve. Every claim the argument rests on holds at the source, the three focus
precisions (encryption scope, 5m default, the flat-history-can't query) are
accurate and well-cited, and the slop and punctuation fixes were mine to make in
place, leaving no publication-blocking work.
