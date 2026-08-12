# Draft handoff: paper-of-the-day/mixture-of-experts (01)

## Original-work sentence

The article reconstructs the 2017 noisy top-k gate and its two coefficient-of-variation
balancing losses directly from the paper's own equations, then reads that specific
balancing design against the seven-year follow-on record to separate what survived
(sparse top-k routing) from what was replaced (the k>1 premise, the two-loss balancing,
and the mixed-parallelism batch fix) — a separation the evidence record supplies as
scattered facts but never performs.

## Final proof result

`./nb check ... --series paper-of-the-day --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

No warnings intentionally left. All ten source URLs resolved, including the gated MIT
Press page for Jacobs et al. 1991 (s3), which the evidence flagged as returning 403 to
automated fetch; the link checker did not warn on it.

## Notes for the editor

- Capacity claim is anchored to the controlled comparison, per brief: the 6%-compute row
  and the same-compute 34.7 -> 28.0 drop on the 1B-word benchmark (Table 1, rebuilt as an
  `nb-table`), with the abstract's ">1000x" explicitly reframed as a capacity ceiling and
  the parameter gap on that benchmark stated as roughly thirtyfold (4.3B vs 151M). The
  131,072-expert / 137B model is placed on the separate 100B-word corpus, not conflated.
- Two source assets captured with `nb asset` from the paper PDF and inspected: Figure 1
  (asset-1.png, the layer schematic, gate selecting two of n experts with the unselected
  experts left inactive) and Figure 2 (asset-2.png, both perplexity-vs-capacity and
  perplexity-vs-compute plots with axis units and the log scaling noted). Table 2 is read
  in prose (BLEU 40.56 vs 39.22) rather than captured, and no other figures were brought
  in.
- Math is set with the equation furniture: softmax gate (Eq. 2), noisy top-k gate
  (Eqs. 3-5) as the single annotated equation, importance loss (Eqs. 6-7) and load loss
  (Appendix A), plus the Switch and GShard successor losses. Only the noisy-gate equation
  uses the colored-legend annotated form (one per article); the layer-output and
  successor-loss equations were converted to plain captioned equations.
- The load-loss equation was split across two `nb-math-eq` lines. The density check counts
  raw TeX (nb-math uses `div`, not a `math` tag, so it is not skipped), and the combined
  form tripped W-SENTENCE-DENSITY at 44 tokens; splitting it cleared the warning and let
  the Load(X) sum show explicitly.
- Follow-on is weighed honestly and left unresolved where the record is: Switch overturns
  the k>1 premise and collapses the two losses to one; GShard uses one l_aux; expert-choice
  removes the auxiliary loss by construction; loss-free balancing removes it and calls it
  harmful; DeepSeek-V3 is read to its abstract only (671B/37B, auxiliary-loss-free);
  DeepSeekMoE retains collapsed auxiliary losses. The expert-choice autoregressive-decoding
  limitation was left out as unverified, per the evidence record.

## Open questions

None blocking. All required claims were available in the evidence record; no researcher
request is owed.
