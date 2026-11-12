# editor brief: reinforcement-learning/the-deadly-triad (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/editorial-direction.md: the standing directions, series prompt and template
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/commission.md: topic, idea, boundaries, recent patterns to break, and decisions
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/writer/01/brief.md: the exact writer brief
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/writing-coach/01/voice-guide.md: the series voice
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/researcher/01/evidence.md: the evidence record
- /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/writer/01/draft-handoff.md: the writer's handoff, including the seed and cell checks
- The article: /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/library/reinforcement-learning/the-deadly-triad.html
Output: /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/agent-artifacts/reinforcement-learning/the-deadly-triad/editor/01/editorial-review.md
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/reinforcement-learning/the-deadly-triad/library/reinforcement-learning/the-deadly-triad.html --series reinforcement-learning --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Recent-pattern notes: the commission's "Recent patterns to break" list is the
record to compare against (headline and dek molds, bookend openings, the
"in the field's standard notation" phrase, takeaway closers).
This round's focus:
- The removal result. Two of the three removals are degenerate on Baird's
  problem: with every reward 0 the Monte Carlo target is identically 0, and
  on-policy weighting only ever updates state 7. Judge whether the page's
  removal tests actually show what the idea claims (that the remaining two
  elements are safe), or only that a trivial case stays put. If the lesson
  needs a non-degenerate removal (for example a nonzero reward, or a variant
  where on-policy sampling visits the upper states), that is a change to the
  experiment: make it yourself if you can run it and update the page to the
  printed output, or say it requires a redraft.
- Rerun both listings exactly as printed with `uv run` and check every
  printed number and every chart of the runs against the output.
- Length: prose is about 2,390 words against the template identity's 2,200
  target; the series band (2,500 to 6,000 including code) is met. Cut where
  the page drags; do not cut a problem below two.
- The Baird citation href is the proceedings DOI; open it and confirm it lands.
Work at extra-high effort: this series requires it. After any edit, run
`/home/user/the-nightly-build/nb stamp <article>` and the proof until BLOCK: 0.
