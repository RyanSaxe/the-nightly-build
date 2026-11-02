# researcher brief: feature/binance-hack-freeze (01)

Inputs:
- editorial-direction.md (one dir up): the full standing editorial standard.
- ../../commission.md: the story, the angle, and what the piece must establish.
Output: evidence.md in this directory (/home/user/the-nightly-build/.nb-work/feature/binance-hack-freeze/agent-artifacts/feature/binance-hack-freeze/researcher/01/evidence.md)

Work from these inputs. Do not tour the repository, the Git history or the archive for background. Where something you need is missing, ask me.

This is a live incident (29 October 2026) and the figures are days old and
provisional. Correctness is the one rule nothing loosens. Open every source you
cite and read the passage; record the owning document, not coverage of it.

Establish, from owning documents where possible:

1. The total stolen and its timing: Binance's own stated figure and TRM Labs'
   tracing figure (~$6.3B / ~$6.36B), the date and that most moved in a short
   window, and the chains involved. Give the range each owner states; do not
   average them into a single false-precise number.
2. The breach path: Binance's stated initial finding (compromised DevOps
   engineer's laptop -> service container -> unauthorized withdrawals). Attribute
   to Binance as an initial finding that may be revised. Get Binance's own wording.
3. The freeze: how much has been frozen and by whom (Tether, Circle, other
   issuers), ideally with each issuer's own announcement. The piece's core claim is
   the **asset/chain composition** of (a) the stolen haul and (b) the frozen
   amount, to show the frozen share is dominated by issued stablecoins and the
   un-freezable share by native assets (BTC, ETH, SOL, BNB). Pin down whatever
   composition data exists (e.g. TRM or analytics breakdown: ETH ~$3.8B, ~18,270
   BTC ~$1.5B, etc.) and mark clearly what is firm vs provisional. If the per-asset
   split of the *frozen* amount cannot be sourced, say so in Limits and the writer
   will narrow the claim.
4. The freeze mechanism, independent of this incident: that USDT (Tether) and USDC
   (Circle) contracts carry an issuer freeze/blocklist function and that issuers
   have used it before (give a prior documented freeze and, if findable, the
   contract function name), and that native/permissionless assets have no
   equivalent. This is checkable regardless of this incident's provisional numbers
   and is what explains the split.
5. Attribution: TRM Labs' assessment that the North Korean group
   (TraderTraitor/Lazarus) is responsible, in TRM's own words and marked as a
   high-confidence assessment, not a confirmed legal finding. Record any
   contradiction or any party disputing it.
6. Comparison: the Bybit 2025 hack figure (~$1.5B) as the prior record, from a
   source that owns that number.

Record Sources / Contradictions / Numbers / Limits / Source assets / Discarded per
the researcher skill. For every figure the argument depends on give exact reading,
owner, scope and period. Classify each source primary/secondary with the reason
(Binance owns its own figures and breach finding; TRM owns its tracing and
attribution; issuers own their freezes; news outlets are secondary). Search for
what would sink the angle (e.g. a large frozen amount that is NOT stablecoin, or a
claim that native assets were in fact clawed back) and record it in full. Confirm
every URL resolves to the document's own page; a 403/paywall means gated, so try a
browser request before giving up. In Source assets, note any exact visual (a TRM
chart of the outflow, an issuer's freeze post) that could carry the argument better
than prose, and what a crop must keep. Report the path and the record's most
important limit, and tell me directly if the evidence undermines the freeze-ceiling
angle.
