import plotly.graph_objects as go

# US DAUq (daily active uniques, millions), Reddit quarterly press releases.
quarters = ["Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"]
us_dauq = [50.3, 51.6, 52.5, 53.5, 53.2]

# Zacks US-DAUq consensus for Q2'26 (secondary; the bar the print was measured against).
consensus_q = ["Q2'26"]
consensus_v = [53.98]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="US DAUq (reported)",
        x=quarters,
        y=us_dauq,
        mode="lines+markers+text",
        text=[f"{v:.1f}" for v in us_dauq],
        textposition="bottom center",
    )
)
fig.add_trace(
    go.Scatter(
        name="Q2'26 consensus (Zacks)",
        x=consensus_q,
        y=consensus_v,
        mode="markers+text",
        text=["53.98"],
        textposition="top center",
    )
)

fig.add_annotation(
    x="Q2'26",
    y=53.2,
    ax="Q1'26",
    ay=53.5,
    xref="x",
    yref="y",
    axref="x",
    ayref="y",
    showarrow=True,
    arrowhead=2,
    arrowwidth=1.5,
    text="",
)
fig.add_annotation(
    x=3.5,
    y=53.35,
    xref="x",
    yref="y",
    showarrow=False,
    text="first sequential<br>decline in the series",
    font=dict(size=13),
)

fig.update_layout(
    yaxis_title="US DAUq (millions)",
    xaxis_title="Fiscal quarter",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
fig.update_yaxes(range=[49, 55])
