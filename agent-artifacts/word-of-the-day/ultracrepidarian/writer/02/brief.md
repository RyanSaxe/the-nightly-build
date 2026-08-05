# writer brief: word-of-the-day/ultracrepidarian (02) — revision

Apply the required items in the editor's review, nothing else. Preserve settled work.

Inputs:
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editor/01/editorial-review.md — the review to apply (Decision: revise)
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/researcher/01/evidence.md — for verifying the corrected facts against the primaries
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html — the article to fix
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/01/draft-handoff.md — your prior handoff

Output: /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/02/draft-handoff.md

Proof: ./nb check /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html --series word-of-the-day --library /tmp/claude-0/-home-user-the-nightly-build/5ac05fa8-7516-5815-8999-41be6fa389b4/scratchpad/library-checkout

Required items (from editor/01):
1. Dek display-text errors — fix BOTH surfaces (the `nb-meta` JSON `dek` AND the `<p class="nb-dekline">`), keeping them identical:
   (a) Apelles is **Greek**, not "Roman" (evidence: the body already says "the most celebrated of the Greeks"; Pliny places him at Cos).
   (b) The **cobbler faulted the sandal; the painter (Apelles) fixed it** — the dek currently misattributes the repair to the cobbler. Correct the attribution.
2. Word-card pronunciation: change `krep-ih` to `krep-i` (no extra "h") to match Dictionary.com's respelling `uhl-truh-krep-i-dair-ee-uhn`, or drop the respelling. (Editor already ruled OED need not be named.)

Do the display-text pass again on the corrected dek (every name/place/attribution against the evidence), then run `nb stamp` and the exact proof to BLOCK: 0, links included. The editor already made a small cut and re-stamped; do not undo settled edits. Add one line per required item resolved to draft-handoff.md.
