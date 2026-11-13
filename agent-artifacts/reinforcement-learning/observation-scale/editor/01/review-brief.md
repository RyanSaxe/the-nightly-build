# editor brief: reinforcement-learning/observation-scale (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editorial-direction.md: the standing directions, series prompt and lesson template
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/commission.md: topic, idea, case, boundaries, recent patterns and decisions
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/brief.md: the exact writer brief
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writing-coach/01/voice-guide.md: the pinned series voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/researcher/01/evidence.md: the evidence record
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/draft-handoff.md: the writer's handoff, with the checks it ran
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/writer/01/code/: the lesson's code and throwaway checks
- The article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/agent-artifacts/reinforcement-learning/observation-scale/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/observation-scale/library/reinforcement-learning/observation-scale.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Recent-pattern notes: the commission's "Recent patterns to break" section is
the record. Recent lesson headlines: "A problem whose true values are all zero
sends off-policy TD's weights to infinity", "TD(0) no longer converges to the
best fit once states share weights", "Four-step TD learns a 19-state random
walk faster than TD(0) or Monte Carlo". Recent deks opened "On Baird's ..."
and with a method name as subject joined by ", and".
This round's focus: (1) the dek is one long sentence with a trailing "which"
clause; judge it under spec/headlines.md. (2) The headline claims millimetres
"keep PPO from using a cart's velocity": check it against agents.py's printed
output and the new-seed checks, and that the page claims no cause for the PPO
gap beyond what its removal tests show. (3) Rerun the listings as printed
(linear.py fast; agents.py takes ~3 min on 4 cores) and check every number
and chart against the printed output. (4) The derivation: A → DAD, the c²
condition, the 2/λmax bound for the expected update vs the per-sample case.
(5) Apply the commission's length and model-field decisions. (6) Inspect the
visuals rendered (nb preview plus Playwright; Chromium preinstalled). After
any edit, run `/home/user/the-nightly-build/nb stamp <article>` and the proof
until BLOCK: 0.
