# The unbiased template's furniture

## The split (`nb-divide` + `nb-side`)

Exactly two positions across an accent spine on wide screens and stacked on
phones. Each position has a heading and an open argument area. The evidence
determines the structure within that area.

```html
<div class="nb-divide">
  <section
    class="nb-side nb-side-left"
    data-nb-section="POSITION-A-SLUG"
    id="POSITION-A-SLUG"
  >
    <h2>HEADING SPECIFIC TO THIS POSITION</h2>
    <div class="nb-side-argument">
      <p>
        EVIDENCE AND REASONING.<sup class="nb-cite"><a href="#s2">2</a></sup>
      </p>
    </div>
  </section>
  <section
    class="nb-side nb-side-right"
    data-nb-section="POSITION-B-SLUG"
    id="POSITION-B-SLUG"
  >
    <h2>HEADING SPECIFIC TO THIS POSITION</h2>
    <div class="nb-side-argument">
      <p>
        EVIDENCE AND REASONING.<sup class="nb-cite"><a href="#s3">3</a></sup>
      </p>
    </div>
  </section>
</div>
```

The shared accent shows the relationship between the positions. It is never a
color assigned to either side.
