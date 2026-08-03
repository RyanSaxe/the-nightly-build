# Draft handoff: paper-of-the-day/double-descent (writer 01)

## Original work

This piece reads Belkin and Nakkiran together with their three-paper
after-record (Curth; Nakkiran-Venkat-Kakade-Ma; Mei & Montanari) as one
argument about a single question the sources never pose in one place — whether
double descent is a law in parameter count — and shows, figure by figure, that
the effect is robust while that specific framing is contingent, tying Belkin's
coinciding norm-and-risk peaks (Fig. 2), Nakkiran's EMC surface (Fig. 3), Curth's
axis decomposition (Fig. 4), and the optimal-ridge curve (Fig. 6) to the same
verdict. The synthesis is visible in the last three sections and the Verdict note.

## Proof

`nb check ... --series paper-of-the-day --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamped words=2417 (band 1800-3400),
sources=8 (floor 8), reading_minutes=11. No warnings left standing.

## Assets

Six source assets captured with `nb asset pdf` from the free arXiv PDFs, each
inspected and cropped clear of printed page captions (subpanel captions kept
where they are themselves evidence, e.g. Nakkiran Fig. 4 a/b). Each figure's
`data-nb-locator`/`data-nb-url` points to the exact figure and PDF page of the
document actually linked. All figures render in place in the built preview.

## Equations

Two equations set with the equation furniture: a bare display for the
interpolation threshold (N = n; nK for K classes) and one annotated equation for
Effective Model Complexity (Nakkiran Def. 1, verbatim from p. 3), five colored
terms named in the legend. Both TeX strings, plus every inline-math span, were
validated against KaTeX 0.16.11 (the version nb.js loads) with throwOnError:true;
all compile. In this sandbox the CDN KaTeX is unreachable, so the offline preview
shows the documented raw-TeX fallback; production supplies KaTeX (press runtime
dependency) and nb.js enables `\htmlClass` (trust) with throwOnError:false.

## Steelman / register

Both sides carried without the banned "follow-up work disagrees" catalog device:
each critique is folded in where it changes the interpretation. Curth's x-axis
critique is scoped honestly to non-deep methods and explicitly does not touch
Nakkiran's ResNet/CNN/Transformer results. Label-noise dependence uses Nakkiran
Fig. 4 to show the peak survives without noise yet sharpens with it. The
misspecification-vs-nothing tension (Nakkiran vs Mei & Montanari) is left open,
not settled. Builder/reviewer register turn is signalled by the gate question
opening the "How much of it is the x-axis" section.

## One resolved judgment the editor should know (not a blocker)

Belkin's abstract card uses the **arXiv title and arXiv link**, not the PNAS
title the evidence suggested. Reason: the PNAS DOI returns HTTP 403 to the
link-checker (publisher bot-gating), which would BLOCK, and the brief's
figure-numbering note directs citing "the version whose URL you actually link."
The card's meta line still records the canonical venue ("arXiv:1812.11118,
published in PNAS 116(32) · 2019"), and only Belkin Fig. 1 and Fig. 2 are used,
both stable across the arXiv and PNAS numbering, so no locator conflict arises.

## Open questions

None blocking. Claim set was not expanded beyond the evidence record; the
supporting primaries read only at abstract level (Zhang, Hastie, Mei & Montanari,
Spigler) are each cited only for their recorded owned claim.
