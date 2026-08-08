import plotly.graph_objects as go

# U.S. segment revenue by quarter, in US$ millions, each figure from the
# Palantir earnings release that owns that quarter (press-release roundings):
#   Q2 2025 release, Q3 2025 release, Q4/FY2025 release, Q1 2026 release,
#   Q2 2026 release. See the article's Sources list.
quarters = ["Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
us_commercial = [306, 397, 507, 595, 764]
us_government = [426, 486, 570, 687, 809]

fig = go.Figure()
fig.add_trace(
    go.Scatter(name="U.S. commercial", x=quarters, y=us_commercial, mode="lines+markers")
)
fig.add_trace(
    go.Scatter(name="U.S. government", x=quarters, y=us_government, mode="lines+markers")
)
fig.update_layout(yaxis_title="Revenue (US$ millions)", xaxis_title="Fiscal quarter")
fig.update_yaxes(rangemode="tozero")
