# Editorial review: reinforcement-learning/training-an-off-the-shelf-agent (editor/02)

## Correct

This round answers reader check 1. The thesis is unchanged. PPO plays its training episodes with moves sampled from its policy, so the training curve scores that sampling policy. A trained agent is judged by its frozen greedy policy, played in a separate evaluation environment, over several seeds, beside baselines. The claims under it are the same three as in editor/01: sampled is below greedy in every seed, ten evaluation episodes cannot sort the seeds and 10,000 still misorder two, and one arrow accounts for each short seed. None of my edits changes a number, a quotation or what a citation is cited for.

The reader's restatement against the main-idea sentence. The reader got the sampling-policy argument, the exact gap, the noise and the evaluation recipe. It did not find where the baselines "of known value" come from once there is no exact solve (its place 2). That is a mismatch in the sentence's last clause, so the page changed: the card and the closing paragraph now say the baselines are random moves and a scripted policy, each played in the evaluation environment like the agent. A corrected main-idea sentence for the handoff, 30 words: "Judge an agent by its frozen greedy policy's return in a separate evaluation environment, over several seeds, beside baselines scored the same way; its training curve scores the sampling policy." I did not edit the writer's handoff.

New facts on the page, and what supports each:

- SB3 logs `rollout/ep_rew_mean` as the mean of the last 100 episodes' undiscounted sums. Already cited (base_class.py L112 and L405, monitor.py L100, on_policy_algorithm.py L291). Moved to the opening, where the term first appears.
- PPO updates its network once per batch of 2,048 steps. ppo.py L33 (the n_steps docstring, "per update") and L85 (default 2048), and on_policy_algorithm.py L324 and L337 (`learn` calls `collect_rollouts`, then `train`). I read these lines in the v2.9.2 clone at /tmp/claude-0/rl-editor/sb3, commit 0cdcd200, the commit the evidence record names. Both are existing sources with new locators.
- In every seed the last 100 training episodes fall inside the last batch. This comes from a throwaway check, /tmp/claude-0/rl-editor/round2/window.py, with seeds 0 to 9 (window.out and window5.out). The last 100 episodes took 410 to 464 moves and began after step 50,736. The last batch began at 49,152. The same runs reproduce Table 1's first column and seeds5.out exactly (1.01, 0.45, 1.25, 1.10, 1.94; 1.79, 0.48, 1.61, 1.10, 2.36), so they are the page's runs. The page gives the conclusion without the numbers, as the series allows for checks.
- The episode-count rule, n ≥ (3σ/d)², twice that for two estimated means. This is arithmetic on the printed σ of 8.5 and the printed values. The 3-standard-error threshold is the flag the lesson on checking a custom environment printed. (3 × 8.5 / 0.25)² = 10,404, and (3 × 8.5 / 0.06)² = 180,625. Before rounding the seed-3 gap is 0.056, which gives about 209,000. The page uses the printed 0.06, so a reader can redo the sum, and says "some 180,000".
- Seed 6 (seeds 5 to 9) aims up in cell 13, and both its 10 and its 10,000 evaluation episodes rank it above an optimal seed. seeds5.out from editor/01's rerun: 5.48 at 10 episodes, first of five, and 1.52 at 10,000 against seed 5's optimal 1.51.

Links. These were added or kept, and each anchor exists in the published library: sarsa-and-q-learning.html#estimates-describe, which solves the ε-greedy policy around fixed arrows; epsilon-greedy-exploration.html#price; and checking-a-custom-environment.html#baselines, where the 3-standard-error flag appears. `nb check --check-links` passes.

Sources. Two sources no longer carry a citation and are removed: the VecEnv documentation and the PyPI torch page. The rest are renumbered in order of first citation (13 sources). Every `data-nb-kind` is still primary.

Listings. agent.py, seeds.py and price.py are byte-identical to the files editor/01 reran, and the printed outputs match those reruns exactly. I changed no listing, so I did not rerun them.

## Reads well

The reader's places, worst first, with my action on each.

1. "Training curve" meant two quantities. Fixed by stating the term once and holding to it. The opening now defines it: SB3 logs `rollout/ep_rew_mean` undiscounted, we record the same 100 episodes at GAMMA, and in this lesson the training curve means that discounted average. Table 1's column header now reads "Training curve, last 100 episodes". The SB3 warning is now tied to the lesson's test: SB3's log and this curve average the same episodes. I did not print SB3's undiscounted number. The throwaway shows it for seed 0 (1.82 against 1.01 discounted), but putting it on the page would add a number on another scale and a paragraph on why it is larger. A sentence that it is the same episodes answers the reader's question.
2. The recipe needed baselines it could not get. Explanation added, because the main idea needs it. Off SlipperyGrid the baselines are random moves and a scripted policy you write, each played in the evaluation environment like the agent. Both the card and the closing paragraph say so.
3. The episode-count advice stopped short. Rewritten into a rule with its arithmetic, using the course's own 3-standard-error flag. "The gap" is now defined as the smallest difference the comparison has to show, with both cases worked: 0.25 needs about 10,000 episodes (what seeds.py ran) and 0.06 needs some 180,000. This sits at the edge of the commission's boundary that statistics of reporting belong to stage 4. I judged it inside the line, because it inverts σ/√n and reuses an earlier flag without teaching an interval. If the orchestrator reads that boundary more strictly, the closing paragraph's last three sentences are the ones to cut.
4. Why PPO stays this stochastic. One sentence added, and no explanation of the algorithm (the commission forbids one): how much probability PPO leaves on other moves depends on its update, which a later stage builds, and this lesson does not vary its budget. The ε-greedy connection the reader asked for is one clause linking the price of ε.
5. The last 100 episodes were played by earlier networks. Answered from the throwaway check and the source lines. The episodes fall inside PPO's last batch, so the network before the final update played them. Table 1's other two columns solve the frozen network itself, so the sampled-against-greedy gap does not rest on the curve. This is a new paragraph made from the old paragraph's last sentence plus three more.
6. The DummyVecEnv paragraph. Cut, with Background item 08 and its source. The Monitor sentences shrank to the one the code needs.
7. "Offline" undefined. The Henderson quotation is replaced by a paraphrase of the same passage: the target policy is scored in an evaluation kept apart from learning. The source (p. 6) uses "offline" in that sense.
8. "The policy optimization view" named before it is explained. The card now names it right after describing it: "this way of judging an agent". The body defines both views.
9. "The last loop of seeds.py" pointed at collapsed code. It now points at the visible line under each grid in Fig. 3.
10. Problem 1 pointed at the wrong tool. The hint now asks the reader to solve the ε-greedy policy around the arrows with `exact_value`, and links where the SARSA and Q-learning lesson solved that policy. I cut the answer's bracket from the price of ε to hold length. Background 08 is now that lesson. DQN is called "SB3's DQN agent". The card of the SARSA and Q-learning lesson already named DQN as a later lesson's subject.

Sections the reader could skip:

- Torch, threads and CUDA. Cut except SB3's reproducibility caveat, which a reader running the code needs. It now closes the folder paragraph.
- Background 08. Replaced (see place 6).
- Henderson's TRPO and HalfCheetah paragraph. Cut. The lesson's own seeds show the seed effect, and Go deeper 02 keeps the pointer.
- Machado's quotations. Kept. The commission requires the online view stated fairly in their words, and the explore-then-exploit point is a fair objection to exactly this lesson's protocol. The two views are now four sentences instead of five.

Results reported without saying what they mean:

- The thread result: cut.
- Seeds 5 to 9: the page now names seed 6 and cell 13, and says both evaluations ranked it above an optimal seed.
- Sampled values near the hand-drawn value: the page now says nothing links the two policies. Which policy is scored decides whether an agent sits at the hand-drawn level or near the optimum.
- Henderson's "statistically different": cut with the paragraph.
- Seeds 3 and 4 at 10,000: the episode-count rule now says what would fix it. The takeaway adds that 10,000 episodes still ranked a short seed above an optimal one.
- Problem 2: kept. A problem may ask about a case the lesson did not work through. This one needs only the standard error the lesson uses, and the answer carries the Machado source for the bias.

Also cut to hold length: the TimeLimit/STUCK point about `evaluate_policy` never ending a looping episode. It is true and useful, but the main idea does not need it. The Background row for the lesson on the value of a state no longer mentions STUCK.

Edges reread after the edits. The closing paragraph before the problems now ends on a computed count. The takeaway's last sentence ends on the 10,000-episode misorder. Neither restates the section.

## The experience

Prose on the rendered page: 2,274 words by my count. That covers the headline, dek, both cards, the 26 words of section headings, body, captions, table cells and problems with answers, and leaves out code, output, SVG text, the reading bands and sources. Without the headings it is 2,248. The same script gives 2,239 for editor/01's page, against the 2,205 editor/01 reported, so on editor/01's basis the page is about 2,240, roughly 35 words above the previous round. I cut whole ideas to hold it there: DummyVecEnv, the CUDA and thread sentences, Henderson's seed study, the TimeLimit/STUCK point, a repeated seed-count sentence and the price-of-ε bracket in problem 1. No explanation that stays was thinned. `nb stamp`: 4,099 words with code, 18 minutes, 13 sources.

Preview with `nb preview` and capture.cjs: 0 px horizontal overflow at phone and desktop width, light and dark. I captured each section on its own at desktop light and phone dark. The new closing paragraph's inline formula renders in both, and the Table 1 header wraps cleanly on a phone. Figs. 1 to 3 are unchanged and still match the output.

What the page gives beyond its sources is unchanged from editor/01: it solves exactly both policies inside one SB3 PPO run. The training curve, the 10- and 10,000-episode evaluations and five seeds all sit against values fixed by the grid's rules. This round adds a rule for choosing the evaluation count, tied to those values.

Second reader check: my response does not change the lesson's central explanation and does not rewrite a whole section. New text that no reader has seen: the training-curve definition in the opening, the last-batch paragraph after Table 1, the card's last sentence, and the closing paragraph's baselines and episode-count rule.

## Edits

- Card: baselines named as random moves and a scripted policy; "this way of judging an agent the policy optimization view"; last sentence now says baselines are played in the evaluation environment and the episode count comes from the smallest gap.
- Background 04: the STUCK mention dropped.
- Background 07: the price of ε glossed as the value an agent loses to its random moves.
- Background 08: the VecEnv documentation replaced by the lesson on SARSA and Q-learning.
- Opening P1: SB3 introduced; `rollout/ep_rew_mean` defined, cited; the training curve defined as the discounted average of the same 100 episodes.
- Opening P3: a clause linking the price of ε; a sentence that PPO's leftover probability depends on its update and that the budget is not varied.
- Library P1: "SB3 for short" moved to the opening.
- Library P3: DummyVecEnv cut; Monitor reduced to the sums behind SB3's log; Returns tied to the training curve.
- Library P5: the CUDA, Apple-silicon, Windows and thread sentences cut; the reproducibility caveat moved into the folder paragraph.
- Which policy P1: the Henderson quotation paraphrased; the two views merged into fewer sentences.
- Which policy P2: SB3's log and this curve average the same episodes.
- Table 1: column header "Training curve, last 100 episodes".
- After Table 1: the sampled values given their meaning, split from a new last-batch paragraph with ppo.py and on_policy_algorithm.py citations.
- Seeds P1: the TimeLimit/STUCK sentence cut; `evaluate_policy` introduced as SB3's own evaluation function.
- Seeds P4: "the line under each grid in Fig. 3" replaces "the last loop of seeds.py".
- Seeds P5: the Henderson TRPO sentences cut; the repeated three-of-five sentence cut; seed 6 and cell 13 named, with both evaluations ranking it above an optimal seed.
- Seeds P6: rewritten as the recipe for an environment of your own, with the n ≥ (3σ/d)² rule and both worked cases.
- Problem 1: "SB3's DQN agent"; the hint now points to solving the ε-greedy policy around the arrows, linked to sarsa-and-q-learning#estimates-describe.
- Problem 1 answer: the price-of-ε bracket cut.
- Takeaway: "and 10,000 still ranked one of them above an optimal seed".
- Sources: VecEnv documentation and PyPI torch removed; renumbered by first citation; the on_policy_algorithm.py note now names L324-L337.
- `nb stamp` (4,099 words, 18 minutes, 13 sources); `nb check`, and `nb check --check-links`: BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. Every place in the reader's report is cut or answered on the page, every figure still matches the printed output, and the proof is clean.
