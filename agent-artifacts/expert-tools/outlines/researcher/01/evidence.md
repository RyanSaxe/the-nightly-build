# Evidence record: expert-tools/outlines (01)

The evidence supports the commission's core claim firmly: Outlines constrains a
language model's decoding so output matches a regex, JSON schema, choice set, or
context-free grammar, and the mechanism is the one the commission names. The
2023 paper by Willard and Louf reconstructs it from first principles: compile the
target to a finite-state machine, precompute a hash-map index from FSM state to
the set of vocabulary tokens valid in that state, and at each step mask the logits
of every token the index excludes. The paper's own words put the naive cost at
O(N) per token (N = vocabulary size) and the indexed cost at O(1) on average. All
of that is checkable in the primary and holds.

Three places need care in the writing. First, the paper's performance framing is
dated. Its only benchmark is a single-run timing against one competitor, Guidance
(2023), which the paper itself hedges. Newer engines, XGrammar and llguidance,
now claim to beat Outlines and criticize the precomputed-index approach directly
for startup cost and memory, so Outlines is not the speed leader among constraint
engines today and should not be written as one. Second, the "valid by
construction" guarantee only fully applies on backends where Outlines controls
the logits (local and open-weight models); with hosted APIs (OpenAI, Anthropic,
Gemini) it delegates to the provider's own structured-output feature and the
paper's FSM masking does not run. Third, whether constraining decoding hurts task
accuracy is genuinely contested (the "Let Me Speak Freely?" paper versus dottxt's
rebuttal); the structural guarantee is not contested, the accuracy effect is.
Note also the byline: the paper was written at Normal Computing in 2023; the
library is now developed by .txt (dottxt-ai). The commission's present-day
attribution to dottxt-ai is correct, but the paper predates the company.

The maintenance read is unambiguous and positive: 84 PyPI releases, latest 1.3.3
six days before this record, with multiple releases per month through 2026.

## Sources

```text
URL:         https://arxiv.org/abs/2307.09702
Kind:        primary. The paper that owns the mechanism and the complexity
             claims; the authors are the library's original authors.
Establishes: The FSM-over-vocabulary masking mechanism, the precomputed index,
             the O(N) vs O(1) claim, CFG handling via pushdown automata, and the
             sole published benchmark against Guidance.
Paraphrase:  Neural text generation is reframed as transitions between the states
             of a finite-state machine; regex and CFG guidance then reduce to
             building an index over the vocabulary. The approach is model-
             agnostic, guarantees output structure, "adds little overhead," and
             "significantly outperforms existing solutions."
Locators:    Abstract; Sec. 1; Sec. 2.2 (masking); Sec. 3 (FSM + index);
             Sec. 3.2 (Guidance comparison); Sec. 4 (CFG/PDA); Sec. 5.
Quote:       "This approach entails a fixed O(N) cost for each token generated,
             where N is the size of the LLM's vocabulary." (Sec. 1) / "The result
             is an algorithm that costs O(1) on average." (Sec. 1) / "Using a
             hash-map for sigma can make the m step in Algorithm 2 cost only O(1)
             on average." (Sec. 3)
```

```text
URL:         https://arxiv.org/pdf/2307.09702
Kind:        primary. Full text of the same paper, read in full for the
             algorithms the abstract omits.
Establishes: Index construction (Algorithm 4 maps every vocabulary string to the
             FSM states that accept it, via Algorithm 3 which tries every viable
             start state). The index sigma: Q -> P(V). Memory is proportional to
             the number of FSM states |Q|; a naive Python-grammar index is
             ~50 MB with un-reduced DFAs. CFGs use a pushdown automaton over an
             LALR(1) parser and the index becomes a trie keyed on stack values.
Paraphrase:  Because a vocabulary string can match an arbitrary part of a regex,
             the index is built by starting matching in every viable FSM state,
             not just q0. The resulting state-to-token map lets each decoding step
             look up valid tokens instead of scanning the whole vocabulary.
Locators:    Sec. 3, Algorithms 3 and 4; Sec. 4.1 (PDA definition and trie);
             Sec. 5 (the 50 MB figure).
Quote:       "even naively constructed indices ... are still only around 50 MB."
             (Sec. 5) / "the index will need to be a trie data structure in order
             to allow queries against the parser's stack values." (Sec. 4.1)
```

```text
URL:         https://dottxt-ai.github.io/outlines/latest/
Kind:        primary. The library's own current documentation.
Establishes: What Outlines says it guarantees and the output types and backends
             it supports, current API shape.
Paraphrase:  "Outlines guarantees structured outputs during generation — directly
             from any LLM," with "Guaranteed schema compliance -- always valid
             JSON." Output types: basic Python types, multiple choice, JSON
             schema / Pydantic, regex, and context-free grammar. Backends listed:
             vLLM (online/offline), Transformers, llama.cpp, Ollama, MLX-LM,
             SGLang, TGI, OpenAI, Anthropic, Gemini, Dottxt.
Locators:    Landing page ("Welcome to Outlines"); features list; first example.
Quote:       Current-API example, verbatim:
             from pydantic import BaseModel
             from typing import Literal
             import outlines
             import openai
             class Customer(BaseModel):
                 name: str
                 urgency: Literal["high", "medium", "low"]
                 issue: str
             client = openai.OpenAI()
             model = outlines.from_openai(client, "gpt-4o")
             customer = model("Alice needs help with login issues ASAP", Customer)
```

```text
URL:         https://dottxt-ai.github.io/outlines/1.0.2/guide/getting_started/
Kind:        primary. Current-API getting-started guide (1.x line).
Establishes: The exact 1.x local-model API surface the writer must reproduce.
Paraphrase:  A model is wrapped with outlines.from_transformers(hf_model,
             hf_tokenizer); the wrapped model is called as model(prompt) for free
             text or model(prompt, OutputType) for constrained output;
             outlines.Generator(model, OutputType) is the reusable-generator form.
Locators:    Getting Started, first local-model example.
Quote:       Verbatim:
             import outlines
             from transformers import AutoModelForCausalLM, AutoTokenizer
             model_name = "HuggingFaceTB/SmolLM2-135M-Instruct"
             hf_model = AutoModelForCausalLM.from_pretrained(model_name)
             hf_tokenizer = AutoTokenizer.from_pretrained(model_name)
             model = outlines.from_transformers(hf_model, hf_tokenizer)
             result = model("Write a short story about a cat.")
```

```text
URL:         https://dottxt-ai.github.io/outlines/latest/features/core/output_types/
Kind:        primary. The output-types reference.
Establishes: The type constructors and the calling convention; the honest limit
             that structured output is not available on every backend.
Paraphrase:  Output types are imported as outlines.types.Choice, JsonSchema,
             Regex, and CFG, or given as a Pydantic BaseModel. The output type is
             passed as the second argument to the model call, e.g.
             model("Create a character", Character, max_new_tokens=100), and the
             result is a JSON string validated with Character.model_validate_json.
             A Regex type is built as Regex(r"[0-9]{3}").
Locators:    Output Types page; per-type sections; the support-limitation note.
Quote:       "Output types ... are not available for all models as some have only
             limited support for structured outputs."
```

```text
URL:         https://github.com/dottxt-ai/outlines
Kind:        primary. The project repository.
Establishes: Maintainer and repository activity signal. Description: structured
             outputs "directly from any LLM," "No more parsing headaches or broken
             JSON." Supported types match the docs (choice, JSON/Pydantic, regex,
             CFG, function calls, basic types).
Paraphrase:  Maintained by .txt (dottxt-ai). Repository-page figures on
             2026-08-12: ~15.6k stars, 94 open issues, 45 open pull requests,
             1,324 commits on main. License Apache-2.0.
Locators:    Repository header and README.
Quote:       "Outlines guarantees structured outputs during generation — directly
             from any LLM."
Note:        The GitHub REST API was gated in this session, so issue/PR/star
             counts are read from the rendered repository page, not the API. Use
             the PyPI release record below as the authoritative maintenance
             signal.
```

```text
URL:         https://pypi.org/pypi/outlines/json
Kind:        primary. The package's own release record.
Establishes: Latest version, release cadence, Python support, license. This is the
             owning source for every version and date claim about the library.
Paraphrase:  Latest 1.3.3, uploaded 2026-08-06. 84 total releases. Recent cadence:
             1.3.2 (2026-07-20), 1.3.1 (2026-06-30), 1.3.0 (2026-05-13), 1.2.13
             (2026-05-04), 1.2.12 (2026-03-03). requires_python <3.14,>=3.10.
             License Apache-2.0. Author "Outlines Developers." Optional extras
             include transformers, vLLM, Ollama, OpenAI, Anthropic, Gemini.
Locators:    info.version; releases object; info.requires_python; info.license.
```

```text
URL:         https://github.com/dottxt-ai/outlines-core
Kind:        primary. The Rust core the FSM/index work was moved into.
Establishes: The paper's index and FSM compilation now live in a separate Rust
             package with Python bindings, "formerly implemented in Outlines,"
             refactored for "performance and portability." It builds regexes from
             JSON schemas and constructs the token-to-state index.
Paraphrase:  outlines-core provides the regex-from-schema step and the index
             object mapping tokens to FSM transitions. The README frames this as
             the extracted core of the main library, not as new research.
Locators:    Repository README; repository header (~303 stars, Apache-2.0).
```

```text
URL:         https://pypi.org/pypi/outlines-core/json
Kind:        primary. Release record for the Rust core.
Establishes: The core moves slower than the wrapper. Latest 0.2.14 (2026-01-09),
             17 total releases; prior 0.2.13 (2025-10-15), 0.2.11 (2025-05-19).
             requires_python >=3.8, Apache-2.0.
Locators:    info.version; releases object.
Scope:       Relevant because a reader trusting the paper's mechanism is trusting
             this package, whose 2026 cadence is a few releases a year against the
             wrapper's few a month.
```

```text
URL:         https://blog.mlc.ai/2024/11/22/achieving-efficient-flexible-portable-structured-generation-with-xgrammar
Kind:        primary for XGrammar's own benchmark; secondary as a characterization
             of Outlines (a competitor reporting on it, with stake).
Establishes: A named alternative and the claim that Outlines is no longer the
             fastest constraint engine. XGrammar (mlc-ai, Apache-2.0) reports "up
             to 3.5x" faster logits masking on JSON schema and "more than 10x" on
             CFG, and "up to 14x" (JSON schema) / "up to 80x" (CFG) end-to-end,
             against baselines including Outlines (Rust 0.1.3, Python 0.0.45),
             llama.cpp, and lm-format-enforcer.
Paraphrase:  XGrammar uses an explicit stack-based character-level parser plus
             precomputation of some token masks, and reports large speedups over
             the systems it tests, Outlines among them.
Locators:    Performance section (latency and speedup figures); baselines list.
Note:        These are the vendor's own figures against its own harness; treat as
             a claim by an interested party, not an independent measurement.
```

```text
URL:         https://github.com/mlc-ai/xgrammar
Kind:        primary. The XGrammar project itself.
Establishes: XGrammar is CFG-based, "ensure[s] 100% structural correctness," is
             Apache-2.0 (~1.8k stars), and is integrated into vLLM (Dec 2024) and
             SGLang (Nov 2024) as a default structured-generation backend.
Paraphrase:  A separate, actively adopted constraint engine offering the same
             structural guarantee Outlines does, now shipping inside the serving
             stacks Outlines also targets.
Locators:    Repository README; integration notes.
Scope:       Matters because "Outlines runs on vLLM/SGLang" and "vLLM/SGLang ship
             XGrammar" are both true; the guarantee a vLLM user gets may come from
             XGrammar, not from Outlines' own index.
```

```text
URL:         https://github.com/guidance-ai/llguidance
Kind:        primary for llguidance; secondary and interested as a critique of
             Outlines (a competing engine describing Outlines' tradeoff).
Establishes: The sharpest technical objection to the precomputed-index design.
             llguidance (guidance-ai / Microsoft, MIT, ~832 stars) computes token
             masks on the fly with "essentially no startup cost," ~50us of
             single-core CPU time per token for a 128k-token tokenizer, under 50us
             average across 2.5M tokens / 10k JSON schemas, <1% over 1ms.
Paraphrase:  llguidance argues that precomputing masks for all automaton states,
             the Outlines approach, brings startup cost and memory overhead and
             limits constraint complexity, and that on-the-fly masking avoids all
             three.
Locators:    README overview; "Comparison to Outlines"; mask-latency benchmark.
Quote:       "Outlines builds an automaton from constraints and then pre-computes
             token masks for all automaton states, potentially making sampling
             fast but inherently limiting constraint complexity and introducing
             significant startup cost and memory overhead. Llguidance computes
             token masks on the fly and has essentially no startup cost."
```

```text
URL:         https://arxiv.org/abs/2408.02442
Kind:        primary. The critique paper that opened the accuracy debate. Read via
             the ar5iv HTML rendering; the address above is the document's own
             page on arXiv.
Establishes: "Let Me Speak Freely?" (Tam, Wu, Tsai, Lin, Lee, Chen; Appier AI
             Research and National Taiwan University; EMNLP 2024 Industry Track).
             Claim: stricter format constraints degrade LLM reasoning. Reported
             GPT-3.5-turbo GSM8K accuracy ~76% natural language versus ~49%
             JSON-mode.
Paraphrase:  The study argues format restriction costs reasoning accuracy and
             tests JSON-mode as its strictest setting.
Locators:    Abstract; reasoning-task results (GSM8K); Format-Restricting
             Instructions vs JSON-mode distinction.
Quote:       "stricter format constraints generally lead to greater performance
             degradation in reasoning tasks."
Note:        The paper's strictest arm is JSON-mode (a provider flag / prompting),
             which is not the same as an FSM constraint engine like Outlines. This
             is the crux of the rebuttal below.
```

```text
URL:         https://blog.dottxt.ai/say-what-you-mean.html
Kind:        primary. dottxt's own rebuttal, by an interested party (the company
             behind Outlines).
Establishes: The counterargument and re-run figures. Author Will Kurt, .txt.
Paraphrase:  The rebuttal argues the critique's "structured" arm was JSON-mode
             prompting with no schema and no constraint engine, used mismatched
             prompts across conditions, and relied on an LLM (Claude-3-Haiku) as
             parser that underperformed hand-written regex (57% vs 61% on their
             cases). On matched re-runs, structured generation matched or beat
             unstructured.
Locators:    Methodology critique; results table.
Quote:       Re-run accuracy (unstructured -> structured): GSM8K 0.77 -> 0.78;
             Last Letter 0.73 -> 0.77; Shuffle Object 0.41 -> 0.44.
Note:        Interested party. The structural guarantee it defends is not in
             dispute; the accuracy claim is, and both sides are recorded here.
```

## Contradictions

- **Speed leadership is stale.** The paper's "significantly outperforms existing
  solutions" rests on one single-run comparison against Guidance in 2023, over
  which the paper itself writes "Barring any configuration oversights that might
  be creating a large run-time discrepancy" (Sec. 3.2). XGrammar and llguidance
  now report beating Outlines, and llguidance names the precomputed index as a
  liability (startup cost, memory, constraint-complexity limits). The mechanism
  claim holds; the "fastest" implication does not. Write Outlines against
  retry-and-parse, its real replacement, not against current constraint engines.

- **The guarantee is backend-dependent.** The docs promise valid output "directly
  from any LLM," but the same docs concede structured output "is not available for
  all models." On hosted APIs (OpenAI, Anthropic, Gemini) Outlines relies on the
  provider's structured-output feature, not the FSM masking the paper describes.
  The paper's by-construction guarantee is a property of the local/open-weight
  path where Outlines (via outlines-core) owns the logits. These two statements
  sit in tension and the article should resolve them explicitly.

- **The vLLM/SGLang path may not be Outlines' own index.** XGrammar is the
  default structured-generation backend inside vLLM and SGLang. A reader who runs
  "Outlines on vLLM" and one who runs "vLLM structured output" may be exercising
  different engines. The guarantee is the same; the code path and its costs are
  not.

- **The accuracy effect is contested; the structural guarantee is not.** "Let Me
  Speak Freely?" reports large reasoning drops under format restriction; dottxt's
  rebuttal attributes those to JSON-mode prompting and experimental mismatch and
  shows flat-to-positive results on matched re-runs. Both are interested or
  single-study, so the honest statement is that structural validity is guaranteed
  and the reasoning-cost question is open.

- **Affiliation shifted.** The paper's byline is Normal Computing (2023) and its
  reference points to github.com/normal-computing/outlines; the library is now
  dottxt-ai/outlines, maintained by .txt. The commission's dottxt-ai attribution
  is correct for today but the paper predates the company.

## Numbers

```text
Figure: O(N) per generated token, naive masking
Owner:  arXiv:2307.09702 (Sec. 1)
Scope:  N = vocabulary size; the cost of scanning the whole vocabulary each step.
```

```text
Figure: O(1) on average, indexed masking
Owner:  arXiv:2307.09702 (Sec. 1, Sec. 3)
Scope:  Per-step token-set lookup via a hash-map index sigma: Q -> P(V); the
        index build is amortized out of the decoding loop.
```

```text
Figure: ~50 MB
Owner:  arXiv:2307.09702 (Sec. 5)
Scope:  A naively constructed index for a slightly augmented Python grammar, with
        un-reduced DFAs; offered as an upper-ish bound, not a typical schema.
```

```text
Figure: N = 50,257
Owner:  arXiv:2307.09702 (Sec. 3.2)
Scope:  GPT-2 vocabulary size, the per-step scan Guidance performed in the
        comparison.
```

```text
Figure: latest 1.3.3, uploaded 2026-08-06; 84 total releases
Owner:  pypi.org/pypi/outlines/json
Scope:  The outlines package; recent cadence several releases per month in 2026.
```

```text
Figure: outlines-core latest 0.2.14, uploaded 2026-01-09; 17 total releases
Owner:  pypi.org/pypi/outlines-core/json
Scope:  The Rust core holding the index/FSM code; a few releases per year.
```

```text
Figure: ~15.6k stars, 94 open issues, 45 open PRs, 1,324 commits
Owner:  github.com/dottxt-ai/outlines (repository page, read 2026-08-12)
Scope:  Repository-page display, not the REST API (API gated this session).
```

```text
Figure: XGrammar "up to 3.5x" (JSON schema mask) / ">10x" (CFG mask);
        "up to 14x" / "up to 80x" end-to-end
Owner:  blog.mlc.ai (2024-11-22), XGrammar's own benchmark
Scope:  Vendor harness vs Outlines (Rust 0.1.3 / Python 0.0.45), llama.cpp,
        lm-format-enforcer; an interested-party measurement.
```

```text
Figure: llguidance ~50us single-core CPU per token, 128k-token tokenizer;
        <50us average over 2.5M tokens / 10k schemas; <1% over 1ms
Owner:  github.com/guidance-ai/llguidance (README benchmark)
Scope:  On-the-fly mask computation; an interested-party measurement.
```

```text
Figure: GPT-3.5-turbo GSM8K ~76% natural language vs ~49% JSON-mode
Owner:  arXiv:2408.02442 ("Let Me Speak Freely?")
Scope:  The critique's headline reasoning-degradation result; strictest arm is
        JSON-mode, not an FSM constraint engine.
```

```text
Figure: matched re-run, unstructured -> structured: GSM8K 0.77->0.78;
        Last Letter 0.73->0.77; Shuffle Object 0.41->0.44
Owner:  blog.dottxt.ai/say-what-you-mean.html
Scope:  dottxt's re-run under matched prompts; interested party; small sample.
```

## Source assets

```text
Asset: Figure 1, arXiv:2307.09702 (Sec. 3) — FSM masking for the regex
       ([0-9]*)?\.?[0-9]*, three panels showing the automaton advancing through
       states 0/1/2/3 as ".2" then "1" are sampled, with the logit column beside
       each panel showing which of "A", ".", "42", ".2", "1" are masked.
Shows: The whole mechanism in one picture: FSM state determines the mask, and the
       mask changes as tokens are sampled. This is the single best artifact for
       the article's mechanism section.
Crop:  Must retain at least one state transition together with its logit/mask
       column so the reader sees state-drives-mask; may omit the third panel to
       fit. Do not crop away the state labels or the masked "A".
```

```text
Asset: The runtime plot in Sec. 3.2, arXiv:2307.09702 — generated-tokens (x, up
       to 100) vs runtime in seconds (y), one steeply rising "guidance" curve to
       ~120s and one near-flat "outlines" curve.
Shows: The scaling difference the paper claims. Useful only if paired with the
       paper's own hedge and the note that it is a single run against a 2023
       version of one competitor.
Crop:  Keep both curves and both axis labels. Do not present it without the
       caveat; on its own it overstates a current speed claim.
```

```text
Asset: Algorithms 3 and 4, arXiv:2307.09702 (Sec. 3) — pseudocode for finding the
       FSM sub-sequences that accept a vocabulary string and for building the
       state-to-vocabulary map.
Shows: How the index is constructed, for a reader who wants the build step rather
       than the intuition. Better rendered by the writer as a short prose walk or
       a re-typeset listing than screenshotted.
Crop:  If shown as an image, keep the loop over the vocabulary and the sigma
       update; a screenshot of raw pseudocode is weak furniture, prefer prose.
```

```text
Asset: For the Outlines docs and repository — None found. The value is the code
       example (captured verbatim above), which belongs in the article as a code
       listing, not as a screenshot of a docs page.
Shows: n/a
Crop:  n/a
```

## Discarded

```text
URL: https://huggingface.co/papers/2307.09702 — Hugging Face's paper page mirrors
     the arXiv abstract; the arXiv primary was used instead.
URL: https://www.semanticscholar.org/paper/... c4ceaef... — index/aggregator page
     for the same paper; not the owning source.
URL: https://pypistats.org/packages/outlines — download stats, not needed; no
     version or mechanism claim rests on download counts.
URL: https://medium.com/@brijeshrn/beyond-free-form-text-... — secondary blog
     overview of constrained decoding; adds no claim the primaries do not own.
URL: https://letsdatascience.com/blog/structured-outputs-... — secondary
     explainer; superseded by the paper and the docs for every claim used.
URL: https://arxiv.org/abs/2501.10868 (JSONSchemaBench) — relevant independent
     benchmark surfaced in search but not opened directly; not cited so it is not
     recorded as read. Flagged for a later invocation if independent accuracy
     numbers are wanted.
```
