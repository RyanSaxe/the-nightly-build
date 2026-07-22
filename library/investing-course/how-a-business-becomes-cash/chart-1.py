"""Net income to operating cash flow bridge, Costco fiscal 2025.

Every value is a line of the operating-activities section of Costco's
Consolidated Statements of Cash Flows, fiscal year ended August 31, 2025
(Form 10-K, accession 0000909832-25-000101), in US$ millions. The bar heights
sum from net income ($8,099M) to net cash provided by operating activities
($13,335M):

    8,099 + 2,426 + 303 + 860 - 117 + 559 + 404 + 801 = 13,335

The "Other non-cash, net" step (impairment of assets and other non-cash
operating activities, net) is negative in this year, a reminder that non-cash
items are reversed, not always added.
"""

import plotly.graph_objects as go

labels = [
    "Net income",
    "Depreciation<br>& amortization",
    "Non-cash<br>lease expense",
    "Stock-based<br>compensation",
    "Other non-cash,<br>net",
    "Merchandise<br>inventories",
    "Accounts<br>payable",
    "Other operating<br>items, net",
    "Operating<br>cash flow",
]
values = [8099, 2426, 303, 860, -117, 559, 404, 801, 13335]
measure = [
    "absolute",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "total",
]
text = [f"{v:+,}" if m == "relative" else f"{v:,}" for v, m in zip(values, measure)]

fig = go.Figure(
    go.Waterfall(
        orientation="v",
        measure=measure,
        x=labels,
        y=values,
        text=text,
        textposition="outside",
        connector={"line": {"width": 1}},
    )
)
fig.update_layout(
    yaxis_title="US$ millions",
    showlegend=False,
    margin={"t": 10},
)
fig.update_yaxes(range=[0, 15200])
