# Editorial review: reinforcement-learning/training-an-off-the-shelf-agent (editor/01)

## Correct

Thesis, from the draft alone: PPO plays its training episodes with moves sampled from its policy, so the training curve scores that sampling policy. A trained agent is judged by its frozen greedy policy, played in a separate evaluation environment, over several seeds, between baselines of known value. Three claims carry it.

1. In every seed the sampled policy is worth less than the greedy policy of the same network: 1.36 to 1.43 against 1.51 to 1.61 (Table 1). Held. I copied the writer's run folder to /tmp/claude-0/rl-editor/run and reran `uv run seeds.py` exactly as printed. The output was byte-identical to the page, in 232 s. `uv run seeds.py 5` (seeds 5 to 9) was also identical, in 233 s. Greedy beats sampled in all ten seeds. One supporting sentence did not hold. The draft said each run's last 1,000 training episodes came out within two standard errors of its sampled value. The rerun of checks.py (identical to the writer's) shows the same averages also fall within two standard errors of each greedy value: the standard error is about 0.27, and the gap between a seed's sampled and greedy values is 0.11 to 0.24. So the check cannot say which policy the curve scores, and I cut the sentence. The claim rests on how training episodes are played and on Table 1's comparison of one network both ways, and both are on the page.

2. Ten evaluation episodes, with a standard error of 2.7, cannot place a seed inside the 0.25 band between the hand-drawn and optimal values, and they rank the optimal seed 0 last. At 10,000 episodes (0.09) seeds 3 and 4 are still out of order. Held against the printed output. I recomputed Fig. 2's scale (x = 128.2 + 29.1 v), and every dot, error bar and band edge sits where the output puts it.

3. Seeds 2 and 3 each end one arrow short of optimal, and aiming that cell up restores 1.61. Held; seeds.py prints both.

Problem 1, the commission's decision after writer/01. The answer rested on a loss at ε = 0.05 that no run printed. I ran it. `price.py`, now printed in the answer with its output, solves the ε-greedy policy around the optimal arrows with `exact_value` and prints value 1.08, below optimal by 0.53. A throwaway check of the same code at ε = 0.01 and 0.10 reproduces the losses that epsilon-greedy-exploration printed there, 0.10 and 1.08. That check confirms `exact_value` on an ε-greedy table agrees with that lesson's `best_soft`. Two other things also hold. SB3's DQN explores by `action_space.sample()` with probability `exploration_rate` (dqn.py L253 at v2.9.2), so a random move can be the greedy one. That is the ε-greedy lesson's convention. Both lessons also average over the same 14 start cells. The writer's "near 0.5" and "near 1.1" were right, and the page now prints both numbers.

Breaks against sources, and the fix for each:

- Machado et al., §4.1 (arXiv v2, p. 8). The draft gave the explore-then-exploit agent as the reason the after-learning protocol "hides issues of sample efficiency". The paper gives its own reason, "since agents are not evaluated during the entire training period", and offers the explore-then-exploit agent as a separate downside after "Furthermore". I quoted the reason and stated the second point as its own sentence.
- callbacks.py L518 to L523 at tag v2.9.2. EvalCallback always records the best mean, but it saves the best model only when `best_model_save_path` is set, and that defaults to `None`. Problem 2 said it "keeps the model with the highest mean". The evidence record says the same without the condition. The record and the source disagree, which is where I would ask. I decided by the source line and narrowed the sentence to "records the highest mean so far and, given a folder in `best_model_save_path`, saves that model as the best one".
- Source 8, PyPI torch 2.14.1. The printed page shows the release date, the Python requirement and the wheel list, and WebFetch confirms it lists no install dependencies. It cannot show what it was cited for, that the default Linux wheel installs NVIDIA's CUDA packages. PyPI's JSON metadata does list the nvidia-* packages under `platform_system == "Linux"`, and the researcher's install check downloaded them, but the JSON endpoint is not a page a reader can land on. I kept the CUDA clause uncited, as common ground for readers who have installed torch on Linux. I moved the citation to what the page does show: the same release ships wheels for Apple-silicon Macs and Windows. That new sentence also explains the listing's Linux-only marker, which is the commission's accepted decision after writer/01. This is a judgment call. If the orchestrator wants the CUDA clause cited, it needs a readable source the researcher did not gather.
- Henderson et al., p. 5. "Found the same" overstated the match: their result is about averaged learning curves, and this lesson's is about the greedy policy each seed ends on. I reworded it to say they saw seeds alone change a result on a larger task, and named TRPO as a policy-gradient algorithm so the sentence stands for a reader who has not met it.

Headline, dek and headings. Every figure checks against the output: three of five seeds at 14/14 optimal arrows and two at 13/14. The headline's claim, greedy outscoring sampled, holds for whole policies in ten of ten seeds.

Citations. I opened every `href`. The four SB3 documentation pages, arXiv and JAIR land. Both PyPI pages land in WebFetch; curl gets a JavaScript challenge from them. Every github.com blob link returned 403 inside this session. The response body shows the 403 comes from this session's network policy, not from GitHub. I cloned the repository at tag v2.9.2, which resolves to commit 0cdcd200, the commit the record names. Every cited path exists there, and every locator matches its line: `get_actions` L82 to L91, Categorical `mode` L304 to L305, PPO defaults L80 to L108, `_wrap_env` L204 to L224, `stats_window_size` L112, `ep_info_buffer` L405, Monitor's sum L100, `rollout/ep_rew_mean` L291, `evaluate_policy`'s signature, docstring and loop, DQN's exploration defaults, schedule and `predict`, and EvalCallback's defaults and best-model block. Not verified: that the blob pages render for a reader outside this sandbox. The quotations from RL Tips (three) and Reproducibility match the v2.9.2 pages, and every anchor exists.

`data-nb-kind`. All 15 are primary, and correctly so: each is the library's own code, documentation or release record, or the paper that ran the experiment. No source is presented as an independent secondary.

Internal links. The seven Background titles match the published lessons, and the anchors #gymnasium, #baselines, #ranges, #discount and #price exist and open on the sections the sentences describe. I added one link: "target policy", inside the Henderson quotation, now points to sarsa-and-q-learning#off-policy, where the course defined it.

Other reruns from draft-handoff.md, all in my copy at /tmp/claude-0/rl-editor/writer-scratch, all identical to the writer's: checks.py on seeds 0 to 4, checks2.py, and det.py with one thread and with four (1.364902 and 1.82 against 1.406224 and 1.38).

## Reads well

What went, and why:

- "These are the cases the explanation of Table 1 fits worst" and "Taking the most probable move instead is the removal test". These came from the briefing, the series prompt's names for its own checks. The page never defines "the removal test" for a reader. I restated the point in the article's terms: the same networks earn more with their most probable moves. The worst-fit paragraph was later cut whole for length (see The experience).
- "Afterward you can train PPO on an environment of your own". This repeated the recent record: it is the "You can then prove" build the commission flagged. The card's third part is now a recipe in this lesson's nouns.
- "That is measured after training". Said nothing: "that" stood alone for an unnamed thing. Gone with the card rewrite.
- The first body paragraph repeated the card's definition of a training curve, which the identity rules out. It now gives only the specific: the last 100 episodes.
- "Stable-Baselines3 is a library of off-the-shelf agents" opened both the card and the library section. The section now says what the library trains on.
- "The curve and the frozen greedy policy describe two different policies". A policy does not describe a policy. Now: the curve scores a different policy from the frozen greedy one.
- "Which makes it a frozen policy" said the network was a policy. "Frozen policy" is now defined in one sentence.
- "Those 14 moves" and, a section later, "those 16 moves" for the same table. One word per thing.
- "The underestimate can be solved". You solve for a policy's value, not for an underestimate.
- "The training curve adds noise of its own" became "The curve is also noisy". That paragraph now ends on what its numbers mean: four of the five curves end below the hand-drawn 1.36, though all five greedy policies earn more than it.
- "Seeds 5 to 9, run as a check" now gives the command that runs them.
- A sentence that opened on lowercase `gamma`.

What I lifted. The Why this matters card now runs in the identity's order: what SB3 logs and why that scores the sampling policy, what to judge instead, the name of the view, and what a reader can do on an environment with no exact solve. The opening case uses "we" for the steps the reader and writer take together, as the identity asks. Elsewhere the draft was already close to the voice guide's register, and I did not rewrite toward it for its own sake.

The article's last sentence stays: "Ten evaluation episodes, with a standard error of 2.7, could not show which two." It is concrete, and the page shows it.

## The experience

Prose on the rendered page: 2,205 words. That counts the headline, dek, both cards, body, captions, table cells and problems with their answers. It leaves out code, printed output, SVG text, the reading bands and the sources. I counted from the HTML with the same script before and after. The writer's draft counts 2,150 by that script (the writer reported 2,198 by theirs). Problem 1's worked answer and the card took the page to 2,265, past the identity's limit of about 2,200. I cut one whole result rather than thin an explanation: the off-page finding that in seeds 2 and 3's one wrong cell, sampling beats the greedy move. The main idea does not need it. The page's explanation already covers it, since sampling adds value only where the greedy move is wrong, and the series prompt lets that check stay off the page.

Rendered with `nb preview` and captured at phone and desktop width, light and dark: 0 px horizontal overflow in all four. I also opened problem 1's answer and captured it in all four views. `price.py` and its one-line output render in both themes, and on a phone the listing scrolls inside its own block. Figs. 1 to 3 are unchanged from the draft and still match the output. Fig. 2's labels are small on a phone but follow the press's 400-unit viewBox.

The seeds section is the longest, and it carries the second result and the spread across seeds. The weight sits where the idea needs it. No component needs adding: Table 1 is the right form for its fifteen numbers, and the three figures each show something a paragraph would show more slowly.

What the page gives beyond its sources: it solves exactly both policies inside one SB3 PPO run, so the training curve, the 10- and 10,000-episode evaluations and five seeds each sit against values fixed by the grid's rules. SB3 says only that the curve "underestimates". This matches the writer's original-work sentence.

## Edits

- Dek, page and nb-meta: three of five runs on the optimal arrows and two one arrow short, a gap ten evaluation episodes cannot detect. Replaces the bare 1.51 to 1.61 range.
- Why this matters: rewritten. Opens on what SB3 logs, then what to judge instead, the policy optimization view, and a recipe for an environment with no exact solve.
- Opening case: "We train"; training-curve sentence trimmed to the last-100 detail; GAMMA and start-cell sentence split in two.
- Opening case: "frozen policy" defined; "In each cell we take".
- Opening case: "The curve scores a different policy from the frozen greedy one."
- Library: SB3's first sentence no longer repeats the card.
- Library: "PPO's discount, `gamma`," to open the sentence.
- Library: "one move per cell is the whole frozen greedy policy", replacing "those 16 moves".
- Library, torch: CUDA clause kept without a citation; new sentence on Apple-silicon Macs and Windows taking 2.14.1 from PyPI, carrying citation 8 with a new locator.
- Which policy: Machado's sample-efficiency reason quoted in full; explore-then-exploit stated as a separate point; locator narrowed to "Evaluation after learning"; "the Atari games of" added before the Arcade Learning Environment.
- Which policy: "target policy" in the Henderson quotation linked to sarsa-and-q-learning#off-policy.
- Which policy: "the policy behind the curve can be solved exactly".
- Which policy: removal-test sentence rewritten as a comparison of the same networks; last-1,000-episode sentence cut; noise paragraph now ends on all five greedy policies beating the hand-drawn value.
- Seeds: "The last loop of `seeds.py`" replaces "The removal test in `seeds.py`"; sampled-probability and worst-fit sentences cut.
- Seeds: Henderson sentence reworded and split; TRPO named as a policy-gradient algorithm; "the HalfCheetah benchmark".
- Seeds: "Seeds 5 to 9, from `uv run seeds.py 5`".
- Problem 1: question now says "the first 10% of its training steps" and asks for the exact solve as well as the price of ε.
- Problem 1 answer: the interpolation replaced by the bracket from the earlier lesson, the new `price.py` listing and its printed output, and the conclusion at 1.08.
- Problem 2: EvalCallback narrowed to recording the best mean and saving the model only when `best_model_save_path` is given.
- Takeaway: "A trained agent is judged by its frozen greedy policy instead", replacing "The policy training ends with is the frozen greedy policy".
- `nb stamp` run (words 4,065, 18 minutes, 15 sources); `nb check` with `--check-links`: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The argument stands, every listing and check reproduces, and the required corrections are made on the page. The reader check comes next.
