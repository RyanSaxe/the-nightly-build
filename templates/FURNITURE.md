# Furniture

The shared catalog gives articles a small set of reading aids. Choose a
component for the information it makes easier to read. Section structure,
citations, and sources follow the template and proof contracts, not this
catalog.

Each example below is rendered in the [gallery](../scripts/gallery/build.py).
The examples use the cited papers by Holtzman, Finlayson, and Vaswani. Adapt the
content and sources to the article. A press may add shared furniture in
`press/furniture/`; a template may add furniture for its own articles.

## Stat strip

Use a stat strip when a few figures carry the point. Put the source and meaning
in nearby prose; the strip is not a substitute for either.

```html
<div class="nb-stat-strip">
  <div class="nb-stat">
    <span class="nb-stat-n">2019</span
    ><span class="nb-stat-l">NUCLEUS SAMPLING PAPER</span>
  </div>
  <div class="nb-stat">
    <span class="nb-stat-n">2023</span
    ><span class="nb-stat-l">FOLLOW-UP ANALYSIS</span>
  </div>
</div>
```

## Table

Use a table for comparable rows. Keep explanations in prose cells and put the
source in the caption. The runtime wraps the table for horizontal scrolling on a
phone.

```html
<table class="nb-table">
  <caption>
    Two papers ask different questions about token truncation.<sup
      class="nb-cite"
      ><a href="#s1">1</a></sup
    ><sup class="nb-cite"><a href="#s2">2</a></sup>
  </caption>
  <thead>
    <tr>
      <th>Paper</th>
      <th>Year</th>
      <th class="txt">Question</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="nb-table-token">Holtzman et al.</span></td>
      <td>2019</td>
      <td class="txt">How does the decoding rule affect generated text?</td>
    </tr>
    <tr>
      <td><span class="nb-table-token">Finlayson et al.</span></td>
      <td>2023</td>
      <td class="txt">
        Why can truncating low-probability tokens improve text?
      </td>
    </tr>
  </tbody>
</table>
```

## Figure

Use a figure when the reader needs to see a diagram, chart, or source image.
State whether an illustration is conceptual. Give the image useful alternative
text and cite the source in the caption.

```html
<figure class="nb-figure">
  <img
    src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='800' height='300' viewBox='0 0 800 300'%3E%3Crect width='800' height='300' fill='%23f7f4ec'/%3E%3Ctext x='40' y='45' font-family='Arial' font-size='22' fill='%23212730'%3ENext-token choices%3C/text%3E%3Crect x='40' y='80' width='330' height='70' fill='%237e9eaf'/%3E%3Crect x='370' y='80' width='220' height='70' fill='%239bb6c4'/%3E%3Crect x='590' y='80' width='170' height='70' fill='%23d9c1ae'/%3E%3Ctext x='55' y='121' font-family='Arial' font-size='18' fill='%23172129'%3Ehigh probability%3C/text%3E%3Ctext x='385' y='121' font-family='Arial' font-size='18' fill='%23172129'%3Emiddle%3C/text%3E%3Ctext x='605' y='121' font-family='Arial' font-size='18' fill='%23172129'%3Etail%3C/text%3E%3Cpath d='M590 165v45H40' stroke='%23a24935' stroke-width='3' fill='none'/%3E%3Ctext x='45' y='243' font-family='Arial' font-size='18' fill='%23212730'%3EA truncation rule removes the tail before sampling.%3C/text%3E%3C/svg%3E"
    alt="Conceptual diagram of high-, middle-, and low-probability token choices; a truncation rule removes the low-probability tail"
  />
  <figcaption>
    Fig. 1 · Nucleus sampling excludes the low-probability tail before choosing
    a token. Diagram is conceptual, not a measured distribution.<sup
      class="nb-cite"
      ><a href="#s1">1</a></sup
    >
  </figcaption>
</figure>
```

## Equation

Use an equation when its terms matter to the argument. KaTeX typesets the TeX
when JavaScript loads; the TeX remains visible without it. Cite a sourced
equation in its caption or nearby prose.

```html
<p>The probability of a token depends on its score relative to the others.</p>
<figure class="nb-math">
  <div class="nb-math-eq">P(x_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}</div>
  <figcaption>
    Softmax turns token scores into a probability distribution.<sup
      class="nb-cite"
      ><a href="#s3">3</a></sup
    >
  </figcaption>
</figure>

<figure class="nb-math">
  <div class="nb-math-eq">
    \mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(
    \frac{\htmlClass{nb-mc1}{Q} \, \htmlClass{nb-mc2}{K^{\top}}}{
    \htmlClass{nb-mc3}{\sqrt{d_k}}}\right) \htmlClass{nb-mc4}{V}
  </div>
  <ul class="nb-math-legend">
    <li>
      <span class="nb-math-term nb-mc1">Q</span
      ><span>what each token is looking for</span>
    </li>
    <li>
      <span class="nb-math-term nb-mc2">K^{\top}</span
      ><span>what each token offers to be found</span>
    </li>
    <li>
      <span class="nb-math-term nb-mc3">\sqrt{d_k}</span
      ><span>the scale that keeps scores stable</span>
    </li>
    <li>
      <span class="nb-math-term nb-mc4">V</span
      ><span>the content mixed into the result</span>
    </li>
  </ul>
  <figcaption>
    Annotated terms make the operation readable without leaving the
    equation.<sup class="nb-cite"><a href="#s3">3</a></sup>
  </figcaption>
</figure>
```

## Code listing

Use a listing when the behavior of code is evidence. Put the language in
`data-language`, escape the source as HTML, and name the file or context in the
header. Shiki highlights it when available; plain source remains readable
otherwise.

```html
<figure class="nb-code">
  <div class="nb-code-head">
    <span class="nb-code-file">decoding.py · illustrative</span
    ><span>python</span>
  </div>
  <pre><code data-language="python">def nucleus(tokens, probabilities, threshold):
    ranked = sorted(zip(tokens, probabilities), key=lambda pair: -pair[1])
    kept, mass = [], 0.0
    for token, probability in ranked:
        kept.append(token)
        mass += probability
        if mass >= threshold:
            break
    return kept</code></pre>
  <figcaption class="nb-code-cap">
    Illustrative top-p selection: retain the smallest leading set whose
    cumulative probability reaches the threshold.<sup class="nb-cite"
      ><a href="#s1">1</a></sup
    >
  </figcaption>
</figure>
```

## Note

Use a note for a labeled explanation that interrupts the main argument. Name the
passage for its specific job. Do not add a repeated closing label to every
article.

```html
<aside class="nb-note">
  <span class="nb-note-label">Nucleus sampling</span>
  <p>
    At each step, the method keeps the smallest set of leading tokens whose
    combined probability passes a chosen threshold, then samples from that
    set.<sup class="nb-cite"><a href="#s1">1</a></sup>
  </p>
</aside>
```

## Pull quote

Lift a sentence from the article itself when it earns visual emphasis. A pull
quote adds no new claim or source.

```html
<div class="nb-pull">
  <p>
    The decoding rule can change the writing even when the model stays the same.
  </p>
</div>
```

## Numbered steps

Use steps for a process whose order matters. Keep an unordered collection in
prose or a list.

```html
<ol class="nb-steps">
  <li>
    <h3>Rank the tokens</h3>
    <p>
      Order candidate tokens by their model probabilities.<sup class="nb-cite"
        ><a href="#s1">1</a></sup
      >
    </p>
  </li>
  <li>
    <h3>Find the threshold</h3>
    <p>
      Keep the shortest prefix whose cumulative probability reaches the chosen
      value.
    </p>
  </li>
  <li>
    <h3>Sample</h3>
    <p>Choose the next token from that retained set.</p>
  </li>
</ol>
```

## Timeline

Use a timeline when dates explain the sequence. Each event needs a date and a
specific consequence.

```html
<ol class="nb-timeline">
  <li class="nb-tl-event major">
    <span class="nb-tl-date">2019</span>
    <h3>
      Holtzman and colleagues propose nucleus sampling<sup class="nb-cite"
        ><a href="#s1">1</a></sup
      >
    </h3>
    <p>
      The paper tests decoding strategies against the problem of repetitive
      generated text.
    </p>
  </li>
  <li class="nb-tl-interlude">
    <p>The later question is why removing the tail can help.</p>
  </li>
  <li class="nb-tl-event major">
    <span class="nb-tl-date">2023</span>
    <h3>
      Finlayson and colleagues revisit truncation<sup class="nb-cite"
        ><a href="#s2">2</a></sup
      >
    </h3>
    <p>The follow-up analyzes what a probability threshold excludes.</p>
  </li>
</ol>
```

## Rubric

Use a rubric for a review with named criteria. Each row has a `data-score` from
0 to 5, matching visible score text, and a cited reason.

```html
<div class="nb-rubric">
  <div class="nb-rubric-row" data-nb-criterion="repetition" data-score="4">
    <div class="nb-rubric-head">
      <span class="nb-rubric-name">Repetition evidence</span
      ><span class="nb-rubric-gauge"
        ><span class="nb-rubric-meter"><i></i></span
        ><span class="nb-rubric-score">4/5</span></span
      >
    </div>
    <p class="nb-rubric-note">
      The paper compares decoding methods on repetition, but its examples do not
      cover every writing task.<sup class="nb-cite"><a href="#s1">1</a></sup>
    </p>
  </div>
  <div class="nb-rubric-row" data-nb-criterion="truncation" data-score="3">
    <div class="nb-rubric-head">
      <span class="nb-rubric-name">Truncation account</span
      ><span class="nb-rubric-gauge"
        ><span class="nb-rubric-meter"><i></i></span
        ><span class="nb-rubric-score">3/5</span></span
      >
    </div>
    <p class="nb-rubric-note">
      The later analysis explains why truncation can help while noting that a
      threshold also removes tokens with nonzero true probability.<sup
        class="nb-cite"
        ><a href="#s2">2</a></sup
      >
    </p>
  </div>
</div>
```

## Reading card

Use this optional card to connect an article's point to specific sources. The
title and band label are yours to name. Name the point above the summary, then
say why each linked source is worth reading. "Further reading" is a useful
default, not a required label.

```html
<aside class="nb-reading-card">
  <p class="nb-reading-name">The decoding rule</p>
  <div class="nb-reading-rule" aria-hidden="true"></div>
  <p class="nb-reading-summary">
    Holtzman and colleagues found that changing how a model selects the next
    token changes its output, even when the model stays the same. They proposed
    nucleus sampling to avoid low-probability tokens.
  </p>
  <div class="nb-reading-band">
    <span class="nb-reading-label">Further reading</span>
  </div>
  <dl class="nb-reading-list">
    <dt>01</dt>
    <dd>
      <a href="https://arxiv.org/abs/1904.09751"
        >The Curious Case of Neural Text Degeneration</a
      >: why decoding changes repetition.
    </dd>
    <dt>02</dt>
    <dd>
      <a href="https://arxiv.org/abs/2310.01693"
        >Closing the Curious Case of Neural Text Degeneration</a
      >: why truncation can work.
    </dd>
  </dl>
</aside>
```

## Quote card

Reserve this card for a short quotation whose exact wording matters. Attribute
it in the footer. Put ordinary quotations in the prose.

```html
<figure class="nb-quote-card">
  <span class="nb-quote-mark" aria-hidden="true">“</span>
  <blockquote>
    <p>
      However, thresholds are a coarse heuristic, and necessarily discard some
      tokens with nonzero true probability as well.
    </p>
  </blockquote>
  <figcaption>
    Finlayson et al. ·
    <a href="https://arxiv.org/abs/2310.01693"
      >Closing the Curious Case of Neural Text Degeneration</a
    >
  </figcaption>
</figure>
```
