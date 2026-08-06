# writer brief: paper-of-the-day/instructgpt (02)

Purpose: integrate the round-02 evidence so the article clears the paper
template's 8-source floor honestly, then re-prove. This is a sourcing/evidence
round, not a rewrite — do not expand the claim set beyond what the new sources
support.

Inputs:
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/researcher/02/evidence.md  (the CURRENT complete claim set — 9 opened sources; supersedes 01)
- .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writer/01/draft-handoff.md  (your prior handoff)
- .nb-work/paper-of-the-day/instructgpt/library/paper-of-the-day/instructgpt.html  (your existing draft to edit in place)
- editorial-direction.md, commission.md, writing-coach/01/voice-guide.md (unchanged)
- .nb-work/paper-of-the-day/instructgpt/.nb-context/

Output: .nb-work/paper-of-the-day/instructgpt/agent-artifacts/paper-of-the-day/instructgpt/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/paper-of-the-day/instructgpt/library/paper-of-the-day/instructgpt.html --series paper-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/976dc2e8-9069-59ea-94ea-a08d4d77fd63/scratchpad/library-checkout
(run from repo root; --no-check-links while iterating, then links-included until BLOCK: 0 AND W-SOURCES-MIN cleared)

What to do (only this):
- Weave the four added primaries into the lineage the article already argues —
  that InstructGPT assembled and scaled an existing method rather than inventing
  it — citing each where the prose already makes (or should make) that point:
  Christiano et al. 2017 (preference-to-reward origin, Bradley-Terry + CE loss);
  Ziegler et al. 2019 (first KL-to-pretrained-policy penalty on an LM, and its
  self-reported labeler-heuristic exploitation as an early instance of the
  over-optimization Gao later formalizes); Stiennon et al. 2020 (the same
  SFT->RM->PPO+KL pipeline a year earlier, overlapping author set); Schulman et
  al. 2017 (PPO, the Stage-3 RL algorithm — cite where you name PPO).
- Add each to the Sources list with the correct data-nb-kind (primary for its
  own claim) in first-citation order, and update nb-meta counts via `nb stamp`.
- Swap the OpenAI-release citation to the resolvable page
  https://openai.com/index/instruction-following/ (the cdn.production path is a
  non-citable transport per the evidence record).
- Honor the evidence record's venue-string flags: print only venues confirmed
  there; leave others as arXiv preprints. Do not invent a venue.
- Keep every round-01 equation, the headline verification, and the central
  finding intact. The three W-SENTENCE-DENSITY warnings on the displayed
  equations may remain if still justified (record why in the handoff); the goal
  is BLOCK: 0 with the source floor met.

Record in writer/02/draft-handoff.md: the new source total, one line per source
added and where it is cited, and the final proof result. Do NOT run git.
