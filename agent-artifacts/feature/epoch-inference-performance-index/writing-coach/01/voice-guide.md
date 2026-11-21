# Voice guide: feature/epoch-inference-performance-index (01)

## How this piece should sound

The register is one engineer explaining to another how a number was made. The reader builds ML systems and knows what a matmul, a KV cache and a batch size are, so the piece spends its words on how the index is constructed and what each choice does to the result, and none on defining the field. Horace He and kipply both write to a reader like this: they put hardware figures next to each other and let the reader see the ratio. Their sentences are plain and first-person where a judgment is being made ("which I find really cute", "I say may a lot here"). A few words of the practitioner's slang are fine where the field uses them.

Where the article reports a measured result, it can sound like Brendan Gregg: say what the benchmark actually tests, what limited it, and why the result was X and not 2X. His passages show a writer who distrusts a bare comparison and says so in a sentence. The piece's own reader will meet FLOP/s comparisons and vendor tables daily, so the doubt belongs in the same plain voice, aimed at the unit and the method. It should never be aimed at a person.

Hardware terms stay exact and unexplained beyond a clause: memory bandwidth, scale-up domain, low-precision formats, latency target, batch size, arithmetic and geometric mean. He and kipply never swap in a looser word for the sake of variety. Where one quantity is the point, give it beside a quantity the reader already holds, as He does with 400 billion numbers loaded against 20 trillion operations.

A ratio and its two inputs can be given in one sentence when the reader needs all three to check it. Kipply walks from a hardware spec to a single derived number and then says what that number means for the reader's system. The same step can carry a stated index construction, where a sentence says where each figure comes from and what the next step does to it.

Where the article is unsure, or the source is silent, one plain sentence saying what is not known does the work, in the way Gregg states what a result can and cannot be used for. Humor, if any, comes from a specific figure or the field's own habits, as in He's Python-versus-A100 comparison. Keep out vendor launch vocabulary and any sentence the reader could not check. Keep the persona of each exemplar out too: none of them is the voice of this paper.

## Horace He, "Making Deep Learning Go Brrrr From First Principles"

Source: https://horace.io/brrr_intro.html

> "Just like with training ML models, knowing what regime you're in allows you to narrow in on optimizations that matters. For example, if you're spending all of your time doing memory transfers (i.e. you are in an memory-bandwidth bound regime), then increasing the FLOPS of your GPU won't help. On the other hand, if you're spending all of your time performing big chonky matmuls (i.e. a compute-bound regime), then rewriting your model logic into C++ to reduce overhead won't help."

Checked: https://horace.io/brrr_intro.html (raw HTML fetched and stripped), retrieved 2026-11-21
He states the consequence for each regime in a sentence of its own, using the terms his reader already uses. The "i.e." clauses name the regime in passing. The person shows in one informal word, "chonky", placed where the technical content is already complete.

> "For simple operators, it's feasible to reason about your memory bandwidth directly. For example, an A100 has 1.5 terabytes/second of global memory bandwidth, and can perform 19.5 teraflops/second of compute. So, if you're using 32 bit floats (i.e. 4 bytes), you can load in 400 billion numbers in the same time that the GPU can perform 20 trillion operations."

Checked: https://horace.io/brrr_intro.html (raw HTML fetched and stripped), retrieved 2026-11-21
Two spec-sheet figures are turned into one comparison a reader can picture, with the unit conversion shown (4 bytes per float). The arithmetic is short enough to follow without a pencil, and the numbers are the A100's own published ones.

> "The primary reason overhead is such a pernicious problem is that modern GPUs are really fast. An A100 can perform 312 trillion floating point operations per second (312 TeraFLOPS). In comparison, Python is really slooooowwww. Benchmarking locally, Python can perform 32 million additions in one second."

Checked: https://horace.io/brrr_intro.html (raw HTML fetched and stripped), retrieved 2026-11-21
The joke is the stretched word "slooooowwww", and it sits between two figures that carry the claim. He says he benchmarked it himself, which puts a person at a machine.

## kipply, "Transformer Inference Arithmetic"

Source: https://kipp.ly/transformer-inference-arithmetic/

> "We assume (correctly, this has been very well optimised) that we can start the computations while we load the weights. Flop bound would then mean that there is time when nothing is being passed through memory, and memory bound would mean that no floperations are occurring. Nvidia uses the term math bandwidth which I find really cute."

Checked: https://kipp.ly/transformer-inference-arithmetic/ (raw HTML fetched and stripped), retrieved 2026-11-21
An assumption is stated with its justification in a parenthesis, then the two regimes are defined against each other in one sentence. The writer's own taste appears in the last sentence, which is about a term and not about the argument.

> "None of the model architecture matters anymore — we get a distinct ratio here of 208 given this hardware specification. This means that if we're going to compute kv for one token, it'll take the same amount of time to compute for up to 208 tokens! Anything below, we're memory bandwidth bound. Above, flops bound."

Checked: https://kipp.ly/transformer-inference-arithmetic/ (raw HTML fetched and stripped), retrieved 2026-11-21
One derived number is followed by what it means for a single token and then by the two-sided rule, in short sentences. The exclamation mark is the writer's own pleasure at the result. The short last two sentences carry the finding.

> "If an API had the load for large batches it would probably want to serve the lowest batch size that gets flop bound even if there is capacity left so that it could optimise for per-request-latency. In say mass-inferencing jobs like AlphaCode we might want to insert as many chips as we can and then do the largest batch we can do with that capacity. I say "may" a lot here but I actually think these are absolute and all three kinds of cases."

Checked: https://kipp.ly/transformer-inference-arithmetic/ (raw HTML fetched and stripped), retrieved 2026-11-21
The latency regime (an API serving per-request latency) and the throughput regime (a mass-inference job) are set against each other with a concrete example for each. The last sentence reports the writer's own hedging habit and then overrides it, so the reader sees how sure the writer is.

## Brendan Gregg, "Active Benchmarking"

Source: https://www.brendangregg.com/activebenchmarking.html

> "Debugging benchmarks is something I've done for many years, and I've seen an amazing and comical variety of failure modes. The problem is that benchmark tools are often run without understanding what they are testing or checking that the results are valid. This can lead to poor development or architectural choices that haunt you later on."

Checked: https://www.brendangregg.com/activebenchmarking.html (raw HTML fetched and stripped), retrieved 2026-11-21
He opens with his years of doing the work, which is why the claim is believed, then names the failure and what it costs a team. The sentences are plain and a little rueful.

> "A telltale sign is when the only technical results presented are the benchmark results. I've seen countless slide decks, blog posts, and articles that present an impressive bar chart of comparitive results, but then no supporting technical evidence. It's been my job to get to the bottom of many of these, and I typically find that they are wrong or misleading almost every time."

Checked: https://www.brendangregg.com/activebenchmarking.html (raw HTML fetched and stripped), retrieved 2026-11-21
This describes a recognizable artifact, the bar chart with no mechanism beside it, and then gives how often he found it wrong, in his own words and from his own job. The skepticism is aimed at a practice and not at a named person. The source's spelling "comparitive" is kept as published.

> "The most common case is where a benchmark is not really testing what it claims to test, which can be identified using active benchmarking. Sometimes the results are still useful, now that they can be interpreted correctly."

Checked: https://www.brendangregg.com/activebenchmarking.html (raw HTML fetched and stripped), retrieved 2026-11-21
After the criticism he says what survives: a flawed benchmark can still be used once its target is understood. The two sentences give the limit and the use of a result without a verdict on the people who ran it.
