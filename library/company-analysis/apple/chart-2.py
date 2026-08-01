"""Q3 fiscal-2026 net sales by product/service category, vs. Q3 fiscal-2025.

Quarter ended June 27, 2026 vs. quarter ended June 28, 2025. Dollar figures
($B) are Apple's own reported net sales by category, not YoY percentages
alone, so category size and category growth are both visible at once.

Data ($M, Q3 FY2025 -> Q3 FY2026):
  iPhone:                      44,582 -> 54,252  (+21.7%)
  Mac:                          8,046 -> 10,352  (+28.7%)
  iPad:                         6,581 ->  6,191  (-5.9%)
  Wearables, Home & Accessories 7,404 ->  7,883  (+6.5%)
  Services:                    27,423 -> 30,739  (+12.1%)

Source: Apple Inc., Form 8-K Exhibit 99.1, "Apple reports third quarter
results" (quarter ended June 27, 2026), filed with SEC EDGAR 2026-07-30,
accession 0000320193-26-000018, "Net sales by category" table.
"""

import plotly.graph_objects as go

categories = ["iPhone", "Mac", "iPad", "Wearables,\nHome & Accessories", "Services"]
fy25 = [44.582, 8.046, 6.581, 7.404, 27.423]
fy26 = [54.252, 10.352, 6.191, 7.883, 30.739]

fig = go.Figure()
fig.add_trace(go.Bar(name="Q3 FY2025", x=categories, y=fy25))
fig.add_trace(go.Bar(name="Q3 FY2026", x=categories, y=fy26))
fig.update_layout(
    barmode="group",
    yaxis_title="Net sales ($B)",
    xaxis_title="Category",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)
