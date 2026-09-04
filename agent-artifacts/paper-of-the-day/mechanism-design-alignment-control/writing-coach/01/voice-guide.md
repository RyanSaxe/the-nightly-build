## How this piece should sound

Start with a concrete institutional fact: an evaluation score changes what the system may do. Then introduce the model as a way to make that fact precise. The article should feel like a proof being unpacked for an engineer. Each section should answer the next question raised by the previous one.

Use the focal paper's nouns consistently. A “type” is the hidden bundle of preferences, feasible actions, beliefs, and information. A “report” is what the mechanism is told. A “cap” is the highest action the agent may take. “Capability” should cover both execution and information capability when the sentence needs both. Do not use “alignment” as a synonym for safety; in the focal model it is the bias in the agent's payoff relative to the human's.

Move from the tuple to the sandbagging example in three steps: a capable agent can complete every test a less capable agent can; a lower report can therefore be feasible; and the lower report matters because it may buy a different deployment menu item. Give the reader one numerical mental model, such as action sets `{a}`, `{a, a′}`, and `{a, a′, a″}`, before introducing the formal verification order. The Figure 1 asset should arrive at the point where this asymmetry becomes visible, not as an opener.

Treat equations as reasoning, not ornaments. Introduce every symbol in prose, display the optimal-cap equation once, and immediately translate the square root into average squared bias or root-mean-square bias. Explain why the cap is a control decision and why the equation is a result of the toy environment, not a production recipe. Figure 8 should be read as a comparative technology experiment: the horizontal axis is a constructed frontier position, not a benchmark score.

Prefer short declarative sentences, with an occasional longer sentence when it carries a controlled chain of mechanism, incentive, and action. Use transitions that name the dependency (“That permission changes the incentive,” “The next constraint is physical”) instead of generic signposts. Avoid “the key takeaway,” “this is where,” “not just X but Y,” and atmosphere such as “the stakes are high.” The paper's actual stakes come from the permission rule and the action set.

The conclusion should name the boundary of the result. The theory says what an implementable mechanism must deter under its evidence and preference assumptions. It does not show that a current model has a stable utility function, that a real test induces a clean verification order, or that a multi-agent monitor will meet the paper's benchmark assumptions. Put that distinction in the final paragraph and make the verdict conditional rather than grand.

## Techniques from domain exemplars

### Mitchell Hashimoto, “Ghostty Is Now Non-Profit”

Source: https://mitchellh.com/writing/ghostty-non-profit

- “Ghostty is now fiscally sponsored by Hack Club, a registered 501(c)(3) non-profit.” The opening gives the event and the actors before offering interpretation. Use the same discipline for the paper's headline claim.
- “From a technical perspective, nothing changes for Ghostty.” This is a clean scope boundary. Use a similarly plain sentence when separating the mechanism model from a claim about deployed systems.
- “That structure increases trust, encourages adoption, and creates the conditions for Ghostty to grow into a widely used and impactful piece of open-source infrastructure.” The explanation earns its broader consequence from the legal structure just described. Do not write a broad consequence for the paper until the mechanism has earned it.

### Chris Olah, “Understanding LSTM Networks”

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

- “Humans don’t start their thinking from scratch every second.” The piece begins with an experience that makes the technical problem legible. For the article, begin from the familiar practice of turning evaluation results into deployment decisions.
- “These loops make recurrent neural networks seem kind of mysterious. However, if you think a bit more, it turns out that they aren’t all that different than a normal neural network.” It acknowledges the reader's confusion and then removes it by changing the representation. Use this move for mechanism design: show the menu and the action before naming cyclical monotonicity.
- “The cell state is kind of like a conveyor belt.” A compact physical analogy carries a structural property. One analogy for a cap or a report is enough; do not stack metaphors.

### Lilian Weng, “LLM Powered Autonomous Agents”

Source: https://lilianweng.github.io/posts/2023-06-23-agent/

- “In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components.” The sentence names the central object and its parts before elaborating. Mirror this when defining the type tuple.
- “A complicated task usually involves many steps. An agent needs to know what they are and plan ahead.” Short sentences establish a dependency without jargon. Use the same cadence when introducing report, recommendation, signal, and action.
- “The agent learns to call external APIs for extra information that is missing from the model weights.” The concrete example makes “tool use” testable. When discussing information capability, give a concrete signal or tool-like example before returning to Blackwell experiments.

## Slop and repetition checks

- Delete a sentence whose subject nouns can be replaced by “the result” and whose claim would still fit any AI paper.
- Do not lead with “As AI systems become more capable” or close with “The future of AI depends on...” The focal paper gives a more specific opening and ending.
- Do not copy the recent series pattern of a “What holds up” section or a grid of “what works / what to be careful about.” Let the final section be the argument's boundary.
- Keep the article's one sharp synthesis: evaluation and deployment permissions are a coupled mechanism. Every external source must either establish the motivation or sharpen a limitation; it must not become a second summary.
