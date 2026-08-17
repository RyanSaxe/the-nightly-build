import plotly.graph_objects as go

# Peloton revenue by stream, fiscal years ended June 30 (US$ millions).
# FY2026 and FY2025 from the FY2026 SEC-filed earnings release (Exhibit 99.1);
# FY2024 and FY2023 from the FY2024 SEC-filed shareholder letter.
years = ["FY2023", "FY2024", "FY2025", "FY2026"]
connected_fitness = [1130.2, 991.7, 817.1, 770.4]
subscription = [1670.1, 1708.7, 1673.7, 1675.6]

fig = go.Figure()
fig.add_trace(go.Bar(name="Connected-fitness hardware", x=years, y=connected_fitness))
fig.add_trace(go.Bar(name="Subscription", x=years, y=subscription))
fig.update_layout(
    barmode="group",
    yaxis_title="Revenue (US$ millions)",
    xaxis_title="Fiscal year ended June 30",
)
