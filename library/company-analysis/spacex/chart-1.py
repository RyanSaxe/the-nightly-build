import plotly.graph_objects as go

# SpaceX Q2 2026 (three months ended June 30, 2026), US$ millions.
# Source: SpaceX Q2 2026 earnings release (EX-99.1 to the 8-K).
segments = ["Space", "Connectivity", "AI"]
revenue = [962, 4291, 2561]
capex = [1174, 1367, 15828]

fig = go.Figure()
fig.add_trace(go.Bar(name="Revenue", x=segments, y=revenue))
fig.add_trace(go.Bar(name="Capital expenditure", x=segments, y=capex))
fig.update_layout(
    barmode="group",
    yaxis_title="US$ millions, Q2 2026",
    xaxis_title="Reported segment",
)
