# This paper's shared furniture

## Code block (`rs-code`)

Retired: the engine's `nb-code` (templates/FURNITURE.md) is this piece,
promoted upstream, with Prism shipped by `nb.js` itself. New articles use
`nb-code`; these styles stay so the published shelf keeps rendering.

## Case docket (`rs-docket`)

The standing facts of a legal matter as reference data, set apart so the prose
can argue instead of recite. Use when appropriate to highlight a court case.

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
