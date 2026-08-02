# Furniture

Furniture is reusable article markup with a defined communicative purpose: a
timeline, comparison, evidence card, pull quote, rubric, or other reading aid.
Start with `templates/FURNITURE.md`. Its components work in every template.

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

A component makes specific information easier to understand than prose would.
Its catalog entry is its contract, giving the purpose, exact markup, and
constraints. Components must work without JavaScript, on narrow screens, in
both themes, and for screen readers. The furniture gallery renders every
piece for inspection: `uv run python scripts/gallery/build.py`, output under
the gitignored `press-check/`.

Owner-declared JavaScript or CSS libraries belong under `assets` in
`site.yaml`. They must use HTTPS and Subresource Integrity. Articles themselves
remain script-free. Prefer CSS and semantic HTML when they are sufficient.

The two components that need a real library ship with the engine: `nb.js`
loads KaTeX for equations and Prism for code listings, version-pinned,
SRI-hashed, and only on pages that carry the furniture, so most papers
declare nothing. Declare a library under `assets` for anything beyond them,
such as more Prism languages or a different typesetter. A press-declared copy
of a library the engine also ships wins: `nb.js` sees it in the page and
loads nothing. Readers with JavaScript off still get readable content: the
TeX source of an equation, plain monospace code, and charts as ordinary PNG
images.

The proof also guards class names against likely typos. It builds an inventory
from `nb.css`, the composed `theme.css`, and every stylesheet declared under
`assets`, fetching each external sheet and verifying it against its pinned
integrity hash before counting its classes. Article markup that names a class
no inventoried stylesheet defines is reported as `W-DEAD-CLASS`. Classes the
engine's code highlighting injects at runtime are known built-ins. When an
external sheet cannot be fetched or verified, the check suppresses itself for
that run and notes why instead of guessing. The inventory is automatic, and
there is no user-maintained allowlist.
