# Voice guide: feature/binance-hack-freeze (01)

## How this piece should sound

The register is an engineer who has read the contracts and the postmortems and is telling a peer what they found. The reader has a CS or math degree and has shipped production systems, so nothing is softened and nothing is explained twice. A term such as blocklist, issuer, native asset or tracing gets one plain definition where it first matters, and from then on it is the same word every time. Wit, where it appears, comes out of the mechanism itself and costs the reader nothing to follow.

Cloudflare's postmortem shows how to open on a finding and then refuse the tidy version of it. The writer states the cause in one sentence and then says the story is more complex than that sentence. This incident has a similar tidy version ("the freeze recovered about half"), and the material may call for saying what that figure leaves out and then showing it. The same piece shows how to report an early guess as a guess. The attack theory is stated as speculation, and then the evidence that dismissed it is listed with its source: CPU data, `strace`, error logs. An attribution to a named group can be handled the same way. Give the analyst's assessment in the analyst's own words with the confidence level it states, say what it rests on, and keep it visibly separate from what the chain data establishes. Binance's account of the breach path is an initial finding and reads that way. Neither exemplar here covers a named-actor attribution directly, so this is an extension of what the Cloudflare passage does with a theory, not a copy of a demonstrated move.

Samczsun shows how to explain a mechanism to someone who can read code. He names the exact function, says what the callee controls and what the caller assumed, and then runs one concrete case through to a number (39 masks where 20 were allowed). A freeze can be carried the same way: what the issuer's contract can do to an address, what it cannot do to a balance of a native asset, and one traced path followed to the point where the two diverge. He also lets a short rueful remark stand where the design is at odds with its own name, without commenting on it afterwards.

Patrick McKenzie shows how to handle financial plumbing without borrowing its jargon or inflating it. A definition is given in one sentence and in the plumbing's own terms, and a dry remark carries the judgment ("Boring is a feature!"). On provenance, he states plainly what the ledger does not record. That is useful here for the difference between what an address holds, what an analyst believes about who controls it, and what an issuer is willing to act on. His note that cross-chain swaps are how heist proceeds leave the system is general background and says nothing about this incident.

Where the material calls for it: put a comparison or a figure beside a number the reader already holds, rather than reaching for an adjective. Leave unsettled figures unsettled and say who owns each one. Treat the person who made the decision (the issuer, the exchange, the analyst) as a person making a decision with a reason, and let the reader judge it. The piece is short, so most of these will not be needed. The first one to reach for is the finding stated flatly and the mechanism that explains it.

## Patrick McKenzie, "Stablecoin mechanisms and use cases" (Bits about Money)

Source: https://www.bitsaboutmoney.com/archive/stablecoin-mechanisms-and-use-cases/

> "A stablecoin is designed to be a deposit (i.e. money) recorded in a slow database which is negotiable among other actors who use the same slow database."

Checked: https://www.bitsaboutmoney.com/archive/stablecoin-mechanisms-and-use-cases/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
A definition in one sentence, using the reader's own vocabulary (database, negotiable), which lets an engineer reason from it. The person is in the choice of "slow database", a phrase that carries the comparison to banks without arguing for it.

> "The money market model is, relative to other ways to construct stablecoins, boring. Boring is a feature! Boring means that the stablecoin operator can’t get seigniorage income through digital alchemy. Boring also means that the stablecoin is unlikely to see its value vaporized under conditions of market stress."

Checked: https://www.bitsaboutmoney.com/archive/stablecoin-mechanisms-and-use-cases/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
The judgment is dry, repeated once, and then cashed out in two concrete consequences. The exclamation is the only flourish, and the next two sentences say what it means.

## Patrick McKenzie, "Money laundering and AML compliance" (Bits about Money)

Source: https://www.bitsaboutmoney.com/archive/money-laundering-and-aml-compliance/

> "Paper bills don’t have an endorsement, and databases don’t hold a column, that says certain money has been laundered or not. That is a necessarily subjective belief held by certain actors about a consequence of the action of others."

Checked: https://www.bitsaboutmoney.com/archive/money-laundering-and-aml-compliance/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
He separates what the system records from what some actors believe about it, and says exactly whose belief it is. The writer is visible in the "databases don't hold a column" step, which an engineer can check against how a ledger works.

> "These days we sometimes see echoes of it in e.g. cryptocurrency heists, where criminals might swap assets between various chains before attempting to exfiltrate from the cryptocurrency ecosystem(s) to money."

Checked: https://www.bitsaboutmoney.com/archive/money-laundering-and-aml-compliance/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
One sentence connects a general mechanism (layering) to the present case, with "sometimes" and "might" used where the claim is general. It is quoted for how it scopes the claim and not for anything about this heist.

## samczsun, "The Dangers of Surprising Code"

Source: https://samczsun.com/the-dangers-of-surprising-code/

> "Well, one reason might be our old friend reentrancy, or as I've been trying my hardest to rebrand it to: unsafe external calls. Recall that any external call is potentially unsafe if the recipient is attacker-controlled because the attacker may be able to cause your contract to transition into an undefined state."

Checked: https://samczsun.com/the-dangers-of-surprising-code/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
He renames a familiar bug to say what it is, then states the condition under which it applies. The person is the aside about trying to rebrand it; the rule that follows is exact enough to be tested.

> "If we do this, we'll reenter the function after only one mask has been minted, which means we can request to mint another 19 masks. This results in a total of 39 masks being minted, even though the maximum allowable was only 20."

Checked: https://samczsun.com/the-dangers-of-surprising-code/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
A mechanism walked through one case to a count, with the limit and the result side by side. The sentences are plain, in the first person plural, and the arithmetic is left for the reader to check.

> "It turns out that in this case, these functions are more of the latter and less of the former. This is especially unfortunate because given the choice between transfer and safeTransfer, why wouldn't you pick the safe one? It's in the name!"

Checked: https://samczsun.com/the-dangers-of-surprising-code/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
The wit comes from the function names themselves, and the next paragraph goes straight on to the cost. This is the one kind of joke the genre can hold: one that depends on the subject's own nouns.

## John Graham-Cumming, "Details of the Cloudflare outage on July 2, 2019"

Source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/

> "Although the regular expression itself is of interest to many people (and is discussed more below), the real story of how the Cloudflare service went down for 27 minutes is much more complex than “a regular expression went bad”."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
The proximate cause has already been stated, and here the writer says it is not the whole account and promises the longer sequence. A named person writes it in the first person, and the duration is given as a figure.

> "In the initial moments of the outage there was speculation it was an attack of some type we’d never seen before."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
An early theory is reported as speculation, and its holders are not named or mocked. The writer is present in the account but does not endorse the theory.

> "At 14:00 the WAF was identified as the component causing the problem and an attack dismissed as a possibility. The Performance Team pulled live CPU data from a machine that clearly showed the WAF was responsible. Another team member used strace to confirm. Another team saw error logs indicating the WAF was in trouble."

Checked: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/ (raw HTML via curl, tags stripped), retrieved 2026-11-02
The dismissal of the theory comes with the independent evidence that did it, each item in its own short sentence and attributed to a team and a tool. Tool names (`strace`) are used as a practitioner would use them.
