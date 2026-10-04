# Commission: daily-brief/2026-10-04 (Sunday)

## The assignment

The Daily Brief for Saturday–Sunday, October 3–4, 2026: six items, in this fixed
order (the template enforces the word card first and six items total):

1. Word of the Day
2. News
3. News
4. News
5. Technology
6. Technology

Each item explains why it matters. Every item is cited with at least one primary
source (the record that owns the claim) and at least one secondary. Template floor
is 12 sources total; per item: exactly 1 primary, 1+ secondary.

## Item decisions

### 1. Word of the Day
Choose a word with a precise present-day meaning and an origin worth knowing. Give
part of speech, pronunciation (IPA or a clear respelling), and a one-sentence
definition. Spend the rest on the documented origin and a telling moment in its
history. Primary = a dictionary/lexical authority that owns the definition
(Merriam-Webster, OED, or equivalent). Secondary = an independent word-history
(etymonline, a reputable etymology column) that is NOT just the same dictionary.
The researcher proposes a specific word with both sources confirmed; the writer may
substitute an equally well-sourced word if a better one surfaces. Avoid a word that
is merely trendy; pick one whose etymology teaches something. Keep the card lively
and brief.

### 2–4. Three news items (favor the United States; importance over attention)
Pick the three most important, verifiable developments from Oct 2–4, 2026. Favor
U.S. national stories. Candidate pool (researcher verifies each against primary
sources and selects the best three; order by importance):

- The Sixth Circuit's last-minute stay of Christa Pike's execution in Tennessee
  (reported 2-1; she would have been the first woman executed in Tennessee in over
  200 years; she requested a firing squad). VERIFY CAREFULLY: at least one
  low-quality source claimed a "botched execution"/ventilator, which conflicts with
  the stay accounts. Establish what actually happened from the court order and
  reputable reporting; attribute anything unverified to its source.
- Fatal ICE-enforcement incidents (reported in Maine, Georgia, Florida within ~24h)
  and the multi-state protests that followed. Verify the facts and the status of
  each incident; make the evidentiary status explicit.
- Governor Hochul naming Attorney General Letitia James special prosecutor in a
  Cornell case. Verify scope and the primary (the governor's order/press release).
- A Latitude air-ambulance Gulfstream reported missing over the Atlantic
  (Bermuda→Boston, six aboard). Verify with aviation-authority / operator primary.

Do not cover the Third Circuit ROSS copyright ruling here (it is the edition's
feature). Avoid repeating recent brief leads (see recent-patterns.md): no SCOTUS
lead, no "N developments for <day>" roundup headline, no "Month NN: Title Case"
date-prefixed headline.

### 5–6. Two technology developments
Both are decided; researcher verifies every figure and resolves the primary record:

- **GPT-6.1 Sol** (OpenAI, announced ~Sep 29, 2026 at Dev Day): a release. Give the
  claim (near-GPT-6-Astra capability at ~1/5 the token price), the exact API prices
  ($2 / $10 per million input/output tokens; $0.10 per million cached input), who is
  making the claim (OpenAI), and availability. Primary = OpenAI's own announcement /
  pricing page; secondary = independent reporting. State that the capability claim is
  the vendor's.
- **SynthID Bio** (Google DeepMind, ~Sep 30, 2026): a research result. Watermarking
  AI-designed protein sequences; DeepMind reports watermarked binders matched
  unwatermarked ones on hit rate, binding affinity, and sequence diversity across
  three wet-lab targets (VEGF-A, SARS-CoV-2 RBD, PD-L1), using AlphaProteo +
  a SynthID-enabled ProteinMPNN. Primary = DeepMind's blog/paper; secondary =
  independent reporting. Give what was announced, who claims it, and what the record
  supports; note it is described as a proof of concept.

Keep both tech items distinct from the technical article (OpenCode V2) and the
feature (copyright). Link the underlying record and independent reporting for each.

## Boundaries

- Each item must stand on its own and introduce its own terms.
- Numbers: give the figure, the range the source gives, and no more precision.
  Attribute vendor/claimant figures to the claimant.
- Headline/dek: the brief's `nb-meta` title + dekline describe the edition. Make the
  headline distinctive to the day's lead (not a generic roundup), per
  `spec/headlines.md` and recent-patterns.md.
- Every source URL must resolve (the proof blocks on 404/dead domains; a paywall or
  403 is fine). Record the document's own canonical page, not a fetch route.

## Template, sources, production

- Template: `brief` (press override; shortread; exactly 6 items; sources section;
  per-item citation; min 12 sources; per-item primary [1,1], secondary [1,null]).
- `nb-meta`: series `daily-brief`, slug `2026-10-04`, mode `rolling`, date
  `2026-10-04`.
- Source policy: `nb source-policy --series daily-brief`.
- Production (`nb production-policy --series daily-brief`): editor required, high
  effort, model inherit. researcher capable/high, writer capable/medium,
  writing-coach capable/low. Recorded: coach/researcher/writer on a capable model
  (sonnet-class), editor on the orchestrator's model (opus-class) at high effort. No
  `required` directive traded down.

## Neighbouring articles in this edition

- feature/thomson-reuters-ross-appeal (copyright ruling) — not in the brief.
- technical/opencode-v2-plugin-api (dev tooling) — not a brief tech item.

## Orchestrator decision (after researcher/01) — verified items

The researcher resolved the open questions (20 sources). Adopt as decided:

- LEAD item is the Pike FAILED execution, not a stay. Verified sequence: the Sixth
  Circuit's 2-1 stay (Sept 30) was VACATED by the Supreme Court the same day, 6-3
  (Sotomayor, Kagan, Jackson dissenting; docket 26A428); Tennessee then carried out the
  injection; Pike survived two doses of pentobarbital; Gov. Lee halted executions for
  the rest of 2026 and ordered a third-party review; TDOC Commissioner Strada announced
  his resignation Oct 3. The "unconscious on a ventilator" claim is from Pike's
  attorneys — attribute it to them (TDOC/governor have not confirmed). DROP the
  firing-squad request (unverified by reputable outlets) or attribute it narrowly.
  Do NOT write a stay-only item.
- Three news items, in order: (1) Pike failed execution; (2) Hochul Executive Order 64
  naming AG James special prosecutor in the Cornell case, displacing the Tompkins
  County DA; (3) Latitude air-ambulance Gulfstream G100 (tail C-GRJP), six aboard,
  Bermuda→Boston, Coast Guard confirmed a debris field Saturday night, people still
  unaccounted for. The ICE-incident cluster is SET ASIDE (unconfirmed; only a Substack
  roundup; the Biddeford, Maine shooting is real but dates to July 2026).
- Word of the Day: "robot" (Merriam-Webster primary; Etymonline secondary). Note the
  sources disagree on first use (1922 vs 1923) — state it carefully or pick the
  attributable one. M-W prints the respelling ˈrō-ˌbät (variant -bət), no IPA; use the
  respelling.
- Tech item GPT-6.1 Sol: prices confirmed on OpenAI's developer pages — $2 input,
  $10 output, $0.10 cached input per million tokens (Astra is $10/$50, cached $1).
  "~1/5" holds for input and output; cached input is ~1/10. "Near-Astra" and all
  benchmarks are OpenAI's own claims — attribute them. Primary = OpenAI developer
  model/pricing pages (the launch blog returns 403; do not use it as the resolving
  primary).
- Tech item SynthID Bio: DeepMind blog is the primary (the Nature paper is gated). It
  confirms the three targets (VEGF-A, SARS-CoV-2 RBD, PD-L1) and AlphaProteo + a
  SynthID-enabled ProteinMPNN, labels the work a "proof of concept", and names
  tamper-robustness as open. It gives NO numeric hit rates/KD values — keep the result
  QUALITATIVE (watermarked designs matched unwatermarked on the tested properties); do
  not invent figures.

Template/source note: the brief requires EXACTLY ONE primary per item (primary [1,1])
plus ≥1 secondary. Where the record lists a second owner-document as a "supporting
primary" (e.g. the TDOC advisory for Pike), tag it data-nb-kind="secondary" in the HTML
so each item has exactly one primary. Pick the single strongest primary per item.
