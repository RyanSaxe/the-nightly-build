# Commission: paper-of-the-day/generative-adversarial-networks

## Authorized work
Scheduled duty for UTC 2026-08-04 returned `paper-of-the-day` in open mode. This
run publishes exactly one paper article for that series.

## Re-scope note (why not ResNet)
This slot was first commissioned as `deep-residual-learning` (ResNet). The writer
correctly caught that ResNet was already published as `paper-of-the-day/resnet`
on 2026-07-26 — a slug outside the 8-item window the orchestrator first surveyed.
Publishing a second reconstruction of the same paper is an editorial-repetition
failure the slug-based proof would not catch. That attempt is withdrawn and this
GANs commission replaces it. (Also already covered and not to be repeated:
adam-optimizer, attention-is-all-you-need, batch-normalization,
chain-of-thought-prompting, chinchilla, double-descent, emergent-abilities,
grokking, knowledge-distillation, lora, lottery-ticket-hypothesis, resnet,
word2vec.)

## Subject
Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville, Bengio,
"Generative Adversarial Nets" (NeurIPS 2014; arXiv:1406.2661).

## Why this paper, and the angle to examine
The paper's central claim is a clean theoretical result: a generator and a
discriminator playing a minimax game have a global optimum at which the
generator's distribution equals the data distribution, reached when the optimal
discriminator is D*(x) = p_data(x) / (p_data(x) + p_g(x)) and the value function
reduces to a Jensen-Shannon divergence between p_data and p_g. The examine-able
tension is the gap between that theorem and what training actually does: the
proof assumes optimization in function space and an inner loop trained to
optimality, while real GANs are trained by alternating gradient steps in
parameter space and are notorious for mode collapse and instability. The public
record adjudicates this gap: Arjovsky, Chintala & Bottou's "Wasserstein GAN"
(2017) and the companion "Towards Principled Methods for Training GANs" (2017)
argue the JS divergence the original optimum rests on gives near-zero gradient
when the supports of p_data and p_g barely overlap, which is exactly the
early-training regime — a principled diagnosis of the instability, and a proposed
fix (the Earth-Mover / Wasserstein distance). The reconstruction rebuilds the
minimax game and its optimum from the paper's own artifacts, then weighs the
elegant theory against the training reality and the WGAN diagnosis of why they
diverge.

## Required contribution
Not an announcement of a famous result. The reader finishes able to state (a) the
minimax objective and why its optimal discriminator yields a JS divergence, (b)
what the global-optimum theorem does and does not promise (function-space
assumption; inner-loop-to-optimality assumption; the non-saturating heuristic
loss the paper itself substitutes in practice), and (c) how the after-record
(WGAN) locates the instability in the very divergence the optimum is built on.
The "elegant theory, messy practice, and the field's principled diagnosis" shape
— not a debunking (GANs worked and reshaped generative modeling), and not the
recent desk mold of "a famous claim was later overturned."

## Artifacts the reconstruction must use
Per the series prompt, set the math the reconstruction leans on rather than
paraphrasing it: the value function min_G max_D V(D,G), the optimal discriminator
D*, and the reduction to the Jensen-Shannon divergence (Prop. 1 / Thm. 1). Bring
the figures the claim turns on as source assets: Fig. 1 (the schematic of the two
distributions and the discriminator being pushed to 1/2), Algorithm 1 (the
minibatch alternating-SGD training loop), and a results figure (Fig. 2 samples)
if it earns space. The researcher identifies exact figure locations; the writer
captures them with `nb asset` from the arXiv source and sets the equations with
the template's equation furniture.

## Template and policy
- Template: `paper` (fixed). Series `min_sources: 8`.
- Source policy: `{templates: {paper: {min_sources: 8}}}`.
- Production policy (balanced): editor required at high effort, model inherit.
  Actual harness: writing-coach = Sonnet; researcher, writer, editor = Opus.
  Record the actual writer model in nb-meta.

## Boundaries — do not repeat
See the covered-slugs list above. Avoid the "famous claim debunked" mold; the
shape here is theory-vs-practice with a principled after-record. Avoid a
colon-subtitle headline and the comma-triad dek; check recent paper-of-the-day
deks before settling.

## Neighbors this edition
Same run publishes: current-events (US news), tech-news (the day's AI/tech news —
keep current model/lab news there, not here), unbiased (Iran war-powers),
parenting-research (infant vitamin D), word-of-the-day (apophenia). This piece is
the foundational reconstruction of the 2014 paper and its after-record.
