# Draft handoff: tech-news/2026-08-17 (writer 01)

## Original-work statement

This brief reads the week's two vulnerability-finding model launches as a single
governance event, OpenAI's gated GPT-5.6-Cyber set against Z.ai's soon-to-be-open
GLM-5.3, where the evidence record lists them as separate items, and it holds each
capability figure to the vendor that measured it.

## Proof result

`./nb check ... --series tech-news --library <checkout>` with links included:
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** `nb stamp` written (words 751,
reading 3 min, sources 9). No warnings left standing. Every citation href resolves
to the source's own page; the two Nature entries record the article URLs, not the
`idp.nature.com` login redirect.

## Design decisions worth the editor's eye

- Four items, all meeting the per-item floor (>=1 primary that owns the
  development + >=1 independent account). The lead is the cyber cluster carried
  across items 1 (OpenAI, gated) and 2 (Z.ai, open), not "another Chinese open
  model with self-reported benchmarks"; GLM-5.3 sits inside the governance story
  with its vendor numbers labeled as claims. Item 3's headline avoids the Aug 16
  "fits on a single GPU" mold and leads on Meta's return to open weights.
- No furniture. I considered a two-model cyber comparison table and an Aug 10-14
  "quiet window" timeline and rejected both: the two headline capability numbers
  (OpenAI's 95.0% exploit-chain completion, Z.ai's 84.5% CyberGym) measure
  different things, so a side-by-side table would imply a comparability that does
  not exist and risk laundering vendor scoreboards the evidence explicitly warns
  against; the timeline would only restate the four dated items. The wire-brief
  form carries the divergence and every provenance caveat in attributed prose.

## Open evidence / verification questions

- **OpenAI primary (s1) could not be re-fetched live.** `openai.com/index/gpt-5-6-cyber/`
  returns HTTP 403 to automated fetch (bot block, not a 404); the link check
  treats it as restricted and non-blocking. Its content rests on the researcher's
  read plus The Hacker News (s2) corroborating the reduced-safeguard posture. All
  OpenAI figures are stated as OpenAI's own and unverified.
- **Muse Glimmer secondary.** The evidence named independent outlets but supplied
  no URL. I verified Phoronix (s7) directly: it confirms 30B, Apache 2.0, single
  consumer GPU, Aug 10. It does not mention distillation, so the "distilled from
  Muse" and "return to open releases" framing is attributed to Meta's own post (s6)
  only. VentureBeat/Bloomberg were considered but bot-block automated fetch.
- **Nature items are gated (s8, s9).** Per the brief, no figures are stated: item 4
  carries only the abstract-level qualitative claim (improved glycaemic control and
  lipid profiles, preclinical, mice and non-human primates) and says plainly that
  effect sizes and colonization duration cannot yet be checked against the primary.
  Editor decision open: whether an unread primary abstract is sufficient grounding
  to keep the item, or whether it should wait for the paper text.
