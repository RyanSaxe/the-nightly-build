# Reader and presentation

Assume a widely read audience with degrees in computer science and mathematics and
experience building machine learning systems in production. Introduce only the
subject-specific context needed to follow the work.

Write concisely and clearly. This audience learns by seeing, so show an idea
wherever it can be shown and use prose for what a visual cannot say. Keep the page
readable and the article free of filler.

Aim past the basic bar or line chart. Draw the mechanism itself: how the parts
connect, where a quantity comes from, what changes from one step to the next. Reach
for whichever of these fits, along with anything else in the furniture catalogs:

- Inline SVG inside `figure.nb-figure`, for a diagram drawn for the article. Set
  colors and fonts with theme variables in `style` attributes (`var(--ink)`,
  `var(--ink-soft)`, `var(--panel)`, `var(--chart-1)` through `var(--chart-6)`,
  `var(--sans)`) so the diagram follows the light and dark themes. Give the `svg`
  an `aria-label` saying what it shows and `style="width: 100%; min-width: 34rem;
  height: auto"`, with `style="overflow-x: auto"` on the figure, so its text stays
  readable on a phone.
- Plotly figures from `nb chart`, for anything computed: heatmaps, small multiples,
  surfaces, annotated plots.
- Figures captured from a source with `nb asset`, where the original shows the idea
  best.
- Annotated equations, with color-coded terms in an `nb-math` legend and every
  symbol defined, wherever the math is the point.

Look at every visual in the rendered article before handing it on. Overlapping
labels and arrows that stop short of their target are the common faults, and the
proof catches neither.
