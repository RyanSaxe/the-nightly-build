# Writer handoff: tech-news/2026-08-13 (02, revision)

## What changed this round

Applied editor/01/editorial-review.md's two routed findings, resolved by
researcher/03/evidence.md. The editor's own direct edits to the article
(nb-meta and dekline rewrite; item 3 heading and "Reuters, carried by BNN
Bloomberg" body fix; item 4's closing sentence) are untouched — I edited only
the two spans the review routed to the writer and the researcher.

1. **Item 1 (Zoomsday) platform scope.** The draft's "exploiting both macOS
   and Android clients" understated what both opened sources state.
   Corrected to the two-tier claim researcher/03 establishes: the underlying
   flaw is present on all five Zoom clients (Windows, Mac, iPhone, Android,
   Linux), and the working exploit chain was specifically confirmed on four
   of those five (Windows, macOS, iOS, Android), with the fullest live
   demonstration on macOS. Also tightened the TechRepublic sentence to note
   it independently corroborates the same four-platform confirmed set (not
   Linux), matching the evidence record exactly.

2. **Item 4 (probiotics) secondary swap.** Replaced the Nature Podcast
   citation (`s9`, same-publisher, the editor's blocking finding) with China
   Science Daily / ScienceNet (news.sciencenet.cn, dated 2026-08-13),
   verified by researcher/03 as independent of both Springer Nature and East
   China Normal University in authorship and stake. Body prose now cites it
   for independent confirmation of the paper's findings plus one added,
   non-paywalled fact the record specifically flagged as useful color: the
   paper's roughly three-year review history at Nature (October 2023
   submission to August 2026 publication), which counters a "just announced,
   untested" reading without touching the still-missing effect-size figure.
   `data-nb-kind="secondary"` carried over unchanged; source numbering
   (`s9`, last-cited) was already correct in first-citation order and did not
   need to shift. No paywalled effect-size figure was invented; the editor's
   own closing sentence stating that gap is preserved as written.

## Proof result

`./nb check .nb-work/tech-news/2026-08-13/library/tech-news/2026-08-13.html --series tech-news --library /home/user/library-checkout`

BLOCK: 0, WARN: 0 (links checked). No warnings intentionally left.

`nb stamp` was run last at words=894, sources=9, reading_minutes=4.

## Confirmation

The editor's direct edits (dek/dekline rewrite, item 3 heading and body wire
attribution, item 4 closer) are preserved verbatim in the current file; this
revision did not revert or rephrase any of them.

## Open question

None blocking. Per researcher/03's Discarded section, three additional
Chinese-language outlets covering the same paper (科技日报/Science and
Technology Daily, Sina Tech, 163.com) were found but not opened — available
if the editor wants a second independent secondary on this item, but not
needed to clear the per-item or four-item floors.
