import plotly.graph_objects as go

# Realized-price change (year over year, %) by geography, Q1 2026 and Q2 2026.
# Source: Lilly Q1 2026 earnings release (worldwide -13%, US -7%, ex-US -25%)
# and Q2 2026 earnings release (worldwide -13%, US -3% reported, ex-US -36%).
# The Q2 US figure is flattered by favorable rebate/discount estimate
# adjustments; excluding them, Lilly says US price fell ~9% (CFO confirmed).
geographies = ["Worldwide", "United States", "Outside the US"]
q1 = [-13, -7, -25]
q2_reported = [-13, -3, -36]

fig = go.Figure()
fig.add_trace(go.Bar(name="Q1 2026", x=geographies, y=q1))
fig.add_trace(go.Bar(name="Q2 2026 (reported)", x=geographies, y=q2_reported))

# The US Q2 reported -3% understates the underlying decline; mark the ~-9%.
fig.add_annotation(
    x="United States",
    y=-9,
    ax=0,
    ay=-38,
    text="Underlying −9%<br>(ex. rebate/discount adjustments)",
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
    arrowwidth=1.2,
    font=dict(size=13),
    align="center",
)
fig.add_trace(
    go.Scatter(
        name="Q2 2026 US, underlying",
        x=["United States"],
        y=[-9],
        mode="markers",
        marker=dict(symbol="diamond", size=12),
    )
)

fig.update_layout(
    barmode="group",
    yaxis_title="Realized-price change, YoY (%)",
    xaxis_title=None,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
)
fig.update_yaxes(zeroline=True, ticksuffix="%")
