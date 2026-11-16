# Voice guide: feature/toolturns-multi-turn-agents (01)

## How this piece should sound

The readers build ML systems in production and have the degrees to follow a probability argument without being walked through it. The register is that of a colleague who has run the evaluation and is showing the result: plain declaratives, the field's own vocabulary (per-turn success, dialogue completion, rubric, user simulator, checker), and no tutorial voice. Eugene Yan's passage on thresholds and Chip Huyen's passage on retries both treat the reader as someone who ships systems. They define a term in a clause when it first appears and go straight to what it costs in a deployment. Keep to that scale: a term gets a clause, and a mechanism gets a figure.

At 600 to 1200 words the prose does little, and the figures carry the argument. Yan's note on accuracy and Huyen's retry arithmetic show how short a paragraph can be when the number is in it. The sentence says what the figure shows, gives the one figure a reader should hold, and stops. Where a result could be taken the wrong way, the sentence that qualifies it names what was and was not measured, as Yan does when he says a model can score well on AUC and still be unusable.

A person should be visible. Yan writes "IMHO" and "I prefer" where the call is a judgment. Hamel Husain says what he has seen go wrong and from where he saw it. Here the writer's stance is a plain verdict on what the paper's numbers support, held at the strength the numbers allow. This is one preprint with a simulator-driven design, and the sentence that says so can be short and flat, with no ceremony around it.

Where the paper's tables permit a computation the paper does not present, report it as a computation: inputs, operation, result, the same way Huyen counts "one retry means 2x the number of API calls". Where the tables do not permit it, say what is reported and stop. Humor, if any, comes from the subject's own nouns and stays dry.

Keep the register constant from the opening finding to the last sentence. The exemplars show no flourish at the ends of paragraphs.

## Eugene Yan, "Task-Specific LLM Evals that Do & Don't Work"

Source: https://eugeneyan.com/writing/evals/

> "If you've run off-the-shelf evals for your tasks, you may have found that most don't work. They barely correlate with application-specific performance and aren't discriminative enough to use in production. As a result, we could spend weeks and still not have evals that reliably measure how we're doing on our tasks."

Checked: https://eugeneyan.com/writing/evals/ (raw HTML, retrieved 2026-11-16)
The opening states the problem in the practitioner's terms, with the cost counted in weeks. "You may have found" puts the reader's likely experience first, and "we" puts the author in the same position.

> "Examining the separation of distributions is valuable because a model can have high ROC-AUC and PR-AUC but still not be suitable for production. For example, if a chunk of the predicted probabilities fall between 0.4 and 0.6 (below), it'll be hard to choose a threshold—getting it wrong by merely 0.05 could lead to a big drop in precision or recall."

Checked: https://eugeneyan.com/writing/evals/ (raw HTML, retrieved 2026-11-16)
A claim about why an aggregate metric misleads, followed at once by a concrete case with numbers and a pointer to the figure. The technical terms are used without gloss. The writer is visible in the choice of which failure to warn about.

> "IMHO, accuracy is too coarse a metric to be useful. We'd need to separate it into recall and precision at minimum, ideally across thresholds."

Checked: https://eugeneyan.com/writing/evals/ (raw HTML, retrieved 2026-11-16)
An opinion marked as an opinion, then the specific replacement in the next sentence. Two sentences, no hedging beyond the "IMHO".

## Chip Huyen, "Building A Generative AI Platform"

Source: https://huyenchip.com/2024/07/25/genai-platform.html

> "AI models are probabilistic, which means that if you try a query again, you might get a different response. Many failures can be mitigated using a basic retry logic."

Checked: https://huyenchip.com/2024/07/25/genai-platform.html (raw HTML, retrieved 2026-11-16)
A premise stated in one clause and the practical consequence in the next. The prose assumes the reader builds systems and moves to the engineering consequence.

> "This retry policy, however, can incur extra latency and cost. One retry means 2x the number of API calls. If the retry is carried out after failure, the latency experienced by the user will double."

Checked: https://huyenchip.com/2024/07/25/genai-platform.html (raw HTML, retrieved 2026-11-16)
The cost is worked out as arithmetic in short sentences, each one a step the reader can check. The sentences carry no adjectives.

> "Reliability vs. latency tradeoff: While acknowledging the importance of guardrails, some teams told me that latency is more important. They decided not to implement guardrails because they can significantly increase their application's latency. However, these teams are in the minority."

Checked: https://huyenchip.com/2024/07/25/genai-platform.html (raw HTML, retrieved 2026-11-16)
The author reports what teams told her and what proportion held the view, so the evidence is attributed to practitioners she spoke with. The minority view is stated fairly before she gives hers.

## Hamel Husain, "Your AI Product Needs Evals"

Source: https://hamel.dev/blog/posts/evals/

> "To know whether your AI product is working, you need a way to measure success beyond vibe checks (which are useful, but not enough). This calls for product evals tailored to your users' tasks, which measure something different from general model benchmarks."

Checked: https://hamel.dev/blog/posts/evals/ (raw HTML, retrieved 2026-11-16)
Concedes the competing practice in a parenthesis, then says what the evaluation has to measure instead. The distinction between product evals and general benchmarks is drawn in one sentence.

> "However, as Lucy's surface area expanded, the performance of the AI plateaued."

Checked: https://hamel.dev/blog/posts/evals/ (raw HTML, retrieved 2026-11-16)
One short sentence reports what happened in a named system, with a concrete noun as its subject. The author is a participant telling what he saw.

> "If you streamline your evaluation process, all other activities become easy. This is very similar to how tests in software engineering pay massive dividends in the long term despite requiring up-front investment."

Checked: https://hamel.dev/blog/posts/evals/ (raw HTML, retrieved 2026-11-16)
An analogy to something the reader already does, used to make a claim about evaluation concrete. The cost it names is up-front investment, which is how the reader would weigh it.
