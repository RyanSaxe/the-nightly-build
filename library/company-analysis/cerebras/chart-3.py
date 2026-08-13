import plotly.graph_objects as go

# Cerebras gross margin, GAAP vs. the company's own non-GAAP "core" measure,
# by quarter. Core excludes stock-based compensation and non-core
# pass-through items and adds back customer-warrant amortization.
# Sources: Cerebras Q2 2026 earnings release (investors.cerebras.ai) for
# Q2 2025 and Q2 2026 GAAP and core gross margin; Cerebras Q1 2026 earnings
# release for Q1 2026 core gross margin; Cerebras 10-Q for the quarter ended
# March 31, 2026 for Q1 2026 GAAP gross margin.
quarters = ["Q2 2025", "Q1 2026", "Q2 2026"]
gaap = [31.1, 44.6, 14.2]
core = [31.2, 47, 41]

fig = go.Figure()
fig.add_trace(go.Scatter(name="GAAP", x=quarters, y=gaap, mode="lines+markers"))
fig.add_trace(go.Scatter(name="Core (non-GAAP)", x=quarters, y=core, mode="lines+markers"))
fig.update_layout(
    yaxis_title="Gross margin (%)",
    xaxis_title="Fiscal quarter",
)
fig.update_yaxes(rangemode="tozero")
