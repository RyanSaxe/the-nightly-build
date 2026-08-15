# Writer handoff: tech-news/2026-08-15 (writer/01)

## Original work

Checked all seven researcher candidates against this paper's own tech-news
coverage from the five prior days and found three of them — GPT-5.6-Cyber's
Chrome V8 finding, Meta's Muse Glimmer 30B, and Gemini 3.7 Flash's
Google-reported benchmarks — already reported there in near-identical detail
(same CVE, same parameter counts, same benchmark table), so the article drops
those three rather than repeat stale ground, keeps Gemini 3.7 Flash only for
the one independent benchmark (Artificial Analysis's GDPVal-AA v2) the earlier
coverage never carried, and fills out the four-item floor with the record's
weaker science candidate instead of re-running a covered story to hit a count.

## Selection notes

- Six commissioned candidates were real and evidenced, but three duplicated
  this paper's own August 11 and August 14 coverage of the same launches with
  no dated development since. Excluded on significance/freshness, not on
  source quality.
- Apple's China-model item was dropped outright: the evidence found no
  company-confirmed primary source at all, only a single Reuters origin
  republished across outlets. The tech-news series requires exactly one
  primary source per item (`per_item_sources: primary: [1,1]`); an item with
  no primary source cannot run here regardless of how the caveat is framed, so
  I did not relabel Reuters as primary to force it in.
- DeepSeek V4 Pro's benchmark table is presented as DeepSeek's own,
  unverified — the evidence's central caveat for that item, carried into a
  table caption plus a verbatim quote rather than repeating the vendor's
  numbers at face value.
- GPT-5.6-Cyber's "High" Preparedness Framework classification and Muse
  Glimmer's benchmark table were both weighed and cut: the underlying launches
  (Aug 10) are already told in the August 11 edition in comparable or greater
  detail, and neither had a dated development since to build on.

## Proof result

`./nb check --series tech-news .nb-work/tech-news/2026-08-15/library/tech-news/2026-08-15.html --library /home/user/library-checkout`
(links checked, after `nb stamp`): **BLOCK: 0, WARN: 0**, verdict
PUBLISHABLE. No warnings were left in place.

## Open questions

None. No evidence or voice decision is pending.
