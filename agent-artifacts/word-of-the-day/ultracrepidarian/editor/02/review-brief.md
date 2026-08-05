# review-brief: word-of-the-day/ultracrepidarian (editor/02) — confirm revision

The editor/01 decision was `revise` for two dek display-text errors and a pronunciation
respelling. The writer applied them in writer/02. Confirm the fixes resolved the issues and
introduced nothing new. This is a focused confirmation read, not a fresh full review; do not
raise new standards late (editor skill).

Inputs:
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editor/01/editorial-review.md — the required items
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/writer/02/draft-handoff.md — what the writer changed
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/researcher/01/evidence.md — to verify the corrected facts
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/library/word-of-the-day/ultracrepidarian.html — the article
- /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editorial-direction.md — standards

Output: /home/user/the-nightly-build/.nb-work/word-of-the-day/ultracrepidarian/agent-artifacts/word-of-the-day/ultracrepidarian/editor/02/editorial-review.md

Run environment: harness = claude-code, model = inherit (Opus-class), high effort.

Confirm:
- The dek (both surfaces — nb-meta JSON `dek` and `<p class="nb-dekline">`) now reads identically and correctly: Apelles is GREEK (Pliny is the Roman who recorded it); the cobbler FAULTED the sandal and the painter fixed it (repair correctly attributed). Check against the evidence (NH 35.85; the body's own "Greeks"/Cos).
- The word-card pronunciation is `krep-i` (no stray "h"), matching Dictionary.com.
- No new error introduced; the editor/01 settled cut ("The wording matters.") remains; counts still in band (words≈603).
- Every citation href still resolves to its own page (spot-check is fine; the writer re-proved links BLOCK:0).

Decision: approve if the required items are resolved and nothing new is broken; otherwise name the precise remaining item and owner. Do not run the full proof (the writer did); after any direct cut of your own, run `nb stamp`.
