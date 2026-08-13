# writer brief: tech-news/2026-08-13 (01)

Inputs:
- editorial-direction.md (house standard, slop, headlines, press voice, brief
  template identity, series prompt) — at the artifact root
- commission.md (the beat, the significance standard, the split, the do-not-repeat
  list) — at the artifact root
- writing-coach/01/voice-guide.md (how the items should sound)
- researcher/02/evidence.md (the COMPLETE record — use this one, not 01; the
  final verified slate is here)
- the initialized article: library/tech-news/2026-08-13.html
- template context under .nb-context/

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/tech-news/2026-08-13/library/tech-news/2026-08-13.html --series tech-news --library /home/user/library-checkout

The slate (from researcher/02): four fully-sourced items — the AI-assisted
zero-click Zoom exploit chain ("Zoomsday"); Meta's Muse Glimmer 30B open-weight
agent model; the IBM/Together AI Nvidia inference cluster; and the Nature
glucose-responsive engineered-probiotics paper. Each item carries exactly one
primary and at least one independent secondary, labelled honestly with
data-nb-kind. Two cautions from the record: the Nvidia $500B financing story was
dropped as a stale repeat of an August 10 MOU — do not add it back; and the
probiotics paper's exact effect-size figures are paywalled and not in the record,
so do not invent a number — report what the record supports and say what is not
yet public. Keep the CloudSEK breach and the California AI-bill votes OUT (they go
to current-events). Order items by significance; lead with the one that matters
most.

Recent shapes to break (from the commission): recent tech briefs headline on a
thematic "X stays quiet while Y" summary line and pair-adjective molds. Pick the
one development that matters most and say what happened to it, per the headline
standard. Each item's "why it matters" does analysis, not recap.

nb-meta: date "2026-08-13", harness "claude-code-routine", model "claude-sonnet".
Run `nb stamp` before the final links-checked proof.
