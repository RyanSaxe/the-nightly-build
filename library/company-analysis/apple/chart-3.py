"""Gross margin by segment, Q3 FY2025 vs. Q3 FY2026, with the tariff-refund
component marked on the blended figure.

Products and Services carry structurally different margins; the blended
company margin depends on both the segment margins and the revenue mix
between them. The dashed marker on the Q3 FY2026 blended bar shows
Apple's own approximation of the blended margin with the tariff-refund
benefit removed.

Data (gross margin %, Q3 FY2025 -> Q3 FY2026):
  Products margin:  34.5% -> 40.1%
  Services margin:  75.6% -> 75.6%  (flat)
  Blended margin:   46.5% -> 50.1%

Apple's own approximation: the blended Q3 FY2026 margin of 50.1% includes
"a favorable impact of approximately 2 percentage points from tariff
refunds," implying a margin near 48.1% without that one-time item.

Sources: Apple Inc., Form 10-Q for the quarter ended June 27, 2026, filed
with SEC EDGAR 2026-07-31, accession 0000320193-26-000020 (Products/Services
gross-margin table, MD&A "Gross Margin" section) and Form 8-K Exhibit 99.1,
"Apple reports third quarter results," filed 2026-07-30, accession
0000320193-26-000018 (tariff-refund quantification, opening paragraph).
"""

import plotly.graph_objects as go

categories = ["Products margin", "Services margin", "Blended margin"]
fy25 = [34.5, 75.6, 46.5]
fy26 = [40.1, 75.6, 50.1]

fig = go.Figure()
fig.add_trace(go.Bar(name="Q3 FY2025", x=categories, y=fy25))
fig.add_trace(go.Bar(name="Q3 FY2026", x=categories, y=fy26))

fig.add_trace(
    go.Scatter(
        name="Q3 FY2026 blended, ex. tariff refund (Apple's approx.)",
        x=["Blended margin"],
        y=[48.1],
        mode="markers",
        marker=dict(symbol="diamond", size=14, color="#c0392b"),
    )
)

fig.update_layout(
    barmode="group",
    yaxis_title="Gross margin (%)",
    yaxis=dict(range=[0, 85]),
    xaxis_title="Segment",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
)
