# Chart 1: the sign flip in the Chilean iron-fortified-formula trial's 10-year
# follow-up (Lozoff et al. 2012, Arch Pediatr Adolesc Med — this article's
# source 6). Healthy, full-term infants were randomized at 6 months to
# iron-fortified formula (12.7 mg/L) or low-iron formula (2.3 mg/L). At age
# 10, the trial scored 473 reassessed children on six measures: IQ, spatial
# memory, arithmetic achievement, visual-motor integration, visual
# perception, motor functioning. Each bar is the range (min to max) of the
# point difference across those six measures, iron-fortified minus low-iron
# group, for one subgroup, taken verbatim from the evidence record's Numbers
# section (no value here is estimated or interpolated):
#   Whole sample: 1.4-4.6 points LOWER for the fortified group -> -4.6 to -1.4
#   High hemoglobin at 6 mo (>12.8 g/dL, iron-replete): 10.7-19.3 points
#     LOWER for the fortified group -> -19.3 to -10.7
#   Low hemoglobin at 6 mo (<10.5 g/dL, lower iron status): 2.6-4.5 points
#     HIGHER for the fortified group -> +2.6 to +4.5
# Effect-size ranges (Cohen's d equivalent, also from the same source) are
# annotated on each bar as the paired, standardized figure.
import plotly.graph_objects as go

subgroups = [
    "Whole sample",
    "High Hb at 6 mo<br>(>12.8 g/dL, iron-replete)",
    "Low Hb at 6 mo<br>(<10.5 g/dL, lower iron status)",
]
low = [-4.6, -19.3, 2.6]
high = [-1.4, -10.7, 4.5]
es_labels = ["ES 0.13–0.21", "ES 0.85–1.36", "ES 0.22–0.36"]
bar_base = [min(l, h) for l, h in zip(low, high)]
bar_len = [abs(h - l) for l, h in zip(low, high)]
bar_colors = ["#4e5866", "#a8332e", "#008a74"]
label_pos = [l - 0.9 for l in low]  # whole sample, high-Hb: negative, label below
label_pos[2] = high[2] + 0.9  # low-Hb: positive, label above

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=subgroups,
        y=bar_len,
        base=bar_base,
        marker_color=bar_colors,
        width=0.5,
        showlegend=False,
    )
)

for i, (xs, yl, es) in enumerate(zip(subgroups, label_pos, es_labels)):
    fig.add_annotation(
        x=xs,
        y=yl,
        text=es,
        showarrow=False,
        font=dict(size=13),
        yanchor="top" if yl < 0 else "bottom",
    )

fig.add_shape(
    type="line",
    x0=-0.5,
    x1=2.5,
    y0=0,
    y1=0,
    line=dict(color="#68727f", width=1),
)

fig.update_layout(
    yaxis=dict(
        title="10-year point difference, iron-fortified minus low-iron formula<br>(range across 6 outcome measures)",
        range=[-22, 8],
        zeroline=False,
    ),
    xaxis_title="Hemoglobin subgroup at randomization, 6 months",
    showlegend=False,
)
