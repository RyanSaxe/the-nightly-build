# This paper's shared furniture

## Word card (`rs-word-card`)

The opening definition for Word of the Day. The word and its lexical details
sit beside one plain definition, giving the smallest article in the paper a
clear visual point of entry. Keep the definition to one sentence and cite the
authority that establishes it.

```html
<div class="rs-word-card">
  <div class="rs-word-card-head">
    <span class="rs-word-term">WORD</span>
    <span class="rs-word-meta">
      <span class="rs-word-pos">PART OF SPEECH</span>
      <span class="rs-word-pronunciation">/PRONUNCIATION/</span>
    </span>
  </div>
  <p class="rs-word-definition">
    ONE PLAIN-SENTENCE DEFINITION.<sup class="nb-cite"
      ><a href="#s1">1</a></sup
    >
  </p>
</div>
```

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
