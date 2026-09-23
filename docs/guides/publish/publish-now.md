# Publish an article now

You can commission an article with any useful starting point: a topic, a
question, a URL, a group of documents, or a detailed brief. For example:

> Write an article about birds for my paper today.

The request is not yet an article contract. Expect the assistant to inspect the
press, choose a series and template, clarify only details that materially change
the article, and record the request as a commission. Every article needs a
series before production starts. A fresh paper's Dispatches series accepts any
request without a configuration change. Other series accept articles according
to their mode.

Choose a series according to its mode:

- An open series on a schedule usually needs no configuration change: any new
  slug is admissible. When the series has a pending commission queue, add the
  article to `items` so it joins the queue. Adding an item is always a valid way
  to record the commission.
- A `cadence: manual` series admits any slug and is never scheduled. Use it for
  requested articles. Its `items` field suggests topics and does not restrict
  commissions.
- A collection takes any configured, unpublished item, adding one if needed. A
  sequence admits only its next unpublished item.
- A rolling series publishes one dated edition per UTC day, so publishing now
  means producing today's edition early. A second same-day edition is not
  possible.

Publishing an article early does not consume a future slot. The scheduled run
skips a series only when an article dated the same UTC day is already published.
A manual article can therefore serve as that day's scheduled article. It does
not affect the next day's run.

Once any configuration change is validated and merged into `main`, production
runs. The result is an ordinary Article PR through the same CI gate as a
scheduled article: no source, artifact, rendering, or PR-shape requirement is
bypassed, and a clean PR publishes automatically. Ask to read the article first
and the PR opens as a draft instead: CI validates it and nothing merges until
you mark it ready, which runs the check again and publishes.
