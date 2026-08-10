# researcher brief: expert-tools/atuin (01)

Inputs:
- `agent-artifacts/expert-tools/atuin/editorial-direction.md` — citation standard, series territory, declared reader
- `agent-artifacts/expert-tools/atuin/commission.md` — the tool, the workflow it changes, and the boundaries

Output: `agent-artifacts/expert-tools/atuin/researcher/01/evidence.md`
Source policy: minimum 6 sources.

Research questions the evidence record must answer:

- How does Atuin store history? Confirm from the project's own source or docs
  that it is a local SQLite database and record exactly which context fields it
  captures per command (directory, exit code, duration, session, hostname, and
  any others).
- How does the search work, interactively (the Ctrl-R replacement) and from the
  command line (`atuin search` and its filters)? Record the exact flags that let
  a user query by the recorded context, with a concrete working example the
  writer can show.
- What does the shell integration install and change? Record what happens to
  up-arrow and Ctrl-R, which shells are supported, and what the init hook does.
- How does sync work and what is the encryption design? Confirm the end-to-end
  encryption claim against the project's own description; record what the server
  can and cannot see, and whether self-hosting is supported.
- Is it maintained well enough to trust? Record the maintainer/governance
  situation, release cadence, and any open issues that bear on reliability. Note
  the language it is written in and how it is distributed.
- What is the honest cost and the strongest case against adopting it? Record
  contradictions and caveats in full (daemon/database overhead, the trust
  question of any sync server, migration friction).

Classify each source primary or secondary. In Source assets, note any figure
from the project's docs only if an exact visual would carry an argument better
than prose; a tool write-up usually needs none. Report in your handoff whether
every capability claim in the commission is confirmed by a primary source or
must be softened.
