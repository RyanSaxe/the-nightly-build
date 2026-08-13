import plotly.graph_objects as go

# Cerebras GAAP revenue by category, Q2 2025 vs Q2 2026, US$ millions.
# Source: Cerebras Form 10-Q for the quarter ended June 30, 2026, Note 3
# (Revenue). Hardware fell 23% year over year; Cloud and other services
# rose 281% year over year.
quarters = ["Q2 2025", "Q2 2026"]
hardware = [70.3, 54.1]
cloud = [33.0, 126.0]

fig = go.Figure()
fig.add_trace(go.Bar(name="Hardware", x=quarters, y=hardware))
fig.add_trace(go.Bar(name="Cloud and other services", x=quarters, y=cloud))
fig.update_layout(
    barmode="group",
    yaxis_title="Revenue (US$ millions)",
    xaxis_title="Fiscal quarter",
)
fig.update_yaxes(rangemode="tozero")
