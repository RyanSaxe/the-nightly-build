# Commission: paper-of-the-day/generative-adversarial-networks

## Assignment
Report on one paper: **Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing
Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville, Yoshua Bengio,
"Generative Adversarial Nets," NIPS 2014** (arXiv:1406.2661). Rebuild its central
claim, show how the claim is earned, and mark where the claim stops.

## Why this paper
GANs proposed learning a generative model as a two-player minimax game: a
generator maps noise to samples, a discriminator learns to tell real from
generated, and at the game's optimum the generator's distribution equals the
data distribution. The paper carries a clean theoretical result and a practice
that never behaved as cleanly. The public record after it is rich: the loss's
vanishing-gradient problem, mode collapse, training instability, the Wasserstein
GAN reframing (Arjovsky, Chintala, Bottou, 2017) that diagnosed the divergence
being minimized, and the large-scale "Are GANs Created Equal?" study (Lucic,
Kurach, Michalski, Gelly, Bousquet, 2018) that found no clearly superior variant
under a fair compute budget. And diffusion models later displaced GANs for much
of image generation. That gap between an elegant proof and an ungovernable game
is the article's subject.

## Angle / contribution required
Rebuild the minimax objective and the paper's two theoretical results in the
piece's own words: (1) for a fixed generator, the optimal discriminator is
D*(x) = p_data / (p_data + p_g); (2) substituting it makes the generator's
objective a Jensen-Shannon divergence between p_g and p_data, minimized (global
optimum) exactly when p_g = p_data. Then weigh the claim against what happened
next: the non-saturating vs minimax generator loss and the vanishing gradient
when the discriminator is confident; mode collapse; instability; what WGAN
changed about the divergence and why; and what the Lucic et al. study found about
claimed progress. The article's own work is the argument connecting the proof's
assumptions (an optimal discriminator, sufficient capacity, the value function
actually optimized) to the specific ways practice departed from them. Land a
reviewer's verdict: what the paper established, what it only assumed, and what
the field had to add.

## Reader / mode / template
House reader (ML-engineering background). Mode open; template `paper` (bands
1800-3400 words, 2-8 flex sections). The abstract anchor puts the paper's link
and its own words up front; flex sections carry the reconstruction and land the
verdict. Subject is the paper, never the experience of reading about it. Use
furniture where evidence has a shape prose would hide (an equation for the value
function and the D* result; a small table or timeline for the follow-on record;
a chart only from verified numbers).

## Source obligations
- Template floor: **minimum 8 sources**; per-section citation; carry honest
  primary/secondary kinds into `data-nb-kind`.
- **Primary**: the GAN paper itself (arXiv/NIPS) for every claim about what it
  says and proves; WGAN (arXiv:1701.07875) and Lucic et al. (arXiv:1711.10337)
  as primaries for their own results. Read the actual math and the actual
  experimental tables, not summaries.
- **Secondary**: independent explanations/critiques for context only; verify any
  figure against the owning primary.
- Every URL resolves; verify every equation, author name/affiliation, and figure
  exactly. Steelman defenses of the original formulation before weighing them.

## Relevant prior coverage (do not repeat subject or shape)
Paper desk recently: attention, resnet, adam, batchnorm, lottery-ticket,
chinchilla, lora, chain-of-thought, knowledge-distillation, emergent-abilities,
grokking. GANs (generative modeling, adversarial training) does not overlap these
subjects. Avoid the recent run's dominant shape (training-dynamics/scaling). The
recurring house move "the paper proved X for a setting practice never occupied"
(cf. adam, batchnorm) is apt here but must be argued freshly, not stamped.

## Structures not to inherit
Recent paper pieces open on a one-line paradox headline and a "N follow-ups
disagree" dek. Find this piece's own opener and dek. Do not close on a reading
list.

## Neighboring articles tonight
tech-news brief (do NOT let it cover this paper), word-of-the-day, current-events,
investing, parenting. This is the only in-depth ML paper tonight.

## Output paths
- Article: `.nb-work/paper-of-the-day/generative-adversarial-networks/library/paper-of-the-day/generative-adversarial-networks.html`
- Artifacts under `agent-artifacts/paper-of-the-day/generative-adversarial-networks/`.

## Harness / model (balanced profile)
harness `claude-code`; writing-coach `claude-sonnet-5`/low; researcher
`claude-sonnet-5`/high; writer `claude-sonnet-5`/medium (record in nb-meta);
editor `claude-opus-4-8` (inherit)/high, required.
