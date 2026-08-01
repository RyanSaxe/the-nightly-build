"""Services net sales, year-over-year growth by fiscal quarter.

Seven quarters ended June 27, 2026. Each YoY figure is computed from the
current quarter's Services net sales against the same quarter one year
earlier, both taken from Apple's own SEC filings (8-K exhibits and 10-Qs).

Data (Services net sales, $M -- current-quarter figure / prior-year base):
  Q1 FY2025 (qtr end 2024-12-28): $26,340M vs $23,117M (Q1 FY2024) -> +13.9%
  Q2 FY2025 (qtr end 2025-03-29): $26,645M vs $23,867M (Q2 FY2024) -> +11.6%
  Q3 FY2025 (qtr end 2025-06-28): $27,423M vs $24,213M (Q3 FY2024) -> +13.3%
  Q4 FY2025 (qtr end 2025-09-27): $28,750M vs $24,972M (Q4 FY2024) -> +15.1%
  Q1 FY2026 (qtr end 2025-12-27): $30,013M vs $26,340M (Q1 FY2025) -> +13.9%
  Q2 FY2026 (qtr end 2026-03-28): $30,976M vs $26,645M (Q2 FY2025) -> +16.3%
  Q3 FY2026 (qtr end 2026-06-27): $30,739M vs $27,423M (Q3 FY2025) -> +12.1%

Sources: Apple Inc. 8-K Exhibit 99.1 filings (accessions 0000320193-26-000018,
0000320193-25-000077, 0000320193-24-000080, 0000320193-24-000067,
0000320193-24-000005) and 10-Q filings (accessions 0000320193-26-000020,
0000320193-26-000013, 0000320193-26-000006), all filed with SEC EDGAR,
CIK 0000320193.
"""

import plotly.graph_objects as go

quarters = [
    "Q1 FY25",
    "Q2 FY25",
    "Q3 FY25",
    "Q4 FY25",
    "Q1 FY26",
    "Q2 FY26",
    "Q3 FY26",
]
yoy_growth = [13.9, 11.6, 13.3, 15.1, 13.9, 16.3, 12.1]

colors = ["#7a8699"] * 6 + ["#c0392b"]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=quarters,
        y=yoy_growth,
        marker_color=colors,
        text=[f"{v:.1f}%" for v in yoy_growth],
        textposition="outside",
        cliponaxis=False,
    )
)
fig.update_layout(
    yaxis_title="Services net sales, YoY growth (%)",
    yaxis=dict(range=[0, 19]),
    xaxis_title="Fiscal quarter",
)
