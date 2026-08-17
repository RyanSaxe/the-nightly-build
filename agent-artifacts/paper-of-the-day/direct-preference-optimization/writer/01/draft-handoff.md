# Draft handoff: paper-of-the-day/direct-preference-optimization (writer 01)

## Original-work statement

The article rebuilds DPO's derivation in a teaching order the paper itself does
not use — the shared RLHF objective, its closed-form optimum that no one can
evaluate, the reparameterization that reads a reward off the policy, then the
loss and gradient — and stages the paper's own preliminary out-of-distribution
result (Table 1) directly against Xu et al.'s later contrary reading, so that the
undisputed objective-level theorem and the contested practical question of what
offline DPO reaches are kept visibly separate. The evidence record supplies these
as a claim set; the reordering, the connected six-equation derivation ending in
the annotated DPO loss, and the side-by-side framing of the internal tension are
the article's own work.

## Proof result

`./nb check … --series paper-of-the-day --library <scratchpad>/library-checkout`
(links included): **BLOCK: 0, PUBLISHABLE.** Link verification ran and every
source URL resolved.

Warnings intentionally left (5, all W-SENTENCE-DENSITY, none in editable prose):

- One is the paper's abstract sentence in the `nb-paper-card` blockquote
  ("However, RLHF is a complex and often unstable procedure…"). The template
  requires the abstract verbatim, so it cannot be split.
- Four are the required display equations counted as "sentences": the annotated
  DPO loss (Eq. 7), the optimal policy with its partition-function definition
  (Eq. 4), the loss gradient, and the Bradley-Terry substitution (Eq. 6). The
  reconstruction demands these exact equations; the density score comes from the
  LaTeX token count, and the math cannot be broken up.

Every W-SENTENCE-DENSITY warning on actual prose was resolved by splitting; the
banned-term hit (`load-bearing`) was removed.

## Source floor / evidence question

Floor of 8 reached with all-primary sources, none padded: the DPO paper (s1); the
three derivation primaries the argument actually spends — InstructGPT/RLHF
(s2, arXiv 2203.02155), PPO (s3, arXiv 1707.06347), and the Bradley-Terry model
(s4, doi 10.2307/2334029); and four follow-ups (Xu s5, Tang s6, Azar/IPO s7,
Pal/DPOP s8).

Flag for the orchestrator/editor: the researcher's evidence record opened 6
sources (DPO plus IPO, KTO, Xu, Pal, Tang). To reach the floor honestly I added
the three derivation primaries (s2–s4), which the brief names as the legitimate
path to 8 and which the orientation and objective sections genuinely rest on; I
verified each by focused web fetch (titles, authors, resolving URLs) before
citing. KTO was in the evidence but left out on purpose: 8 was reached without it,
and adding a third alternative-loss method (with IPO and DPOP already present)
would have pushed the piece toward the survey the commission's boundary forbids.
If the editor would rather every cited source come through the evidence artifact,
the clean fix is a short researcher addendum recording s2–s4; the claims they
support are already standard and attributed in-text.

## Open voice/evidence questions

None blocking. The Anthropic-HH dialogue figure (Fig. 4 / paper Figure 3 left)
shows Best-of-128 above the 0.5 chosen-response line at the lowest temperature,
while the paper's own caption states DPO is the only method that improves over
chosen. I phrased the caption and prose to what the figure shows across
temperatures ("climbs above … and holds") and attributed the stronger "only
method" claim to the paper, rather than overstating from the single low-temperature
point. If the editor wants that softened further, it is a one-line caption change.
