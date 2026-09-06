# Writer brief · 01

## Inputs

- `editorial-direction.md`
- `commission.md`
- `writing-coach/01/voice-guide.md`
- `researcher/01/evidence.md`
- `library/current-events/2026-09-06.html`
- `templates/brief/manifest.yaml` and `templates/brief/skeleton.html`

## Output

Write the finished article to `library/current-events/2026-09-06.html`.

## Contract

- Keep the brief at four `data-nb-item` blocks under the `items` section.
- Replace all skeleton placeholders. Set title, dek, date, tags, source count,
  word count, reading time, harness, and model in `nb-meta`.
- Link each headline to its primary source. Place citations immediately after
  every sourced claim and include both source kinds in the Sources list for
  each item.
- Use a stat strip only in the jobs item, with exact BLS figures and nearby
  citations. Keep the entire page concise enough to remain a brief.
- Preserve the template's section names and source markup. Do not add an
  unsupported conclusion or a generic sign-off.

## Proof required

Before handing off, validate every number and procedural verb against
`researcher/01/evidence.md`, ensure the two court items retain their interim
posture, and run a placeholder search over the HTML. The writer handoff should
state the final item count, source count, and any remaining uncertainty.
