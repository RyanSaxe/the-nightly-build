import plotly.graph_objects as go

# Quarter-end inventory and accounts receivable, five balance-sheet dates.
# Jun 30, 2025 is from the audited FY2025 10-K (corroborated by the 8-K
# Exhibit 99.1 comparative column); the other four dates are from SMCI's own
# Forms 10-Q and the Q4 FY2026 8-K Exhibit 99.1. See researcher/01/
# evidence.md, "Numbers" section, "Quarter-end inventory and accounts-
# receivable series, FY2025 Q4 through FY2026 Q4".
dates = ["Jun 30, 2025", "Sep 30, 2025", "Dec 31, 2025", "Mar 31, 2026", "Jun 30, 2026"]
inventory = [4680.375, 5730.002, 10595.448, 11103.376, 12895.949]
receivables = [2203.942, 2525.039, 11004.122, 8413.396, 6125.414]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="Inventory",
        x=dates,
        y=inventory,
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        name="Accounts receivable, net",
        x=dates,
        y=receivables,
        mode="lines+markers",
    )
)
fig.update_layout(
    yaxis_title="US$ millions",
    xaxis_title="Balance-sheet date",
)
