"""Boeing H1 2026 cash bridge: net loss to free cash flow.

All figures in US$ millions, six months ended June 30, 2026, from Boeing's
Q2 2026 Form 10-Q (Condensed Consolidated Statements of Cash Flows) and the
matching earnings press release (capital expenditures, free cash flow).

Primary sources:
- 10-Q: https://www.sec.gov/Archives/edgar/data/12927/000162828026050038/ba-20260630.htm
    Net loss (total):                       (435)
    Advances and progress billings:        +4,660
    Inventories:                           (3,859)
    Net cash from operating activities:    +1,185   (subtotal)
    Property, plant and equipment additions (capex): (2,008)
- Release: https://www.sec.gov/Archives/edgar/data/12927/000162828026049929/a202606jun308kprex991.htm
    Free cash flow:                          (823)  (= 1,185 - 2,008)

"All other operating" (+819) is the identity plug that reconciles the three
named working-capital lines and the net loss to reported operating cash flow:
1,185 - (-435) - 4,660 - (-3,859) = 819. It bundles accounts payable (+1,381),
accounts receivable (-553), depreciation/amortization, pension/OPEB, share-based
compensation, taxes, and other working-capital movements.
"""

import plotly.graph_objects as go

labels = [
    "Net loss",
    "Customer advances",
    "Inventory build",
    "All other operating",
    "Operating cash flow",
    "Capital spending",
    "Free cash flow",
]
measures = ["relative", "relative", "relative", "relative", "total", "relative", "total"]
values = [-435, 4660, -3859, 819, 1185, -2008, -823]

fig = go.Figure(
    go.Waterfall(
        orientation="v",
        measure=measures,
        x=labels,
        y=values,
        text=[f"{v:+,}" if m == "relative" else f"{v:,}" for v, m in zip(values, measures)],
        textposition="outside",
        connector={"line": {"width": 1}},
        decreasing={"marker": {"color": "#b3402a"}},
        increasing={"marker": {"color": "#2f6f4f"}},
        totals={"marker": {"color": "#26456e"}},
    )
)
fig.update_layout(
    yaxis_title="US$ millions",
    showlegend=False,
    margin=dict(t=20),
)
fig.update_xaxes(tickangle=-30)
