# Editorial review: paper-of-the-day/mixture-of-experts (editor/01)

## Skeptic

The thesis: the 2017 sparsely-gated MoE layer's core idea, that a sparse
trainable gate buys capacity at nearly fixed per-example compute, carried into
today's frontier models, while almost all of its specific machinery (routing to
more than one expert, the two coefficient-of-variation balancing losses, and the
mixed-parallelism batch fix) was replaced by later work. The headline commits to
exactly that and the piece defends it.

The claims it stands on, and how each held:

- The gate math. I checked the softmax gate, the noisy top-k gate, KeepTopK, the
  noise term H(x)_i, the importance loss, and the load loss against the evidence
  record's readings of Eqs. 2-7 and Appendix A. Each equation as typeset matches
  the paper's own form, including the verbatim H(x)_i = (x·W_g)_i +
  StandardNormal()·Softplus((x·W_noise)_i). The prose reads the algebra rather
  than paraphrasing it: the noise term's two jobs (breaking the top-k lock, and
  making the example count differentiable) and the two-losses distinction
  (importance equalizes summed gate weight, load equalizes example counts) are
  set out as the mechanism, not gestured at. The furniture rule holds: only the
  noise equation uses the annotated colored-legend form, one per article.
- The capacity claim and its scope. The controlled 1B-word comparison is correct
  and, importantly, not conflated. The fastest model (8.9 M ops, 34.1 ppl) beats
  the best published result (151 M ops, 34.7 ppl) at about six percent of that
  baseline's compute; held near the baseline's budget (142.7 M ops) the sparse
  model reaches 28.0. The abstract's ">1000x" is correctly reframed as a capacity
  ceiling, with the controlled parameter gap stated as roughly thirtyfold (4.3 B
  excluding embeddings against 151 M, which computes to about 28x). The
  131,072-expert, 137 B-parameter model is kept on its separate 100B-word corpus
  at 28.9-29.2 perplexity, not merged into the 1B-word rows. The dek's "at six
  percent of its compute" attaches to the model that actually achieves it (34.1
  beating 34.7), so it does not imply 28.0 came free.
- The follow-on verdict. Switch top-1 overturning the k>1 premise (1.571 T
  params, 4x speedup), the collapse of the two losses to one (Switch, GShard),
  expert-choice removing the loss by construction (>2x convergence), loss-free
  balancing calling the loss harmful, and DeepSeek-V3 (671 B/37 B,
  auxiliary-loss-free) all match their owning primaries. DeepSeek-V3 is held to
  its abstract's claims and asserts nothing beyond. The expert-choice
  autoregressive-decoding limitation, flagged unverified in the record, is
  correctly absent.

Display text checked descriptor by descriptor: author list and order, venue,
arXiv id, the Jacobs et al. 1991 attribution (Hinton an author of both), and
Bengio, Léonard and Courville 2013 all match the record. Headline, dek, and every
subhead make a claim about the world; none grades the article's own selection.

Citations: I opened all ten source hrefs as printed. Every arXiv id resolves and
its title matches the paper it is cited as (verified 1701.06538, 1308.3432,
2101.03961, 2006.16668, 2202.09368, 2408.15664, 2412.19437, 2401.06066). The
ar5iv full-text render resolves. The MIT Press page for Jacobs et al. returns 403
to automated fetch; it is gated, not dead, and is the article's own canonical
page, matching the record's note. Every data-nb-kind is "primary" and each is the
document that owns its claim. Citation order is first-appearance (s1 through s10
in body order).

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

Both source assets read honestly. Figure 1's crop keeps the gating network, the
full expert row with the unselected experts left inactive, and the weighted sum
back into the sequence. Figure 2 keeps both axis labels, their units, the
baseline points, and is log-scaled on both axes as the caption states. No recrop
needed.

Four sentences failed the test and were cut or trimmed:

- The orientation's closing sentence began "What follows rebuilds that gate..."
  which is the self-reference `spec/slop.md` names outright ("what follows"). It
  was a structural roadmap carrying no fact; deleted. The section now ends on the
  concrete "The rest of the experts, for that input, do no work."
- In the batch-cost section, "This is worth marking, because it is not the route
  the field later took" opened on a signpost about the article's own emphasis.
  Trimmed to its factual content, "It is not the route the field later took."
- In the follow-on section, "What happened to the parts around it is the more
  useful reading" was a signpost that also self-graded which analysis matters;
  deleted, and the argument moves straight into the overturned premise.
- The verdict's final sentence, "A reader who knew MoE only as the thing frontier
  models use to scale can now see which half of the 2017 design they are actually
  running," was lightly rewritten from the commission's required-contribution
  ("A reader who knows modern MoE only as 'the thing frontier models use to
  scale'") and asserted the article had fulfilled its assignment. This is prompt
  leakage of the kind the cut read targets; deleted. Its s5/s8 citations were
  redistributed onto the three replacement claims they support (top-1: s5 Sec.
  2.1; one loss or bias: s5 Sec. 2.2 and s8; fixed capacity: s6 Sec. 2.2), so the
  verdict stays sourced and now closes on "Fixed capacity with token dropping
  replaced the parallelism-and-convolution batch fix."

No repeated formula in the survivors. Section headings are varied in
construction, each a real step in the piece's own nouns, and none is stamped to
the "The X does Y" declarative the pattern notes flag. The dek is descriptive of
the original result and does not fall into the corrective-finding mold, the
semicolon reversal, the suspended question, or the comma triad. The close, after
the leaked sentence was removed, lands on the concrete three-part replacement the
argument built rather than the "naming a section or a cheaper alternative" mold
of recent reconstructions. Furniture earns its place: the annotated noise
equation is the one the gate turns on, the holds-up grid and Verdict note carry
the weighed judgment, the table holds the three compute-matched rows, and the two
figures are read where the prose spends them. The edge sentences that survive
(for example "A dense network pays for every parameter on every example" and the
distinction "Equal importance is not the same as equal work," which corrects a
named misconception) each carry a fact or a reasoning step. No borrowed phrasing
from the voice-guide exemplars. Grammar and punctuation are clean.

## Reader

Read straight through as the declared reader, what I have that the sources alone
would not give me: the 2017 gate and its two balancing losses rebuilt from the
equations with the noise term's double role made explicit, the capacity claim cut
down to its honest controlled size (about thirtyfold, not the abstract's
thousandfold ceiling), and a clean separation of what survived from what was
replaced across the seven-year follow-on record. The draft-handoff's
original-work sentence claims exactly this separation as a synthesis the evidence
record supplies only as scattered facts, and the article performs it in the
holds-up grid and verdict. Both answers survive; the piece does not restate its
sources. The prose sits closer to the voice-guide exemplars than a median
summary: it poses design questions and answers them with the algebra, gives each
balancing loss its own reason, states what breaks before naming the fix, attaches
numbers directly to the claims they support, and holds an honest non-resolving
verdict on balancing. The headline reads true as the largest claim.

## Edits

- Cut the self-referential roadmap sentence ("What follows rebuilds that
  gate...") closing the orientation section.
- Trimmed "This is worth marking, because it is not the route the field later
  took" to "It is not the route the field later took" in the batch-cost section.
- Cut the self-grading signpost "What happened to the parts around it is the more
  useful reading" in the follow-on section.
- Cut the prompt-leaked, assignment-fulfilling final sentence of the Verdict
  note, and redistributed its s5 and s8 citations across the three replacement
  claims (adding s6 Sec. 2.2 on the batch-fix claim) so the verdict stays sourced
  and closes on the batch-fix replacement.

## Required work

None. No evidence gap, no chart or asset fix, no math error, no broken claim to
route. The orchestrator will re-stamp the counts and re-prove before the PR.

## Decision

approve — the reconstruction sets the math correctly, scopes the capacity claim
honestly, and weighs the follow-on record without overreach; the four cuts
removed self-reference, a signpost, and prompt leakage, and nothing publication-
blocking remains.
