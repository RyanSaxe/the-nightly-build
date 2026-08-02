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

Treat each component as product design, not decoration:

1. State what information it makes easier to understand and when prose is
   better.
2. Design semantic markup, keyboard and screen-reader behavior, useful
   alternative text, and a no-JavaScript fallback.
3. Define responsive behavior, long-content behavior, and light/dark theme
   treatment.
4. Add an exact catalog example and a gallery sample.
5. Run the furniture gallery (`uv run python scripts/gallery/build.py`; it
   writes to the gitignored `press-check/gallery/`) and an article preview;
   inspect narrow and wide layouts, both themes, and realistic edge cases.
6. Iterate until the component improves comprehension in a representative
   article.

Owner-declared JavaScript or CSS libraries belong under `assets` in
`site.yaml`. They must use HTTPS and Subresource Integrity. Articles themselves
remain script-free. Prefer CSS and semantic HTML when they are sufficient.

The proof also guards class names against likely typos. It builds an inventory
from `nb.css`, the composed `theme.css`, and every stylesheet declared under
`assets`, fetching each external sheet and verifying it against its pinned
integrity hash before counting its classes. Article markup naming a class no
inventoried stylesheet defines earns `W-DEAD-CLASS`; classes the engine's code
highlighting injects at runtime are known built-ins. When an external sheet
cannot be fetched or verified, the check suppresses itself for that run and
notes why instead of guessing. This is feedback, not a user-maintained
allowlist.
