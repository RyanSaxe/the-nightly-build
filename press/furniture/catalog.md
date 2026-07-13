# This paper's shared furniture

Two components this paper adds on top of the engine's base catalogue
(`templates/FURNITURE.md`), styled in `styles.css` beside this file on the `rs-`
prefix (`nb-` is the engine's). They are shared: any section may reach for them,
so they live here rather than in one template's folder. A section that uses one
says so in its `prompt.md`. The engine concatenates this styles.css into
`assets/theme.css` on every build, so a class defined here restyles past articles
too.

## Code block (`rs-code`)

A real code listing with a header (file · language) and an optional cited
caption. The article writes plain `<pre><code class="language-python">`; Prism
(declared in `site.yaml` `assets:`, loaded on every page) highlights it into
`.token` spans and `styles.css` colors them. No-JS readers still get clean
monospace. Used by The Build.

```html
<figure class="rs-code">
  <div class="rs-code-head">
    <span class="rs-code-file">path/to/file.py</span><span>PYTHON</span>
  </div>
  <pre><code class="language-python">def attention(q, k, v):
    ...</code></pre>
  <figcaption class="rs-code-cap">
    Fig. 1 · What the listing shows.<sup class="nb-cite"
      ><a href="#s1">1</a></sup
    >
  </figcaption>
</figure>
```

## Case docket (`rs-docket`)

The standing facts of a legal matter as reference data, set apart so the prose
can argue instead of recite. Used by The Record.

```html
<div class="rs-docket">
  <span class="rs-docket-case">PARTIES, SHORT FORM</span>
  <span class="rs-docket-court">COURT · DOCKET NO.</span>
  <dl class="rs-docket-grid">
    <dt>Stage</dt>
    <dd>WHERE IT IS NOW</dd>
    <dt>Question</dt>
    <dd>THE LEGAL QUESTION IN ONE LINE</dd>
    <dt>Stakes</dt>
    <dd>WHAT TURNS ON IT, FOR WHOM</dd>
  </dl>
</div>
```

## Financial metrics (`rs-metrics`)

The numbers behind a business piece as reference data: a compact table of
metric, value, and change, so the prose can argue what the numbers mean
instead of reciting them. Cite the filing or release in the caption. Used by
The Ledger.

```html
<table class="rs-metrics">
  <caption>
    PERIOD, SOURCE.<sup class="nb-cite"><a href="#s1">1</a></sup>
  </caption>
  <thead>
    <tr>
      <th>Metric</th>
      <th>Value</th>
      <th>YoY</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>METRIC</td>
      <td>VALUE</td>
      <td>CHANGE</td>
    </tr>
    <tr>
      <td>METRIC</td>
      <td>VALUE</td>
      <td>CHANGE</td>
    </tr>
  </tbody>
</table>
```
