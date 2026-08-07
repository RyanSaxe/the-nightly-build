# Voice guide: paper-of-the-day/bert (01)

Write as a reviewer reconstructing an empirical pretraining paper for an
engineer who can read a loss function unaided. Keep the house register (calm,
first-principles, structure carrying the persuasion) but shift the job from
expositor to adjudicator: the sentences do not only teach the recipe, they put
each of the paper's claims on trial and report the verdict the evidence
supports. Hand the reader the training objective as notation and trust them to
hold it; spend the rest of the paragraph on what the notation forces. Treat
every reported comparison as a hypothesis under test, never as a settled fact
restated. Let confidence track the evidence: press the claim the record
sustained, retire the one it did not, and mark the limit that was real without
softening it into balance.

Two failures live closest to this material. The first is the equation as
ornament: notation set down, then re-read in words, teaching nothing the symbols
did not already say. The second is the table as decoration: a number quoted, an
adjective attached, no argument made about what the number does and does not
establish. Both are cut here by the licenses below, which say what a single such
sentence must accomplish to stay.

## Licenses

form: an objective set as notation, then operated on
move: the exemplars make an equation the middle term of a paragraph — prose
  names the need, the notation states it exactly, and the next sentence spends a
  consequence the notation forces (Rush hands each equation to the mechanism it
  becomes; Weng re-parameterizes a loss the moment its naive form fails). The
  form deploys once per turn in the reconstruction, where a design choice hinges
  on what the objective can and cannot condition on.
bar:  the sentence after the equation must state something the equation compels
  and the argument then uses — a factorization it forbids, a token it leaves
  unsupervised — not a prose paraphrase of its symbols. If the paragraph reads
  the same with the equation deleted, the equation was ornament and the sentence
  is cut.

form: a reported comparison read as a claim under test
move: Ruder refuses the headline number and asks what causal story sits beneath
  it, what confound a competing account would predict, and what the comparison
  therefore does and does not establish. He stratifies a headline result from a
  secondary claim and weighs each at its own confidence. The form turns a table
  into testimony by naming the alternative hypothesis the table is being asked to
  distinguish.
bar:  a use must name the competing account in play (a longer-trained baseline,
  a removed auxiliary term, a feature-based rather than fine-tuned setup) and
  point to the specific row or figure that separates it from the paper's reading.
  A number carrying only an evaluative adjective, or a contrast whose losing side
  no source actually holds, fails the bar and is cut.

form: the counterfactual read of a paper's own table against its own claim
move: the strongest empirical writing lets a result cross-examine the paper that
  reported it — a margin already narrow in the authors' ablation is read forward
  as the later refutation waiting to happen. This is not the banned hypothetical
  reader; it is a stated alternative hypothesis measured against a printed row.
bar:  the counterfactual must be one a cited source actually advanced, and the
  row read against it must be the paper's own reported evidence. The move earns
  its place only when the paper's number and the later finding point the same
  way; absent that alignment, report the two results plainly and drop the framing.

form: a design decision narrated through its named alternatives
move: Weng makes a choice feel earned rather than arbitrary by listing the
  options actually on the table and reporting, with the paper's stated reason,
  why the losing ones lose (the split of a masking scheme, the sharing pattern of
  a parameter budget). The reader watches the decision space, then the decision.
bar:  every alternative named must be one the paper weighed or a real failure
  mode it guarded against, and the resolution must carry the paper's own reason,
  cited. An enumeration that exists to look thorough, or whose alternatives were
  never live, is padding and comes out.

## Sebastian Ruder, "NLP's ImageNet moment has arrived"
Source: https://www.ruder.io/nlp-imagenet/
Craft:
- cadence: a punchy claim followed at once by the sentence that complicates it,
  so drive never tips into overclaim; short declaratives set the thesis, longer
  subordinate clauses attach the limits.
- argument: the headings alone reconstruct the reasoning — precedent, why the
  analogy holds, candidates tested, the strongest defended, the gap admitted,
  the synthesis. A skimmer of headings leaves with the whole case.
- evidence: a consistent gain across benchmarks is read as one variable doing the
  work, and the limit ("only a proxy to true language understanding") is featured
  as a real bound, not buried as a hedge.
- stance: modal precision — "very likely" where benchmarks cluster, "much more
  research is necessary" where theory lags. Confidence is rationed to evidence
  density; no "proves."
- notice: he notices that independent teams with divergent architectures reached
  the same gains, and reads the convergence itself as the evidence.
- diction: technical term set beside a concrete gloss ("anaphora" clarified as
  coreference); adjectives kept light so the numbers carry the weight.
- reader: assumes the field's practitioner; explains the analogy, not the
  machinery.
- the important move the axes missed: he extracts a field-level claim from a
  pattern of results without letting any one paper carry more than it can, by
  making the shared conclusion of several independent findings the unit of proof.

## Sebastian Ruder, "Challenges and Opportunities in NLP Benchmarking"
Source: https://www.ruder.io/nlp-benchmarking/
Craft:
- cadence: short negations reset an inflated claim ("Far from it") before a
  specific, longer sentence supplies the mechanism; a question answered by a
  declarative makes the answer feel earned rather than asserted.
- argument: separates the empirical fact (a benchmark saturated fast) from the
  interpretation (capability is solved), accepting the first while rejecting the
  second.
- evidence: demands the causal story under a number — annotation artifacts that
  let a model score high on the hypothesis alone — so a headline result is shown
  to measure less than it appears to.
- stance: skeptical but fair; he steelmans the original choice (a coarse metric
  was right for its decade) and aims the critique at the failure to update when
  conditions changed.
- notice: a lone statistic (how few papers use anything but one metric) is turned
  into evidence of a field-wide habit, not a remark about one paper.
- diction: verbs of failure carry the judgment ("fall short", "not able to
  identify") while the concession stays explicit, so the critique reads exact
  rather than sour.
- reader: assumes someone who trusts benchmarks by default and shows them where
  the trust is unearned.
- the important move the axes missed: he treats a benchmark number as a claim
  with a confound to rule out, which is the exact posture this article needs for
  a re-examination that overturned an earlier result.

## Lilian Weng, "Generalized Language Models"
Source: https://lilianweng.github.io/posts/2019-01-31-lm/
Craft:
- cadence: sentences shorten as density rises; a dense derivation is broken by a
  short fragment naming the next idea before the long sentence that unpacks it.
- argument: contrastive scaffolding — each model opens by naming what its
  predecessor could not do, so a new objective arrives as a response to a stated
  limitation rather than as the next item in a list.
- evidence: design decisions are narrated as problem-then-solution inside the
  derivation itself; a masking split appears with the failure it prevents, so the
  choice reads as forced by a constraint.
- stance: guide to a capable reader — assumes mathematical literacy, not domain
  expertise, and never apologizes for density.
- notice: she notices the alternatives a paper rejected and walks the decision
  space (which parameters to share, whether to train a generator adversarially),
  reporting each negative result with its reason.
- diction: verbs over nominalizations ("employed tricks", not "the employment
  of"); jargon defined at the point of first use, then reused exactly.
- reader: offers footholds — a table comparing two models, a link, a parenthetical
  scope note — without slowing the main line.
- the important move the axes missed: she re-parameterizes a loss the instant its
  naive form breaks, letting the mathematics state the problem the next design
  step solves — the objective operated on, not displayed.

## Alexander Rush, "The Annotated Transformer"
Source: https://blog.rush-nlp.com/the-annotated-transformer.html
Craft:
- cadence: terse definitions land fast, then expand into the mechanism they name,
  so the reader feels a compression and its release.
- argument: a stepping motion — prose states a need, notation formalizes it, the
  implementation instantiates it — with no backflip into pure paraphrase between
  the steps.
- evidence: the equation is the blueprint the following block executes, so the
  claim "this is how it works" is discharged by showing it work, not by asserting
  it.
- stance: collaborative rather than didactic; assumes linear algebra and basic
  deep learning and does not re-explain them.
- notice: notices where an equation must become a concrete operation and hands it
  straight to that operation, refusing to let notation sit inert.
- diction: names a thing once with precision and reuses the exact name, trusting
  the reader to carry the shorthand — cognitive economy over restatement.
- reader: an implementer who wants the formal object connected to what it does,
  not a summary of the paper's prose.
- the important move the axes missed: notation is never the endpoint; it is the
  middle term between a stated need and a demonstrated consequence, which is the
  discipline that keeps a reconstruction from decaying into a summary.
