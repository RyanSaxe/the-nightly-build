# Publish an article now

You can commission an article with any useful starting point: a topic, a
question, a URL, a group of documents, or a detailed brief. For example:

> Write an article about birds for my paper today.

The request is not yet an article contract. Expect the assistant to inspect the
press, choose a series and template, clarify only what materially changes the
piece, and turn the request into a configured commission. Every article needs
that home before production starts. A fresh paper's Dispatches series takes any
request with no configuration change; other series admit articles by their mode.

What a home requires depends on the series mode:

- An open series on a schedule usually needs no configuration change: any new
  slug is admissible. When the series has a pending commission queue, add the
  article to `items` so it joins the queue. Adding an item is always a valid way
  to record the commission.
- A `cadence: manual` series admits any slug and is never scheduled. It is the
  natural home for pieces you ask for; its `items` are suggestions, not a gate.
- A collection takes any configured, unpublished item, adding one if needed. A
  sequence admits only its next unpublished item.
- A rolling series publishes one dated edition per UTC day, so publishing now
  means producing today's edition early. A second same-day edition is not
  possible.

Publishing now never consumes a future slot. The scheduled run skips a series
only when an article dated the same UTC day is already published, so a manual
article can stand in for that day's scheduled one. Tomorrow is never affected.

Once any configuration change is validated and merged into `main`, production
runs. The result is an ordinary Article PR through the same CI gate as a
scheduled article: no source, artifact, rendering, or PR-shape requirement is
bypassed, and a clean PR publishes automatically. Ask to read the article first
and the PR opens as a draft instead: CI validates it and nothing merges until
you mark it ready, which runs the check again and publishes.
