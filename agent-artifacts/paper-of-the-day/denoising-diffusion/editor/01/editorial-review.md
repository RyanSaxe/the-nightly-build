# Editorial review: paper-of-the-day/denoising-diffusion (editor/01)

## Skeptic

Thesis: DDPM's competitive image quality came not from a new model but from one
training change to a five-year-old framework — regress on the added noise, then
discard the derivation's own step-dependent weight — and that change is what the
whole later field inherited. The claims it stands on:

1. The forward/reverse diffusion framework predates DDPM (Sohl-Dickstein 2015),
   and the score-matching/Langevin half of the "novel connection" is NCSN 2019;
   DDPM's own contribution is the epsilon-parameterization and the unweighted
   objective.
2. The derivation is set correctly and each move is forced by a named
   constraint: the closed-form marginal (tractability of training), the
   posterior conditioned on x0 (tractability of the KL term), the fixed reverse
   variance (leaves only the mean to match), and dropping the weight (an
   empirical choice, not an identity).
3. The numbers are the paper's own: CIFAR-10 FID 3.17 / IS 9.46, the ablation
   13.51 vs 3.17, NLL <=3.75 (L_simple) vs <=3.70 (fixed-Sigma variant), LSUN
   Church 7.89 / Bedroom 4.90, Score-SDE 2.20.
4. The honest verdict is a split decision: state-of-the-art samples, but a
   log-likelihood beaten by the paper's own variant and a 1000-step sampling
   cost the paper never frames as a limitation.

I tried to break each. The math is **set verbatim, not paraphrased**, and every
displayed equation matches the evidence record term for term: forward process
(Eq. 2), closed-form marginal with the alpha-bar reparameterization (Eq. 4),
reverse parameterization (Eq. 1), the L_T / L_{t-1} / L_0 bound (Eq. 5), the
tractable posterior with beta-tilde (Eq. 6-7), mean-matching (Eq. 8), the
epsilon reparameterization of the mean (Eq. 11), the weighted noise term
(Eq. 12), and L_simple (Eq. 14) with the coefficient explicitly set to one. Each
transition carries its forcing constraint in a sentence of its own; the collapse
to L_simple is correctly presented as a reported empirical decision ("This is
not a derivation. It is a choice, and the paper defends it with a result rather
than an identity"), which is exactly the voice guide's load-bearing move. I
could not retire a claim.

Numbers: every figure checks against the paper's own Table 1, Table 2, and the
Figure 3/4 captions. The 25.32 attributed to "the score-based field" is NCSN's
Table 1 FID; NCSN's IS 8.87 is its own abstract number. The after-record numbers
(DDIM 10-50x, Score-SDE 2.20, Improved DDPM order-of-magnitude fewer passes) are
each carried from the source that owns them, not a restatement.

Sourcing: all nine hrefs are arXiv `/abs/` pages (no PDF endpoints), and I
opened every one — each resolves to the exact title and author list the Sources
list prints (DDPM, Sohl-Dickstein et al., Song & Ermon, DDIM, Improved DDPM,
Score-SDE, Dhariwal & Nichol, Ho & Salimans, Rombach et al.). Every source is
`data-nb-kind="primary"`, which is correct here: each after-record paper is
cited for its own contribution (what that follow-up did), never as outside
commentary on DDPM, so none is functioning as a secondary.

Display text: headline states a defended causal claim in the piece's own
opposition (noise vs image); dek adds actors, the 3.17 figure, the year, the
mechanism, and the consequence without restating the headline; nb-meta `dek` is
identical to the rendered dekline; no colon-subtitle; the dek is a two-clause
compound, not the banned comma-triad. Subheads are argument steps in the paper's
nouns. Nothing false in a label.

## Cut

The prose is disciplined and earns its length; this is a reconstruction, and the
equation furniture is load-bearing, not padding. One clean cut: in the verdict I
removed "and stating it that way is not a demotion" — the article grading its own
framing choice, and a redundant "not X" contrast. The sentence now reads "That
is a training recipe, not a model family. The recipe is what the field kept."

Worst tell, and a pattern: the "not X" / "X, not Y" contrast is reached for
repeatedly — "the noise, not the image"; "not a derivation... a choice"; "not a
matter of taste"; "a setting, not a cost"; "a floor, not a ceiling"; "a training
recipe, not a model family." Each individual use is earned (it corrects a real,
named view, or states one of the piece's genuine oppositions), so I did not
mass-cut defensible contrasts and regress the voice. But the frequency sits over
the standard's one-or-two ceiling and is worth the writer's eye on a future
pass. I cut only the one that was also self-grading.

Heading cadence: two of six headings share the comma-and shape the headline spec
flags as stamped — "Strong samples, a likelihood that lost, and a cost left
unnamed" and "A training recipe, not a new model, and the recipe was right."
Sharp lines, but the repeated cadence is the tell the spec names. Varying one is
a small writer fix (below).

The five remaining W-SENTENCE-DENSITY warnings are **justified furniture, not
prose run-ons**. I read each: all five are verbatim display-equation TeX inside
`nb-math-eq` divs (Eq. 4, Eq. 5, Eq. 6-7, Eq. 12, Eq. 14) that the density
heuristic scores as one long "sentence" because the div is not a skip tag.
Splitting them would corrupt the math. No genuine prose run-on hides among them;
the one real 55-word sentence flagged in the prior build was already split.

## Reader

Read straight through, the piece gives what the paper's own text does not hand
you: it reorders the derivation around a single fork the paper treats as routine
(predict the mean vs predict the noise) and shows the headline result is the
consequence of taking the noise branch and then *throwing away* the weight the
same derivation produced — with the paper's own ablation (13.51 vs 3.17), not
algebra, as the defense. That is the original-work sentence in the handoff, and
the article delivers it. The prose sits with the voice-guide exemplars (Weng's
"state a constraint, then produce the reparameterization that removes it";
Song's figure-as-failure; the empirical-decision honesty) rather than a median
summary: it names which steps are proof and which are a choice the authors made
and defended with a result. The verdict earns its split — state-of-the-art
samples set against a non-competitive likelihood and an unquestioned 1000-step
sampler — and places the paper against both its lineage (2015/2019) and the
after-record that closed its two soft spots.

## Visual evidence

Asset-1 (Algorithm 1 Training / Algorithm 2 Sampling boxes): verified against
the evidence line by line — the training gradient step on
`||eps - eps_theta(sqrt(alpha-bar_t) x0 + sqrt(1-alpha-bar_t) eps, t)||^2` and
the full sampling update including the `+ sigma_t z` term and the `z=0 at t=1`
condition are all present and legible. Crop is clean, no clutter, both boxes
retained. Caption is factual and cited to Sec. 3.2, Algorithms 1-2. The caption's
"cheap to train... expensive to sample" is the specific claim the paired boxes
settle, which the voice guide's figure-as-claim license permits. Fine as is.

Asset-2 (LSUN Church grid, FID 7.89): matches the paper's Figure 3; FID cited
in-caption as the paper prints it. **Watermark ruling:** the top-left cell
carries a clearly legible "shutterstock" mark and the string
"www.shutterstock.com 193883335." This is the well-known DDPM artifact — the
LSUN samples reproduce a training-set watermark — but the caption is silent on
it and labels the grid "Generated LSUN Church samples." That silence is a real
honesty gap, not acceptable-unremarked: a reader who spots a stock-photo
watermark in images labeled "generated" either reads it as an error or is left
with an unaddressed training-data-memorization question, and either outcome
undercuts the asset's evidentiary job. The fix is minimal and the caption must
stay a factual label, so this is a small writer task (below), not an asset
recrop — the watermark is in the paper's own figure and cannot be cropped out.

## Edits

- Verdict: cut "and stating it that way is not a demotion" (self-grading of the
  article's own framing; also a redundant "not X" contrast).
- Ran `nb stamp`: words 2720 -> 2711, reading_minutes 12, sources 9.

## Required work

- **writer** — Add a brief factual acknowledgment that the LSUN Church grid
  reproduces a Shutterstock watermark present in the training data (a short
  factual note in the asset-2 caption, keeping the caption a factual label; the
  memorization point itself, if made, belongs in the what-it-measured prose).
  Do not attempt to recrop or edit the asset — the watermark is in the paper's
  Figure 3. This is the one publication-blocking item.
- **writer** (minor, same pass) — Vary the cadence of one of the two comma-and
  headings ("Strong samples, a likelihood that lost, and a cost left unnamed" /
  "A training recipe, not a new model, and the recipe was right") so the shape
  does not repeat. Optional but worth doing while the file is open: thin the
  recurring "not X" contrast where a use is not load-bearing.

No researcher work: the claim set, equations, and numbers are fully supported by
the evidence record and need nothing new. No orientation/commission gap.

## Decision

revise — the reconstruction, math, numbers, sourcing, and verdict all hold, but
the asset-2 LSUN grid shows a legible Shutterstock training-set watermark that
the caption leaves unremarked, and that honesty gap is a required writer fix
before publication.
</content>
</invoke>
