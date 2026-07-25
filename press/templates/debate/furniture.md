# The debate template's furniture

## The debate (`rs-debate` + `rs-debate-position`)

Exactly two positions share the page. Each position has a heading and an open
argument area; the evidence determines the structure inside that area.

```html
<div class="rs-debate">
  <section
    class="rs-debate-position rs-debate-position-left"
    data-nb-section="POSITION-A-SLUG"
    id="POSITION-A-SLUG"
  >
    <h2>HEADING FOR THIS POSITION</h2>
    <div class="rs-debate-argument">
      <p>
        EVIDENCE AND REASONING.<sup class="nb-cite"><a href="#s2">2</a></sup>
      </p>
    </div>
  </section>
  <section
    class="rs-debate-position rs-debate-position-right"
    data-nb-section="POSITION-B-SLUG"
    id="POSITION-B-SLUG"
  >
    <h2>HEADING FOR THIS POSITION</h2>
    <div class="rs-debate-argument">
      <p>
        EVIDENCE AND REASONING.<sup class="nb-cite"><a href="#s3">3</a></sup>
      </p>
    </div>
  </section>
</div>
```

The shared accent is page structure, not a color assigned to either position.
