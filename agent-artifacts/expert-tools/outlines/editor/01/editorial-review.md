# Editorial review: expert-tools/outlines (editor/01)

## Skeptic

Thesis: Outlines guarantees schema-valid output by masking every invalid token
during decoding, using an FSM compiled from the schema and a precomputed
state-to-token index; the guarantee is real but holds only where Outlines owns
the logits, it is no longer the fastest constraint engine, and the accuracy
cost of constraining is contested while the structural guarantee is not.

The claims it stands on, and how each held:

- The mechanism (FSM compiled from the schema, per-state mask, O(N) naive scan,
  O(1) indexed lookup, memory tracking the number of FSM states, CFG trie).
  Checked descriptor by descriptor against the paper (s2) and the docs. O(N)
  per token with N the vocabulary size, O(1) average via the hash-map index
  sigma:Q->P(V), GPT-2 N=50,257, ~50 MB naive Python-grammar index as a loose
  upper bound, CFG trie keyed on parser stack values, and the move of the FSM
  and index into the Rust `outlines-core` "for performance and portability" all
  match the evidence record and the sources I opened. Held.

- The backend caveat (by-construction only where Outlines holds the logits; on
  hosted APIs it delegates to the provider). Both docs quotes verified live:
  "directly from any LLM" (s1) and "not available for all models" (s4). The
  worked example uses the local `from_transformers` path, and the backend
  section states the hosted-API and vLLM/SGLang-runs-XGrammar splits plainly.
  The guarantee is not overclaimed across backends. Held.

- The speed framing (no longer the fastest; weigh against retry-and-parse, not
  against current engines). The paper's own hedge is quoted; XGrammar's "up to
  3.5x / >10x" and llguidance's on-the-fly "~50us, essentially no startup cost"
  are labeled vendor figures, and the piece redirects the comparison to
  retry-and-parse. Held.

- The accuracy question kept separate from the structural guarantee. "Let Me
  Speak Freely?" (76% -> 49% GSM8K under JSON-mode) and dottxt's matched re-run
  (0.77 -> 0.78) are both present, both flagged as interested or small-sample,
  and the piece states the structural guarantee is not in dispute. Held.

- Attribution (2023 paper bylined Normal Computing; library now dottxt-ai).
  Stated without conflation. Held.

Tried hardest to break the claim I most wanted to keep, the by-construction
guarantee: pushed on whether the headline ("masks every invalid token as a
model decodes") overclaims. It states the mechanism as the finding and the dek
carries the scope condition (local vs hosted), which is the headline/dek
division the standard asks for; the body is explicit. It survives.

data-nb-kind audit: all 13 sources labeled primary. Under the authorship-and-
stake test each is primary for the claim it is cited for. The engine-comparison
sources (s6 XGrammar repo, s7 MLC blog, s8 llguidance) are competitors with a
stake, but they are cited only for their own reported figures and integration
facts, and every speed number is labeled a vendor benchmark in prose and in the
table caption, so "primary" is defensible and the interested-party status is
disclosed to the reader. The one genuinely independent critique, "Let Me Speak
Freely?" (s9, academic), is represented and cited; the design/speed critiques
come from interested engines and are framed as such. No sourcing failure hides a
missing independent source.

Citation hrefs: opened all 13 as printed. Each lands on the source's own page
and supports its claim. s12 (pypi.org/project/outlines-core/) returned a bot
challenge, a transport gate rather than a dead link; it is the correct
project-page URL, identical in shape to s11, which loaded and confirmed the
release record. The figure's `data-nb-locator` ("Fig. 1 · Sec. 3") and
`data-nb-url` (the PDF) match the asset's origin.

Code example: audited against the captured API surface. `from_transformers(
hf_model, hf_tokenizer)` matches s3 verbatim; passing a Pydantic `Customer` as
the second argument and validating with `model_validate_json` matches s4; the
`Customer` schema and prompt match the evidence's captured example. Correct, and
on the one path where the guarantee actually holds.

No break found. Nothing routed to the researcher or writer.

## Cut

Sentence-by-sentence slop pass, then the edges alone, then the arrived-from-a-
link read, then the delete test. Four sentences failed and were cut or repaired:

- "The demonstration is the whole reason to keep reading: the string came back
  valid, and the next question is how." Self-reference plus the "X is the whole
  Y" punchline, gesturing at the reader. Cut; the next section heading carries
  the bridge and no fact was lost.
- "Its edges are just as real." Empty parallelism ("its X are just as Y"),
  a hollow hinge into the caveats. Cut; the concrete edge sentences that follow
  do the work.
- "The guarantee is genuine, and worth taking apart, because it is produced
  inside the decoding loop..." Trimmed the "worth taking apart" signpost; the
  surviving clause carries the real mechanism contrast.
- "which is not the FSM engine this piece has been describing" narrated the
  article. Rewritten to "not the FSM constraint engine Outlines runs," which the
  evidence supports.

Punctuation (reflex-semicolon repairs, per the editorial direction's default to
the period): four reader-facing semicolons splitting two thoughts became
periods (the local-vs-hosted turn, the state/sampling step, the uniform-call
contrast, the verdict's first line), plus the Fig. 2 caption where a semicolon
joined a fragment to a clause. The alt-text semicolon and the terse table-cell
semicolon were left as functional and telegraphic, not reader prose. Em-dash
count is 0 of 4.

Precision: "A reader who runs 'Outlines on vLLM'" changed to "A user," since the
actor is a practitioner, not the article's reader, and the overlap read as a
gesture at the reader.

Formula pass against the recent-pattern notes. The recent desk headline mold
("<Tool> <verb>s the work your old tool can't") is not reused; this headline is
built on the piece's own nouns (masks, invalid token, decodes, schema, by
construction). The stamped closer pair ("When the swap pays off" / "What it
costs, and whether to trust it") is not reused; the closer here is "Reach for it
when you own the model and the schema." No heading is "<Tool> does X." One
heading, "It is no longer the fastest, and the accuracy cost is contested,"
opened with a dangling "It" that a headings-only skim cannot resolve and echoed
the prior desk's comma-and closer shape; retitled to name the subject:
"Outlines is no longer the fastest, and its accuracy cost is contested."

Furniture pass. The closing holds-up grid plus Verdict note is the same pairing
recent desk pieces use, so I tested it for formula rather than assuming it. It
carries the adopt-or-not judgment the piece assembles, the Verdict note is the
sanctioned weight-of-evidence landing with its falsifiers, and the closer
heading above it is this piece's own. It earns its place as deliberate emphasis,
not a stamped block, so it stays. The table genuinely carries the three-engine
comparison prose would bury. No component is decoration and none was added or
removed.

Prompt-leakage and borrowed-phrasing passes: the workflow-site list is reworded
reported fact about where the tool fits, not lifted instruction language; no
planning labels or assignment-fulfillment claims; no distinctive phrasing from
the voice-guide exemplars (Luu, Evans, Elhage) appears in the draft.

## Reader

Read straight through as the paper's machine-learning engineer. What I have that
the sources alone would not give me: one assembled adopt-or-not judgment, built
from a paper, the docs, two competitor blogs, and two PyPI records that never sit
together, resolving four findings the evidence records as separate and in
tension into a single call, depend on it where you own the logits, treat its
speed as adequate not leading, confirm whether your stack runs Outlines or
XGrammar, and keep the accuracy question open. The original-work sentence in the
draft handoff claims exactly that synthesis, and it survives the read. The prose
sits closer to the voice-guide exemplars than a median summary: the guarantee is
stated early and proved by the code and the FSM figure before it is explained,
the numbers do the arguing, and the release cadence carries the maintenance
judgment without reaching for a grading adjective. The headline, read last as the
largest claim, is one the piece defends on its demonstrated path and the dek
scopes.

## Edits

- Cut "The demonstration is the whole reason to keep reading: the string came back valid, and the next question is how." (self-reference / unearned punchline).
- Cut "Its edges are just as real." (empty parallelism).
- Trimmed "and worth taking apart," from the orientation guarantee sentence (signpost).
- Rewrote "which is not the FSM engine this piece has been describing" to "not the FSM constraint engine Outlines runs" (self-reference).
- Retitled the speed/accuracy heading from "It is no longer the fastest, and the accuracy cost is contested" to "Outlines is no longer the fastest, and its accuracy cost is contested" (dangling referent; comma-and echo of the prior closer).
- Semicolon to period: "...where Outlines controls the logits. Point the same call at a hosted API...".
- Semicolon to period: "...while a digit or a dot is allowed. Sampling .2 advances the machine...".
- Semicolon to period: "The uniform call is a real convenience. The guarantee behind it is not uniform.".
- Semicolon to period in the Verdict: "...when you run the model yourself. That guarantee is real...".
- Semicolon to period in the Fig. 2 caption: "...passed as the output type. The result is a JSON string...".
- "A reader who runs 'Outlines on vLLM'" to "A user who runs 'Outlines on vLLM'" (precision).

## Required work

None blocking. For the orchestrator: the direct cuts changed the body slightly,
so the article needs a re-stamp (the nb-meta word and reading counts) and a
re-proof before the PR. No work routed to the researcher or writer.

## Decision

approve — the mechanism, backends, speed framing, accuracy split, attribution,
citations, code, and figure all hold, and the prose failures found were the
editor's to cut directly.
