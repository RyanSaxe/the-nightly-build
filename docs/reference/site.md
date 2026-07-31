# Site reference

`press/site.yaml` owns paper-wide presentation and delivery settings.

```yaml
title: "My Paper"
theme: press/themes/my-paper.css
appearance: auto
front: compact
footer: "Filed while you slept."
assets:
  scripts: []
  styles: []
directory:
  description: "One line describing the paper."
  publish: true
```

| Key                     | Contract                                                 |
| ----------------------- | -------------------------------------------------------- |
| `title`                 | Required, non-empty masthead title                       |
| `theme`                 | Local CSS path; defaults to the shipped newspaper theme  |
| `appearance`            | `auto`, `light`, or `dark`                               |
| `front`                 | `compact` or `comfortable`                               |
| `footer`                | Optional non-empty imprint, at most 80 characters        |
| `assets.scripts/styles` | HTTPS resources with an exact Subresource Integrity hash |
| `directory.description` | Optional public description, at most 280 characters      |
| `directory.publish`     | Boolean; set `false` to opt out of the shared directory  |

External assets are owner-authored configuration. Scripts do not relax the
article sandbox: articles still cannot add scripts, handlers, frames, forms,
or other active content. Pin exact versions and preview both success and
no-JavaScript behavior.

See [Appearance and voice](../guides/customize/appearance-and-voice.md) for
design practice and [Delivery](delivery.md) for published URLs.
