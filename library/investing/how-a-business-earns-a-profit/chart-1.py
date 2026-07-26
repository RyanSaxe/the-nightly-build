"""Costco's operating income split by source, fiscal 2023 through fiscal 2025.

Every input is a line from Costco's Consolidated Statements of Income, Form
10-K (FY2025, accession 0000909832-25-000101), in US$ millions:

    Net sales:          237,710 (FY23)  249,625 (FY24)  269,912 (FY25)
    Merchandise costs:  212,586 (FY23)  222,358 (FY24)  239,886 (FY25)
    SG&A:                21,590 (FY23)   22,810 (FY24)   24,966 (FY25)
    Membership fees:      4,580 (FY23)    4,828 (FY24)    5,323 (FY25)
    Operating income:     8,114 (FY23)    9,285 (FY24)   10,383 (FY25)

"Operating profit from merchandise" is derived, not a reported line: net
sales minus merchandise costs minus SG&A. Adding membership fees back
reproduces Costco's reported operating income exactly in all three years,
which is the check that the split is real rather than illustrative:

    FY23: (237,710 - 212,586 - 21,590) + 4,580 = 3,534 + 4,580 = 8,114
    FY24: (249,625 - 222,358 - 22,810) + 4,828 = 4,457 + 4,828 = 9,285
    FY25: (269,912 - 239,886 - 24,966) + 5,323 = 5,060 + 5,323 = 10,383
"""

import plotly.graph_objects as go

years = ["FY2023", "FY2024", "FY2025"]
merch_operating_profit = [3534, 4457, 5060]
membership_fees = [4580, 4828, 5323]
totals = [a + b for a, b in zip(merch_operating_profit, membership_fees)]

fig = go.Figure()
fig.add_trace(
    go.Bar(
        name="Operating profit from merchandise",
        x=years,
        y=merch_operating_profit,
        text=[f"{v:,}" for v in merch_operating_profit],
        textposition="inside",
    )
)
fig.add_trace(
    go.Bar(
        name="Membership fees",
        x=years,
        y=membership_fees,
        text=[f"{v:,}" for v in membership_fees],
        textposition="inside",
    )
)
for x, total in zip(years, totals):
    fig.add_annotation(
        x=x,
        y=total,
        text=f"{total:,}",
        showarrow=False,
        yshift=16,
        font={"size": 14},
    )
fig.update_layout(
    barmode="stack",
    yaxis_title="US$ millions",
    legend={"orientation": "h", "y": 1.12, "x": 0},
    margin={"t": 40},
)
fig.update_yaxes(range=[0, 11800])
