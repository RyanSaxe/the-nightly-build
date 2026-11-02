# Editorial review: feature/binance-hack-freeze (editor/01)

## Correct

Thesis, from the draft alone: how much of a crypto theft a freeze can claw back
is fixed by two things, the share of the haul held in tokens that have an issuer
or administrator who can freeze an address (here overwhelmingly stablecoins) and
how fast the thief swaps out of those tokens before the freezes land. Binance's
stablecoin-heavy haul saw 44% frozen or seized; Bybit's 2025 all-native haul saw
under 4%.

The claims under it:
1. About $6.3B to $6.43B left Binance on 29 October; Elliptic counts $3.46B of
   its $6.43B as stablecoin.
2. A stablecoin contract carries an owner-only blocklist checked on transfer;
   un-administered assets (BTC, XRP, SOL, NEAR) have no such switch, and the
   administered non-stablecoin exceptions are small ($36M).
3. $2.85B was frozen or seized (Elliptic, 44%), 94% of it stablecoin.
4. The attacker converted about $786M of stablecoins into ETH and TRX before the
   freezes, so about 77% of the stolen stablecoin was frozen against about 6% of
   everything else; speed, not only composition, set the gap.
5. Bybit 2025 was about $1.5B, all ETH and staking derivatives, under 4% frozen.

How each held. I tried hardest to break the freeze-ceiling claim, the one the
piece is built on. It holds, and it is honestly qualified where it is thin.
Three things could have sunk it and do not: the 44% mixes a theft-time
denominator ($6.43B) with a frozen figure at 1 November prices ($2.85B), but the
piece attributes the 44% to Elliptic, who computes it that way and owns it, and
does not present it as the paper's own arithmetic. The contrast conflates
composition with speed, and the piece says so in its own words rather than
hiding it. Elliptic has a commercial stake in a traceability narrative, and that
is carried in the source note. The comparison axis in Fig. 3 puts Bybit's
share-of-ETH beside Binance's share-of-dollars, which is fair only because
Bybit's haul was near-homogeneous ETH; the caption states the Bybit basis.

Reopened sources. I reopened Elliptic's page and confirmed its attribution word
is verbatim "likely" ("TraderTraitor as the likely perpetrator", "assessed this
as likely", "the likely culprit"), so the quoted "likely" in the attribution
table is the holder's own word, not a paraphrase dressed as a quote. I confirmed
on the same page the $786M, $3.46B, $2.85B, 94% and $3.25B figures as printed.
Teng's X post is login-gated (HTTP 402 to every client I have, as the researcher
also found), so I could not reopen it; the quoted "Our investigation has not
attributed responsibility to any individual" matches the evidence record's
Contradictions entry verbatim, the researcher read the full post directly, and
the orchestrator's query decision treats "Binance has not attributed" as
settled, so it stays, with the gating noted here.

Figures against denominators. Fig. 2's derived split reconciles: frozen
stablecoin 0.94 x $2.85B = $2.68B, which is $2.68B / $3.46B = 77%; non-stablecoin
frozen $2.85B - $2.68B = $0.17B against stolen $6.43B - $3.46B = $2.97B = 6%; the
two stablecoin segments sum to $3.47B against $3.46B stolen, within the stated
rounding. The caption states the price-date mixing and the one point of rounding
error and claims no precision past whole percents. No false precision.

data-nb-kind. Every tag survives the primary/secondary test. The two the writer
flagged are both held to secondary and neither is dressed as an independent
primary: Bybit's 0%-stablecoin composition rests on Block Scholes (secondary,
reading the chain) and the FBI attribution row rests on BleepingComputer
(secondary, because the FBI's own page is behind a bot challenge), and the table
row and source note say so.

The one break I made a change for: the body read "counted 3.84% frozen on 21
April 2025, up from 3% in early March, as Decrypt reported", which puts both
numbers inside Decrypt's report. Only the 3.84% (21 April) is on the cited
Decrypt page; the 3% is Zhou's earlier count carried through coverage the
researcher did not open. I moved the Decrypt attribution and its citation to sit
against the 3.84% and left "up from 3% in early March" as Zhou's own earlier
count, which is what the evidence and the source note support. No number changed.

Totals read as ranges with their owners ($6.3B Binance, $6.36B TRM, $6.43B
Elliptic; frozen $2.7B to $3B). The breach path reads as Binance's initial
finding, posted and then walked back within 70 minutes to "additional points of
breach". The attributions are presented as assessments with each holder's
confidence word, set apart from the chain data by their own table and the line
"These are assessments, not a court finding". Headline, dek and subheads carry
no wrong label: $6.43B, 44%, 54%, 3.84% and the co-CEO title all match their
owning documents.

## Reads well

Little had to go. The piece was already cut close to the mechanism, and the
edges hold up read alone and out of order. The opener states the finding flatly
("A freeze reaches only tokens that have an issuer, and only those the thief has
not yet swapped out"), which is the register the voice guide asks for, and the
article's last sentence lands on the concrete beyond-reach split rather than a
moral. I ran the placeholder test on every best-line-in-paragraph candidate.
"Two thefts are not a rule, but the mechanism in Fig. 1 predicts the order"
survives it: it is a real qualification about a sample of two, not performed
carefulness, and the clause after it does the piece's own work. The how-to-read
line before Fig. 2 is the series form, not filler. I found no sentence carried
over from the briefing or the voice-guide exemplars, no banned dek mold, and no
heading built to a scaffolding slot; the five headings are distinct steps of
this argument in its own nouns.

## The experience

Read from the top, the page earns its three visuals. Fig. 1 draws the mechanism
the prose describes, three asset outcomes with the swap-before-the-flag path
marked, and at phone width the labels sit inside their boxes and every arrow
reaches its target. Fig. 2 is the finding itself, the stablecoin and
non-stablecoin bars split into frozen, swapped-out and not-frozen, and Fig. 3 is
the Bybit contrast that carries the argument. The writer went by asset type and
by haul, not by chain, so the by-chain trap the commission warns about never
arises. No chart drags or restates a neighbour.

What the piece gives beyond its sources: it sets the Binance and Bybit hauls side
by side by composition and splits the Binance stablecoin side into frozen versus
swapped-out-first, so the freeze ceiling reads as a joint function of the
issuer-administered share of a haul and the speed of the thief's exit. That is
the writer's original-work sentence, and the page shows it rather than asserting
it.

## Edits

- Repositioned the Decrypt attribution and its citation in the Bybit paragraph so
  "as Decrypt reported" and source 11 bind only to the sourced 3.84% (21 April
  2025), leaving "up from 3% in early March" as Zhou's own earlier count; no
  number altered, net-zero words.

## Decision

approve. The freeze-ceiling finding survived every break I could put to it and is
qualified where it is thin; the one attribution defect is fixed, the figures
reconcile against their denominators, all three visuals render clean, and the
proof passes BLOCK 0 / WARN 0 at 1182 of 1200 words.
