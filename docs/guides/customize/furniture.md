# Furniture

Furniture is reusable article markup with a defined communicative purpose: a
timeline, comparison, evidence card, pull quote, rubric, or other reading aid.
Start with `templates/FURNITURE.md`; its components work in every template.

Custom furniture has two scopes:

```text
press/furniture/
├── catalog.md
├── styles.css
└── samples/<slug>.html

press/templates/<id>/
├── furniture.md
├── furniture.css
└── samples/<slug>.html
```

Use shared press furniture when several series may need it. Keep a component
inside a template when its meaning depends on that template. Use your own CSS
prefix because `nb-` is reserved.

A component is product design, not decoration. It earns its place by making
specific information easier to understand than prose would, and it must hold
up for every reader: semantic markup, keyboard and screen-reader behavior, a
no-JavaScript fallback, long content, narrow screens, and both themes. Its
catalog entry is the component's contract: when to use it, the exact markup,
and its constraints.

Your assistant designs furniture with you. Expect it to draft candidates with
realistic content, render them in the furniture gallery
(`uv run python scripts/gallery/build.py`, written to the gitignored
`press-check/gallery/`) and in article previews, and iterate from your
reaction in the browser. You judge rendered pages, not CSS.

Owner-declared JavaScript or CSS libraries belong under `assets` in
`site.yaml`. They must use HTTPS and Subresource Integrity. Articles themselves
remain script-free. Prefer CSS and semantic HTML when they are sufficient.

The two components that need a real library ship with the engine: `nb.js`
loads KaTeX for equations and Prism for code listings, version-pinned,
SRI-hashed, and only on pages that carry the furniture, so most papers
declare nothing. Declare a library under `assets` for anything beyond them,
such as more Prism languages or a different typesetter. A press-declared copy
of a library the engine also ships wins: `nb.js` sees it in the page and
loads nothing. Readers with JavaScript off still get the raw content, the TeX
source of an equation and plain monospace code, and charts are plain PNGs
readable everywhere.

The proof also guards class names against likely typos. It builds an inventory
from `nb.css`, the composed `theme.css`, and every stylesheet declared under
`assets`, fetching each external sheet and verifying it against its pinned
integrity hash before counting its classes. Article markup naming a class no
inventoried stylesheet defines earns `W-DEAD-CLASS`; classes the engine's code
highlighting injects at runtime are known built-ins. When an external sheet
cannot be fetched or verified, the check suppresses itself for that run and
notes why instead of guessing. This is feedback, not a user-maintained
allowlist.
