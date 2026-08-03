import plotly.graph_objects as go

# Total revenue ($M) and YoY growth (%), Reddit quarterly press releases.
quarters = ["Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"]
revenue = [499.6, 584.9, 726.0, 663.0, 804.9]
yoy = [78, 68, 70, 69, 61]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Total revenue ($M)",
        x=quarters,
        y=revenue,
        text=[f"${v:.0f}M" for v in revenue],
        textposition="outside",
        yaxis="y",
    )
)
fig.add_trace(
    go.Scatter(
        name="Revenue YoY growth (%)",
        x=quarters,
        y=yoy,
        mode="lines+markers+text",
        text=[f"{v}%" for v in yoy],
        textposition="bottom center",
        yaxis="y2",
    )
)

fig.update_layout(
    yaxis=dict(title="Total revenue ($M)", range=[0, 950]),
    yaxis2=dict(
        title="YoY growth (%)",
        overlaying="y",
        side="right",
        range=[0, 100],
        showgrid=False,
    ),
    xaxis_title="Fiscal quarter",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
