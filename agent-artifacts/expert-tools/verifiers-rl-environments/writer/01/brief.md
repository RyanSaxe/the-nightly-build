# writer brief: expert-tools/verifiers-rl-environments (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/editorial-direction.md : standing directions
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/commission.md : the assignment, boundaries, recent patterns and decisions
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writing-coach/01/voice-guide.md : how the piece sounds
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/evidence.md : the complete claim set, with Appendix A signatures
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/researcher/01/nowcast_alfred/ , eval.toml : the environment that ran against 0.4.0
- /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/.nb-context/ : template contract and furniture catalogs
Output: /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/agent-artifacts/expert-tools/verifiers-rl-environments/writer/01/draft-handoff.md, and the article at
  /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html
Proof:  /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/expert-tools/verifiers-rl-environments/library/expert-tools/verifiers-rl-environments.html --series expert-tools --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository, the Git history or the
archive for background. Where something you need is missing, ask me.

Run-environment notes:
- The word band (1200 to 3000) counts every word in the rendered article,
  including code listings, table cells and the sources list. Budget code
  tightly: listings excerpted from nowcast_alfred, trimmed to the lines that
  teach a hook, with an honest caption saying they were run against 0.4.0
  under the subprocess runtime with a stub model.
- Owner rule: zero em-dashes and zero semicolons anywhere in the article
  file's rendered text, including code comments and captions. Check with grep
  before handoff.
- Recent shapes to break are in the commission (no "Verdict" closer, no
  comma-and headline, no second-person scenario opener).
- nb-meta: date 2026-10-14, harness "claude-code", model "claude".
- Use furniture from the catalogs where it teaches faster: code listings,
  a table mapping each leak path to what closes it, possibly a stat strip
  for the noise figures. Read the catalog markup, do not infer classes.
