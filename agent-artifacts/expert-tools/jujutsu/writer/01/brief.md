# writer brief: expert-tools/jujutsu (01)

Inputs:
- ../../editorial-direction.md — house standard, article-template identity, series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the verified model, the command sessions (run against jj 0.44.0), the honest costs and the backing ambiguity; cite only what it carries
- /home/user/the-nightly-build/.nb-work/expert-tools/jujutsu/.nb-context — template contract, furniture catalogs
- the initialized article at /home/user/the-nightly-build/.nb-work/expert-tools/jujutsu/library/expert-tools/jujutsu.html — edit in place; keep engine assets/labels exact

Output: ./draft-handoff.md
Proof (from /home/user/the-nightly-build): ./nb check .nb-work/expert-tools/jujutsu/library/expert-tools/jujutsu.html --series expert-tools --library /home/user/library-checkout
  (use --no-check-links while iterating; final run links included, to BLOCK: 0)

This round's focus:
- Prove the value on the evidence's verified demonstration: the botched rebase
  undone exactly, where `jj undo` restored byte-identical commit IDs. Build the
  model it rests on first (working copy as a commit, the `@` revision, no staging
  area, the operation log). Use the real commands and observable effects the
  evidence recorded; do not invent command output. Name the jj version (0.44.0).
  Show a code listing where the reader could follow the sequence; the example
  proves the tool, it is not an install tutorial.
- Give the honest-cost section real weight from the evidence: the Git-backend
  index-corruption risk, the lossy conflict auto-resolution rule, missing Git
  hooks and no `--fixup` equivalent, bookmark-push and colocation friction.
- The backing question is genuinely unresolved in the record (the Google
  disclaimer vs. the paid-contributors disclosure naming East River Source
  Control). Characterize maintenance honestly on that evidence; do not default to
  "Google's tool" or "a funded startup's tool." Say what the record shows and
  what it leaves open.
- Name the tool and the work it changes in the headline and the section titles.

Recent shapes to break (do not inherit):
- Do not write the dek in the recent expert-tools mold of a headline capability
  followed by an undercutting caveat ("... thins to the provider's feature",
  "... covers less than the word suggests"). Put the honest cost in the body and
  write a dek that states this tool's actual surprise.
- A version-control tool is a clean change of family from the recent Python/CLI/
  Neovim picks; nothing structural should echo those pieces.
