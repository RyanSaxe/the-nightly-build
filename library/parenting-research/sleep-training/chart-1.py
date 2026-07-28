# Chart 1: the sleep-problem gap between intervention and control arms of the
# Melbourne "Infant Sleep Study" / "Kids Sleep Study" cohort, across every
# published follow-up of the same 328-family cluster RCT. Each pair of rates
# is the trial lineage's own reported parent-reported sleep-problem
# prevalence, taken verbatim from research.md's Numbers section:
#   10 months (Hiscock et al. 2007, Arch Dis Child, this article's source 3):
#     intervention 56%, control 68%
#   12 months (same paper, source 3): intervention 39%, control 55%
#   2 years (Hiscock et al. 2008, Pediatrics, source 4): intervention 27.3%,
#     control 32.6%
#   6 years (Price et al. 2012, Pediatrics, source 5): intervention 9.0%,
#     control 6.9% (the only timepoint where the intervention arm's rate is
#     the higher of the two, though the difference is not significant, P=.2)
# The gap plotted is control-minus-intervention, in percentage points, so a
# positive bar means the intervention arm had fewer reported sleep problems.
# No number here is estimated or interpolated; all are the trial lineage's
# own published rates.
import plotly.graph_objects as go

timepoints = ["10 months", "12 months", "2 years", "6 years"]
intervention = [56, 39, 27.3, 9.0]
control = [68, 55, 32.6, 6.9]
gap = [c - i for c, i in zip(control, intervention)]
labels = [f"{g:+.1f} pts" for g in gap]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Control minus intervention",
        x=timepoints,
        y=gap,
        text=labels,
        textposition="outside",
        width=0.55,
    )
)

fig.add_shape(
    type="line",
    x0=-0.5,
    x1=3.5,
    y0=0,
    y1=0,
    line=dict(color="#68727f", width=1),
)

fig.update_layout(
    yaxis=dict(
        title="Sleep-problem gap (control % minus intervention %, points)",
        range=[-4, 20],
    ),
    xaxis_title="Follow-up age, same 328-family cohort",
    showlegend=False,
)
