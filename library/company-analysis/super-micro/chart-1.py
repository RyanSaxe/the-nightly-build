from decimal import ROUND_HALF_UP, Decimal

import plotly.graph_objects as go

# Quarterly GAAP gross margin, computed as gross profit / net sales from the
# income-statement lines in each period's primary filing: SEC Forms 10-Q
# (Q1-Q3 of each fiscal year) and the Q4 FY2026 8-K Exhibit 99.1. Source and
# per-quarter dollar figures are in researcher/01/evidence.md, "Numbers"
# section, "Quarterly gross margin series, FY2025-FY2026".
#
# Net sales and gross profit are carried in whole thousands of dollars, as
# filed, so the displayed percentage is computed here from the same exact
# figures the prose cites rather than from a pre-rounded intermediate value.
# (Rounding an already-rounded 2-decimal percentage to 1 decimal can flip the
# last digit versus rounding the precise fraction directly -- e.g. the
# 2-decimal figure 9.95 rounds up to 10.0, while the precise fraction it came
# from, 9.9451%, rounds to 9.9. Decimal arithmetic on the filed dollar
# figures avoids both that double-rounding error and binary-float imprecision
# such as 9.45 displaying as 9.4.)
quarters = [
    "Q1 FY25",
    "Q2 FY25",
    "Q3 FY25",
    "Q4 FY25",
    "Q1 FY26",
    "Q2 FY26",
    "Q3 FY26",
    "Q4 FY26",
]
net_sales = [5937256, 5677962, 4599913, 5756911, 5017790, 12682491, 10243014, 11119777]
gross_profit = [775580, 670022, 440218, 544102, 467373, 798567, 1018680, 1942631]

margin_exact = [
    Decimal(gp) / Decimal(ns) * 100 for gp, ns in zip(gross_profit, net_sales)
]
margin = [float(m) for m in margin_exact]
labels = [
    f"{m.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)}%" for m in margin_exact
]

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        name="GAAP gross margin",
        x=quarters,
        y=margin,
        mode="lines+markers+text",
        text=labels,
        textposition="top center",
    )
)
fig.update_layout(
    yaxis_title="Gross margin (%)",
    yaxis_range=[0, 20],
    xaxis_title="Fiscal quarter",
)
