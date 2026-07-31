# Architecture

The Nightly Build separates intent, production, validation, and publication:

```text
press/ on main
      |
      v
scheduled correspondent -> role artifacts + article workspace
      |
      v
generated Article PR -> CI proof + browser render
      |
      v
library branch -> static site + feeds + catalog
```

`press/` is the user's specification. `nb duty` turns its cadence and the
published catalog into a deterministic work list. The correspondent routes an
article through writing coach, researcher, writer, and editor roles, recording
each brief and result.

`nb prepare-pr` creates a generated one-commit branch from current `library`,
proves the exact commit, and opens a PR. CI loads trusted engine and press
configuration from `main`, validates the untrusted content diff, renders the
candidate site, and checks the article in a browser. Only the resulting merge
changes publication state.

The site has no application backend. GitHub Pages serves generated HTML,
assets, feeds, search data, and `catalog.json` from the `library` branch.
