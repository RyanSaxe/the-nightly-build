# Writer handoff: tech-news/2026-08-13 (01)

## Original work

Where the evidence record hands over four separately-verified developments,
this draft reads each one for the frame its own best secondary source
supplies rather than the vendor's or discoverer's framing alone — TechRepublic's
"capability story before a product-security one" for Zoomsday, TechCrunch's
read of Glimmer as a map of Meta's open/closed boundary, and The Next Web's
cost-per-token framing for the IBM/Together deal — and orders the four by
that reading of significance (security capability shift, then open-model
capability, then compute economics, then early-stage science with an
explicitly flagged evidence gap), rather than by source-count or recency.

## Proof result

`./nb check .nb-work/tech-news/2026-08-13/library/tech-news/2026-08-13.html --series tech-news --library /home/user/library-checkout`

BLOCK: 0, WARN: 0 (links checked). No warnings intentionally left.

`nb stamp` was run last at words=813, sources=9, reading_minutes=4.

## Sourcing decisions worth flagging

- Zoomsday and Muse Glimmer each had two candidate primary sources in the
  evidence record (A Security's writeup + Zoom's own bulletin; Meta's
  research-blog post + Meta's developer/model-card page). `per_item_sources`
  requires exactly one primary per item, so I kept the source that owns the
  actual development being reported (A Security's discovery; Meta's research
  blog) and did not cite the second primary-kind document. This meant
  dropping Zoom's own CVSS/severity score from the piece, since it was
  established only in the bulletin I chose not to cite — I did not substitute
  an unsourced severity claim.
- The probiotics item's independent secondary is Nature's own podcast page —
  editorially separate from the paper's authors but sharing a publisher with
  the primary, exactly as the evidence record flags. It is honestly labeled
  secondary and clears the per-item floor, but it is the weakest secondary
  in the piece; if an outside-Nature secondary can be found before
  publication, it would strengthen this item's sourcing meaningfully. I did
  not invent the paywalled effect-size figures; the item states plainly that
  the exact glucose/HbA1c magnitude is unpublished here.
- The Nvidia $500B financing item is not in this draft, per the researcher's
  and brief's freshness call (same August 10 MOU, no August 13-adjacent
  dated development).

## Open question

None blocking. The one editorial judgment worth a second look: whether the
probiotics item's single same-publisher secondary is strong enough for this
paper's bar, or whether the editor would rather hold it for a stronger
outside secondary.
