# Draft handoff: tech-news/2026-08-06 (writer 01)

## Original work (one sentence)
This front page ranks the day's developments by how firmly each is established
rather than by AI salience, promoting a peer-reviewed long-COVID result above the
louder AI announcements, and it tags every interested-party number (SK hynix's
2.5x-per-watt figure, OpenAI's swarm-coordination narrative) with its
verification status in the clause where it lands, so a reader can tell measured
from claimed.

## Proof result
`./nb check ... --series tech-news --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings intentionally left; the
three W-SENTENCE-DENSITY notes raised during iteration were all resolved by
splitting the long sentences (HBF spec, DeepMind memo lead, OpenAI coordination).
Stamped words=829, reading_minutes=4, sources=12.

## Selection (4 items)
1. Anellovirus reactivation / long COVID (Immunology) — lead, by significance.
2. First open HBF standard at FMS 2026 (Memory & Storage).
3. Hassabis hands off day-to-day GDM; Jeff Dean departs (AI Leadership) — carries
   a role-mapping table built from the primary memo to keep the exact titles
   precise (defends the "DeepMind loses its CEO" imprecision).
4. OpenAI's Black Hat evaluation-agents debrief (AI Security) — kept only because
   the coordination / rebuilt-message-board / swarm detail is genuinely new
   beyond the recent agent-security editions; carried with caveats (OpenAI
   self-report, technical postmortem still pending).

K-EXAONE 2.0 was dropped: weakest candidate, ~5–6 days stale, and it re-treads
the open/closed-weights theme the 2026-08-05 edition already led with. The
"mark self-reports as claims" discipline still applies where it lands (SK hynix's
per-watt figure is attributed "it says"). Discarded June/July Nature papers were
not resurrected.

## Sourcing
Every item has exactly one owning primary plus at least one independent account
(items carry two independents each): Nature+MedicalXpress+UT Dell Med;
SK hynix+HotHardware+EE Times Asia; blog.google+Axios+CNBC;
OpenAI+Axios+SC Media.

## Open question (link integrity, for the editor)
The OpenAI primary (openai.com/index/hugging-face-model-evaluation-security-incident/)
returns HTTP 403 to scripted fetchers (TLS/HTTP-2 fingerprinting, not a dead
page). The engine's own link-checker classifies it non-blocking by design — a 403
means "you are a script," not "unreadable" — and a human reader opens it
normally, so the proof passes links-included with BLOCK 0. It is corroborated by
two openable independent accounts (Axios, SC Media). No action needed unless a
stricter downstream policy ever hard-fails on 403, in which case swap for an
openable OpenAI-owned copy or drop the item. Similarly, EE Times Asia (s6)
probes as "unverified" (connection error via the proxy, not a DNS failure), also
non-blocking; it corroborates only the consortium membership (Google,
Tenstorrent), a non-load-bearing detail.
