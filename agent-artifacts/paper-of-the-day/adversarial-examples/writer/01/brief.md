# writer brief: paper-of-the-day/adversarial-examples (01)

Inputs (paths relative to the workspace root `.nb-work/paper-of-the-day/adversarial-examples/`):
- `agent-artifacts/paper-of-the-day/adversarial-examples/editorial-direction.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/writing-coach/01/voice-guide.md`
- `agent-artifacts/paper-of-the-day/adversarial-examples/researcher/01/evidence.md` — the reconstruction kit and the weighed public record
- `agent-artifacts/paper-of-the-day/adversarial-examples/commission.md` — what to rebuild, what to weigh, the habits to break
- `library/paper-of-the-day/adversarial-examples.html` — the initialized paper article to edit in place
- `.nb-context/` — effective template contract (paper) and furniture catalogs

Output: `agent-artifacts/paper-of-the-day/adversarial-examples/writer/01/draft-handoff.md`

Proof (from repo root, workspace-prefixed; iterate with `--no-check-links`, links on until BLOCK: 0):
`./nb check .nb-work/paper-of-the-day/adversarial-examples/library/paper-of-the-day/adversarial-examples.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/980fb41b-a65b-5e72-a2d0-4a92f8c0f978/scratchpad/library-checkout`
Run `./nb stamp` on that path before the final check.

Evidence/reconstruction cautions to honor (from the researcher):
- Set the math correctly: the perturbation is `eta = epsilon * sign(grad_x J)` (each component +/- epsilon, saturating the max-norm bound), and the linear-explanation growth term is `epsilon * m * n`. The paper prints `eta = sign(w)` in one place; do not copy that and drop the epsilon. Set the equations with the equation furniture, do not paraphrase them.
- Figure 1 (panda 57.7% -> "gibbon" 99.3%, middle sign panel at epsilon=0.007) is the source asset. Capture it with `./nb asset` from the paper, caption it factually (imperceptible perturbation, high-confidence wrong label), and spend what it shows. Never use an external image URL.
- Weigh honestly. The linear view got real things right (perturbations cheap, gradient-aligned, transferable; FGSM + adversarial training became the field's starting point). It was incomplete: Ilyas 2019 reframes the cause as non-robust-but-predictive features in the data; Tsipras 2019 shows a robustness-accuracy tension against the paper's regularizer optimism; Madry 2018 / Athalye 2018 / Carlini & Wagner 2017 show single-step FGSM training was weak and most later defenses illusory. The paper's own numbers already qualify the harnessing claim: adversarial training only cut error to 17.9%, still 81.4% confident when wrong. Ground the reframing in the paper itself, not as an outside verdict.
- Represent the prior view accurately: Szegedy 2013 hypothesized "low-probability pockets" and discontinuity, not simply "nonlinearity." The nonlinearity framing is partly Goodfellow's construction; the pockets-vs-contiguous-regions disagreement is a real, citable clash. Do not repeat a strawman.
- "Where robustness stands" is anchored to the dated Wang et al. 2023 figure (70.69%), not a live leaderboard; present it as a dated checkpoint.

nb-meta: set `date` 2026-08-16, `harness` `claude-code-routine`, `model` `claude-opus`, `tags` []. Keep nb-meta `dek` identical to the rendered dekline. The abstract card carries the paper's link and its own words up front, per the paper template.

This round's focus (recent paper-desk shapes to break, per the commission):
- The desk's recurring headline/dek mold is "the paper's own proof or measurement leaves out its claim." This paper's story is a proposed explanation partly right and later reframed; do not force it into that mold.
- The recent GAN piece was built as "theorem versus Algorithm 1"; do not mirror its structure. Close on the piece's own weighing, not a stamped "what the paper is right about" heading.
