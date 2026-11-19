"""Fig. 1: debt beside off-balance-sheet obligations, seven firms, 2020 to 2026:Q2.

Source: Federal Reserve Board, Financial Stability Report, November 2026,
Box 2.2, figure C "Debt and other obligations" (p. 24). The Fed has published
no data table for this report; every value below was read from the vector
geometry of the published chart (precision about +/- $5 billion), not taken
from a Fed table. Firms: Alphabet, Amazon, Broadcom, Meta Platforms,
Microsoft, Nvidia, Oracle. Debt is discounted; the two commitment series are
undiscounted (FSR p. 24, footnote 5), so the bars are not like for like.
"""

import plotly.graph_objects as go

periods = ["2020", "2021", "2022", "2023", "2024", "2025", "2026:Q2"]
debt = [346, 393, 447, 517, 502, 663, 879]
leases_yet_to_start = [47, 55, 58, 93, 231, 534, 1019]
guarantees_and_contract_commitments = [80, 138, 173, 217, 306, 637, 2068]

off_total = [a + b for a, b in zip(leases_yet_to_start, guarantees_and_contract_commitments)]

# Numeric positions so the on- and off-balance-sheet bars sit side by side
# for each period, with the two commitment series stacked.
pos = list(range(len(periods)))
left = [p - 0.21 for p in pos]
right = [p + 0.21 for p in pos]
width = 0.38

fig = go.Figure()
fig.add_trace(go.Bar(name="Debt (on balance sheet)", x=left, y=debt, width=width))
fig.add_trace(go.Bar(name="Leases yet to start", x=right, y=leases_yet_to_start, width=width))
fig.add_trace(
    go.Bar(
        name="Guarantees & contract commitments",
        x=right,
        y=guarantees_and_contract_commitments,
        base=leases_yet_to_start,
        width=width,
    )
)
fig.update_traces(marker_line_color="#ffffff", marker_line_width=2)

for x, y, text, xshift in [
    (right[-1], off_total[-1], "$3,087bn", -20),
]:
    fig.add_annotation(
        x=x, y=y, text=text, showarrow=False, xshift=xshift, yshift=22, font={"size": 30}
    )

fig.add_annotation(
    x=left[-1], y=debt[-1], ax=left[-1] + 0.19, ay=1450, axref="x", ayref="y",
    text="$879bn", xanchor="right", showarrow=True, arrowhead=0, arrowwidth=2,
    arrowcolor="#68727f", font={"size": 30},
)

fig.update_layout(
    barmode="overlay",
    font={"size": 30},
    legend={"font": {"size": 28}, "orientation": "v", "y": 0.97, "yanchor": "top", "x": 0.03, "xanchor": "left", "traceorder": "normal", "bgcolor": "rgba(255,255,255,0.9)"},
    margin={"t": 60, "r": 30, "b": 70, "l": 150},
    yaxis={
        "title": {"text": "US$ billions", "font": {"size": 28}, "standoff": 18},
        "tickfont": {"size": 28},
        "range": [0, 3400],
        "dtick": 500,
        "tickformat": ",",
    },
    xaxis={
        "tickmode": "array",
        "tickvals": pos,
        "ticktext": periods,
        "tickfont": {"size": 28},
        "range": [-0.6, len(periods) - 0.4],
    },
)
