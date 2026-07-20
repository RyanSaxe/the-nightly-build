import plotly.graph_objects as go

# Alphabet capital expenditures (purchases of property and equipment).
# 2023-2025 are filed figures from the FY2025 Form 10-K cash-flow statement.
# 2026e is the midpoint of management's $180-190bn guidance given on the
# Apr 29 2026 earnings call (reported by CNBC); it is guidance, not a filing.
years = ["2023", "2024", "2025", "2026e"]
capex = [32.3, 52.5, 91.4, 185.0]
labels = ["$32.3bn", "$52.5bn", "$91.4bn", "~$185bn"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Capital expenditures",
        x=years,
        y=capex,
        text=labels,
        textposition="outside",
    )
)
fig.update_layout(
    yaxis_title="Capital expenditures, US$ billions",
    xaxis_title=None,
    showlegend=False,
)
fig.update_yaxes(range=[0, 210])
fig.update_xaxes(type="category")
