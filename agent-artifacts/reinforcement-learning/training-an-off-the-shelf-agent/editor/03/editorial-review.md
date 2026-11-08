# Editorial review: reinforcement-learning/training-an-off-the-shelf-agent (editor/03)

## Correct

This round answers the second and last reader check. Under the template's rule I answered it by cutting or correcting text. I started no experiment and changed no listing.

The thesis has not changed. PPO plays its training episodes with sampled moves, so its training curve scores sampling. A trained agent is judged by its frozen greedy policy, played in a separate evaluation environment, over several seeds, beside baselines scored the same way. Three claims sit under it. First, sampled moves are worth less than greedy moves in every seed (Table 1, exact). Second, ten evaluation episodes cannot sort the seeds, and 10,000 still put two of them in the wrong order. Third, one arrow accounts for each short seed (the removal test in seeds.py). All three still hold against the printed output.

The reader's restatement matches the main-idea sentence that the commission confirmed after editor/02. It covers the sampled policy against the greedy one, the exact solve, the noise, the separate environment, seeds, baselines and the episode count. There is no mismatch, so the main idea's wording does not change.

Two places needed a correctness decision.

Place 1, "target policy". The term was wrong. The Q-learning lesson defines the target policy as the policy an agent learns about, and calls a method on-policy when that is the policy that makes its moves. SB3 files PPO as on-policy: `class PPO(OnPolicyAlgorithm)` (ppo.py L18), and on_policy_algorithm.py L23 reads "The base for On-Policy algorithms (ex: A2C/PPO)". I read these in the v2.9.2 clone at /tmp/claude-0/rl-editor/sb3, commit 0cdcd200, the commit the evidence record names. In the course's terms, then, PPO's target policy is the stochastic sampling policy, which is Table 1's middle column. The page had used the term for the greedy column. Henderson et al. (p. 6) write "a target policy" in the looser sense of whichever policy is evaluated. The fix was to remove the term and its link to sarsa-and-q-learning#off-policy, and to paraphrase Henderson as "scores the policy the agent has learned". I did not add a sentence calling PPO on-policy. The main idea does not need that sentence, and it leans toward explaining the algorithm, which the commission rules out. The reader also asked why the greedy policy is the one put to use. That answer comes from a source already cited. SB3's guide, in the same paragraph as the curve warning (s10, after the second Note box), advises trying deterministic=True for stochastic policies such as PPO, which "frequently leads to better performance". I reread that paragraph in the saved page /tmp/claude-0/rl-editor/pages/rl_tips.html. The evidence record has the same quote.

Place 4, the 10,000-episode figure. The reader was right. The paragraph sets up "an environment of your own, with no exact solve", where the scripted baseline is played too. By the paragraph's own clause, both means are then estimated and the count doubles. The 10,000 fits only SlipperyGrid, where the hand-drawn value is exact. The page now says that: on SlipperyGrid the hand-drawn value is exact, so 0.25 needs (3 × 8.5 / 0.25)² ≈ 10,400 episodes, and were the hand-drawn policy played too, each would need about 20,000. That is 2 × 10,404. With lesson 8's hand-drawn sd of 8.79 in place of 8.5 for that policy, it comes to about 21,500, which "about 20,000" covers. The reader made two further points under place 4, and both needed correcting.
- σ = 8.5 is the greedy policies' pooled spread in evaluation. That is the right σ when only the agent is estimated. The doubling clause covers the two-estimate case and does not claim equal spreads exactly.
- The 3-SE rule had been worded as if it guaranteed the flag would fire. It does not. With n = (3σ/d)² and a true gap of exactly d, the observed gap clears 3 SE only about half the time, as the reader said. What n buys is the order. A true gap of d is then at least 3 standard errors, the size checking-a-custom-environment flagged as more than noise, so noise rarely reverses the order of two policies that far apart (a one-sided 3 SE excursion, about 0.1%). The page now says this. The formula, its link to the earlier flag and both worked cases stay, as the commission decided after editor/02. This explains the rule's existing arithmetic. It is not a new rule and teaches no interval.

Other facts I checked or that are new on the page:
- Each seed's curve end lies within about one standard error (0.86) of its frozen sampled value. From the printed Table 1: 0.35, 0.96, 0.14, 0.30 below and 0.51 above. Seed 1's 0.96 is 1.1 SE. This is the conclusion of SB3's warning check, which the page had promised and never stated (place 2). On average the warning holds, because the curve estimates sampled moves and every seed's sampled value is below its greedy value. One curve end is too noisy to show this, and seed 4's sits above its greedy 1.61.
- The last-batch fact stays: in every seed the last 100 episodes fall inside PPO's last batch of 2,048 steps. It comes from editor/02's throwaway, /tmp/claude-0/rl-editor/round2/window.out and window5.out, with the existing ppo.py and on_policy_algorithm.py citations. The page now says what it means. One network played those episodes, one update before the frozen one. Because the curve ends agree with the frozen sampled values only to within one standard error, the curve cannot show what that last update changed. These runs do not measure it, and the page no longer suggests they do.
- Seeds 3 and 4 at 10,000 episodes: exact values 1.55 and 1.61 differ by 0.06, under the 0.09 standard error. The page now says this where the misorder appears.
- After training, a second SlipperyGrid changes only the random stream that draws starts and slips. The evaluation env is TimeLimit(SlipperyGrid(), 200). The training env wraps the same thing in Returns, Monitor and DummyVecEnv, and none of those changes rewards or dynamics. SB3's stated reason, exploration noise during training, is about scoring an agent "at a given time" while it trains. The guide's next sentence recommends evaluating periodically. The evidence record's Contradictions section draws the same conclusion ("that reason does not apply once training has stopped").
- Seeds 5 to 9 (/tmp/claude-0/rl-editor/run/seeds5.out): four end on the optimal arrows, and every sampled value is below its greedy value. The page keeps only that clause.
- Fig. 1's number in the tied cells: seeds.py computes `(probs * optimal).sum(axis=1)` with both tied moves marked optimal, so 0.57 in cell 9 is P(up) + P(right). The legend now says so.
- Problem 2: callbacks.py L518-L523 saves the best model only when best_model_save_path is set. The shortened stem keeps that condition as "given a save folder".

Listings and numbers: agent.py, seeds.py and price.py and both printed outputs are byte-identical to editor/02's page. They also match editor/01's rerun outputs (/tmp/claude-0/rl-editor/run/seeds.out, price-run/price.out) exactly. No listing changed, so I did not rerun.

Sources: all 13 are still cited, each primary, in order of first citation. One locator went with a cut sentence (s10, "General advice ... third paragraph"). One went with the cut Monitor sentence (s1, `_wrap_env`). Every href: pypi, readthedocs, jair and arXiv return 200. The eight github.com blob pages return 403 to an automated client, as the evidence record says. The same paths at tag v2.9.2 return 200 on raw.githubusercontent.com. Links to earlier lessons removed: sarsa-and-q-learning#off-policy and checking-a-custom-environment#ranges. `nb check --check-links` passes.

## Reads well

The reader's places, worst first, with my action on each.

1. "Target policy". Corrected by cutting the term (see Correct). Background 08 no longer lists the target policy. The paragraph now says the policy optimization view is the question when an agent is put to use after training. SB3's deterministic advice then says why the greedy policy is the one put to use.
2. The curve, the last batch and the "gap between them". Rewritten. The sampled values get their meaning: about what the hand-drawn policy earns, against greedy values of 1.51 to 1.61, three of them optimal. The confusing last sentence ("the gap between them does not rest on the curve") is cut. The last-batch clause now names which network played the curve, and the next sentence says the runs cannot show what the final update changed. A new two-sentence verdict closes the promised check of SB3's warning, seed 4 included.
3. Machado's explore-then-exploit clause. Cut. It raised an objection the lesson never answered. The commission requires the online view in Machado's words, and their two quotations ("requiring an agent to perform well while it is learning", "hides issues of sample efficiency") carry it, now in one sentence.
4. The episode-count rule. Corrected (see Correct). The worked case is now explicitly SlipperyGrid's exact baseline, with the played-baseline figure beside it. The rule says it protects the order.
5. Why a separate environment. Corrected. The quoted reason is kept but placed where it applies, during training. One sentence says what the second SlipperyGrid does after training: it changes only the random stream.
6. Fig. 1's tied cells and doubled encoding. The legend now reads "cells 9 and 12: up and right tie, and the number adds both", and the aria-label says the same. Shading is relabelled "darker where the number is lower", so it reads as the same quantity drawn twice for scanning, not as a second quantity.
7. The "budget" sentence. Cut.
8. Why seeds stop one arrow short. One sentence added after the removal test: these runs do not show why a seed stops one arrow short, which depends on how PPO updates its network. The reader's SARSA "safe arrow" idea might fit seed 3's cell 9, but testing it needs a new computation, and seeds 2 (cell 8) and 6 (cell 13) are not cells the ε-greedy lesson discussed. The series prompt's rule for an unexplained run applies: say so in a sentence and move on.
9. "Units" and "nothing links the two policies". The first is rewritten as "averaged over starts drawn uniformly ..., as the course's baselines were solved". The second is cut.

Sections the reader could skip:
- PPO as a library call. Trimmed. The one-hot sentence, the Monitor sentence and the observation-is-the-cell sentence are cut, and the Returns sentence is folded into the gamma paragraph. The listing stays, because seeds.py imports agent.py and the series requires every file a listing needs. Also kept: the version, the gamma setting the commission requires, `greedy_moves` against `model.predict(deterministic=True)` (the definition of the greedy policy), the folder list and the reproducibility caveat.
- The Machado paragraph. Kept and shortened (see place 3). The commission requires it.
- Seeds 5 to 9. Cut to one clause. SB3's "always do several runs" quotation is cut too, because the lesson's own seeds make the point. Seed 6's ranking claim, which had no numbers on the visible page, is cut.

Results reported without their meaning:
- Table 1's curve column against the sampled column: the check is now concluded.
- "No more than 0.07 above the hand-drawn policy": replaced by its meaning.
- Seeds 3 and 4 at 10,000: the reason is given in the same paragraph.
- Seeds 5 to 9's ranking: cut.
- The standard deviations 8.6 and 8.5: each sentence now says seeds.py prints them.
- Fig. 1's other probabilities: the paragraph under it now says every cell leaves some probability on moves that are not optimal, and those moves are where the training episodes lose value.

Edges reread after the edits. The last sentence of the curve section ends on seed 4 above its greedy 1.61. The closing paragraph ends on the 180,000 count. The takeaway is unchanged and ends on the 10,000-episode misorder. None restates its section. Placeholder test on every new sentence: each falls apart without its nouns.

## The experience

Prose on the rendered page: 2,181 words. That counts the headline, dek, both cards, the 26 words of section headings, body, captions, table cells, and problems with their answers. It leaves out code, output, SVG text, the reading bands, sources, card names, summaries, labels, byline and eyebrow. The same script counts editor/02's page at 2,229, so this round removed 48 words. On editor/02's own basis, which gave 2,274, the page is about 2,225. Most of the cutting went to whole ideas: the explore-then-exploit objection, the budget sentence, the Monitor, one-hot and observation sentences, SB3's several-runs quotation, seed 6's ranking, and a bracket in problem 1's answer. The corrections in places 2, 4, 5 and 8 added words back. No explanation that stays was thinned. `nb stamp`: 4,039 words with code, 18 minutes, 13 sources.

Preview with `nb preview` and capture.cjs: 0 px horizontal overflow at phone and desktop width, in light and dark. I captured each section at desktop light and phone dark, and the seeds section in phone-dark slices (/tmp/claude-0/rl-editor/round3/). Fig. 1's new legend lines fit inside the 400-unit viewBox at both widths. The closing paragraph's formulas render. Figs. 2 and 3 are unchanged and still match the output.

What the page gives beyond its sources has not changed: it solves exactly both policies one SB3 PPO network carries, so the curve, the 10- and 10,000-episode evaluations and five seeds all sit against values fixed by the grid's rules. That agrees with the handoff's original-work sentence. This round also makes the episode-count rule say what it guarantees.

## Edits

- Card: "call judging the policy an agent ends with the policy optimization view"; "the sampling policy's included".
- Background 08: "the target policy, and" cut.
- Opening P1: the "units" sentence rewritten; "In those units" cut.
- Opening P3: every cell leaves probability on other moves, pointing to Fig. 1; the budget sentence cut.
- Fig. 1: shading legend "darker where the number is lower"; tie note "cells 9 and 12: up and right tie, and the number adds both"; aria-label extended.
- Library P1: two sentences merged on the policy-gradients stage.
- Library P2: the one-hot sentence cut; the Returns sentence moved in from P3.
- Library P3: the Monitor sentence and its s1 `_wrap_env` citation cut.
- Library P4: the observation-is-the-cell sentence cut.
- Which policy P1: Machado's explore-then-exploit clause cut; the two quotations merged into one sentence; "target policy" and its link replaced by "the policy the agent has learned"; "an agent is put to use after training".
- Which policy P2: SB3's deterministic=True advice quoted (s10, same locator); "in the course's discounted units" cut.
- After Table 1: the sampled values given their meaning; "nothing links" cut.
- Curve paragraph: rewritten around what the curve estimates, which network played it, the standard deviation from seeds.py, and the within-one-standard-error agreement.
- New paragraph: the verdict on SB3's warning, seed 4 named.
- Seeds P1: SB3's separate-environment reason placed as applying during training; a second SlipperyGrid changes only the random stream; `evaluate_policy`'s default count.
- Seeds P2: the 8.5 attributed to seeds.py.
- Seeds P3: "The order can still be wrong"; the exact values differ by less than one standard error.
- Seeds P4: these runs do not show why a seed stops one arrow short.
- Seeds P5: SB3's several-runs quotation cut; seeds 5 to 9 reduced to one clause; seed 6's ranking cut.
- Seeds P6: the rule restated as an ordering guarantee; the SlipperyGrid case marked as an exact baseline; about 20,000 each for a played baseline; the 180,000 formula dropped and the count kept.
- Problem 1 answer: "as it solved PPO's sampled policy in Table 1" cut.
- Problem 2: best_model_save_path replaced by "given a save folder".
- `nb stamp` (4,039 words, 18 minutes, 13 sources); `nb check` and `nb check --check-links`: BLOCK 0, WARN 0, PUBLISHABLE.

Decisions I took without asking, each conservative, for the orchestrator to overrule:
- The page does not say PPO is on-policy. I only removed the wrong term.
- SB3's separate-environment reason is read as applying while training runs, following the evidence record's own reading.
- The word count is reported on my script's basis, with the conversion to editor/02's basis.

## Decision

approve. The reader's restatement matches the main idea, and every place in the second report is cut or corrected on the page. The two correctness questions are settled against the earlier lesson and the source. Every number still matches the printed output, and the proof is clean.
