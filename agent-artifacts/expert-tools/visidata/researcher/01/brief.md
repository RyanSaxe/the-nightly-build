# researcher brief: expert-tools/visidata (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/editorial-direction.md — citation standard, series territory, declared reader
- /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/commission.md — the tool, the changing move, cost/maintenance obligations, sourcing

Output: /home/user/the-nightly-build/.nb-work/expert-tools/visidata/agent-artifacts/expert-tools/visidata/researcher/01/evidence.md

Run environment: harness = claude-code, model = capable, high effort. Web search
and fetch available; you may also inspect VisiData's public source/docs.

Focus:
- Go past the README. Establish firsthand, from the PRIMARY record (visidata.org
  docs, the saulpwanson/visidata GitHub repo, the changelog/releases, the
  author's writing/talks): the exact commands and keybindings for the moves the
  article will show — at minimum a frequency table (`F`), adding an aggregator
  (`+`), a Python-expression computed column, and pivot/melt — and confirm each
  against current docs or source. Note the current released version and its date.
- Establish the async/incremental loader claim firsthand (that exploration can
  begin before a large file finishes loading) from docs/source, and any concrete
  numbers about supported formats. Do not carry a remembered API; if a keybinding
  changed across versions, record the current one and the version.
- Maintenance/trust: who maintains it, release cadence, open-issue posture,
  license. Adoption cost: the modal-keystroke learning curve, where a notebook or
  SQL is still the better tool, and known limitations. Search for credible
  critiques, not just praise (Contradictions section).
- Identify whether any real visual (e.g. an official screenshot from the docs
  that the argument would actually spend) is a legitimate source asset, or write
  None found. A demonstration is better shown as an authored code/transcript
  block than as a decorative screenshot; flag this for the writer.
- Confirm every URL resolves to the source's own page.
