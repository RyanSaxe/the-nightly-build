# Appearance and voice

Paper-wide identity has two owners:

- `press/editorial.md` describes the reader, register, point of view, recurring
  editorial moves, and habits to avoid.
- `press/site.yaml` selects the masthead, theme, appearance, front-page density,
  footer, and directory settings. See [Site reference](../../reference/site.md).

Write editorial direction as decisions a writer can apply. Ground it in
specific examples and counterexamples. Naming an outlet or asking for
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
was authored with, so changing a font token alone does not install a web font.

Themes, furniture, and templates are yours to define in `press/` with no
engine edit. The site's frame is not: the top navigation, the front-page
layout, and how each series-page mode renders are fixed by the engine. A new
navigation entry or a different front page is an engine contribution, which
takes the fork off the conflict-free `press/`-only update path.

## Banned terms: press/banned-terms.yaml

The proof counts every article against a list of ruled-out strings. Each
entry carries the exact strings to match, the most uses an article may keep,
and the note the writer sees when the count runs over. The engine seeds the
list in `spec/banned-terms.yaml`. An over-limit count is a `W-BANNED-TERM`
warning, promoted to a block when the series sets `strict`. Counting covers
the rendered text (title, dek, headings, body) minus the sources section,
case-insensitively, so "leverage" also catches "leveraged".

Your press layers `press/banned-terms.yaml` over the seed, by `id`:

```yaml
# A new id adds a ban. State every field: the strings to count, the
# ceiling, and the note the writer acts on.
- id: synergy
  terms: [synergy, synergies]
  max: 0
  suggestion: name the mechanism; what does the combination actually do?

# Reusing an engine id changes only the fields you state.
- id: em-dash
  max: 8

# Retire an engine entry outright.
- id: leverage
  enabled: false
```

Write each `suggestion` as the correction you would give a writer. A synonym
swap keeps the underlying problem, so point the note at rewriting the
sentence, not replacing the word. `nb validate` checks both files, so a typo
surfaces before a scheduled run trips on it.
