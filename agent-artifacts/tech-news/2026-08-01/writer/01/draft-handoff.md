# Writer draft handoff — tech-news/2026-08-01 (01)

## Original work
This piece resolves five candidate items down to four by applying the
house citation bar (cite only what you have read; the URL must resolve) to
the researcher's own flag on the GPT-5.6 Sol item, whose only OpenAI-owned
source returned HTTP 403 on every attempt (confirmed again independently
before dropping it), then writes the remaining four so each stands as a
self-contained judgment naming who the development changes something for
(NIST's post-quantum reviewers, a developer choosing which model to call,
engineers scaling silicon qubits, and DMD patients ahead of an FDA
decision) rather than a spec-sheet recap.

## Items kept / dropped
Kept, strongest-first per the evidence record: (1) Anthropic Claude Mythos
cryptanalysis, (2) Moonshot Kimi K3 open weights, (3) HRL silicon quantum
processor, (4) HOPE-3 / deramiocel Lancet trial. Dropped: OpenAI GPT-5.6
Sol kernel rewrite — the researcher flagged this as weaker-sourced (primary
unread, 403 on both openai.com URLs); I re-fetched the primary URL myself
and got the same 403, so per the brief's instruction ("if it weakens the
brief, drop it") and the house rule that a citation's URL must resolve, it
is excluded rather than hedged in. Dropping it also improves the mix: four
items now span cryptography/AI-safety, an open-weight model release,
quantum hardware, and a health result, rather than leaning further into a
models-only set.

## Sourcing and figures
Each of the four items carries exactly one primary (Anthropic's research
post; the Kimi K3 Hugging Face model card; the HRL arXiv preprint, used
because the Nature version of record is gated; the Lancet trial via its own
EurekAlert release, since thelancet.com is subscriber-gated) plus one
independent secondary (CyberScoop; Fortune; The Quantum Insider; UC Davis
Health). Kimi K3's parameter count uses the model card's 2.8 trillion
figure, per the researcher's resolution, with a one-clause hedge against
Fortune's earlier 2.7 trillion launch-day figure. All other numbers (HAWK-256
2^64 → 2^38, the 200–800x AES-128 figure, HOPE-3's 54% and ~65% figures, the
64/22 cardiac sub-cohorts, the 42% vs. 15% infusion-reaction rates, HRL's
~5x error suppression and 4-kelvin operating point) are taken exactly as
given in the evidence record's Numbers table.

## Proof result
`nb check library/tech-news/2026-08-01.html --series tech-news --repo
/home/user/the-nightly-build` → **BLOCK: 0, WARN: 0** on the final run.
Along the way I fixed five W-SENTENCE-DENSITY warnings by splitting
over-dense sentences (numeral-heavy clauses inflate the tool's word count,
since each decimal or comma-grouped figure tokenizes into multiple words)
and corrected nb-meta's word/reading-minutes counts to the tool's measured
totals (759 words, 4 min). No warnings were left unresolved.

## Open items
None outstanding for the researcher or writing-coach. If a future edition
gets a clean, unblocked read of OpenAI's GPT-5.6 Sol post, that item could
be reconsidered on its own merits — it is not carried forward here in any
form.
