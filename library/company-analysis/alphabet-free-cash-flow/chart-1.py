# Chart 1: Alphabet's operating cash flow, capital expenditures, and the
# resulting free cash flow, by quarter, Q1 2025 through Q2 2026. Figures are
# Alphabet's own consolidated statements of cash flows and earnings releases,
# tied out across the Q1 2026 10-Q, the Q2 2026 10-Q, and the Q2/Q3/Q4 2025
# earnings releases (all filed with the SEC). Free cash flow is each
# quarter's operating cash flow minus capex; Q2 2026 uses the unrounded 10-Q
# figures (operating cash flow $39.069B, capex $44.924B) so the plotted point
# ties out exactly to -$5.855B (rounds to -$5.9B). Dollars in US$ billions.
import plotly.graph_objects as go

quarters = ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]
operating_cash_flow = [36.2, 27.7, 48.4, 52.4, 45.8, 39.069]
capex = [17.2, 22.4, 24.0, 27.9, 35.7, 44.924]
free_cash_flow = [19.0, 5.3, 24.4, 24.5, 10.1, -5.855]

fig = go.Figure()
fig.add_trace(
    go.Scatter(name="Operating cash flow", x=quarters, y=operating_cash_flow, mode="lines+markers")
)
fig.add_trace(
    go.Scatter(name="Capital expenditures", x=quarters, y=capex, mode="lines+markers")
)
fig.add_trace(
    go.Scatter(name="Free cash flow", x=quarters, y=free_cash_flow, mode="lines+markers")
)
fig.add_hline(y=0, line_width=1, line_dash="dot")

fig.update_layout(
    yaxis_title="US$ billions",
    xaxis_title="Fiscal quarter",
    legend_title_text="",
)
