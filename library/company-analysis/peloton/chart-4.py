import plotly.graph_objects as go

# From FY2026 GAAP net income to free cash flow. Figures from Peloton's FY2026
# SEC-filed earnings release (Exhibit 99.1), cash-flow statement and the
# free-cash-flow non-GAAP reconciliation. US$ millions. "Other, net" folds the
# remaining working-capital and reconciling items; operating cash flow was
# $387.6M and capital expenditure $9.9M, giving free cash flow of $377.6M.
labels = [
    "Net income",
    "Stock-based<br>compensation",
    "Depreciation &<br>amortization",
    "Impairment",
    "Inventory<br>drawdown",
    "Other, net",
    "Capital<br>expenditure",
    "Free cash<br>flow",
]
measures = [
    "absolute",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "relative",
    "total",
]
values = [63.2, 198.6, 57.2, 34.6, 81.3, -47.4, -9.9, 377.6]
text = ["63.2", "+198.6", "+57.2", "+34.6", "+81.3", "-47.4", "-9.9", "377.6"]

fig = go.Figure(
    go.Waterfall(
        measure=measures,
        x=labels,
        y=values,
        text=text,
        textposition="outside",
        connector={"line": {"color": "rgba(120,120,120,0.5)"}},
    )
)
fig.update_layout(
    yaxis_title="US$ millions",
    showlegend=False,
)
