# Furniture reference

Furniture is reusable article markup with a defined communicative purpose. The
shipped catalog is `templates/FURNITURE.md`, and its components work in every
template. Custom furniture has two scopes:

```text
press/furniture/          # shared, available to every series
├── catalog.md
├── styles.css
└── samples/<slug>.html

press/templates/<id>/     # bespoke to one template
├── furniture.md
├── furniture.css
└── samples/<slug>.html
```

A component's catalog entry is its contract: the purpose, the exact markup, and
the constraints. Production writers use only documented markup, never classes
inferred from a stylesheet, so an undocumented component goes unused.

## Requirements

- Use your own CSS prefix. `nb-` is reserved for the engine.
- Components must work without JavaScript, on narrow screens, in both themes,
  and for screen readers.
- The builder concatenates the selected theme and every furniture stylesheet
  into the published `assets/theme.css`, so a style change restyles the back
  catalog on the next build.

## The gallery

`uv run python scripts/gallery/build.py` renders every documented component with
its samples for inspection. Output lands under the gitignored `press-check/`.

## External libraries

Owner-declared JavaScript or CSS libraries belong under `assets` in `site.yaml`.
They must use HTTPS and Subresource Integrity. Articles themselves remain
script-free, and CSS with semantic HTML is preferred whenever it is sufficient.

The engine loads KaTeX for equations and one version-pinned Shiki module for
code listings only when those components appear. Shiki reads the code block's
`data-language` value. If the network or grammar is unavailable, the original
source stays visible. Other external assets declared by a press still require
HTTPS and Subresource Integrity. Static components, including Reading and Quote
cards, need no JavaScript.

The shared catalog contains Stat strip, Table, Figure, Equation, Code listing,
Note, Pull quote, Numbered steps, Timeline, Rubric, Reading card, and Quote
card. Position card, Holds-up grid, and Claim card remain styled for published
articles but are blocked by the proof in new articles. Give each Note an
article-specific label. Link to media as ordinary links. When a social post is
evidence, quote only the relevant words in a linked blockquote.

## The class inventory

The proof guards class names against likely typos. It builds an inventory from
`nb.css`, the composed `theme.css`, and every stylesheet declared under
`assets`, fetching each external sheet and verifying it against its pinned
integrity hash before counting its classes. Article markup that names a class no
inventoried stylesheet defines is reported as `W-DEAD-CLASS`. Classes that Shiki
injects at runtime are known built-ins. When an external sheet cannot be fetched
or verified, the check suppresses itself for that run and notes why instead of
guessing. The inventory is automatic, and there is no user-maintained allowlist.

See [Furniture](../guides/customize/furniture.md) for when and how to design
components, and [Site reference](site.md) for the `assets` key.
