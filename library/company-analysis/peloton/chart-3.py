import plotly.graph_objects as go

# Paid connected-fitness subscribers (ending, millions) against fourth-quarter
# average net monthly connected-fitness churn (%). FY2026 and FY2025 from the
# FY2026 SEC-filed earnings release (Exhibit 99.1); FY2024 from the FY2024
# SEC-filed shareholder letter. Q4 is seasonally the highest-churn quarter,
# so the churn points compare like quarter with like quarter.
years = ["FY2024", "FY2025", "FY2026"]
subscribers = [2.98, 2.80, 2.553]
churn = [1.9, 1.8, 2.2]

fig = go.Figure()
fig.add_trace(
    go.Bar(name="Ending paid subscribers", x=years, y=subscribers, yaxis="y")
)
fig.add_trace(
    go.Scatter(name="Q4 monthly churn", x=years, y=churn, yaxis="y2", mode="lines+markers")
)
fig.update_layout(
    yaxis=dict(title="Paid connected-fitness subscribers (millions)", rangemode="tozero"),
    yaxis2=dict(
        title="Q4 avg. net monthly churn (%)",
        overlaying="y",
        side="right",
        rangemode="tozero",
    ),
    xaxis_title="Fiscal year ended June 30",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
