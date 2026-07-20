import plotly.graph_objects as go

# Google Cloud: revenue and implied operating margin.
# FY2024 and FY2025 are from the FY2025 Form 10-K; Q1 2026 is the single
# quarter ended Mar 31 2026 from the Q1-2026 earnings release. Margin is
# segment operating income divided by segment revenue.
periods = ["FY2024", "FY2025", "Q1 2026"]
revenue = [43.2, 58.7, 20.0]
margin = [14.1, 23.7, 32.9]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Cloud revenue (US$ bn)",
        x=periods,
        y=revenue,
        yaxis="y",
    )
)
fig.add_trace(
    go.Scatter(
        name="Operating margin (%)",
        x=periods,
        y=margin,
        yaxis="y2",
        mode="lines+markers+text",
        text=["14.1%", "23.7%", "32.9%"],
        textposition="top center",
    )
)
fig.update_layout(
    yaxis=dict(title="Revenue, US$ billions", range=[0, 70]),
    yaxis2=dict(
        title="Operating margin, %",
        overlaying="y",
        side="right",
        range=[0, 40],
    ),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
)
