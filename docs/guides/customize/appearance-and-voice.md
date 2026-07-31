# Appearance and voice

Paper-wide identity has two owners:

- `press/editorial.md` describes the reader, register, point of view, recurring
  editorial moves, and habits to avoid.
- `press/site.yaml` selects the masthead, theme, appearance, front-page density,
  footer, and directory settings. See [Site reference](../../reference/site.md).

Write editorial direction as decisions a writer can apply. Ground it in
specific examples and counterexamples; naming an outlet or asking for
"engaging" prose is not enough. Put paper-wide commitments here, series
territory in each `prompt.md`, and one-off angles in configured item prompts.

To create a custom theme:

1. Copy `engine/assets/themes/newspaper.css` to
   `press/themes/<name>.css`.
2. Edit every light, dark, and manual-override token block.
3. Keep chart colors distinguishable without color alone and check text and
   status contrast.
4. Set `theme: press/themes/<name>.css` in `site.yaml`.
5. Build a preview and inspect generated pages plus several old articles in
   both color schemes.

The builder republishes the selected theme as `assets/theme.css`, so theme and
furniture CSS restyle the back catalog. Template HTML keeps the font links it
was authored with; changing a font token alone does not install a web font.
