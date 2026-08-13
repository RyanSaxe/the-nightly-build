# writer brief: tech-news/2026-08-13 (02)

Inputs:
- editor/01/editorial-review.md (the routed changes; the editor's own direct edits
  are already in the article — preserve them)
- researcher/03/evidence.md (the COMPLETE record now — use researcher/03; it
  resolves the probiotics secondary and states the Zoom platform scope)
- writer/01/draft-handoff.md and the article in place

Output: writer/02/draft-handoff.md

Apply the editor's routed items, preserving the editor's direct edits already in
the file:
1. Probiotics item: replace/add the independent secondary with China Science
   Daily / ScienceNet (https://news.sciencenet.cn/htmlnews/2026/8/569743.shtm,
   dated 2026-08-13), which researcher/03 confirmed is independent of Springer
   Nature and the authors' institution. Keep the Nature paper as the primary. Fix
   the data-nb-kind labels and source numbering accordingly. Do not invent the
   paywalled effect-size figure.
2. Zoom "Zoomsday" item: correct the platform claim. The primary confirms the
   working exploit chain on FOUR platforms — Windows, macOS, iOS, and Android —
   with the underlying vulnerability present on five (add Linux) but the chain not
   confirmed there; the live macOS walkthrough is the fullest demonstration.
   Replace the draft's "macOS and Android" with the accurate scope.
3. Re-run nb stamp and the full links-checked nb check to BLOCK: 0; update nb-meta
   counts if they shift.

Proof: ./nb check .nb-work/tech-news/2026-08-13/library/tech-news/2026-08-13.html --series tech-news --library /home/user/library-checkout
