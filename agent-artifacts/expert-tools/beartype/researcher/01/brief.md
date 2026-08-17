# researcher brief: expert-tools/beartype (01)

Inputs:
- editorial-direction.md   the citation standard, the series territory, the reader
- commission.md            the tool, what to show, and the boundaries

Output: /home/user/the-nightly-build/.nb-work/expert-tools/beartype/agent-artifacts/expert-tools/beartype/researcher/01/evidence.md

Notes:
- Read the primary record: beartype's own documentation and README, the source
  implementation of its near-constant-time checking (the sampling strategy), the
  changelog/release history, and the issue tracker for real limitations and
  maintenance signal. Confirm current version and maintenance status.
- Verify the specific mechanism claims (how the O(1) sampling works and what it
  therefore cannot guarantee), overhead characteristics, and Python-version and
  hint-coverage support against the primary docs/source, not blog summaries.
- Gather exact, runnable example material: a call boundary where beartype catches
  a type violation, and a precise comparison against typeguard, pydantic, and
  static checkers on what each does at runtime.
- Record contradictions or overstated claims (in the project's own marketing or
  in third-party posts) with the primary that settles them.
