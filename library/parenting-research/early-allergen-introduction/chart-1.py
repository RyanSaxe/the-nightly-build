# Chart 1: LEAP trial, peanut allergy at 60 months, intention-to-treat.
# Avoidance-arm and consumption-arm incidence are the trial's own reported
# rates (Du Toit et al., NEJM 2015, this article's source 1). The 81%
# relative-risk-reduction and 14.0-point absolute-risk-reduction annotations
# are computed from those two literals only: RRR = (17.2-3.2)/17.2, ARR =
# 17.2-3.2. No number here comes from any source but the trial itself.
import plotly.graph_objects as go

arms = ["Avoided peanut", "Ate peanut regularly"]
peanut_allergy_pct = [17.2, 3.2]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Peanut allergy at age 5",
        x=arms,
        y=peanut_allergy_pct,
        text=["17.2%", "3.2%"],
        textposition="outside",
        width=0.5,
    )
)

fig.update_layout(
    yaxis=dict(title="Infants with peanut allergy at age 5 (%)", range=[0, 22]),
    xaxis_title="LEAP trial arm, high-risk infants (n=640)",
    showlegend=False,
)

fig.add_annotation(
    x=0.5,
    y=20,
    xref="x",
    yref="y",
    text="14.0-point absolute drop · 81% relative reduction",
    showarrow=False,
    font=dict(size=13),
)
fig.add_shape(
    type="line",
    x0=0,
    x1=1,
    y0=18.5,
    y1=18.5,
    line=dict(color="#68727f", width=1, dash="dot"),
)
