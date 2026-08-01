# Publish an article now

You can commission an article with any useful starting point: a topic, a
question, a URL, a group of documents, or a detailed brief. For example:

> Write an article about birds for my paper today.

The request is not yet an article contract. The assistant should inspect the
press, choose an existing series and template, clarify only what materially
changes the piece, and turn the request into a rigorous configured commission.
Every article needs that home before production starts.

For an open series, add an `items` entry containing a stable slug and the
article-specific prompt. For a collection or sequence, add or select the
corresponding configured item. A `cadence: manual` series is a good home for
pieces that should never be scheduled automatically.

After the configuration change is validated on `main`, the assistant runs the
normal production chain: initialize with `nb start-article`, research and
draft, conduct editorial review, preview, and call `nb prepare-pr`. The result
is an ordinary Article PR with the same CI gate as a scheduled article.

A manual commission does not bypass source, artifact, rendering, or PR-shape
requirements. Its clean Article PR publishes automatically like any scheduled
article.
