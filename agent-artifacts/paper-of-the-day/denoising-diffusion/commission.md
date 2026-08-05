# Commission: paper-of-the-day/denoising-diffusion

## Authorized work
Scheduled duty for UTC 2026-08-05 returned `paper-of-the-day` (open section,
`paper` template). Publish exactly one paper article this run. Slug:
`denoising-diffusion`.

## The paper
**Denoising Diffusion Probabilistic Models**, Jonathan Ho, Ajay Jain, Pieter
Abbeel, NeurIPS 2020 (arXiv:2006.11239). Chosen because rebuilding its central
claim clarifies an active technical problem the reader cares about: it is the
paper that made diffusion models work as high-quality generative models and set
the training objective the whole subsequent wave (Stable Diffusion, Imagen, DALL-E
2's prior, and later samplers/guidance work) inherited. It has an unusually rich
public record after publication — improved/accelerated samplers (DDIM),
classifier and classifier-free guidance, latent diffusion, score-based unification
(Song et al.), and serious later scrutiny — which lets the article weigh the
claim against what happened next. It is squarely in ML/AI.

## Required contribution (what the reconstruction must do)
- Rebuild the argument with the paper's OWN artifacts, not a description of them.
  The `paper` template opens with the abstract card (title, authors, venue, link,
  abstract verbatim). Then reconstruct in the order that teaches best.
- **Set the math the reconstruction leans on, do not paraphrase it.** At minimum:
  the fixed forward (noising) process and its closed-form marginal q(x_t | x_0)
  with the alpha-bar reparameterization; the reverse parameterization; and the
  key move that made it work — the simplification of the variational bound to the
  **noise-prediction (epsilon) objective L_simple**, and why predicting the added
  noise (with the specific loss weighting dropped) is the paper's decisive
  choice. Use the equation furniture; do not hand-wave the derivation the claim
  turns on.
- **Bring the figures the claim turns on into the article as source assets** (via
  `nb asset`), with captions and prose that say what each one settles — e.g., the
  paper's sample quality figures and the training/sampling algorithm boxes
  (Algorithm 1 / Algorithm 2). A reconstruction that only describes the figures
  underuses the strongest material. Only use a visual the argument actually
  spends.
- Weigh the evidence as a reviewer: what was measured (CIFAR-10 FID/Inception,
  LSUN, CelebA-HQ), on what, and where the claim stops (log-likelihoods vs.
  competing likelihood-based models; sampling cost; the choices left unexplained).
  Place the paper among what it builds on (Sohl-Dickstein et al. 2015; NCSN /
  score matching, Song & Ermon 2019) and what came after. State a verdict on its
  claims before the Sources.

## Sourcing
`min_sources: 8`. The focal paper is the spine and owns its claims. Additional
sources earn space only when they change the interpretation (the 2015 precursor,
score-based work, DDIM, guidance, latent diffusion, a serious critique/replication
or a later survey). Verify every reported number against the paper's own tables.
Confirm every URL resolves (arXiv abs page, not a PDF-fetch endpoint; official
proceedings where relevant).

## Boundaries — do not repeat
- Published paper-of-the-day slugs include: attention-is-all-you-need, adam,
  batch-normalization, chain-of-thought-prompting, chinchilla, double-descent,
  emergent-abilities, GANs, grokking, knowledge-distillation, lora, lottery-
  ticket-hypothesis, resnet, word2vec. Diffusion/DDPM is fresh. Use
  `nb history --structure paper-of-the-day/<a-recent-slug>` for shape/continuity
  only, and break its outline/opener/closer shapes — do not inherit another
  paper article's structure.
- **Non-overlap with tech-news (same run):** tech-news covers current field news;
  this is a 2020-paper reconstruction. Do not turn it into a diffusion news recap.

## Template and policy
- Template: `paper` (fixed).
- Production policy (balanced): editor required at high effort, model inherit.
  Researcher/writer models = capable. Charts only from verified series; source
  assets only from the paper's own figures via `nb asset`.

## Neighbors this edition
Full edition: current-events, tech-news, expert-tools/visidata,
investing/free-cash-flow, opinion/mandate-frontier-ai-disclosure,
paper-of-the-day (this), word-of-the-day/ultracrepidarian.
